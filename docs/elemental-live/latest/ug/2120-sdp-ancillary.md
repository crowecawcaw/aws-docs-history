# Format of an SDP file for ancillary data

```
v=0
o=- 1443716955 1443716955 IN IP4 10.xx.xxx.236
s=st2110 0-9-0
t=0 0
m=video 20000 RTP/AVP 100
c=IN IP4 239.x.x.xx/64
a=source-filter: incl IN IP4 239.x.x.xx 10.xx.xxx.236
a=rtpmap:100 smpte291/90000
a=fmtp:100 VPID_Code=133;
a=mediaclk:direct=0 rate=90000
a=ts-refclk:ptp=IEEE1588-2008:04-5c-6c-ff-fe-0a-53-70:127
```

Following is information about the data in this example:

- `o=` This line identifies the source IP for the stream
- `m=` The combination of `m=video` and
  `smpte291` (in the `a=rtpmap:` line) identifies this file
  as an ancillary data file. `20000` is the port of the stream. This line
  must occur before the `a` lines.
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
