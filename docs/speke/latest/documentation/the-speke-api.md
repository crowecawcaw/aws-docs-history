# SPEKE API v1

This is the REST API for Secure Packager and Encoder Key Exchange (SPEKE) v1. Use this specification to provide DRM copyright protection for customers who use encryption. To be SPEKE-compliant, your DRM key provider must expose the REST API described in this specification. The encryptor makes API calls to your key provider.

###### Note

The code examples in this specification are for illustration purposes only. You can’t run the examples because they aren’t part of a complete SPEKE implementation.

SPEKE uses the DASH Industry Forum Content Protection Information Exchange Format (DASH-IF-CPIX) data structure definition for key exchange, with some restrictions. DASH-IF-CPIX defines a schema to provide an extensible, multi-DRM exchange from the DRM platform to the encryptor. This enables content encryption for all adaptive bitrate packaging formats at the time of content compression and packaging. Adaptive bitrate packaging formats include HLS, DASH, and MSS.

For detailed information about the exchange format, see the DASH Industry Forum CPIX specification at https://dashif.org/docs/DASH-IF-CPIX-v2-0.pdf.

###### Topics

- [SPEKE API v1 - Customizations and constraints to the DASH-IF specification](speke-constraints.md "speke-constraints.md")
- [SPEKE API v1 - Standard payload components](standard-payload-components.md "standard-payload-components.md")
- [SPEKE API v1 - Live workflow method call examples](live-workflow-methods.md "live-workflow-methods.md")
- [SPEKE API v1 - VOD workflow method call examples](vod-workflow-methods.md "vod-workflow-methods.md")
- [SPEKE API v1 - Content key encryption](content-key-encryption.md "content-key-encryption.md")
- [SPEKE API v1 - Heartbeat](heartbeat.md "heartbeat.md")
- [SPEKE API v1 - Overriding the key identifier](kid-override.md "kid-override.md")
