

# What a function can read

Your request expression is evaluated against a single object named `media`. Each field of `media` is one kind of context that Elemental Inference can supply, as the following table shows.


| Context variable | Type | What it contains | Requires | 
| --- | --- | --- | --- | 
| media.frames | Array of strings | Video frames sampled from the trigger window, decoded by Elemental Inference, resized if the function output sets a frame size, and encoded as Base64 JPEG. | A model target whose model accepts images. | 
| media.transcript | String | The plain-text transcript of the speech in the trigger window. | An enabled smart subtitles output on the same feed, named in the function output's subtitlingSettings. Only with the fixedInterval trigger. | 
| media.contextual | Object | The contextual metadata of the current shot and the current scene: Interactive Advertising Bureau (IAB) categories, Global Alliance for Responsible Media (GARM) brand safety ratings, a summary, descriptive labels, and mood. | An enabled contextual metadata output on the same feed, named in the function output's contextualMetadataSettings. Only with the perScene or perShot trigger. | 
| media.clip | Object | The clips that event clipping detected in the window, and the tracked game state. | An enabled event clipping output on the same feed, named in the function output's clippingSettings. Only with the perClip or fixedInterval trigger. | 

`media.frames` comes from the feed's own video for the trigger window, so it needs no other output. The other three come from another output on the feed, which is why they each require one. A passthrough function can't read `media.frames`.

**Important**  
Reading data from more than one existing feature is not supported. A function can read `media.frames` together with at most *one* of `media.transcript`, `media.contextual`, and `media.clip`. A function that references two of those three is rejected when you create or update it.

You don't declare which context you want. Elemental Inference parses your request expression, derives the context from the `media.` paths that it references, and returns the result in the read-only `contextTypes` field of the function. The values are `FRAMES` (`media.frames`), `SUBTITLES` (`media.transcript`), `CONTEXTUAL_METADATA` (`media.contextual`), and `CLIP_METADATA` (`media.clip`). Reading `media.frames` is what causes frames to be decoded; if `contextTypes` comes back empty, your expression does not reference any media, and none is supplied at runtime.

**Note**  
The derivation reads the structure of the expression, not its text. A string literal or a field name that merely contains `media.frames` is not a reference.

## Fields in `media.contextual`
<a name="functions-context-contextual"></a>

`media.contextual` has two levels, `shot` and `scene`. Each level holds the contextual metadata of the current shot or the current scene, with the same field names and shapes as a contextual metadata item that `GetMetadata` returns. For more information about each field, see [Querying contextual metadata](query-metadata-query.md#query-metadata-contextual).

A function runs when its shot (`perShot`) or its scene (`perScene`) ends, and sees the latest contextual metadata at that moment. Both levels are present on both triggers. The level that the trigger is based on is final, and describes the whole shot or scene. The other level is its value so far. For example, when a `perShot` function runs, `scene` describes the scene up to the end of that shot.

A field that has no value is left out of the level. It is never `null`. A label list, such as `objects`, is left out when it has no entries, and `iabTaxonomy` is left out when no category matched. Which fields are present depends on the `summaryGeneration` and `extendedAnalysis` settings of the contextual metadata output, as it does for `GetMetadata`. Test for a field with `$exists()` before you build on it. `$exists(media.contextual.scene.summary)` is `false` when the scene has no summary.

The following table describes the fields of each level.


| Field | Type | Description | 
| --- | --- | --- | 
| startPts | Number | The start of the shot or scene, as a presentation timestamp in timescale units. | 
| timescale | Number | The timescale of startPts. Always 90000, the timescale that media.clip events also use. | 
| iabTaxonomy | Object | The IAB Content Taxonomy categories. version is V3\_1, and each entry in categories has a uniqueId and a path, for example ["Sports", "Soccer"]. | 
| garm | Object | The GARM brand safety ratings. Each entry in garm.suitability.categories has a category and a flagged value. A flagged category also has a risk: LOW, MEDIUM, HIGH, or FLOOR. FLOOR is the most severe. | 
| summary | String | A short description of what happens in the shot or scene. | 
| objects, actions, people, environments, domains, brands, onScreenTexts | Array of strings | The descriptive labels for the shot or scene. | 
| mood | Object | The intensity of eight emotions: anger, anticipation, joy, trust, fear, surprise, sadness, and disgust. Each is a number from 1 to 10. | 

The following example shows `media.contextual` when a `perShot` function runs. Fields that have no value, such as the `people` of the scene, are left out. The GARM category lists are shortened.

```
{
  "shot": {
    "startPts": 161388406721700,
    "timescale": 90000,
    "iabTaxonomy": {
      "version": "V3_1",
      "categories": [{ "uniqueId": "483", "path": ["Sports", "Soccer"] }]
    },
    "garm": {
      "suitability": {
        "categories": [
          { "category": "ILLEGAL_DRUGS_TOBACCO_ALCOHOL", "flagged": false },
          { "category": "OBSCENITY_PROFANITY", "flagged": true, "risk": "MEDIUM" }
        ]
      }
    },
    "summary": "A striker scores from the edge of the box.",
    "objects": ["ball", "goal net"],
    "actions": ["kicking", "celebrating"],
    "people": ["player", "goalkeeper"],
    "environments": ["stadium"],
    "mood": {
      "anger": 1.4, "anticipation": 6.8, "joy": 8.1, "trust": 4.9,
      "fear": 1.6, "surprise": 5.2, "sadness": 1.1, "disgust": 1.0
    },
    "brands": ["Example Corp"],
    "onScreenTexts": ["GOAL"]
  },
  "scene": {
    "startPts": 161388400000000,
    "timescale": 90000,
    "iabTaxonomy": {
      "version": "V3_1",
      "categories": [{ "uniqueId": "483", "path": ["Sports", "Soccer"] }]
    },
    "garm": {
      "suitability": {
        "categories": [
          { "category": "ILLEGAL_DRUGS_TOBACCO_ALCOHOL", "flagged": false },
          { "category": "OBSCENITY_PROFANITY", "flagged": true, "risk": "MEDIUM" }
        ]
      }
    },
    "summary": "The second half of a soccer match.",
    "objects": ["ball", "goal net", "scoreboard"]
  }
}
```

The following expressions read that example.

```
media.contextual.scene.summary                                        "The second half of a soccer match."
media.contextual.shot.iabTaxonomy.categories.path[-1]                 "Soccer", the IAB leaf labels
media.contextual.shot.garm.suitability.categories[flagged].category   "OBSCENITY_PROFANITY"
"Example Corp" in media.contextual.shot.brands                        true
```

A path that matches one value returns that value, not an array that contains it. Wrap the path in `[ ]` when your result needs an array. `[media.contextual.shot.iabTaxonomy.categories.path[-1]]` returns `["Soccer"]`.

## Fields in `media.clip`
<a name="functions-context-clip"></a>

`media.clip` describes the clips that the event clipping output detected in the window. A window can contain more than one clip – in American football, an interception returned for a touchdown is both events. The following table describes the fields of `media.clip`.


| Field | Type | Description | 
| --- | --- | --- | 
| events | Array of objects | One entry for each clip detected in the window. | 
| events[].keyword | String | The event keyword that matched, for example touchdown. | 
| events[].description | String | The play-by-play text for the event when the clipping output is mapped to a sports data source, or the clip description otherwise. | 
| events[].startPts, events[].endPts | Number | The start and end of the clip, as presentation timestamps. | 
| events[].timescale | Number | The timescale that startPts and endPts are expressed in. | 
| eventState | Object | The game state from the sports data source. Present only for a clipping output that is mapped to a sports data source. Each field is omitted when the data source doesn't report it. Until the first play is matched, only phase (PRE\_GAME) and sport are present. | 
| eventState.homeScore, eventState.awayScore | Number | The score of each team. | 
| eventState.period | Number | The current period, such as the quarter or half. | 
| eventState.clock | String | The game clock, for example 08:15. | 
| eventState.phase | String | The phase of the game: PRE\_GAME, IN\_PROGRESS, INTERMISSION, END\_OF\_REGULATION, OVERTIME, or FINAL. | 
| eventState.sport | String | BASKETBALL or FOOTBALL (American football). | 
| eventState.league | String | The league: NBA, NCAAMB (NCAA men's basketball), NCAAWB (NCAA women's basketball), NFL, or NCAAFB (NCAA football). | 

With a sports data source, `events` also reports changes of game phase. The event with keyword `gameStart` marks the first matched play, and an event with keyword `phase:{{PHASE}}` marks each change of `eventState.phase` – for example, `phase:INTERMISSION`. Each change is reported once.

**Note**  
`eventState` is carried forward, so it reports the last known game state even in a window whose own events matched nothing.