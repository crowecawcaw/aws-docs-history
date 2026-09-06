

# Data protection in AWS Security Agent
<a name="data-protection"></a>

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in AWS Security Agent. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For information about data protection in Europe, see the [AWS Shared Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/) blog post on the *AWS Security Blog*. For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
+ Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-working-with-trails.html) in the *AWS CloudTrail User Guide*.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with AWS Security Agent or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.

## Encryption at rest
<a name="_encryption_at_rest"></a>

AWS Security Agent encrypts all data at rest using AWS-managed encryption keys by default. This includes:
+  **Design documents and code** – All design documents, code repositories, and application artifacts you provide for security reviews are encrypted using AES-256 encryption.
+  **Security findings** – All security findings, vulnerability reports, and remediation recommendations are encrypted at rest.
+  **Configuration data** – Security requirements, custom policies, and service configurations are encrypted.
+  **Audit logs** – All service activity logs and audit trails are encrypted.

AWS Security Agent uses AWS Key Management Service (AWS KMS) to manage encryption keys. You can optionally use a customer managed key to encrypt your data, giving you full control over the encryption keys that protect your resources. For more information, see [Customer managed keys for AWS Security Agent](customer-managed-keys.md).

## Encryption in transit
<a name="_encryption_in_transit"></a>

AWS Security Agent encrypts all data in transit using Transport Layer Security (TLS) 1.2 or higher. This applies to:
+  **API communications** – All API calls between your applications and AWS Security Agent use HTTPS with TLS encryption.
+  **Console access** – The AWS Security Agent console is accessed over HTTPS.
+  **Repository connections** – Connections to GitHub and other code repositories use encrypted protocols.
+  **Agent communications** – All communications between the AWS Security Agent service and penetration testing agents use encrypted channels.

## Key management
<a name="_key_management"></a>

AWS Security Agent uses AWS Key Management Service (AWS KMS) to manage encryption keys. By default, data is encrypted using AWS-managed keys. You can optionally specify a customer managed key when creating resources such as Agent Spaces and integrations. For more information, see [Customer managed keys for AWS Security Agent](customer-managed-keys.md).

## Internetwork traffic privacy
<a name="_internetwork_traffic_privacy"></a>

AWS Security Agent uses the public internet to communicate with cloud-hosted source control providers (GitHub, GitLab, Bitbucket) and Confluence Cloud.

For self-hosted providers (GitLab Self-Managed, GitHub Enterprise Server), you can configure private connections using Amazon VPC Lattice to keep all traffic within the AWS network. For more information, see [Connect to privately hosted source control](connect-private-connection.md).

In the default configuration, AWS Security Agent uses the public internet to reach your app for penetration testing. You can optionally configure penetration tests to use a VPC to access your application. For more information, see [Connect agent to private VPC resources](connect-agent-vpc.md).

## Cross-Region data processing
<a name="cross-region-processing"></a>

AWS Security Agent uses [cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) to optimize available compute resources and model availability. Depending on the Region where the request originates, we might process input prompts and output results in a different Region.
+ In US East (N. Virginia) – `us-east-1`, US West (Oregon) – `us-west-2`, Asia Pacific (Sydney) – `ap-southeast-2`, Asia Pacific (Tokyo) – `ap-northeast-1`, Europe (Frankfurt) – `eu-central-1`, and Europe (Ireland) – `eu-west-1`, AWS Security Agent uses [geographic cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/geographic-cross-region-inference.html). For most features, data processing remains within the geographic boundary (such as US, EU, Australia, or Japan) where the request originated. For Code Remediation, requests from Australia and Japan are processed in the European Union. For feature-specific routing details, see the [Cross Region Inference table](security-best-practices.md).
+ In Asia Pacific (Mumbai) – `ap-south-1`, Asia Pacific (Singapore) – `ap-southeast-1`, and South America (São Paulo) – `sa-east-1`, AWS Security Agent uses [global cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/global-cross-region-inference.html). We might process input prompts and output results in any [commercial AWS Region](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#region).

In all cases, your data remains stored only in the Region where the request originated. All data transmitted during cross-Region operations remains on the AWS network and does not traverse the public internet. We encrypt data in transit between AWS Regions.

Cross-Region inference is always enabled and cannot be opted out of. For details on which Regions process requests for each feature, see the Cross Region Inference section in [Security best practices for AWS Security Agent](security-best-practices.md).

**Note**  
For GitHub Enterprise Cloud with data residency, AWS Security Agent processes your repository content in the Region of your AWS Security Agent instance. If that Region differs from your tenant’s GitHub data residency Region, AWS Security Agent processes your content outside that Region. To connect a data residency tenant, see [Connect AWS Security Agent to GitHub Enterprise](connect-github-enterprise.md).

## Data deletion
<a name="_data_deletion"></a>

When you delete data from AWS Security Agent:
+ The data is marked for deletion and is no longer accessible through the service.
+ The data is deleted from all AWS Security Agent systems within 30 days.

To delete your data

1. In the AWS console, navigate to AWS Security Agent.

1. Choose the data you want to delete (security reviews, findings, or custom requirements).

1. Choose **Delete** and confirm the deletion.