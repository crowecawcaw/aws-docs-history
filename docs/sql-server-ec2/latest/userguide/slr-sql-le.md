# Service-linked role for SQL License Exemption

Amazon EC2 uses service-linked roles for the permissions that it requires to call other
AWS services on your behalf. A service-linked role is a unique type of IAM role that
is linked directly to an AWS service. Service-linked roles provide a secure way to
delegate permissions to AWS services because only the linked service can assume a
service-linked role. For more information about how Amazon EC2 uses IAM roles, including
service-linked roles, see [IAM roles for Amazon EC2](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md")
in the _Amazon EC2 User Guide_.

SQL Server on EC2 uses the service-linked role named **AWSServiceRoleForEC2SqlHa**
to allow the service to detect whether an EC2 instance that's tagged with the EC2 SQL
High Availability identifier (`SqlHaMonitored` set to `true`) is
running in active or passive mode.

## Permissions granted by AWSServiceRoleForEC2SqlHa

The AWSServiceRoleForEC2SqlHa service-linked role trusts the following service
to assume the role: `ec2sqlha.amazonaws.com`

Amazon EC2 uses the [AWSEC2SqlHaServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSEC2SqlHaServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSEC2SqlHaServiceRolePolicy.md") managed policy to complete
the following actions:

- **Amazon EC2** – Access is granted for the
  EC2 SQL High Availability service to describe EC2 instances, instance
  attributes, instance status which are tagged with the service identifier
  (`SqlHaMonitored` set to `true`).
- **Amazon EventBridge** – Includes access to create
  Amazon EventBridge event rules and retrieve details about or delete rules that it created.
  This is to allow the System Manager document **AWSEC2-DetectSqlHaState**
  execution output being forwarded to the service. A managed Amazon EventBridge rule will
  be created to forward System Manager run command events. Managed rules are
  predefined by User Notifications and include event patterns that are required
  by the service to manage customer notifications, and unless defined otherwise,
  only the owning service can utilize these managed rules.
- **AWS Systems Manager** – Includes access to describe
  instance information and list commands and command invocations. To run the
  command document that begins with **AWSEC2-DetectSqlHaState**,
  on a monitored instance, access is granted for the `SendCommand` and
  `GetCommandInvocation` operations to EC2 SQL Server instances tagged with
  the service identifier(`SqlHaMonitored` set to `true`).

To view the permissions for this policy, see [AWSEC2SqlHaServiceRolePolicy](../../../aws-managed-policy/latest/reference/AWSEC2SqlHaServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AWSEC2SqlHaServiceRolePolicy.md") in the _AWS
Managed Policy Reference_.

For more information about using managed policies for EC2 instances, see
[AWS managed policies
for Amazon EC2](../../../AWSEC2/latest/UserGuide/security-iam-awsmanpol.md "../../../AWSEC2/latest/UserGuide/security-iam-awsmanpol.md") in the _Amazon EC2 User Guide_.
