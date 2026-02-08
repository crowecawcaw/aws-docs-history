# Bring Your Own Certificate Authority (BYOCA)

By default, when a public key certificate is needed for asymmetric(RSA,ECC) keys created within the service,
these certificates are issued by a AWS Payment Cryptography and account-unique certificate authority(CA). This is intended to make it
simple to use X.509 without the burden of identifying or setting up a CA or managing Certificate Signing Requests(CSR).

AWS Payment Cryptography also provides the ability to use your own CA when it is required for policy or compliance reasons.

## Overview

The BYOCA feature allows you to use your own Certificate Authority anywhere that certificates are used, including TR-34 import/export,
RSA Unwrap, and ECDH-based key transfers.
This is useful when you need to maintain a consistent certificate chain across your
organization or when working with partners who require specific CA certificates.
The following example demonstrates the BYOCA workflow using TR-34 key export.

The three key differences compared to the standard TR-34 export flow are:

1. The signing RSA key is explicitly created using [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md"). Previously, it was implicitly created via [GetParametersForExport](../DataAPIReference/API_GetParametersForExport.md "../DataAPIReference/API_GetParametersForExport.md").
2. A new API [GetCertificateSigningRequest](../DataAPIReference/API_GetCertificateSigningRequest.md "../DataAPIReference/API_GetCertificateSigningRequest.md") creates a Certificate Signing Request (CSR) that can be signed by your external CA.
3. The [ExportKey](../DataAPIReference/API_ExportKey.md "../DataAPIReference/API_ExportKey.md") API is extended to allow a certificate to be provided at runtime. Previously, this was implicitly provided by `import-token`, which becomes an optional field.

###### Important Considerations

- These examples use RSA-2048 keys and wrap a TDES-2KEY key. When exporting AES-128, make sure that all keys are RSA-3072 or RSA-4096.
- The most common error is that the key represented by `SigningKeyIdentifier` and `SigningKeyCertificate` do not match.

## BYOCA Workflow

The following steps demonstrate the complete BYOCA workflow for TR-34 export.

###### Steps

- [Step 1: Create RSA Key](#keyexchange-byoca.create-rsa "#keyexchange-byoca.create-rsa")
- [Step 2: Generate Certificate Signing Request](#keyexchange-byoca.generate-csr "#keyexchange-byoca.generate-csr")
- [Step 3: Review CSR (Optional)](#keyexchange-byoca.review-csr "#keyexchange-byoca.review-csr")
- [Step 4: Sign the CSR with a Certificate Authority](#keyexchange-byoca.sign-csr "#keyexchange-byoca.sign-csr")
- [Step 5: Import CA Certificate](#keyexchange-byoca.import-ca "#keyexchange-byoca.import-ca")
- [Step 6: Get KRD Encryption Certificate](#keyexchange-byoca.get-krd "#keyexchange-byoca.get-krd")
- [Step 7: Export Key with BYOCA](#keyexchange-byoca.export-key "#keyexchange-byoca.export-key")

### Step 1: Create RSA Key

First, create an RSA Key Pair that will ultimately be the KDH Signing Certificate. You can add tags to identify the key's purpose.

###### Example Create RSA Key for Signing

```
`$` `aws payment-cryptography create-key --exportable \
 --key-attributes KeyAlgorithm=RSA_2048,KeyUsage=TR31_S0_ASYMMETRIC_KEY_FOR_DIGITAL_SIGNATURE,KeyClass=ASYMMETRIC_KEY_PAIR,KeyModesOfUse='{Sign=True}'`
```

```
`{
 "Key": {
 "KeyArn": "arn:aws:payment-cryptography:us-east-1:111122223333:key/xgmq6fs6uow736uc",
 "KeyAttributes": {
 "KeyUsage": "TR31_S0_ASYMMETRIC_KEY_FOR_DIGITAL_SIGNATURE",
 "KeyClass": "ASYMMETRIC_KEY_PAIR",
 "KeyAlgorithm": "RSA_2048",
 "KeyModesOfUse": {
 "Sign": true
 }
 },
 "KeyCheckValue": "41E3723C",
 "KeyCheckValueAlgorithm": "SHA_1",
 "Enabled": true,
 "Exportable": true,
 "KeyState": "CREATE_COMPLETE",
 "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY"
 }
}`
```

Take note of the `KeyArn` as you'll need it in the next step.

### Step 2: Generate Certificate Signing Request

Generate a Certificate Signing Request (CSR) to be signed by your external CA using the [GetCertificateSigningRequest](../DataAPIReference/API_GetCertificateSigningRequest.md "../DataAPIReference/API_GetCertificateSigningRequest.md") API. The output is a base64-encoded PEM file.
If you base64 decode the contents and save them, you will have a valid CSR in PEM format.

###### Example Generate CSR

```
`$` `aws payment-cryptography-data get-certificate-signing-request \
 --key-identifier arn:aws:payment-cryptography:us-east-1:111122223333:key/xgmq6fs6uow736uc \
 --signing-algorithm SHA512 \
 --certificate-subject '{
 "CommonName": "MyCertificateAWSUSEAST",
 "Organization": "Amazon",
 "OrganizationUnit": "PaymentCryptography",
 "Country": "US",
 "StateOrProvince": "Virginia",
 "City": "Arlington"
 }'`
```

```
`{
 "CertificateSigningRequest": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS0..."
}`
```

The `CertificateSigningRequest` field contains the base64-encoded CSR that you'll send to your CA for signing.

### Step 3: Review CSR (Optional)

You can optionally use OpenSSL to review the CSR contents and ensure it's valid and as expected.

###### Example Review CSR with OpenSSL

```
`$` `echo "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS0..." | base64 -d | openssl req -text`
```

### Step 4: Sign the CSR with a Certificate Authority

After generating the CSR, you need to have it signed by a Certificate Authority (CA). In production environments,
you would typically use AWS Private CA or your organization's established CA infrastructure.
For testing purposes, you can use OpenSSL to create a self-signed certificate.

#### Using AWS Private CA

To sign the CSR using AWS Private CA, first decode the base64-encoded CSR and save it to a file, then use the
[IssueCertificate](../../../acm-pca/latest/APIReference/API_IssueCertificate.md "../../../acm-pca/latest/APIReference/API_IssueCertificate.md") API.

###### Example Sign CSR with AWS Private CA

```
`$` `echo "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS0..." | base64 -d > csr.pem`

`$` `aws acm-pca issue-certificate \
 --certificate-authority-arn arn:aws:acm-pca:us-east-1:111122223333:certificate-authority/12345678-1234-1234-1234-123456789012 \
 --csr fileb://csr.pem \
 --signing-algorithm SHA256WITHRSA \
 --validity Value=365,Type=DAYS`
```

```
`{
 "CertificateArn": "arn:aws:acm-pca:us-east-1:111122223333:certificate-authority/12345678-1234-1234-1234-123456789012/certificate/abcdef1234567890"
}`
```

Then retrieve the signed certificate:

###### Example Retrieve Signed Certificate

```
`$` `aws acm-pca get-certificate \
 --certificate-authority-arn arn:aws:acm-pca:us-east-1:111122223333:certificate-authority/12345678-1234-1234-1234-123456789012 \
 --certificate-arn arn:aws:acm-pca:us-east-1:111122223333:certificate-authority/12345678-1234-1234-1234-123456789012/certificate/abcdef1234567890`
```

```
`{
 "Certificate": "-----BEGIN CERTIFICATE-----\nMIID...\n-----END CERTIFICATE-----",
 "CertificateChain": "-----BEGIN CERTIFICATE-----\nMIID...\n-----END CERTIFICATE-----"
}`
```

Save the certificate content for use in the export step. You'll need to base64-encode it when providing it to the `ExportKey` API.

#### Using OpenSSL for Testing

For testing purposes, you can use OpenSSL to create a self-signed CA and sign the CSR. First, create a CA private key and self-signed certificate:

###### Example Create Test CA with OpenSSL

```
`$` `# Generate CA private key
openssl genrsa -out ca-key.pem 4096`

`$` `# Create self-signed CA certificate
openssl req -new -x509 -days 3650 -key ca-key.pem -out ca-cert.pem \
 -subj "/C=US/ST=Virginia/L=Arlington/O=TestOrg/CN=Test CA"`
```

Then decode the CSR from the previous step and sign it with your test CA:

###### Example Sign CSR with OpenSSL

```
`$` `# Decode the base64-encoded CSR
echo "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS0..." | base64 -d > csr.pem`

`$` `# Sign the CSR with the CA
openssl x509 -req -in csr.pem -CA ca-cert.pem -CAkey ca-key.pem \
 -CAcreateserial -out signed-cert.pem -days 365 -sha512`
```

```
`Certificate request self-signature ok
subject=C=US, ST=Virginia, L=Arlington, O=Amazon, OU=PaymentCryptography, CN=MyCertificateAWSUSEAST`
```

The signed certificate is now in `signed-cert.pem`. You'll need to base64-encode this certificate when providing it to the `ExportKey` API:

###### Example Base64 Encode the Signed Certificate

```
`$` `cat signed-cert.pem | base64 -w 0`
```

### Step 5: Import CA Certificate

Any CA being used needs to be trusted first to prevent arbitrary certificates from being used.
Import your external CA's root certificate using the [ImportKey](../APIReference/API_ImportKey.md "../APIReference/API_ImportKey.md") API. If using an intermediate CA, call `import-key` again
but specify `TrustedPublicKey` instead of `RootCertificatePublicKey` and specify the root CA ARN.

###### Example Import Root CA Certificate

```
`$` `aws payment-cryptography import-key --key-material='{
 "RootCertificatePublicKey": {
 "KeyAttributes": {
 "KeyAlgorithm": "RSA_4096",
 "KeyClass": "PUBLIC_KEY",
 "KeyModesOfUse": {
 "Verify": true
 },
 "KeyUsage": "TR31_S0_ASYMMETRIC_KEY_FOR_DIGITAL_SIGNATURE"
 },
 "PublicKeyCertificate": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0t..."
 }
}'`
```

```
`{
 "Key": {
 "KeyArn": "arn:aws:payment-cryptography:us-east-1:111122223333:key/xivpaqy7qbbm7cdw",
 "KeyAttributes": {
 "KeyUsage": "TR31_S0_ASYMMETRIC_KEY_FOR_DIGITAL_SIGNATURE",
 "KeyClass": "PUBLIC_KEY",
 "KeyAlgorithm": "RSA_4096",
 "KeyModesOfUse": {
 "Verify": true
 }
 },
 "Enabled": true,
 "KeyState": "CREATE_COMPLETE",
 "KeyOrigin": "EXTERNAL"
 }
}`
```

Take note of the CA's `KeyArn` for use in the export step.

### Step 6: Get KRD Encryption Certificate

In this example, we're importing back into AWS Payment Cryptography, so we call the service to receive a KRD public key certificate using the [GetParametersForImport](../DataAPIReference/API_GetParametersForImport.md "../DataAPIReference/API_GetParametersForImport.md") API.
In a real scenario, this would be provided by the other system, like an HSM, an ATM, a payment terminal or payment terminal management system.

###### Example Get Parameters for Import

```
`$` `aws payment-cryptography-data get-parameters-for-import \
 --key-material-type "TR34_KEY_BLOCK" \
 --wrapping-key-algorithm RSA_2048`
```

```
`{
 "WrappingKeyCertificate": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0t...",
 "WrappingKeyCertificateChain": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0t...",
 "WrappingKeyAlgorithm": "RSA_2048",
 "ImportToken": "import-token-v2rxpl6drxeptn7w",
 "ParametersValidUntilTimestamp": "2025-11-01T18:45:31.271000-07:00"
}`
```

### Step 7: Export Key with BYOCA

Finally, export the key using TR-34 with your own CA-signed certificate using the [ExportKey](../DataAPIReference/API_ExportKey.md "../DataAPIReference/API_ExportKey.md") API.
Provide the signing certificate that was signed by your external CA.

###### Example TR-34 Export with BYOCA

```
`$` `aws payment-cryptography-data export-key \
 --export-key-identifier arn:aws:payment-cryptography:us-east-1:111122223333:key/iox73p5f4c4yjiod \
 --key-material '{
 "Tr34KeyBlock": {
 "CertificateAuthorityPublicKeyIdentifier": "arn:aws:payment-cryptography:us-east-1:111122223333:key/j625deyfqlwctu57",
 "SigningKeyIdentifier": "arn:aws:payment-cryptography:us-east-1:111122223333:key/xgmq6fs6uow736uc",
 "SigningKeyCertificate": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0t...",
 "KeyBlockFormat": "X9_TR34_2012",
 "WrappingKeyCertificate": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0t..."
 }
 }'`
```

```
`{
 "WrappedKey": {
 "WrappedKeyMaterialFormat": "TR34_KEY_BLOCK",
 "KeyMaterial": "3082055A06092A864886F70D010702A082054B30820547...",
 "KeyCheckValue": "3DCA31",
 "KeyCheckValueAlgorithm": "ANSI_X9_24"
 }
}`
```

The exported key block can now be imported by the receiving system using the standard TR-34 import process.

## Additional Notes

- These examples are shown using the AWS CLI. The same functionality is available in all AWS SDKs including Java, Python, Go, and Rust.
- If you're testing with a self-signed CA, you can use OpenSSL to create a test CA and sign the CSR. In production, use your organization's established CA infrastructure.
