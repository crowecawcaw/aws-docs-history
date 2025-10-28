# Use AMS SSP to provision Amazon Quick Suite in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Quick Suite capabilities directly in your AMS managed account. Quick Suite is a fast, cloud-powered business intelligence service that delivers insights to everyone
in your organization. As a fully managed service, Quick Suite lets you easily create and publish interactive dashboards
that include machine learning (ML) insights.
To learn more, see [Amazon Quick Suite](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/").

## Quick Suite in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to Quick Suite in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned
service | Add change type (ct-1w8z66n899dct). This RFC provisions the
following IAM role to your account:
`customer_quicksight_console_admin_role`. After it's
provisioned in your account, you must onboard the role in your federation
solution.

**Q: What are the restrictions to using Quick Suite in my AMS account?**

- AWS resource settings on Quick Suite won’t be accessible to you
  because of the IAM policy dependency. However, the AMS team enables each resource for you in
  response to your
  request to enable the service.
- Resource access for individual users and groups are not supported in this model because this
  feature enables users to alter IAM permissions that could compromise
  AMS infrastructure.
- The ability to invite IAM identities from within QuickSight is not supported due to the
  risk involved altering IAM objects.
- Quick Suite service offers two editions: Enterprise and Standard. Both provide a single sign-on
  (SSO) option that is supported on AMS. However, the Enterprise
  Edition has an option to integrate Quick Suite with Active Directory
  (AD). Quick Suite on AMS does not support integration with AD due to
  incompatibilities between AMS account structure and the Quick Suite trust requirements.

**Q: What are the prerequisites or dependencies to using Quick Suite in my AMS account?**

- When AMS receives this RFC to add Quick Suite, you are sent a service request for
  additional information; provide them the following:
  - Quick Suite account name (for example,
    ``CustomerName`-quicksight`
  - Quick Suite Edition (Standard versus Enterprise)
  - The AWS Region in which to enable the Quick Suite service (defaults to your AMS AWS
    Region).
  - A notification email address for Quick Suite account.
  - (Optional) The S3 bucket where data files to be analyzed are located.
  - The VPC and subnet IDs that connect to Quick Suite support a feature to
    add a VPC connection, which enables private connectivity between Quick Suite and resources inside
    the account.

An AMS operator performs the sign up process on your behalf and configures
two QuickSight functionalities:

- [Auto discovery](../../../quicksight/latest/user/autodiscover-aws-data-sources.md "../../../quicksight/latest/user/autodiscover-aws-data-sources.md") to data sources.
- [VPC connections](../../../quicksight/latest/user/working-with-aws-vpc.md "../../../quicksight/latest/user/working-with-aws-vpc.md").

###### Note

These actions need to be performed by an AMS operator because
elevated IAM and VPC permissions are required during the sign-in process.
