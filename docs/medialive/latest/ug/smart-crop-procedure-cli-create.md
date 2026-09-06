

# Setting up Elemental Inference features for the first time
<a name="smart-crop-procedure-cli-create"></a>

This section describes how to set up the first set of Elemental Inference features in MediaLive. You can set up when you are first creating a channel, or you can set up in an existing channel. You can set up one Elemental Inference feature or several features at the same time. 

You must set up a fully-configured feed: resource - feed - output or outputs, where the MediaLive channel is the resource and each output represents one Elemental Inference feature.

1. **In Elemental Inference**, use `create-feed` to create a new feed. Follow these guidelines:
   + Give the feed a memorable name. You might want to give it the same name or similar name to the MediaLive channel. 

     Note that if you previously set up Elemental Inference features using the MediaLive console, you will see these feeds when you use `list-feeds`. These feeds will always have a name that is identical to the channel name.
   + Include outputs as described in the following table.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/smart-crop-procedure-cli-create.html)

1. The response includes the following information that you should make a note of:
   + The feed ID, which you will need for CLI commands on this feed.
   + The feed ARN, which you will need to work with the MediaLive channel. You can also obtain the ARN using `get-feed`.

1. **In MediaLive**, use `create-channel` or `update-channel` to create a channel or edit an existing channel. 
   + At the top level of the JSON, add an `InferenceSettings` section and include:
     + `feedArn`: The ARN of the feed that you created. Include this line only once, even if you are enabling more than one Elemental Inference feature.
   + Make changes for each feature, as described in the following table.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/smart-crop-procedure-cli-create.html)

   The following example shows the JSON for enabling both smart crop and event clipping. 

   Smart crop is enabled in the video encode (video description) named `high_resolution` in an output named `output_A` in the output group named `My_outputgroup` in the channel with the ID `9042242`. The video description includes, among other parameters, the parameters `Height`, `Name`, `ScalingBehavior`, and `Width`. 

   The ARN of the feed ends with the unique ID `vbphju6m7nohlpcs3sd`.

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

   The following example shows the key JSON sections for enabling Smart Subtitles. The channel has an input attachment with an audio selector (`Audio_1`), a Smart Subtitles caption selector that references a subtitling output on the feed, and a captions-only WebVTT output in a MediaPackage output group.

   ```
   {
   ...
     "InferenceSettings": {
       "FeedArn": "arn:aws:elemental-inference:us-west-2:111122223333:feed/abbrngaa6sbvawovk36",
       "AudioFeedInputs": [
         {
           "FeedInput": "default-audio",
           "AudioSelectorName": "Audio_1"
         }
       ]
     },
     "InputAttachments": [
       {
         "InputAttachmentName": "my-input",
         "InputId": "1112233",
         "InputSettings": {
           "AudioSelectors": [
             {
               "Name": "Audio_1",
               "SelectorSettings": {
                 "AudioLanguageSelection": {
                   "LanguageSelectionPolicy": "LOOSE",
                   "LanguageCode": "eng"
                 }
               }
             }
           ],
           "CaptionSelectors": [
             {
               "LanguageCode": "eng",
               "Name": "SmartSubtitlesSelector1",
               "SelectorSettings": {
                 "SmartSubtitleSourceSettings": {
                   "CaptionSynchronizationMode": "VIDEO_ALIGNED_CAPTIONS",
                   "InferenceFeedOutput": "medialive-subtitling-output-0"
                 }
               }
             }
           ]
   ...
         }
       }
     ],
     "EncoderSettings": {
       "CaptionDescriptions": [
         {
           "CaptionSelectorName": "SmartSubtitlesSelector1",
           "DestinationSettings": {
             "WebvttDestinationSettings": {
               "StyleControl": "NO_STYLE_DATA"
             }
           },
           "Name": "caption_subtitles"
         }
       ],
       "OutputGroups": [
         {
           "Outputs": [
             {
               "AudioDescriptionNames": [],
               "CaptionDescriptionNames": ["caption_subtitles"],
               "OutputName": "subtitles_only",
               "OutputSettings": {
                 "MediaPackageOutputSettings": {}
               }
             }
           ]
         }
       ]
   ...
     }
   }
   ```

   The `AudioFeedInputs` array in `InferenceSettings` associates a specific audio selector from the input attachment with the feed. If the input attachment has no audio selectors, you can omit `AudioFeedInputs` and MediaLive uses the default audio from the input.

1. When you save the channel, MediaLive updates the Elemental Inference feed as follows:
   + It creates a crop output in the feed. 
   + It associates the channel (the resource) with the feed.

   You now have a usable feed: resource - feed - output.

1. In MediaLive, use `StartChannel`. When the channel is running, MediaLive performs the following actions:
   + MediaLive delivers the source stream to Elemental Inference.
   + It handles the metadata as described in the following table.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/smart-crop-procedure-cli-create.html)

**Observations**

There are differences in the procedure for setting up different Elemental Inference, particularly in terms of how the division of labor between Elemental Inference and MediaLive in one feature is different from the division of labor in another feature.

The following table summarizes the key differences in this division of labor. In the table, read across the row for each feature.


|  Feature  |  Actions you perform in Elemental Inference  | Actions your perform in MediaLive | 
| --- | --- | --- | 
| Event clipping | You create a feed for the channel (if there isn't one already), and you attach a clipping output.  | You make sure that the feed ARN is specified.  | 
| Smart crop | You create a feed for the channel (if there isn't one already), but you don't attach a smart crop output. | You make sure that the feed ARN is specified. And you configure the video outputs in the channel to work with smart crop. MediaLive is the actor that creates the smart crop output in Elemental Inference. | 
| Smart Subtitles | You create a feed for the channel (if there isn't one already), and you attach a subtitling output with the language configuration. | You make sure that the feed ARN is specified. You add SmartSubtitleSourceSettings caption selectors to input attachments, create caption descriptions referencing those selectors, and add a captions-only output (TTML for MediaPackage V2, CMAF Ingest, or Microsoft Smooth; or WebVTT for HLS or MediaPackage). | 