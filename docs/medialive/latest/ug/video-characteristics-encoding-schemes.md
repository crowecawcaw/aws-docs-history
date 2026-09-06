

# Encoding schemes supported in video outputs in MediaLive
<a name="video-characteristics-encoding-schemes"></a>

**Topics**
+ [Encoding schemes for the AV1 codec](#video-characteristics-encoding-schema-av1)
+ [Encoding schemes for the AVC (H.264) codec](#video-characteristics-encoding-scheme-avc)
+ [Encoding schemes for the HEVC (H.265) codec](#video-characteristics-encoding-scheme-hevc)
+ [Encoding schemes for MPEG-2](#video-characteristics-encoding-scheme-mpeg2)

This section provides information about the encoding schemes that MediaLive supports in the different codecs that are supported in outputs.

## Encoding schemes for the AV1 codec
<a name="video-characteristics-encoding-schema-av1"></a>

The AV1 codec encoding schemes for output video include profile, bit depth, chroma sampling, tier, and level. You can configure the bit depth by setting the **Bit Depth** field to **DEPTH\_8** (8-bit) or **DEPTH\_10** (10-bit). If you don't specify a value, the default is 8-bit. 



- ** Main  **
  - **Bit Depth:**
    - 8-bit 
    - 10-bit 
  - **Chroma Sampling:** 4:2:0 
  - **Tier:** Main 
  - **Level:** All levels indicated in the AV1 specification



## Encoding schemes for the AVC (H.264) codec
<a name="video-characteristics-encoding-scheme-avc"></a>

The AVC (H.264) codec encoding schemes for output video include profile, bit depth, and chroma sampling. In the following table, each row is a different scheme. 


<table>
<thead>
  <tr><th>Profile </th><th>Bit Depth </th><th>Chroma Sampling </th><th>Level</th></tr>
</thead>
<tbody>
  <tr><td>Baseline </td><td>8-bit </td><td>4:2:0 </td><td rowspan="6">All levels indicated in the AVC specification</td></tr>
  <tr><td>Main </td><td>8-bit </td><td>4:2:0 </td></tr>
  <tr><td>High </td><td>8-bit </td><td>4:2:0 </td></tr>
  <tr><td>High </td><td>10-bit </td><td>4:2:0 </td></tr>
  <tr><td>High </td><td>8-bit </td><td>4:2:2 </td></tr>
  <tr><td>High </td><td>10-bit </td><td>4:2:2 </td></tr>
</tbody>
</table>


## Encoding schemes for the HEVC (H.265) codec
<a name="video-characteristics-encoding-scheme-hevc"></a>

The HEVC (H.265) codec encoding schemes for output video include profile, bit depth, chroma sampling, tier, and level. In the following table, each row is a different scheme. 


<table>
<thead>
  <tr><th>Profile </th><th>Bit Depth </th><th>Chroma Sampling </th><th>Tier </th><th>Level</th></tr>
</thead>
<tbody>
  <tr><td>Main </td><td>8-bit </td><td>4:2:0 </td><td>Main </td><td rowspan="4">All levels indicated in the HEVC specification</td></tr>
  <tr><td>Main </td><td>8-bit </td><td>4:2:0 </td><td>High </td></tr>
  <tr><td>Main </td><td>10-bit </td><td>4:2:0 </td><td>Main </td></tr>
  <tr><td>Main </td><td>10-bit </td><td>4:2:0 </td><td>High </td></tr>
</tbody>
</table>


## Encoding schemes for MPEG-2
<a name="video-characteristics-encoding-scheme-mpeg2"></a>

The MPEG-2 codec encoding schemes for output video include profile, bit depth, and chroma sampling. 


|  Profile   |  Bit Depth   |  Chroma Sampling   | 
| --- | --- | --- | 
| Main  | 8-bit  | 4:2:0  | 