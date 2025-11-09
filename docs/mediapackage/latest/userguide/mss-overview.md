# MSS in AWS Elemental MediaPackage

AWS Elemental MediaPackage supports Microsoft Smooth Streaming (MSS) for delivering content to legacy
devices such as smart TVs and other platforms where MSS is the preferred or required
streaming format. This topic provides an overview of MSS and how it works with MediaPackage.

MSS remains important for reaching legacy devices and platforms that don't support newer
protocols, even though HLS and DASH are more common in modern streaming environments.

Similar to other adaptive bitrate streaming protocols like HLS and DASH, MSS dynamically
adjusts the quality of a video stream based on network conditions and device capabilities.
The key difference is that MSS uses a different format and structure for its manifests and
segments, and it was developed by Microsoft specifically for their platforms (like
Silverlight, Xbox, etc.).

## When to use MSS

MSS is particularly valuable in the following scenarios:

- **Legacy device support**: If your audience uses
  older smart TVs, set-top boxes, or gaming consoles (particularly Xbox 360) that
  only support MSS, this format is essential for reaching those viewers.
- **Corporate environments**: Many enterprise
  environments standardized on Microsoft technologies, including Silverlight-based
  players, and may not have updated their infrastructure to support newer
  protocols.
- **Multi-protocol strategy**: For maximum audience
  reach, content providers often implement a multi-protocol strategy where the
  same content is available in HLS, DASH, and MSS formats, allowing the client to
  use whichever format it supports best.
- **Regions with older device penetration**: In
  some geographic regions, older devices with MSS support remain common, making
  this format important for reaching those markets.

## Choosing the right streaming protocol for your

audience

To reach the widest possible audience, select the appropriate streaming protocols
based on your viewers' devices. This section helps you decide when to use MSS versus
other protocols.

### Protocol selection guide

Use this guide to determine which protocols you need to implement:

1. **Identify your audience's devices**: Survey
   your target audience to understand what devices they use to consume your
   content.
2. **Check device compatibility**: If your
   audience includes any of these devices, consider implementing MSS:
   - Xbox 360 consoles
   - Legacy smart TVs (especially older Samsung and LG models)
   - Devices with Microsoft Silverlight players
   - Corporate environments with standardized Microsoft
     infrastructure

3. **Evaluate audience reach vs. implementation
   cost**: Determine what percentage of your audience requires MSS
   support and whether the additional implementation effort is
   justified.
4. **Consider a multi-protocol approach**: For
   maximum audience reach, implement multiple protocols and use device
   detection to serve the appropriate format.

### Protocol comparison for

implementation planning

This comparison helps you understand the key differences between streaming
protocols to plan your implementation:

| Streaming Protocol Comparison | Feature                            | MSS                         | HLS                                  | DASH |
| ----------------------------- | ---------------------------------- | --------------------------- | ------------------------------------ | ---- |
| Developer                     | Microsoft                          | Apple                       | MPEG                                 |
| Year introduced               | 2008                               | 2009                        | 2012                                 |
| Manifest format               | XML                                | M3U8 (text)                 | XML (MPD)                            |
| Segment format                | MP4 (ISM)                          | TS or fMP4                  | MP4                                  |
| DRM support                   | PlayReady only                     | FairPlay, AES-128           | Multiple (Widevine, PlayReady, etc.) |
| Device support                | Xbox, Silverlight, older smart TVs | iOS, macOS, newer smart TVs | Android, browsers, newer smart TVs   |
| Industry adoption             | Limited (legacy)                   | Widespread                  | Growing                              |

### Common implementation

scenarios

Based on your audience needs, consider these common implementation
scenarios:

Modern devices only

If your audience exclusively uses modern devices (smartphones,
tablets, newer smart TVs, modern browsers):

- **Recommended**: HLS and
  DASH
- **Not needed**: MSS

Mixed device ecosystem

If your audience uses a mix of modern and legacy devices:

- **Recommended**: HLS, DASH, and
  MSS
- **Implementation approach**: Use
  device detection at the CDN level to route viewers to the
  appropriate format

Corporate/Enterprise environments

If delivering to corporate environments with standardized Microsoft
infrastructure:

- **Recommended**: MSS (primary)
  with HLS/DASH as alternatives
- **Implementation approach**:
  Optimize for MSS playback while providing alternatives for BYOD
  scenarios

While HLS and DASH are now the dominant streaming protocols for modern devices,
MSS continues to play an important role in comprehensive streaming strategies that
aim to reach the widest possible audience.

## Planning your MSS implementation

When you plan your MSS implementation in MediaPackage, you need to understand the technical
requirements and considerations to ensure successful delivery to legacy devices.

### Technical requirements

Make sure your implementation meets these technical requirements:

- **Container type**: MSS requires the ISM
  container type. You cannot use CMAF or TS containers with MSS
  manifests.
- **Encryption**: Only CENC encryption with
  PlayReady DRM is supported for MSS content. Key rotation is not
  supported.
- **Audio codecs**: MSS typically uses AAC
  audio with the AACL FourCC code.
- **Video codecs**: MSS typically uses H.264
  video with the H264 FourCC code.

### Implementation options

When you configure your MSS endpoints, consider these options:

- **Manifest layouts**: Choose between:
  - **Full layout**: Better compatibility
    with older players but larger manifest size
  - **Compact layout**: Uses the
    FragmentRepeat field to significantly reduce manifest size for
    streams with consistent segment durations

- **Subtitles**: If you need subtitles, use
  TTML format as MSS does not support WebVTT.

### Implementation limitations

Be aware of these limitations when you plan your MSS implementation:

- **SCTE-35**: MSS endpoints do not support
  SCTE-35 message passthrough or ad marker insertion. If you need ad
  insertion, consider server-side ad insertion before packaging.
- **DRM options**: Only PlayReady DRM is
  supported. Key rotation is not supported for MSS content. If you need
  multi-DRM support, you'll need to implement additional protocols alongside
  MSS.
- **Subtitle formats**: Limited to TTML
  subtitles only.

### Implementation checklist

Use this checklist when you plan your MSS implementation:

1. Verify your source content is compatible with MSS requirements (codecs,
   container)
2. Decide on manifest layout based on your audience's devices (Full for
   maximum compatibility, Compact for efficiency)
3. Understand that LookaheadCount is fixed at 2 and plan your segment
   duration accordingly for desired latency
4. If encryption is needed, set up a SPEKE key provider for PlayReady
   DRM
5. Configure your CDN with appropriate cache settings and MIME types for MSS
   content
6. Test playback on representative devices from your target audience

For step-by-step instructions on creating MSS endpoints, see [Create an MSS manifest](endpoints-create.md#endpoints-ism "endpoints-create.md#endpoints-ism").

## MSS use cases

Consider using MSS endpoints in the following scenarios:

- Delivering content to legacy smart TVs and devices that only support
  MSS
- Supporting Microsoft platforms where MSS is the preferred streaming
  format
- Creating multi-protocol streaming workflows that need to include MSS alongside
  other formats
- Broadcasting to regions where older devices with MSS support are still
  common
- Supporting Xbox 360 and other legacy Microsoft gaming consoles
- Providing content to corporate environments that standardized on Microsoft
  Silverlight-based players

Here's a real-world example of MSS implementation:

###### Example Broadcasting sports events to multiple device types

A major sports broadcaster needed to stream live events to viewers using a wide
range of devices, from modern smartphones to older smart TVs and gaming consoles.
They implemented a multi-protocol strategy using MediaPackage to create:

- HLS endpoints for iOS devices and newer smart TVs
- DASH endpoints for Android devices and modern browsers
- MSS endpoints for Xbox 360 consoles and older Samsung smart TVs
  By including MSS in their delivery strategy, they were able to reach an additional
  15% of their audience who were using legacy devices that didn't support newer
  protocols. The broadcaster configured their CDN to route viewers to the appropriate
  format based on device detection, ensuring optimal playback for all viewers
  regardless of their device.

For information about testing MSS playback on compatible devices, see [Testing MSS playback in AWS Elemental MediaPackage](mss-testing-playback.md "mss-testing-playback.md").

The following sections provide more information about using MSS with MediaPackage.

###### Topics

- [MSS manifest structure in AWS Elemental MediaPackage](mss-manifest-structure.md "mss-manifest-structure.md")
- [MSS encryption and DRM in AWS Elemental MediaPackage](mss-encryption.md "mss-encryption.md")
- [Testing MSS playback in AWS Elemental MediaPackage](mss-testing-playback.md "mss-testing-playback.md")
- [Troubleshooting MSS endpoints in AWS Elemental MediaPackage](mss-troubleshooting.md "mss-troubleshooting.md")
- [CDN configuration for MSS in AWS Elemental MediaPackage](mss-cdn-configuration.md "mss-cdn-configuration.md")
