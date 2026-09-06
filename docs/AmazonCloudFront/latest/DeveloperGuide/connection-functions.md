

# Associate a CloudFront Connection Function
<a name="connection-functions"></a>

CloudFront Connection Functions allow you to implement custom certificate validation logic during TLS handshakes, providing extensions to the built-in mTLS authentication capabilities.

## What are Connection Functions?
<a name="what-are-connection-functions"></a>

Connection Functions are JavaScript functions that run during the TLS handshake after client certificates have been validated. The validated client certificate is passed to the Connection Function at which point the Connection Function can make an additional determination on whether to grant access or not. For detailed information about Connection Functions, see [Customize at the edge with CloudFront Functions](cloudfront-functions.md).

## How Connection Functions work with mTLS
<a name="how-connection-functions-work"></a>

When a client attempts to establish an mTLS connection to your CloudFront distribution, the following sequence occurs:

1. Client initiates TLS handshake with CloudFront edge location.

1. CloudFront requests and receives client certificate.

1. CloudFront performs standard certificate validation against trust store.

1. If the certificate passes standard validation, CloudFront invokes your Connection Function. If **IgnoreCertificateExpiry** is enabled within your **ViewerMtlsConfig**, then your expired—but otherwise valid—certificates are also passed to the Connection Function. If the client certificates are invalid, Connection Functions will not be invoked.

1. Your Connection Function receives parsed certificate information and connection details.

1. Your function makes an allow/deny decision based on custom logic.

1. CloudFront completes or terminates the TLS connection based on your decision.

Connection Functions are invoked for both verify mode and optional mode (when clients present certificates).

## Create a Connection Function
<a name="create-connection-function"></a>

You can create Connection Functions using the CloudFront console or AWS CLI.

### To create a Connection Function (Console)
<a name="create-connection-function-console"></a>

1. Sign in to the AWS Management Console and open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home).

1. In the navigation pane, choose **Functions**.

1. Choose the **Connection Functions** tab and choose **Create Connection Function**.

1. Enter a function name that is unique within your AWS account.

1. Choose **Continue**.

1. In the function editor, write your JavaScript code for certificate validation. The function handler must call either allow or deny.

1. Optional: a KeyValue store can be associated to the Connection Function to implement revocation control.

1. Choose **Save changes**.

### To create a Connection Function (AWS CLI)
<a name="create-connection-function-cli"></a>

The following example shows how to create a Connection Function:

Write your function code in a separate file, for example code.js:

```
function connectionHandler(connection) {
  connection.allow();
}
```

```
aws cloudfront create-connection-function \
  --name "certificate-validator" \
  --connection-function-config '{
      "Comment": "Client certificate validation function",
      "Runtime": "cloudfront-js-2.0"
  }' \
  --connection-function-code fileb://code.js
```

## Connection Function code structure
<a name="connection-function-code-structure"></a>

Connection Functions implement connectionHandler function that receives a connection object containing certificate and connection information. Your function must use either `connection.allow()` or `connection.deny()` to make a decision about the connection.

### Basic Connection Function example
<a name="basic-connection-function-example"></a>

The following example shows a simple Connection Function that verifies the subject field of client certificates:

```
function connectionHandler(connection) {
    // Only process if a certificate was presented
    if (!connection.clientCertificate) {
        console.log("No certificate presented");
        connection.deny();
    }
    
    // Check the subject field for specific organization
    const subject = connection.clientCertificate.certificates.leaf.subject;
    if (!subject.includes("O=ExampleCorp")) {
        console.log("Certificate not from authorized organization");
       connection.deny();
    } else {
        // All checks passed
        console.log("Certificate validation passed");
        connection.allow();
    }
}
```

The full specification of client certificate properties available on the connection object are available here:

```
{
  "connectionId": "Fdb-Eb7L9gVn2cFakz7wWyBJIDAD4-oNO6g8r3vXDV132BtnIVtqDA==", // Unique identifier for this TLS connection
  "clientIp": "203.0.113.42", // IP address of the connecting client (IPv4 or IPv6)
  "clientCertificate": {
    "certificates": {
      "leaf": {
        "serialNumber": "4a:3f:5c:92:d1:e8:7b:6c", // Unique serial number assigned by the issuing CA (hexadecimal)
        "issuer": "CN=Example Corp Intermediate CA,O=Example Corp,C=US", // Distinguished Name (DN) of the certificate authority that issued this certificate.
        "subject": "CN=client.example.com,O=Example Corp,C=US", // Distinguished Name (DN) of the certificate holder.
        "validity": {
          "notBefore": "2024-01-15T00:00:00Z", // Certificate validity start date (ISO 8601 format)
          "notAfter": "2025-01-14T23:59:59Z"   // Certificate expiration date (ISO 8601 format)
        },
        "sha256Fingerprint": "a1b2c3d4e5f6...abc123def456", // SHA-256 hash of the certificate (64 hex characters)
        "ocspEndpoint": "http://ocsp.example.com", // OCSP responder URL from the certificate's AIA extension.
        "san": "DNS:client.example.com,DNS:api.example.com", // Subject Alternative Names.
        "spki": "30820122300d06092a864886f70d01010105000382010f003082010a0282010100...", // Subject Public Key Info (DER-encoded, hex).
        "sanHex": "3032820f636c69656e742e6578616d706c652e636f6d820f6170692e6578616d706c652e636f6d..." // Subject Alternative Names (DER-encoded, hex).
      },
      "intermediates": [
        {
          "serialNumber": "00:d4:04:a5:fd:cb:20:37:54", // Serial number of the intermediate certificate.
          "issuer": "CN=Example Corp Root CA,O=Example Corp,C=US", // Issuer of the intermediate certificate.
          "subject": "CN=Example Corp Intermediate CA,O=Example Corp,C=US", // Subject of the intermediate certificate.
          "validity": {
            "notBefore": "2020-01-01T00:00:00Z",
            "notAfter": "2030-01-01T23:59:59Z"
          },
          "sha256Fingerprint": "b2c3d4e5f6a1...def456abc123",
          "ocspEndpoint": "http://ocsp.example.com/intermediate",
          "san": "DNS:ca.example.com",
          "spki": "30820122300d06092a864886f70d01010105000382010f003082010a0282010100b389dd513b...",
          "sanHex": "3015820d63612e6578616d706c652e636f6d..."
        }
      ]
    }
  }
}
```

## Associate a Connection Function
<a name="associate-connection-function-section"></a>

After creating your Connection Function, you must publish it to the LIVE stage and associate it with your distribution.

### To publish and associate a Connection Function (Console)
<a name="publish-associate-console"></a>

1. Sign in to the AWS Management Console and open the CloudFront console at [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home).

1. In the navigation pane, choose **Functions**

1. Choose the **Connection Functions** tab and select your Connection Function.

1. Choose **Publish** to move it to the LIVE stage.

1. Choose **Add association** in the associated distributions table below the publishing section.

1. Select the distribution with Viewer mTLS enabled that you wish to associate.

Alternatively published Connection Functions can also be associated from the distribution details page.

1. Navigate to the console home page where all your distributions are listed.

1. Select the distribution that you wish to associate.

1. Choose the **General** tab.

1. In the **Settings** section, choose **Edit**.

1. In the **Connectivity** section, find **Viewer mutual authentication (mTLS)**.

1. For **Connection Function**, select your function.

1. Choose **Save changes**.

### To associate a Connection Function (AWS CLI)
<a name="associate-connection-function-cli"></a>

The following example shows how to associate a Connection Function with a distribution:

```
// DistributionConfig:
{
   ...other settings,
    "ConnectionFunctionAssociation": {
        "Id": "cf_30c2CV2elHwCoInb3LtcaUJkZeD"
    }
}
```

## Use cases for Connection Functions
<a name="connection-function-use-cases"></a>

Connection Functions enable several advanced mTLS use cases:
+ **Certificate attribute validation** - Verify specific fields in client certificates like organizational unit requirements or subject alternative name patterns.
+ **Certificate revocation checking** - Implement custom certificate revocation checking using KeyValueStore to store revoked certificate serial numbers.
+ **IP-based certificate policies** - Apply different certificate policies based on client IP addresses or geographic restrictions.
+ **Multi-tenant validation** - Implement tenant-specific validation rules where different certificate requirements apply based on hostnames or certificate attributes.

**Note**  
Connection Functions run once per client connection during the TLS handshake.  
Connection Functions can only allow or deny connections, not modify HTTP requests/responses.  
Only LIVE stage functions (published) can be associated with distributions.  
Each distribution can have at most one Connection Function.

## Next steps
<a name="connection-function-next-steps"></a>

After associating a Connection Function with your CloudFront distribution, you can configure optional settings to customize the behavior of your mTLS implementation. For detailed instructions on configuring additional settings such as an optional client certificate validation mode, see [Configuring additional settings](configuring-additional-settings.md).