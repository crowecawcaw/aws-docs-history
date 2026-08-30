# Configure hybrid post-quantum TLS

In this procedure, add a Maven dependency for the AWS Common Runtime HTTP Client. Next,
configure an HTTP client that prefers post-quantum TLS. Then, create an AWS KMS client that uses
the HTTP client.

To see a complete working example of configuring and using hybrid post-quantum TLS with
AWS KMS, see the [aws-kms-pq-tls-example](https://github.com/aws-samples/aws-kms-pq-tls-example "https://github.com/aws-samples/aws-kms-pq-tls-example") repository on GitHub.

1. Add the AWS Common Runtime client to your Maven dependencies. We recommend using the
   latest available version.

For example, this statement adds version `2.30.22` of the AWS Common
Runtime client to your Maven dependencies. Use version `2.30.22` or later to
enable ML-KEM.

```
<dependency>
    <groupId>software.amazon.awssdk</groupId>
    <artifactId>aws-crt-client</artifactId>
    <version>2.30.22</version>
</dependency>
```

2. To enable the hybrid post-quantum cipher suites, add the AWS SDK for Java 2.x to your project
   and initialize it. Then enable the hybrid post-quantum cipher suites on your HTTP client
   as shown in the following example.

This code uses the `postQuantumTlsEnabled()` method parameter to configure
an [AWS common runtime HTTP
client](../../../sdk-for-java/latest/developer-guide/http-configuration-crt.md "../../../sdk-for-java/latest/developer-guide/http-configuration-crt.md") that prefers the recommended hybrid post-quantum cipher suite, ECDH with
ML-KEM. Then it uses the configured HTTP client to build an instance of
the AWS KMS asynchronous client, [`KmsAsyncClient`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/kms/KmsAsyncClient.html "https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/kms/KmsAsyncClient.html"). After this code completes, all [AWS KMS API](../APIReference.md "../APIReference.md") requests on the `KmsAsyncClient`
instance use hybrid post-quantum TLS.

```
// Configure HTTP client
SdkAsyncHttpClient awsCrtHttpClient = AwsCrtAsyncHttpClient.builder()
          .postQuantumTlsEnabled(true)
          .build();

// Create the AWS KMS async client
KmsAsyncClient kmsAsync = KmsAsyncClient.builder()
         .httpClient(awsCrtHttpClient)
         .build();
```

3. Test your AWS KMS calls with hybrid post-quantum TLS.

When you call AWS KMS API operations on the configured AWS KMS client, your calls are
transmitted to the AWS KMS endpoint using hybrid post-quantum TLS. To test your
configuration, call an AWS KMS API, such as `ListKeys`.

```
ListKeysReponse keys = kmsAsync.listKeys().get();
```

To confirm that your call used hybrid post-quantum TLS, inspect its CloudTrail log entry as
described in [Verifying Hybrid Post-Quantum TLS](pqtls.md#pqtls-verify "pqtls.md#pqtls-verify").
