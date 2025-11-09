# Content encryption and DRM in AWS Elemental MediaPackage

Protect your content from unauthorized use through content encryption and digital rights management (DRM). AWS Elemental MediaPackage uses the [AWS Secure Packager and Encoder Key Exchange (SPEKE) API](https://aws.amazon.com/media/tech/speke-basics-secure-packager-encoder-key-exchange-api/ "https://aws.amazon.com/media/tech/speke-basics-secure-packager-encoder-key-exchange-api/") to facilitate content encryption and decryption by a DRM provider. Using SPEKE, the DRM provider supplies encryption keys to MediaPackage through the SPEKE API. The DRM provider also supplies licenses to supported media players for decryption. For more information about how SPEKE is used with services and features running in the cloud, see [AWS cloud-based architecture](../../../speke/latest/documentation/what-is-speke.md#services-architecture "../../../speke/latest/documentation/what-is-speke.md#services-architecture") in the _Secure Packager and Encoder Key Exchange API Specification guide_.

## Limitations and requirements

When implementing content encryption for MediaPackage, refer to the following limitations
and requirements:

- Use the AWS Secure Packager and Encoder Key Exchange (SPEKE) API to facilitate integration with a digital rights
  management (DRM) system provider. For information about SPEKE, see [What is Secure
  Packager and Encoder Key Exchange?](../../../speke/latest/documentation/what-is-speke.md "../../../speke/latest/documentation/what-is-speke.md")
- Your DRM system provider must support SPEKE. For a list of DRM providers that support
  SPEKE, see the [Get on
  board with a DRM platform provider](../../../speke/latest/documentation/customer-onboarding.md#choose-drm-provider "../../../speke/latest/documentation/customer-onboarding.md#choose-drm-provider") topic in the _AWS Elemental MediaPackage User Guide_. Your DRM provider can help you set up DRM encryption use in
  MediaPackage.
- Use MediaPackage to encrypt live content.

## Container and DRM system support with

SPEKE

MediaPackage supports [SPEKE Version 2.0](../../../speke/latest/documentation/the-speke-api-v2.md "../../../speke/latest/documentation/the-speke-api-v2.md") which uses
multiple, distinct encryption keys for audio and video tracks and uses [Content Protection Information Exchange
(CPIX) Version 2.3](https://dashif.org/docs/CPIX2.3/Cpix.html "https://dashif.org/docs/CPIX2.3/Cpix.html"). For more information about SPEKE Version 2.0 encryption
configurations, see [Encryption presets in AWS Elemental MediaPackage](drm-content-speke-v2-presets.md "drm-content-speke-v2-presets.md").

**Supported containers and DRM systems**

The following table lists the different containers and digital rights management (DRM)
systems that SPEKE Version 2.0 supports.

| SPEKE Version 2.0 – Support matrix for container and DRM system | Apple FairPlay                | ClearKey AES-128      | Google Widevine                        | Microsoft PlayReady                    | Irdeto                        |
| --------------------------------------------------------------- | ----------------------------- | --------------------- | -------------------------------------- | -------------------------------------- | ----------------------------- |
| **TS container**                                                | √<br>Supports SAMPLE-AES      | √<br>Supports AES-128 | Not supported                          | Not supported                          | Not supported                 |
| **CMAF container**                                              | √<br>Supports cbcs encryption | Not supported         | √<br>Supports cbcs and cenc encryption | √<br>Supports cbcs and cenc encryption | √<br>Supports cenc encryption |

**Supported DRM system IDs**

The following table lists the different DRM [system IDs](https://dashif.org/identifiers/content_protection/ "https://dashif.org/identifiers/content_protection/") that
MediaPackage supports.

| System IDs – Support matrix for DRM system | Apple FairPlay                       | ClearKey AES-128                     | Google Widevine                      | Microsoft PlayReady                  | Irdeto                               |
| ------------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
|                                            | 94ce86fb-07ff-4f43-adb8-93d2fa968ca2 | 3ea8778f-7742-4bf9-b18b-e834b2acbd47 | edef8ba9-79d6-4ace-a3c8-27dcd51d21ed | 9a04f079-9840-4286-ab92-e65be0885f95 | 80a6be7e-1448-4c37-9e70-d5aebe04c8d2 |

## Deploying SPEKE

Your digital rights management (DRM) system provider can help you get set up to use DRM
encryption in MediaPackage. Generally, the provider gives you a SPEKE gateway to deploy in
your AWS account in the same AWS Region where MediaPackage is running.
For
information about configuring encryption settings for your endpoint, see [encryption
fields](../ug/endpoints-encryption.md "../ug/endpoints-encryption.md").

If you must build your own API Gateway to connect MediaPackage to your key service, you can use
the [SPEKE Reference
Server](https://github.com/awslabs/speke-reference-server "https://github.com/awslabs/speke-reference-server") available on GitHub as a starting point.

The following sections provide guidance on how to implement content encryption using SPEKE
for MediaPackage.

###### Topics

- [Key rotation](drm-content-key-rotation.md "drm-content-key-rotation.md")
- [Managing DRM segment metadata](drm-segment-metadata-management.md "drm-segment-metadata-management.md")
- [Encryption presets](drm-content-speke-v2-presets.md "drm-content-speke-v2-presets.md")
