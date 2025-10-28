# How IAM works with other AWS services

While IAM is the primary AWS service you will use to manage IAM resources, all other
AWS services work with IAM to control access to the resources in your account.

- AWS CloudFormation

AWS CloudFormation integrates with IAM by allowing you to define and manage IAM
resources as part of your AWS CloudFormation
templates. You can use AWS CloudFormation to specify the necessary IAM permissions for other
AWS resources you provision. AWS CloudFormation also supports the use of IAM roles to
manage the credentials required for provisioning and managing your AWS
infrastructure, and its drift detection feature helps you maintain the integrity of
your IAM configurations.

- AWS CloudShell

When you access AWS CloudShell, your authentication and authorization are handled
through IAM. AWS CloudShell runs within the context of an IAM role assigned to your
user or account. When you launch AWS CloudShell, it automatically generates temporary
security credentials based on the IAM role assigned to you.

- AWS SDKs

The AWS SDKs work with IAM by handling the authentication and authorization
process, managing AWS credentials, and respecting the permissions and policies
defined in IAM to ensure your application can only access the resources it is
authorized to use. The SDKs provide mechanisms for obtaining and using temporary
security credentials, as well as validating the permissions required for your
application's operations.
For a list of AWS services that work with IAM and the IAM features the services support, see [AWS services that work with
IAM](reference_aws-services-that-work-with-iam.md "reference_aws-services-that-work-with-iam.md").
