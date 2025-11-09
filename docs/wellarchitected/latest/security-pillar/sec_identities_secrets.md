# SEC02-BP03 Store and use secrets securely

A workload requires an automated capability to prove its identity to
databases, resources, and third-party services. This is accomplished
using secret access credentials, such as API access keys, passwords,
and OAuth tokens. Using a purpose-built service to store, manage,
and rotate these credentials helps reduce the likelihood that those
credentials become compromised.

**Desired outcome:** Implementing a
mechanism for securely managing application credentials that
achieves the following goals:

- Identifying what secrets are required for the workload.
- Reducing the number of long-term credentials required by
  replacing them with short-term credentials when possible.
- Establishing secure storage and automated rotation of remaining
  long-term credentials.
- Auditing access to secrets that exist in the workload.
- Continual monitoring to verify that no secrets are embedded in
  source code during the development process.
- Reduce the likelihood of credentials being inadvertently
  disclosed.

**Common anti-patterns:**

- Not rotating credentials.
- Storing long-term credentials in source code or configuration
  files.
- Storing credentials at rest unencrypted.

**Benefits of establishing this best
practice:**

- Secrets are stored encrypted at rest and in transit.
- Access to credentials is gated through an API (think of it as a
  _credential vending machine_).
- Access to a credential (both read and write) is audited and
  logged.
- Separation of concerns: credential rotation is performed by a
  separate component, which can be segregated from the rest of the
  architecture.
- Secrets are automatically distributed on-demand to software
  components and rotation occurs in a central location.
- Access to credentials can be controlled in a fine-grained
  manner.

**Level of risk exposed if this best practice
is not established**: High

## Implementation guidance

In the past, credentials used to authenticate to databases,
third-party APIs, tokens, and other secrets might have been
embedded in source code or in environment files. AWS provides
several mechanisms to store these credentials securely,
automatically rotate them, and audit their usage.

The best way to approach secrets management is to follow the
guidance of remove, replace, and rotate. The most secure
credential is one that you do not have to store, manage, or
handle. There might be credentials that are no longer necessary to
the functioning of the workload that can be safely removed.

For credentials that are still required for the proper functioning
of the workload, there might be an opportunity to replace a
long-term credential with a temporary or short-term credential.
For example, instead of hard-coding an AWS secret access key,
consider replacing that long-term credential with a temporary
credential using IAM roles.

Some long-lived secrets might not be able to be removed or
replaced. These secrets can be stored in a service such as
[AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md"), where they can be centrally stored,
managed, and rotated on a regular basis.

An audit of the workload's source code and configuration files can
reveal many types of credentials. The following table summarizes
strategies for handling common types of credentials:

| Credential type                                  | Description                                                                                                    | Suggested strategy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IAM access keys                                  | AWS IAM access and secret keys used to assume IAM roles<br>inside of a workload                                | Replace: Use<br>[IAM<br>roles](../../../IAM/latest/UserGuide/id_roles_common-scenarios.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios.md") assigned to the compute instances (such as<br>[Amazon EC2](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md") or<br>[AWS Lambda](../../../lambda/latest/dg/lambda-intro-execution-role.md "../../../lambda/latest/dg/lambda-intro-execution-role.md")) instead. For interoperability with<br>third parties that require access to resources in your AWS account, ask if they support<br>[AWS cross-account access](../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md"). For mobile apps,<br>consider using temporary credentials through<br>[Amazon Cognito identity pools (federated identities)](../../../cognito/latest/developerguide/cognito-identity.md "../../../cognito/latest/developerguide/cognito-identity.md").<br>For workloads running outside of AWS, consider<br>[IAM<br>Roles Anywhere](../../../rolesanywhere/latest/userguide/introduction.md "../../../rolesanywhere/latest/userguide/introduction.md") or<br>[AWS Systems Manager Hybrid Activations](../../../systems-manager/latest/userguide/activations.md "../../../systems-manager/latest/userguide/activations.md"). For<br>containers see<br>[Amazon ECS task IAM role](../../../AmazonECS/latest/developerguide/task-iam-roles.md "../../../AmazonECS/latest/developerguide/task-iam-roles.md") or<br>[Amazon EKS node IAM role](../../../eks/latest/userguide/create-node-role.md "../../../eks/latest/userguide/create-node-role.md"). |
| SSH keys                                         | Secure Shell private keys used to log into Linux EC2<br>instances, manually or as part of an automated process | Replace: Use<br>[AWS Systems Manager](https://aws.amazon.com/blogs/mt/vr-beneficios-session-manager/ "https://aws.amazon.com/blogs/mt/vr-beneficios-session-manager/") or<br>[EC2<br>Instance Connect](../../../AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.md "../../../AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.md") to provide programmatic and human<br>access to EC2 instances using IAM roles.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Application and database credentials             | Passwords – plain text string                                                                                  | Rotate: Store credentials in<br>[AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") and establish automated rotation if<br>possible.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Amazon RDS and Aurora Admin Database credentials | Passwords – plain text string                                                                                  | Replace: Use the<br>[Secrets Manager integration with Amazon RDS](../../../AmazonRDS/latest/UserGuide/rds-secrets-manager.md "../../../AmazonRDS/latest/UserGuide/rds-secrets-manager.md") or<br>[Amazon Aurora](../../../AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.md "../../../AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.md"). In addition, some RDS database types can<br>use IAM roles instead of passwords for some use cases (for<br>more detail, see<br>[IAM<br>database authentication](../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md "../../../AmazonRDS/latest/UserGuide/UsingWithRDS.md")).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| OAuth tokens                                     | Secret tokens – plain text string                                                                              | Rotate: Store tokens in<br>[AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") and configure automated rotation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| API tokens and keys                              | Secret tokens – plain text string                                                                              | Rotate: Store in<br>[AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") and establish automated rotation if<br>possible.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

A common anti-pattern is embedding IAM access keys inside source
code, configuration files, or mobile apps. When an IAM access key
is required to communicate with an AWS service, use
[temporary
(short-term) security credentials](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md"). These short-term
credentials can be provided through
[IAM
roles for EC2](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md") instances,
[execution
roles](../../../lambda/latest/dg/lambda-intro-execution-role.md "../../../lambda/latest/dg/lambda-intro-execution-role.md") for Lambda functions,
[Cognito
IAM roles](../../../cognito/latest/developerguide/iam-roles.md "../../../cognito/latest/developerguide/iam-roles.md") for mobile user access, and
[IoT
Core policies](../../../iot/latest/developerguide/iot-policies.md "../../../iot/latest/developerguide/iot-policies.md") for IoT devices. When interfacing with third
parties, prefer
[delegating
access to an IAM role](../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_third-party.md") with the necessary access to your
account's resources rather than configuring an IAM user and
sending the third party the secret access key for that user.

There are many cases where the workload requires the storage of
secrets necessary to interoperate with other services and
resources.
[AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") is purpose built to securely manage these
credentials, as well as the storage, use, and rotation of API
tokens, passwords, and other credentials.

AWS Secrets Manager provides five key capabilities to ensure the
secure storage and handling of sensitive credentials:
[encryption
at rest](../../../secretsmanager/latest/userguide/security-encryption.md "../../../secretsmanager/latest/userguide/security-encryption.md"),

[encryption
in transit](../../../secretsmanager/latest/userguide/data-protection.md "../../../secretsmanager/latest/userguide/data-protection.md"),

[comprehensive
auditing](../../../secretsmanager/latest/userguide/monitoring.md "../../../secretsmanager/latest/userguide/monitoring.md"),

[fine-grained
access control](../../../secretsmanager/latest/userguide/auth-and-access.md "../../../secretsmanager/latest/userguide/auth-and-access.md"), and

[extensible
credential rotation](../../../secretsmanager/latest/userguide/rotating-secrets.md "../../../secretsmanager/latest/userguide/rotating-secrets.md"). Other secret management services from
AWS Partners or locally developed solutions that provide similar
capabilities and assurances are also acceptable.

When you retrieve a secret, you can use the Secrets Manager client
side caching components to cache it for future use. Retrieving a
cached secret is faster than retrieving it from Secrets Manager.
Additionally, because there is a cost for calling Secrets Manager
APIs, using a cache can reduce your costs. For all of the ways you
can retrieve secrets, see
[Get
secrets](../../../secretsmanager/latest/userguide/retrieving-secrets.md "../../../secretsmanager/latest/userguide/retrieving-secrets.md").

###### Note

Some languages may
require you to implement your own in-memory encryption for client
side caching.

### Implementation steps

1. Identify code paths containing hard-coded credentials using
   automated tools such as
   [Amazon CodeGuru](https://aws.amazon.com/codeguru/features/ "https://aws.amazon.com/codeguru/features/").
   1. Use Amazon CodeGuru to scan your code repositories. Once
      the review is complete, filter on
      Type=Secrets in CodeGuru to find
      problematic lines of code.

2. Identify credentials that can be removed or replaced.
   1. Identify credentials no longer needed and mark for
      removal.
   2. For AWS Secret Keys that are embedded in source code,
      replace them with IAM roles associated with the
      necessary resources. If part of your workload is outside
      AWS but requires IAM credentials to access AWS
      resources, consider
      [IAM
      Roles Anywhere](https://aws.amazon.com/blogs/security/extend-aws-iam-roles-to-workloads-outside-of-aws-with-iam-roles-anywhere/ "https://aws.amazon.com/blogs/security/extend-aws-iam-roles-to-workloads-outside-of-aws-with-iam-roles-anywhere/") or
      [AWS Systems Manager Hybrid Activations](../../../systems-manager/latest/userguide/activations.md "../../../systems-manager/latest/userguide/activations.md").

3. For other third-party, long-lived secrets that require the
   use of the rotate strategy, integrate Secrets Manager into
   your code to retrieve third-party secrets at runtime.
   1. The CodeGuru console can automatically
      [create
      a secret in Secrets Manager](https://aws.amazon.com/blogs/aws/codeguru-reviewer-secrets-detector-identify-hardcoded-secrets/ "https://aws.amazon.com/blogs/aws/codeguru-reviewer-secrets-detector-identify-hardcoded-secrets/") using the discovered
      credentials.
   2. Integrate secret retrieval from Secrets Manager into
      your application code.
      1. Serverless Lambda functions can use a
         language-agnostic
         [Lambda
         extension](../../../secretsmanager/latest/userguide/retrieving-secrets_lambda.md "../../../secretsmanager/latest/userguide/retrieving-secrets_lambda.md").
      2. For EC2 instances or containers, AWS provides
         example
         [client-side
         code for retrieving secrets from Secrets Manager](../../../secretsmanager/latest/userguide/retrieving-secrets.md "../../../secretsmanager/latest/userguide/retrieving-secrets.md") in several popular programming
         languages.

4. Periodically review your code base and re-scan to verify no
   new secrets have been added to the code.
   1. Consider using a tool such as
      [git-secrets](https://github.com/awslabs/git-secrets "https://github.com/awslabs/git-secrets")
      to prevent committing new secrets to your source code
      repository.

5. [Monitor
   Secrets Manager activity](../../../secretsmanager/latest/userguide/monitoring.md "../../../secretsmanager/latest/userguide/monitoring.md") for indications of
   unexpected usage, inappropriate secret access, or attempts
   to delete secrets.
6. Reduce human exposure to credentials. Restrict access to
   read, write, and modify credentials to an IAM role dedicated
   for this purpose, and only provide access to assume the role
   to a small subset of operational users.

## Resources

**Related best practices:**

- [SEC02-BP02 Use temporary
  credentials](sec_identities_unique.md "sec_identities_unique.md")
- [SEC02-BP05 Audit and rotate
  credentials periodically](sec_identities_audit.md "sec_identities_audit.md")

**Related documents:**

- [Getting
  Started with AWS Secrets Manager](../../../secretsmanager/latest/userguide/getting-started.md "../../../secretsmanager/latest/userguide/getting-started.md")
- [Identity
  Providers and Federation](../../../IAM/latest/UserGuide/id_roles_providers.md "../../../IAM/latest/UserGuide/id_roles_providers.md")
- [Amazon CodeGuru Introduces Secrets Detector](https://aws.amazon.com/blogs/aws/codeguru-reviewer-secrets-detector-identify-hardcoded-secrets/ "https://aws.amazon.com/blogs/aws/codeguru-reviewer-secrets-detector-identify-hardcoded-secrets/")
- [How
  AWS Secrets Manager uses AWS Key Management Service](../../../kms/latest/developerguide/services-secrets-manager.md "../../../kms/latest/developerguide/services-secrets-manager.md")
- [Secret
  encryption and decryption in Secrets Manager](../../../secretsmanager/latest/userguide/security-encryption.md "../../../secretsmanager/latest/userguide/security-encryption.md")
- [Secrets Manager blog entries](https://aws.amazon.com/blogs/security/tag/aws-secrets-manager/ "https://aws.amazon.com/blogs/security/tag/aws-secrets-manager/")
- [Amazon RDS announces integration with AWS Secrets Manager](https://aws.amazon.com/about-aws/whats-new/2022/12/amazon-rds-integration-aws-secrets-manager/ "https://aws.amazon.com/about-aws/whats-new/2022/12/amazon-rds-integration-aws-secrets-manager/")

**Related videos:**

- [Best Practices
  for Managing, Retrieving, and Rotating Secrets at Scale](https://youtu.be/qoxxRlwJKZ4 "https://youtu.be/qoxxRlwJKZ4")
- [Find
  Hard-Coded Secrets Using Amazon CodeGuru Secrets
  Detector](https://www.youtube.com/watch?v=ryK3PN--oJs "https://www.youtube.com/watch?v=ryK3PN--oJs")
- [Securing
  Secrets for Hybrid Workloads Using AWS Secrets Manager](https://www.youtube.com/watch?v=k1YWhogGVF8 "https://www.youtube.com/watch?v=k1YWhogGVF8")

**Related workshops:**

- [Store,
  retrieve, and manage sensitive credentials in AWS Secrets Manager](https://catalog.us-east-1.prod.workshops.aws/workshops/92e466fd-bd95-4805-9f16-2df07450db42/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/92e466fd-bd95-4805-9f16-2df07450db42/en-US")
- [AWS Systems Manager Hybrid Activations](https://mng.workshop.aws/ssm/capability_hands-on_labs/hybridactivations.html "https://mng.workshop.aws/ssm/capability_hands-on_labs/hybridactivations.html")
