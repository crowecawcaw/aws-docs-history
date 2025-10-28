# Infrastructure Security in Amazon Aurora DSQL

As a managed service, Amazon Aurora DSQL is protected by the AWS global network security
procedures that are described in [Best Practices for Security, Identity, & Compliance](https://aws.amazon.com/https://aws.amazon.com/architecture/security-identity-compliance "https://aws.amazon.com/https://aws.amazon.com/architecture/security-identity-compliance").

You use AWS published API calls to access Aurora DSQL through the network. Clients must
support Transport Layer Security (TLS) 1.2 or later. Clients must also support cipher suites
with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic
Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these
modes.

Additionally, requests must be signed by using an access key ID and a secret access key
that is associated with an IAM principal. Or you can use the [AWS Security Token Service](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") (AWS STS) to generate temporary
security credentials to sign requests.
