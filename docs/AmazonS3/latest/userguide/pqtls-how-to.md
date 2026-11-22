

# Configuring hybrid post-quantum TLS for your client

To use PQ-TLS with Amazon S3, your client must support post-quantum key exchange algorithms. Also ensure that your client supports the hybrid approach, which combines traditional elliptic curve cryptography with post-quantum algorithms like ML-KEM (Module-Lattice-Based Key Encapsulation Mechanism).

The specific configuration depends on your client library and programming language. For other SDKs, tools, and platforms, see [Enabling hybrid post-quantum TLS](https://docs.aws.amazon.com/sdkref/latest/guide/pqtls-details.html) in the *AWS SDKs and Tools Reference Guide*.

## Client configuration example: AWS SDK for Java 2
<a name="UsingEncryptionInTransit.PQ-TLS.configuration.java2-sdk"></a>

In this procedure, add a Maven dependency for the AWS Common Runtime HTTP Client. Next, configure an HTTP client that prefers post-quantum TLS. Then, create an Amazon S3 client that uses the HTTP client.

1. Add the AWS Common Runtime client to your Maven dependencies. We recommend using the latest available version. 

   For example, this statement adds version `2.35.11` of the AWS Common Runtime client to your Maven dependencies. 

   ```xml
   <dependency>
       <groupId>software.amazon.awssdk</groupId>
       <artifactId>aws-crt-client</artifactId>
       <version>2.35.11</version>
   </dependency>
   ```

1. To enable the hybrid post-quantum key exchange, add the AWS SDK for Java 2.x to your project and initialize it. Then enable it on your HTTP client as shown in the following example.

   This code uses the `postQuantumTlsEnabled()` method parameter to configure an [AWS common runtime HTTP client](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/http-configuration-crt.html) that prefers the recommended hybrid post-quantum key exchange, ECDH with ML-KEM. Then it uses the configured HTTP client to build an instance of the Amazon S3 asynchronous client, [`S3AsyncClient`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/s3/S3AsyncClient.html). After this code completes, all [Amazon S3 API](https://docs.aws.amazon.com/AmazonS3/latest/API/) requests on the `S3AsyncClient` instance use hybrid post-quantum TLS when the endpoint supports it.
**Important**  
Starting with version 2.35.11, the AWS CRT HTTP client enables hybrid post-quantum TLS by default, so you don't need to call `.postQuantumTlsEnabled(true)`. Setting it, as in the following example, has no effect on these versions but makes the behavior explicit.

   ```java
   // Configure HTTP client
   SdkAsyncHttpClient awsCrtHttpClient = AwsCrtAsyncHttpClient.builder()
             .postQuantumTlsEnabled(true)
             .build();
   
   // Create the Amazon S3 async client
   S3AsyncClient s3Async = S3AsyncClient.builder()
            .httpClient(awsCrtHttpClient)
            .build();
   ```

1. Test your Amazon S3 calls with hybrid post-quantum TLS.

   When you call Amazon S3 API operations on the configured Amazon S3 client, your calls are transmitted to the Amazon S3 endpoint using hybrid post-quantum TLS. To test your configuration, call an Amazon S3 API, such as `[ListBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html)`.

   ```
   ListBucketsResponse response = s3Async.listBuckets().join();
   ```

1. Confirm that the request used hybrid post-quantum TLS.

   A successful call doesn't show which key exchange the request used, because clients that prefer post-quantum TLS fall back to classical key exchange if the endpoint doesn't support it. To confirm, look up the `ListBuckets` event in AWS CloudTrail and check the `tlsDetails.keyExchange` field. A value of `X25519MLKEM768` or `SecP256r1MLKEM768` means that the request used hybrid post-quantum TLS. `ListBuckets` is a management event, so it appears in CloudTrail Event history within about 15 minutes, without a trail. For more information, see [Verifying hybrid post-quantum TLS with AWS CloudTrail](UsingEncryptionInTransit.PQ-TLS.md#pqtls-verify).

   The following AWS CLI command lists recent `ListBuckets` events with their key exchange. Replace the Region with the Region of your S3 client, and the start time with a time shortly before your test.

   ```
   aws cloudtrail lookup-events \
       --region us-east-2 \
       --lookup-attributes AttributeKey=EventName,AttributeValue=ListBuckets \
       --start-time 2026-11-17T14:25:00Z \
       --query 'Events[].CloudTrailEvent' --output text \
     | jq -c '{eventTime, userAgent, keyExchange: .tlsDetails.keyExchange}'
   ```

   Example output:

   ```
   {"eventTime":"2026-11-17T14:28:24Z","userAgent":"aws-cli/2.40.1 ...","keyExchange":"X25519MLKEM768"}
   ```

### Test your hybrid post-quantum TLS configuration
<a name="pqtls-testing"></a>

Consider running the following tests with hybrid key exchange on your applications that call Amazon S3.
+ Run load tests and benchmarks. The hybrid key exchange performs differently than traditional key exchange algorithms. You might need to adjust your connection timeouts to allow for the longer handshake times. If you’re running inside an AWS Lambda function, extend the execution timeout setting.
+ Try connecting from different locations. Depending on the network path your request takes, you might discover that intermediate hosts, proxies, or firewalls with deep packet inspection (DPI) block the request. This might result from using the new key exchange groups in the [ClientHello](https://tools.ietf.org/html/rfc5246#section-7.4.1.2) part of the TLS handshake, or from the larger key exchange messages. If you have trouble resolving these issues, work with your security team or IT administrators to update the relevant configuration and unblock the new TLS key exchange groups. 