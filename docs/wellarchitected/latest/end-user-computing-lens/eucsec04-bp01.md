# EUCSEC04-BP01 Separate end user systems between different groups of users when required to satisfy policy or regulatory requirements

Many organizations have security requirements that mandate the
segregation of systems accessed and interacted with by end users
from servers that perform an infrastructure or application
hosting function. Regardless of whether there is a specific
security requirement, end user systems should be segregated from
each other. This is for multiple reasons including reducing the
risk of unintended access and exposure to unsafe software.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

- **Use distinct AWS accounts to
  separate EUC services from other AWS workloads:**
  Separate AWS EUC workloads deployed to an AWS account from
  application and infrastructure servers and services that
  are consumed by the EUC workloads using different AWS accounts. You can use
  [AWS Control Tower](../../../controltower/latest/userguide/what-is-control-tower.md "../../../controltower/latest/userguide/what-is-control-tower.md") and

[AWS Organizations](../../../organizations.md "../../../organizations.md") are two services to implement and
manage a multi-account structure in your AWS environment.
Create an AWS account for EUC workloads and use other
accounts for infrastructure and application services. For
more detail, see
[SEC01-BP01
Separate workloads using accounts](../security-pillar/sec_securely_operate_multi_accounts.md "../security-pillar/sec_securely_operate_multi_accounts.md").

- **Use
  [IAM
  roles with AppStream 2.0](../../../appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.md#how-to-use-iam-role-with-streaming-instances "../../../appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.md#how-to-use-iam-role-with-streaming-instances") to enable access to AWS
  services**: To access AWS services from an
  AppStream 2.0 instance, use an IAM role and verify that
  the IAM policy attached to it is scoped to the specific
  services required. This approach avoids the need for users
  in AppStream 2.0 sessions to have access with additional
  credentials. If groups of users require differing levels
  of access to other AWS services, consider creating an
  additional role for each set of permissions. To help
  determine the least privilege policies based on the needed
  access, analyze user access with AWS IAM Access Analyzer.
  For further detail, see
  [Use IAM Access Analyzer policy generation to grant fine-grained permissions for your AWS CloudFormation service roles](https://aws.amazon.com/blogs/security/use-iam-access-analyzer-policy-generation-to-grant-fine-grained-permissions-for-your-aws-cloudformation-service-roles/ "https://aws.amazon.com/blogs/security/use-iam-access-analyzer-policy-generation-to-grant-fine-grained-permissions-for-your-aws-cloudformation-service-roles/").
- **Restrict access to only authorized
  applications**: By default, AppStream 2.0 allows
  users or applications to start programs on the instance,
  beyond what is specified in the image application catalog.
  This is useful when your application relies on another
  application as part of a workflow, but it may be
  undesirable for the user to be able to start that
  dependent application directly. For example, an
  application starts the browser to provide help
  instructions from an application vendor's website, but the
  ability for the user to start the browser directly must be
  blocked.

In some situations, it can be desirable to
control which applications can be launched on streaming
instances. Microsoft AppLocker is application control
software that uses explicit control policies to enable, or
disable, the applications a user can run. An alternative
to Microsoft AppLocker is FSLogix Application Masking
which is available with Windows desktop and server
operating systems. The
[use
of application entitlements with AppStream 2.0](../../../appstream2/latest/developerguide/manage-application-entitlements.md "../../../appstream2/latest/developerguide/manage-application-entitlements.md") can
restrict the ability of users to launch only authorized
applications, but this control by itself does not prevent
the launch of other applications on AppStream 2.0
instances. To achieve this, we recommend the two preceding
approaches AppLocker or FSLogix.

- **Secure access to the S3 buckets
  used by Amazon AppStream 2.0:** Review, maintain,
  and update S3 bucket policies as appropriate. These
  reviews should verify that restricted access is in place
  to protect S3 buckets that are created and used to persist
  user data for both home folders and application settings
  persistence when enabled. This blocks non-AppStream 2.0
  administrators from accessing the data. Use S3 bucket
  policies and IAM policies together. For more information,
  see
  [IAM Policies and Bucket Policies and ACLs! Oh, My! (Controlling Access to S3 Resources)](https://aws.amazon.com/blogs/security/iam-policies-and-bucket-policies-and-acls-oh-my-controlling-access-to-s3-resources/ "https://aws.amazon.com/blogs/security/iam-policies-and-bucket-policies-and-acls-oh-my-controlling-access-to-s3-resources/").
