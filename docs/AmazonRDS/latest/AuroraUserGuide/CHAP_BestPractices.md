# Security best practices for Amazon Aurora

Use AWS Identity and Access Management (IAM) accounts to control access to Amazon RDS API operations, especially
operations that create, modify, or delete
Amazon Aurora resources. Such
resources include DB
clusters, security groups, and parameter groups. Also
use IAM to control actions that perform common administrative actions such as backing
up and restoring DB
clusters.

- Create an individual user for each person who manages
  Amazon Aurora resources, including yourself. Don't use AWS root
  credentials to manage
  Amazon Aurora resources.
- Grant each user the minimum set of permissions required to perform his or her
  duties.
- Use IAM groups to effectively manage permissions for multiple users.
- Rotate your IAM credentials regularly.
- Configure AWS Secrets Manager to automatically rotate the secrets for
  Amazon Aurora. For more information, see [Rotating your AWS Secrets Manager
  secrets](../../../secretsmanager/latest/userguide/rotating-secrets.md "../../../secretsmanager/latest/userguide/rotating-secrets.md") in the _AWS Secrets Manager User Guide_. You can also
  retrieve the credential from AWS Secrets Manager programmatically. For more information,
  see [Retrieving the secret
  value](../../../secretsmanager/latest/userguide/manage_retrieve-secret.md "../../../secretsmanager/latest/userguide/manage_retrieve-secret.md") in the _AWS Secrets Manager User Guide_.
  For more information about
  Amazon Aurora security, see [Security in Amazon Aurora](UsingWithRDS.md "UsingWithRDS.md")
  . For more information about IAM, see [AWS Identity and Access Management](../../../IAM/latest/UserGuide/Welcome.md "../../../IAM/latest/UserGuide/Welcome.md"). For information on IAM best
  practices, see [IAM best
  practices](../../../IAM/latest/UserGuide/IAMBestPractices.md "../../../IAM/latest/UserGuide/IAMBestPractices.md").

AWS Security Hub uses security controls to evaluate resource configurations and security
standards to help you comply with various compliance frameworks. For more information
about using Security Hub to evaluate RDS resources, see [Amazon Relational Database Service controls](../../../securityhub/latest/userguide/rds-controls.md "../../../securityhub/latest/userguide/rds-controls.md") in the
AWS Security Hub User Guide.

You can monitor your usage of RDS as it relates to security best practices by using
Security Hub. For more information, see [What is AWS Security Hub?](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md").

Use the AWS Management Console, the AWS CLI, or the RDS API to change the password for your master
user. If you use another tool, such as a SQL client, to change the master user password,
it might result in privileges being revoked for the user unintentionally.

Amazon GuardDuty is a continuous security monitoring service that analyzes
and processes various data sources, including Amazon RDS login activity. It uses threat
intelligence feeds and machine learning to identify unexpected, potentially
unauthorized, suspicious login behavior, and malicious activity within your AWS
environment.

When Amazon GuardDuty RDS Protection detects a potentially suspicious or anomalous
login attempt that indicates a threat to your database, GuardDuty generates a new finding
with details about the potentially compromised database. For more information, see [Monitoring threats with Amazon GuardDuty RDS Protection for Amazon Aurora](guard-duty-rds-protection.md "guard-duty-rds-protection.md")
.
