# Data protection in AWS Security Agent

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") applies to data protection in AWS Security Agent. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For information about data protection in Europe, see the [AWS Shared Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the _AWS Security Blog_.
For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
- Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](../../../awscloudtrail/latest/userguide/cloudtrail-working-with-trails.md "../../../awscloudtrail/latest/userguide/cloudtrail-working-with-trails.md") in the _AWS CloudTrail User Guide_.
- Use AWS encryption solutions, along with all default security controls within AWS services.
- Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
- If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").
  We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with AWS Security Agent or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.

## Encryption at rest

AWS Security Agent encrypts all data at rest using AWS-managed encryption keys by default. This includes:

- **Design documents and code** – All design documents, code repositories, and application artifacts you provide for security reviews are encrypted using AES-256 encryption.
- **Security findings** – All security findings, vulnerability reports, and remediation recommendations are encrypted at rest.
- **Configuration data** – Security requirements, custom policies, and service configurations are encrypted.
- **Audit logs** – All service activity logs and audit trails are encrypted.

AWS Security Agent uses AWS Key Management Service (AWS KMS) to manage encryption keys. You can optionally use a customer managed key to encrypt your data, giving you full control over the encryption keys that protect your resources. For more information, see [Customer managed keys for AWS Security Agent](customer-managed-keys.md "customer-managed-keys.md").

## Encryption in transit

AWS Security Agent encrypts all data in transit using Transport Layer Security (TLS) 1.2 or higher. This applies to:

- **API communications** – All API calls between your applications and AWS Security Agent use HTTPS with TLS encryption.
- **Console access** – The AWS Security Agent console is accessed over HTTPS.
- **Repository connections** – Connections to GitHub and other code repositories use encrypted protocols.
- **Agent communications** – All communications between the AWS Security Agent service and penetration testing agents use encrypted channels.

## Key management

AWS Security Agent uses AWS Key Management Service (AWS KMS) to manage encryption keys. By default, data is encrypted using AWS-managed keys. You can optionally specify a customer managed key when creating resources such as Agent Spaces and integrations. For more information, see [Customer managed keys for AWS Security Agent](customer-managed-keys.md "customer-managed-keys.md").

## Internetwork traffic privacy

AWS Security Agent uses the public internet to communicate with cloud-hosted source control providers (GitHub, GitLab, Bitbucket) and Confluence Cloud.

For self-hosted providers (GitLab Self-Managed, GitHub Enterprise Server), you can configure private connections using Amazon VPC Lattice to keep all traffic within the AWS network. For more information, see [Connect to privately hosted source control](connect-private-connection.md "connect-private-connection.md").

In the default configuration, AWS Security Agent uses the public internet to reach your app for penetration testing. You can optionally configure penetration tests to use a VPC to access your application. For more information, see [Connect agent to private VPC resources](connect-agent-vpc.md "connect-agent-vpc.md").

## Data deletion

When you delete data from AWS Security Agent:

- The data is marked for deletion and is no longer accessible through the service.
- The data is deleted from all AWS Security Agent systems within 30 days.

To delete your data

1. In the AWS console, navigate to AWS Security Agent.
2. Choose the data you want to delete (security reviews, findings, or custom requirements).
3. Choose **Delete** and confirm the deletion.
