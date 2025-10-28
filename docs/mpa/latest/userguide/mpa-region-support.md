# Region support

To use Multi-party approval, you must create [approval teams](mpa-concepts.md#mpa-team-term "mpa-concepts.md#mpa-team-term") and the [identity source](mpa-concepts.md#mpa-identity-source "mpa-concepts.md#mpa-identity-source") in the US East (N. Virginia) Region.
For more information about AWS Regions, see [Region](../../../glossary/latest/reference/glos-chap.md#region "../../../glossary/latest/reference/glos-chap.md#region") in the _AWS Glossary Reference_.

Multi-party approval requires an organization instance of AWS IAM Identity Center. The IAM Identity Center instance can be enabled in any supported Region. For more information,
see [Considerations for choosing an AWS Region](../../../singlesignon/latest/userguide/identity-center-region-considerations.md "../../../singlesignon/latest/userguide/identity-center-region-considerations.md") in the _IAM Identity Center User Guide_.

**Cross-Region considerations**

You can create approval teams that protect resources which are located in any commercial Region, even in Regions that are not US East (N. Virginia).
During an approval session, user content (specifically requester comments) moves across Regions.
When protecting resources in other Regions, there might be delays in the approval process if the US East (N. Virginia) Region experiences issues.

When you enable Multi-party approval and your IAM Identity Center instance in different Regions, Multi-party approval makes calls across Regions to IAM Identity Center. This means that [user and group](../../../singlesignon/latest/userguide/users-groups-provisioning.md "../../../singlesignon/latest/userguide/users-groups-provisioning.md") information moves across Regions.
If the Region where the IAM Identity Center instance is located experiences issues, approvers might temporarily be unable to access the Multi-party approval portal, and delivery of notifications about new approvals might be delayed.

For more information, see [IAM Identity Center Region data storage and operations](../../../singlesignon/latest/userguide/regions.md "../../../singlesignon/latest/userguide/regions.md") in the _IAM Identity Center User Guide_.
