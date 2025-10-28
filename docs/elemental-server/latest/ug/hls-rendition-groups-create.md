This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Creating HLS Rendition Groups

The key to creating rendition groups is that each output you create must contain only one
stream. Therefore, for each video to include in the output group, you create a stream assembly
that contains only one video (no audio or captions). For each audio to include in a rendition
group, you create a stream assembly that contains only one audio (no video or captions).

This means that when rendition groups are present in the HLS output group, an output is
identical to a stream. (Usually an output contains a mix of several streams and several stream
types.)

###### Topics

- [Getting Ready to Create HLS
  Rendition Groups](hls-rendition-groups-getting-ready-to-create.md "hls-rendition-groups-getting-ready-to-create.md")
- [Creating HLS Rendition Groups
  (Web Interface)](hls-rendition-groups-create-using-web-interface.md "hls-rendition-groups-create-using-web-interface.md")
- [Creating HLS Rendition Groups (REST
  API)](hls-rendition-groups-create-using-rest-api.md "hls-rendition-groups-create-using-rest-api.md")
