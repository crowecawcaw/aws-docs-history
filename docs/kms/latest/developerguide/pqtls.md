# Using hybrid post-quantum TLS with AWS KMS

The data that you send to AWS Key Management Service (AWS KMS) is protected in transit by the encryption
provided by a Transport Layer Security (TLS) connection. The classic cipher suites that AWS KMS
supports for TLS sessions make brute force attacks on the key exchange mechanisms infeasible
with current technology. However, if large-scale quantum computing becomes practical, the
classic cipher suites used in TLS key exchange mechanisms will be susceptible to these
attacks.

In August 2024, NIST finalized its first post-quantum cryptography standards. These include
Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) specified in [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final "https://csrc.nist.gov/pubs/fips/203/final") on the NIST website. AWS KMS now supports a hybrid
post-quantum key exchange option for TLS which combines [Elliptic Curve
Diffie-Hellman](https://en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman "https://en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman") (ECDH) with ML-KEM. This hybrid key exchange retains the strength of
today's classic cipher suites while adding resilience against future quantum-capable adversaries.
For more information, see [ML-KEM post-quantum TLS now supported in AWS KMS, ACM, and Secrets Manager](https://aws.amazon.com/blogs/security/ml-kem-post-quantum-tls-now-supported-in-aws-kms-acm-and-secrets-manager/ "https://aws.amazon.com/blogs/security/ml-kem-post-quantum-tls-now-supported-in-aws-kms-acm-and-secrets-manager/") in the _AWS Security Blog_.

If your applications rely on the long-term confidentiality of data passed over a TLS
connection, you should use post-quantum cryptography. Otherwise, an adversary may be able to
capture data encrypted with classic cipher suites today and decrypt it once quantum computers
become available. This strategy is known as _harvest now, decrypt
later_.

## Using hybrid post-quantum TLS with AWS KMS

You can use hybrid post-quantum TLS for all your API calls to AWS KMS. When setting up your HTTP
client, be aware of the following information.

### AWS KMS Endpoints

AWS KMS supports hybrid post-quantum TLS in all AWS Regions where it is available, on all
endpoints including [FIPS 140-3 validated
endpoints](../../../general/latest/gr/kms.md "../../../general/latest/gr/kms.md"). For a list of AWS KMS endpoints for each AWS Region, see [AWS Key Management Service endpoints and quotas](../../../general/latest/gr/kms.md "../../../general/latest/gr/kms.md") in the _Amazon Web Services General Reference_. For information about FIPS endpoints, see [FIPS endpoints](../../../general/latest/gr/rande.md#FIPS-endpoints "../../../general/latest/gr/rande.md#FIPS-endpoints") in the _Amazon Web Services General Reference_.

### Supported Systems

Many AWS SDKs support hybrid post-quantum TLS, as described in [Enabling hybrid
post-quantum TLS](../../../sdkref/latest/guide/pqtls-details.md "../../../sdkref/latest/guide/pqtls-details.md") in the _AWS SDKs and Tools Reference
Guide_. For a Java example, see [Configure hybrid post-quantum TLS](pqtls-how-to.md "pqtls-how-to.md").

### Verifying Hybrid Post-Quantum TLS

You can confirm that a specific AWS KMS API call used hybrid post-quantum TLS by
inspecting its CloudTrail log entry. Find the `tlsDetails` section in the log entry for
the call. The `keyExchange` field names the key exchange algorithm that was used.
For a hybrid post-quantum connection, this field shows a hybrid algorithm such as
`X25519MLKEM768`. For an example log entry, see [Decrypt with a standard symmetric encryption key over a post-quantum TLS connection](ct-decrypt.md#ct-decrypt-default-pqtls "ct-decrypt.md#ct-decrypt-default-pqtls").

###### Note

The `tlsDetails` field is not present in the log entry when an AWS
service calls AWS KMS on your behalf. For details about the fields in a CloudTrail log entry and
when they are present, see [CloudTrail record
contents](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md") in the AWS CloudTrail User Guide.

### Performance

Hybrid key exchange slightly increases the size and processing time of some TLS
handshake messages, but the overall performance impact is imperceptible for most workloads.
Because these messages are larger, we recommend that you test your AWS KMS API calls from
different locations on your network.

Depending on the network path your request takes, legacy intermediate hosts, proxies,
or firewalls with deep packet inspection (DPI) might block the request. This can result from
the new key exchange groups in the [ClientHello](https://datatracker.ietf.org/doc/html/rfc8446#section-4.1.2 "https://datatracker.ietf.org/doc/html/rfc8446#section-4.1.2")
part of the TLS handshake, or from the larger key exchange messages. If you have trouble
resolving these issues, work with your security team or IT administrators to unblock the new
TLS key exchange groups.

### Encryption in Transit

The hybrid cipher suites are used only for encryption in transit. They protect your data
while it is traveling from your client to the AWS KMS endpoint. AWS KMS does not use these
cipher suites to encrypt data under AWS KMS keys.

Instead, when AWS KMS encrypts your data under KMS keys, it uses symmetric cryptography
with 256-bit keys and the Advanced Encryption Standard in Galois Counter Mode (AES-GCM)
algorithm, which is already quantum resistant. Theoretical future, large-scale quantum
computing attacks on ciphertexts created under 256-bit AES-GCM keys reduce the effective
security of the key to 128 bits. For more information, see the [Quantum
Safe Cryptography and Security](https://www.etsi.org/images/files/ETSIWhitePapers/QuantumSafeWhitepaper.pdf "https://www.etsi.org/images/files/ETSIWhitePapers/QuantumSafeWhitepaper.pdf") paper on the ETSI website. This security level is
sufficient to make brute force attacks on AWS KMS ciphertexts infeasible.

## Learn more about post-quantum TLS in AWS KMS

For more information about using hybrid post-quantum TLS in AWS KMS, see the following
resources.

- To learn about post-quantum cryptography at AWS, including links to blog posts and
  research papers, see [Post-Quantum
  Cryptography](https://aws.amazon.com/security/post-quantum-cryptography/ "https://aws.amazon.com/security/post-quantum-cryptography/").
- AWS KMS uses s2n-tls, the open source TLS implementation from AWS, for
  the server side of its hybrid post-quantum TLS connections. For information about
  s2n-tls, see [Introducing s2n-tls, a New Open Source TLS Implementation](https://aws.amazon.com/blogs/security/introducing-s2n-a-new-open-source-tls-implementation/ "https://aws.amazon.com/blogs/security/introducing-s2n-a-new-open-source-tls-implementation/") and
  [Using
  s2n-tls](https://github.com/aws/s2n-tls/tree/main/docs/usage-guide "https://github.com/aws/s2n-tls/tree/main/docs/usage-guide") on GitHub.
- For information about the AWS Common Runtime HTTP Client, see [Configuring the AWS CRT-based HTTP
  client](../../../sdk-for-java/latest/developer-guide/http-configuration-crt.md "../../../sdk-for-java/latest/developer-guide/http-configuration-crt.md") in the _AWS SDK for Java 2.x Developer Guide_.
- For information about the post-quantum cryptography project at the National Institute
  for Standards and Technology (NIST), see [Post-Quantum
  Cryptography](https://csrc.nist.gov/Projects/Post-Quantum-Cryptography "https://csrc.nist.gov/Projects/Post-Quantum-Cryptography").
- For information about NIST post-quantum cryptography standardization, see [Post-Quantum Cryptography Standardization](https://csrc.nist.gov/Projects/post-quantum-cryptography/post-quantum-cryptography-standardization "https://csrc.nist.gov/Projects/post-quantum-cryptography/post-quantum-cryptography-standardization").
