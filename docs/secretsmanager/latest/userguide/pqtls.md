# Post-quantum TLS

Secrets Manager supports a hybrid post-quantum key exchange option for the Transport Layer
Security (TLS) network encryption protocol. You can use this TLS option when you connect to
Secrets Manager API endpoints. We're offering this feature before post-quantum algorithms are
standardized so you can begin testing the effect of these key exchange protocols on Secrets Manager
calls. These optional hybrid post-quantum key exchange features are at least as secure as
the TLS encryption we use today and are likely to provide additional security benefits.
However, they affect latency and throughput compared to the classic key exchange protocols
in use today. The Secrets Manager Agent uses the post-quantum ML-KEM key exchange as the highest-priority key exchange by default.

To protect data encrypted today against potential future attacks, AWS is participating
with the cryptographic community in the development of quantum-resistant or _post-quantum_ algorithms. We've implemented hybrid post-quantum
key exchange cipher suites in Secrets Manager endpoints. These hybrid cipher suites, which combine
classic and post-quantum elements, ensure that your TLS connection is at least as strong as
it would be with classic cipher suites. However, because the performance characteristics and
bandwidth requirements of hybrid cipher suites are different from those of classic key
exchange mechanisms, we recommend that you test them on your API calls.

Secrets Manager supports PQTLS in all Regions except China Regions.

###### To configure hybrid post-quantum TLS

1. Add the AWS Common Runtime client to your Maven dependencies. We recommend using the latest available version. For example, this statement adds version 2.20.0.

```
<dependency>
  <groupId>software.amazon.awssdk</groupId>
  <artifactId>aws-crt-client</artifactId>
  <version>2.20.0</version>
</dependency>
```

2. Add the AWS SDK for Java 2.x to your project and initialize it. Enable the hybrid post-quantum cipher suites on your HTTP client.

```
SdkAsyncHttpClient awsCrtHttpClient = AwsCrtAsyncHttpClient.builder()
            .postQuantumTlsEnabled(true)
            .build();
```

3. Create the [Secrets Manager asynchronous client](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/secretsmanager/AWSSecretsManagerAsyncClient.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/secretsmanager/AWSSecretsManagerAsyncClient.md").

```
SecretsManagerAsyncClient SecretsManagerAsync = SecretsManagerAsyncClient.builder()
            .httpClient(awsCrtHttpClient)
            .build();
```

Now when you call Secrets Manager API operations, your calls are transmitted to the Secrets Manager endpoint using hybrid post-quantum TLS.
For more information about using hybrid post-quantum TLS, see:

- [AWS SDK for Java 2.x Developer Guide](../../../sdk-for-java/latest/developer-guide.md "../../../sdk-for-java/latest/developer-guide.md") and the [AWS SDK for Java 2.x
  released](https://aws.amazon.com/blogs/developer/aws-sdk-for-java-2-x-released/ "https://aws.amazon.com/blogs/developer/aws-sdk-for-java-2-x-released/") blog post.
- [Introducing s2n-tls, a New Open Source TLS Implementation](https://aws.amazon.com/blogs/security/introducing-s2n-a-new-open-source-tls-implementation/ "https://aws.amazon.com/blogs/security/introducing-s2n-a-new-open-source-tls-implementation/") and
  [Using
  s2n-tls](https://aws.github.io/s2n-tls/usage-guide/ "https://aws.github.io/s2n-tls/usage-guide/").
- [Post-Quantum
  Cryptography](https://csrc.nist.gov/Projects/Post-Quantum-Cryptography "https://csrc.nist.gov/Projects/Post-Quantum-Cryptography") at the National Institute for Standards and Technology
  (NIST).
- [Hybrid Post-Quantum Key Encapsulation Methods (PQ KEM) for Transport Layer Security
  1.2 (TLS)](https://tools.ietf.org/html/draft-campagna-tls-bike-sike-hybrid-01 "https://tools.ietf.org/html/draft-campagna-tls-bike-sike-hybrid-01").
  Post-quantum TLS for Secrets Manager is available in all AWS Regions except China.
