# Example manifests for Apple

HLS

This section lists example manifests for the Apple HLS manifest styles that AWS
Elemental supports.

## Example manifest

for Adobe ad marker

This does not insert any CUE-OUT CONT (continuation tags) to indicate to a player
joining mid-break that there is a current avail. This does not insert a CUE-IN tag at
the end of the avail.

**Structure**

| Segment                               | Tag                 | Tag Count |
| ------------------------------------- | ------------------- | --------- |
| Segment in which the ad avail starts. | 1 CUE: DURATION tag | 1         |

**Tag contents**

- CUE:DURATION containing:
  - duration: Duration in fractional seconds.
  - id: An identifier, unique among all ad avails CUE tags.
  - type: SpliceOut
  - time: The PTS time for the ad avail, in fractional seconds.

The following is the tag for an ad avail lasting 414.171 PTS.

```
#EXT-X-CUE:DURATION="201.467",ID="0",TYPE="SpliceOut",TIME="414.171"
```

## Example

manifest for AWS Elemental ad marker

**Structure**

| Segment                              | Tag          | Tag Count |
| ------------------------------------ | ------------ | --------- |
| Segment in which the ad avail starts | CUE-OUT      | 1         |
| Each succeeding segment              | CUE-OUT-CONT | 0-n       |
| Segment in which ad avail ends       | CUE-IN       | 1         |

**Tag contents**

- CUE-OUT contains Duration.
- CUE-OUT-CONT contains Elapsed time and Duration.
- CUE-IN has no content.

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

## Example manifest for SCTE-35 enhanced ad marker

**Structure**

| Segment                              | Tag           | Tag Count |
| ------------------------------------ | ------------- | --------- |
| Segment in which the ad avail starts | OATCLS-SCTE35 | 1         |
| Segment in which the ad avail starts | ASSET         | 1         |
| Segment in which the ad avail starts | CUE-OUT       | 1         |
| Each succeeding segment              | CUE-OUT-CONT  | 0-n       |
| Segment in which ad avail ends       | CUE-IN        | 1         |

**Tag contents**

- OATCLS-SCTE35 containing the base-64-encoded raw bytes of the original SCTE-35
  ad avail message.
- ASSET containing the CAID or UPID as specified in the original SCTE35
  message.
- 1 CUE-OUT per ad avail.
- CUE-OUT-CONT containing:
  - The elapsed time of the avail.
  - The duration declared in the original SCTE35 message.
  - SCTE35 containing the base-64-encoded raw bytes of the original SCTE-35
    ad avail message.

  These lines repeat until the ad avail ends.

- CUE-IN to indicate the end of the avail.

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
