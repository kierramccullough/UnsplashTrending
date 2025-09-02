import os
import requests

# ---------------------------
# CONFIG
# ---------------------------
UNSPLASH_ACCESS_KEY = ""  # put your access key here
DOWNLOAD_DIR = "unsplash_top10"  # folder to save images
OUTPUT_FILE = "unsplash_top10_metadata.txt"
PER_PAGE = 10

# ---------------------------
# CREATE FOLDER
# ---------------------------
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

# ---------------------------
# GET TOP PHOTOS
# ---------------------------
def get_top_photos():
    url = "https://api.unsplash.com/photos"
    params = {
        "order_by": "popular",  # top photos of the day
        "per_page": PER_PAGE
    }
    headers = {
        "Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print("Error fetching photos:", response.status_code, response.text)
        return []
    return response.json()

# ---------------------------
# DOWNLOAD IMAGE VIA download_location
# ---------------------------
def download_photo(photo):
    photo_id = photo["id"]
    
    # First, get the full photo data to extract tags and alt text
    url_photo = f"https://api.unsplash.com/photos/{photo_id}"
    headers = {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}
    r_photo = requests.get(url_photo, headers=headers)
    if r_photo.status_code != 200:
        print(f"Error fetching full photo data for {photo_id}: {r_photo.status_code}")
        return None, None  # return both filename and full photo data

    full_photo = r_photo.json()

    # Download the actual image
    download_location = full_photo["links"]["download_location"]
    r_download = requests.get(download_location, headers=headers)
    if r_download.status_code != 200:
        print(f"Error getting download URL for {photo_id}: {r_download.status_code}")
        return None, full_photo

    download_url = r_download.json().get("url")
    if not download_url:
        print(f"No download URL found for {photo_id}")
        return None, full_photo

    img_data = requests.get(download_url).content
    filename = os.path.join(DOWNLOAD_DIR, f"{photo_id}.jpg")
    with open(filename, "wb") as f:
        f.write(img_data)
    print(f"Downloaded {photo_id} to {filename}")

    return filename, full_photo

# ---------------------------
# EXTRACT METADATA
# ---------------------------
def extract_metadata(photo, filename):
    # Tags
    tags_list = [tag.get("title") for tag in photo.get("tags", []) if tag.get("title")]
    tags_str = ", ".join(tags_list) if tags_list else "No tags"

    # Alt text
    alt_text = photo.get("alt_description", "") or ""

    return f"Image: {os.path.basename(filename)}\nTags: {tags_str}\nAlt Text: {alt_text}\n{'='*60}\n"


# ---------------------------
# MAIN
# ---------------------------
if __name__ == "__main__":
    photos = get_top_photos()
    if not photos:
        print("No photos retrieved. Exiting.")
        exit()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f_txt:
        for photo in photos:
            filename, full_photo = download_photo(photo)
            if filename and full_photo:
                # Extract tags
                tags_list = [tag.get("title") for tag in full_photo.get("tags", []) if tag.get("title")]
                tags_str = ", ".join(tags_list) if tags_list else "No tags"

                # Extract alt text
                alt_text = full_photo.get("alt_description", "") or ""

                # Write metadata
                f_txt.write(f"Image: {os.path.basename(filename)}\n")
                f_txt.write(f"Tags: {tags_str}\n")
                f_txt.write(f"Alt Text: {alt_text}\n")
                f_txt.write("="*60 + "\n")
