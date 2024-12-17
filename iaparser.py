import csv
import json
entries = []
with open('responses.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        [timestamp, email, submission, studio, attendance, contact, bookingEmail, split, discord, unique, runtime, light, sound, tourney, url, images, thumbnail, header, description, tweet, location] = row
        if attendance == "Yep! See you there!":
            entries.append({
                "submission": submission,
                "studio": studio,
                "url": url,
                "images": images,
                "thumbnail": thumbnail,
                "header": header,
                "description": description
            })

with open('result.json', 'w') as output:
    output.write(json.dumps(entries))