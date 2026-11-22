

# Choose a domain for your Lightsail website

A domain is the name in the URL that people use to reach your website or application, such as `example.com` in `https://example.com`. In Lightsail, you can use one of two kinds of domain:
+ **A Lightsail web address** is a subdomain of `amazonlightsail.com`, such as `mysite.amazonlightsail.com`. Lightsail manages its DNS records and SSL/TLS certificate on your behalf. For more information, see [Lightsail web addresses](amazon-lightsail-web-addresses.md).
+ **A custom domain** is a domain that you own, such as `example.com` or `blog.example.com`. You register it in Lightsail or with another registrar, such as Cloudflare. You're responsible for managing the domain, its DNS records, and its SSL/TLS certificate. For more information, see [Registered domains](amazon-lightsail-domain-registration.md).

## Choose a web address or a custom domain
<a name="choose-web-address-or-domain"></a>

Choose a Lightsail web address if:
+ You want to avoid domain registration and renewal fees.
+ You want HTTPS on your distribution without registering a domain, managing DNS records, or creating a certificate. Lightsail provides the name, the DNS records, and the certificate.
+ A name that ends in `amazonlightsail.com` works for you.

Choose a custom domain if:
+ You want a name that's fully your own, such as `example.com`, or a top-level domain other than `.com`, such as `.org` or `.shop`.
+ You want to receive email at your domain, such as `you@example.com`. Email needs MX records, which you can add only in a DNS zone that you manage.
+ You want a domain for an instance, load balancer, or container service without a distribution.

The following table shows all the differences between a Lightsail web address and a custom domain.


|  |  Lightsail web address  |  Custom domain  | 
| --- | --- | --- | 
| Example | `mysite.amazonlightsail.com`, `blog.mysite.amazonlightsail.com` (a child web address) | `example.com`, `www.example.com` | 
| Your own name | Yes, but it's always a subdomain of `amazonlightsail.com`. | Yes. | 
| DNS management | Not supported. Lightsail manages the DNS records for you, so you can't add records, such as MX records for email. | Supported. You manage the DNS records in a Lightsail DNS zone or with a third-party DNS provider, such as Cloudflare, including MX records for email. | 
| SSL/TLS certificate | Not needed. Lightsail creates and renews the certificate for you. | You create and validate an SSL/TLS certificate for HTTPS. | 
| Resources that can use it | Distributions. For instructions, see [Attach a web address using the Lightsail console](amazon-lightsail-create-attach-web-address.md#attach-web-address). | Instances, load balancers, container services, and distributions. | 
| Subdomains | Yes, but a web address name can have at most two parts, such as `blog.mysite.amazonlightsail.com` (a child web address). For more information, see [Child web addresses](amazon-lightsail-web-addresses.md#web-addresses-child). | Yes. | 
| Cost | Free while attached to a resource. Each month, you get 24 hours of free unattached web address time. After that, we charge USD $1 per month for each unattached web address. DNS queries count toward your monthly DNS query allowance. For more information, see [What do Lightsail web addresses cost?](amazon-lightsail-frequently-asked-questions-faq-billing-and-account-management.md#what-do-lightsail-web-addresses-cost). | Registration and renewal fees. Lightsail DNS zones are free. DNS queries to your Lightsail DNS zone count toward the same DNS query allowance. For more information, see [What do Lightsail domains cost?](amazon-lightsail-frequently-asked-questions-faq-billing-and-account-management.md#what-do-lightsail-domains-cost). | 
| Quotas | Up to 30 web addresses in your account. For more information, see [Quotas and considerations](amazon-lightsail-web-addresses.md#web-addresses-considerations). | Up to 6 Lightsail DNS zones. To manage more domains, use Route 53. | 

You can start with a web address and switch your distribution to a custom domain later, or switch back. For instructions, see [Switch between a web address and a custom domain](amazon-lightsail-enabling-distribution-custom-domains.md#switch-web-address-custom-domain).

**Note**  
In the Lightsail API and AWS CLI, DNS zones are called *domains*, and web addresses are called *subdomains*.

## Topics
<a name="web-addresses-and-domains-topics"></a>
+ [Web addresses](amazon-lightsail-web-addresses.md)
+ [Registered domains](amazon-lightsail-domain-registration.md)
  + [DNS in Lightsail](understanding-dns-in-amazon-lightsail.md)