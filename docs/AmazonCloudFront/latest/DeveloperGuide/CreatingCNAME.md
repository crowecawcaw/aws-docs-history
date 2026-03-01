# Add an alternate domain name

The following task list describes how to use the CloudFront console to add an
alternate domain name to your distribution so that you can use your own domain name in your links
instead of the CloudFront domain name. For
information about updating your distribution using the CloudFront API, see
[Configure distributions](distribution-working-with.md "distribution-working-with.md").

###### Note

If you want viewers to use HTTPS with your alternate domain name, see
[Use alternate domain names and HTTPS](using-https-alternate-domain-names.md "using-https-alternate-domain-names.md").

**Before you begin:** Make sure that you do the following
before you update your distribution to add an alternate domain name:

- Register the domain name with Route 53 or another domain registrar.
- Get a TLS certificate from an authorized certificate authority (CA) that covers the
  domain name. Add the certificate to your distribution to validate that you
  are authorized to use the domain. For more information, see [Requirements for using alternate domain names](CNAMEs.md#alternate-domain-names-requirements "CNAMEs.md#alternate-domain-names-requirements").

###### Add an alternate domain name

1. Sign in to the AWS Management Console and open the CloudFront console at
   [https://console.aws.amazon.com/cloudfront/v4/home](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home").
2. Choose the ID for the distribution that you want to update.
3. On the **General** tab, choose **Add a domain**.
4. Enter up to five domains to serve.
5. Choose **Next**.
6. For **TLS certificate**, if CloudFront can't find an existing AWS Certificate Manager (ACM) certificate for your domain in your AWS account in the `us-east-1` AWS Region, you can choose to automatically create a certificate or manually create it in ACM.
7. When your certificate is provisioned, you must update your DNS records with your DNS provider to prove domain ownership. The entries that you need to make to your DNS records are provided for you in the CloudFront console.
8. After you update your DNS records, choose **Validate certificate**.
9. When the certificate is validated, choose **Next**.
10. Review your changes and choose **Add domains**.
11. On the **General** tab for the distribution, confirm that
    **Distribution Status** has changed to **Deployed**.
    If you try to use an alternate domain name before the updates to your distribution have
    been deployed, the links that you create in the following steps might not work.
12. Configure the DNS service for the alternate domain name (such as www.example.com) to
    route traffic to the CloudFront domain name for your distribution (such as
    d111111abcdef8.cloudfront.net). The method that you use depends on whether you’re
    using Route 53 as the DNS service provider for the domain or another
    provider. For more information, see [Add a domain to your CloudFront standard distribution](add-domain-existing-distribution.md "add-domain-existing-distribution.md").

**Route 53**

Create an alias resource record set. With an alias resource record set, you don’t pay
for Route 53 queries. You can also create an alias resource
record set for the root domain name (example.com), which DNS
doesn’t allow for CNAMEs. For instructions on creating an alias resource record set, see [Routing traffic to an Amazon CloudFront web
distribution by using your domain name](../../../Route53/latest/DeveloperGuide/routing-to-cloudfront-distribution.md "../../../Route53/latest/DeveloperGuide/routing-to-cloudfront-distribution.md") in the
_Amazon Route 53 Developer Guide_.

Optionally, you can create an HTTPS record for an alternate domain name to allow protocol negotiation as part of the DNS lookup if the client supports it.

###### To create an alias resource record set with an HTTPS record (optional)

    1. Enable HTTP/2 or HTTP/3 in your CloudFront distribution settings. For more information, see [Supported HTTP versions](DownloadDistValuesGeneral.md#DownloadDistValuesSupportedHTTPVersions "DownloadDistValuesGeneral.md#DownloadDistValuesSupportedHTTPVersions") and [Update a distribution](HowToUpdateDistribution.md "HowToUpdateDistribution.md").
    2. In the Route 53 console, create an alias resource record set. Follow the [Routing traffic to an Amazon CloudFront web
     distribution by using your domain name](../../../Route53/latest/DeveloperGuide/routing-to-cloudfront-distribution.md "../../../Route53/latest/DeveloperGuide/routing-to-cloudfront-distribution.md") procedure.
    3. While you are creating the alias resource record set, create an alias record with record type **HTTPS**.

**Another DNS service provider**

Use the method provided by your DNS service provider to add a CNAME record for your
domain. This new CNAME record will redirect DNS queries from
your alternate domain name (for example, www.example.com) to the
CloudFront domain name for your distribution (for example,
d111111abcdef8.cloudfront.net). For more information, see the
documentation provided by your DNS service provider.

###### Important

If you already have an existing CNAME record for your alternate domain name, update
that record or replace it with a new one that points to the
CloudFront domain name for your distribution. 13. Using `dig` or a similar DNS tool, confirm that the DNS configuration that you
created in the previous step points to the domain name for your
distribution.

The following example shows a `dig` request on the www.example.com domain, as
well as the relevant part of the response.

```
PROMPT> dig www.example.com

; <<> DiG 9.3.3rc2 <<> www.example.com
;; global options:	printcmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 15917
;; flags: qr rd ra; QUERY: 1, ANSWER: 9, AUTHORITY: 2, ADDITIONAL: 0

;; QUESTION SECTION:
;www.example.com.     IN    A

;; ANSWER SECTION:
`www.example.com. 10800 IN CNAME d111111abcdef8.cloudfront.net.`
...
```

The answer section shows a CNAME record that routes queries for www.example.com to the
CloudFront distribution domain name d111111abcdef8.cloudfront.net. If the name on the right
side of `CNAME` is the domain name for your CloudFront distribution,
the CNAME record is configured correctly. If it’s any other value, for
example, the domain name for your Amazon S3 bucket, then the CNAME record is
configured incorrectly. In that case, go back to step 7 and correct the
CNAME record to point to the domain name for your distribution. 14. Test the alternate domain name by visiting URLs with your domain name instead of the CloudFront
domain name for your distribution. 15. In your application, change the URLs for your objects to use your alternate domain name
instead of the domain name of your CloudFront distribution.
