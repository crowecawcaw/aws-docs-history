# Amazon Nova Lite and Pro Customizable Content Moderation Settings

Content generation for Amazon Nova models is moderated by multiple [responsible AI (RAI) controls](https://www.amazon.science/blog/amazon-nova-and-our-commitment-to-responsible-ai "https://www.amazon.science/blog/amazon-nova-and-our-commitment-to-responsible-ai"). Two key controls are the alignment of the
core model to RAI pillars, and a runtime control – called an output model – that moderates core model responses to ensure alignment
with these pillars.

Amazon Nova Lite and Pro support customizable content moderation settings for customers with approved business use cases. These settings
allow content generation through three available combinations: the security pillar only, a combined setting for safety, sensitive content,
and fairness, or all pillars together.

These pillars encompass:

- **Safety** — Covering dangerous activities, weapons, and controlled substances.
- **Sensitive content** — Including profanity, nudity, and bullying.
- **Fairness** — Considerations around bias and culture.
- **Security** — Concerns involving malware and malicious content.
  Amazon Nova customizable content moderation settings allow you to adjust safeguards relevant to your business requirements. In all cases, Amazon Nova enforces essential,
  non-configurable controls to ensure responsible use of AI, such as controls to prevent harm to children and preserve privacy.
  Please see [Responsible use](responsible-use.md "responsible-use.md") for additional details on Amazon Nova safeguards.

Nova customizable content moderation settings are available for the Lite and Pro models using the method in
[Deploy a custom model for on-demand inference](../../../bedrock/latest/userguide/deploy-custom-model-on-demand.md "../../../bedrock/latest/userguide/deploy-custom-model-on-demand.md") in the Bedrock User Guide, in the us-east-1
(N. Virginia) region.

To access customizable content moderation settings, contact your AWS Account Manager.
