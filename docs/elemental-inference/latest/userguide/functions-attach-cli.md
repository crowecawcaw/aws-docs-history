

# Attaching a function using the CLI

The `outputs` array that you send to `update-feed` replaces the feed's existing outputs. Call `get-feed` first, and resend every output that you want to keep.

In the following commands, replace `{{us-west-2}}` with your AWS Region, `{{feed-id}}` with the ID of your feed, `{{my-feed}}` with the name of your feed, `{{111122223333}}` with your AWS account ID, `{{ElementalInferenceFeedAccessRole}}` with the name of your access role, and `{{function-id}}` with the ID of your function.

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
             "functionArn": "arn:aws:elemental-inference:{{us-west-2}}:{{111122223333}}:function/{{function-id}}",
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

In each example, replace `{{us-west-2}}`, `{{111122223333}}`, and `{{function-id}}` in the function ARN with the AWS Region, the account ID, and the ID of your function.

**Example – Transcript summary every 30 seconds**. This function output reads from a smart subtitles output named `subs-eng`.

```
{
  "name": "transcript-summary",
  "status": "ENABLED",
  "outputConfig": {
    "function": {
      "functionArn": "arn:aws:elemental-inference:{{us-west-2}}:{{111122223333}}:function/{{function-id}}",
      "trigger": { "fixedInterval": { "intervalSeconds": 30 } },
      "subtitlingSettings": { "outputName": "subs-eng" }
    }
  }
}
```

**Example – Brand-safety check once per scene**. This function output reads from a contextual metadata output named `ctx-md`.

```
{
  "name": "ad-suitability",
  "status": "ENABLED",
  "outputConfig": {
    "function": {
      "functionArn": "arn:aws:elemental-inference:{{us-west-2}}:{{111122223333}}:function/{{function-id}}",
      "trigger": { "perScene": {} },
      "contextualMetadataSettings": { "outputName": "ctx-md" }
    }
  }
}
```

**Example – Shot described once per shot boundary**. This function output samples three frames evenly across the shot and resizes them to 640 x 360.

```
{
  "name": "shot-description",
  "status": "ENABLED",
  "outputConfig": {
    "function": {
      "functionArn": "arn:aws:elemental-inference:{{us-west-2}}:{{111122223333}}:function/{{function-id}}",
      "trigger": { "perShot": {} },
      "frameSettings": {
        "frameSampling": { "mode": "UNIFORM", "count": 3 },
        "frameSize": { "widthPixels": 640, "heightPixels": 360 }
      }
    }
  }
}
```

**Example – Headline written for each detected clip**. This function output reads from an event clipping output named `game-clips`, and uses the first frame of the clip as visual context.

```
{
  "name": "clip-headline",
  "status": "ENABLED",
  "outputConfig": {
    "function": {
      "functionArn": "arn:aws:elemental-inference:{{us-west-2}}:{{111122223333}}:function/{{function-id}}",
      "trigger": { "perClip": {} },
      "clippingSettings": { "outputName": "game-clips" },
      "frameSettings": { "frameSampling": { "mode": "FIRST", "count": 1 } }
    }
  }
}
```