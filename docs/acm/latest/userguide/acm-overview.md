# What is AWS Certificate Manager?

AWS Certificate Manager (ACM) handles the complexity of creating, storing, and renewing public and
private SSL/TLS X.509 certificates and keys that protect your AWS websites and
applications. You can provide certificates for your [integrated
AWS services](acm-services.md "acm-services.md") either by issuing them directly with ACM or by [importing](import-certificate.md "import-certificate.md") third-party certificates into the ACM
management system. ACM certificates can secure singular domain names, multiple specific
domain names, wildcard domains, or combinations of these. ACM wildcard certificates can
protect an unlimited number of subdomains. You can also [export](export-private.md "export-private.md") ACM certificates signed by AWS Private CA for use anywhere in your internal
PKI.

###### Note

ACM is not intended for use with a stand-alone web server. If you want to set up a
stand-alone secure server on an Amazon EC2 instance, the following tutorial has instructions:
[Configure SSL/TLS on Amazon Linux 2023](../../../AWSEC2/latest/UserGuide/SSL-on-amazon-linux-2023.md "../../../AWSEC2/latest/UserGuide/SSL-on-amazon-linux-2023.md").

###### Topics

- [Supported Regions](#acm-regions "#acm-regions")
- [Pricing for AWS Certificate Manager](#acm-billing "#acm-billing")
- [AWS Certificate Manager concepts](acm-concepts.md "acm-concepts.md")
- [What is the right AWS certificate service for my
  needs?](service-options.md "service-options.md")

## Supported Regions

ACM supports IPv4 and IPv6 on public endpoints. Visit [AWS Regions and Endpoints](../../../general/latest/gr/rande.md#acm_region "../../../general/latest/gr/rande.md#acm_region") in the
_AWS General Reference_ or the [AWS Region Table](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/") to see the regional availability for ACM.

Certificates in ACM are regional resources. To use a certificate with ELB for the
same fully qualified domain name (FQDN) or set of FQDNs in more than one AWS region,
you must request or import a certificate for each region. For certificates provided by
ACM, this means you must revalidate each domain name in the certificate for each
region. You cannot copy a certificate between regions.

To use an ACM certificate with Amazon CloudFront, you must request or import the certificate
in the US East (N. Virginia) region. ACM certificates in this region that are associated
with a CloudFront distribution are distributed to all the geographic locations configured for
that distribution.

## Pricing for AWS Certificate Manager

You are not subject to an additional charge for SSL/TLS certificates that you manage
with AWS Certificate Manager. You pay only for the AWS resources that you create to run your website
or application. For the latest ACM pricing information, see the [AWS Certificate Manager Service Pricing](https://aws.amazon.com/certificate-manager/pricing/ "https://aws.amazon.com/certificate-manager/pricing/")
page on the AWS website.
