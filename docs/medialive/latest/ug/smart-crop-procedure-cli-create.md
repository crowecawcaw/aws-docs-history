

# Setting up Elemental Inference features for the first time
<a name="smart-crop-procedure-cli-create"></a>

This section describes how to set up the first set of Elemental Inference features in MediaLive. You can set up when you are first creating a channel, or you can set up in an existing channel. You can set up one Elemental Inference feature or several features at the same time. 

You must set up a fully-configured feed: resource - feed - output or outputs, where the MediaLive channel is the resource and each output represents one Elemental Inference feature.

1. **In Elemental Inference**, use `create-feed` to create a new feed. Follow these guidelines:
   + Give the feed a memorable name. You might want to give it the same name or similar name to the MediaLive channel. 

     Note that if you previously set up Elemental Inference features using the MediaLive console, you will see these feeds when you use `list-feeds`. These feeds will always have a name that is identical to the channel name.
   + Include outputs as described in the following table.


<table>
<thead>
  <tr><th>Feature to set up</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td>Event clipping</td><td>Create one output of type <code>ClippingConfig</code> </td></tr>
  <tr><td>Smart crop</td><td>Don't include any outputs in the feed. MediaLive will create an output to use. It won't use any output that you create, but any feed you create will count towards one or more the <a href="https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/elemental-inference/quotas">quotas</a> for Elemental Inference.</td></tr>
  <tr><td>Smart Subtitles</td><td>Create one output of type <code>SubtitlingConfig</code>. Configure the <code>language</code> parameter with the language code of the source audio (for example, <code>eng</code>). Optionally configure <code>profanityFilter</code> (<code>DISABLED</code>, <code>CENSOR</code>, or <code>DROP</code>).</td></tr>
  <tr><td>Contextual metadata enrichment</td><td>Create one output of type <code>ContextualMetadataConfig</code>.</td></tr>
</tbody>
</table>


1. The response includes the following information that you should make a note of:
   + The feed ID, which you will need for CLI commands on this feed.
   + The feed ARN, which you will need to work with the MediaLive channel. You can also obtain the ARN using `get-feed`.

1. **In MediaLive**, use `create-channel` or `update-channel` to create a channel or edit an existing channel. 
   + At the top level of the JSON, add an `InferenceSettings` section and include:
     + `feedArn`: The ARN of the feed that you created. Include this line only once, even if you are enabling more than one Elemental Inference feature.
   + Make changes for each feature, as described in the following table.


<table>
<thead>
  <tr><th>Feature to set up</th><th>Action</th></tr>
</thead>
<tbody>
  <tr><td>Event clipping</td><td>There are no further changes to make.</td></tr>
  <tr><td>Smart crop</td><td>In the JSON for each video encode (video description section) where you want to enable Elemental Inference features, include these parameters:<ul><li> <code>Width</code> and <code>Height</code>: The resolution for this video encode. </li><li> <code>ScalingBehavior</code>: Set to <code>SMART_CROP</code>.  </li></ul></td></tr>
  <tr><td>Smart Subtitles</td><td>In each input attachment's <code>CaptionSelectors</code> array, add a caption selector with <code>SmartSubtitleSourceSettings</code>:<ul><li> <code>Name</code>: A name for the selector (for example, <code>SmartSubtitlesSelector1</code>). </li><li> <code>LanguageCode</code>: The language code (for example, <code>eng</code>). </li><li> <code>SelectorSettings</code>: Include <code>SmartSubtitleSourceSettings</code> with the following fields: <ul><li> <code>InferenceFeedOutput</code>: The name of the subtitling output from the feed (for example, <code>medialive-subtitling-output-0</code>). </li><li> <code>CaptionSynchronizationMode</code> (optional): Set to <code>VIDEO_ALIGNED_CAPTIONS</code> (default) to delay video for caption synchronization, or <code>NO_VIDEO_DELAY</code> to avoid video delay. </li></ul> </li></ul><br />Then add a <code>CaptionDescription</code> in <code>EncoderSettings</code> that references this selector and sets the destination to TTML (for MediaPackage V2, CMAF Ingest, or Microsoft Smooth output groups) or WebVTT (for HLS or MediaPackage output groups). Add a captions-only output in the appropriate output group for the subtitle sidecar.</td></tr>
  <tr><td>Contextual metadata enrichment</td><td>In the <code>InferenceSettings</code> section, add <code>EnrichmentMethods</code> with the value <code>["SCTE35_ELEMENTAL_INFERENCE_QUERY_PARAMS"]</code>. No other changes are needed. MediaLive automatically enriches SCTE-35 cue-out markers on all outputs that support SCTE-35 passthrough.</td></tr>
</tbody>
</table>


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


<table>
<thead>
  <tr><th>Feature </th><th>Action by MediaLive</th></tr>
</thead>
<tbody>
  <tr><td>Event clipping</td><td>MediaLive doesn't retrieve metadata. You need to set up your own solution to retrieve the event clipping metadata and create event clips.</td></tr>
  <tr><td>Smart crop</td><td>MediaLive retrieves the smart crop metadata from Elemental Inference. This metadata describes the region of interest in each video frame. In each video output where Elemental Inference features is set up, MediaLive crops the video to the new region of interest. MediaLive then continues with regular processing to encode the video. </td></tr>
  <tr><td>Smart Subtitles</td><td>MediaLive retrieves the subtitle metadata from Elemental Inference and converts it to WebVTT or TTML format. MediaLive outputs the subtitles as a sidecar in the configured HLS, MediaPackage, MediaPackage V2, CMAF Ingest, or Microsoft Smooth output.</td></tr>
  <tr><td>Contextual metadata enrichment</td><td>MediaLive enriches outgoing SCTE-35 cue-out markers with Elemental Inference query parameters. Downstream consumers parse these parameters to query Elemental Inference at ad-decision time.</td></tr>
</tbody>
</table>


**Observations**

There are differences in the procedure for setting up different Elemental Inference, particularly in terms of how the division of labor between Elemental Inference and MediaLive in one feature is different from the division of labor in another feature.

The following table summarizes the key differences in this division of labor. In the table, read across the row for each feature.


|  Feature  |  Actions you perform in Elemental Inference  | Actions your perform in MediaLive | 
| --- | --- | --- | 
| Event clipping | You create a feed for the channel (if there isn't one already), and you attach a clipping output.  | You make sure that the feed ARN is specified.  | 
| Smart crop | You create a feed for the channel (if there isn't one already), but you don't attach a smart crop output. | You make sure that the feed ARN is specified. And you configure the video outputs in the channel to work with smart crop. MediaLive is the actor that creates the smart crop output in Elemental Inference. | 
| Smart Subtitles | You create a feed for the channel (if there isn't one already), and you attach a subtitling output with the language configuration. | You make sure that the feed ARN is specified. You add SmartSubtitleSourceSettings caption selectors to input attachments, create caption descriptions referencing those selectors, and add a captions-only output (TTML for MediaPackage V2, CMAF Ingest, or Microsoft Smooth; or WebVTT for HLS or MediaPackage). | 
| Contextual metadata enrichment | You create a feed for the channel (if there isn't one already), and you attach a contextual metadata output. | Verify that the feed ARN is specified. Add SCTE35\_ELEMENTAL\_INFERENCE\_QUERY\_PARAMS to EnrichmentMethods in InferenceSettings. | 