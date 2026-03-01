# AWS Certificate Manager HTTP validation

Hypertext Transfer Protocol (HTTP) is a foundational protocol for data communication
on the World Wide Web. When you choose HTTP validation for certificates used with CloudFront,
ACM leverages this protocol to verify your domain ownership. ACM works in
conjunction with CloudFront to provide you with a specific URL and a unique token that must be
made accessible at that URL on your domain. This token serves as proof that you control
the domain. By setting up a redirect from your domain to an ACM-controlled location
within the CloudFront infrastructure, you demonstrate your ability to modify content on the
domain, thus validating your ownership. This seamless integration between ACM and CloudFront
simplifies the certificate issuance process, especially for CloudFront distributions.

###### Important

HTTP validation does not support wildcard domain certificates (such as
\*.example.com). For wildcard certificates, you must use either DNS validation or
email validation instead.

For example, if you request a certificate for the `example.com` domain with
`www.example.com` as an additional name using CloudFront, ACM provides you
with two sets of URLs for HTTP validation. Each set contains a `redirectFrom`
URL and a `redirectTo` URL, created specifically for your domain and your
AWS account. The `redirectFrom` URL is a path on your domain (for example,
`http://example.com/.well-known/pki-validation/example.txt`) that you
need to configure. The `redirectTo` URL points to an ACM-controlled
location within the CloudFront infrastructure where a unique validation token is stored. You
need to set up these redirects only once. When a certificate authority attempts to
validate your domain ownership, it will request the file from the
`redirectFrom` URL, which CloudFront redirects to the `redirectTo`
URL, allowing access to the validation token. ACM automatically renews your
certificate as long as the certificate is in use with CloudFront and your redirect remains in
place.

Once you've set up HTTP validation for a fully qualified domain name (FQDN) with CloudFront,
you can request additional ACM certificates for that FQDN without repeating the
validation process, as long as the HTTP redirect remains in place. This means you can
create replacement certificates with the same domain name. You can also replace a
deleted certificate without going through the validation process again, provided the
redirect is still active.

To stop automatic renewal of your HTTP-validated certificate, you have two options.
You can either remove the certificate from the CloudFront distribution with which it is
associated, or you can delete the HTTP redirect you set up for validation. If you're
using a content delivery network (CDN) or web server other than CloudFront to manage your
redirects, consult their documentation to learn how to remove a redirect. If you're
using CloudFront to manage your redirects, you can remove the redirect by updating your
distribution's configuration. For more information about managed certificate renewal,
see [Managed certificate renewal in AWS Certificate Manager](managed-renewal.md "managed-renewal.md"). Remember that
stopping automatic renewal may lead to certificate expiration, which could interrupt
your HTTPS traffic.

## How HTTP redirects for ACM work

###### Note

This section is for customers who are using CloudFront for content delivery and
ACM for SSL/TLS certificate management.

When using HTTP validation with ACM and CloudFront, you need to set up HTTP redirects.
These redirects allow ACM to verify your domain ownership for initial certificate
issuance and ongoing automated renewal. The redirect mechanism works by pointing a
specific URL on your domain to an ACM-controlled location within the CloudFront
infrastructure where a unique validation token is stored.

The following table shows example redirect configurations for domain names. Note
that HTTP validation does not support wildcard domains (such as \*.example.com). Each
configuration's **Redirect From**-**Redirect To** pair serves to authenticate domain name
ownership.

| Example HTTP redirect configurations | Domain name                                                             | Redirect From                                                                              | Redirect To | Comment |
| ------------------------------------ | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ----------- | ------- |
| example.com                          | `http://example.com/.well-known/pki-validation/`x2`.txt`                | `https://validation.`region`.acm-validations.aws/`y2`/.well-known/pki-validation/`x2`.txt` | Unique      |
| www.example.com                      | `http://www.example.com/.well-known/pki-validation/`x3`.txt`            | `https://validation.`region`.acm-validations.aws/`y3`/.well-known/pki-validation/`x3`.txt` | Unique      |
| host.example.com                     | `http://host.example.com/.well-known/pki-validation/`x4`.txt`           | `https://validation.`region`.acm-validations.aws/`y4`/.well-known/pki-validation/`x4`.txt` | Unique      |
| subdomain.example.com                | `http://subdomain.example.com/.well-known/pki-validation/`x5`.txt`      | `https://validation.`region`.acm-validations.aws/`y5`/.well-known/pki-validation/`x5`.txt` | Unique      |
| host.subdomain.example.com           | `http://host.subdomain.example.com/.well-known/pki-validation/`x6`.txt` | `https://validation.`region`.acm-validations.aws/`y6`/.well-known/pki-validation/`x6`.txt` | Unique      |

The `xN` values in the file names and the
`yN` values in the ACM-controlled domains are unique
identifiers generated by ACM. For example,

```
http://example.com/.well-known/pki-validation/`3639ac514e785e898d2646601fa951d5`.txt
```

is representative of a resulting generated **Redirect
From** URL. The associated **Redirect To**
URL might be

```
https://validation.`region`.acm-validations.aws/`98d2646601fa`/.well-known/pki-validation/`3639ac514e785e898d2646601fa951d5`.txt
```

for the same validation record.

###### Note

If your web server or content delivery network does not support setting up
redirects at the specified path, see [Troubleshoot HTTP Validation
Problems](troubleshooting-HTTP-validation.md "troubleshooting-HTTP-validation.md").

When you request a certificate and specify HTTP validation, ACM provides
redirect information in the following format:

| Domain Name | Redirect From                                                                      | Redirect To                                                                                                                      |
| ----------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| example.com | http://example.com/.well-known/pki-validation/a79865eb4cd1a6ab990a45779b4e0b96.txt | https://validation.`region`.acm-validations.aws/`a424c7224e9b`/.well-known/pki-validation/`a79865eb4cd1a6ab990a45779b4e0b96`.txt |

_Domain Name_ is the FQDN associated with the
certificate. _Redirect From_ is the URL on your
domain where ACM will look for the validation file. _Redirect To_ is the ACM-controlled URL where the actual validation
file is hosted.

You need to configure your web server or CloudFront distribution to redirect requests
from the _Redirect From_ URL to the _Redirect To_ URL. The exact method for setting up this
redirect depends on your web server software or CloudFront configuration. Ensure that the
redirect is set up correctly to allow ACM to validate your domain ownership and
issue or renew your certificate.

## Setting up HTTP validation

ACM uses HTTP validation to verify your domain ownership when issuing public
SSL/TLS certificates for use with CloudFront. This section describes how to configure a
public certificate to use HTTP validation.

###### To set up HTTP validation in the console

###### Note

This procedure assumes that you have already requested a certificate
through CloudFront and that you're working in the AWS Region where you created
it. HTTP validation is available only through the CloudFront Distribution Tenants
feature.

1. Open the ACM console at [https://console.aws.amazon.com/acm/](https://console.aws.amazon.com/acm/ "https://console.aws.amazon.com/acm/").
2. In the list of certificates, choose the **Certificate
   ID** of a certificate with status **Pending
   validation** that you want to configure. This opens a details
   page for the certificate.
3. In the **Domains** section, you can see the
   **Redirect From** and **Redirect To**
   values for each domain in your certificate request.
4. For each domain, set up an HTTP redirect from the **Redirect
   From** URL to the **Redirect To** URL. You can
   do this through your CloudFront distribution configuration.
5. Configure your CloudFront distribution to redirect requests from the
   **Redirect From** URL to the **Redirect
   To** URL. The method for setting up this redirect depends on
   your CloudFront configuration.
6. After you set up the redirects, ACM automatically attempts to validate
   your domain ownership. This process can take up to 30 minutes.

If ACM can't validate the domain name within 72 hours from the time it generates
the redirect values for you, ACM changes the certificate status to
**Validation timed out**. The most likely reason for this
result is that you didn't successfully set up the HTTP redirects. To fix this issue,
you must request a new certificate after reviewing the redirect instructions.

###### Important

To avoid validation problems, make sure that the content at the
**Redirect From** location matches the content at the
**Redirect To** location. If you encounter problems, see
[Troubleshooting HTTP validation problems](troubleshooting-HTTP-validation.md "troubleshooting-HTTP-validation.md").

###### Note

Unlike DNS validation, you can't programmatically request that ACM
automatically create your HTTP redirects. You must configure these redirects
through your CloudFront distribution settings.

For more information about how HTTP validation works, see [How HTTP redirects for ACM work](#http-redirects-overview "#http-redirects-overview").
