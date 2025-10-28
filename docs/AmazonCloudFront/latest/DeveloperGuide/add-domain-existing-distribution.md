# Add a domain to your CloudFront standard distribution

After you create a new CloudFront standard distribution, you can add a domain to it. Optionally, you can set up a Amazon Route 53 domain for your standard distribution when you create it. For more information, see [Create a CloudFront distribution in the console](distribution-web-creating-console.md#create-console-distribution "distribution-web-creating-console.md#create-console-distribution").

## Add a domain to your existing standard distribution

###### To add a domain to your standard distribution

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. In the navigation pane, choose **Distributions**, then choose
   the distribution ID.
3. Under **Settings**, **Alternate domain names**, choose **Add a domain**.
4. Enter up to five domains to serve.
5. Choose **Next**.
6. For **TLS certificate**, if CloudFront can't find an existing AWS Certificate Manager (ACM) certificate for your domain in your AWS account in the `us-east-1` AWS Region, you can create one.
   - If you are using Amazon Route 53 (Route 53), CloudFront automatically creates a certificate for you.

7. When your certificate is provisioned, you must update your DNS records with your DNS provider to prove domain ownership. Then, choose **Validate certificate**. For more information, see [Point domains to CloudFront (standard distribution)](#point-domains-standard "#point-domains-standard").
   - If you are using Route 53, CloudFront updates your DNS records for you.

8. Choose **Next**.
9. Review your changes and choose **Add domains**.
10. Before you send traffic to your distribution, make sure to update your DNS records to point to CloudFront. For more information, choose **Route domains to CloudFront** in the **Settings** section of your distribution details page.
    - If you are using Route 53, you can have CloudFront set up DNS routing for you automatically.

## Point domains to CloudFront (standard distribution)

Update your DNS records to route traffic from each domain to the CloudFront hostname. You can have multiple domain names, but they must all resolve to this
hostname.

###### To point domains to CloudFront

1. Copy the CloudFront hostname value, such as
   d111111abcdef8.cloudfront.net.
2. Update your DNS records to route traffic from each domain to the CloudFront hostname.
   1. Sign in to your domain registrar or DNS provider management console.
   2. Navigate to the DNS management section for your domain.
      - For subdomains – Create a CNAME record. For example:
        - Name – Your subdomain (such as `www` or `app`)
        - Value / Target – Your CloudFront hostname
        - Record type – CNAME
        - TTL – 3600 (or whatever is appropriate for your use case)

      - For apex/root domains – This requires a unique DNS configuration, because standard CNAME records can’t be used at the root or apex domain level. Because most DNS providers don’t support ALIAS records, we recommend creating an ALIAS record in Route 53. For example:
        - Name – Your apex domain (such as `example.com`)
        - Record type – A
        - Alias – Yes
        - Alias target – Your CloudFront hostname
        - Routing policy – Simple (or whatever is appropriate for your use case)

   3. Verify that the DNS change has propagated. (This usually happens when the TTL is expired. Sometimes it can take 24-48 hours.) Use a tool like `dig` or `nslookup`.

   ```
   dig www.example.com
   # Should eventually return a CNAME pointing to your CloudFront hostname
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
