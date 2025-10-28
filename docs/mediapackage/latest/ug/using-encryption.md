# Content encryption and DRM in AWS Elemental MediaPackage

Protect your content from unauthorized use through content encryption and digital rights management (DRM). AWS Elemental MediaPackage uses the [AWS Secure Packager and Encoder Key Exchange (SPEKE) API](https://aws.amazon.com/media/tech/speke-basics-secure-packager-encoder-key-exchange-api/ "https://aws.amazon.com/media/tech/speke-basics-secure-packager-encoder-key-exchange-api/") to facilitate content encryption and decryption by a DRM provider. Using SPEKE, the DRM provider supplies encryption keys to MediaPackage through the SPEKE API. The DRM provider also supplies licenses to supported media players for decryption. For more information about how SPEKE is used with services and features running in the cloud, see [AWS cloud-based architecture](../../../speke/latest/documentation/what-is-speke.md#services-architecture "../../../speke/latest/documentation/what-is-speke.md#services-architecture") in the _Secure Packager and Encoder Key Exchange API Specification guide_.

## Limitations and requirements

When implementing content encryption for AWS Elemental MediaPackage, refer to the following
limitations and requirements:

- Use the AWS Secure Packager and Encoder Key Exchange (SPEKE) API to facilitate integration with a digital rights
  management (DRM) provider. For information about SPEKE, see [What is
  Secure Packager and Encoder Key Exchange?](../../../speke/latest/documentation/what-is-speke.md "../../../speke/latest/documentation/what-is-speke.md")
- Your DRM provider must support SPEKE. For a list of DRM providers that support SPEKE,
  see the [Get on board with a DRM platform provider](../../../speke/latest/documentation/customer-onboarding.md#choose-drm-provider "../../../speke/latest/documentation/customer-onboarding.md#choose-drm-provider") topic in the _MediaPackage User Guide_. Your DRM solution provider can help you set up DRM
  encryption use in MediaPackage.
- Use MediaPackage to encrypt live and video on demand (VOD) content. Assets that must
  be delivered through the MediaPackage VOD service must be harvested from an unencrypted HLS live
  endpoint. You can harvest live-to-VOD assets from HLS and DASH endpoints that are
  protected by DRM or encryption. However, the MediaPackage VOD service can't ingest these assets
  because they're encrypted (not clear) content. For more information about this kind of
  workflow, see [Creating live-to-VOD assets with AWS Elemental MediaPackage](ltov.md "ltov.md").

The following sections provide guidance on how to choose and implement content encryption
using SPEKE for MediaPackage.

###### Topics

- [Choosing the right SPEKE Version](encryption-choosing-speke-version.md "encryption-choosing-speke-version.md")
- [Deploying SPEKE](encryption-deploying-speke.md "encryption-deploying-speke.md")
- [Preparing and managing certificates for use with
  content keys](drm-content-key-encryption.md "drm-content-key-encryption.md")
- [Understanding key rotation behavior](drm-content-key-rotation.md "drm-content-key-rotation.md")
- [SPEKE Version 2.0 presets](drm-content-speke-v2-presets.md "drm-content-speke-v2-presets.md")
- [Removing tags from the parent manifest from
  AWS Elemental MediaPackage](drm-query-param.md "drm-query-param.md")
