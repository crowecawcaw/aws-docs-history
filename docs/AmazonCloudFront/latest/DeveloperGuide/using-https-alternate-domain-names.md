# Use alternate domain names and HTTPS

If you want to use your own domain name in the URLs for your files (for example,
`https://www.example.com/image.jpg`) and you want your viewers to use HTTPS,
you must complete the steps in the following topics. (If you use the default CloudFront distribution
domain name in your URLs, for example,
`https://d111111abcdef8.cloudfront.net/image.jpg`, follow the guidance in the
following topic instead: [Require HTTPS for communication between viewers and CloudFront](using-https-viewers-to-cloudfront.md "using-https-viewers-to-cloudfront.md").)

###### Important

When you add a certificate to your distribution, CloudFront immediately propagates the
certificate to all of its edge locations. As new edge locations become available,
CloudFront propagates the certificate to those locations, too. You can't restrict the edge
locations that CloudFront propagates the certificates to.

###### Topics

- [Choose how CloudFront serves HTTPS requests](cnames-https-dedicated-ip-or-sni.md "cnames-https-dedicated-ip-or-sni.md")
- [Requirements for using SSL/TLS certificates with CloudFront](cnames-and-https-requirements.md "cnames-and-https-requirements.md")
- [Quotas on using SSL/TLS certificates with CloudFront (HTTPS between viewers and CloudFront only)](cnames-and-https-limits.md "cnames-and-https-limits.md")
- [Configure alternate domain names and HTTPS](cnames-and-https-procedures.md "cnames-and-https-procedures.md")
- [Determine the size of the public key in an SSL/TLS RSA certificate](cnames-and-https-size-of-public-key.md "cnames-and-https-size-of-public-key.md")
- [Increase the quotas for SSL/TLS certificates](increasing-the-limit-for-ssl-tls-certificates.md "increasing-the-limit-for-ssl-tls-certificates.md")
- [Rotate SSL/TLS certificates](cnames-and-https-rotate-certificates.md "cnames-and-https-rotate-certificates.md")
- [Revert from a custom SSL/TLS certificate to the default CloudFront certificate](cnames-and-https-revert-to-cf-certificate.md "cnames-and-https-revert-to-cf-certificate.md")
- [Switch from a custom SSL/TLS certificate with dedicated IP addresses to SNI](cnames-and-https-switch-dedicated-to-sni.md "cnames-and-https-switch-dedicated-to-sni.md")
