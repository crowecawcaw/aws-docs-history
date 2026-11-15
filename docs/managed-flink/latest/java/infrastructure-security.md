

# Infrastructure security in Managed Service for Apache Flink
<a name="infrastructure-security"></a>

As a managed service, Managed Service for Apache Flink is protected by the AWS global network security procedures that are described in the [Amazon Web Services: Overview of Security Processes](https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf) whitepaper.

You use AWS published API calls to access Managed Service for Apache Flink through the network. All API calls to Managed Service for Apache Flink are secured via Transport Layer Security (TLS) and authenticated via IAM. Clients must support TLS 1.2 or later. Clients must also support cipher suites with perfect forward secrecy (PFS) such as Ephemeral Diffie-Hellman (DHE) or Elliptic Curve Ephemeral Diffie-Hellman (ECDHE). Most modern systems such as Java 7 and later support these modes.

Additionally, requests must be signed by using an access key ID and a secret access key that is associated with an IAM principal. Or you can use the [AWS Security Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/Welcome.html) (AWS STS) to generate temporary security credentials to sign requests.

When you import or export an enhanced snapshot, Managed Service for Apache Flink accesses your Amazon S3 bucket from service-owned VPCs through Amazon S3 gateway endpoints. The requests use the Regional Amazon S3 endpoint over HTTPS. Managed Service for Apache Flink makes these requests with temporary credentials for the IAM role in the import or export request. A session policy limits these credentials to the bucket prefix in the request and to the Amazon S3 and AWS KMS actions that the transfer needs. For more information, see [IAM role for import and export](security-iam-snapshots.md#security-iam-snapshots-transfer-role).