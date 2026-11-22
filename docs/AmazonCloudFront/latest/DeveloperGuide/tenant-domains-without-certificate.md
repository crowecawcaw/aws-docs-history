

# Serve distribution tenant domains without a certificate

You can add a domain to a distribution tenant even when no certificate covers it. Instead of a certificate, CloudFront uses the domain's DNS records to verify that you control the domain. CloudFront then serves the domain over HTTP. You can use this to do the following:
+ Start serving HTTP traffic for a domain as soon as its DNS records point to CloudFront.
+ Get a certificate for the domain from a third-party certificate authority (CA) that validates domains over HTTP, and then add that certificate to the distribution tenant. For more information, see [Use a certificate from a third-party CA](#tenant-third-party-ca-certificate).

**Topics**
+ [How it works](#tenant-domains-without-certificate-how-it-works)
+ [Use a certificate from a third-party CA](#tenant-third-party-ca-certificate)

## How it works
<a name="tenant-domains-without-certificate-how-it-works"></a>

When you create or update a distribution tenant, CloudFront checks each domain that you add. If no certificate on the distribution tenant or its multi-tenant distribution covers a domain, CloudFront checks that the domain's DNS configuration points to the distribution tenant. Usually, this is the domain's CNAME record. CloudFront accepts any of the following records:
+ A CNAME record that points the domain to the routing endpoint of the distribution tenant's connection group.
+ An A record that resolves the domain to the Anycast static IP addresses of the distribution tenant's connection group.
+ A TXT record that associates the domain with the routing endpoint of the distribution tenant's connection group.

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


An apex domain, such as `example.com`, can't have a CNAME record, and an alias record that resolves the domain to the shared CloudFront IP addresses doesn't pass this check. If you point an apex domain to CloudFront with an alias record, also create a TXT record. The alias record routes viewers to the distribution tenant, and the TXT record passes the check. If the connection group uses Anycast static IPs, an A record that resolves the domain to those addresses does both, so you don't need the TXT record.

If the DNS check fails for a domain, the request fails with `InvalidArgument`. If you get this error when you add a domain that no certificate covers, check the domain's DNS records. A distribution tenant doesn't need any certificate if every domain passes this check.

Until a certificate covers the domain, CloudFront serves the domain over HTTP only, and HTTPS requests for the domain fail. After you add a certificate that covers the domain, CloudFront serves it over HTTPS too.

**Important**  
Viewers can reach the domain over HTTP only if the cache behaviors of the multi-tenant distribution allow HTTP. If [Viewer protocol policy](DownloadDistValuesCacheBehavior.md#DownloadDistValuesViewerProtocolPolicy) is **Redirect HTTP to HTTPS**, CloudFront redirects viewers to HTTPS, which fails until a certificate covers the domain. If it's **HTTPS only**, HTTP requests for the domain fail.

The same rules apply to domains that you set to `anycast-ip-list-only` and to domains that you move to the distribution tenant with `OnDomainTakeover`. For more information, see [Serve domains on specific IP addresses with address-based selection](address-based-selection.md) and [Move domains when you create or update a distribution tenant](alternate-domain-names-move-options.md#alternate-domain-names-move-takeover).

## Use a certificate from a third-party CA
<a name="tenant-third-party-ca-certificate"></a>

Some certificate authorities validate a domain by requesting a file from it over HTTP, for example at `/.well-known/acme-challenge/` or `/.well-known/pki-validation/`. Because CloudFront serves the domain over HTTP before you have a certificate, the CA's validation request reaches your origin through CloudFront. After the CA issues the certificate, you import it into ACM and add it to the distribution tenant.

**To use a certificate from a third-party CA**

1. In your DNS configuration, point the domain to the distribution tenant's connection group, so that the CA's validation request reaches CloudFront. For more information, see [Point domains to CloudFront](managed-cloudfront-certificates.md#point-domains-to-cloudfront).

   If you point an apex domain to CloudFront with an alias record, also create a TXT record, as described in [How it works](#tenant-domains-without-certificate-how-it-works).

1. Add the domain to the distribution tenant. You don't need a certificate for it. Replace the ID, the ETag, and the domains with your own, and include every domain on the distribution tenant.

   ```bash
   aws cloudfront update-distribution-tenant \
       --id {{dt_EXAMPLE22222}} \
       --if-match {{E3QWRUHEXAMPLE}} \
       --domains '[{"Domain": "{{www.example.com}}"}]'
   ```

1. Make sure that the multi-tenant distribution can serve the CA's validation request:
   + A cache behavior that matches the validation path allows HTTP and forwards the request to an origin that serves the validation file.
   + CloudFront doesn't serve an old copy of the validation file from its cache.

   For example, add a cache behavior like the following to the multi-tenant distribution. It allows HTTP, turns off caching, and forwards the `Host` header, so that your origin can return the right validation file for each domain. This example shows only the relevant settings.

   ```json
   {
       "PathPattern": "/.well-known/acme-challenge/*",
       "TargetOriginId": "{{my-origin}}",
       "ViewerProtocolPolicy": "allow-all",
       "CachePolicyId": "4135ea2d-6df8-44a3-9df3-4b5a84be39ad",
       "OriginRequestPolicyId": "216adef6-5c7f-47e4-b989-5492eafa07d3"
   }
   ```

   These IDs are the managed [CachingDisabled](using-managed-cache-policies.md#managed-cache-policy-caching-disabled) cache policy and the managed [AllViewer](using-managed-origin-request-policies.md#managed-origin-request-policy-all-viewer) origin request policy.

1. Request the certificate from your CA with HTTP validation, and put the validation file on your origin as the CA instructs.

1. After the CA issues the certificate, import it into ACM in the US East (N. Virginia) (`us-east-1`) Region. For more information, see [Import certificates into ACM](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the *AWS Certificate Manager User Guide*.

1. Update the distribution tenant to use the certificate. Replace the ETag and the certificate ARN with your own.

   ```bash
   aws cloudfront update-distribution-tenant \
       --id {{dt_EXAMPLE22222}} \
       --if-match {{E4QWRUHEXAMPLE}} \
       --domains '[{"Domain": "{{www.example.com}}"}]' \
       --customizations '{"Certificate": {"Arn": "arn:aws:acm:us-east-1:{{123456789012}}:certificate/{{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}"}}'
   ```

   After the distribution tenant is deployed, CloudFront serves the domain over HTTPS.

**Note**  
ACM doesn't renew certificates that you import. Before the certificate expires, get a new certificate from your CA the same way, and reimport it to the same certificate ARN. Because the ARN doesn't change, you don't need to update the distribution tenant.