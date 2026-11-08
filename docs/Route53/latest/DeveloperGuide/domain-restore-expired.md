

# Restoring an expired or deleted domain
<a name="domain-restore-expired"></a>

If you don't renew a domain before the end of the late-renewal period or if you accidentally delete the domain, for some registries for top-level domains (TLDs), you can [restore](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_RestoreDomain.html) the domain before it becomes available for others to register.

When a domain is deleted or it passes the end of the late-renewal period, it no longer appears in the Amazon Route 53 console. 

**Note**  
You can't use AWS credits to pay the fee for restoring a domain.

**Important**  
Restoring a domain typically costs more than registering or renewing one. For the current price, see the Restoration Price column in [Amazon Route 53 Pricing for Domain Registration](https://d32ze2gidvkk54.cloudfront.net/Amazon_Route_53_Domain_Registration_Pricing_20140731.pdf). If the domain is a premium domain, its restoration price isn't listed here and varies by domain name; search for the domain in the Route 53 console or use the `GetDomainPrices` API operation to see its price.

**Important**  
For generic TLD domains deleted within the first 5 days after registration, the standard 30-day redemption period doesn't apply. Anyone can register these domains immediately. To check the redemption period for a TLD, see [Domains that you can register with Amazon Route 53](registrar-tld-list.md).<a name="domain-restore-expired-procedure"></a>

**To restore domain registration when a domain is deleted or the late-renewal period has expired**

1. Determine whether the TLD registry for the domain supports restoring domains and, if so, the period during which restoration is allowed.

   1. See [Domains that you can register with Amazon Route 53](registrar-tld-list.md).

   1. Find the TLD for your domain, and review the values in the Deadlines for renewing and restoring domains section. 

1. Using the AWS account that the domain was registered to, call the [RestoreDomain](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_RestoreDomain.html) API action for the domain that you want to restore.

1. If the restoration succeeds, the domain reappears in the console and in the response to [GetDomainDetail](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_GetDomainDetail.html). The new expiration date might be different from the domain's previous expiration date. If the domain can no longer be restored, the request fails with no charge.