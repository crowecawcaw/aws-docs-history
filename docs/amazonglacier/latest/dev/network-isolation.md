**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) will no longer accept new customers starting December 15, 2025, with no impact to existing customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Infrastructure Security in Amazon Glacier

As a managed service, Amazon Glacier (Amazon Glacier) is protected by the AWS global network security
procedures that are described in the [Amazon
Web Services: Overview of Security Processes](https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf "https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf").

Access to Amazon Glacier via the network is through AWS published APIs. Clients must support
Transport Layer Security (TLS) 1.2. We recommend TLS 1.3 or later. Clients must also support
cipher suites with Perfect Forward Secrecy (PFS) such as Ephemeral Diffie-Hellman (DHE) or
Elliptic Curve Diffie-Hellman Ephemeral (ECDHE). Most modern systems such as Java 7 and
later support these modes. Additionally, requests must be signed using an access key ID and
a secret access key that is associated with an IAM principal, or you can use the [AWS Security Token Service (AWS STS)](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") to generate temporary security
credentials to sign requests.

## VPC Endpoints

A virtual private cloud (VPC) endpoint enables you to privately connect your VPC to
supported AWS services and VPC endpoint services powered by AWS PrivateLink without
requiring an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection.
Although Amazon Glacier does not support VPC endpoints directly, you can take advantage of Amazon S3
VPC endpoints if you access Amazon Glacier as a storage tier integrated with Amazon S3.

For more information about Amazon S3 lifecycle configuration and transitioning objects to
the Amazon Glacier storage class, see [Object Lifecycle Management](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") and
[Transitioning Objects](../../../AmazonS3/latest/userguide/lifecycle-transition-general-considerations.md "../../../AmazonS3/latest/userguide/lifecycle-transition-general-considerations.md") in the _Amazon Simple Storage Service User Guide_. For more
information about VPC endpoints, see [VPC
Endpoints](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md") in the _Amazon VPC User Guide_.
