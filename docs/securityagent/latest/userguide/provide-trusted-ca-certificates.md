

# Provide trusted CA certificates for a penetration test
<a name="provide-trusted-ca-certificates"></a>

If a target endpoint uses a Transport Layer Security (TLS) certificate that is not publicly trusted, provide the trust anchor. This applies when the certificate is issued by a private or internal certificate authority (CA), an intermediate CA, or a self-signed certificate. AWS Security Agent uses the trust anchor to validate the connection during testing. Without the trust anchor, endpoint validation rejects the target before testing begins.

Trusted CA certificates apply to the entire penetration test. You can provide them in the AWS Security Agent web application or with the AWS CLI or API.

**Note**  
Skip this task if your target endpoints use certificates issued by a publicly trusted CA. For a private endpoint hosted in a VPC, provide the trust anchor in addition to the VPC configuration. For more information, see [Connect agent to private VPC resources](connect-agent-vpc.md).

**Important**  
Provide the certificate only, never a private key. AWS Security Agent does not accept a certificate that is expired or not yet valid.

## Provide a trusted CA certificate in the console
<a name="_provide_a_trusted_ca_certificate_in_the_console"></a>

Trusted CA certificates are part of **Advanced network access** in the penetration test create and edit forms.

1. In the penetration test form, expand **Advanced network access**, and then expand **Trusted CA certificates - optional**.

1. Choose **Add certificate**.

1. For **Source**, choose one of the following:
   +  **Paste PEM** - Paste a PEM-encoded X.509 certificate. An inline certificate is limited to 8,192 characters.
   +  **Upload a file** - Upload a `.pem`, `.crt`, or `.cer` certificate file.
   +  **S3 URI** - Enter the Amazon S3 URI of a certificate that you staged, in the form `s3://amzn-s3-demo-bucket/ca.pem`. AWS Security Agent reads the certificate from Amazon S3 when the penetration test runs, using the penetration test service role. Enter the `s3://` URI form. An Amazon S3 HTTPS URL is not accepted.

1. Review the parsed certificate details (subject, issuer, type, and validity), and then choose **Save**.

To add more than one trust anchor, choose **Add certificate** again. To change or remove a certificate later, choose the actions menu on its row, and then choose **Edit** or **Remove**. Trusted CA certificates that you save are retained when you edit the penetration test.

## Provide a trusted CA certificate with the AWS CLI or API
<a name="_provide_a_trusted_ca_certificate_with_the_aws_cli_or_api"></a>

Set `trustedCaCertificates` in the `assets` parameter of your `create-pentest` or `update-pentest` request. Each entry has exactly one `source`: an inline PEM-encoded certificate (`inlinePem`) or an Amazon S3 location (`s3Location`).

The following example attaches an inline certificate:

```
aws securityagent create-pentest \
  --title "My penetration test" \
  --agent-space-id "your-agent-space-id" \
  --assets '{"trustedCaCertificates": [{"source": {"inlinePem": "-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----"}}]}'
```

The following example reads the certificate from Amazon S3 when the penetration test runs. AWS Security Agent reads the object using the penetration test service role, so the role must have `s3:GetObject` permission for the object.

```
aws securityagent create-pentest \
  --title "My penetration test" \
  --agent-space-id "your-agent-space-id" \
  --assets '{"trustedCaCertificates": [{"source": {"s3Location": "s3://amzn-s3-demo-bucket/ca.pem"}}]}'
```

To update the trust anchors on an existing penetration test, send the complete list in `trustedCaCertificates` on an `update-pentest` request. The list replaces the previously saved anchors, and an empty list removes them all.