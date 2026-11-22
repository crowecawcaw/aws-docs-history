

# SEC02-BP03 Store and use secrets securely

 Workloads prove their identity to databases, APIs, and third-party services with secrets such as passwords, API keys, and tokens. A secret in source code, a configuration file, or an environment variable is easy to disclose and hard to rotate. A secrets service encrypts these credentials, controls access, and rotates them automatically. 

 **Desired outcome:** 
+  You know which secrets your workload requires and why each one exists. 
+  You have replaced long-term credentials with short-term credentials wherever the workload supports it. 
+  Your remaining long-term secrets are stored encrypted and rotated automatically. 
+  You scope, audit, and log access to every secret. 
+  Your development process continuously checks that no secrets are committed to source code. 

 **Common anti-patterns:** 
+  Teams store long-term credentials in source code or configuration files. 
+  Teams store credentials at rest without encryption. 
+  Teams never rotate credentials, so a single instance of unauthorized access remains there indefinitely. 
+  Teams grant broad human access to production secrets instead of restricting it to a dedicated role. 

 **Benefits of establishing this best practice:** 
+  Secrets are encrypted at rest and in transit. 
+  Access to each secret is gated through an API and recorded for audit. 
+  Rotation runs in a central location, separate from application logic. 
+  Fine-grained access control limits which principals can read or change a secret. 
+  Automated scanning catches secrets before they reach a shared repository. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Manage secrets in three ordered steps to reduce what needs long-term protection: remove, replace, and rotate. 1. Remove credentials the workload no longer needs. 2. Replace long-term credentials with short-term ones where possible — for example, swap a stored access key for a role that supplies temporary credentials. 3. Store and rotate what remains. 

 An audit of source code and configuration usually surfaces several kinds of credentials. The following table maps each to a handling strategy: 


|  Credential type  |  Description  |  Suggested strategy  | 
| --- | --- | --- | 
|  IAM access keys  |  Access and secret keys used to call AWS from within a workload  |  Replace with [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios.html) on the compute runtime, such as [Amazon EC2](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html) or [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html). For third-party access, ask whether they support [cross-account access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html). For mobile apps, use [Amazon Cognito identity pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html). For workloads outside AWS, use [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) or [AWS Systems Manager hybrid activations](https://docs.aws.amazon.com/systems-manager/latest/userguide/activations.html). For containers, use the [Amazon ECS task role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) or [Kubernetes service account for EKS](https://docs.aws.amazon.com/eks/latest/userguide/service-accounts.html).  | 
|  SSH keys  |  Private keys used to log in to Linux instances  |  Replace with [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) or [EC2 Instance Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-linux-inst-eic.html), using IAM roles.  | 
|  Application and database passwords  |  Plaintext password strings  |  Rotate by storing them in [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) with automated rotation.  | 
|  Amazon RDS and Aurora admin credentials  |  Plaintext password strings  |  Replace with the Secrets Manager integration for [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) or [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html), or use [IAM database authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html) where supported.  | 
|  OAuth and API tokens  |  Secret token strings  |  Rotate by storing them in [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) with automated rotation.  | 

 Access AWS services with [temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) from a role. Use [roles for EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) instances, [execution roles](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) for Lambda functions, [Cognito roles](https://docs.aws.amazon.com/cognito/latest/developerguide/iam-roles.html) for mobile users, or [IoT Core policies](https://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html) for devices. For third-party integrations, [delegate access to a role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_third-party.html). Do not share static access keys with partners. 

 For secrets that must persist, use a managed service for storage, rotation, and access control. [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) provides [encryption at rest](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html), [encryption in transit](https://docs.aws.amazon.com/secretsmanager/latest/userguide/data-protection.html), [auditing](https://docs.aws.amazon.com/secretsmanager/latest/userguide/monitoring.html), [fine-grained access control](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html), and [automated rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html). Partner or self-built solutions with the same guarantees also work. Client-side caching speeds up retrieval and lowers API cost (for retrieval options, see [Get secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html)). 

**Note**  
 Some languages require you to implement your own in-memory encryption for client-side caching. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Find hard-coded credentials in code:** Scan your repositories with automated tooling such as [Amazon Inspector code scanning](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments.html) in your CI/CD pipeline, then filter findings for secrets/credentials to locate the offending lines. Treat every finding as a credential to replace with role-based authentication, or at minimum rotate, rather than only a line to edit. 

1.  **Remove or replace what you can:** Mark credentials that are no longer needed for deletion. Replace embedded AWS access keys with IAM roles on the associated resources, and for components outside AWS use [IAM Roles Anywhere](https://aws.amazon.com/blogs/security/extend-aws-iam-roles-to-workloads-outside-of-aws-with-iam-roles-anywhere/) or [AWS Systems Manager hybrid activations](https://docs.aws.amazon.com/systems-manager/latest/userguide/activations.html). 

1.  **Move remaining long-lived secrets into a secrets service:** For third-party secrets that need the rotate strategy, integrate [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) into your code to retrieve them at runtime. Retrieve secrets using the [Lambda extension](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_lambda.html) for serverless functions or the [client-side examples](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html) for instances and containers. 

1.  **Prevent new secrets from entering the codebase:** Re-scan periodically, and add a pre-commit guard such as [git-secrets](https://github.com/awslabs/git-secrets) to block new credentials from being committed. 

1.  **Monitor secret access:** [Monitor Secrets Manager activity](https://docs.aws.amazon.com/secretsmanager/latest/userguide/monitoring.html) for unexpected usage, inappropriate access, or deletion attempts. 

1.  **Reduce human exposure to secrets:** Restrict read, write, and modify access to a dedicated IAM role, and let only a small set of operators assume it. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC02-BP02 Use temporary credentials](sec02-bp02.md) 
+  [SEC02-BP05 Audit and rotate credentials periodically](sec02-bp05.md) 
+  [SEC02-BP04 Rely on a centralized identity provider for users and machines](sec02-bp04.md) 

 **Related documents:** 
+  [IAM identity providers and federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html) 
+  [How AWS Secrets Manager uses AWS KMS](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html) 
+  [AWS Secrets Manager posts on the AWS Security Blog](https://aws.amazon.com/blogs/security/tag/aws-secrets-manager/) 

 **Related videos:** 
+  [AWS re:Invent 2024 - A proactive approach to secrets management at scale (SEC234)](https://www.youtube.com/watch?v=vMGYf09XBek) 

 **Related workshops:** 
+  [Store, retrieve, and manage sensitive credentials in AWS Secrets Manager](https://catalog.us-east-1.prod.workshops.aws/workshops/92e466fd-bd95-4805-9f16-2df07450db42/en-US) 