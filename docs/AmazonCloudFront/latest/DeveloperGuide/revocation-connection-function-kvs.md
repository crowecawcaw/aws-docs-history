# Revocation using CloudFront Connection Function and KVS

You can implement certificate revocation checking for mutual TLS authentication by combining CloudFront Connection Functions with KeyValueStore. This approach provides a scalable, real-time certificate revocation mechanism that complements CloudFront's built-in certificate validation.

Connection Functions are JavaScript functions that run during TLS connection
establishment at CloudFront edge locations and allow you to implement custom certificate
validation logic for mTLS authentication. For detailed information about Connection Functions, see [Associate a CloudFront Connection Function](connection-functions.md "connection-functions.md").

## How certificate revocation works with Connection Functions

CloudFront's standard certificate validation verifies the certificate chain, signature, and expiration but doesn't include built-in certificate revocation checking. By using Connection Functions, you can implement custom revocation checking during the TLS handshake.

The certificate revocation process works as follows:

1. Store revoked certificate serial numbers in a CloudFront KeyValueStore.
2. When a client presents a certificate, your Connection Function is invoked.
3. The function checks the certificate's serial number against the KeyValueStore.
4. If the serial number is found in the store, the certificate is revoked.
5. Your function denies the connection for revoked certificates.

This approach provides near-real-time revocation checking across CloudFront's global edge network.

## Set up KeyValueStore for revoked certificates

First, create a KeyValueStore to store the serial numbers of revoked certificates:

### To create a KeyValueStore (Console)

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Key value stores**.
3. Choose **Create key value store**.
4. Enter a name for your key value store (e.g., revoked-certificates).
5. (Optional) Add a description.
6. Choose **Create key value store**.

### To create a KeyValueStore (AWS CLI)

The following example shows how to create a KeyValueStore:

```

aws cloudfront create-key-value-store \
  --name "revoked-certificates" \
  --comment "Store for revoked certificate serial numbers"

```

## Import revoked certificate serial numbers

After creating a KeyValueStore, you need to import the serial numbers of revoked certificates:

### Prepare revocation data

Create a JSON file with your revoked certificate serial numbers:

```
{
  "data": [
    {
      "key": "ABC123DEF456",
      "value": ""
    },
    {
      "key": "789XYZ012GHI",
      "value": ""
    }
  ]
}
```

### Import from S3

1. Upload the JSON file to an S3 bucket
2. Import the file to your KeyValueStore:

```
aws cloudfront create-key-value-store \
  --name "revoked-certificates" \
  --import-source '{
    "SourceType": "S3",
    "SourceARN": "arn:aws:s3:::amzn-s3-demo-bucket1/revoked-serials.json"
  }'
```

## Create a Connection Function for revocation checking

Create a Connection Function that checks certificate serial numbers against your KeyValueStore:

### Connection Function code example

The following example shows a Connection Function that performs certificate revocation checking:

```

import cf from 'cloudfront';

async function connectionHandler(connection) {
    const kvsHandle = cf.kvs();

    // Get client certificate serial number
    const clientSerialNumber = connection.clientCertificate.certificates.leaf.serialNumber;

    // Check if the serial number exists in the KeyValueStore
    const isRevoked = await kvsHandle.exists(clientSerialNumber.replaceAll(':', ''));

    if (isRevoked) {
        console.log(`Certificate ${clientSerialNumber} is revoked. Denying connection.`);
        connection.logCustomData(`REVOKED:${clientSerialNumber}`);
        connection.deny();
    } else {
        console.log(`Certificate ${clientSerialNumber} is valid. Allowing connection.`);
        connection.allow();
    }

}

```

### To create the Connection Function (AWS CLI)

The following example shows how to create a Connection Function with KeyValueStore association:

```

aws cloudfront create-connection-function \
  --name "revocation-checker" \
  --connection-function-config '{
      "Comment": "Certificate revocation checking function",
      "Runtime": "cloudfront-js-2.0",
      "KeyValueStoreAssociations": {
          "Quantity": 1,
          "Items": [
              {
                  "KeyValueStoreARN": "arn:aws:cloudfront::123456789012:key-value-store/revoked-certificates"
              }
          ]
      }
  }' \
  --connection-function-code fileb://revocation-checker.js

```

## Associate the function with your distribution

After creating and publishing your Connection Function, associate it with your
mTLS-enabled CloudFront distribution as described in the [Associate a CloudFront Connection Function](connection-functions.md "connection-functions.md")
section.
