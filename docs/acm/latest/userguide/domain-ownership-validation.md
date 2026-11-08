

# Validate domain ownership for AWS Certificate Manager public certificates
<a name="domain-ownership-validation"></a>

Before the Amazon certificate authority (CA) can issue a certificate for your site, AWS Certificate Manager (ACM) must prove that you own or control all of the domain names that you specify in your request. You can choose to prove your ownership with Domain Name System (DNS) validation, email validation, or HTTP validation when you request a certificate.

**Note**  
Validation applies only to publicly trusted certificates issued by ACM. ACM does not validate domain ownership for [imported certificates](import-certificate.md) or for certificates signed by a private CA. ACM cannot validate resources in an Amazon VPC [private hosted zone](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-private-hosted-zones) or any other private domain. For more information, see [Troubleshoot certificate validation](certificate-validation.md).

**Note**  
If you use ACME certificate automation, domain validation is handled differently. ACME domain validations are persistent resources configured by PKI administrators that pre-authorize domains for certificate issuance. ACME clients do not perform live validation challenges. For more information, see [ACME domain validation](acm-acme-domain-validation.md).

We recommend using DNS validation over email validation for the following reasons:
+ AWS Certificate Manager will deprecate email validation throughout 2027 for new public certificates and renewals. For more information, see [AWS Certificate Manager will discontinue email validation to prove domain validation for certificates](https://aws.amazon.com/blogs/security/aws-certificate-manager-will-discontinue-email-validation-to-prove-domain-validation-for-certificates/) on the AWS Security Blog.
+ If you use Amazon Route 53 to manage your public DNS records, you can update your records through ACM directly.
+ ACM automatically renews DNS-validated certificates for as long as a certificate remains in use and the DNS record is in place.
+ Email-validated certificates require an action by the domain owner to be renewed. ACM begins sending renewal notices 45 days before expiration. These notices go to one or more of the domain's five common administrator addresses. The notifications contain a link that the domain owner can click for easy renewal. Once all listed domains are validated, ACM issues a renewed certificate with the same ARN.

HTTP validation is available for certificates used with CloudFront. This method uses HTTP redirects to prove domain ownership and offers automatic renewal similar to DNS validation.

**Note**  
To switch an existing certificate from email validation to DNS validation, use the [`UpdateCertificateOptions`](https://docs.aws.amazon.com/acm/latest/APIReference/API_UpdateCertificateOptions.html) API.

**Topics**
+ [AWS Certificate Manager DNS validation](dns-validation.md)
+ [AWS Certificate Manager email validation](email-validation.md)
+ [AWS Certificate Manager HTTP validation](http-validation.md)