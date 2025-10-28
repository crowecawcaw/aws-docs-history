# Requirements

When implementing content encryption for MediaConvert, refer to the following
limitations and requirements:

- Use the AWS Secure Packager and Encoder Key Exchange (SPEKE) API to facilitate integration with a digital rights
  management (DRM) system provider. For information about SPEKE, see [What is
  Secure Packager and Encoder Key Exchange?](../../../speke/latest/documentation/what-is-speke.md "../../../speke/latest/documentation/what-is-speke.md")
- Your DRM system provider must support SPEKE. For a list of DRM providers that support
  SPEKE, see the [Get on
  board with a DRM platform provider](../../../speke/latest/documentation/customer-onboarding.md#choose-drm-provider "../../../speke/latest/documentation/customer-onboarding.md#choose-drm-provider") topic in the _SPEKE
  partner and customer guide_. Your DRM provider can help you set up DRM
  encryption use in MediaConvert.
