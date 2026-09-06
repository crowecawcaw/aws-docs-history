

# Creating HLS rendition groups (web interface)
<a name="hls-rendition-groups-create-using-web-interface"></a>

**Topics**
+ [Step 1. Create video-only outputs](#hls-rendition-groups-create-using-web-interface-video-only-outputs)
+ [Step 3. Create audio-only outputs](#hls-rendition-groups-create-using-web-interface-audio-only-outputs)
+ [Step 4. Caption-only streams](#hls-rendition-groups-create-using-web-interface-caption-only-streams)
+ [Step 5. Verify Outputs for the HLS Rendition Group](#hls-rendition-groups-create-using-web-interface-verify-outputs)
+ [Summary of the steps to create an HLS rendition group](#hls-rendition-groups-create-using-web-interface-summary)
+ [Example of the Event Output: Creating Caption-Only Streams for an HLS Rendition Group](#hls-rendition-groups-create-using-web-interface-example-of-event-output)

## Step 1. Create video-only outputs
<a name="hls-rendition-groups-create-using-web-interface-video-only-outputs"></a>

You must create “video-only” outputs. Follow these steps for each video-only output you need:

1. In the Elemental Live web interface, display the **Apple HLS** output group tab.

1. Click **Add Output** in order to create an output.

1. Select or create a stream to be associated with that output. For example, Stream 1.

1. In that stream, delete the **Default Audio** tab. This stream now contains only a video stream.

1. Go back to the Output section associated with this stream and click **Advanced**. The **Audio Rendition Sets **field now appears, with a default value of “audio\_program.” This field shows in an output only when the associated stream contains only one video stream.

1. Change the **Audio Rendition Sets** field to specify the rendition group or groups to associate with this video: 
   + To associate the video with one rendition group, enter the name of the rendition group.
   + To associate the video with several rendition groups, enter a comma-separated list of the rendition group names. Do not put a space after each comma.

## Step 3. Create audio-only outputs
<a name="hls-rendition-groups-create-using-web-interface-audio-only-outputs"></a>

Follow these steps for each audio-only output you need:

1. Click **Add Output** in order to create an output.

1. Select or create a stream to be associated with that output. For example, Stream 3.

1. In that stream, delete the default **Video **and **Captions** tabs.This stream is now an audio stream.

1. Complete the following fields in the **Advanced** section:
   + **Stream Name**: The wording for the NAME parameter in the manifest, as described in [Audio information for an HLS output group with audio rendition group event](hls-rendition-groups-sample-manifest.md#hls-rendition-groups-sample-manifest-audio-information). This is the audio description that the client player user interface displays. If the description is a language, it should be in that language. For example, “Deutsch ”, not “German”.
   + **Language Code**: Optional; complete only if the audio is a language. The wording that is to appear in the LANGUAGE parameter in the manifest should be the language code as per RFC 5646, as described in [Audio information for an HLS output group with audio rendition group event](hls-rendition-groups-sample-manifest.md#hls-rendition-groups-sample-manifest-audio-information). This is the language code that the client player reads.

     You can also leave this field blank and check **Follow Input Language Code**; the language of the audio (specified in **Audio Source**, a bit higher up on the screen) is detected. 

1. Go back to the Output section associated with the first audio stream and click **Advanced**. 

   The **Audio Group ID** field and **Audio Track Type** now show. These fields show in an output only when the associated stream contains only one audio stream. The **Audio Group ID** field shows the default value “audio\_program.”

   (Note that the **Audio Only Image** field also appears in an audio-only stream. This field has nothing to do with audio rendition groups; it is used to assign an image in a “regular stream that has no video.”)
   + Set the **Audio Group ID **field to specify the audio rendition group that this audio will belong to. For example, “AAC group” or “Dolby group.” 
   + Set up the **Alternate Audio Track Selection **field (**Audio Track Type** field), as described in [Step 2. Determine defaults and auto-selection behavior](hls-rendition-groups-getting-ready-to-create.md#hls-rendition-groups-getting-ready-determine-defaults).

## Step 4. Caption-only streams
<a name="hls-rendition-groups-create-using-web-interface-caption-only-streams"></a>

If your output includes captions, you must create “captions-only” outputs. Follow these steps for each captions-only output you need:

1. Click **Add Output **in order to create an output.

1. Select or create a stream to be associated with that output.For example, Stream 4.

1. In that stream, delete the default **Video** tab and the default **Audio** tab. This stream now contains only a **captions** stream.

For more information about setting up captions, see [Working with captions](captions.md).

## Step 5. Verify Outputs for the HLS Rendition Group
<a name="hls-rendition-groups-create-using-web-interface-verify-outputs"></a>
+ Finally, check all your outputs for the HLS output groups and make sure you do not have an output that contains both audio and video. Including such an output may produce a manifest that the client player cannot interpret. 

## Summary of the steps to create an HLS rendition group
<a name="hls-rendition-groups-create-using-web-interface-summary"></a>

After these steps, you have:
+ One or more video-only outputs. Each output is associated through its **Audio Rendition Sets** field to one or more audio rendition groups.
+ Two or more audio-only outputs. Each output belongs to an audio rendition group based on the value in the **Audio Group ID** field.
+ Optionally, one or more captions-only outputs.

## Example of the Event Output: Creating Caption-Only Streams for an HLS Rendition Group
<a name="hls-rendition-groups-create-using-web-interface-example-of-event-output"></a>

Here is the Output section.

![Output section showing six stream configurations with name and segment modifiers.](http://docs.aws.amazon.com/elemental-live/latest/ug/images/hls-rendition-groups-create-example-output.png)


Here is the Streams section.

![Four stream configurations showing video and audio encoding settings with codec and bitrate options.](http://docs.aws.amazon.com/elemental-live/latest/ug/images/hls-rendition-groups-create-example-streams-1.png)![Four stream configurations showing video and audio encoding settings with codec and bitrate options.](http://docs.aws.amazon.com/elemental-live/latest/ug/images/hls-rendition-groups-create-example-streams-2.png)
