

# Monitor BGP route protection
<a name="monitor-bgp-route-security"></a>

IPAM BGP route protection monitors Resource Public Key Infrastructure (RPKI) validity for all Bring Your Own IP (BYOIP) prefixes across accounts and Regions from a single dashboard, detects route overlaps that may indicate hijacking, and, with delegated RPKI, eliminates manual Route Origin Authorization (ROA) management at ARIN, RIPE, APNIC, and LACNIC. You go from logging into Regional Internet Registry (RIR) portals per-prefix to zero manual ROA operations.

## The problem this solves
<a name="monitor-bgp-route-security-problem"></a>

Customers who bring their own IP addresses to AWS must manually manage BGP route protection at their Regional Internet Registry. This means logging into RIR portals (ARIN, RIPE, APNIC) for every prefix, tracking expiration dates across dozens or hundreds of ROAs, and relying on third-party tools to detect route hijacks. For ROA management, customers either use their RIR's hosted portal or run open-source tools like Krill (NLnet Labs) to operate their own RPKI certificate authority (CA). Many customers skip ROA creation entirely or create them once and forget to renew. There's no integrated solution that combines route monitoring, RPKI management, and IP address management in one place.

With delegated RPKI, you no longer have to provide authenticity or ownership proof of CIDRs or prefixes when provisioning, because AWS verifies it on your behalf. At the same time, AWS creates ROAs for each new CIDR that you provision.

## How it works
<a name="monitor-bgp-route-security-how"></a>

BGP route protection is built from three layers, each building on the previous one:
+ **Route discovery**: IPAM discovers all BYOIP routes across accounts and Regions. You see prefix, ASN, advertisement status, and RPKI validity in one dashboard.
+ **Route protection findings**: IPAM evaluates each route against published ROA data. It flags conflicting ROAs, missing ROAs, permissive configurations, and overlapping announcements from other ASNs. Without this, you have no way to detect sub-prefix hijacks or expired ROAs until traffic is already misrouted.
+ **Delegated RPKI**: You authorize AWS to manage ROAs on your behalf through a one-time setup with your RIR. From that point, IPAM auto-creates ROAs when you provision CIDRs, auto-renews them before expiration, and manages ROAs for on-premises prefixes you haven't brought to AWS. Without delegation, you must manually track expiration dates across dozens of ROAs and renew them at each RIR portal individually.

## When to use it
<a name="monitor-bgp-route-security-when"></a>

Consider BGP route protection if any of the following apply:
+ You have BYOIP prefixes and want to know if they're protected against hijacking.
+ You want to stop manually creating and renewing ROAs at your RIR.
+ You want a single dashboard showing RPKI posture across all accounts and Regions.
+ You need to manage ROAs for on-premises IP space from the same console as your AWS IPs.

BGP route protection is not needed if any of the following apply:
+ You only use AWS-owned IP space (Elastic IP addresses, service-managed prefixes). AWS manages ROAs for those automatically.
+ Your BYOIP prefixes are not advertised to the internet (private use only within AWS). No BGP announcements means no hijack risk.
+ Your organization already runs a mature RPKI CA (such as Krill) with full automation and monitoring. In that case, delegated RPKI would duplicate what you already have, though the monitoring dashboard may still add value for centralized visibility.

## Getting started options
<a name="monitor-bgp-route-security-getting-started"></a>

You don't have to enable everything at once. Each capability works independently:
+ **Monitoring**: View all BYOIP routes that IPAM automatically discovers from your provisioned prefixes, including advertisement status, RPKI validity, ROA strength, route overlaps, and ROA expiration. Free Tier customers can call the route discovery API; Advanced Tier adds the full dashboard with RPKI findings and overlap detection. No RIR setup is needed. Start here to understand your current posture before making changes.
+ **Delegate RPKI**: Delegate ROA management to AWS through a one-time Internet Registry Association setup with your RIR. Once active, ROAs are created on provisioning and renewed automatically. Delegated RPKI supports batch updates for managing multiple prefixes atomically. Start here if you're already managing ROAs manually and want to eliminate that operational burden.

You can start with monitoring, evaluate your posture, and add delegated RPKI later without disrupting existing routes.

## Tier requirements
<a name="monitor-bgp-route-security-tiers"></a>


| Capability | Free Tier | Advanced Tier | 
| --- | --- | --- | 
| Route discovery (view routes) | Yes | Yes | 
| Route protection findings (RPKI status, overlaps) | No | Yes | 
| Delegated RPKI (automated ROA management) | No | Yes | 
| On-premises ROA management (routing policy registrations) | No | Yes | 

For pricing details, see the IPAM tab on the [Amazon VPC pricing page](https://aws.amazon.com/vpc/pricing/).

## Supported Regional Internet Registries
<a name="monitor-bgp-route-security-rirs"></a>


| RIR | Coverage | Notes | 
| --- | --- | --- | 
| ARIN | North America, parts of the Caribbean | Most common for US-based customers | 
| RIPE NCC | Europe, Middle East, Central Asia |  | 
| APNIC | Asia Pacific |  | 
| LACNIC | Latin America, Caribbean | Delegated RPKI supported. Automatic CIDR discovery and ROA pre-creation are not available during initial setup. | 
| AFRINIC | Africa | Route discovery and findings only. Delegated RPKI not supported. | 

## Key concepts
<a name="monitor-bgp-route-security-concepts"></a>

ROA (Route Origin Authorization)  
A cryptographically signed object that authorizes a specific ASN to advertise a specific IP prefix. ROAs have three key attributes: CIDR, ASN, and max-length. Max-length indicates the longest (most-specific) subnet that the ASN is authorized to announce.

Strict ROA  
Max-length matches the prefix length exactly. Only this exact prefix is RPKI-valid when announced by the authorized ASN. More-specific announcements from any ASN are RPKI-invalid. This is the recommended default.

Permissive ROA  
Max-length is greater than the prefix length. The authorized ASN can announce more-specific subnets that are also RPKI-valid. This is useful for traffic engineering but offers weaker protection against sub-prefix hijacking.

Internet Registry Association  
The trust relationship between your IPAM and your RIR. Once active, AWS can publish and manage ROAs for your IP space.

Routing policy registration (RPR)  
A set of ROAs for a prefix, managed by IPAM for IP space that hasn't been brought to AWS. An RPR consists of a prefix and a list of ASNs, mapping to multiple ROAs (one per ASN). RPRs cover on-premises prefixes.

ROA auto-renewal  
When delegated RPKI is active, AWS renews ROAs before expiration automatically. No tracking or manual action is needed.

## What happens without BGP route protection
<a name="monitor-bgp-route-security-without"></a>
+ **No ROA at all**: Your prefix has RPKI status *Unknown*. Networks that enforce RPKI validation may still accept it, but you have zero protection against route hijacks. Any ASN can announce your prefix or a more-specific prefix, and validating networks have no basis to reject it.
+ **Permissive ROA**: Your prefix is RPKI-valid, but so are more-specific announcements from the same ASN. An attacker who compromises your ASN credentials can announce more-specific prefixes that are also valid, splitting your traffic.
+ **Expired ROA**: Your prefix transitions from *Valid* to *Unknown* silently. Traffic continues flowing, but the prefix is no longer protected against route hijack because validating networks cannot distinguish your legitimate announcement from an unauthorized one.
+ **No overlap detection**: A third party announces your prefix or a sub-prefix. Without monitoring, you don't know until customers report connectivity issues, which can take hours or days.

## Console visualizations
<a name="monitor-bgp-route-security-visualizations"></a>

The Route monitoring dashboard (**IPAM** > **Monitoring** > **Route monitoring**) shows three charts:
+ **RPKI Coverage**: A pie chart showing Valid, Invalid, and Unknown across all advertised routes.
+ **ROA Strength**: A pie chart showing the Strict versus Permissive distribution.
+ **Routes with Overlaps**: A count of routes with conflicting more-specific advertisements from different ASNs.

## Command line
<a name="monitor-bgp-route-security-cli"></a>

The commands in this section link to the *AWS CLI Command Reference*. The documentation provides detailed descriptions of the options that you can use when you run the commands.
+ View discovered routes: [get-ipam-discovered-routes](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-ipam-discovered-routes.html)
+ View route protection findings: [get-ipam-route-protection-findings](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-ipam-route-protection-findings.html)
+ Create an Internet Registry Association: [create-ipam-internet-registry-association](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-ipam-internet-registry-association.html)
+ Enable an Internet Registry Association: [enable-ipam-internet-registry-association](https://docs.aws.amazon.com/cli/latest/reference/ec2/enable-ipam-internet-registry-association.html)
+ View ROAs: [get-ipam-route-origin-authorizations](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-ipam-route-origin-authorizations.html)
+ View association CIDRs: [get-ipam-internet-registry-association-cidrs](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-ipam-internet-registry-association-cidrs.html)
+ Create a routing policy registration: [create-ipam-routing-policy-registration](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-ipam-routing-policy-registration.html)
+ Batch modify registrations: [batch-modify-ipam-routing-policy-registrations](https://docs.aws.amazon.com/cli/latest/reference/ec2/batch-modify-ipam-routing-policy-registrations.html)
+ View registration deltas: [get-ipam-routing-policy-registration-deltas](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-ipam-routing-policy-registration-deltas.html)

To see examples of how you can use the AWS CLI to set up BGP route protection, see [Tutorial: Set up delegated RPKI for BYOIP prefixes](tutorials-byoip-bgp-security.md).