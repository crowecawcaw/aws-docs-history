

# Setting up with the MediaLive API or CLI
<a name="functions-medialive-cli"></a>

The only change a function output needs on the MediaLive side is the feed ARN. There is no video description to add (that is smart crop), no caption selector (that is smart subtitles), and no output group.

```
{
  "InferenceSettings": {
    "FeedArn": "arn:aws:elemental-inference:us-west-2:111122223333:feed/{{feed-id}}"
  }
}
```

If the function reads `media.transcript`, map the feed's audio input to a channel audio selector so that speech recognition has audio to work with.

```
{
  "InferenceSettings": {
    "FeedArn": "arn:aws:elemental-inference:us-west-2:111122223333:feed/{{feed-id}}",
    "AudioFeedInputs": [
      { "FeedInput": "default-audio", "AudioSelectorName": "{{Audio_1}}" }
    ]
  }
}
```

If the input attachment has no audio selectors, you can omit `AudioFeedInputs` and MediaLive uses the input's default audio. For more information, see [AWS Elemental Inference](https://docs.aws.amazon.com/medialive/latest/ug/elemental-inference.html) in the *AWS Elemental MediaLive User Guide*.