

# Setting up with the MediaLive API or CLI

The only change a function output needs on the MediaLive side is the feed ARN. There is no video description to add (that is smart crop), no caption selector (that is smart subtitles), and no output group. In the following examples, replace `{{us-west-2}}`, `{{111122223333}}`, and `{{feed-id}}` in the feed ARN with the AWS Region, the account ID, and the ID of your feed.

```
{
  "InferenceSettings": {
    "FeedArn": "arn:aws:elemental-inference:{{us-west-2}}:{{111122223333}}:feed/{{feed-id}}"
  }
}
```

If the function reads `media.transcript`, map the feed's audio input to a channel audio selector so that speech recognition has audio to work with. Replace `{{audio-selector-name}}` with the name of the audio selector.

```
{
  "InferenceSettings": {
    "FeedArn": "arn:aws:elemental-inference:{{us-west-2}}:{{111122223333}}:feed/{{feed-id}}",
    "AudioFeedInputs": [
      { "FeedInput": "default-audio", "AudioSelectorName": "{{audio-selector-name}}" }
    ]
  }
}
```

If the input attachment has no audio selectors, you can omit `AudioFeedInputs` and MediaLive uses the input's default audio. For more information, see [AWS Elemental Inference](https://docs.aws.amazon.com/medialive/latest/ug/elemental-inference.html) in the *AWS Elemental MediaLive User Guide*.