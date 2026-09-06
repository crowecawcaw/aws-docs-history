

# SPEKE API v2.1
<a name="the-speke-api-v2-1"></a>

This is the REST API for Secure Packager and Encoder Key Exchange (SPEKE) v2.1. Use this specification to provide DRM copyright protection for customers who use encryption. To be SPEKE-compliant, your DRM key provider must expose the REST API described in this specification. The encryptor makes API calls to your key provider.

**Note**  
The code examples in this specification are for illustration purposes only. You can’t run the examples because they aren’t part of a complete SPEKE implementation.

SPEKE v2.1 is a minor revision of SPEKE v2.0 that aligns with the DASH Industry Forum [CPIX 2.4 specification](https://dashif.org/docs/CPIX2.4/Cpix.html) on the DASH-IF website. A SPEKE v2.1 request is a SPEKE v2.0 request with the additions described in [Changes from SPEKE v2.0](changes-from-v2-0-v2-1.md). All SPEKE v2.0 behavior that is not listed as a change applies to SPEKE v2.1 without modification.

As with SPEKE v2.0, the `X-Speke-Version` HTTP request header indicates the version on the SPEKE side. The `CPIX@version` attribute indicates the version on the CPIX side. For SPEKE v2.1, the encryptor sends `X-Speke-Version` value `2.1` and `CPIX@version` value `2.4`. If the key provider does not support the SPEKE version used by the encryptor, it returns an error with description 'Unsupported SPEKE version' and does not process the CPIX document.

**Topics**
+ [SPEKE API v2.1 - Changes from SPEKE v2.0](changes-from-v2-0-v2-1.md)
+ [SPEKE API v2.1 - Customizations and constraints to the DASH-IF specification](speke-constraints-v2-1.md)
+ [SPEKE API v2.1 - Standard payload components](standard-payload-components-v2-1.md)
+ [SPEKE API v2.1 - Encryption contract](encryption-contract-v2-1.md)
+ [SPEKE API v2.1 - Live workflow method call examples](live-workflow-methods-v2-1.md)
+ [SPEKE API v2.1 - VOD workflow method call examples](vod-workflow-method-v2-1.md)
+ [SPEKE API v2.1 - Content key encryption](content-key-encryption-v2-1.md)
+ [SPEKE API v2.1 - Overriding the key identifier](kid-override-v2-1.md)
+ [SPEKE API v2.1 - HDCP signaling](hdcp-signaling-v2-1.md)