# Identity and access management for Microsoft SQL Server on Amazon EC2

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access
to AWS resources. IAM administrators control who can be _authenticated_ (signed in) and _authorized_
(have permissions) to use SQL Server on EC2> resources. IAM is an AWS service that you can
use with no additional charge.

Your security credentials identify you to services in AWS and grant you access to
AWS resources, such as your Amazon EC2 resources. You can use features of Amazon EC2 and IAM
to allow other users, services, and applications to use your Amazon EC2 resources without
sharing your security credentials. You can use IAM to control how other users use
resources in your AWS account, and you can use security groups to control access
to your Amazon EC2 instances. You can choose to allow full or limited use of your Amazon EC2
resources.

If you are a developer, you can use IAM roles to manage the security credentials
needed by the applications that you run on your EC2 instances. After you attach an
IAM role to your instance, your applications running on the instance can retrieve
the credentials from the Instance Metadata Service (IMDS).

For best practices for securing your AWS resources using IAM, see [Security best
practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

###### Contents

- [AWS managed policies for SQL Server on EC2](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
- [Service-linked role for SQL License Exemption](slr-sql-le.md "slr-sql-le.md")
