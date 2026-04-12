# Setting up Elemental Inference features for the first time

This section describes how to set up the first set of Elemental Inference features in MediaLive. You
can set up when you are first creating a channel, or you can set up in an existing
channel. You can set up one Elemental Inference feature or several features at the same time.

You must set up a fully-configured feed: resource - feed - output or outputs, where
the MediaLive channel is the resource and each output represents one Elemental Inference feature.

1. **In Elemental Inference**, use `create-feed` to
   create a new feed. Follow these guidelines:
   - Give the feed a memorable name. You might want to give it the same
     name or similar name to the MediaLive channel.

   Note that if you previously set up Elemental Inference features using the MediaLive
   console, you will see these feeds when you use `list-feeds`.
   These feeds will always have a name that is identical to the channel
   name.
   - Include outputs as described in the following table.

| Feature to set up | Action                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Event clipping    | Create one output of type `ClippingConfig`                                                                                                                                                                                                                                                                                                                                                                                                      |
| Smart crop        | Don't include any outputs in the feed. MediaLive will create an<br>output to use. It won't use any output that you create, but any<br>feed you create will count towards one or more the [quotas](https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/elemental-inference/quotas "https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/elemental-inference/quotas") for Elemental Inference. |

2. The response includes the following information that you should make a note
   of:
   - The feed ID, which you will need for CLI commands on this feed.
   - The feed ARN, which you will need to work with the MediaLive channel. You
     can also obtain the ARN using `get-feed`.

3. **In MediaLive**, use `create-channel` or
   `update-channel` to create a channel or edit an existing channel.
   - At the top level of the JSON, add an `InferenceSettings`
     section and include:
     - `feedArn`: The ARN of the feed that you created.
       Include this line only once, even if you are enabling more than
       one Elemental Inference feature.

   - Make changes for each feature, as described in the following
     table.

| Feature to set up | Action                                                                                                                                                                                                                                                                   |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Event clipping    | There are no further changes to make.                                                                                                                                                                                                                                    |
| Smart crop        | In the JSON for each video encode (video description<br>section) where you want to enable Elemental Inference features, include<br>these parameters:<br>• `Width` and `Height`: The<br>resolution for this video encode.<br>• `ScalingBehavior`: Set to<br>`SMART_CROP`. |

The following example shows the JSON for enabling both smart crop and event
clipping.

Smart crop is enabled in the video encode (video description) named
`high_resolution` in an output named `output_A` in the
output group named `My_outputgroup` in the channel with the ID
`9042242`. The video description includes, among other
parameters, the parameters `Height`, `Name`,
`ScalingBehavior`, and `Width`.

The ARN of the feed ends with the unique ID
`vbphju6m7nohlpcs3sd`.

```
{
  "Arn": "arn:aws:medialive:us-west-2:111122223333:channel:9042242",
...
  "EncoderSettings": {
...
    "OutputGroups": [
      {
        "Name": "My_outputgroup",
...
        "Outputs": [
          {
...
            "OutputName": "output_A",
...
            "VideoDescriptionName": "high_resolution"
          }
        ]
      }
    ],
...
    "VideoDescriptions": [
...
        "Height": 1280,
        "Name": "high_resolution",
        "ScalingBehavior": "SMART_CROP",
        "Width": 720
      }
    ]
  },
  "Id": "9042242",


  "InferenceSettings": {
    "FeedArn": "arn:aws:elemental-inference:us-west-2:111122223333:feed/vbphju6m7nohlpcs3sd"
...
}

```

4.  When you save the channel, MediaLive updates the Elemental Inference feed as follows:

        * It creates a crop output in the feed.
        * It associates the channel (the resource) with the feed.

    You now have a usable feed: resource - feed - output.

5.  In MediaLive, use `StartChannel`. When the channel is running, MediaLive
    performs the following actions:
    - MediaLive delivers the source stream to Elemental Inference.

    - It handles the metadata as described in the following table.

| Feature        | Action by MediaLive                                                                                                                                                                                                                                                                                                                                     |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Event clipping | MediaLive doesn't retrieve metadata. You need to set up your<br>own solution to retrieve the event clipping metadata and<br>create event clips.                                                                                                                                                                                                         |
| Smart crop     | MediaLive retrieves the smart crop metadata from Elemental Inference. This<br>metadata describes the region of interest in each video frame.<br>In each video output where Elemental Inference features is set up, MediaLive<br>crops the video to the new region of interest. MediaLive then<br>continues with regular processing to encode the video. |

**Observations**

There are differences in the procedure for setting up different Elemental Inference, particularly
in terms of how the division of labor between Elemental Inference and MediaLive in one feature is
different from the division of labor in another feature.

The following table summarizes the key differences in this division of labor. In the
table, read across the row for each feature.

| Feature        | Actions you perform in Elemental Inference                                                                   | Actions your perform in MediaLive                                                                                                                                                                                 |
| -------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Event clipping | You create a feed for the channel (if there isn't one already), and<br>you attach a clipping output.         | You make sure that the feed ARN is specified.                                                                                                                                                                     |
| Smart crop     | You create a feed for the channel (if there isn't one already), but<br>you don't attach a smart crop output. | You make sure that the feed ARN is specified. And you configure the<br>video outputs in the channel to work with smart crop. MediaLive is the<br>actor that creates the smart crop output in Elemental Inference. |
