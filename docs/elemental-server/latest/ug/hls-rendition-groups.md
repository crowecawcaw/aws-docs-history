This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Setting up HLS Rendition Groups

In AWS Elemental Server, you can set up an HLS output group to support
an audio rendition group.

In setting up an HLS output group to support an audio rendition group, each HLS output you
create contains a “set” consisting of one video stream and several audio streams. All the audio
streams in the set are associated with that one video stream. The HLS output group can contain
more than one of these outputs. For example, one set consisting of high bitrate video and audio in
four languages and another set consisting of low bitrate video and audio in the same four
languages.

With this setup, the manifest that is created provides options for video. The logic of the
manifest allows the player to select one of those video options and then to select audio that is
valid for that video option.

For example:

1. The client player reads the manifest and selects the desired video, such as a high bitrate
   video.
2. The client player then selects an audio group from among the groups associated with that
   video, such as the Dolby Digital group instead of the AAC group.
3. The client player then selects an audio from that group, such as Spanish.

Typically, the player makes its audio selection based on rules on the player side, such as
selecting the language that corresponds to the operating system language, or based on rules
defined in the manifest, such as when the manifest identifies one audio as the default.
**Standards Compliance**

This implementation of audio rendition groups is compliant with the “HTTP Live Streaming
draft-pantos-http-live-streaming-18” section 4.3.4.1.1.

Note that AWS Elemental Server does not support rendition groups for video. They do
support rendition groups for captions since AWS Elemental Server automatically creates one captions
rendition group to hold all caption stream assemblies in a given output.

###### Topics

- [How
  Video Is Associated with Audio Rendition Groups](hls-rendition-groups-how-video-is-associated-with-audio-rendition-groups.md "hls-rendition-groups-how-video-is-associated-with-audio-rendition-groups.md")
- [Rules for Rendition Groups](hls-rendition-groups-rules.md "hls-rendition-groups-rules.md")
- [Examples of HLS Rendition Groups](hls-rendition-groups-examples.md "hls-rendition-groups-examples.md")
- [Creating HLS Rendition Groups](hls-rendition-groups-create.md "hls-rendition-groups-create.md")
- [Sample HLS Output Group with Audio
  Rendition Group Event Manifest](hls-rendition-groups-sample-manifest.md "hls-rendition-groups-sample-manifest.md")
