# Retrieve a private certificate

You can use the AWS Private CA API and AWS CLI to issue a private certificate. If you do, you
can use the AWS CLI or AWS Private CA API to retrieve that certificate. If you used ACM to
create your private CA and to request certificates, you must use ACM to export the
certificate and the encrypted private key. For more information, see [Exporting a private certificate](../../../acm/latest/userguide/export-private.md "../../../acm/latest/userguide/export-private.md").

###### To retrieve an end-entity certificate

Use the [get-certificate](../../../cli/latest/reference/acm-pca/get-certificate.md "../../../cli/latest/reference/acm-pca/get-certificate.md") AWS CLI
command to retrieve a private end-entity certificate. You can also use the [GetCertificate](../APIReference/API_GetCertificate.md "../APIReference/API_GetCertificate.md") API operation. We
recommend formatting the output with [jq](https://stedolan.github.io/jq/ "https://stedolan.github.io/jq/"), a sed-like parser.

###### Note

If you want to revoke a certificate, you can use the
**get-certificate** command to retrieve the serial number in
hexadecimal format. You can also create an audit report to retrieve the hex serial
number. For more information, see [Use audit reports with your private CA](PcaAuditReport.md "PcaAuditReport.md").

```
`$` `aws acm-pca get-certificate \
 --certificate-arn arn:aws:acm-pca:`region`:`account`:certificate-authority/`CA_ID`/certificate/`certificate_ID` \
 --certificate-authority-arn arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566` | \
 jq -r '.Certificate, .CertificateChain'`
```

This command outputs the certificate and certificate chain in the following standard
format.

```
-----BEGIN CERTIFICATE-----
`...base64-encoded certificate...`
-----END CERTIFICATE----
-----BEGIN CERTIFICATE-----
`...base64-encoded certificate...`
-----END CERTIFICATE----
-----BEGIN CERTIFICATE-----
`...base64-encoded certificate...`
-----END CERTIFICATE----
```

###### To retrieve a CA certificate

You can use the AWS Private CA API and AWS CLI to retrieve the certificate authority (CA)
certificate for your private CA. Run the [get-certificate-authority-certificate](../../../cli/latest/reference/acm-pca/get-certificate-authority-certificate.md "../../../cli/latest/reference/acm-pca/get-certificate-authority-certificate.md") command. You can also call
the [GetCertificateAuthorityCertificate](../APIReference/API_GetCertificateAuthorityCertificate.md "../APIReference/API_GetCertificateAuthorityCertificate.md") operation. We recommend
formatting the output with [jq](https://stedolan.github.io/jq/ "https://stedolan.github.io/jq/"), a
sed-like parser.

````
`$` `aws acm-pca get-certificate-authority-certificate \
 --certificate-authority-arn arn:`aws`:acm-pca:`us-east-1`:`111122223333`:certificate-authority/`11223344-1234-1122-2233-112233445566` \
| jq -r '.Certificate'` ``` This command outputs the CA certificate in the following standard format. ``` -----BEGIN CERTIFICATE----- `...base64-encoded certificate...` -----END CERTIFICATE---- ```
````
