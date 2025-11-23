# Request a public certificate in

AWS Certificate Manager

You can request AWS Certificate Manager public certificates from the ACM console, AWS CLI, or API.
You can use these certificates with integrated AWS services or export them for use
outside of AWS Cloud.

The following list describes the differences between public certificates and
exportable public certificates.

**Public certificates**

Use ACM public certificates with integrated AWS services like ELB,
Amazon CloudFront, and Amazon API Gateway. For more information, see [Services integrated with ACM](acm-services.md "acm-services.md").

###### Note

ACM public certificates created prior to June 17, 2025 cannot be exported.

**Exportable public certificates**

Exportable public certificates work with integrated AWS services and can also be
used outside AWS Cloud. For more information, see [AWS Certificate Manager exportable public certificates](acm-exportable-certificates.md "acm-exportable-certificates.md") and [Services integrated with ACM](acm-services.md "acm-services.md"). You must create a
new ACM public certificate and enable exportable to be able to export the
public certificate.

The following sections discuss how to request, export, and revoke a public ACM
certificate.

###### Topics

- [Request a public certificate using the
  console](#request-public-console "#request-public-console")
- [Request a public certificate using the
  CLI](#request-public-cli "#request-public-cli")

## Request a public certificate using the

console

###### To request an ACM public certificate (console)

1. Sign in to the AWS Management Console and open the ACM console at
   [https://console.aws.amazon.com/acm/home](https://console.aws.amazon.com/acm/home "https://console.aws.amazon.com/acm/home").

Choose **Request a certificate**. 2. In the **Domain names** section, type your domain name.

You can use a fully qualified domain name (FQDN), such as
`www.example.com`, or a bare or apex domain name
such as `example.com`. You can also use an asterisk
(`*`) as a wild card in the leftmost position to
protect several site names in the same domain. For example,
`*.example.com` protects
`corp.example.com`, and
`images.example.com`. The wildcard name will appear
in the **Subject** field and in the **Subject
Alternative Name** extension of the ACM certificate.

When you request a wildcard certificate, the asterisk
(`*`) must be in the leftmost position of the
domain name and can protect only one subdomain level. For example,
`*.example.com` can protect
`login.example.com`, and
`test.example.com`, but it cannot protect
`test.login.example.com`. Also note that
`*.example.com` protects _only_
the subdomains of `example.com`, it does not protect
the bare or apex domain (`example.com`). To protect
both, see the next step.

###### Note

In compliance with [RFC
5280](https://datatracker.ietf.org/doc/html/rfc5280 "https://datatracker.ietf.org/doc/html/rfc5280"), the length of the domain name (technically, the Common
Name) that you enter in this step cannot exceed 64 octets (characters),
including periods. Each subsequent Subject Alternative Name (SAN) that
you provide, as in the next step, can be up to 253 octets in length.

    1. To add another name, choose **Add another name to this
     certificate** and type the name in the text box. This
     is useful for protecting both a bare or apex domain (such as
     `example.com`) and its subdomains such as
     `*.example.com`).

3. If you want to create an ACM exportable public certificates, select the **Enable
   export** option. You'll be able to access the certificate's
   private keys and use it outside AWS Cloud. For more information, see [AWS Certificate Manager exportable public certificates](acm-exportable-certificates.md "acm-exportable-certificates.md").
4. In the **Validation method** section, choose either
   **DNS validation – recommended** or
   **Email validation**, depending on your needs.

###### Note

If you are able to edit your DNS configuration, we recommend that you
use DNS domain validation rather than email validation. DNS validation
has multiple benefits over email validation. See [AWS Certificate Manager DNS validation](dns-validation.md "dns-validation.md").

Before ACM issues a certificate, it validates that you own or control
the domain names in your certificate request. You can use either email
validation or DNS validation.

    1. If you choose email validation, ACM sends validation email to
     the domain that you specify in the domain name field. If you specify
     a validation domain, ACM sends the email to that validation domain
     instead. For more information about email validation, see [AWS Certificate Manager email validation](email-validation.md "email-validation.md").
    2. If you use DNS validation, you simply add a CNAME record provided
     by ACM to your DNS configuration. For more information about DNS
     validation, see [AWS Certificate Manager DNS validation](dns-validation.md "dns-validation.md").

5. In the **Key algorithm** section, choose an
   algorithm.
6. In the **Tags** page, you can optionally tag your
   certificate. Tags are key-value pairs that serve as metadata for identifying
   and organizing AWS resources. For a list of ACM tag parameters and for
   instructions on how to add tags to certificates after creation, see [Tag AWS Certificate Manager resources](tags.md "tags.md").

When you finish adding tags, choose **Request**. 7. After the request is processed, the console returns you to your
certificate list, where information about the new certificate is
displayed.

A certificate enters status **Pending validation** upon
being requested, unless it fails for any of the reasons given in the
troubleshooting topic [Certificate request fails](troubleshooting-cert-requests.md#troubleshooting-failed "troubleshooting-cert-requests.md#troubleshooting-failed"). ACM makes repeated attempts to
validate a certificate for 72 hours and then times out. If a certificate
shows status **Failed** or **Validation timed
out**, delete the request, correct the issue with [DNS validation](dns-validation.md "dns-validation.md") or [Email validation](email-validation.md "email-validation.md"), and
try again. If validation succeeds, the certificate enters status
**Issued**.

###### Note

Depending on how you have ordered the list, a certificate you are
looking for might not be immediately visible. You can click the
black triangle at right to change the ordering. You can also navigate
through multiple pages of certificates using the page numbers at
upper-right.

## Request a public certificate using the

CLI

Use the [request-certificate](../../../cli/latest/reference/acm/request-certificate.md "../../../cli/latest/reference/acm/request-certificate.md") command to request a new public ACM certificate
on the command line. Optional values for the validation method are DNS and EMAIL.
Optional values for the key algorithm are RSA_2048 (the default if the parameter is
not explicitly provided), EC_prime256v1, and EC_secp384r1.

```
aws acm request-certificate \
--domain-name www.example.com \
--key-algorithm EC_Prime256v1 \
--validation-method DNS \
--idempotency-token 1234 \
--options CertificateTransparencyLoggingPreference=DISABLED,Export=ENABLED
```

This command outputs the Amazon Resource Name (ARN) of your new public
certificate.

```
{
    "CertificateArn": "arn:aws:acm:`Region`:`444455556666`:certificate/`certificate_ID`"
}
```
