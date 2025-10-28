# IAM permissions for MediaLive as a trusted

entity

AWS Elemental MediaLive must be set up so that when a channel is running, MediaLive itself has access to
perform operations on resources that belong to your organization's AWS account. In other words,
MediaLive must be set up as a _trusted entity_ in your organization's AWS account.

###### Topics

- [About the trusted entity role](about-trusted-entity.md "about-trusted-entity.md")
- [Options for implementing the trusted
  entity](scenarios-for-medialive-role.md "scenarios-for-medialive-role.md")
- [Create the trust entity – simple option](setup-trusted-entity-simple.md "setup-trusted-entity-simple.md")
- [Create the trusted entity - complex option](setup-trusted-entity-complex.md "setup-trusted-entity-complex.md")
