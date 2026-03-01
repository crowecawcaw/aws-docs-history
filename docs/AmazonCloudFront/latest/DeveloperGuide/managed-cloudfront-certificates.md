# Request certificates for your CloudFront distribution tenant

When you create a distribution tenant, the tenant inherits the shared AWS Certificate Manager (ACM) certificate
from the multi-tenant distribution. This shared certificate provides HTTPS for all tenants associated with
the multi-tenant distribution.

When you create or update a CloudFront distribution tenant to add domains, you can add a managed CloudFront
certificate from ACM. CloudFront then gets an HTTP-validated certificate from ACM on your
behalf. You can use this tenant-level ACM certificate for custom domain configurations.
CloudFront streamlines the renewal workflow to help keep certificates up-to-date and secure
content delivery uninterrupted.

###### Note

You own the certificate, but it can _only_ be used with CloudFront
resources and the private key _cannot_ be exported.

You can request the certificate when you create or update the distribution tenant.

###### Topics

- [Add a domain and certificate (distribution tenant)](#vanity-domain-tls-tenant "#vanity-domain-tls-tenant")
- [Complete domain setup](#complete-domain-ownership "#complete-domain-ownership")
- [Point domains to CloudFront](#point-domains-to-cloudfront "#point-domains-to-cloudfront")
- [Domain considerations (distribution tenant)](#tenant-domain-considerations "#tenant-domain-considerations")
- [Wildcard domains (distribution tenant)](#tenant-wildcard-domains "#tenant-wildcard-domains")

## Add a domain and certificate (distribution tenant)

The following procedure shows you how to add a domain and update the certificate for a
distribution tenant.

###### To add a domain and certificate (distribution tenant)

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Under **SaaS**, choose
   **Distribution tenants**.
3. Search for the distribution tenant. Use the dropdown menu in the search bar to filter by
   domain, name, distribution ID, certificate ID, connection group ID, or web ACL
   ID.
4. Choose the distribution tenant name.
5. For **Domains**, choose **Manage domain**.
6. For
   **Certificate**, choose if you want a
   **Custom TLS certificate** for your
   distribution tenant. The certificate verifies whether you're authorized to
   use the domain name. The certificate must exist in the
   US East (N. Virginia) Region.
7. For **Domains**, choose **Add domain** and enter the domain name. Depending on
   your domain, the following messages will appear under the domain name that you
   enter.
   - This domain is covered by the certificate.
   - This domain is covered by the certificate, pending
     validation.
   - This domain isn't covered by a certificate. (This means you must
     verify domain ownership.)

8. Choose **Update distribution tenant**.

On the tenant details page, under **Domains**, you can see
the following fields:

    * **Domain ownership** – The status of domain
     ownership. Before CloudFront can serve content, your domain ownership must be
     verified by using TLS certificate validation.
    * **DNS status** – Your domain's DNS
     records must point to CloudFront to route traffic correctly.

9. If your domain ownership isn't verified, on the tenant details page, under
   **Domains**, choose **Complete domain
   setup** and then complete the following procedure to point the DNS
   record to your CloudFront domain name.

## Complete domain setup

Follow these procedures to verify that you own the domain for your distribution tenants.
Depending on your domain, choose one of the following procedures.

###### Note

If your domain is already pointed to CloudFront with an Amazon Route 53 alias record, you must
add your DNS TXT record with `_cf-challenge.` in front of the domain
name. This TXT record verifies that your domain name is linked to CloudFront. Repeat this
step for each domain. The following shows how to update your TXT record:

- Record name: `_cf-challenge.`DomainName``
- Record type: `TXT`
- Record value: `CloudFrontRoutingEndpoint`
  For example, your TXT record might look like: `_cf-challenge.example.com TXT
 d111111abcdef8.cloudfront.net`

You can find your CloudFront routing endpoint in the console on the distribution tenant detail page or use the [ListConnectionGroups](../../../cloudfront/latest/APIReference/API_ListConnectionGroups.md "../../../cloudfront/latest/APIReference/API_ListConnectionGroups.md") API action in the _Amazon CloudFront API Reference_ to find it.

###### Tip

If you're a SaaS provider and you want to allow certificate issuance without requiring your
customers (tenants) to add a TXT record directly to their DNS, do the
following:

1. If you own the domain `example-saas-provider.com`, assign
   subdomains to your tenants, such as
   `customer-123.example-saas-provider.com`
2. In your DNS, add the
   `_cf-challenge.customer-123.example-saas-provider.com TXT
d111111abcdef8.cloudfront.net` TXT record to your DNS
   configuration.
3. Next, your customers (the tenants) can then update their own DNS record to
   map their domain name to the subdomain that you provided.

`www.customer-domain.com CNAME
 customer-123.example-saas-provider.com`

I have existing traffic
Select this option if your domain can't tolerate downtime. You must have access to
your origin/web server. Use the following procedure to validate domain ownership.

###### To complete domain setup when you have existing traffic

1. For **Specify your web traffic**, choose **I have
   existing traffic** and then choose
   **Next**.
2. For **Verify domain ownership**, choose one of the
   following options:
   - **Use existing certificate** – Search for an
     existing ACM certificate or enter the certificate ARN that covers
     the listed domains.
   - **Manual file upload** – Choose if you
     have direct access to upload files to your web server.

   For each domain, create a plain text file that
   contains your validation token from the **Token
   location** and upload it to your origin at the
   specified **File path** on your existing
   server. The path to this file might look like the following
   example:
   `/.well-known/pki-validation/acm_9c2a7b2ec0524d09fa6013efb73ad123.txt`.
   After you complete that step, ACM verifies the token and
   then issues the TLS certificate for the domain.
   - **HTTP redirect** – Choose if you don't
     have direct access to upload files to your web server, or if you're
     using a CDN or proxy service.

   For each domain, create a 301 redirect on your existing server.
   Copy the well-known path under **Redirect from**
   and point to the specified certificate endpoint under
   **Redirect to**. Your redirect might look like
   the following example:

   ```
   If the URL matches: example.com/.well-known/pki-validation/leabe938a4fe077b31e1ff62b781c123.txt
   Then the settings are:Forwarding URL
   Then 301 Permanent Redirect:To validation.us-east-1.acm-validations.aws/123456789012/.well-known/pki-validation/leabe938a4fe077b31e1ff62b781c123.txt

   ```

###### Note

You can choose **Check certificate status** to verify
when ACM issues the certificate for the domain. 3. Choose **Next**. 4. Complete the steps for [Point domains to CloudFront](#point-domains-to-cloudfront "#point-domains-to-cloudfront").

I don't have traffic
Select this option if you're adding new domains. CloudFront will manage certificate
validation for you.

###### To complete domain setup if you don't have traffic

1. For **Specify your web traffic**, choose **I
   don't have traffic yet**.
2. For each domain name, complete the steps for [Point domains to CloudFront](#point-domains-to-cloudfront "#point-domains-to-cloudfront").
3. After you update your DNS records for each domain name, choose
   **Next**.
4. Wait for the certificate
   to be issued.

###### Note

You can choose **Check certificate status** to verify
when ACM issues the certificate for the domain. 5. Choose **Submit**.

## Point domains to CloudFront

Update your DNS records to route traffic from each domain to the CloudFront routing
endpoint. You can have multiple domain names, but they must all resolve to this
endpoint.

###### To point domains to CloudFront

1. Copy the CloudFront routing endpoint value, such as
   d111111abcdef8.cloudfront.net.
2. Update your DNS records to route traffic from each domain to the CloudFront routing endpoint.
   1. Sign in to your domain registrar or DNS provider management console.
   2. Navigate to the DNS management section for your domain.
      - For subdomains – Create a CNAME record. For example:
        - Name – Your subdomain (such as `www` or `app`)
        - Value / Target – The CloudFront routing endpoint
        - Record type – CNAME
        - TTL – 3600 (or whatever is appropriate for your use case)

      - For apex/root domains – This requires a unique DNS configuration, because standard CNAME records can’t be used at the root or apex domain level. Because most DNS providers don’t support ALIAS records, we recommend creating an ALIAS record in Route 53. For example:
        - Name – Your apex domain (such as `example.com`)
        - Record type – A
        - Alias – Yes
        - Alias target – Your CloudFront routing endpoint
        - Routing policy – Simple (or whatever is appropriate for your use case)

   3. Verify that the DNS change has propagated. (This usually happens when the TTL is expired. Sometimes it can take 24-48 hours.) Use a tool like `dig` or `nslookup`.

   ```
   dig www.example.com
   # Should eventually return a CNAME pointing to your CloudFront routing endpoint
   ```

3. Return to the CloudFront console and choose **Submit**. When your domain is active, CloudFront updates
   the domain status to indicate that your domain is ready to serve traffic.

For more information, see the documentation for your DNS provider:

- [Cloudflare](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/ "https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/")
- [ClouDNS](https://www.cloudns.net/wiki/article/9/ "https://www.cloudns.net/wiki/article/9/")
- [DNSimple](https://support.dnsimple.com/categories/dns/ "https://support.dnsimple.com/categories/dns/")
- [Gandi.net](https://www.gandi.net/ "https://www.gandi.net/")
- [GoDaddy](https://www.godaddy.com/help/manage-dns-records-680 "https://www.godaddy.com/help/manage-dns-records-680")
- [Google Cloud DNS](https://cloud.google.com/dns/docs/records "https://cloud.google.com/dns/docs/records")
- [Namecheap](https://www.namecheap.com/support/knowledgebase/article.aspx/767/10/how-to-change-dns-for-a-domain/ "https://www.namecheap.com/support/knowledgebase/article.aspx/767/10/how-to-change-dns-for-a-domain/")

## Domain considerations (distribution tenant)

When a domain is active, domain control has been established and CloudFront will respond to all
viewer requests to this domain. Once activated, a domain can't be deactivated or changed to
an inactive status. The domain can't be associated with another CloudFront resource while it's
already in use. To associate the domain with another distribution, use the [UpdateDomainAssociation](../../../cloudfront/latest/APIReference/API_UpdateDomainAssociation.md "../../../cloudfront/latest/APIReference/API_UpdateDomainAssociation.md") request to move the domain from one CloudFront resource to
another.

When a domain is inactive, CloudFront won't respond to viewer requests to the domain. While the
domain is inactive, note the following:

- If you have a pending certificate request, CloudFront will respond to requests for the
  well-known path. While the request is pending, the domain can't be associated with
  any other CloudFront resources.
- If you don't have a pending certificate request, CloudFront won't respond to requests
  for the domain. You can associate the domain with other CloudFront resources.
- You can only have _one pending certificate request_ per
  distribution tenant. Before you can request another certificate for additional domains, you
  must cancel the existing pending request. Canceling an existing certificate request
  does not delete the associated ACM certificate. You can delete that by using the ACM API.
- If you apply a new certificate to your distribution tenant, this will disassociate the
  previous certificate. You can reuse the certificate to cover the domain for another
  distribution tenant.

As with renewals for DNS-validated certificates, you will be notified when the certificate
renewal succeeds. However, you don't need to do anything else. CloudFront will manage the
certificate renewal for your domain automatically.

###### Note

You don't need to call the ACM API operations to create or update your certificate resources.
You can manage your certificates by using the [CreateDistributionTenant](../../../cloudfront/latest/APIReference/API_CreateDistributionTenant.md "../../../cloudfront/latest/APIReference/API_CreateDistributionTenant.md") and [UpdateDistributionTenant](../../../cloudfront/latest/APIReference/API_UpdateDistributionTenant.md "../../../cloudfront/latest/APIReference/API_UpdateDistributionTenant.md") API operations to specify the details for your
managed certificate request.

## Wildcard domains (distribution tenant)

Wildcard domains are supported for distribution tenants in the following situations:

- When the wildcard is included in the shared certificate that's inherited from the parent multi-tenant distribution
- When you use a valid existing custom TLS certificate for your distribution tenant
