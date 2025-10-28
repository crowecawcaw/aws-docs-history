This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Rules for Rendition Groups

Rules exist for associating both audio and video streams in their respective rendition
groups. These are described following.

- A given audio stream can belong to only one audio rendition group.
- Any given video stream can be associated with more than one rendition group. (For example,
  “video high” can be associated with both “Dolby audio streams” and “AAC audio streams.” You do
  not need to create two video streams.)

With this setup, all the rendition groups associated with the same video stream must
contain the same audio streams.( For example, “Dolby audio streams” and “AAC audio streams”
must contain the same audio streams (perhaps English, French and Spanish)).

- Any given audio rendition group can be associated with more than one video stream.( For
  example, “Dolby audio streams” rendition group can be associated with “video high” and “video
  low.” You do not need to create two rendition groups, one for each video.)
- Any video stream can be associated with more than one output group. (For example, “video
  high” can appear in two different HLS output groups).
  You can use a combination of these rules. For more information, see [Examples of HLS Rendition Groups](hls-rendition-groups-examples.md "hls-rendition-groups-examples.md").
