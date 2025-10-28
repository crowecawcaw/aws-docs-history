# Data protection in Amazon GameLift Streams

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in Amazon GameLift Streams. As described in this model, AWS is
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
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Amazon GameLift Streams or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

Amazon GameLift Streams handles service-specific data as follows:

- **Customer-supplied applications** – Amazon GameLift Streams stores customer data, if provided, in internal
  service-managed Amazon S3 buckets and on NVME storage drives attached to Amazon EC2 instances. All data is stored with service-managed encryption at
  rest. There is no direct customer access to this copy of the data. To delete an application, use the Amazon GameLift Streams console or the service
  API.
- **Customer-supplied metadata** – Customers may provide metadata to Amazon GameLift Streams APIs including
  descriptions, connection information, and opaque identifiers such as customer IDs. This metadata is always associated with specific
  customer resources.
- **Customer-generated data** – If an application writes new data as part of its normal operation,
  this customer-generated data is retained until the end of the user session. At the end of the session, generated data can optionally be
  exported to an Amazon S3 bucket destination of the customer's choice. Customer-generated data otherwise does not leave the Amazon EC2 instance where
  it was generated. For more information about data handling, refer to the topics on [Session
  isolation](#data-security-linux "#data-security-linux").
- **Metrics and event data** – Amazon GameLift Streams metric and event data, which can be accessed through the
  Amazon GameLift Streams console or by calls to the service API. Data is available on applications, stream groups, and stream sessions. Authorized users
  can also access this data through Amazon CloudWatch and CloudWatch Events.

###### Important

If you provide customer IDs or other identifiers to Amazon GameLift Streams, it is expected that these values are anonymized references and do not
contain any sensitive or personal information. Amazon GameLift Streams does not redact any metadata fields.

For more information about data protection, see the [AWS
shared responsibility model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the _AWS Security Blog_.

## Encryption at rest

At-rest encryption of Amazon GameLift Streams-specific data is handled as follows:

- Application content is stored in service-managed encrypted Amazon S3 buckets and additionally on hardware-encrypted NVME drives attached
  to service-managed Amazon EC2 instances.

## Encryption in transit

Calls to the Amazon GameLift Streams APIs are made over a secure (SSL) connection and authenticated using [AWS Signature Version 4](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") (when connecting through the AWS CLI or AWS SDK, signing
is handled automatically). Calling entities use security credentials, which are authenticated by applying the IAM access policies that are
defined for Amazon GameLift Streams resources.

In the context of multi-location stream groups, in order to stream an application from any location in the stream group that has
been allocated streaming capacity, Amazon GameLift Streams securely replicates applications to those locations.

Similarly, Amazon GameLift Streams will save log data and session files, when requested, to customer-named Amazon S3 buckets at the end of a session. If
the bucket is not in the same location as the session, Amazon GameLift Streams will transfer the files securely to the AWS Region where the bucket is
located.

## Protection of end-user streams

Individual end-user streams are direct connections between the end-user's web browser and the Amazon GameLift Streams backend hosts. Those streams are
protected with industry-standard WebRTC encryption, and both endpoints of the stream are positively identified by cryptographic
identifiers which are part of the `SignalRequest` and `SignalResponse` values negotiated through the stream session
APIs.

Data channel messages are also covered by the WebRTC encryption used for streams. These messages are decrypted by Amazon GameLift Streams and passed
locally on-the-host to the customer's application through an unencrypted API. If end-to-end encryption which even the Amazon GameLift Streams service
cannot decrypt is required, this additional layer of encryption is the responsibility of the application developer.

## Session isolation in Linux stream classes

On Linux stream classes (Ubuntu and Proton runtimes), Amazon GameLift Streams uses _container isolation_. Every session runs in a new
Linux container which is discarded after use. This means each new session runs in a fresh environment, isolated from other users sharing the
compute resource (if running in a shared-resource stream class). No data from prior sessions exists when a new session starts up.

## Session isolation in Windows stream classes

On Windows stream classes (Microsoft Windows Server runtimes), Amazon GameLift Streams uses _software isolation_. The service relies
on a software agent to reset critical system state between sessions. Some folders are preserved across multiple sessions to allow for
performance optimizations, such as on-host disk caching. The software agent automatically removes any files that were generated in the user's
profile directory during the prior stream session. However, the agent does not remove any files that existed prior to the application running
and were modified while the application was running. Nor does it remove any Windows registry keys that the application had added. Customers
should be aware that it is their responsibility to avoid damaging the integrity of the overall operating system. Applications are executed as
the Administrator user, which may permit modification to critical system-level files, including changes that persist across multiple
sessions. It is the responsibility of the customer to secure their applications and guard against creating unsafe or unstable operating
system modifications.

Customers are responsible for cleaning up those modified files and added registry keys from previous sessions when the application
launches. This is an important step to protect confidential or sensitive information that the application writes to the user's profile
directory. To do this, customers can write their own custom script that performs the following actions:

- Restore any files outside of the `%USERPROFILE%` directory that were modified by the application.
- Clean up any sensitive or user-specific registry keys that the application added.

## Encryption key management

The service uses AWS-managed encryption keys. Each region uses a separate KMS key. Customer-managed keys (CMKs) are not supported.

Application files provided to Amazon GameLift Streams cannot be republished or exported from the service. The customer can use the service console or
APIs to delete applications. Drives which previously held these application files can be completely purged by deleting the associated stream
groups.

## Inter-network traffic privacy

Amazon GameLift Streams uses public-facing networks to host stream sessions. Each stream group consists of one or more service-managed VPC
networks which are isolated from other stream groups and from other customers. Inbound network connections are denied except for
authenticated, service-brokered WebRTC stream connections. Customer applications may connect out from these VPCs to other public addresses
without restriction.

Additionally, there is no way for a customer to make a stream or their application data publicly-accessible using service API calls or
settings alone. All service interactions are gated by AWS-authenticated API calls. If the customer wishes to make a stream accessible to the
public they must create their own client web application which makes the authenticated calls to start and display a stream.
