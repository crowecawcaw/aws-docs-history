# Security best practices for Amazon RDS

Use AWS Identity and Access Management (IAM) accounts to control access to Amazon RDS API operations, especially
operations that create, modify, or delete Amazon RDS
resources. Such
resources include DB instances
, security groups, and parameter groups. Also
use IAM to control actions that perform common administrative actions such as backing
up and restoring DB instances
.

- Create an individual user for each person who manages Amazon RDS
  resources, including yourself. Don't use AWS root
  credentials to manage Amazon RDS
  resources.
- Grant each user the minimum set of permissions required to perform his or her
  duties.
- Use IAM groups to effectively manage permissions for multiple users.
- Rotate your IAM credentials regularly.
- Configure AWS Secrets Manager to automatically rotate the secrets for Amazon RDS
  . For more information, see [Rotating your AWS Secrets Manager
  secrets](../../../secretsmanager/latest/userguide/rotating-secrets.md "../../../secretsmanager/latest/userguide/rotating-secrets.md") in the _AWS Secrets Manager User Guide_. You can also
  retrieve the credential from AWS Secrets Manager programmatically. For more information,
  see [Retrieving the secret
  value](../../../secretsmanager/latest/userguide/manage_retrieve-secret.md "../../../secretsmanager/latest/userguide/manage_retrieve-secret.md") in the _AWS Secrets Manager User Guide_.
  For more information about Amazon RDS
  security, see [Security in Amazon RDS](UsingWithRDS.md "UsingWithRDS.md")
  . For more information about IAM, see [AWS Identity and Access Management](../../../IAM/latest/UserGuide/Welcome.md "../../../IAM/latest/UserGuide/Welcome.md"). For information on IAM best
  practices, see [IAM best
  practices](../../../IAM/latest/UserGuide/IAMBestPractices.md "../../../IAM/latest/UserGuide/IAMBestPractices.md").

AWS Security Hub CSPM uses security controls to evaluate resource configurations and security
standards to help you comply with various compliance frameworks. For more information
about using Security Hub CSPM to evaluate RDS resources, see [Amazon Relational Database Service controls](../../../securityhub/latest/userguide/rds-controls.md "../../../securityhub/latest/userguide/rds-controls.md") in the
AWS Security Hub User Guide.

You can monitor your usage of RDS as it relates to security best practices by using
Security Hub CSPM. For more information, see [What is AWS Security Hub CSPM?](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md").

Use the AWS Management Console, the AWS CLI, or the RDS API to change the password for your master
user. If you use another tool, such as a SQL client, to change the master user password,
it might result in privileges being revoked for the user unintentionally.
