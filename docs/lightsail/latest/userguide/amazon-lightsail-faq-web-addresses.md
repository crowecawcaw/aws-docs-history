

# Lightsail web addresses
<a name="amazon-lightsail-faq-web-addresses"></a>

## What are Lightsail web addresses?
<a name="what-are-lightsail-web-addresses"></a>

Lightsail web addresses are subdomains of `amazonlightsail.com`, such as `mysite.amazonlightsail.com`, that are automatically configured for HTTPS traffic. When you attach a web address to one of your Lightsail resources, Lightsail creates and manages its DNS records and its SSL/TLS certificate for you. For more information, see [Lightsail web addresses](amazon-lightsail-web-addresses.md).

You don't need to register a domain, manage DNS records, or create and validate a certificate, so a web address is quicker and easier to set up than a custom domain. For more information, see [Choose a web address or a custom domain](amazon-lightsail-web-addresses-and-domains.md#choose-web-address-or-domain).

**Note**  
Web addresses are free while they are attached to your Lightsail resources. Each month, you get 24 hours of free unattached web address time. After that, we charge USD $1 per month for each unattached web address.

## When should I use a web address instead of a custom domain?
<a name="when-to-use-web-address-or-custom-domain"></a>

Use a Lightsail web address when you want HTTPS on your distribution without registering a domain, managing DNS records, or creating a certificate, and a name that ends in `amazonlightsail.com` works for you. Use a custom domain when you want a name that's fully your own, email at your domain, or a domain for a resource without a distribution. For more information, see [Choose a web address or a custom domain](amazon-lightsail-web-addresses-and-domains.md#choose-web-address-or-domain).

## Why did I get charged for my web address?
<a name="when-am-i-charged-for-a-web-address"></a>

Web addresses are free while they are attached to your Lightsail resources. If you were charged, a web address in your account wasn't attached to a resource for longer than the free time. Each month, you get 24 hours of free unattached web address time. After that, we charge USD $1 per month for each unattached web address.
+ A web address is unattached while it has the **Unattached** status: from when it's ready after you create it until you attach it, and from when you detach it until you attach it again or delete it.
+ A web address stays attached while you transfer it, so a transfer doesn't incur charges.
+ You aren't charged for implicit web addresses or web addresses that failed to create.

DNS queries to your web addresses, attached or not, count toward your monthly allowance of 3 million DNS queries. If your account belongs to an organization in AWS Organizations, the allowance is shared by all the accounts in the organization. Beyond the allowance, you're charged USD $0.40 per 1 million DNS queries.

## Which resources can I attach a web address to?
<a name="which-resources-can-use-web-addresses"></a>

You can attach a web address to a Lightsail distribution. To use a web address with a bucket, instance, load balancer, or container service, create a distribution with that resource as its origin, and attach the web address to the distribution. You can attach a web address to one distribution at a time, and a distribution can have one web address. For more information, see [Understand distribution origins in Amazon Lightsail](amazon-lightsail-distribution-origins.md).

**Note**  
The distribution has its own monthly plan cost. For more information, see [Understand distribution plans in Amazon Lightsail](amazon-lightsail-distribution-plans.md).

## Can a distribution use a web address and a custom domain at the same time?
<a name="web-address-and-custom-domain"></a>

No. A distribution can use a Lightsail web address or a custom domain, but you can switch between them. For instructions, see [Switch between a web address and a custom domain](amazon-lightsail-enabling-distribution-custom-domains.md#switch-web-address-custom-domain).

## How many web addresses can I have?
<a name="how-many-web-addresses"></a>

You can have up to 30 web addresses in your account.
+ Web addresses that failed to create count toward this quota.
+ Deleted web addresses that are still in their cooldown period count toward this quota.
+ Implicit web addresses don't count toward this quota.
+ You can't increase this quota.

## Why can't I create a web address with the name that I want?
<a name="why-is-web-address-name-unavailable"></a>

Web address names are unique across all AWS accounts. You might not be able to create a web address with the name that you want for one of the following reasons:
+ Another account has the name.
+ The name is in another account's cooldown period.
+ Lightsail reserves the name. Lightsail reserves names such as brand names, trademarks, AWS service names, and common words. Common words, such as `blog`, are reserved only as one-part names, so you can use one as the first part of a child web address, such as `blog.mysite`.
+ The name doesn't follow the naming rules. For more information, see [Web address naming rules](amazon-lightsail-create-attach-web-address.md#web-address-naming-rules).
+ You already have 30 web addresses, counting web addresses that failed to create and deleted web addresses that are still in their cooldown period.

## What happens to the name of a web address after I delete it?
<a name="what-happens-to-deleted-web-address-name"></a>

If the web address was previously attached to a resource, Lightsail holds its name for 30 to 37 days. During that time, your account can create a web address with the same name again, and other accounts can't. If the web address was never attached, its name is available as soon as the deletion finishes. For more information, see [What happens to the name of a deleted web address](amazon-lightsail-delete-web-address.md#web-address-cooldown).

## Do I need an SSL/TLS certificate for a web address?
<a name="web-address-certificate"></a>

No. Lightsail creates, validates, and renews the SSL/TLS certificate for your web address. The certificate doesn't appear with your other Lightsail certificates, and it doesn't count toward your Lightsail certificate quota.

## Can I add DNS records to my web address or use it for email?
<a name="web-address-dns-records"></a>

No. Lightsail manages the DNS records for your web address, and you can't add or change records, such as MX records for email. To use your own DNS records, use a custom domain. For more information, see [Choose a web address or a custom domain](amazon-lightsail-web-addresses-and-domains.md#choose-web-address-or-domain).

## In which AWS Regions are web addresses available?
<a name="web-address-regions"></a>

Web addresses are global resources, like distributions, so you don't choose a Region for them in the Lightsail console. In the Lightsail API and AWS CLI, use the US East (N. Virginia) (`us-east-1`) AWS Region.

## What are child and implicit web addresses?
<a name="child-and-implicit-web-addresses"></a>

A child web address has two parts, such as `blog.mysite.amazonlightsail.com`, and if you haven't created its parent, the parent is reserved for your account as an implicit web address. For more information, see [Child web addresses](amazon-lightsail-web-addresses.md#web-addresses-child).

## Can I change the name of my web address?
<a name="rename-web-address"></a>

No. To use a different name, create a web address with the new name, detach the old web address from your resource, attach the new one, and then delete the old one.

## My web address is attached, but my site doesn't load. What should I do?
<a name="web-address-site-doesnt-load"></a>

If you visited your web address in a browser before it was attached, it can take up to 15 minutes after it's attached before it works for you.

If the origin of your distribution is a WordPress instance, configure WordPress to use your web address. For instructions, see [Configure WordPress with a Lightsail content delivery network](amazon-lightsail-configure-wordpress-for-distribution.md).

If your instance uses WordPress packaged by Bitnami, see the [Bitnami version](amazon-lightsail-configure-wordpress-for-distribution-bitnami.md) of that tutorial.

## Can I move a web address to another AWS account?
<a name="move-web-address-to-another-account"></a>

No. You can transfer a web address only between resources in your account.