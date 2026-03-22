# Using hybrid post-quantum TLS with Amazon S3

Amazon S3 supports a hybrid post-quantum key exchange option for the TLS network encryption
protocol. You can use this TLS option when you make requests to Amazon S3 endpoints utilizing TLS
1.3. The classic cipher suites that S3 supports for TLS sessions make brute force attacks on
the key exchange mechanisms infeasible with current technology. However, if a
cryptographically relevant quantum computer becomes practical in the future, the classic
cipher suites used in TLS key exchange mechanisms will be susceptible to these attacks. At
present, the industry is aligned on hybrid post-quantum key exchange that combines classic
and post-quantum elements to ensure that your TLS connection is at least as strong as it
would be with classic cipher suites. Amazon S3 supports hybrid PQ-TLS, in compliance with the
industry-standard IANA specification, today

If you’re developing applications that rely on the long-term confidentiality of data
passed over a TLS connection, you should consider a plan to migrate to post-quantum
cryptography before large-scale quantum computers become available for use. As part of the
shared responsibility model, S3 enables quantum-safe cryptography on our service endpoints.
As browsers and applications enable PQ-TLS on their side, S3 will choose the strongest
possible configuration to secure data in transit.

**Supported endpoint types and
AWS Regions**

Post-quantum TLS for Amazon S3 is available in all AWS Regions. For a list of S3 endpoints for
each AWS Region, see [Amazon Simple Storage Service
endpoints and quotas](../../../general/latest/gr/s3.md "../../../general/latest/gr/s3.md") in the _Amazon Web Services General Reference_.

###### Note

Hybrid post-quantum TLS is supported for all S3 endpoints except for AWS PrivateLink for Amazon S3,
Multi-Region Access Points, and S3 Vectors.

## Using hybrid post-quantum TLS with Amazon S3

You must configure the client that makes requests to Amazon S3 to support hybrid post-quantum
TLS. When setting up your HTTP client test environment or production environments, be
aware of the following information:

**Encryption in Transit**

Hybrid post-quantum TLS is only used for encryption in transit. This protects your data
while it is traveling from your client to the S3 endpoint. This new support combined
with Amazon S3’s server-side encryption by default utilizing AES-256
algorithms offers customers quantum-resistant encryption both in-transit and at-rest.
For more information about server-side encryption in Amazon S3, see [Protecting data with server-side encryption](serv-side-encryption.md "serv-side-encryption.md").

**Supported Clients**

The use of hybrid post-quantum TLS requires using a client that supports this functionality.
AWS SDKs and tools have cryptographic capabilities and configuration that differ across
languages and runtimes. To learn more about post-quantum cryptography for specific
tools, see [Enabling hybrid
post-quantum TLS](../../../payment-cryptography/latest/userguide/pqtls-details.md "../../../payment-cryptography/latest/userguide/pqtls-details.md").

###### Note

PQ-TLS key exchange details for requests to Amazon S3 are not available in AWS CloudTrail events or S3 server access logs.

## Learn more about post-quantum TLS

For more information about using hybrid post-quantum TLS, see the following
resources.

- To learn about post-quantum cryptography at AWS, including links to blog posts and
  research papers, see [Post-Quantum Cryptography for AWS](https://aws.amazon.com/security/post-quantum-cryptography/ "https://aws.amazon.com/security/post-quantum-cryptography/").
- For information about s2n-tls, see [Introducing s2n-tls, a New Open Source TLS Implementation](https://aws.amazon.com/blogs/security/introducing-s2n-a-new-open-source-tls-implementation/ "https://aws.amazon.com/blogs/security/introducing-s2n-a-new-open-source-tls-implementation/") and
  [Using
  s2n-tls](https://github.com/aws/s2n-tls/tree/main/docs/usage-guide "https://github.com/aws/s2n-tls/tree/main/docs/usage-guide").
- For information about the AWS Common Runtime HTTP Client, see [Configuring the AWS CRT-based HTTP
  client](../../../sdk-for-java/latest/developer-guide/http-configuration-crt.md "../../../sdk-for-java/latest/developer-guide/http-configuration-crt.md") in the _AWS SDK for Java 2.x Developer Guide_.
- For information about the post-quantum cryptography project at the National Institute
  for Standards and Technology (NIST), see [Post-Quantum
  Cryptography](https://csrc.nist.gov/Projects/Post-Quantum-Cryptography "https://csrc.nist.gov/Projects/Post-Quantum-Cryptography").
- For information about NIST post-quantum cryptography standardization, see [NIST's Post-Quantum Cryptography Standardization](https://csrc.nist.gov/Projects/post-quantum-cryptography/post-quantum-cryptography-standardization "https://csrc.nist.gov/Projects/post-quantum-cryptography/post-quantum-cryptography-standardization").
