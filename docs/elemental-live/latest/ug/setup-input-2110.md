# Setting up a SMPTE 2110 input without NMOS

Follow this procedure if you have a SMPTE 2110 source and your organization doesn't use
[NMOS IS-04 and IS-05](2110-and-nmos.md "2110-and-nmos.md").

###### Note

This section assumes that you have read [Working with SMPTE 2110](SMPTE-ST-2110.md "SMPTE-ST-2110.md") and are
familiar with how SMPTE 2110 works and with its prerequisites.

When your organization doesn't use NMOS, you must provide
information about the SDP that applies to this source, so that Elemental Live
can extract content correctly. For example, you must specify where the
SDP file for the video is located, and identify the specific video
streams to ingest. In addition, if you are using seamless protection
switching, you must configure two interfaces for traffic.

Elemental Live supports ingest of SMPTE 2110 sources that implement SMPTE 2022-7. In this case,
you can configure the input to ingest one or both instances of the source.

###### Note

The information in this section assumes that you are familiar
with the general steps for creating an event.

To set up a SMPTE 2110 input

1. From the **Input** menu in the event, select **SMPTE 2110
   Input**.
2. In **Video SDP Location**, enter
   the location of the SDP file for the video. For example:

[http://172.18.8.19/curling_video.sdp](rtp://239.255.100.100:5000 "rtp://239.255.100.100:5000")

For more information about SDP files, see [About SDP files](2110-sdp-about.md "2110-sdp-about.md"). 3. In **Media Index**, enter the index of the
video stream that you want Elemental Live to extract. For example, enter
`0` if the video is the first stream,
`1` if it's the second stream, and so
on. 4. Complete the **Interface** fields:

    * **Interface**: Enter the network interface for this stream
     to connect to the Elemental Live node. For example, `eth4`.
    * **Secondary Interface**: If you want to implement SMPTE
     2022-7 , enter the interface for the secondary source. For example,
     `eth5`.

In either case, choose the interface carefully. In Elemental Live, network interfaces are
shared across events. Be careful not to overload the capacity of an interface. 5. Complete the audio fields in the same way – **Audio
SDP Location**, **Media Index**, and
**Interface** fields.

Keep in mind that you can support SMPTE 2022-7 for some
streams and not for others. 6. If the source includes an ancillary data stream, choose
**Add Ancillary SDP +**. Complete the
**Ancillary SDP Location**, **Media
Index**, and **Interface**
fields.
