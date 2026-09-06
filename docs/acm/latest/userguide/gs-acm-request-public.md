

# AWS Certificate Manager public certificates
<a name="gs-acm-request-public"></a>

After you request a public certificate you must validate domain ownership, as described in [Validate domain ownership for AWS Certificate Manager public certificates](domain-ownership-validation.md).

Public ACM certificates follow the X.509 standard and are subject to the following restrictions: 
+ **Names:** You must use DNS-compliant subject names. For more information, see [Domain Names](acm-concepts.md#concept-dn).
+ **Algorithm:** For encryption, the certificate private key algorithm must be either 2048-bit RSA, 256-bit ECDSA, or 384-bit ECDSA.
+ **Expiration:** Each certificate is valid for 198 days.
+ **Renewal:** ACM attempts to renew a public certificate automatically 45 days before expiration. 

**Note**  
To automate public certificate issuance and renewal outside integrated services such as on Amazon EC2 instances, use the ACME protocol. For more information, see [ACME certificate automation](acm-acme.md). Alternatively, if you cannot use ACME, you can automate exportable certificates issued from ACM through [AWS Workload Credentials Provider](acm-certificate-automation.md).

Administrators can use ACM [Conditional Key Policies](https://docs.aws.amazon.com/acm/latest/userguide/acm-conditions.html) to control how end users issue new certificates. These Conditional keys allow restrictions to be placed on domains, validation methods, and other attributes related to a certificate request. If you encounter problems when requesting a certificate, see [Troubleshoot certificate requests](troubleshooting-cert-requests.md).

To request a certificate for a private PKI using AWS Private CA, see [Request a private certificate in AWS Certificate Manager](gs-acm-request-private.md). 

**Topics**
+ [AWS Certificate Manager public certificate characteristics and limitations](acm-certificate-characteristics.md)
+ [Request a public certificate in AWS Certificate Manager](acm-public-certificates.md)
+ [AWS Certificate Manager exportable public certificates](acm-exportable-certificates.md)
+ [Validate domain ownership for AWS Certificate Manager public certificates](domain-ownership-validation.md)