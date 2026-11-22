

# Lightsail web addresses

Lightsail web addresses are subdomains of `amazonlightsail.com`, such as `mysite.amazonlightsail.com`, that are automatically configured for HTTPS traffic. When you attach a web address to a distribution, Lightsail creates the DNS records and the SSL/TLS certificate for it, so visitors can reach the distribution over HTTPS. Lightsail manages the certificate and the DNS records for you: they don't appear with your SSL/TLS certificates or in your DNS zones, and you can't change them.

Lightsail web addresses are easier and quicker to set up than custom domains. For more information, see [Choose a web address or a custom domain](amazon-lightsail-web-addresses-and-domains.md#choose-web-address-or-domain).

**Note**  
Web addresses are free while they are attached to your Lightsail resources. Each month, you get 24 hours of free unattached web address time. After that, we charge USD $1 per month for each unattached web address.

A web address name can have one or two parts, separated by a period. For example, `mysite.amazonlightsail.com` has one part (`mysite`), and its child web address `blog.mysite.amazonlightsail.com` has two parts (`blog` and `mysite`). For more information, see [Child web addresses](#web-addresses-child).

**Note**  
In the Lightsail API and AWS CLI, web addresses are called *subdomains*. For more information, see [CreateSubdomain](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateSubdomain.html) in the *Lightsail API Reference*.

**Contents**
+ [Use a web address](#web-addresses-use)
+ [How much do web addresses cost?](#web-addresses-cost)
+ [Web address statuses](#web-address-statuses)
+ [Child web addresses](#web-addresses-child)
+ [Quotas and considerations](#web-addresses-considerations)

## Use a web address
<a name="web-addresses-use"></a>

To use a web address, attach it to a distribution. To use a web address with an instance, bucket, container service, or load balancer, create a distribution with that resource as its origin. For more information, see [Understand distribution origins in Amazon Lightsail](amazon-lightsail-distribution-origins.md).

**Note**  
A web address can be attached to one distribution at a time, and a distribution can have one web address.

For instructions, see the following topics:
+ [Create and attach a Lightsail web address](amazon-lightsail-create-attach-web-address.md)
+ [Detach or transfer a Lightsail web address](amazon-lightsail-detach-transfer-web-address.md)
+ [Add a web address when you create a distribution](amazon-lightsail-creating-content-delivery-network-distribution.md#distribution-web-address-create-time)
+ [Delete a Lightsail web address](amazon-lightsail-delete-web-address.md)

## How much do web addresses cost?
<a name="web-addresses-cost"></a>

Web addresses are free while they are attached to your Lightsail resources. Each month, you get 24 hours of free unattached web address time. After that, we charge USD $1 per month for each unattached web address. If your account belongs to an organization in AWS Organizations, the 24 free hours are shared by all the accounts in the organization.

DNS queries to your web addresses count toward your monthly allowance of 3 million DNS queries. If your account belongs to an organization in AWS Organizations, the allowance is shared by all the accounts in the organization. Beyond the allowance, you're charged USD $0.40 per 1 million DNS queries.

## Web address statuses
<a name="web-address-statuses"></a>

The status of a web address shows whether you can attach, detach, or delete it, or whether it's waiting for an operation to finish. You can see it on the **Lightsail web addresses** page and in the `state` that `GetSubdomains` returns.

**Creating**  
Lightsail is setting up your web address. You can't attach or delete it yet. You aren't charged for it.

**Create failed**  
Lightsail accepted your request but couldn't finish setting up your web address. You aren't charged for it, but it counts toward your quota until you delete it. Delete the web address, and then create it again.  
If your request to create a web address fails, for example because the name isn't available, no web address is created, and you get an error right away.

**Unattached**  
Your web address is ready to be attached to a distribution. You can attach or delete it.

**Attaching**  
Lightsail is attaching your web address to a distribution.

**Attached**  
Your web address is attached to a distribution and serves its content over HTTPS.

**Detaching**  
Lightsail is detaching your web address from a resource.

**Transferring**  
Lightsail is moving your web address to a different resource.

**Implicit**  
Reserved for your account because you created a child web address under it. For more information, see [Child web addresses](#web-addresses-child).

## Child web addresses
<a name="web-addresses-child"></a>

A child web address is a web address under one of your web addresses, such as `blog.mysite.amazonlightsail.com` under `mysite.amazonlightsail.com`. Use one for another site under the same name, such as a blog. A child web address has two parts, and its parent is the web address with one part.

When you create a child web address, such as `blog.mysite.amazonlightsail.com`, and you haven't created its parent, `mysite.amazonlightsail.com`, Lightsail reserves `mysite.amazonlightsail.com` for your account with the **Implicit** status, so that no other account can create it. An implicit web address isn't charged and doesn't count toward your quota of web addresses. To use an implicit web address, claim it. After you claim it, it counts toward your quota and is charged while it isn't attached. For instructions, see [Claim an implicit web address](amazon-lightsail-create-attach-web-address.md#claim-web-address).

A child web address is a separate web address. You can attach, detach, transfer, and delete a child web address like any other web address. You can't attach a web address and its child web address to the same resource.

**Note**  
You're charged for a child web address while it isn't attached, like any other web address.

**Note**  
To reach one resource at more than one name, such as `example.com` and `blog.example.com`, use a custom domain instead of web addresses. For more information, see [Use a custom domain with your distribution](amazon-lightsail-enabling-distribution-custom-domains.md#distribution-custom-domain).

## Quotas and considerations
<a name="web-addresses-considerations"></a>
+ You can have up to 30 web addresses in your account.
+ Web addresses that failed to create count toward this quota until you delete them.
+ When you delete a web address that was attached to a distribution, Lightsail holds its name for your account for 30 to 37 days, called the cooldown period. The exact length is random, so that no one can predict when the name becomes available to other accounts. The deleted web address counts toward this quota during that time. For more information, see [What happens to the name of a deleted web address](amazon-lightsail-delete-web-address.md#web-address-cooldown).
+ Implicit web addresses don't count toward this quota.
+ You can't increase this quota.
+ Web address names are unique across all AWS accounts. For the naming rules, see [Web address naming rules](amazon-lightsail-create-attach-web-address.md#web-address-naming-rules).
+ AWS can take down a web address, or take other action described in the [AWS Acceptable Use Policy](https://aws.amazon.com/aup/), if AWS believes that its name or content violates someone else's rights, such as copyrights or trademarks, or doesn't follow that policy.
+ You can attach a web address to one resource at a time. To move a web address to a different resource, transfer it. For instructions, see [Transfer a web address using the Lightsail console](amazon-lightsail-detach-transfer-web-address.md#transfer-web-address).
+ You can transfer a web address once every 24 hours. This limit applies to each web address, not to your account.
+ A distribution can use a web address or a custom domain, but not both at the same time. To change from one to the other, see [Switch between a web address and a custom domain](amazon-lightsail-enabling-distribution-custom-domains.md#switch-web-address-custom-domain).
+ Lightsail manages the DNS records for your web address. You can't add or change records, such as MX records for email.
+ Lightsail manages the SSL/TLS certificate for your web address and renews it for you. The certificate doesn't appear with your other Lightsail certificates, and it doesn't count toward your Lightsail certificate quota.
+ Web addresses are global resources. When you use the [Lightsail API](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/Welcome.html) or the [AWS CLI](https://docs.aws.amazon.com/cli/latest/reference/lightsail/) to manage web addresses, specify the US East (N. Virginia) (`us-east-1`) AWS Region.

## Topics
<a name="web-addresses-topics"></a>
+ [Create and attach a Lightsail web address](amazon-lightsail-create-attach-web-address.md)
+ [Detach or transfer a Lightsail web address](amazon-lightsail-detach-transfer-web-address.md)
+ [Delete a Lightsail web address](amazon-lightsail-delete-web-address.md)