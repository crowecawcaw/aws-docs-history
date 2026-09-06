

# Security best practices for Amazon DocumentDB
<a name="security_best_practices"></a>

Amazon DocumentDB provides security features including Amazon VPC isolation, encryption at rest using AWS KMS, encryption in transit using TLS, and fine-grained access control through IAM. Use the following best practices to secure your Amazon DocumentDB clusters, instances, and data.

Use AWS Identity and Access Management (IAM) roles to control access to Amazon DocumentDB API operations. This includes operations that create, modify, or delete Amazon DocumentDB resources such as clusters, security groups, and parameter groups. When applications or other AWS services need to access Amazon DocumentDB resources, use an IAM role to provide temporary credentials rather than storing long-term credentials in your application. When creating IAM roles, apply the principle of least privilege. For more information, see [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) and [Common scenarios for roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios.html) in the *IAM User Guide*.
+ Enforce least privilege with [role-based access control](role_based_access_control.md). 
+ Don't use the AWS account root user to manage Amazon DocumentDB resources. Instead, use AWS Identity and Access Management Identity Center to create human users with temporary credentials. For more information, see [IAM Identity Center users](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_identity-management.html) in the *IAM User Guide*.
+ Grant each identity the minimum set of permissions required to perform their duties.
+ Use IAM policies to manage permissions and follow the principle of least privilege. For more information, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*. 
+ If you use IAM users with long-term credentials, rotate those credentials regularly.
**Warning**  
This scenario requires IAM users with programmatic access and long-term credentials, which presents a security risk. To help mitigate this risk, we recommend that you provide these users with only the permissions they require to perform the task and that you remove these users when they are no longer needed. Access keys can be updated if necessary. For more information, see [Update access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id-credentials-access-keys-update.html) in the *IAM User Guide*.
+ Configure Secrets Manager to automatically rotate the secrets for Amazon DocumentDB. For more information, see [ Rotating your secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) and [ Rotating secrets for Amazon DocumentDB](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets-documentdb.html) in the *AWS Secrets Manager User Guide*. 
+ Use Transport Layer Security (TLS) and encryption at rest to encrypt your data. 