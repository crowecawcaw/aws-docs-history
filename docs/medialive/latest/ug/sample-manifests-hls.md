# Sample manifests - HLS

MediaLive supports the following HLS manifest styles for outputs:

- Adobe
- Elemental
- SCTE 35 Enhanced
  This section describes the ad marker tagging for each style of output
  manifest.

###### Note

MediaLive doesn't interpret the ad avail decoration information in the manifest
attached to the input source.

## Ad marker: Adobe

Inserts a CUE: DURATION for each ad avail. Does not insert any CUE-OUT CONT
(continuation tags) to indicate to a client player joining midbreak that there
is a current avail. This does not insert a CUE-IN tag at the end of the
avail.

**Structure**

| Segment                               | Tag                 | Tag Count |
| ------------------------------------- | ------------------- | --------- |
| Segment in which the ad avail starts. | 1 CUE: DURATION tag | 1         |

**Tag contents**

- CUE:DURATION contains the following:
  - duration – Duration in fractional
    seconds
  - id – An identifier, unique among all ad
    avails CUE tags
  - type – SpliceOut
  - time – The PTS time for the ad avail, in
    fractional seconds

**Example**

This is the tag for an ad avail lasting 414.171 PTS:

```
#EXT-X-CUE:DURATION="201.467",ID="0",TYPE="SpliceOut",TIME="414.171"
```

## Ad marker: Elemental

**Structure**

| Segment                               | Tag          | Tag Count |
| ------------------------------------- | ------------ | --------- |
| Segment in which the ad avail starts. | CUE-OUT      | 1         |
| Each succeeding segment.              | CUE-OUT-CONT | 0-n       |
| Segment in which ad avail ends.       | CUE-IN       | 1         |

**Tag contents**

- CUE-OUT contains DURATION
- CUE-OUT-CONT contains Elapsed time and Duration
- CUE-IN has no content

**Example**

```
#EXT-X-CUE-OUT:30.000
.
.
.
# EXT-X-CUE-OUT-CONT: 8.308/30
.
.
.
# EXT-X-CUE-OUT-CONT: 20.391/30
.
.
.
# EXT-X-CUE-IN
```

## Ad marker: SCTE 35

enhanced

Structure

| Segment                               | Tag           | Tag Count |
| ------------------------------------- | ------------- | --------- |
| Segment in which the ad avail starts. | OATCLS-SCTE35 | 1         |
| Segment in which the ad avail starts. | ASSET         | 1         |
| Segment in which the ad avail starts. | CUE-OUT       | 1         |
| Each succeeding segment.              | CUE-OUT-CONT  | 0-n       |
| Segment in which ad avail ends.       | CUE-IN        | 1         |

Tag contents

- OATCLS-SCTE35 containing the base64 encoded raw bytes of
  the original SCTE 35 ad avail message.
- ASSET containing the CAID or UPID as specified in the
  original SCTE35 message.
- 1 CUE-OUT per ad avail.
- CUE-OUT-CONT containing the following:
  - The elapsed time of the avail.
  - The duration declared in the original SCTE35
    message.
  - SCTE35 containing the base64 encoded raw bytes of
    the original SCTE 35 ad avail message.

  These lines repeat until the ad avail ends.

- CUE-IN to indicate the end of the avail.

Example

```
#EXT-OATCLS-SCTE35:/DA0AAAAAAAAAAAABQb+ADAQ6QAeAhxDVUVJQAAAO3/PAAEUrEoICAAAAAAg+2UBNAAANvrtoQ==
#EXT-X-ASSET:CAID=0x0000000020FB6501
#EXT-X-CUE-OUT:201.467
.
.
.
#EXT-X-CUE-OUT-CONT:ElapsedTime=5.939,Duration=201.467,SCTE35=/DA0AAAA+…AAg+2UBNAAANvrtoQ==
.
.
.
#EXT-X-CUE-IN
```
