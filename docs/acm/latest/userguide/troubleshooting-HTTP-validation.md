# Troubleshooting HTTP validation problems

Consult the following guidance if you're having trouble validating a certificate with
HTTP.

The first step in HTTP troubleshooting is to check the current status of your domain
with tools such as the following:

- **curl** — [Linux and Windows](https://curl.se/docs/manpage.html "https://curl.se/docs/manpage.html")
- **wget** — [Linux and
  Windows](https://www.gnu.org/software/wget/manual/wget.html "https://www.gnu.org/software/wget/manual/wget.html")

###### Topics

- [Content mismatch between RedirectFrom and RedirectTo locations](#http-validation-content-mismatch "#http-validation-content-mismatch")
- [Incorrect CloudFront configuration](#http-validation-cloudfront-configuration "#http-validation-cloudfront-configuration")
- [HTTP redirect issues](http-validation-redirect-issues.md "http-validation-redirect-issues.md")
- [Validation timeout](http-validation-timeout.md "http-validation-timeout.md")

## Content mismatch between RedirectFrom and RedirectTo locations

If the content at the `RedirectFrom` location doesn't match the content at
the `RedirectTo` location, validation will fail. Ensure that the content is
identical for each domain in the certificate.

## Incorrect CloudFront configuration

Make sure your CloudFront distribution is correctly configured to serve the validation
content. Check that the origin and behavior settings are correct and that the distribution
is deployed.
