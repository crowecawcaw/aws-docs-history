This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Creating HLS Rendition Groups

(Web Interface)

###### Topics

- [Step 1.
  Create Video-Only Outputs](#hls-rendition-groups-create-using-web-interface-video-only-outputs "#hls-rendition-groups-create-using-web-interface-video-only-outputs")
- [Step 3.
  Create Audio-Only Outputs](#hls-rendition-groups-create-using-web-interface-audio-only-outputs "#hls-rendition-groups-create-using-web-interface-audio-only-outputs")
- [Step 4.
  Caption-Only Streams](#hls-rendition-groups-create-using-web-interface-caption-only-streams "#hls-rendition-groups-create-using-web-interface-caption-only-streams")
- [Step 5. Verify
  Outputs for the HLS Rendition Group](#hls-rendition-groups-create-using-web-interface-verify-outputs "#hls-rendition-groups-create-using-web-interface-verify-outputs")
- [Summary of the Steps
  to Create an HLS Rendition Group](#hls-rendition-groups-create-using-web-interface-summary "#hls-rendition-groups-create-using-web-interface-summary")
- [Example of the Event Output: Creating Caption-Only Streams for an HLS Rendition
  Group](#hls-rendition-groups-create-using-web-interface-example-of-event-output "#hls-rendition-groups-create-using-web-interface-example-of-event-output")

## Step 1.

Create Video-Only Outputs

You must create “video-only” outputs. Follow these steps for each video-only output you
need:

1. In the AWS Elemental Server web interface, display the **Apple
   HLS** output group tab.
2. Click **Add Output** in order to create an output.
3. Select or create a stream to be associated with that output. For example, Stream
4.
5. In that stream, delete the **Default Audio** tab. This
   stream now contains only a video stream.
6. Go back to the Output section associated with this stream and click **Advanced**. The **Audio Rendition Sets** field now appears, with a default value of “audio_program.” This field shows in an
   output only when the associated stream contains only one video stream.
7. Change the **Audio Rendition Sets** field to specify the
   rendition group or groups to associate with this video:
   - To associate the video with one rendition group, enter the name of the rendition
     group.
   - To associate the video with several rendition groups, enter a comma-separated list of
     the rendition group names. Do not put a space after each comma.

## Step 3.

Create Audio-Only Outputs

Follow these steps for each audio-only output you need:

1. Click **Add Output** in order to create an output.
2. Select or create a stream to be associated with that output. For example, Stream
3.
4. In that stream, delete the default **Video** and **Captions** tabs.This stream is now an audio stream.
5. Complete the following fields in the **Advanced**
   section:
   - **Stream Name**: The wording for the NAME parameter in
     the manifest, as described in [Audio Information for
     an HLS Output Group with Audio Rendition Group Event](hls-rendition-groups-sample-manifest.md#hls-rendition-groups-sample-manifest-audio-information "hls-rendition-groups-sample-manifest.md#hls-rendition-groups-sample-manifest-audio-information") . This is the
     audio description that the client player user interface displays. If the description is a
     language, it should be in that language. For example, “Deutsch ”, not “German”.
   - **Language Code**: Optional; complete only if the audio
     is a language. The wording that is to appear in the LANGUAGE parameter in the manifest
     should be the language code as per RFC 5646, as described in [Audio Information for
     an HLS Output Group with Audio Rendition Group Event](hls-rendition-groups-sample-manifest.md#hls-rendition-groups-sample-manifest-audio-information "hls-rendition-groups-sample-manifest.md#hls-rendition-groups-sample-manifest-audio-information") . This is the
     language code that the client player reads.

   You can also leave this field blank and check **Follow Input
   Language Code**; the language of the audio (specified in **Audio Source**, a bit higher up on the screen) is detected.

6. Go back to the Output section associated with the first audio stream and click **Advanced**.

The **Audio Group ID** field and Alternate **Audio Track Type** field (named **Audio Track
Selection** in earlier versions) now show. These fields show in an output only when
the associated stream contains only one audio stream. The **Audio Group
ID** field shows the default value “audio_program.”

(Note that the **Audio Only Image** field also appears in
an audio-only stream. This field has nothing to do with audio rendition groups; it is used to
assign an image in a “regular stream that has no video.”)

    * Set the **Audio Group ID** field to specify the audio
     rendition group that this audio will belong to. For example, “AAC group” or “Dolby group.”
    * Set up the **Alternate Audio Track Selection** field
     (**Audio Track Type** field), as described in [Step 2. Determine
     Defaults and Auto-Selection Behavior](hls-rendition-groups-getting-ready-to-create.md#hls-rendition-groups-getting-ready-determine-defaults "hls-rendition-groups-getting-ready-to-create.md#hls-rendition-groups-getting-ready-determine-defaults").

## Step 4.

Caption-Only Streams

If your output includes captions, you must create “captions-only” outputs. Follow these
steps for each captions-only output you need:

1. Click **Add Output** in order to create an output.
2. Select or create a stream to be associated with that output.For example, Stream
3.
4. In that stream, delete the default **Video** tab and the
   default **Audio** tab. This stream now contains only a **captions** stream.

For more information on setting up captions, see [Setting Up Captions with AWS Elemental Server](setting-up-captions.md "setting-up-captions.md").

## Step 5. Verify

Outputs for the HLS Rendition Group

- Finally, check all your outputs for the HLS output groups and make sure you do not have
  an output that contains both audio and video. Including such an output may produce a manifest
  that the client player cannot interpret.

## Summary of the Steps

to Create an HLS Rendition Group

After these steps, you have:

- One or more video-only outputs. Each output is associated through its **Audio Rendition Sets** field to one or more audio rendition
  groups.
- Two or more audio-only outputs. Each output belongs to an audio rendition group based
  on the value in the **Audio Group ID** field.
- Optionally, one or more captions-only outputs.

## Example of the Event Output: Creating Caption-Only Streams for an HLS Rendition

Group

Here is the Output section.

![Audio stream configuration interface with multiple output streams and advanced settings.](images/hls-rendition-groups-create-example-output.png)

Here is the Streams section.

![Stream configuration interface showing settings for video, audio, and encoding options.](images/hls-rendition-groups-create-example-streams-1.png)
![Stream configuration interface showing settings for video, audio, and encoding options.](images/hls-rendition-groups-create-example-streams-2.png)
