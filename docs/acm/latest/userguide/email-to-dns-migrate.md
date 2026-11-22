

# Migrating a certificate (console or AWS CLI)
<a name="email-to-dns-console-procedure"></a>

**To migrate a certificate from email to DNS validation (console)**
**Note**  
The exact label of the migration action in the console might vary. Look for the option to switch the validation method to DNS in the **Actions** menu on the certificate details page.

1. Open the ACM console at [https://console.aws.amazon.com/acm/](https://console.aws.amazon.com/acm/).

1. In the list of certificates, choose the **Certificate ID** of an issued, email-validated certificate.

1. Choose **Actions**, and then choose **Migrate to DNS validation**.

1. Review the generated CNAME records for each domain on the certificate.

1. Add each CNAME record to the DNS configuration for its domain. If your domain is hosted in Route 53 and you have permission to write to the zone, you can choose **Create records in Route 53** to add the records automatically.

1. Choose **Migrate** to confirm the request.

1. Monitor the certificate's domain validation status on the certificate details page. Migration completes after ACM verifies all CNAME records.

**Tip**  
To migrate multiple certificates at the same time, select more than one certificate from the certificate list and then choose **Migrate to DNS validation**.<a name="email-to-dns-cli-procedure"></a>

**To migrate a certificate from email to DNS validation (AWS CLI)**

1. Initiate the migration by calling the [update-certificate-options](https://docs.aws.amazon.com/acm/latest/APIReference/API_UpdateCertificateOptions.html) command with the `ValidationMethod` option set to `DNS`. Replace the example ARN with your certificate ARN.

   ```
   aws acm update-certificate-options \
       --certificate-arn arn:aws:acm:us-east-1:111122223333:certificate/12345678-1234-1234-1234-123456789012 \
       --options ValidationMethod=DNS
   ```

1. Retrieve the CNAME records that you must add to your DNS configuration by calling the [list-certificate-domain-validations](https://docs.aws.amazon.com/acm/latest/APIReference/API_ListCertificateDomainValidations.html) command.

   ```
   aws acm list-certificate-domain-validations \
       --certificate-arn arn:aws:acm:us-east-1:111122223333:certificate/12345678-1234-1234-1234-123456789012
   ```

   For each domain, the response includes a `RequestedValidationConfiguration` with a CNAME record under `DnsValidationChallenge.ResourceRecord`.

1. Add each CNAME record to the DNS configuration for its domain.

1. Wait for ACM to verify the CNAME records. Verify the migration progress by calling `list-certificate-domain-validations` again. When migration completes, the `ActiveValidationConfiguration` for each domain shows `ValidationMethod` set to `DNS`.