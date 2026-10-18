

# Data protection in AWS Agent Registry
<a name="registry-data-protection"></a>

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in AWS Agent Registry. As described in this model, we are responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. This content includes the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq) on the AWS website.

For data protection purposes, we recommend that you protect AWS account credentials and set up individual user accounts with IAM. That way each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources.
+ Set up API and user activity logging with AWS CloudTrail.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing personal data that is stored in Amazon S3.

We strongly recommend that you never put sensitive identifying information, such as your customers' account numbers, into free-form fields such as a **Name** field. This includes when you work with AWS Agent Registry or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into AWS Agent Registry or other services might get picked up for inclusion in diagnostic logs. When you provide a URL to an external server, don’t include credentials information in the URL to validate your request to that server.

## Validate record metadata before you act on it
<a name="registry-consumer-validation"></a>

Publishers provide record metadata, including package identifiers, repository URLs, and remote endpoint URLs. AWS Agent Registry checks this metadata only against the schema for the record’s descriptor. It doesn’t verify the packages, repositories, or endpoints that a record references. Under the AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/), you are responsible for validating these fields. Validate them before your agent installs, downloads, or connects to anything a record references, in the same way you validate input from any external source. For the fields that each descriptor supports, see [Supported record types and descriptors](registry-supported-record-types.md).

To validate record metadata, use patterns such as the following:
+ Install packages only from an allowlist or from a package repository that you control, such as AWS CodeArtifact, and pin each package to a specific version.
+ Download source code only from repository hosts and owners that you allow.
+ Connect only to MCP server endpoints whose URL scheme and domain you allow.

**Topics**