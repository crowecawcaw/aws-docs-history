# About SDP files

The SMPTE 2110 specification relies on SDP files to describe the contents of the SMPTE
2110 streams. There is one file for each type of stream. The file for each stream contains
the following information:

- The source IP address for the file. This is an address that the sender
  controls.
- The unicast or multicast address that the receiver can connect to, in order to
  obtain the content.
- Descriptions of the media in the stream.
  **SDP files for content into Elemental Live**

For SMPTE 2110 inputs, Elemental Live is the receiver and the upstream system is the
sender.

- Typically, the sender (the upstream system) is responsible for creating the
  _source SDP file_.

If the sender hasn't created the file, or if your organization is the originator
of the stream and the file wasn't created by an automated system, then you can create
the file. For more information, see About SDP files.

- If the source SMPTE 2110 streams aren't managed by NMOS, the source SDP files must
  be stored on a server that Elemental Live can access using HTTP. You and the sender should
  agree on a suitable location.
- If the source SMPTE 2110 streams are being managed by NMOS, you should have
  already set up the stream in the NMOS registry.
  **SDP files for output from Elemental Live**

For SMPTE 2110 outputs, Elemental Live is the sender and the downstream system is the
receiver.

- Elemental Live always generates the applicable _output SDP
  files_ and places them on a directory on the appliance.
- If the SMPTE 2110 output group doesn't use NMOS, you must make the output SDP
  files available to the receiver. The files must be on an HTTP server that the
  receiver can access. For information about obtaining the SDP files, see [Step 4: Download and post the SDP file](locate-sdp.md "locate-sdp.md").
- If the SMPTE 2110 output group does use NMOS, Elemental Live handles delivery of the output
  SDP files available to the NMOS registry. There is nothing you need to do with the
  files.
  The following topics describe the format of each type of SDP file, using
  examples.

###### Note

You are responsible for understanding the SMPTE 2110 specification. We provide the
examples below only as a courtesy. Refer to the specification for complete information
about the SDP file.

###### Topics

- [Format of an SDP file for video](2120-sdp-video.md "2120-sdp-video.md")
- [Format of an SDP file for audio](2120-sdp-audio.md "2120-sdp-audio.md")
- [Format of an SDP file for ancillary data](2120-sdp-ancillary.md "2120-sdp-ancillary.md")
- [SDP file with 2022-7 information](2120-sdp-2022-7.md "2120-sdp-2022-7.md")
