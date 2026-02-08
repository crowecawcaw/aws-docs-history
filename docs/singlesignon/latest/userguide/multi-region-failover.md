# Failover to an additional Region for AWS account access

The topic of AWS account access through IAM Identity Center is covered extensively in [Configure access to AWS accounts](manage-your-accounts.md "manage-your-accounts.md"). This section provides additional details relevant to
maintaining AWS account access across multiple AWS Regions in the event of a service
disruption in the primary Region.

If your IAM Identity Center instance is experiencing a disruption in the primary Region, your workforce
can switch to an additional Region to continue accessing AWS accounts and unaffected
applications. The section [Workforce access through an additional Region](multi-region-workforce-access.md "multi-region-workforce-access.md") explains how to access the
AWS access portal in an additional Region.

We recommend that you communicate the AWS access portal endpoints in additional Regions and
the external IdP setup (such as bookmark apps for the additional Regions) to your workforce as
soon as you complete the setup in [Replicate IAM Identity Center to an
additional Region](replicate-to-additional-region.md "replicate-to-additional-region.md"). This will
enable them to be ready for failover to an additional Region if needed.

Similarly, we recommend that AWS CLI users create [AWS CLI
profiles](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md") for additional Regions for each of the profiles they have for the primary
Region. Then, they can switch to that profile if there is a service disruption in the primary
Region.

###### Note

Continuity of access to AWS accounts also depends on the health of your external IdP
and permissions such as permission set assignments and group memberships being provisioned
and replicated before a service disruption. We recommend your organization also set up [AWS
break-glass access](../../../wellarchitected/latest/devops-guidance/ag.sad.md "../../../wellarchitected/latest/devops-guidance/ag.sad.md") to maintain AWS access to a small group of privileged users
when the external IdP has a service disruption. [Set up emergency access to the AWS Management Console](emergency-access.md "emergency-access.md") is a
similar option that avoids using IAM users, but it too depends on the external IdP.

## AWS account access

resiliency without multiple ACS URLs

Some external identity providers (IdPs) don't support multiple assertion consumer service
(ACS) URLs in their IAM Identity Center application. Multiple ACS URLs are a SAML feature that is required for direct sign-in to a specific Region in a multi-Region IAM Identity Center.

To enable your users to access their
AWS accounts through multiple IAM Identity Center Regions, you must configure the respective
regional ACS URLs in the external IdP. However, if the external IdP
supports only a single ACS URL in their IAM Identity Center application, users can directly
sign into a single IAM Identity Center Region.

To resolve this issue, work with your IdP vendor to enable support for multiple ACS
URLs. In the meantime, you can use
additional Regions as backup for access to AWS accounts.

If an IAM Identity Center service disruption occurs in the
primary Region, you must update the ACS URL in the external IdP with an additional
Region's ACS URL. After this update, your users can access the AWS access portal in the additional
Region using
the existing IAM Identity Center application in the external IdP portal, or through a direct link that you share
with
them.

We recommend that you test this setup periodically to ensure that it works when needed and
communicate this failover process to your organization.

###### Note

When you use an additional Region for access to AWS accounts in this setup,
your users might not be able to access AWS managed applications that are
connected to the primary Region. Therefore, we recommend this only as a temporary measure
to maintain access to AWS accounts.
