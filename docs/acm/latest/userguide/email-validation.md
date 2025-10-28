# AWS Certificate Manager email validation

Before the Amazon certificate authority (CA) can issue a certificate for your site,
AWS Certificate Manager (ACM) must verify that you own or control all of the domains that you
specified in your request. You can perform verification using either email or DNS. This
topic discusses email validation.

If you encounter problems using email validation, see [Troubleshoot email validation
problems](troubleshooting-email-validation.md "troubleshooting-email-validation.md").

## How email validation works

ACM sends validation email messages to the following five common system emails
for each domain. Alternatively, you can specify a superdomain as a validation domain
if you wish to receive these emails at that domain instead. Any subdomain up to the
minimal website address is valid, and is used as the domain for the email address as
the suffix after `@`. For example, you can receive an email to
admin@example.com if you specify example.com as the validation domain for
subdomain.example.com.

- administrator@your_domain_name
- hostmaster@your_domain_name
- postmaster@your_domain_name
- webmaster@your_domain_name
- admin@your_domain_name

To prove that you own the domain, you must select the validation link included in
these emails. ACM also sends validation emails to these same addresses to renew
the certificate when the certificate is 45 days from expiry.

Email validation for multi-domain certificate requests using the ACM API or CLI
results in an email message being sent by each requested domain, even if the request
includes subdomains of other domains in the request. The domain owner needs to
validate an email message for each of these domains before ACM can issue the
certificate.

###### Exception to this process

If you request an ACM certificate for a domain name that begins with
`www` or a wildcard asterisk
(`*`), ACM removes the leading `www`
or asterisk and sends email to the administrative addresses. These addresses are
formed by pre-pending admin@, administrator@, hostmaster@, postmaster@, and
webmaster@ to the remaining portion of the domain name. For example, if you
request an ACM certificate for www.example.com, email is sent to
admin@example.com rather than to admin@www.example.com. Likewise, if you request
an ACM certificate for \*.test.example.com, email is sent to
admin@test.example.com. The remaining common administrative addresses are
similarly formed.

###### Important

ACM no longer supports WHOIS email validation for new certificates or
renewals. Common system addresses remain supported. For details, see [blog post](https://aws.amazon.com/blogs/security/aws-certificate-manager-will-discontinue-whois-lookup-for-email-validated-certificates/ "https://aws.amazon.com/blogs/security/aws-certificate-manager-will-discontinue-whois-lookup-for-email-validated-certificates/").

## Considerations

Observe the following considerations about email validation.

- You need a working email address registered in your domain in order to use
  email validation. Procedures for setting up an email address are outside the
  scope of this guide.
- Validation applies only to publicly trusted certificates issued by ACM. ACM does not
  validate domain ownership for [imported
  certificates](import-certificate.md "import-certificate.md") or for certificates signed by a private CA. ACM
  cannot validate resources in an Amazon VPC
  [private hosted
  zone](../../../vpc/latest/userguide/vpc-dns.md#vpc-private-hosted-zones "../../../vpc/latest/userguide/vpc-dns.md#vpc-private-hosted-zones") or any other private domain. For more information, see
  [Troubleshoot certificate validation](certificate-validation.md "certificate-validation.md").
- After you create a certificate with email validation, you cannot switch to validating it with DNS. To use DNS validation, delete the certificate and then create a new one that uses DNS validation.

## Certificate expiration and renewal

ACM certificates are valid for 13 months (395 days). Renewing a certificate requires action by the domain owner. ACM begins sending renewal notices to the email addresses associated with the domain 45 days before expiration. The notifications contain a link that the
domain owner can click for renewal. Once all listed domains are validated,
ACM issues a renewed certificate with the same ARN.

## (Optional) Resend validation email

Each validation email contains a token that you can use to approve a certificate
request. However, because the validation email required for the approval process can
be blocked by spam filters or lost in transit, the token automatically expires after
72 hours. If you do not receive the original email or the token has expired, you can
request that the email be resent. For information about how to resend a validation
email, see [Resend validation
email](email-renewal-validation.md#request-domain-validation-email-for-renewal "email-renewal-validation.md#request-domain-validation-email-for-renewal")

For persistent problems with email validation, see the [Troubleshoot email validation
problems](troubleshooting-email-validation.md "troubleshooting-email-validation.md") section in [Troubleshoot issues with AWS Certificate Manager](troubleshooting.md "troubleshooting.md").
