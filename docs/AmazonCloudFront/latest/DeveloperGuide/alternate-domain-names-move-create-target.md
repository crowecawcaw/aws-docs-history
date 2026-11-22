

# Set up the target standard distribution or distribution tenant

Before you can move an alternate domain name, you must set up the target resource. This is the target standard distribution or distribution tenant that you're moving the alternate domain name to.

------
#### [ Standard distribution ]

**To set up a target standard distribution**

1. Request a TLS certificate. This certificate includes the alternate domain name as the Subject or Subject Alternative Domain (SAN), or a wildcard (\*) that covers the alternate domain name that you’re moving. If you don’t have one, you can request one from AWS Certificate Manager (ACM) or from another certificate authority (CA) and import it into ACM. 
**Note**  
You must request or import the certificate in the US East (N. Virginia) (`us-east-1`) Region.

   For more information, see [Request a public certificate using the console](https://docs.aws.amazon.com/acm/latest/userguide/acm-public-certificates.html#request-public-console) and [Import a certificate](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate-api-cli.html) in the AWS Certificate Manager in the *AWS Certificate Manager User Guide*.

1. If you haven’t created the target standard distribution, create one now. As part of creating the standard distribution, associate the certificate with this standard distribution. For more information, see [Create a distribution](distribution-web-creating-console.md).

   If you already have a target standard distribution, associate the certificate with the standard distribution. For more information, see [Update a distribution](HowToUpdateDistribution.md).

1. **If you're using **update-domain-association** to move alternate domain names within the same AWS account, skip this step.**

   To move an alternate domain name from one AWS account to another, a DNS record must point the alternate domain name to the target standard distribution. This verification step helps prevent unauthorized domain transfers. CloudFront uses this DNS record to validate your ownership of the alternate domain name. 

   Usually, this is the domain's CNAME record, which points to the CloudFront domain name of the target standard distribution, such as d111111abcdef8.cloudfront.net. You can also create a TXT record instead.

   An apex domain, such as `example.com`, can't have a CNAME record, and an alias record doesn't prove that you control the domain. For an apex domain, create a TXT record.

   The name of the TXT record depends on the type of domain. The value is the CloudFront domain name of the target standard distribution, or the routing endpoint of the target distribution tenant's connection group, such as d111111abcdef8.cloudfront.net.


<table>
<thead>
  <tr><th>Domain type</th><th>Domain</th><th>TXT record</th></tr>
</thead>
<tbody>
  <tr><td>Subdomain</td><td><code>www.example.com</code></td><td><code>_www.example.com TXT d111111abcdef8.cloudfront.net</code></td></tr>
  <tr><td>Apex (root) domain</td><td><code>example.com</code></td><td><code>_.example.com TXT d111111abcdef8.cloudfront.net</code></td></tr>
  <tr><td>Wildcard domain</td><td><code>*.example.com</code></td><td><code>_*.example.com TXT d111111abcdef8.cloudfront.net</code></td></tr>
</tbody>
</table>


------
#### [ Distribution tenant ]

**To set up the target distribution tenant**

1. Request a TLS certificate. This certificate includes the alternate domain name as the Subject or Subject Alternative Domain (SAN), or a wildcard (\*) that covers the alternate domain name that you’re moving. If you don’t have one, you can request one from AWS Certificate Manager (ACM) or from another certificate authority (CA) and import it into ACM. 
**Note**  
You must request or import the certificate in the US East (N. Virginia) (`us-east-1`) Region.

   For more information, see [Request a public certificate using the console](https://docs.aws.amazon.com/acm/latest/userguide/acm-public-certificates.html#request-public-console) and [Import a certificate](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate-api-cli.html) in the AWS Certificate Manager in the *AWS Certificate Manager User Guide*.

1. If you haven’t created the target distribution tenant, create one now. As part of creating the distribution tenant, associate the certificate with the distribution tenant. For more information, see [Create a distribution](distribution-web-creating-console.md).

   If you already have a target distribution tenant, associate the certificate with the distribution tenant. For more information, see [Add a domain and certificate (distribution tenant)](managed-cloudfront-certificates.md#vanity-domain-tls-tenant).

1. **If you're using **update-domain-association** to move alternate domain names within the same AWS account, skip this step.** If you're setting `OnDomainTakeover` to `allow`, you need a DNS record that points the domain to the target distribution tenant even within the same AWS account. For more information, see [Move domains when you create or update a distribution tenant](alternate-domain-names-move-options.md#alternate-domain-names-move-takeover).

   To move an alternate domain name from one AWS account to another, a DNS record must point the alternate domain name to the target distribution tenant. This verification step helps prevent unauthorized domain transfers, and CloudFront uses this DNS record to validate your ownership of the alternate domain name. 

   Usually, this is the domain's CNAME record, which points to the routing endpoint of the target distribution tenant's connection group. You can also create a TXT record instead.

   An apex domain, such as `example.com`, can't have a CNAME record, and an alias record that resolves the domain to the shared CloudFront IP addresses doesn't prove that you control the domain. For an apex domain, create a TXT record, or an A record that resolves the domain to the Anycast static IP addresses of the target distribution tenant's connection group.

   The name of the TXT record depends on the type of domain. The value is the CloudFront domain name of the target standard distribution, or the routing endpoint of the target distribution tenant's connection group, such as d111111abcdef8.cloudfront.net.


<table>
<thead>
  <tr><th>Domain type</th><th>Domain</th><th>TXT record</th></tr>
</thead>
<tbody>
  <tr><td>Subdomain</td><td><code>www.example.com</code></td><td><code>_www.example.com TXT d111111abcdef8.cloudfront.net</code></td></tr>
  <tr><td>Apex (root) domain</td><td><code>example.com</code></td><td><code>_.example.com TXT d111111abcdef8.cloudfront.net</code></td></tr>
  <tr><td>Wildcard domain</td><td><code>*.example.com</code></td><td><code>_*.example.com TXT d111111abcdef8.cloudfront.net</code></td></tr>
</tbody>
</table>


------

Next, see the following topic to find the source standard distribution or distribution tenant that is already associated with the alternate domain name.