

# Public DNS fallback for private hosted zones

With public DNS fallback, when a query from your VPC asks for a name that doesn't exist in your private hosted zone, Route 53 retries the query against public DNS instead of returning NXDOMAIN (non-existent domain). Use it when your private hosted zone holds internal records, or records that override public names inside your VPCs, and you want every other name to resolve the way it does on the internet.

When public DNS fallback is disabled, Route 53 treats a private hosted zone as authoritative for its whole domain inside the associated VPCs. Suppose your private hosted zone is `example.com`. A query from the VPC for `www.example.com`, which exists only in public DNS, returns NXDOMAIN. The usual workaround is to copy the public record into the private hosted zone and keep the two in sync. When public DNS fallback is enabled, the query for `www.example.com` returns the public answer, so you don't need the copy.

Public DNS fallback is a setting on a private hosted zone, and it applies to every VPC that's associated with the zone, directly or through a Route 53 Profile. It's disabled by default and is available only for private hosted zones that use the `ADVANCED` tier. For more information, see [Hosted zone tiers](hosted-zone-tiers.md).

**Topics**
+ [How public DNS fallback works](#hosted-zone-private-public-dns-fallback-how-it-works)
+ [When changes take effect](#hosted-zone-private-public-dns-fallback-when-changes-take-effect)
+ [Enabling and disabling public DNS fallback](#hosted-zone-private-public-dns-fallback-enable)
+ [Checking the public DNS fallback status](#hosted-zone-private-public-dns-fallback-check-status)
+ [Considerations for public DNS fallback](#hosted-zone-private-public-dns-fallback-considerations)

## How public DNS fallback works
<a name="hosted-zone-private-public-dns-fallback-how-it-works"></a>

Route 53 VPC Resolver, the DNS resolver that's available by default in all VPCs, always checks the private hosted zone first. What happens next depends on the answer that the zone returns:
+ If the zone has a record of the requested type, VPC Resolver returns that record.
+ If the name exists in the zone but has no record of the requested type, VPC Resolver returns NODATA. For example, an A record exists for `app.example.com`, and a query asks for the AAAA record.
+ If the name doesn't exist in the zone:
  + If public DNS fallback is disabled, VPC Resolver returns NXDOMAIN.
  + If public DNS fallback is enabled, VPC Resolver retries the query against public DNS and returns the public answer.

Queries for the following names never fall back, because the zone doesn't return NXDOMAIN for them:
+ The zone apex, such as `example.com`, which always exists because every zone has start of authority (SOA) and NS records. Create any other apex records that your VPC clients need, such as an A record for your website or MX records for email, in the private hosted zone as well.
+ Names that match a wildcard record, such as `*.example.com`. Create any public records that your VPC clients need for those names in the private hosted zone as well.
+ Names in a subdomain that the zone delegates with NS records, which get a referral instead. To resolve those names from the VPC, use a VPC Resolver delegation rule. For more information, see [Resolver delegation rules tutorial](outbound-delegation-tutorial.md).

When private hosted zones overlap, such as `example.com` and `accounting.example.com`, the public DNS fallback setting of the zone that's authoritative for the name applies. To use public DNS fallback for every name in a domain, enable it on each private hosted zone. For more information about which zone is authoritative, see [Private hosted zones that have overlapping namespaces](hosted-zone-private-considerations.md#hosted-zone-private-considerations-private-overlapping).

## When changes take effect
<a name="hosted-zone-private-public-dns-fallback-when-changes-take-effect"></a>

After you enable or disable public DNS fallback, the change generally propagates to all Route 53 servers within 60 seconds. To confirm that it has, see [Checking the public DNS fallback status](#hosted-zone-private-public-dns-fallback-check-status).

A change to the public DNS fallback setting doesn't affect answers that are currently in resolver caches. With the default SOA record, a name that returned NXDOMAIN shortly before you enable fallback can keep returning NXDOMAIN for up to 15 minutes. For more information about how long negative answers are cached, see [The start of authority (SOA) record](SOA-NSrecords.md#SOArecords). To test the change sooner, query a name that you haven't queried recently. The same applies when you disable fallback: cached public answers keep resolving until their TTLs expire.

## Enabling and disabling public DNS fallback
<a name="hosted-zone-private-public-dns-fallback-enable"></a>

You can enable or disable public DNS fallback on an existing private hosted zone that uses the `ADVANCED` tier by using the Route 53 console, API, AWS CLI, or SDK. If the zone uses the `STANDARD` tier, first change its tier. For more information, see [Changing the tier of a hosted zone](hosted-zone-tiers.md#hosted-zone-tiers-change).

**To enable or disable public DNS fallback using the Route 53 console**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Hosted zones**.

1. Choose the name of the advanced private hosted zone that you want to update.

1. In **Hosted zone details**, choose **Edit hosted zone**.

1. Under **Public DNS fallback**, select **Enable public DNS fallback** to enable it, or clear it to disable it.

1. Choose **Save changes**.

To do this through the API, set `EnablePublicDNSFallback` to `true` or `false` in [UpdateHostedZoneFeatures](https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHostedZoneFeatures.html), or use one of the following AWS CLI commands, replacing `{{Z1D633PJN98FT9}}` with the ID of your hosted zone.

To enable public DNS fallback:

```
aws route53 update-hosted-zone-features --hosted-zone-id {{Z1D633PJN98FT9}} --enable-public-dns-fallback
```

To disable public DNS fallback:

```
aws route53 update-hosted-zone-features --hosted-zone-id {{Z1D633PJN98FT9}} --no-enable-public-dns-fallback
```

To enable public DNS fallback when you create a private hosted zone in the console, choose **Advanced** for **Tier**, and then select **Enable public DNS fallback**. With the API or AWS CLI, include it in the create request. For an example, see [Updating optional features](hosted-zone-features.md#hosted-zone-features-optional).

## Checking the public DNS fallback status
<a name="hosted-zone-private-public-dns-fallback-check-status"></a>

To check the public DNS fallback status of a zone, look at the **Public DNS fallback** status on the hosted zone details page in the Route 53 console. You can also call [GetHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHostedZone.html), or the `get-hosted-zone` AWS CLI command, and read the `PublicDNSFallbackStatus` field in the `Features` element of the response. The status is one of the following values:

`ENABLING`  
The change to enable public DNS fallback is propagating to the Route 53 name servers.

`ENABLED`  
Public DNS fallback is enabled, and the change has propagated.

`DISABLING`  
The change to disable public DNS fallback is propagating to the Route 53 name servers.

`DISABLED`  
Public DNS fallback is disabled, and any change has propagated.

## Considerations for public DNS fallback
<a name="hosted-zone-private-public-dns-fallback-considerations"></a>

Keep the following in mind when you use public DNS fallback:
+ If a VPC Resolver forwarding rule covers the same domain name as the private hosted zone, the rule takes precedence and public DNS fallback doesn't apply. For more information about VPC Resolver rules, see [Private hosted zones and Route 53 VPC Resolver rules](hosted-zone-private-considerations.md#hosted-zone-private-considerations-resolver-rules).
+ Resolver DNS Firewall rules still apply to queries that fall back. If a rule blocks a domain name, queries for that name stay blocked. For more information about DNS Firewall, see [Using DNS Firewall to filter outbound DNS traffic](resolver-dns-firewall.md).
+ Public answers can come from any public DNS provider. Your public hosted zone doesn't have to be in Route 53.
+ Public DNS fallback also applies to VPCs that you associate with the zone after you enable it.
+ If a CNAME record in the zone points to a name in another private hosted zone, VPC Resolver looks up the target in that zone. That zone's public DNS fallback setting decides whether a missing target falls back.