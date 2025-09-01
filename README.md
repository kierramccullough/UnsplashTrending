This is a small script that will pull the descriptions of the top 10 photos on [Unsplash](https://unsplash.com/), and export those descriptions to a .txt file. This is a functional test to demostrate Unsplash API usage.

_Please note that [Unsplash does not permit data mining](https://help.unsplash.com/en/articles/2511256-guideline-high-quality-authentic-experiences). The information obtained by this script could be obtained much more easily by visiting the Unsplash homepage. I'm just making scripts that are fun to code and look good on a resume. Advice/ suggestions are welcome :)_

Requirements:
- Python (made with 3.13.7)
- Libraries "request" and "pytrends".
- Unsplash Dev account ([sign-up is quick, easy, and free](https://unsplash.com/developers)).
- Unsplash access key (project does not need to be in production, public access is fine).

Usage:
- Replace "YOUR_UNSPLASH_ACCESS_KEY" on line 6.
- Open .py via cmd.
- "trending_terms".txt will generate in the same directory.
