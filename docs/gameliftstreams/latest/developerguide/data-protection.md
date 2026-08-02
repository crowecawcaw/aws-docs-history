# Data protection in Amazon GameLift Streams

The AWS
[shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")

applies to data protection in Amazon GameLift Streams.

As described in this model, AWS is
responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are
responsible for maintaining control over your content that is hosted on this infrastructure.
You are also responsible for the security configuration and management tasks for the AWS services
that you use.

For more information about data privacy, see
[Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/").

For information about data protection in Europe, see the
[General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/ "https://aws.amazon.com/compliance/gdpr-center/").

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
- **Customer-supplied metadata** – Customers can provide metadata to Amazon GameLift Streams APIs including
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
- **Session credentials** – When you provide an
  IAM role ARN on `StartStreamSession`, Amazon GameLift Streams assumes the role and provides short-lived
  temporary credentials to the application. Amazon GameLift Streams stores credentials only in memory on the streaming
  instance for the duration of the session. Amazon GameLift Streams never writes credentials to disk, never includes them in service
  logs, and never returns them in API responses. When the session ends, Amazon GameLift Streams clears credentials from
  memory. Amazon GameLift Streams stores only the role ARN (a resource identifier, not a credential) in service
  databases, subject to the existing session record retention policies.
- **Stream URLs** – A stream URL grants temporary, unauthenticated access to start a stream
  session. The stream URL embeds a bearer token, so anyone who has the complete URL can start a session until the stream URL expires, is
  revoked, or reaches its usage limit. Amazon GameLift Streams does not require the end user to present AWS credentials when activating a stream URL. Treat
  the full stream URL as a credential: distribute it only over trusted channels, give it the shortest workable expiration and usage limit,
  and revoke it when it is no longer needed. For more information, see [Security best practices for Amazon GameLift Streams](security-best-practices.md "security-best-practices.md") and [Share stream sessions with stream URLs](stream-urls.md "stream-urls.md").

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

In the context of multi-location stream groups, to stream an application from any location in the stream group that has
been allocated streaming capacity, Amazon GameLift Streams securely replicates applications to those locations.

Similarly, Amazon GameLift Streams saves log data and session files, when requested, to customer-named Amazon S3 buckets at the end of a session. If
the bucket is not in the same location as the session, Amazon GameLift Streams transfers the files securely to the AWS Region where the bucket is
located.

When session credentials are configured, Amazon GameLift Streams fetches credentials from AWS STS over
TLS-encrypted connections. Your application receives credentials securely within the
session's isolated environment.

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
and were modified while the application was running. Nor does it remove any Windows registry keys that the application had added. You
must avoid damaging the integrity of the overall operating system. Applications are executed as
the Administrator user, which can permit modification to critical system-level files, including changes that persist across multiple
sessions. It is your responsibility to secure your applications and guard against creating unsafe or unstable operating
system modifications.

You are responsible for cleaning up those modified files and added registry keys from previous sessions when the application
launches. This is an important step to protect confidential or sensitive information that the application writes to the user's profile
directory. To do this, you can write a custom script that performs the following actions:

- Restore any files outside of the `%USERPROFILE%` directory that were modified by the application.
- Clean up any sensitive or user-specific registry keys that the application added.

## Encryption key management

The service uses AWS managed keys for encryption. Each Region uses a separate KMS key. Customer managed keys are not supported.

Application files provided to Amazon GameLift Streams cannot be republished or exported from the service. You can use the service console or
APIs to delete applications. Drives which previously held these application files can be completely purged by deleting the associated stream
groups.

## Inter-network traffic privacy

Amazon GameLift Streams uses public-facing networks to host stream sessions. Each stream group consists of one or more service-managed VPC
networks which are isolated from other stream groups and from other customers. Inbound network connections are denied except for
authenticated, service-brokered WebRTC stream connections. Your applications can connect out from these VPCs to other public addresses
without restriction.

By default, your application data is not publicly accessible. Management API calls require AWS-authenticated credentials, and you can
integrate Amazon GameLift Streams into your own client web application that makes authenticated calls to start and display a stream.

Amazon GameLift Streams also provides stream URLs, a deliberate mechanism for granting temporary, unauthenticated access to start a stream session. When
you create a stream URL, you are intentionally allowing anyone who has the stream URL to start a session in a supported web browser, without
AWS credentials and without building your own client. Because the stream URL itself is the credential, treat every stream URL as a bearer
credential and control its distribution, expiration, and usage limit accordingly. Stream URLs are the only supported way to make a stream
publicly reachable without your own authenticated client; all other service interactions continue to require AWS-authenticated API calls.
For more information, see [Share stream sessions with stream URLs](stream-urls.md "stream-urls.md") and [Security best practices for Amazon GameLift Streams](security-best-practices.md "security-best-practices.md").
