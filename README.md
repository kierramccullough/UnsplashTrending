This is a small script that will pull the alt description and tags of the top 10 photos on [Unsplash](https://unsplash.com/), in addition to downloading the images. This is a functional test to demostrate Unsplash API usage.

_Please note that [Unsplash does not permit data mining](https://help.unsplash.com/en/articles/2511256-guideline-high-quality-authentic-experiences). The information obtained by this script could be obtained much more easily by visiting the Unsplash homepage. I'm just making scripts that are fun to code and look good on a resume. Advice/ suggestions are welcome :)_

Requirements:
- Python (made with 3.13.7)
- Libraries "os" and "requests".
- Unsplash Dev account ([sign-up is quick, easy, and free](https://unsplash.com/developers)).
- Unsplash access key (project does not need to be in production, public access is fine).

Usage:
- Replace "YOUR_UNSPLASH_ACCESS_KEY" on line 7.
- Open trendsUnsplash.py via cmd.
- "unsplash_top10" folder will generate in the same directory, populated by the top 10 photos.
- "unsplash_top10_metadata.txt" will generate in the same directory, populated by photos' alt descriptions and tags.
