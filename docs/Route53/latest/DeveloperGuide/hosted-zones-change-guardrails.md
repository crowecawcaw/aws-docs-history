

# Change Guardrails for hosted zones

Amazon Route 53 Change Guardrails are safety checks that stop a change to the records in a hosted zone when the change would take part of your domain offline. Before Route 53 applies a change, it runs each guardrail that is on for the hosted zone. If a guardrail finds a problem, Route 53 rejects the whole request with an `InvalidChangeBatch` error, applies none of its changes, and tells you which record and which guardrail caused the rejection and how to fix it.

Route 53 provides six guardrails. Two are always on. You turn the other four on for each hosted zone, and three of them are available only for hosted zones that use the `ADVANCED` tier. Guardrails apply to the changes that you make with the Route 53 console, the `ChangeResourceRecordSets` API, the AWS SDKs, the AWS CLI, and CloudFormation. The following table lists the six guardrails.


| Guardrail | What it rejects | Default | Tier | Hosted zones | 
| --- | --- | --- | --- | --- | 
| Name server format check (`NS_FORMAT_CHECK`) | An NS record value that looks like a Route 53 name server but isn't one. | Always on | `STANDARD` and `ADVANCED` | Public and private | 
| Delegation authority check (`NS_DELEGATION_AUTHORITY_CHECK`) | An NS record that delegates a subdomain to Route 53 name servers that aren't authoritative for the subdomain. | Always on | `STANDARD` and `ADVANCED` | Public only | 
| Name server occlusion check (`NS_OCCLUSION_CHECK`) | A record that an existing delegation hides from resolvers, or a delegation that would hide existing records. | Off | `STANDARD` and `ADVANCED` | Public and private | 
| Alias target check (`ALIAS_TARGET_CHECK`) | Deleting a record that an alias record points to. | Off | `ADVANCED` only | Public and private | 
| Active record check (`ACTIVE_RECORD_CHECK`) | Deleting a record that still receives DNS queries. | Off | `ADVANCED` only | Public and private | 
| Active delegation check (`ACTIVE_DELEGATION_CHECK`) | Deleting a delegation that resolvers still use. | Off | `ADVANCED` only | Public and private | 

**Topics**
+ [What each guardrail checks](#change-guardrails-checks)
+ [How Route 53 decides that a record is in use](#change-guardrails-in-use)
+ [Enabling and disabling guardrails for a hosted zone](#change-guardrails-enable)

## What each guardrail checks
<a name="change-guardrails-checks"></a>

Each guardrail checks your change for one kind of mistake. It judges your hosted zone as it would be after the whole request, so a request that creates and deletes records is judged on its net result.

### Name server format check
<a name="change-guardrails-ns-format"></a>

**What it rejects**  
An NS record value that looks like a Route 53 name server but has a format error, such as a misspelled or missing top-level domain, a missing letter, a trailing comma, or several name servers in one value.

**Why it matters**  
A delegation to a name server that doesn't exist takes the subdomain offline. If the misspelled name belongs to someone else, that party can answer the queries for your subdomain.

**How it works**  
Route 53 compares every NS record value that looks like one of its own name servers with the formats that it uses. It doesn't check the name servers of other DNS providers. For example, the guardrail rejects `ns-1234.awsdns-56.og`, where `org` is misspelled, and `ns-1234.awsdns-56.org.example.com`, which has extra labels, and accepts `ns-1234.awsdns-56.org`.

### Delegation authority check
<a name="change-guardrails-delegation-authority"></a>

**What it rejects**  
An NS record that delegates a subdomain to Route 53 name servers that aren't authoritative for the subdomain, which means that they don't serve a hosted zone for it. This happens when you create the NS record before the hosted zone for the subdomain exists, when you keep the NS record after that hosted zone is deleted, or when you copy name servers from another hosted zone.

**Why it matters**  
Queries for the subdomain fail, and the subdomain is at risk of takeover: anyone who gets a hosted zone that uses those name servers can answer for your subdomain. This is a dangling delegation. For more information, see [Protection from dangling delegation records in Route 53](protection-from-dangling-dns.md).

**How it works**  
For example, an NS record for `dev.example.com` in your `example.com` hosted zone passes if the name servers in it serve a hosted zone for `dev.example.com`. If that hosted zone was deleted and the NS record still names its name servers, the guardrail rejects the record. Create the hosted zone first, and then put the four name servers that Route 53 assigns to it in the NS record. Route 53 checks only its own name servers, not the name servers of other DNS providers, and because the check verifies public delegations, it doesn't apply to private hosted zones.

![An NS record in the example.com hosted zone delegates dev.example.com to Route 53 name servers. Allowed if they serve a hosted zone for dev.example.com, rejected if not.](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/images/change-guardrails-delegation-authority.png)


### Name server occlusion check
<a name="change-guardrails-ns-occlusion"></a>

**What it rejects**  
A change that occludes records. When an NS record delegates a subdomain to other name servers, the delegation occludes the records at or under that subdomain in your own hosted zone: resolvers that follow the delegation ask the other name servers, which don't have your records. The guardrail rejects whichever record you add second: a record at or under a subdomain that your hosted zone already delegates, or an NS record for a subdomain that already has records under it.

**Why it matters**  
The occluded names stop resolving for the clients whose resolvers follow the delegation, even though the records are still in your hosted zone, which makes the problem hard to find.

**How it works**  
For example, your `example.com` hosted zone delegates `sub.example.com` to other name servers. If you create an A record for `app.sub.example.com`, the guardrail rejects it. If `app.sub.example.com` already exists and you create the NS record for `sub.example.com`, the guardrail rejects the NS record. The guardrail allows the records that belong at a delegation: the NS record itself and a Delegation Signer (DS) record at the delegated name, glue records (A or AAAA records whose name is one of the delegation's name servers), and the NS record at the zone apex, which names your hosted zone's own name servers. The guardrail doesn't check deletions, and it allows a request that fixes the conflict in the same step, such as deleting the records under `sub.example.com` and creating the NS record in one request. If more records would be occluded than one request can delete, delete them in earlier requests, and then create the NS record.

![In the example.com hosted zone, an NS record delegates sub.example.com. A new A record under it is rejected; the glue record and a DS record at the delegation are allowed.](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/images/change-guardrails-occlusion.png)


### Alias target check
<a name="change-guardrails-alias-target"></a>

**What it rejects**  
Deleting a record that an alias record in the same hosted zone points to. For example, `www.example.com` is an alias record that points to the A record `app.example.com`, and you delete `app.example.com`.

**Why it matters**  
Without its target, the alias record stops resolving, and every client that queries it gets an error, even though you didn't change the alias record itself.

**How it works**  
The guardrail allows the deletion if the same request deletes or retargets every alias record that points to the target, or if another record with the same name and type remains, such as the other members of a weighted record set. Changing a record's values isn't a deletion. The guardrail checks only alias records in the same hosted zone. To delete a chain of alias records in several requests, start at the top: delete each alias record before the record that it points to. If more alias records point to the target than one request can delete or retarget, delete or retarget them in earlier requests, and then delete the target.

![In the example.com hosted zone, the alias records www and api point to app.example.com. Deleting app.example.com while they point to it is rejected.](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/images/change-guardrails-alias-target.png)


### Active record check
<a name="change-guardrails-active-record"></a>

**What it rejects**  
Deleting a record that is still receiving DNS queries when no record would remain at the same name and type to answer them. For example, you delete the A record for `api.example.com` during a cleanup, but clients queried it a few minutes ago and no other record for `api.example.com` remains.

**Why it matters**  
Nothing fails right away, because resolvers keep the old answer until its TTL runs out. After that, every client that asks for the name gets no answer.

**How it works**  
Route 53 checks whether the record answered a DNS query recently. For how long a record counts as in use, see [How Route 53 decides that a record is in use](#change-guardrails-in-use). The guardrail judges only records that are gone after your request. Changing a record's values isn't a deletion, and NS records are judged by the active delegation check instead.  
Deleting one record of a set that uses a routing policy is allowed when a remaining record still answers the deleted record's clients:  
+ Weighted, latency, failover, multivalue answer, and geoproximity sets – Any remaining record.
+ Geolocation sets – A remaining record for a larger area, such as the continent or the default record.
+ AZ-affinity sets – A remaining record for a larger area, such as the Region or the Global record.
+ IP-based sets – The remaining default record of the same CIDR collection.
Route 53 rejects deleting the default record of a geolocation, AZ-affinity, or IP-based set while it is in use, because no other record answers its clients.  
The guardrail counts only the queries for the record's own name, so it can't protect these records:  
+ The secondary record of a failover set while the primary record is healthy. It receives no queries.
+ A record that clients reach only through a CNAME record. The queries count for the CNAME record, not for its target.
To protect a record regardless of its query activity, add a record set protection for it. For more information, see [Protecting records from changes](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/rrset-protection.html).

![Resolvers query api.example.com in the example.com hosted zone. Deleting the record while it still receives queries is rejected; deleting it after the queries stop is allowed.](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/images/change-guardrails-active-record.png)


### Active delegation check
<a name="change-guardrails-active-delegation"></a>

**What it rejects**  
Deleting the NS record for a subdomain (a delegation) while resolvers are still being referred to it. For example, you delete the NS record that delegates `eu.example.com` to another hosted zone, but that hosted zone still answers queries for names under `eu.example.com`.

**Why it matters**  
Deleting a delegation takes down every name under the subdomain at once, as soon as the resolvers' cached referrals expire, and nothing warns you until queries fail.

**How it works**  
The delegation is in use if Route 53 recently referred resolvers to the subdomain. If the NS record names Route 53 name servers that serve a hosted zone for the subdomain, the delegation is also in use while that hosted zone receives DNS queries, because resolvers that have the delegation cached query the hosted zone directly. Delegations to name servers outside Route 53 are judged by the referrals alone. Changing the name servers in the NS record isn't a deletion. For how long a delegation counts as in use, see [How Route 53 decides that a record is in use](#change-guardrails-in-use).

![Resolvers are referred by the example.com hosted zone to eu.example.com, then query its hosted zone directly. Deleting the NS record is rejected while either continues.](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/images/change-guardrails-active-delegation.png)


## How Route 53 decides that a record is in use
<a name="change-guardrails-in-use"></a>

Route 53 keeps track of the names and record types that recently answered DNS queries, and of the subdomains that it recently referred resolvers to. Because resolvers cache an answer for the record's time to live (TTL) and don't ask Route 53 again until it expires, Route 53 treats a record or a delegation as in use for 15 minutes plus its TTL after it last answered a query, up to a maximum of one hour. A record with a TTL of 60 seconds is in use for 16 minutes after its last query, so you can delete it 20 minutes after it stops receiving traffic. A record with a TTL of 24 hours is in use for one hour.

Because of the one-hour maximum, resolvers can keep using a record whose TTL is longer than one hour after Route 53 has stopped treating it as in use. Before you delete a record that has a long TTL, lower the TTL, wait for the old TTL to expire, and then delete the record.

The active record check and the active delegation check are based on the DNS queries that Route 53 receives, so they work best for hosted zones that receive regular traffic. A rarely queried record is in use only for a short time after each query, and it might not be in use at the moment you delete it, even if something still depends on it. To protect a record regardless of its query activity, add a record set protection for it. For more information, see [Protecting records from changes](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/rrset-protection.html).

Occasionally, Route 53 might not have current query activity data, for example during a service event that affects the system that collects it. The two checks then use the most recent activity that Route 53 has recorded. If that activity shows that your record is in use, Route 53 rejects the deletion. If Route 53 has no recorded activity for the record, or can't read its activity data at all, it allows the deletion, because it doesn't block a change that it can't verify. The other guardrails don't depend on query activity. If a service event affects the guardrails, you can see the status and the affected period in the AWS Health Dashboard. For more information, see the [AWS Health User Guide](https://docs.aws.amazon.com/health/latest/ug/).

## Enabling and disabling guardrails for a hosted zone
<a name="change-guardrails-enable"></a>

You turn the four optional guardrails on or off for each hosted zone. Enabling a guardrail doesn't change your records. From then on, Route 53 applies the guardrail to the changes that you make in that hosted zone. The two always-on guardrails can't be turned off.

To turn a guardrail on or off, specify it in `ChangeGuardrails` when you create the hosted zone with [CreateHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html), or later with [UpdateHostedZoneFeatures](https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHostedZoneFeatures.html). Each entry has a `Name` (`NS_OCCLUSION_CHECK`, `ALIAS_TARGET_CHECK`, `ACTIVE_RECORD_CHECK`, or `ACTIVE_DELEGATION_CHECK`) and a `Status` (`ENABLED` or `DISABLED`). To see the guardrails that Route 53 applies to a hosted zone, call [GetHostedZone](https://docs.aws.amazon.com/Route53/latest/APIReference/API_GetHostedZone.html) and look at `ChangeGuardrails` in `Features`. The response lists every guardrail with its status. For the console and AWS CLI procedures, see [Updating optional features](hosted-zone-features.md#hosted-zone-features-optional).

The following AWS CLI command turns on the active record check for a hosted zone. Replace {{Z123456789}} with the ID of your hosted zone.

```bash
aws route53 update-hosted-zone-features \
    --hosted-zone-id {{Z123456789}} \
    --change-guardrails Name=ACTIVE_RECORD_CHECK,Status=ENABLED
```

`ALIAS_TARGET_CHECK`, `ACTIVE_RECORD_CHECK`, and `ACTIVE_DELEGATION_CHECK` require the `ADVANCED` tier. If you turn one of them on for a hosted zone that uses the `STANDARD` tier, Route 53 rejects the request with an `InvalidInput` error. Route 53 also rejects a change of the hosted zone to the `STANDARD` tier while one of them is on. Turn them off first. For more information, see [Hosted zone tiers](hosted-zone-tiers.md).

If a guardrail rejects a change that you want to make anyway, turn the guardrail off, make the change, and then turn the guardrail on again. AWS CloudTrail records every change that you make to a hosted zone's guardrails, so you can see who turned a guardrail off, what changed while it was off, and when it was turned on again.