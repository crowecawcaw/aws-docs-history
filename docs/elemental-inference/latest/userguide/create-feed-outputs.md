

# Configuring each feature
<a name="create-feed-outputs"></a>

Following are details about how to configure each feature (output) that you include in a Elemental Inference feed. 

## Configuring event clipping
<a name="create-feed-console-event-clip"></a>

In **Callback config**, you can enter a string that you want Elemental Inference to always include in the event clipping metadata for this output. This information is useful when you later work with Elemental Inference events in Amazon EventBridge. You will be able to filter events using this information, in order to find the events for one feed. The string might identify the sports event in the feed, for example.

### Aligning clips to plays with Sports Data
<a name="event-clip-sports-data"></a>

To use Sports Data, you find the game in the sports data feed and attach it to an event clipping output. Elemental Inference then aligns the clips for that output to the plays in the game.

**Note**  
You must have a feed on a running MediaLive channel that carries the game. You must search for the game and attach it from the same AWS account. You can attach one game to each event clipping output.

#### Supported sports and leagues
<a name="event-clip-sports-leagues"></a>

Sports Data supports the following sports and leagues.


| Sport | Leagues | 
| --- | --- | 
| Basketball | NBA, WNBA, NCAA Men's Basketball, NCAA Women's Basketball | 
| American football | NFL, NCAA Men's Football | 

For each sport, Elemental Inference aligns clips to the following events. The tag is the value that identifies the event in the game data.

##### Basketball events
<a name="event-clip-sports-leagues-basketball"></a>


| Event | Tag | 
| --- | --- | 
| Dunk | dunk | 
| Three-pointer | threepointer | 
| Two-pointer | twopointer | 

##### American football events
<a name="event-clip-sports-leagues-football"></a>


| Event | Tag | 
| --- | --- | 
| Touchdown | touchdown | 
| Punt return touchdown | puntreturntouchdown | 
| Kickoff return touchdown | kickoffreturntouchdown | 
| Interception | interception | 
| Fumble | fumble | 
| Pick six | picksix | 
| Strip sack | stripsack | 
| Turnover on downs | turnoverondowns | 

#### Step 1: Find your game
<a name="event-clip-find-game"></a>

Use the `SearchFixtures` operation to find the game that you want to align clips to. You provide a sport and a date range, and optionally filter by team. Each game in the response includes a `fixtureId` that you attach to your event clipping output in the next step.

The following example searches for basketball games on `2026-03-03` and `2026-03-04` that involve the Comets.

```
$ awscurl --service "elemental-inference" --region <{{region}}> \
  -X POST "https://elemental-inference.<{{region}}>.amazonaws.com/v1/fixtures" \
  -H "Content-Type: application/json" \
  -d '{
    "sport": "basketball",
    "startDate": "2026-03-03",
    "endDate": "2026-03-04",
    "filters": [{ "name": "COMPETITOR", "values": ["Comets"] }]
  }'
```

The response returns the matching games. Note the `fixtureId` of the game that you want to clip.

```
{
  "fixtures": [
    {
      "fixtureId": "NwrW5B17Rw9W25g1jPlobSGdQfBOKyD3227bcsRK0w3Bq7aG2xRrO8qx2XEjl6R1sOH2kwyjbojN4Rk7qHiF2w",
      "name": "Northport Comets vs. Southport Meteors",
      "fixtureGroup": "Regular Season",
      "scheduledStart": "2026-03-04T03:00:00Z",
      "status": "Scheduled",
      "competitors": [
        { "name": "Meteors", "isHome": true },
        { "name": "Comets", "isHome": false }
      ]
    }
  ]
}
```

**CLI example**

The following example makes the same request using the AWS CLI:

```
aws elemental-inference search-fixtures \
  --sport "basketball" \
  --start-date "2026-03-03" \
  --end-date "2026-03-04" \
  --filters '[{"name": "COMPETITOR", "values": ["Comets"]}]'
```

##### Request parameters
<a name="event-clip-request-params"></a>


| Parameter | Required | Description | 
| --- | --- | --- | 
| sport | Yes | Either basketball or american-football. | 
| startDate | Yes | The first day to search, in YYYY-MM-DD format (UTC). | 
| endDate | No | The last day to search, in YYYY-MM-DD format (UTC). Defaults to startDate. The window must be 7 days or fewer, inclusive. | 
| filters | No | Up to 10 filters, with up to 10 values each. See [Filtering by team](#event-clip-filter-team). | 
| maxResults | No | The maximum number of games to return, from 1 to 100. Defaults to 100. If the response includes a nextToken value, pass it in a subsequent request to retrieve the remaining games. | 

##### Game status
<a name="event-clip-game-status"></a>

The `status` of a game tells you whether it is safe to attach.

`Scheduled`  
The game has not started yet. You can attach it now, and clips begin when play starts.

`InProgress`  
The game is underway. Clips align to plays as they happen.

`Completed`  
The game has finished. Attach it to clip an already-aired game.

**Note**  
Dates are whole UTC days. An evening game in the United States can fall on the next UTC day. For example, a game that starts at 03:00 UTC on March 4 appears on the March 4 search date, not March 3. If you don't see your game, set `endDate` to a day later.

You can search for past games the same way. Set `startDate` and `endDate` to dates in the past, and attach a `Completed` game to clip a game that has already aired.

##### Filtering by team
<a name="event-clip-filter-team"></a>

When you filter by team, every word that you send must appear in the game's team names. Matching is case-insensitive and matches partial words, but does not do fuzzy matching. You can search by city name even though the response returns only the team name.

For the game *Northport Comets vs. Southport Meteors*, the values `comets`, `Comet`, and `Northport` all match, but `Cometz` does not.
+ **Either team** – use one filter with two values, such as `["Comets", "Meteors"]`.
+ **An exact matchup** – use two filters, with one team in each.

Words match independently, so `Northport Meteors` also matches the game in the previous example.

#### Step 2: Attach the game to your output
<a name="event-clip-attach-game"></a>

Attach the game to an event clipping output by including the `fixtureId` in the output's `dataSourceConfiguration`. You can do this when you create the feed, or on an existing feed by using `UpdateFeed`. The `fixtureId` is the only value you provide, and you can attach one game to each event clipping output.

The following example attaches a game to an event clipping output when creating a feed.

```
aws elemental-inference create-feed \
  --name "my-feed" \
  --outputs '[{
    "name": "clipping",
    "status": "ENABLED",
    "outputConfig": {
      "clipping": {
        "dataSourceConfiguration": {
          "fixtureId": "NwrW5B17Rw9W25g1jPlobSGdQfBOKyD3227bcsRK0w3..."
        }
      }
    }
  }]'
```

#### Checking that it works
<a name="event-clip-verify"></a>

Clips appear only after both of the following are true: the game has started, and your channel is sending media. You can confirm the results as follows:
+ Call `GetFeed` to confirm that the `fixtureId` stored on the output is the game that you picked.
+ As clips are produced, they appear in the metadata that Elemental Inference emits for the output. This is the primary confirmation that Sports Data is working.

If you don't see clips yet, check the following.

Feed isn't receiving media  
The feed isn't associated with a running channel yet, so no media is arriving. Start the channel, and confirm that it is sending to this feed.

Game hasn't started  
A `Scheduled` game produces no clips until play starts. This is expected, not a fault.

Wrong game attached  
Call `GetFeed` and compare the `fixtureId` against your search result.

## Configuring smart crop
<a name="create-feed-console-smart-crop"></a>

Smart crop has no required configuration. Optionally, you can add **graphic composition** to a smart crop output to detect known graphics, such as scoreboards and advertisements, in your source media. You provide one or more reference images, called **templates**, and Elemental Inference reports, for each analyzed frame, whether each graphic is present and where it appears as a bounding box. Elemental Inference returns graphic composition results as part of the smart crop metadata. For more information, see [Metadata for graphic composition](query-metadata-query.md#query-metadata-smart-crop-graphics).

You can configure one to four template groups of reference images, where each group represents a single graphic to detect. Configuring at least one group enables graphic composition in the output. Each group has the following settings:
+ **Name** (required) – A name for the graphic. The name can be 1–128 characters, must start and end with an alphanumeric character, and can contain letters, numbers, hyphens (-), and underscores (\_). Elemental Inference returns this same name in the metadata so that you can identify which graphic was detected.
+ **Template URIs** (required) – Up to two Amazon S3 URIs of reference images for the graphic. Provide more than one image when the same graphic can appear in more than one variation.

**Note**  
Store your reference images in an Amazon S3 bucket in the same account that creates the feed, and that Elemental Inference can read using the access role (`accessRoleArn`) associated with the feed.

For the best detection performance, follow these recommendations when you prepare your template images:
+ Provide each template as a PNG image with an alpha channel. Set the alpha value to 0 for any regions that Elemental Inference should ignore when matching. Elemental Inference uses only the non-transparent regions for detection. Make transparent the parts of the graphic that change from frame to frame. Leave the parts that stay the same fully opaque. For example, in a scoreboard template, set the alpha to 0 over the score and clock digits and over any animated or moving elements. Leave the parts that don't change, such as the scoreboard outline and the team labels, fully opaque.
+ Graphic detection runs at a resolution of 2560 x 1440. For the best results, size each template to match how large the graphic appears in a 2560 x 1440 frame.

The following example shows how to include a smart crop output that detects two graphics, a scoreboard and ads, when creating a feed using the CLI:

```
aws elemental-inference create-feed \
  --name "my-feed" \
  --access-role-arn "arn:aws:iam::111122223333:role/my-ei-access-role" \
  --outputs '[{
    "name": "crop",
    "status": "ENABLED",
    "outputConfig": {
      "cropping": {
        "templateGroups": [
          {
            "name": "scoreboard",
            "templateUris": [
              "s3://amzn-s3-demo-bucket/scoreboard-v1.png",
              "s3://amzn-s3-demo-bucket/scoreboard-v2.png"
            ]
          },
          {
            "name": "ads",
            "templateUris": [
              "s3://amzn-s3-demo-bucket/ads.png"
            ]
          }
        ]
      }
    }
  }]'
```

## Configuring smart subtitles
<a name="create-feed-console-smart-subtitles"></a>

Smart subtitles uses automatic speech recognition (ASR) to generate TTML subtitles from the audio in your source media. Configure the following settings for the smart subtitles output:
+ **Language** (required) – The language of the audio in the source media. Elemental Inference uses this setting to optimize transcription accuracy. Supported values:
  + `deu` – German
  + `eng` – English
  + `eng-au` – English (Australia)
  + `eng-gb` – English (Great Britain)
  + `eng-us` – English (United States)
  + `fra` – French
  + `ita` – Italian
  + `por` – Portuguese
  + `spa` – Spanish
+ **Aspect ratio** (optional) – The width and height of the output video, specified as integer values. Elemental Inference uses the aspect ratio to determine subtitle layout and line lengths.
+ **Dictionary** (optional) – The ID of a custom dictionary to improve transcription accuracy for domain-specific terminology. For information about creating and managing dictionaries, see [Managing dictionaries](#create-feed-console-dictionaries).
+ **Profanity filter** (optional) – Controls how profanity is handled in the generated subtitles. Supported values:
  + `DISABLED` – No filtering (default). All words appear as transcribed.
  + `CENSOR` – Replace profanity with asterisks.
  + `DROP` – Remove profanity from the transcript entirely.

**CLI example**

The following example shows how to include a smart subtitles output when creating a feed using the CLI:

```
aws elemental-inference create-feed \
  --name "my-feed" \
  --outputs '[{
    "name": "subtitles",
    "status": "ENABLED",
    "outputConfig": {
      "subtitling": {
        "language": "eng",
        "aspectRatio": {"width": 16, "height": 9},
        "profanityFilter": "DISABLED"
      }
    }
  }]'
```

## Managing dictionaries
<a name="create-feed-console-dictionaries"></a>

A dictionary contains custom words and phrases that the ASR engine might not recognize, such as brand names, technical terms, or proper nouns. You can reference a dictionary when configuring a smart subtitles output to improve transcription accuracy for domain-specific terminology.

Use the Elemental Inference dictionary API operations to manage dictionaries:
+ `CreateDictionary` – Create a new dictionary. Specify a name, language, and optionally provide entries.
+ `GetDictionary` – Retrieve details about a dictionary.
+ `UpdateDictionary` – Update the name, language, or entries of a dictionary.
+ `ExportDictionaryEntries` – Export the entries from a dictionary.
+ `ListDictionaries` – List all dictionaries in your account.
+ `DeleteDictionary` – Deletes a dictionary. You cannot delete a dictionary that is referenced by a feed. To delete a dictionary, first update or delete any feeds that reference it.

**Dictionary validation rules**

When creating or updating a dictionary, the following validation rules apply:
+ **Name**
  + 1–128 characters
  + Must start and end with an alphanumeric character
  + Allowed characters: letters, digits, hyphen (-), underscore (\_)
+ **Language**

  One of: `deu`, `eng`, `fra`, `ita`, `por`, `spa`

  Regional language variants (such as `eng-au`, `eng-gb`, `eng-us`) are not supported for dictionaries. Use the base language code (for example, `eng`) instead.
+ **Entries** (JSON payload)
  + Must be a valid JSON array. A top-level object or scalar is rejected.
  + Maximum 40 KB serialized payload size.
  + Each entry must include a `content` field that is not blank.
  + Each entry may optionally include a `sounds_like` field. If provided, it must be an array of non-blank strings.
  + Each `sounds_like` hint must contain only characters from the dictionary language's primary script. Currently, all supported languages use Latin script (Latin alphabet, accented letters, and script-neutral punctuation are accepted; non-Latin scripts are rejected).