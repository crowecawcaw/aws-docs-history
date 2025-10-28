# Preventative security best practices

for Aurora DSQL

In addition to the following ways to securely use Aurora DSQL, see [Security](../../../wellarchitected/latest/framework/security.md "../../../wellarchitected/latest/framework/security.md") in AWS Well-Architected Tool to learn about how cloud technologies improve your
security.

**Use IAM roles to authenticate access to Aurora DSQL.**

Users, applications, and other AWS services that access Aurora DSQL must
include valid AWS credentials in AWS API and AWS CLI requests. You
shouldn't store AWS credentials directly in the application or EC2
instances. These are long-term credentials that aren't automatically
rotated. There is significant business impact if these credentials are
compromised. An IAM role lets you obtain temporary access keys that you
can use to access AWS services and resources.

For more information, see [Authentication and authorization for
Aurora DSQL](authentication-authorization.md "authentication-authorization.md").

**Use IAM policies for Aurora DSQL base authorization.**

When you grant permissions, you decide who is getting them, which Aurora DSQL
API operations they are getting permissions for, and the specific actions
you want to allow on those resources. Implementing least privilege is key in
reducing security risk and the impact that can result from errors or
malicious intent.

Attach permissions policies to IAM roles and grant permissions to
perform operations on Aurora DSQL resources. Also available are [permissions
boundaries for IAM entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md"), which let you set the maximum
permissions that an identity-based policy can grant to an IAM
entity.

Similar to the [root user best
practices for your AWS account](../../../IAM/latest/UserGuide/root-user-best-practices.md "../../../IAM/latest/UserGuide/root-user-best-practices.md"), don't use the
`admin` role in Aurora DSQL to perform everyday operations.
Instead, we recommend that you create custom database roles to manage and
connect to your cluster. For more information, see [Accessing Aurora DSQL](accessing.md "accessing.md") and [Understanding
authentication and authorization for Aurora DSQL](accessing.md "accessing.md").

**Use `verify-full` in production environments.**

This setting verifies that the server certificate is signed by a trusted
certificate authority and that the server hostname matches the certificate.

**Update your PostgreSQL client**

Regularly update your PostgreSQL client to the latest version to benefit
from security improvements. We recommend using PostgreSQL version 17.
