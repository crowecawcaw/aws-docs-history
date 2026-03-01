# Configure secure access and restrict access to content

CloudFront provides several options for securing content that it delivers. The following are some
ways you can use CloudFront to secure and restrict access to content:

- Configure HTTPS connections
- Prevent users in specific geographic locations from accessing content
- Require users to access content using CloudFront signed URLs or signed cookies
- Set up field-level encryption for specific content fields
- Use AWS WAF to control access to your content
  You should also implement a DDoS-resilient architecture for your infrastructure and applications. For more information, see [AWS Best Practices for DDoS Resiliency](../../../whitepapers/latest/aws-best-practices-ddos-resiliency/aws-best-practices-ddos-resiliency.md "../../../whitepapers/latest/aws-best-practices-ddos-resiliency/aws-best-practices-ddos-resiliency.md").

For additional information, see the following:

- [Securing your content delivery with CloudFront](https://aws.amazon.com/cloudfront/security/ "https://aws.amazon.com/cloudfront/security/")
- [SIEM on Amazon OpenSearch Service](https://github.com/aws-samples/siem-on-amazon-opensearch-service/blob/main/README.md "https://github.com/aws-samples/siem-on-amazon-opensearch-service/blob/main/README.md")

###### Topics

- [Use HTTPS with CloudFront](using-https.md "using-https.md")
- [Use alternate domain names and HTTPS](using-https-alternate-domain-names.md "using-https-alternate-domain-names.md")
- [Mutual TLS authentication with CloudFront (Viewer mTLS)](mtls-authentication.md "mtls-authentication.md")
- [Origin mutual TLS with CloudFront](origin-mtls-authentication.md "origin-mtls-authentication.md")
- [Serve private content with signed URLs and signed cookies](PrivateContent.md "PrivateContent.md")
- [Restrict access to an AWS origin](private-content-restricting-access-to-origin.md "private-content-restricting-access-to-origin.md")
- [Restrict access to Application Load Balancers](restrict-access-to-load-balancer.md "restrict-access-to-load-balancer.md")
- [Restrict the geographic distribution of your content](georestrictions.md "georestrictions.md")
- [Use field-level encryption to help protect sensitive data](field-level-encryption.md "field-level-encryption.md")
