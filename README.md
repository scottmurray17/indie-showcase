# indie-showcase
## iaparser.py
This python script takes the google form responses downloaded as `responses.csv` (saved in the same directory) and turns it into a slightly more usable `result.json`. There are fields in `result.json` we likely do not need, and the images need to be saved elsewhere statically so we can reference them in the actual html, but it is at least a good starting point to get to a json file we can use for the site.

I have not included the csv or json files in this repo to keep out any info we would otherwise not include on the website.

## showcase.html
Ideally, we can copy the entire `showcase.html` file into the website and it *should* work as intended, though I'm not sure as I have been unable to test the script being loaded alongside the page. Not all the images are working current state due to CORS but this would be resolved once we statically host the files ourselves, either on the site itself or on imgur.

The styles were created to function if this code was pasted into the existing Indie Arcade 2024 Showcase page, so if the styles are going to change on the new site we will need to either include our own styles in the script or adopt the styles that exist on the new page. Shouldn't be too terrible

Inside `showcase.html` is a variable called `games`. This is a sanitized version of `result.json`, however shortened for testing purposes. It will need to be updated to the full list when we're ready to launch.

## screenshot.png
This is a screenshot of what the code looks like when pasted into the Indie Showcase 2024 page (with a bit of messing around in the dev terminal to get scripts to work). I believe there are only a few differences between this script and the original squarespace rendering:
1. The horizontal lines aren't the right color, that's because I was lazy
2. The padding around the games list is a bit less, so they take up a bit more of the screen. This felt negligible to me since it will depend on where and how the script is pasted into the page so we can address it when we can actually test it on the 2025 page.
3. When the description of the game was longer than the height of the image, it would wrap back to the leftmost point of the section (underneath the image), where my script would keep all text to the right of the image. At the current moment I don't think any of the descriptions are long enough to trigger that kind of behavior but it is something I can look to fix if we deem it necessary.

## closing thoughts
1. Some survey responses included more than one url, often to a game page and/or 1+ social media account(s). We could add more space for those.
2. It might be nice to include some alt text for images / other a11y features that I have not really thought about