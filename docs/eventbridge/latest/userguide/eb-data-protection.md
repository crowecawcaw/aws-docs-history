# Data protection in Amazon EventBridge

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in Amazon EventBridge. As described in this model, AWS is
responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are
responsible for maintaining control over your content that is hosted on this infrastructure.
You are also responsible for the security configuration and management tasks for the AWS services
that you use. For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/"). For information about data protection in Europe, see the [AWS Shared
Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the _AWS Security
Blog_.

For data protection purposes, we recommend that you protect AWS account
credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
- Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](../../../awscloudtrail/latest/userguide/cloudtrail-trails.md "../../../awscloudtrail/latest/userguide/cloudtrail-trails.md") in the _AWS CloudTrail User Guide_.
- Use AWS encryption solutions, along with all default security controls within AWS services.
- Use advanced managed security services such as Amazon Macie, which assists in discovering
  and securing sensitive data that is stored in Amazon S3.
- If you require FIPS 140-3 validated cryptographic modules when accessing AWS through
  a command line interface or an API, use a FIPS endpoint. For more information about the
  available FIPS endpoints, see [Federal
  Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").
  We strongly recommend that you never put confidential or sensitive information, such as your
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with EventBridge or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

## Data encryption in EventBridge

EventBridge provides both _encryption at rest_ and
_encryption in transit_ to protect your data:

- Encryption at rest

EventBridge integrates with AWS Key Management Service (KMS) to encrypt
stored data. By default, EventBridge uses an AWS owned key
to encrypt data. You can also specify for EventBridge to use a customer managed key for specific features instead.

- Encryption in transit

EventBridge encrypts data that passes between EventBridge and
other services by using Transport layer Security (TLS).

For event buses, this
includes during an event being sent to EventBridge, as well as when
EventBridge sends an event to a rule target.

## Encryption at rest in Amazon EventBridge

EventBridge provides transparent server-side encryption by integrating with
AWS Key Management Service (KMS). Encryption of data at rest by default helps reduce
the operational overhead and complexity involved in protecting sensitive data. At
the same time, it enables you to build secure applications that meet strict
encryption compliance and regulatory requirements.

By default, EventBridge uses an AWS owned key to encrypt
data. You can specify for EventBridge to use customer managed keys for specific
resources instead.

The following table lists the artifacts that EventBridge encrypts at rest, by
resource:

| **Resource**                                                        | **Details**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | **AWS owned key** | **Customer managed key**                                                         |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | -------------------------------------------------------------------------------- |
| [API destinations](eb-api-destinations.md "eb-api-destinations.md") | Connection authorization parameters are stored in an AWS Secrets Manager secret.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Supported         | [Supported](encryption-connections.md "encryption-connections.md")               |
| [Archives](eb-archive.md "eb-archive.md")                           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Supported         | [Supported](encryption-archives.md "encryption-archives.md")                     |
| [Connections](eb-target-connection.md "eb-target-connection.md")    | Connection authorization parameters are stored in an AWS Secrets Manager secret.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Supported         | [Supported](encryption-connections.md "encryption-connections.md")               |
| [Event buses](eb-event-bus.md "eb-event-bus.md")                    | Includes:<br>• Events from [custom](eb-putevents.md "eb-putevents.md") and [partner](eb-saas.md "eb-saas.md") sources<br>Event data includes all fields contained in the `event-detail` element of the event.<br>EventBridge does not encrypt event metadata.<br>• [Rule event patterns](eb-event-patterns.md "eb-event-patterns.md").<br>• Rule [target](eb-targets.md "eb-targets.md") information, including input, input transformers, and configuration parameters.<br>• For [event bus logging](eb-event-bus-logs.md "eb-event-bus-logs.md"), the `detail` and `error` sections of log records. | Supported         | [Supported](eb-encryption-event-bus-cmkey.md "eb-encryption-event-bus-cmkey.md") |
| [Pipes](eb-pipes.md "eb-pipes.md")                                  | Includes:<br>• [Event patterns](eb-event-patterns.md "eb-event-patterns.md")<br>• [Input transformers](eb-pipes-input-transformation.md "eb-pipes-input-transformation.md")<br>• [Execution data](eb-pipes-logs.md#eb-pipes-logs-execution-data "eb-pipes-logs.md#eb-pipes-logs-execution-data") in logs<br>Events flowing through a pipe are never stored at rest.                                                                                                                                                                                                                                   | Supported         | [Supported](eb-encryption-pipes-cmkey.md "eb-encryption-pipes-cmkey.md")         |

###### Important

We strongly recommend that you never put confidential or sensitive information
in the following artifacts, as they are not encrypted at rest:

- Event bus names
- Rule names
- Shared resources, such at tags
