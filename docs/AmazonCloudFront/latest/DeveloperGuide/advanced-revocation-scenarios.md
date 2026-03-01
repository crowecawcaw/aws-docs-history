# Advanced revocation scenarios

For more complex certificate revocation requirements, consider these additional
configurations:

###### Topics

- [Convert Certificate Revocation Lists (CRL) to KeyValueStore format](#convert-crl-kvs-format "#convert-crl-kvs-format")
- [Handle multiple Certificate Authorities](#handle-multiple-cas "#handle-multiple-cas")
- [Add custom data to connection logs](#add-custom-data-logs "#add-custom-data-logs")
- [Manage CRL updates](#manage-crl-updates "#manage-crl-updates")
- [Plan KeyValueStore capacity](#plan-kvs-capacity "#plan-kvs-capacity")

## Convert Certificate Revocation Lists (CRL) to KeyValueStore format

If you have a Certificate Revocation List (CRL) file, you can convert it to
KeyValueStore JSON format using OpenSSL and jq:

**Convert CRL to KeyValueStore format**

Extract serial numbers from the CRL file:

```
openssl crl -text -noout -in rfc5280_CRL.crl | \
  awk '/Serial Number:/ {print $3}' | \
  cut -d'=' -f2 | \
  sed 's/../&:/g;s/:$//' >> serialnumbers.txt
```

Convert the serial numbers to KeyValueStore JSON format:

```
jq -R -s 'split("\n") | map(select(length > 0)) | {data: map({"key": ., "value": ""})}' \
  serialnumbers.txt >> serialnumbers_kvs.json
```

Upload the formatted file to S3 and create the KeyValueStore as described in
Step 1.

## Handle multiple Certificate Authorities

When your TrustStore contains multiple Certificate Authorities (CAs), include
the issuer information in your KeyValueStore keys to avoid conflicts between
certificates from different CAs that might have the same serial number.

For multi-CA scenarios, use a combination of the issuer's SHA1 hash and the
serial number as the key:

```
import cf from 'cloudfront';

async function connectionHandler(connection) {
    const kvsHandle = cf.kvs();
    const clientCert = connection.clientCertInfo;

    // Create composite key with issuer hash and serial number
    const issuer = clientCert.issuer.replace(/[^a-zA-Z0-9]/g, '').substring(0, 20);
    const serialno = clientCert.serialNumber;
    const compositeKey = `${issuer}_${serialno}`;

    const cert_revoked = await kvsHandle.exists(compositeKey);

    if (cert_revoked) {
        console.log(`Blocking revoked cert: ${serialno} from issuer: ${issuer}`);
        connection.deny();
    } else {
        connection.allow();
    }
}
```

###### Note

Using issuer identifier + serial number creates longer keys, which may
reduce the total number of entries you can store in the
KeyValueStore.

## Add custom data to connection logs

Connection functions can add custom data to CloudFront connection logs using the
logCustomData method. This lets you include revocation check results,
certificate information, or other relevant data in your logs.

```
async function connectionHandler(connection) {
    const kvsHandle = cf.kvs();
    const clientSerialNumber = connection.clientCertInfo.serialNumber;
    const serialNumberExistsInKvs = await kvsHandle.exists(clientSerialNumber);

    if (serialNumberExistsInKvs) {
        // Log revocation details to connection logs
        connection.logCustomData(`REVOKED:${clientSerialNumber}:DENIED`);
        console.log("Connection denied - certificate revoked");
        return connection.deny();
    }

    // Log successful validation
    connection.logCustomData(`VALID:${clientSerialNumber}:ALLOWED`);
    console.log("Connection allowed");
    return connection.allow();
}
```

Custom data is limited to 800 bytes of valid UTF-8 text. If you exceed this
limit, CloudFront truncates the data to the nearest valid UTF-8 boundary.

###### Note

Custom data logging only works when connection logs are enabled for your
distribution. If connection logs are not configured, the logCustomData
method is a no-op.

## Manage CRL updates

Certificate Authorities can issue two types of CRLs:

- **Full CRLs**: Contain a complete list of
  all revoked certificates
- **Delta CRLs**: Only list certificates
  revoked since the last full CRL

For full CRL updates, create a new KeyValueStore with the updated data and
redirect the Connection Function association to the new KeyValueStore. This
approach is simpler than calculating differences and performing incremental
updates.

For delta CRL updates, use the update-keys command to add new revoked
certificates to the existing KeyValueStore:

```
aws cloudfront update-key-value-store \
  --name "revoked-serials-kvs" \
  --if-match "current-etag" \
  --put file://delta-revoked-serials.json
```

## Plan KeyValueStore capacity

KeyValueStore has a 5 MB size limit and supports up to 10 million key-value
pairs. Plan your revocation list capacity based on your key format and data
size:

- **Serial number only**: Efficient storage
  for simple revocation checking
- **Issuer identifier + serial number**:
  Longer keys for multi-CA environments

For large revocation lists, consider implementing a tiered approach where you
maintain separate KeyValueStores for different certificate categories or time
periods.
