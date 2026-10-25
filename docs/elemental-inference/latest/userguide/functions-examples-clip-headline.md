

# Write a headline for each detected clip
<a name="functions-examples-clip-headline"></a>

Runs once for each window in which event clipping detects a clip, and combines the event descriptions with the first frame of the window. Requires an enabled event clipping output on the feed. The score line is included only when the clipping output is mapped to a sports data source, which reports the score. With a sports data source, a change of game phase is also an event, so a window whose only event is a phase change runs the function too.

**Request expression** (Anthropic Claude models)

```
(
  $state := media.clip.eventState;
  {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": $append(
          [{
            "type": "text",
            "text": "Events in this clip:\n" & $join(media.clip.events.(keyword & ": " & description), "\n")
                  & ($state.homeScore != null and $state.awayScore != null
                      ? "\nScore: " & $string($state.homeScore) & "-" & $string($state.awayScore)
                      : "")
                  & "\n\nWrite a headline of at most 10 words for a social post about this clip. Reply with only the headline, in plain text."
          }],
          media.frames.{
            "type": "image",
            "source": { "type": "base64", "media_type": "image/jpeg", "data": $ }
          }
        )
      }
    ]
  }
)
```

**Response expression**

```
{ "headline": content[type = "text"][0].text }
```

**Note**  
A response expression can see only the model response, not `media`. To store the event keyword next to the headline, ask the model to echo it in its answer and parse the answer with `$parse()`, or read the clipping output separately with `GetMetadata`.

**Function output**

```
{
  "name": "clip-headline",
  "status": "ENABLED",
  "outputConfig": {
    "function": {
      "functionArn": "arn:aws:elemental-inference:us-west-2:111122223333:function/{{function-id}}",
      "trigger": { "perClip": {} },
      "clippingSettings": { "outputName": "game-clips" },
      "frameSettings": { "frameSampling": { "mode": "FIRST", "count": 1 } }
    }
  }
}
```

**Result**

```
{"headline":"Pick-six seals it with two minutes left"}
```