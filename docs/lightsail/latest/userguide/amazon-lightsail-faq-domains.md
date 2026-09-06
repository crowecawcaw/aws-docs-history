

# Domains
<a name="amazon-lightsail-faq-domains"></a>

## What can I do with Lightsail domains?
<a name="what-can-i-do-with-lightsail-domains"></a>

Lightsail domains allow you to register and manage domains for your website or application. If you have domains that are registered with other providers, you can transfer management of those domains to Lightsail. You can also point those domains to your Lightsail resources.

## What top-level domains (TLDs) can I use?
<a name="what-top-level-domains-can-i-use"></a>

Lightsail uses the same generic TLDs as Amazon Route 53. If you would like to register a geographic domain, we recommend you use the Route 53 console. Your geographic domain will be available in the Lightsail console after it has been registered using Route 53. For more information about the TLDs that Lightsail supports, see [Domains that you can register with Amazon Route 53 in the Amazon Route 53 Developer Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html#registrar-tld-list-index-generic) .

## Can I make Lightsail the DNS service for my existing domain?
<a name="can-i-make-lightsail-the-dns-service-existing-domain"></a>

You can transfer DNS management of a domain that you registered using another DNS service provider to Lightsail. For more information, see [Create a DNS zone to manage your domain’s DNS records](lightsail-how-to-create-dns-entry.md).

## How do I get started with domain registration in Lightsail?
<a name="how-do-i-get-started-domain-registration"></a>

After logging in to Lightsail, you can use the [Lightsail console](https://lightsail.aws.amazon.com/) to create and manage domains. For more information, see [Domain registration](amazon-lightsail-domain-registration.md).

## When should I register a domain in Lightsail versus Route 53?
<a name="when-should-i-register-domain-in-lightsail-r53"></a>

Tasks such as registering a domain, creating DNS zones, and routing traffic for a domain to Lightsail resources are done in Lightsail. We recommend using Route 53 for advanced tasks, such as extending domain registrations, transferring domains, including traffic policies, and creating private hosted zones. 

## Can I transfer my domain to Lightsail?
<a name="can-i-transfer-domain-to-lightsail"></a>

You can transfer your domain to Route 53. After the domain transfer is complete, your domain will be available in the Lightsail console. For more information, see [Managing a Lightsail domain in Amazon Route 53](amazon-lightsail-manage-domain-advanced.md).

## What Lightsail resources can I use with domains?
<a name="what-resources-can-i-use-with-domain"></a>

After registering a domain in Lightsail, you can point your domain to a Lightsail instance, container, load balancer, static IP, or content distribution network (CDN).