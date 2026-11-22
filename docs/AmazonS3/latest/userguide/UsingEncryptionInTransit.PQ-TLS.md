

# Using hybrid post-quantum TLS with Amazon S3

Amazon S3 supports a hybrid post-quantum key exchange option for the TLS network encryption protocol. You can use this TLS option when you make requests to Amazon S3 endpoints utilizing TLS 1.3. The classic cipher suites that S3 supports for TLS sessions make brute force attacks on the key exchange mechanisms infeasible with current technology. However, if a cryptographically relevant quantum computer becomes practical in the future, the classic cipher suites used in TLS key exchange mechanisms will be susceptible to these attacks. At present, the industry is aligned on hybrid post-quantum key exchange that combines classic and post-quantum elements to ensure that your TLS connection is at least as strong as it would be with classic cipher suites. Amazon S3 supports hybrid PQ-TLS, in compliance with the industry-standard IANA specification, today.

If you’re developing applications that rely on the long-term confidentiality of data passed over a TLS connection, you should consider a plan to migrate to post-quantum cryptography before large-scale quantum computers become available for use. As part of the shared responsibility model, S3 enables quantum-safe cryptography on our service endpoints. As browsers and applications enable PQ-TLS on their side, S3 will choose the strongest possible configuration to secure data in transit.

**Supported endpoint types and AWS Regions**

Post-quantum TLS for Amazon S3 is available in all AWS Regions. For a list of S3 endpoints for each AWS Region, see [Amazon Simple Storage Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/s3.html) in the *Amazon Web Services General Reference*.

**Note**  
Hybrid post-quantum TLS is supported for all S3 endpoints except for Multi-Region Access Points.

## Using hybrid post-quantum TLS with Amazon S3
<a name="pqtls-details"></a>

You must configure the client that makes requests to Amazon S3 to support hybrid post-quantum TLS. When setting up your HTTP client test environment or production environments, be aware of the following information:

**Encryption in Transit**

Hybrid post-quantum TLS is only used for encryption in transit. This protects your data while it is traveling from your client to the S3 endpoint. This new support combined with Amazon S3’s server-side encryption by default utilizing AES-256 algorithms offers customers quantum-resistant encryption both in-transit and at-rest. For more information about server-side encryption in Amazon S3, see [Protecting data with server-side encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html).

**Supported Clients**

The use of hybrid post-quantum TLS requires using a client that supports this functionality. AWS SDKs and tools have cryptographic capabilities and configuration that differ across languages and runtimes. To learn more about post-quantum cryptography for specific tools, see [Enabling hybrid post-quantum TLS](https://docs.aws.amazon.com/sdkref/latest/guide/pqtls-details.html) in the *AWS SDKs and Tools Reference Guide*. For a configuration example, see [Configuring hybrid post-quantum TLS for your client](pqtls-how-to.md).

## Verifying hybrid post-quantum TLS with AWS CloudTrail
<a name="pqtls-verify"></a>

AWS CloudTrail records the key exchange used for each request to Amazon S3 in the `keyExchange` field of the `tlsDetails` element. You can use this field to confirm that your clients use hybrid post-quantum TLS, and to find clients that still use classical key exchange. For more information about `tlsDetails`, see [CloudTrail record contents](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.html) in the *AWS CloudTrail User Guide*.

The `keyExchange` field contains one of the following values:


| Value | Meaning | 
| --- | --- | 
| X25519MLKEM768 | Hybrid post-quantum key exchange (X25519 with ML-KEM-768), TLS 1.3 | 
| SecP256r1MLKEM768 | Hybrid post-quantum key exchange (P-256 with ML-KEM-768), TLS 1.3 | 
| x25519 | Classical elliptic curve key exchange, TLS 1.3 or TLS 1.2 | 
| secp256r1, secp384r1 | Classical elliptic curve key exchange, TLS 1.3 or TLS 1.2 | 

The following example shows the `tlsDetails` element of a CloudTrail event for a request that used hybrid post-quantum TLS.

```json
{
  "eventVersion": "1.11",
  "eventSource": "s3.amazonaws.com",
  "eventName": "ListBuckets",
  "awsRegion": "us-east-2",
  "userAgent": "aws-cli/2.40.1 ...",
  "tlsDetails": {
    "tlsVersion": "TLSv1.3",
    "cipherSuite": "TLS_AES_128_GCM_SHA256",
    "clientProvidedHostHeader": "s3.us-east-2.amazonaws.com",
    "keyExchange": "X25519MLKEM768"
  },
  ...
}
```

**Note**  
Amazon S3 server access logs record the TLS version and cipher suite for each request, but not the key exchange.

## Learn more about post-quantum TLS
<a name="pqtls-see-also"></a>

For more information about using hybrid post-quantum TLS, see the following resources.
+ To learn about post-quantum cryptography at AWS, including links to blog posts and research papers, see [Post-Quantum Cryptography for AWS](https://aws.amazon.com/security/post-quantum-cryptography/).
+ For information about s2n-tls, see [Introducing s2n-tls, a New Open Source TLS Implementation](https://aws.amazon.com/blogs/security/introducing-s2n-a-new-open-source-tls-implementation/) and [Using s2n-tls](https://github.com/aws/s2n-tls/tree/main/docs/usage-guide).
+ For information about the AWS Common Runtime HTTP Client, see [Configuring the AWS CRT-based HTTP client](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/http-configuration-crt.html) in the *AWS SDK for Java 2.x Developer Guide*.
+ For information about the post-quantum cryptography project at the National Institute for Standards and Technology (NIST), see [Post-Quantum Cryptography](https://csrc.nist.gov/Projects/Post-Quantum-Cryptography).
+ For information about NIST post-quantum cryptography standardization, see [NIST's Post-Quantum Cryptography Standardization](https://csrc.nist.gov/Projects/post-quantum-cryptography/post-quantum-cryptography-standardization).