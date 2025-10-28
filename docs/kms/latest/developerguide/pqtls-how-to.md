# Configure hybrid post-quantum TLS

In this procedure, add a Maven dependency for the AWS Common Runtime HTTP Client. Next,
configure an HTTP client that prefers post-quantum TLS. Then, create an AWS KMS client that uses
the HTTP client.

To see a complete working examples of configuring and using hybrid post-quantum TLS with
AWS KMS, see the [aws-kms-pq-tls-example](https://github.com/aws-samples/aws-kms-pq-tls-example "https://github.com/aws-samples/aws-kms-pq-tls-example") repository.

###### Note

The AWS Common Runtime HTTP Client, which has been available as a preview, became
generally available in February 2023. In that release, the `tlsCipherPreference`
class and the `tlsCipherPreference()` method parameter are replaced by the
`postQuantumTlsEnabled()` method parameter. If you were using this example
during the preview, you need to update your code.

1. Add the AWS Common Runtime client to your Maven dependencies. We recommend using the
   latest available version.

For example, this statement adds version `2.30.22` of the AWS Common
Runtime client to your Maven dependencies.

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

## Test your hybrid post-quantum TLS configuration

Consider running the following tests with hybrid cipher suites on your applications that
call AWS KMS.

- Run load tests and benchmarks. The hybrid cipher suites perform differently than
  traditional key exchange algorithms. You might need to adjust your connection timeouts
  to allow for the longer handshake times. If you’re running inside an AWS Lambda function,
  extend the execution timeout setting.
- Try connecting from different locations. Depending on the network path your request
  takes, you might discover that intermediate hosts, proxies, or firewalls with deep
  packet inspection (DPI) block the request. This might result from using the new cipher
  suites in the [ClientHello](https://tools.ietf.org/html/rfc5246#section-7.4.1.2 "https://tools.ietf.org/html/rfc5246#section-7.4.1.2") part of the TLS handshake, or from the larger key exchange
  messages. If you have trouble resolving these issues, work with your security team or IT
  administrators to update the relevant configuration and unblock the new TLS cipher
  suites.
