

# Certificate revocation
<a name="certificate-revocation"></a>

When certificates need to be revoked — due to compromise, policy changes, or terminated relationships — you need a mechanism to reject those certificates during the mTLS handshake. CloudFront provides two native approaches to certificate revocation, and you can combine them for layered control.
+ **OCSP (Online Certificate Status Protocol)** — CloudFront queries your Certificate Authority's OCSP responder in real time to check whether a client certificate has been revoked. Enable OCSP on your trust store and CloudFront handles the validation automatically during the TLS handshake. OCSP results are also visible in Connection Functions, giving you programmatic access to revocation status for custom decision-making.
+ **CloudFront Functions and KeyValueStore** — You maintain a list of revoked certificate serial numbers in a CloudFront KeyValueStore. A Connection Function queries the KeyValueStore during the TLS handshake and allows or denies the connection. This gives you full control over revocation data, update timing, and custom logic like grace periods or IP-based exceptions.


**Comparison: OCSP vs. CloudFront Functions with KeyValueStore**  

|  | OCSP | CloudFront Functions \+ KeyValueStore | 
| --- | --- | --- | 
| Data source | Certificate Authority's OCSP responder | You manage the revocation list | 
| Update mechanism | Real-time query to CA | You push updates to KeyValueStore | 
| Custom logic | Available via Connection Functions | Built into your function code | 
| External dependency | Requires CA OCSP responder availability | No external dependency | 
| Best for | CAs that maintain OCSP responders; real-time CA-authoritative status | Self-managed revocation; custom policies; CAs without OCSP support | 

You can use both approaches together. Enable OCSP for CA-authoritative revocation checking, then use a Connection Function to layer additional logic on top of the OCSP result — for example, allowing revoked certificates from trusted IP ranges during a grace period.

## OCSP (Online Certificate Status Protocol)
<a name="ocsp-revocation"></a>

OCSP is a real-time protocol that checks a certificate's revocation status directly with the Certificate Authority (CA). During the certificate signing process, the CA embeds an OCSP responder URL in the certificate. When a client presents their certificate during the mTLS handshake, CloudFront sends an OCSP request to the embedded responder URL and acts on the response: valid certificates proceed, revoked certificates are terminated.

CloudFront validates the entire certificate chain — the leaf certificate and up to three intermediate certificates — each against their respective OCSP responder URLs. Certificates in the trust store are treated as trust anchors and are excluded from OCSP validation. This applies to any certificate in the trust store, whether it is a root CA or an intermediate CA. When you place an intermediate CA in your trust store, it becomes a trust anchor and chain validation terminates at that certificate. Only the certificates below it in the chain are OCSP-validated.

### Enable OCSP
<a name="enable-ocsp"></a>

Enable OCSP on your trust store. When enabled, CloudFront automatically performs OCSP validation for any client certificate that contains an OCSP responder URL in its Authority Information Access (AIA) extension. Once OCSP is enabled, every certificate in the client certificate chain below the trust anchor must have an OCSP URL. If any certificate below the trust anchor doesn't contain an OCSP URL, CloudFront does not establish the connection. Certificates in the trust store (trust anchors) are exempt from this requirement.

CloudFront caches OCSP responses at the edge to reduce round-trip time and protect against OCSP responder downtime. OCSP responses are cached for approximately 30 minutes, and updated revocation status may take up to 30 minutes to be reflected.

### OCSP results in Connection Functions
<a name="ocsp-results-connection-functions"></a>

When a Connection Function is configured on the same distribution, CloudFront invokes it after OCSP validation completes. The connection object contains the OCSP status for the leaf and intermediate certificates:

```
{
  "clientCertificate": {
    "certificates": {
      "leaf": {
        "subject": "CN=client.example.com, O=Example Org",
        "issuer": "CN=Intermediate CA, O=Example Org",
        "serialNumber": "00:a7:30:9e:73:7b:3e:63:bd:b7:c0:7e:bf:d5:c9:86",
        "validity": {
          "notBefore": "2024-01-01T00:00:00Z",
          "notAfter": "2025-01-01T00:00:00Z"
        },
        "sha256Fingerprint": "AB:CD:EF:12:34:56:78:90:AB:CD:EF:12:34:56:78:90:AB:CD:EF:12:34:56:78:90:AB:CD:EF:12:34:56:78:90",
        "ocspEndpoint": "http://ocsp.example.org"
      },
      "intermediates": [
        {
          "subject": "CN=Intermediate CA, O=Example Org",
          "issuer": "CN=Root CA, O=Example Org",
          "serialNumber": "00:a7:30:9e:73:7b:3e:63:bd:b7:c0:7e:bf:d5:c9:86",
          "validity": {
            "notBefore": "2020-01-01T00:00:00Z",
            "notAfter": "2030-01-01T00:00:00Z"
          },
          "sha256Fingerprint": "12:34:56:78:90:AB:CD:EF:12:34:56:78:90:AB:CD:EF:12:34:56:78:90:AB:CD:EF:12:34:56:78:90:AB:CD:EF",
          "ocspEndpoint": "http://ocsp.example.org"
        }
      ]
    },
    "revocationStatus": {
      "chainValidity": "Valid",           // "Valid" | "Invalid" | "Unknown"
      "certificates": {
        "leaf": {
          "method": "OCSP",               // "OCSP"
          "status": "Good",               // "Good" | "Revoked" | "Unknown" | "Error"
          "serialNumber": "00:a7:30:9e:73:7b:3e:63:bd:b7:c0:7e:bf:d5:c9:86"
        },
        "intermediates": [
          {
            "method": "OCSP",             // "OCSP"
            "status": "Error",            // "Good" | "Revoked" | "Unknown" | "Error"
            "errorType": "InternalError", // "InternalError" | "OCSP response verification failed: {Type}"
            "serialNumber": "00:a7:30:9e:73:7b:3e:63:bd:b7:c0:7e:bf:d5:c9:86"
          }
        ]
      }
    }
  },
  "clientIp":"127.0.0.1",
  "endpoint":"d123.cloudfront.net",
  "distributionId":"E1NXS4MQZH501R",
  "connectionId":"xdzQ6lJUDUt8b7OuqOD8lmzOC9HcMaXPmhH5ZdzLCZpKxqzfCPpR4A=="
}
```

The `chainValidity` field can be `Valid`, `Invalid`, or `Unknown`. Individual certificate `status` values can be `Good`, `Revoked`, `Unknown`, or `Error`. The `errorType` field contains `InternalError` or `OCSP response verification failed: {Type}` when the status is `Error`.

The Connection Function can override the OCSP result — for example, allowing a revoked certificate from a trusted IP range, or denying a certificate that OCSP reports as "good" based on additional business logic.

**Note**  
The `errorType` field will only be present if the status is `Error`.

### Example: Custom OCSP handling with trusted IP exception
<a name="ocsp-example"></a>

```
function connectionHandler(connection) {
    var revocationStatus = connection.clientCertificate.revocationStatus;
    var trustedIP = (connection.clientIp === "[IP_ADDRESS]");

    if (revocationStatus.chainValidity === "Invalid") {
        if (trustedIP) {
            connection.allow();
        } else {
            connection.deny();
        }
    } else if (revocationStatus.certificates.leaf.status === "Error") {
        console.log(revocationStatus.certificates.leaf.errorType);
        connection.deny();
    } else {
        connection.allow();
    }
}
```

### OCSP failure behavior
<a name="ocsp-failure-behavior"></a>

When CloudFront cannot determine a certificate's revocation status — because the OCSP responder is unreachable, returns an error, or returns "unknown" — CloudFront denies the connection by default. To implement soft-fail behavior, use a Connection Function. Connection Functions will not be executed if OCSP is enabled and the OCSP URL is absent in the client certificates. The OCSP result is available in the connection object, and your function can allow connections when the OCSP status is undetermined:

```
async function connectionHandler(connection) {
    var revocationStatus = connection.clientCertificate.revocationStatus;

    if (revocationStatus.certificates.leaf.status === "Error" ||
        revocationStatus.certificates.leaf.status === "Unknown") {
        // OCSP responder unreachable — allow connection (soft-fail)
        connection.logCustomData(`OCSP_SOFT_FAIL:${revocationStatus.certificates.leaf.errorType}`);
        return connection.allow();
    }

    if (revocationStatus.chainValidity === "Invalid") {
        return connection.deny();
    }

    return connection.allow();
}
```

## Certificate revocation with CloudFront Functions and KeyValueStore
<a name="kvs-revocation"></a>

You can use CloudFront Connection Functions with KeyValueStore to implement certificate revocation checking without any external dependency. You maintain a list of revoked certificate serial numbers in a KeyValueStore, and your Connection Function checks each client certificate against this list during the TLS handshake.

The certificate revocation process works as follows:

1. Store revoked certificate serial numbers in a CloudFront KeyValueStore.

1. When a client presents a certificate, your Connection Function is invoked.

1. The function checks the certificate's serial number against the KeyValueStore.

1. If the serial number is found in the store, the certificate is revoked.

1. Your function denies the connection for revoked certificates.

This approach provides near-real-time revocation checking across CloudFront's global edge network.

To implement this approach, you need:
+ A distribution configured with viewer mTLS
+ A KeyValueStore containing revoked certificate serial numbers
+ A Connection Function that queries the KeyValueStore to check certificate status

When a client connects, CloudFront validates the certificate against the trust store, then runs your Connection Function. Your function checks the certificate serial number against the KeyValueStore and allows or denies the connection.

### Step 1: Create a KeyValueStore for revoked certificates
<a name="step1-create-kvs"></a>

Prepare your revoked certificate serial numbers in JSON format:

```
{
  "data": [
    { "key": "ABC123DEF456", "value": "" },
    { "key": "789XYZ012GHI", "value": "" }
  ]
}
```

Upload this JSON file to an S3 bucket, then create the KeyValueStore:

```
aws s3 cp revoked-serials.json s3://your-bucket-name/revoked-serials.json

aws cloudfront create-key-value-store \
  --name revoked-serials-kvs \
  --import-source '{
    "SourceType": "S3",
    "SourceARN": "arn:aws:s3:::your-bucket-name/revoked-serials.json"
  }'
```

Wait for the KeyValueStore to finish provisioning. Check the status with:

```
aws cloudfront get-key-value-store --name "revoked-serials-kvs"
```

### Step 2: Create the revocation Connection Function
<a name="step2-create-revocation-function"></a>

Create a Connection Function that checks certificate serial numbers against the KeyValueStore:

```
aws cloudfront create-connection-function \
  --name "revocation-control" \
  --connection-function-config file://connection-function-config.json \
  --connection-function-code file://connection-function-code.txt
```

The configuration file specifies the KeyValueStore association:

```
{
  "Runtime": "cloudfront-js-2.0",
  "Comment": "A function that implements revocation control via KVS",
  "KeyValueStoreAssociations": {
    "Quantity": 1,
    "Items": [
      {
        "KeyValueStoreArn": "arn:aws:cloudfront::account-id:key-value-store/kvs-id"
      }
    ]
  }
}
```

Sample Connection Function code:

```
import cf from 'cloudfront';

async function connectionHandler(connection) {
    const kvsHandle = cf.kvs();

    // Get client serial number from client certificate
    const clientSerialNumber =
        connection.clientCertificate.certificates.leaf.serialNumber;

    // Check KVS to see if serial number exists as a key
    // Remove : from the clientSerialNumber if KVS entries dont have it
    const serialNumberExistsInKvs =
        await kvsHandle.exists(clientSerialNumber.replaceAll(":", ""));

    // Deny connection if serial number exists in KVS
    if (serialNumberExistsInKvs) {
        console.log("Connection denied — certificate revoked");
        connection.logCustomData("Connection denied — certificate revoked");
        return connection.deny();
    }

    // Allow connections that don't exist in KVS
    console.log("Connection allowed");
    return connection.allow();
}
```

### Step 3: Test your revocation function
<a name="step3-test-revocation-function"></a>

Use the CloudFront console to test your Connection Function with sample certificates. Navigate to the Connection Function in the console and use the Test tab.
+ Paste a sample certificate in PEM format into the test interface.
+ Optionally specify a client IP address for testing IP-based logic.
+ Choose **Test function** to see the execution results.
+ Review the execution logs to verify your function logic.

Test with both valid and revoked certificates to ensure your function handles both scenarios correctly.

### Step 4: Associate the function to your distribution
<a name="step4-associate-function"></a>

Once you publish your Connection Function, associate it with your mTLS-enabled distribution to activate certificate revocation checking. Navigate to your distribution settings, scroll to the "Viewer mutual authentication (mTLS)" section, select your Connection Function, and save the changes.

## Advanced revocation strategies
<a name="advanced-revocation-strategies"></a>

### Combine OCSP with Connection Function logic
<a name="combine-ocsp-kvs"></a>

You can enable OCSP for CA-authoritative revocation checking and layer a Connection Function on top for custom policies. The Connection Function receives the OCSP result and can apply additional logic:
+ **Grace periods** — Allow revoked certificates from internal networks for a defined period during certificate rotation.
+ **Emergency access** — Permit connections from specific IPs even when OCSP reports revoked status.
+ **Custom deny logic** — Block certificates that OCSP reports as "good" based on your own revocation data in KeyValueStore.

**Example OCSP \+ KVS combined revocation**  

```
import cf from 'cloudfront';

async function connectionHandler(connection) {
    var kvsHandle = cf.kvs();
    var revocationStatus = connection.clientCertificate.revocationStatus;
    var serialNumber = connection.clientCertificate.certificates.leaf.serialNumber;

    // Check your own revocation list first (immediate revocation, no cache delay)
    var inKvs = await kvsHandle.exists(serialNumber.replaceAll(":", ""));
    if (inKvs) {
        connection.logCustomData("KVS_REVOKED:" + serialNumber);
        return connection.deny();
    }

    // Then check OCSP result
    if (revocationStatus.chainValidity === 'Valid' && revocationStatus.certificates.leaf.status === "Revoked") {
        // OCSP says revoked — allow grace period from trusted IPs
        if (connection.clientIp.startsWith("10.0.")) {
            connection.logCustomData("GRACE_PERIOD:" + serialNumber + ":" + connection.clientIp);
            return connection.allow();
        }
        connection.logCustomData("OCSP_REVOKED:" + serialNumber);
        return connection.deny();
    }

    connection.allow();
}
```

This pattern gives you immediate revocation via KVS (no cache delay) plus CA-authoritative revocation via OCSP, with custom exception handling in between.