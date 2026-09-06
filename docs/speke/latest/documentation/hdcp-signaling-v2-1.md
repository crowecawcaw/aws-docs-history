# SPEKE API v2.1 - HDCP signaling

In SPEKE v2.1, the key provider can return High-bandwidth Digital Content Protection (HDCP) output protection information for a content key. The encryptor uses this information to signal the required HDCP level to players in the manifest or playlist that it produces.

The key provider returns this information in the `<cpix:HDCPData>` element, which is a child of the `<cpix:ContentKey>` element. The `<cpix:HDCPData>` element supports the following:

- The `@HLSHDCPLevel` attribute specifies the value of the `HDCP-LEVEL` attribute of the `EXT-X-STREAM-INF` tag in the HLS multivariant playlist. This attribute has meaning only when an HLS playlist is created for the media content.
- The `<cpix:HDCPOutputProtectionData>` child element is the well-formed standalone XML fragment to be added to the DASH manifest for the HDCP `OutputProtection` element for this content key. This element has meaning only when a DASH manifest is created for the media content.
  For more information about these elements, see the [CPIX 2.4 specification](https://dashif.org/docs/CPIX2.4/Cpix.html "https://dashif.org/docs/CPIX2.4/Cpix.html") on the DASH-IF website.
