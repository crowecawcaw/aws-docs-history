# MSS encryption and DRM in AWS Elemental MediaPackage

This topic explains how to protect your Microsoft Smooth Streaming (MSS) content using
encryption and digital rights management (DRM) in AWS Elemental MediaPackage. For information about MSS
manifest structure and how encryption affects it, see [MSS manifest structure in AWS Elemental MediaPackage](mss-manifest-structure.md "mss-manifest-structure.md"). For general information about MSS in MediaPackage,
see [MSS in AWS Elemental MediaPackage](mss-overview.md "mss-overview.md").

MSS encryption in MediaPackage supports PlayReady DRM only. Other DRM systems are not supported for MSS content.

## Understanding MSS encryption

requirements

When encrypting MSS content in MediaPackage, note the following requirements and
limitations:

- **DRM system**: Only PlayReady DRM is supported
  for MSS content
- **Encryption method**: The encryption method must
  be CENC (Common Encryption)
- **PlayReady header**: The PlayReady header is
  inserted at the top level of the manifest
- **Key rotation and constant IV**: Key rotation
  and constant IV (Initialization Vector) are not supported for MSS content
- **CPIX requirements**: Your key server must
  provide a `smoothProtectionHeaderData` element in the CPIX response
  so that MediaPackage can insert it in the manifest. For more information about CPIX,
  see the [CPIX documentation](https://docs.unified-streaming.com/documentation/drm/cpix_intro.html "https://docs.unified-streaming.com/documentation/drm/cpix_intro.html").
- **Shared DRM presets**: Video and audio presets
  must be set to SHARED because MSS uses the same DRM information across the
  manifest for video, audio, and subtitle segments

For information about how these encryption options affect your CDN configuration, see
[CDN configuration for MSS in AWS Elemental MediaPackage](mss-cdn-configuration.md "mss-cdn-configuration.md"). For
details on planning your MSS implementation with encryption, see [Planning your MSS implementation](mss-overview.md#mss-features "mss-overview.md#mss-features").

## Encrypting your MSS content with

PlayReady

To encrypt your MSS content:

1. When creating or editing your endpoint, select **Encrypt
   content** in the Encryption section.
2. For **Encryption method**, select
   **CENC**.
3. For **DRM systems**, select
   **PlayReady**.
4. Ensure that video and audio presets are set to **SHARED**
   because MSS uses the same DRM information across all segments.
5. Complete the remaining encryption fields as described in [Encryption fields](endpoints-create.md#endpoints-encryption "endpoints-create.md#endpoints-encryption").

## PlayReady DRM for MSS

PlayReady is Microsoft's DRM technology and is the only supported DRM system for MSS
content. When using PlayReady with MSS:

- The PlayReady header is included in the MSS manifest in the
  `Protection` element
- The PlayReady SystemID is
  `9a04f079-9840-4286-ab92-e65be0885f95`
- The encryption keys are provided by your SPEKE key provider

For more information about configuring SPEKE with MediaPackage, see [Content encryption and DRM in AWS Elemental MediaPackage](using-encryption.md "using-encryption.md").

## Key server requirements

When setting up a key server for MSS content, ensure that:

- The key server has the correct headers that match what is present in the PSSH box
- The UUIDs are properly configured
- Request information is in SOAP/HTTP format. MSS uses the same information consistently across all components - the manifest, key service, audio streams, and video streams all share the same request format and authentication details

For more information about requirements for using PlayReady with MSS, see [Microsoft PlayReady documentation](https://docs.microsoft.com/en-us/playready/packaging/mp4-based-formats-supported-by-playready-clients "https://docs.microsoft.com/en-us/playready/packaging/mp4-based-formats-supported-by-playready-clients                 ").

Unlike some other streaming protocols that may use different authentication or request formats for different components, MSS maintains consistency across all elements. This means that once you configure the SOAP/HTTP request format for your key server, the same format and authentication approach will be used whether the player is requesting the manifest, contacting the key service, or accessing audio and video streams.

## MSS encryption limitations

MSS encryption has the following limitations:

- Key rotation is not supported
- Constant IV (Initialization Vector) is not supported

## Verifying your encrypted MSS streams

To test your encrypted MSS content:

1. Use the Castlabs Demo Player at [https://demo.castlabs.com/](https://demo.castlabs.com/ "https://demo.castlabs.com/") for testing PlayReady encrypted MSS
   content
2. Enter your MSS endpoint URL
3. If your content is encrypted with PlayReady DRM, verify that the player can
   decrypt and play the content. Use the Castlabs player specifically for encrypted
   content. Other players might not work reliably with PlayReady encrypted MSS
   streams.

For production environments, ensure your players and devices are properly configured
to handle PlayReady-protected content.

For comprehensive testing procedures and compatible players for MSS content, see [Testing MSS playback in AWS Elemental MediaPackage](mss-testing-playback.md "mss-testing-playback.md").
