

# Region support
<a name="mpa-region-support"></a>

To use Multi-party approval, you must create [approval teams](mpa-concepts.md#mpa-team-term) and the [identity source](mpa-concepts.md#mpa-identity-source) in the US East (N. Virginia) Region. For more information about AWS Regions, see [Region](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html?icmpid=docs_homepage_addtlrcs#region) in the *AWS Glossary Reference*.

Multi-party approval requires an organization instance of AWS IAM Identity Center. The IAM Identity Center instance can be enabled in any supported Region. For more information, see [Considerations for choosing an AWS Region](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-region-considerations.html) in the *IAM Identity Center User Guide*.

**Cross-Region considerations**

You can create approval teams that protect resources which are located in any commercial Region, even in Regions that are not US East (N. Virginia). During an approval session, user content (specifically requester comments) moves across Regions. When protecting resources in other Regions, there might be delays in the approval process if the US East (N. Virginia) Region experiences issues.

When you enable Multi-party approval and your IAM Identity Center instance in different Regions, Multi-party approval makes calls across Regions to IAM Identity Center. This means that [user and group](https://docs.aws.amazon.com/singlesignon/latest/userguide/users-groups-provisioning.html) information moves across Regions. If the Region where the IAM Identity Center instance is located experiences issues, approvers might temporarily be unable to access the Multi-party approval portal, and delivery of notifications about new approvals might be delayed.

For more information, see [IAM Identity Center Region data storage and operations](https://docs.aws.amazon.com/singlesignon/latest/userguide/regions.html) in the *IAM Identity Center User Guide*.