

# Request an Amazon N2 certificate

You can request an Amazon N2 certificate with the [AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/) (AWS CLI) or the ACM API.

**To request an Amazon N2 certificate (AWS CLI)**

1. Request the certificate. The following command requests an Amazon N2 certificate that chains to the Amazon N2 roots and can authenticate both a client and a server. Replace {{service.example.com}} with your domain name.

   ```bash
   aws acm request-certificate \
       --domain-name {{service.example.com}} \
       --validation-method DNS \
       --key-algorithm EC_prime256v1 \
       --root-hierarchy-type N2_AMAZON_MANAGED \
       --certificate-usage CLIENT_AND_SERVER_AUTH
   ```

   The command uses the following parameters:
   + `--validation-method DNS`: required. Amazon N2 certificates support DNS validation only.
   + `--key-algorithm`: `RSA_2048`, `EC_prime256v1`, or `EC_secp384r1`. For more information, see [Key algorithms](acm-amazon-n2-characteristics.md#amazon-n2-algorithms).
   + `--root-hierarchy-type`: `N2_AMAZON_MANAGED` chains to the Amazon N2 roots. `N2_SFG2_AMAZON_MANAGED` chains to the Starfield Services Root Certificate Authority - G2 (SFG2). To choose, see [Compare the Amazon N2 certificates root hierarchies](acm-amazon-n2-certificates.md#acm-amazon-n2-hierarchy-comparison).
   + `--certificate-usage`: optional. `CLIENT_AND_SERVER_AUTH` is the default. To issue a certificate that authenticates only a client, specify `CLIENT_AUTH_ONLY`, which is available only with `N2_AMAZON_MANAGED`.

   Amazon N2 certificates are exportable by default. To prevent export, for example when you use the certificate only with AWS integrated services, add `--options Export=DISABLED`.

   The command returns the ARN of the new certificate.

   ```json
   {
       "CertificateArn": "arn:aws:acm:us-east-1:111122223333:certificate/12345678-1234-1234-1234-123456789012"
   }
   ```

1. Validate your domain. The following command returns the CNAME record that ACM created for validation. Replace the ARN with the ARN from the previous step.

   ```bash
   aws acm describe-certificate \
       --certificate-arn {{arn:aws:acm:us-east-1:111122223333:certificate/12345678-1234-1234-1234-123456789012}} \
       --query "Certificate.DomainValidationOptions[].ResourceRecord"
   ```

   Create the CNAME record with your DNS provider. For more information, see [AWS Certificate Manager DNS validation](dns-validation.md).

1. Confirm issuance. Run the following command to check the status of the certificate.

   ```bash
   aws acm describe-certificate \
       --certificate-arn {{arn:aws:acm:us-east-1:111122223333:certificate/12345678-1234-1234-1234-123456789012}} \
       --query "Certificate.[Status,RootHierarchyType,CertificateUsage]"
   ```

   When the status is `ISSUED`, the certificate is ready to use.

1. Use the certificate in either of these ways:
   + **With an AWS integrated service.** Specify the certificate ARN when you configure the resource. You do not need to export the certificate. The certificate pickers in some service consoles might not list Amazon N2 certificates, so enter the ARN directly. For more information, see [AWS integrated services](acm-amazon-n2-characteristics.md#amazon-n2-integrated).
   + **On your own clients or servers.** Export the certificate, and then install it. To export the certificate, run the following command. The response contains the certificate, the certificate chain, and the private key, encrypted with your passphrase.

     ```bash
     aws acm export-certificate \
         --certificate-arn {{arn:aws:acm:us-east-1:111122223333:certificate/12345678-1234-1234-1234-123456789012}} \
         --passphrase fileb://{{passphrase.txt}}
     ```

   In both cases, make sure that each verifying peer includes the root that the certificate chains to. For more information, see [Amazon N2 roots and trust](acm-amazon-n2-certificates.md#acm-amazon-n2-trust).