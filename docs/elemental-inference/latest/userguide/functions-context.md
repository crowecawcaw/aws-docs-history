

# What a function can read
<a name="functions-context"></a>

Your request expression is evaluated against a single object named `media`. Each field of `media` is one kind of context that Elemental Inference can supply.


| Context variable | Type | What it contains | Requires | 
| --- | --- | --- | --- | 
| media.frames | Array of strings | Video frames sampled from the trigger window, decoded by Elemental Inference, resized if the function output sets a frame size, and encoded as Base64 JPEG. | A model target whose model accepts images. | 
| media.video | String | One short video clip for the trigger window, remuxed from the sampled fragments and encoded as Base64 MP4. | A model target whose model accepts video. | 
| media.transcript | String | The plain-text transcript of the speech in the trigger window. | An enabled smart subtitles output on the same feed, named in the function output's subtitlingSettings. Only with the fixedInterval trigger. | 
| media.contextual | Object | The contextual classification of the shot or scene – summary, categories, objects, actions, and brand-safety risk. | An enabled contextual metadata output on the same feed, named in the function output's contextualMetadataSettings. Only with the perScene or perShot trigger. | 
| media.clip | Object | The clips that event clipping detected in the window, and the tracked game state. | An enabled event clipping output on the same feed, named in the function output's clippingSettings. Only with the perClip or fixedInterval trigger. | 

`media.frames` and `media.video` come from the feed's own video for the trigger window, so they need no other output. The other three come from another output on the feed, which is why they each require one. A passthrough function can't read `media.frames` or `media.video`.

**Important**  
Reading data from more than one existing feature is not supported. A function can read `media.frames` and `media.video` together with at most *one* of `media.transcript`, `media.contextual`, and `media.clip`. A function that references two of those three is rejected when you create or update it.

You don't declare which context you want. Elemental Inference parses your request expression, derives the context from the `media.` paths that it references, and returns the result in the read-only `contextTypes` field of the function. The values are `FRAMES` (`media.frames`), `VIDEO` (`media.video`), `SUBTITLES` (`media.transcript`), `CONTEXTUAL_METADATA` (`media.contextual`), and `CLIP_METADATA` (`media.clip`). Reading `media.frames` is what causes frames to be decoded; if `contextTypes` comes back empty, your expression does not reference any media, and none will be supplied at runtime.

**Note**  
The derivation reads the structure of the expression, not its text. A string literal or a field name that merely contains `media.frames` is not a reference.

## Fields in `media.contextual`
<a name="functions-context-contextual"></a>

`media.contextual` is a flattened view of one shot or scene classification. It is easier to write an expression against than the full `GetMetadata` shape of contextual metadata that is described in [Querying contextual metadata](query-metadata-query.md#query-metadata-contextual).


| Field | Type | Description | 
| --- | --- | --- | 
| summary | String | The descriptive summary of the shot or scene, or null when the contextual metadata output doesn't have summary generation enabled. | 
| categories | Array of strings | The IAB Content Taxonomy categories, as their leaf labels – for example, ["Basketball", "Television"]. | 
| objects | Array of strings | The objects detected in the shot or scene. | 
| actions | Array of strings | The actions detected in the shot or scene. | 
| garm.risk | String | The overall GARM brand-safety risk level: LOW, MEDIUM, HIGH, or FLOOR. FLOOR is the most severe. | 
| garm.flagged | Array of strings | The names of the GARM categories that were flagged – for example, ["ILLEGAL\_DRUGS\_TOBACCO\_ALCOHOL"]. Categories that were not flagged are omitted. | 

## Fields in `media.clip`
<a name="functions-context-clip"></a>

`media.clip` describes the clips that the event clipping output detected in the window. A window can contain more than one clip – in American football, an interception returned for a touchdown is both events.


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