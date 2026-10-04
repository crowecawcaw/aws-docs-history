

# Policy best practices
<a name="nx-security-iam-id-based-examples-best-practices"></a>

Identity-based policies determine whether someone can create, access, or delete AWS End User Messaging resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ Get started with AWS managed policies and move toward least-privilege permissions. See [AWS managed policies for AWS End User Messaging](nx-security-iam-managed-policies.md).
+ Apply least-privilege permissions by granting only the permissions required to perform a task.
+ Use IAM conditions to restrict access further where appropriate.
+ Use IAM Access Analyzer to validate your policies.
+ Require multi-factor authentication (MFA) for sensitive operations.