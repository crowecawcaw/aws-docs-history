# Using hybrid post-quantum TLS with AWS KMS

AWS Key Management Service (AWS KMS) supports a hybrid post-quantum key exchange option for the Transport Layer
Security (TLS) network encryption protocol. You can use this TLS option when you connect to
AWS KMS API endpoints. These optional hybrid post-quantum key exchange features are at least as
secure as the TLS encryption we use today and are likely to provide additional long-term
security benefits. However, they affect latency and throughput compared
to the classic key exchange protocols in use today.

The data that you send to AWS Key Management Service (AWS KMS) is protected in transit by the encryption
provided by a Transport Layer Security (TLS) connection. The classic cipher suites that AWS KMS
supports for TLS sessions make brute force attacks on the key exchange mechanisms infeasible
with current technology. However, if large-scale quantum computing becomes practical in the
future, the classic cipher suites used in TLS key exchange mechanisms will be susceptible to
these attacks. If you’re developing applications that rely on the long-term confidentiality of
data passed over a TLS connection, you should consider a plan to migrate to post-quantum
cryptography before large-scale quantum computers become available for use. AWS is working to
prepare for this future, and we want you to be well-prepared, too.

To protect data encrypted today against potential future attacks, AWS is participating
with the cryptographic community in the development of quantum-resistant or _post-quantum_ algorithms. We've implemented _hybrid_ post-quantum key exchange cipher suites in AWS KMS that combine classic and
post-quantum elements to ensure that your TLS connection is at least as strong as it would be
with classic cipher suites.

These hybrid cipher suites are available for use on your production workloads in [most AWS Regions](#pqtls-regions "#pqtls-regions"). However, because the performance
characteristics and bandwidth requirements of hybrid cipher suites are different from those of
classic key exchange mechanisms, we recommend that you [test them
on your AWS KMS API calls](pqtls-how-to.md#pqtls-testing "pqtls-how-to.md#pqtls-testing") under different conditions.

**Feedback**

As always, we welcome your feedback and participation in our open-source repositories. We’d
especially like to hear how your infrastructure interacts with this new variant of TLS traffic.

- To provide feedback on this topic, use the **Feedback** link in the
  upper right corner of this page.
- We're developing these hybrid cipher suites in open source in the [s2n-tls](https://github.com/aws/s2n-tls "https://github.com/aws/s2n-tls") repository on GitHub. To
  provide feedback on the usability of the cipher suites, or share novel test conditions or
  results, [create an issue](https://github.com/aws/s2n-tls/issues "https://github.com/aws/s2n-tls/issues") in the
  s2n-tls repository.
- We're writing code samples for using hybrid post-quantum TLS with AWS KMS in the [aws-kms-pq-tls-example](https://github.com/aws-samples/aws-kms-pq-tls-example "https://github.com/aws-samples/aws-kms-pq-tls-example") GitHub repository. To ask questions or
  share ideas about configuring your HTTP client or AWS KMS client to use the hybrid cipher
  suites, [create an
  issue](https://github.com/aws-samples/aws-kms-pq-tls-example/issues "https://github.com/aws-samples/aws-kms-pq-tls-example/issues") in the aws-kms-pq-tls-example repository.
  **Supported AWS Regions**

Post-quantum TLS for AWS KMS is available in all AWS Regions that AWS KMS supports.

For a list of AWS KMS endpoints for each AWS Region, see [AWS Key Management Service endpoints and quotas](../../../general/latest/gr/kms.md "../../../general/latest/gr/kms.md") in the _Amazon Web Services General Reference_. For information about FIPS endpoints, see [FIPS endpoints](../../../general/latest/gr/rande.md#FIPS-endpoints "../../../general/latest/gr/rande.md#FIPS-endpoints") in the _Amazon Web Services General Reference_.

## About hybrid post-quantum key exchange in TLS

AWS KMS supports hybrid post-quantum key exchange cipher suites. You can use the
AWS SDK for Java 2.x and AWS Common Runtime on Linux systems to configure an HTTP client that uses
these cipher suites. Then, whenever you connect to an AWS KMS endpoint with your HTTP client,
the hybrid cipher suites are used.

This HTTP client uses [s2n-tls](https://github.com/aws/s2n-tls "https://github.com/aws/s2n-tls"),
which is an open source implementation of the TLS protocol. The hybrid cipher suites that
s2n-tls uses are implemented only for key exchange, not for direct data
encryption. During _key exchange_, the client and server
calculate the key they will use to encrypt and decrypt the data on the wire.

The algorithms that s2n-tls uses are a _hybrid_ that combines [Elliptic Curve
Diffie-Hellman](https://en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman "https://en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman") (ECDH), a classic key exchange algorithm used today in TLS, with
[Module-Lattice-Based
Key-Encapsulation Mechanism](https://csrc.nist.gov/pubs/fips/203/final "https://csrc.nist.gov/pubs/fips/203/final") (ML-KEM), a public-key encryption and
key-establishment algorithm that the National Institute for Standards and Technology (NIST)
[has designated as its first
standard](https://csrc.nist.gov/pubs/fips/203/final "https://csrc.nist.gov/pubs/fips/203/final") post-quantum key-agreement algorithm. This hybrid uses each of the
algorithms independently to generate a key. Then it combines the two keys cryptographically.
With s2n-tls, you can [configure an HTTP
client](pqtls-how-to.md "pqtls-how-to.md") to prefer post-quantum TLS, which places ECDH with ML-KEM first
in the preference list. Classic key exchange algorithms are included in the preference list to
ensure compatibility, but they are lower in the preference order.

## Using hybrid post-quantum TLS with AWS KMS

You can use hybrid post-quantum TLS for your calls to AWS KMS. When setting up your HTTP
client test environment, be aware of the following information:

**Encryption in Transit**

The hybrid cipher suites in s2n-tls are used only for encryption in
transit. They protect your data while it is traveling from your client to the AWS KMS endpoint.
AWS KMS does not use these cipher suites to encrypt data under AWS KMS keys.

Instead, when AWS KMS encrypts your data under KMS keys, it uses symmetric cryptography
with 256-bit keys and the Advanced Encryption Standard in Galois Counter Mode (AES-GCM)
algorithm, which is already quantum resistant. Theoretical future, large-scale quantum
computing attacks on ciphertexts created under 256-bit AES-GCM keys [reduce the
effective security of the key to 128 bits](https://www.etsi.org/images/files/ETSIWhitePapers/QuantumSafeWhitepaper.pdf "https://www.etsi.org/images/files/ETSIWhitePapers/QuantumSafeWhitepaper.pdf"). This security level is sufficient to make
brute force attacks on AWS KMS ciphertexts infeasible.

**Supported Systems**

Use of the hybrid cipher suites in s2n-tls is currently supported only on
Linux systems. In addition, these cipher suites are supported only in SDKs that support the
AWS Common Runtime, such as the AWS SDK for Java 2.x. For an example, see [Configure hybrid post-quantum TLS](pqtls-how-to.md "pqtls-how-to.md").

**AWS KMS Endpoints**

AWS KMS supports hybrid post-quantum TLS on all endpoints including [FIPS 140-3 validated endpoints](../../../general/latest/gr/kms.md "../../../general/latest/gr/kms.md").

## Learn more about post-quantum TLS in AWS KMS

For more information about using hybrid post-quantum TLS in AWS KMS, see the following
resources.

- To learn about post-quantum cryptography at AWS, including links to blog posts and
  research papers, see [Post-Quantum
  Cryptography](https://aws.amazon.com/security/post-quantum-cryptography/ "https://aws.amazon.com/security/post-quantum-cryptography/").
- For information about s2n-tls, see [Introducing s2n-tls, a New Open Source TLS Implementation](https://aws.amazon.com/blogs/security/introducing-s2n-a-new-open-source-tls-implementation/ "https://aws.amazon.com/blogs/security/introducing-s2n-a-new-open-source-tls-implementation/") and
  [Using
  s2n-tls](https://github.com/aws/s2n-tls/tree/main/docs/usage-guide "https://github.com/aws/s2n-tls/tree/main/docs/usage-guide").
- For information about the AWS Common Runtime HTTP Client, see [Configuring the AWS CRT-based HTTP
  client](../../../sdk-for-java/latest/developer-guide/http-configuration-crt.md "../../../sdk-for-java/latest/developer-guide/http-configuration-crt.md") in the _AWS SDK for Java 2.x Developer Guide_.
- For information about the post-quantum cryptography project at the National Institute
  for Standards and Technology (NIST), see [Post-Quantum
  Cryptography](https://csrc.nist.gov/Projects/Post-Quantum-Cryptography "https://csrc.nist.gov/Projects/Post-Quantum-Cryptography").
- For information about NIST post-quantum cryptography standardization, see [Post-Quantum Cryptography Standardization](https://csrc.nist.gov/Projects/post-quantum-cryptography/post-quantum-cryptography-standardization "https://csrc.nist.gov/Projects/post-quantum-cryptography/post-quantum-cryptography-standardization").
