Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Requesting a certificate for a

domain name

Amazon Redshift or Amazon Redshift Serverless require a validated Secure Sockets Layer (SSL) certificate
for a custom endpoint to keep communication secure and to verify ownership of the domain
name. You can use the your AWS Certificate Manager account with an
AWS KMS key for secure certificate management. Security validation includes
full host-name verification (_sslmode=verify-full_).

Certificate renewals are managed by Amazon Redshift only when you choose DNS validation, rather
than email validation. If you use email validation, you can use the certificate, but you
must perform renewal yourself, prior to its expiration. We recommend that you choose DNS
validation for your certificate. You can monitor expiration dates of imported
certificates in AWS Certificate Manager.

###### Request a certificate from ACM for a domain name

1. Sign in to the AWS Management Console and open the ACM console at [https://console.aws.amazon.com/acm/](https://console.aws.amazon.com/acm/ "https://console.aws.amazon.com/acm/").
2. Choose **Request a certificate**.
3. Enter your custom domain name in the **Domain name**
   field.

###### Note

You can specify many prefixes, in addition to the certificate domain, in
order to use a single certificate for multiple custom-domain records. To
illustrate, you can use additional records like
`one.example.com`, `two.example.com`, or a wildcard
DNS record like `*.example.com` with the same certificate. 4. Choose **Review and request**. 5. Choose **Confirm and request**. 6. For a valid request, a registered owner of the internet domain must consent to
the request before ACM issues the certificate. Make sure the status appears as
**Issued** in the ACM console, when you're finished with
the steps.
