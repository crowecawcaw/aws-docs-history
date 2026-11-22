

# Connection logs

CloudFront connection logs provide detailed visibility into TLS connections, including mutual TLS authentication events, allowing you to monitor certificate validation, track connection attempts, and troubleshoot authentication issues.

## What are connection logs?
<a name="what-are-connection-logs"></a>

Connection logs capture detailed information about TLS handshakes and certificate validation for mutual TLS-enabled distributions, and for distribution tenants on the Anycast static IP addresses of their connection group. Unlike standard access logs that record HTTP request information, connection logs focus specifically on the TLS connection establishment phase, including:
+ Connection status (success/failure)
+ Client certificate details
+ TLS protocol and cipher information
+ Connection timing metrics
+ Custom data from Connection Functions

These logs provide comprehensive visibility into certificate-based authentication events, helping you monitor security, troubleshoot issues, and meet compliance requirements.

## Connections that CloudFront logs
<a name="connection-logs-supported-connections"></a>

CloudFront generates connection logs only for the following connections:
+ Connections to a distribution that has mutual TLS (viewer) enabled. For more information, see [Mutual TLS authentication with CloudFront (Viewer mTLS)](mtls-authentication.md).
+ HTTPS connections to a distribution tenant on the Anycast static IP addresses of its connection group. For more information, see [Connection logs for distribution tenants on Anycast static IPs](#connection-logs-anycast-tenants).

**Important**  
CloudFront doesn't generate connection logs for any other connections. For example, you don't get connection logs for a standard distribution that doesn't use mutual TLS, for distribution tenants on the shared CloudFront IP addresses, or for HTTP connections. You can enable connection logs on a distribution that doesn't use mutual TLS, but the logs contain only the connections listed above.

To enable connection logs, see [Enable connection logs](#enable-connection-logs).

## Connection logs for distribution tenants on Anycast static IPs
<a name="connection-logs-anycast-tenants"></a>

When viewers connect to a distribution tenant through the Anycast static IP addresses of the distribution tenant's connection group, CloudFront can log each HTTPS connection, even when the multi-tenant distribution doesn't use mutual TLS. To get these logs, enable connection logs on the multi-tenant distribution, as described in [Enable connection logs](#enable-connection-logs). CloudFront doesn't log HTTP connections, or connections to the shared CloudFront IP addresses.

In these records, `distributionId` is the multi-tenant distribution, `distributionTenantId` is the distribution tenant, and `serverIp` is the Anycast static IP address that the viewer connected to. The client certificate fields contain `-`, because the viewer doesn't present a client certificate. The following is an example record:

```json
{
    "connectionId": "NSbVU0HLuZtjZEOxeIvLdCmqgCsjq0MRqda1ZxQQVNfCCLrxGZB4-A==",
    "connectionStatus": "Success",
    "clientIp": "192.0.2.110",
    "clientPort": "4996",
    "serverIp": "198.51.100.249",
    "distributionTenantId": "dt_EXAMPLE22222",
    "tlsProtocol": "TLSv1.2",
    "tlsCipher": "ECDHE-RSA-AES128-GCM-SHA256",
    "tlsHandshakeDuration": 70.0,
    "tlsSni": "www.example.com",
    "clientLeafCertSerialNumber": "-",
    "clientLeafCertSubject": "-",
    "clientLeafCertIssuer": "-",
    "clientLeafCertValidity": "-",
    "connectionLogCustomData": "-",
    "eventTimestamp": 1794885872306,
    "distributionId": "EDFDVBD6EXAMPLE"
}
```

## Enable connection logs
<a name="enable-connection-logs"></a>

CloudFront generates connection logs only for connections to distributions with mutual TLS enabled, and for HTTPS connections to distribution tenants on the Anycast static IP addresses of their connection group. For more information, see [Connections that CloudFront logs](#connection-logs-supported-connections). You can send connection logs to multiple destinations including CloudWatch Logs, Amazon Data Firehose, and Amazon S3.

### Prerequisites
<a name="connection-logs-prerequisites"></a>

Before enabling connection logs:
+ Enable mutual TLS for your CloudFront distribution, or serve your distribution tenants from a connection group that uses an Anycast static IP list. CloudFront doesn't generate connection logs for other connections.
+ Enable connection logs for your CloudFront distribution
+ Make sure you have the required permissions for your chosen logging destination
+ For cross-account delivery, configure appropriate IAM policies

### To enable connection logs (Console)
<a name="enable-connection-logs-console"></a>

1. Sign in to the AWS Management Console and open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home).

1. From the distribution list, select your mTLS-enabled distribution, or the multi-tenant distribution of your distribution tenants on Anycast static IPs.

1. Choose the **Logging** tab.

1. Choose **Add**.

1. Select the service to receive your logs:
   + **CloudWatch Logs**
   + **Firehose**
   + **Amazon S3**

1. For **Destination**, select the resource for your chosen service:
   + For CloudWatch Logs, enter the **Log group name**
   + For Firehose, select the **Firehose delivery stream**
   + For Amazon S3, enter the **Bucket name** (optionally with a prefix)

1. (Optional) Configure additional settings:
   + **Field selection:** Select specific log fields to include.
   + **Output format:** Choose from JSON, Plain, w3c, Raw, or Parquet (S3 only).
   + **Field delimiter:** Specify how to separate log fields.

1. Choose **Save changes**

### To enable connection logs (AWS CLI)
<a name="enable-connection-logs-cli"></a>

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

**Note**  
When using the CloudWatch API, you must specify the US East (N. Virginia) Region (us-east-1) even when delivering logs to other Regions.

## Connection log fields
<a name="connection-log-fields"></a>

Connection logs include detailed information about each TLS connection attempt:


| Field | Description | Example | 
| --- | --- | --- | 
| eventTimestamp | Unix epoch time in milliseconds when the connection was established or failed | 1731620046814 | 
| connectionId | Unique identifier for the TLS connection | oLHiEKbQSn8lkvJfA3D4gFowK3\_iZ0g4i5nMUjE1Akod8TuAzn5nzg== | 
| connectionStatus | The status of the mTLS connection attempt. | Success or Failed | 
| clientIp | IP address of the connecting client | 2001:0db8:85a3:0000:0000:8a2e:0370:7334 | 
| clientPort | Port used by the client | 12137 | 
| serverIp | IP address of the CloudFront edge server | 99.84.71.136 | 
| distributionId | CloudFront distribution ID | E2DX1SLDPK0123 | 
| distributionTenantId | CloudFront distribution tenant ID (when applicable) | dt\_2te1Ura9X3R2iCGNjW123 | 
| tlsProtocol | TLS protocol version used | TLSv1.3 | 
| tlsCipher | TLS cipher suite used for the connection | TLS\_AES\_128\_GCM\_SHA256 | 
| tlsHandshakeDuration | Duration of the TLS handshake in milliseconds | 153 | 
| tlsSni | Server Name Indication value from the TLS handshake | d111111abcdef8.cloudfront.net | 
| clientLeafCertSerialNumber | Serial number of the client's certificate | 00:b1:43:ed:93:d2:d8:f3:9d | 
| clientLeafCertSubject | Subject field of the client's certificate | C=US, ST=WA, L=Seattle, O=Amazon.com, OU=CloudFront, CN=client.test.mtls.net | 
| clientLeafCertIssuer | Issuer field of the client's certificate | C=US, ST=WA, L=Seattle, O=Amazon.com, OU=CloudFront, CN=test.mtls.net | 
| clientLeafCertValidity | Validity period of the client's certificate | NotBefore=2025-06-05T23:28:21Z;NotAfter=2125-05-12T23:28:21Z | 
| connectionLogCustomData | Custom data added by using Connection Functions | REVOKED:00:b1:43:ed:93:d2:d8:f3:9d | 

## Connection error codes
<a name="connection-error-codes"></a>

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
Failed:ClientCertOcspProcessingError
Failed:ClientCertOcspDenied
Failed:TcpError
Failed:TcpTimeout
Failed:ConnectionFunctionError
Failed:ConnectionFunctionDenied
Failed:Internal
Failed:UnmappedConnectionError
```

When connections fail, CloudFront records specific reason codes:


| Code | Description | 
| --- | --- | 
| ClientCertMaxChainDepthExceeded | Maximum certificate chain depth exceeded | 
| ClientCertMaxSizeExceeded | Maximum certificate size exceeded | 
| ClientCertUntrusted | Certificate is untrusted | 
| ClientCertNotYetValid | Certificate is not yet valid | 
| ClientCertExpired | Certificate is expired | 
| ClientCertTypeUnsupported | Certificate type is unsupported | 
| ClientCertInvalid | Certificate is invalid | 
| ClientCertIntentInvalid | Certificate intent is invalid | 
| ClientCertRejected | Certificate rejected by custom validation | 
| ClientCertMissing | Certificate is missing | 
| ClientCertOcspProcessingError | An error occurred while CloudFront checked the certificate's revocation status with OCSP | 
| ClientCertOcspDenied | The OCSP check didn't confirm that the certificate is valid, for example because the certificate is revoked | 
| TcpError | An error occurred while attempting to establish a connection | 
| TcpTimeout | The connection was not able to be established within the timeout period | 
| ConnectionFunctionError | An uncaught exception was thrown during Connection Function execution | 
| ConnectionFunctionDenied | The Connection Function denied the connection | 
| Internal | An internal service error occurred | 
| UnmappedConnectionError | An error occurred that does not fall into any of the other categories | 