# Format of an SDP file for audio

```
v=0
o=- 1443716955 1443716955 IN IP4 10.xx.xxx.236
s=st2110 0-1-0
t=0 0
m=audio 20000 RTP/AVP 97
c=IN IP4 239.x.x.x/64
a=source-filter: incl IN IP4 239.x.x.x 10.xx.xxx.236
a=rtpmap:97 L24/48000/2
a=mediaclk:direct=0 rate=48000
a=framecount:48
a=ptime:1
a=ts-refclk:ptp=IEEE1588-2008:04-5c-6c-ff-fe-0a-53-70:127
```

Following is information about the data in this example:

- `o=` This line identifies the source IP for the stream
- `m=audio`. This identifies the file as an audio description.
  `20000` is the port of the stream. This line must occur before the
  `a` lines.
- `c=` identifies the destination IP address. This is a unicast or
  multicast address.
- `a=source-filter` identifies a filter. This line is optional.

In a file for an input to Elemental Live:

    + If the line is included, Elemental Live will listen only to the source IP
     (10.xx.xxx.236) for packets.
    + If the line isn't included, Elemental Live will listen to any packets on the
     destination IP address (239.x.x.x).

In a file for an output: Elemental Live always includes this line in any SDP file that
it creates.

- **a=rtpmap** provides information about the audio
  format:
  - An example for PCM:

  `a=rtpmap:97 L24/48000/2`

  `L24` is the number of bits per PCM audio sample.
  `48000` is the sample rate. `2` is the number of
  channels, in this example, a single stereo track.
  - An example for a Dolby Digital codec:

  `a=rtpmap:96 AM824/48000/5 a=fmtp:96
 channel-order=SMPTE2110.(AES3,AES3)`

  `48000` is the sample rate. `6` is the number of
  AM824 subframe pairs, and must be an even number.
