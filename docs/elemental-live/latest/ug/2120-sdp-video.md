# Format of an SDP file for video

```
v=0
o=- 3826217993 3826217993 IN IP4 10.xx.xxx.198
s=AWS Elemental SMPTE 2110 Output: [LiveEvent: 13] [OutputGroup: smpte_2110]
   [EssenceType_ID: 2110-20_video_198]
t=0 0
m=video 50000 RTP/AVP 96
c=IN IP4 239.x.x.x/64
b=AS:2568807
a=source-filter: incl IN IP4 239.x.x.x `10.xx.xxx.2`
a=rtpmap:96 raw/90000
a=fmtp:96 sampling=YCbCr-4:2:2; width=1920; height=1080;
   exactframerate=60; depth=10; TCS=SDR; colorimetry=BT709;
   interlaced; PM=2110GPM; SSN=ST2110-20:2017; TP=2110TPN; PAR=1:1;
a=mediaclk:direct=0
a=ts-refclk:localmac=1c-34-da-5a-be-34
```

Following is information about the data in this example:

- `o=` This line identifies the source IP for the stream
- `m=video`. This identifies the file as a video description.
  `50000` is the port of the stream. This line must occur before the
  `b` and `a` lines..
- `c=` identifies the destination IP address. This is a unicast or
  multicast address.
- `b=AS:2568807` is the bandwidth in kilobytes, and applies only for
  JPEG XS.
- `a=source-filter` identifies a filter. This line is optional.

In a file for an input to Elemental Live:

    + If the line is included, Elemental Live will listen only to the source IP
     (10.xx.xxx.2) for packets.
    + If the line isn't included, Elemental Live will listen to any packets on the
     destination IP address (239.x.x.x).

In a file for an output: Elemental Live always includes this line in any SDP file that
it creates.

- `Width` and `height` together specify the resolution.
- `Exactframerate` specifies the frames per second (fps).
- `Raw` is the video compression—`raw` for uncompressed
  video, `jxsv` for JPEG XS.
- `90000` is the frequency.
