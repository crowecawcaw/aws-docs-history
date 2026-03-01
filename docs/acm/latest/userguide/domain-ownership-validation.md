# Validate domain ownership for AWS Certificate Manager public certificates

Before the Amazon certificate authority (CA) can issue a certificate for your site,
AWS Certificate Manager (ACM) must prove that you own or control all of the domain names that you
specify in your request. You can choose to prove your ownership with Domain Name System
(DNS) validation, email validation, or HTTP validation when you request a
certificate.

###### Note

Validation applies only to publicly trusted certificates issued by ACM. ACM does not
validate domain ownership for [imported
certificates](import-certificate.md "import-certificate.md") or for certificates signed by a private CA. ACM
cannot validate resources in an Amazon VPC
[private hosted
zone](../../../vpc/latest/userguide/vpc-dns.md#vpc-private-hosted-zones "../../../vpc/latest/userguide/vpc-dns.md#vpc-private-hosted-zones") or any other private domain. For more information, see
[Troubleshoot certificate validation](certificate-validation.md "certificate-validation.md").

We recommend using DNS validation over email validation for the following reasons:

- If you use Amazon Route 53 to manage your public DNS records, you can update your
  records through ACM directly.
- ACM automatically renews DNS-validated certificates for as long as a certificate
  remains in use and the DNS record is in place.
- Email-validated certificates require an action by the domain owner to be renewed.
  ACM begins sending renewal notices 45 days before expiration. These notices go to
  one or more of the domain's five common administrator addresses. The notifications
  contain a link that the domain owner can click for easy renewal. Once all listed
  domains are validated, ACM issues a renewed certificate with the same ARN.
  If you can't edit your domain's DNS database, you must use [email validation](email-validation.md "email-validation.md") instead.

HTTP validation is available for certificates used with CloudFront. This method uses HTTP
redirects to prove domain ownership and offers automatic renewal similar to DNS
validation.

###### Note

After you create a certificate with email validation, you cannot switch to validating it with DNS. To use DNS validation, delete the certificate and then create a new one that uses DNS validation.

###### Topics

- [AWS Certificate Manager DNS validation](dns-validation.md "dns-validation.md")
- [AWS Certificate Manager email validation](email-validation.md "email-validation.md")
- [AWS Certificate Manager HTTP validation](http-validation.md "http-validation.md")
