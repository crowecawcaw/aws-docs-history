

# Attaching a function using the CLI
<a name="functions-attach-cli"></a>

**Important**  
`update-feed` replaces the whole feed configuration. The `outputs` array that you send replaces the existing array, and omitting `accessRoleArn` clears the stored role. Always call `get-feed` first and resend the complete list, including the access role. If the feed has a function output with a model target, clearing the role this way is rejected, but an output that you forget to resend is silently dropped.

1. Get the current configuration of the feed.

   ```
   aws elemental-inference get-feed \
     --region {{us-west-2}} \
     --id {{feed-id}}
   ```

1. Resend the feed with your function output added, and with the access role. In the following example, `medialive-clipping` is an existing output that must be preserved, and `play-description` is the new function output.

   ```
   aws elemental-inference update-feed \
     --region {{us-west-2}} \
     --id {{feed-id}} \
     --name {{my-feed}} \
     --access-role-arn arn:aws:iam::{{111122223333}}:role/{{ElementalInferenceFeedAccessRole}} \
     --outputs '[
       {
         "name": "medialive-clipping",
         "status": "ENABLED",
         "outputConfig": { "clipping": { "callbackMetadata": "game-1234" } },
         "fromAssociation": true
       },
       {
         "name": "play-description",
         "description": "One-sentence description of the last 10 seconds of play",
         "status": "ENABLED",
         "outputConfig": {
           "function": {
             "functionArn": "arn:aws:elemental-inference:us-west-2:111122223333:function/{{function-id}}",
             "trigger": { "fixedInterval": { "intervalSeconds": 10 } },
             "frameSettings": { "frameSampling": { "mode": "UNIFORM", "count": 4 } }
           }
         }
       }
     ]'
   ```

   Preserve `"fromAssociation": true` on any output that was created by the service that associated the feed, such as AWS Elemental MediaLive. Omit the field when it is `false`.

You can also include a function output in the `outputs` array of `create-feed`, when you create the feed in the first place.

## Attachment examples
<a name="functions-attach-cli-examples"></a>

**Transcript summary every 30 seconds**, sourced from a smart subtitles output named `subs-eng`.

```
{
  "name": "transcript-summary",
  "status": "ENABLED",
  "outputConfig": {
    "function": {
      "functionArn": "arn:aws:elemental-inference:us-west-2:111122223333:function/{{function-id}}",
      "trigger": { "fixedInterval": { "intervalSeconds": 30 } },
      "subtitlingSettings": { "outputName": "subs-eng" }
    }
  }
}
```

**Brand-safety check once per scene**, sourced from a contextual metadata output named `ctx-md`.

```
{
  "name": "ad-suitability",
  "status": "ENABLED",
  "outputConfig": {
    "function": {
      "functionArn": "arn:aws:elemental-inference:us-west-2:111122223333:function/{{function-id}}",
      "trigger": { "perScene": {} },
      "contextualMetadataSettings": { "outputName": "ctx-md" }
    }
  }
}
```

**Shot described once per shot boundary**, with three frames sampled evenly across the shot and resized to 640 x 360.

```
{
  "name": "shot-description",
  "status": "ENABLED",
  "outputConfig": {
    "function": {
      "functionArn": "arn:aws:elemental-inference:us-west-2:111122223333:function/{{function-id}}",
      "trigger": { "perShot": {} },
      "frameSettings": {
        "frameSampling": { "mode": "UNIFORM", "count": 3 },
        "frameSize": { "widthPixels": 640, "heightPixels": 360 }
      }
    }
  }
}
```

**Headline written for each detected clip**, sourced from an event clipping output named `game-clips`, with the first frame of the clip as visual context.

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