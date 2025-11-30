# Observability using connection logs

CloudFront connection logs provide detailed visibility into mutual TLS authentication events, allowing you to monitor certificate validation, track connection attempts, and troubleshoot authentication issues.

## What are connection logs?

Connection logs capture detailed information about TLS handshakes and certificate validation for mutual TLS-enabled distributions. Unlike standard access logs that record HTTP request information, connection logs focus specifically on the TLS connection establishment phase, including:

- Connection status (success/failure)
- Client certificate details
- TLS protocol and cipher information
- Connection timing metrics
- Custom data from Connection Functions

These logs provide comprehensive visibility into certificate-based authentication events, helping you monitor security, troubleshoot issues, and meet compliance requirements.

## Enable connection logs

Connection logs are available only for distributions with mutual TLS authentication enabled. You can send connection logs to multiple destinations including CloudWatch Logs, Amazon Data Firehose, and Amazon S3.

### Prerequisites

Before enabling connection logs:

- Configure mutual TLS for your CloudFront distribution
- Enable connection logs for your CloudFront distribution
- Ensure you have the required permissions for your chosen logging destination
- For cross-account delivery, configure appropriate IAM policies

### To enable connection logs (Console)

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. From the distribution list, select your mTLS-enabled distribution.
3. Choose the **Logging** tab.
4. Choose **Add**.
5. Select the service to receive your logs:
   - **CloudWatch Logs**
   - **Firehose**
   - **Amazon S3**

6. For **Destination**, select the resource for your
   chosen service:
   - For CloudWatch Logs, enter the **Log group name**
   - For Firehose, select the **Firehose delivery stream**
   - For Amazon S3, enter the **Bucket name** (optionally with a prefix)

7. (Optional) Configure additional settings:
   - **Field selection:** Select specific log fields to include.
   - **Output format:** Choose from JSON, Plain, w3c, Raw, or Parquet (S3
     only).
   - **Field delimiter:** Specify how to separate log fields.

8. Choose **Save changes**

### To enable connection logs (AWS CLI)

The following example shows how to enable connection logs using the CloudWatch API:

```
# Step 1: Create a delivery source
aws logs put-delivery-source \
  --name "cf-mtls-connection-logs" \
  --resource-arn "arn:aws:cloudfront::123456789012:distribution/E1A2B3C4D5E6F7" \
  --log-type CONNECTION_LOGS

# Step 2: Create a delivery destination
aws logs put-delivery-destination \
  --name "s3-destination" \
  --delivery-destination-configuration \
  "destinationResourceArn=arn:aws:s3:::amzn-s3-demo-bucket1"

# Step 3: Create the delivery
aws logs create-delivery \
  --delivery-source-name "cf-mtls-connection-logs" \
  --delivery-destination-arn "arn:aws:logs:us-east-1:123456789012:delivery-destination:s3-destination"
```

###### Note

When using the CloudWatch API, you must specify the US East (N. Virginia) Region (us-east-1) even when delivering logs to other regions.

## Connection log fields

Connection logs include detailed information about each TLS connection attempt:

| Field                        | Description                                                      | Example                                                                           |
| ---------------------------- | ---------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `eventTimestamp`             | ISO 8601 timestamp when the connection was established or failed | 1731620046814                                                                     |
| `connectionId`               | Unique identifier for the TLS connection                         | `oLHiEKbQSn8lkvJfA3D4gFowK3_iZ0g4i5nMUjE1Akod8TuAzn5nzg==`                        |
| `connectionStatus`           | The status of the mTLS connection attempt.                       | `Success` or `Failed`                                                             |
| `clientIp`                   | IP address of the connecting client                              | `2001:0db8:85a3:0000:0000:8a2e:0370:7334`                                         |
| `clientPort`                 | Port used by the client                                          | 12137                                                                             |
| `serverIp`                   | IP address of the CloudFront edge server                         | `99.84.71.136`                                                                    |
| `distributionId`             | CloudFront distribution ID                                       | `E2DX1SLDPK0123`                                                                  |
| `distributionTenantId`       | CloudFront distribution tenant ID (when applicable)              | `dt_2te1Ura9X3R2iCGNjW123`                                                        |
| `tlsProtocol`                | TLS protocol version used                                        | `TLSv1.3`                                                                         |
| `tlsCipher`                  | TLS cipher suite used for the connection                         | `TLS_AES_128_GCM_SHA256`                                                          |
| `tlsHandshakeDuration`       | Duration of the TLS handshake in milliseconds                    | 153                                                                               |
| `tlsSni`                     | Server Name Indication value from the TLS handshake              | `d111111abcdef8.cloudfront.net`                                                   |
| `clientLeafCertSerialNumber` | Serial number of the client's certificate                        | `00:b1:43:ed:93:d2:d8:f3:9d`                                                      |
| `clientLeafCertSubject`      | Subject field of the client's certificate                        | `C=US, ST=WA, L=Seattle, O=Amazon.com, OU=CloudFront,<br>CN=client.test.mtls.net` |
| `clientLeafCertIssuer`       | Issuer field of the client's certificate                         | `C=US, ST=WA, L=Seattle, O=Amazon.com, OU=CloudFront,<br>CN=test.mtls.net`        |
| `clientLeafCertValidity`     | Validity period of the client's certificate                      | `NotBefore=2025-06-05T23:28:21Z;NotAfter=2125-05-12T23:28:21Z`                    |
| `connectionLogCustomData`    | Custom data added via Connection Functions                       | `REVOKED:00:b1:43:ed:93:d2:d8:f3:9d`                                              |

## Connection error codes

```
Failed:ClientCertMaxChainDepthExceeded
Failed:ClientCertMaxSizeExceeded
Failed:ClientCertUntrusted
Failed:ClientCertNotYetValid
Failed:ClientCertExpired
Failed:ClientCertTypeUnsupported
Failed:ClientCertInvalid
Failed:ClientCertIntentInvalid
Failed:ClientCertRejected
Failed:ClientCertMissing
Failed:TcpError
Failed:TcpTimeout
Failed:ConnectionFunctionError
Failed:ConnectionFunctionDenied
Failed:Internal
Failed:UnmappedConnectionError
```

When connections fail, CloudFront records specific reason codes:

| Code                            | Description                                                                |
| ------------------------------- | -------------------------------------------------------------------------- |
| ClientCertMaxChainDepthExceeded | Maximum certificate chain depth exceeded                                   |
| ClientCertMaxSizeExceeded       | Maximum certificate size exceeded                                          |
| ClientCertUntrusted             | Certificate is untrusted                                                   |
| ClientCertNotYetValid           | Certificate is not yet valid                                               |
| ClientCertExpired               | Certificate is expired                                                     |
| ClientCertTypeUnsupported       | Certificate type is unsupported                                            |
| ClientCertInvalid               | Certificate is invalid                                                     |
| ClientCertIntentInvalid         | Certificate intent is invalid                                              |
| ClientCertRejected              | Certificate rejected by custom validation                                  |
| ClientCertMissing               | Certificate is missing                                                     |
| TcpError                        | An error occurred while attempting to establish a<br>connection            |
| TcpTimeout                      | The connection was not able to be established within the<br>timeout period |
| ConnectionFunctionError         | An uncaught exception was thrown during Connection Function<br>execution   |
| Internal                        | An internal service error occurred                                         |
| UnmappedConnectionError         | An error occurred that does not fall into any of the other<br>categories   |
