# Data protection in Amazon Aurora DSQL

The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in . As described in this model, is responsible for protecting the
global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining
control over your content that is hosted on this infrastructure. You are also responsible for
the security configuration and management tasks for the that you use. For more information about
data privacy, see the [Data Privacy
FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/"). For information about data protection in Europe, see the
[Shared
Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the _Security
Blog_.

For data protection purposes, we recommend that you protect credentials and set up
individual users with AWS IAM Identity Center or AWS Identity and Access Management. That way, each user is given only the permissions
necessary to fulfill their job duties. We also recommend that you secure your data in the
following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with resources. We require TLS 1.2 and recommend TLS
  1.3.
- Set up API and user activity logging with AWS CloudTrail. For information about using trails
  to capture activities, see [Working with trails](../../../awscloudtrail/latest/userguide/cloudtrail-trails.md "../../../awscloudtrail/latest/userguide/cloudtrail-trails.md") in
  the _User Guide_.
- Use encryption solutions, along with all default security controls within
  AWS services.
- Use advanced managed security services such as Amazon Macie, which assists in discovering
  and securing sensitive data that is stored in Amazon S3.
  We strongly recommend that you never put confidential or sensitive information, such as your
  customers email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with or other using the console, API,
  AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be
  used for billing or diagnostic logs. If you provide a URL to an external server, we strongly
  recommend that you do not include credentials information in the URL to validate your request to
  that server.

## Data encryption

Amazon Aurora DSQL provides a highly durable storage infrastructure designed for
mission-critical and primary data storage. Data is redundantly stored on multiple devices
across multiple facilities in an Aurora DSQL Region.

### Encryption in transit

By default, encryption in transit is configured for you. Aurora DSQL uses TLS to encrypt all traffic between your SQL client and Aurora DSQL.

Encryption and signing of data in transit between AWS CLI, SDK, or API clients and Aurora DSQL endpoints:

- Aurora DSQL provides HTTPS endpoints for encrypting data in transit.
- To protect the integrity of API requests to Aurora DSQL, API calls must be signed by the caller.
  Calls are signed by an X.509 certificate or the customer's AWS secret
  access key according to the Signature Version 4 Signing Process (Sigv4). For
  more information, see [Signature Version 4 Signing Process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") in the _AWS General Reference_.
- Use the AWS CLI or one of the AWS SDKs to make requests to AWS. These tools
  automatically sign the requests for you with the access key that you specify
  when you configure the tools.

#### FIPS compliance

Aurora DSQL dataplane endpoints (cluster endpoints used for database connections) use FIPS 140-2 validated cryptographic modules by default. No separate FIPS endpoints are required for cluster connections.

For control plane operations, Aurora DSQL provides dedicated FIPS endpoints in supported regions. For more information about control plane FIPS endpoints, see [Aurora DSQL endpoints and quotas](../../../general/latest/gr/dsql.md "../../../general/latest/gr/dsql.md") in the _AWS General Reference_.

For encryption at rest, see [Encryption at rest in Aurora DSQL](data-encryption.md#encryption-at-rest "data-encryption.md#encryption-at-rest").

### Inter-network traffic privacy

Connections are protected both between Aurora DSQL and on-premises applications and between
Aurora DSQL and other AWS resources within the same AWS Region.

You have two connectivity options between your private network and AWS:

- An AWS Site-to-Site VPN connection. For more information, see [What is
  AWS Site-to-Site VPN?](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md")
- An AWS Direct Connect connection. For more information, see [What is AWS Direct Connect?](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md")

You get access to Aurora DSQL through the network by using
AWS-published API operations. Clients must support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS
  1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE
  (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral
  Diffie-Hellman). Most modern systems such as Java 7 and later support
  these modes.

## Data Protection in witness Regions

When you create a multi-Region cluster, a witness Region helps enable automated failure recovery by participating in synchronous replication of encrypted transactions.
If a peered cluster becomes unavailable, the witness Region remains available to validate and process database writes, ensuring no loss of availability.

Witness Regions protect and secure your data through these design features:

- The witness Region receives and stores only encrypted transaction logs. It never hosts, stores or transmits your encryption keys.
- The witness Region focuses soley on write transaction logging and quorum functions. It can't read your data by design.
- The witness Region operates without cluster connection endpoints or query processors. This prevents user database access.

For more information on witness Regions, see [Configuring multi-Region clusters](configuring-multi-region-clusters.md "configuring-multi-region-clusters.md").
