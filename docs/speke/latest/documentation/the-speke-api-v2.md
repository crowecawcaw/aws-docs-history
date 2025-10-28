# SPEKE API v2

This is the REST API for Secure Packager and Encoder Key Exchange (SPEKE) v2. Use this specification to provide DRM copyright protection for customers who use encryption. To be SPEKE-compliant, your DRM key provider must expose the REST API described in this specification. The encryptor makes API calls to your key provider.

###### Note

The code examples in this specification are for illustration purposes only. You can’t run the examples because they aren’t part of a complete SPEKE implementation.

SPEKE uses the DASH Industry Forum Content Protection Information Exchange Format (DASH-IF-CPIX) data structure definition for key exchange, with some restrictions. DASH-IF-CPIX defines a schema to provide an extensible, multi-DRM exchange from the DRM platform to the encryptor. This enables content encryption for all adaptive bitrate packaging formats at the time of content compression and packaging. Adaptive bitrate packaging formats include HLS, DASH, and MSS.

Starting with its version 2.0, SPEKE is aligned on a specific CPIX version:

On the SPEKE side, this is enforced through the use of the `X-Speke-Version` HTTP header, and on the CPIX side through the use of the `CPIX@version` attribute. A lack of these elements in the requests is typical of SPEKE v1 legacy workflows. In SPEKE v2 workflows, the key provider is expected to process CPIX documents only if it supports both version parameters.

For detailed information about the exchange format, see the DASH Industry Forum [CPIX 2.3 specification](https://dashif.org/docs/CPIX2.3/Cpix.html "https://dashif.org/docs/CPIX2.3/Cpix.html").

Overall, SPEKE v2.0 brings the following evolutions compared to SPEKE v1.0:

- All tags from the SPEKE XML namespace are deprecated in favor of equivalent tags in the CPIX XML namespace
- `SPEKE:ProtectionHeader` is deprecated and replaced by `CPIX:DRMSystem.SmoothStreamingProtectionHeaderData`
- `CPIX:URIExtXKey`, `SPEKE:KeyFormat` and `SPEKE:KeyFormatVersions` are deprecated and replaced by `CPIX:DRMSystem.HLSSignalingData`
- `CPIX@id` is replaced by `CPIX@contentId`
- New mandatory CPIX attributes: `CPIX@version`, `ContentKey@commonEncryptionScheme`
- New optional CPIX element: `DRMSystem.ContentProtectionData`
- Support for multiple content keys
- Cross-versioning mechanism between SPEKE and CPIX
- HTTP headers evolution: new `X-Speke-Version` header, `Speke-User-Agent` header renamed into `X-Speke-User-Agent`
- Heartbeat API deprecation
  As the SPEKE v1.0 specification stays unchanged, existing implementations don’t need to change to continue supporting SPEKE v1.0 workflows.

###### Topics

- [SPEKE API v2 - Customizations and constraints to the DASH-IF specification](speke-constraints-v2.md "speke-constraints-v2.md")
- [SPEKE API v2 - Standard payload components](standard-payload-components-v2.md "standard-payload-components-v2.md")
- [SPEKE API v2 - Encryption contract](encryption-contract-v2.md "encryption-contract-v2.md")
- [SPEKE API v2 - Live workflow method call examples](live-workflow-methods-v2.md "live-workflow-methods-v2.md")
- [SPEKE API v2 - VOD workflow method call examples](vod-workflow-method-v2.md "vod-workflow-method-v2.md")
- [SPEKE API v2 - Content key encryption](content-key-encryption-v2.md "content-key-encryption-v2.md")
- [SPEKE API v2 - Overriding the key identifier](kid-override-v2.md "kid-override-v2.md")
