import requests

# ---------------------------
# UNSPLASH API
# ---------------------------
UNSPLASH_ACCESS_KEY = "YOUR_UNSPLASH_ACCESS_KEY"

def get_unsplash_trending():
    print("Sending request to Unsplash...")
    url = "https://api.unsplash.com/photos"
    params = {"order_by": "popular", "per_page": 10}
    headers = {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}
    response = requests.get(url, headers=headers, params=params)
    print("Response received:", response.status_code)

    trending_keywords = []
    if response.status_code == 200:
        data = response.json()
        for photo in data:
            # Try tags first
            tags = [t['title'] for t in photo.get("tags", [])]
            if tags:
                trending_keywords.extend(tags)
            # Fallbacks
            elif photo.get("alt_description"):
                trending_keywords.append(photo["alt_description"])
            elif photo.get("description"):
                trending_keywords.append(photo["description"])
        
        # Deduplicate and truncate
        unique_keywords = []
        seen = set()
        for term in trending_keywords:
            if term and term not in seen:
                truncated = term[:1000]  # truncate if over 1000 chars
                unique_keywords.append(truncated)
                seen.add(term)
        return unique_keywords
    else:
        print("Error:", response.status_code, response.text)
        return []

# ---------------------------
# SAVE RESULTS
# ---------------------------
def save_results_to_txt(terms, filename="trending_terms.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Visual Content Terms from Unsplash\n")
        f.write("=" * 50 + "\n\n")
        for rank, term in enumerate(terms, start=1):
            f.write(f"{rank}. {term}\n")
    print(f"📄 Results saved to {filename}")

# ---------------------------
# MAIN
# ---------------------------
if __name__ == "__main__":
    # 1. Pull Unsplash terms
    unsplash_terms = get_unsplash_trending()
    if not unsplash_terms:
        print("⚠️ No terms found from Unsplash, exiting.")
        exit()

    print("🔹 Unsplash trending terms:", unsplash_terms[:10])

    # 2. Save results to .txt
    save_results_to_txt(unsplash_terms)
