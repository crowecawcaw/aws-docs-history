# Security best practices for Amazon DocumentDB

For security best practices, you must use AWS Identity and Access Management (IAM) accounts
to control access to Amazon DocumentDB API operations, especially operations that
create, modify, or delete Amazon DocumentDB resources. Such resources include
clusters, security groups, and parameter groups. You must also use IAM
to control actions that perform common administrative actions such as
backing up restoring clusters. When creating IAM roles, employ the
principle of least privilege.

- Enforce least privilege with [role-based access
  control](role_based_access_control.md "role_based_access_control.md").
- Assign an individual IAM account to each person who manages
  Amazon DocumentDB resources. Do not use the AWS account root user to manage
  Amazon DocumentDB resources. Create an IAM user for everyone, including
  yourself.
- Grant each user the minimum set of permissions that are
  required to perform their duties.
- Use IAM groups to effectively manage permissions for multiple
  users. For more information about IAM, see the [IAM User Guide](../../../IAM/latest/UserGuide/Welcome.md "../../../IAM/latest/UserGuide/Welcome.md").
  For information about IAM best practices, see [IAM Best Practices](../../../IAM/latest/UserGuide/IAMBestPractices.md "../../../IAM/latest/UserGuide/IAMBestPractices.md").
- Regularly rotate your IAM credentials.
- Configure AWS Secrets Manager to automatically rotate the
  secrets for Amazon DocumentDB. For more information, see [Rotating Your AWS Secrets Manager Secrets](../../../secretsmanager/latest/userguide/rotating-secrets.md "../../../secretsmanager/latest/userguide/rotating-secrets.md") and [Rotating Secrets for Amazon DocumentDB](../../../secretsmanager/latest/userguide/rotating-secrets-documentdb.md "../../../secretsmanager/latest/userguide/rotating-secrets-documentdb.md") in the
  _AWS Secrets Manager User Guide_.
- Use Transport Layer Security (TLS) and encryption at rest to
  encrypt your data.
