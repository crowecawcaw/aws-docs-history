# Direct Connect routing policies and BGP communities

Direct Connect applies inbound (from your on-premises data center) and outbound (from your AWS
Region) routing policies for a public Direct Connect connection. You can also use Border Gateway
Protocol (BGP) community tags on routes advertised by Amazon and apply BGP community tags on
the routes you advertise to Amazon.

## Public virtual interface routing policies

If you're using Direct Connect to access public AWS services, you must specify the public
IPv4 prefixes or IPv6 prefixes to advertise over BGP.

The following inbound routing policies apply:

- You must own the public prefixes and they must be registered as such in the
  appropriate regional internet registry.
- Traffic must be destined to Amazon public prefixes. Transitive routing between
  connections is not supported.
- Direct Connect performs inbound packet filtering to validate that the source of the
  traffic originated from your advertised prefix.

The following outbound routing policies apply:

- AS_PATH and Longest Prefix Match are used to determine the routing path. AWS
  recommends advertising more specific routes using Direct Connect if the same prefix is
  being advertised to both the Internet and to a public virtual interface.
- Direct Connect advertises all local and remote AWS Region prefixes where available
  and includes on-net prefixes from other AWS non-Region points of presence
  (PoP) where available; for example, CloudFront and Route 53.

###### Note

    + Prefixes listed in the AWS IP address ranges JSON file,
     ip-ranges.json, for the AWS China Regions are only advertised in
     the AWS China Regions.
    + Prefixes listed in the AWS IP address ranges JSON file,
     ip-ranges.json, for the AWS Commercial Regions are
     only advertised in the AWS Commercial Regions.For more information about the

ip-ranges.json file, see [AWS IP address
ranges](../../../general/latest/gr/aws-ip-ranges.md "../../../general/latest/gr/aws-ip-ranges.md") in the
_AWS General Reference_.

- Direct Connect advertises prefixes with a minimum path length of 3.
- Direct Connect advertises all public prefixes with the well-known
  `NO_EXPORT` BGP community.
- If you advertise the same prefixes from two different Regions
  using two different public virtual interfaces, and both have the same BGP
  attributes and longest prefix length, AWS will prioritize the home
  Region for outbound traffic.
- If you have multiple Direct Connect connections, you can adjust the load-sharing of
  inbound traffic by advertising prefixes with the same path attributes.
- The prefixes advertised by Direct Connect must not be advertised beyond the network
  boundaries of your connection. For example, these prefixes must not be included
  in any public internet routing table.
- Direct Connect keeps prefixes advertised by customers within the Amazon network. We
  do not re-advertise customer prefixes learned from a public VIF to any of the
  following:
  - Other Direct Connect customers
  - Networks that peer with the AWS Global Network
  - Amazon's transit providers

- When using a public interface, you can use either a public or private ASN.
  However, there are important considerations:
  - Public ASNs: You must own the ASN and have the right to announce it.
    AWS will verify your ownership of the ASN. Both ASNs (1-2147483647)
    and long ASNs (1-4294967295) are supported.
  - Private ASNs: You can use private ASNs from the following ranges:
    - private ASNs: 64512-65534
    - private long ASNs: 4200000000-4294967294
      However, Direct Connect will replace the private ASN with the AWS ASN
      (7224) when advertising your prefixes to other AWS customers or the
      internet.

  - ASN prepending:
    - With a public ASN (both ASN and long ASN), prepending will work as expected,
      and your prepended ASN will be visible to other networks.
    - With a private ASN (both ASN and long ASN, any prepending you do will be stripped
      when AWS replaces your private ASN with 7224. This means ASN prepending is not effective
      for influencing routing decisions outside of AWS when using a private ASN on a public virtual interface.

- When establishing a BGP peering session with AWS over a public virtual
  interface, use 7224 for the autonomous system numbers (ASN) to establish the BGP
  session on the AWS side. The ASN on your router or customer gateway device
  should be different from that ASN. Your customer ASN can be either anASN
  (1-2147483647, excluding reserved ranges) or a long ASN (1-4294967295, excluding
  reserved ranges).

## Public virtual interface BGP communities

Direct Connect supports scope BGP community tags to help control the scope (Regional or
global) and route preference of traffic on public virtual interfaces. AWS treats all
routes received from a public VIF as if they were tagged with the NO_EXPORT BGP
community tag, meaning only the AWS network will use that routing information.

### Scope BGP communities

You can apply BGP community tags on the public prefixes that you advertise to Amazon to
indicate how far to propagate your prefixes in the Amazon network, for the local
AWS Region only, all Regions within a continent, or all public Regions.

#### AWS Region communities

For inbound routing policies, you can use the following BGP communities for your
prefixes:

- `7224:9100`—Local AWS Regions
- `7224:9200`—All AWS Regions for a continent:
  - North America-wide
  - Asia Pacific
  - Europe, the Middle East and Africa

- `7224:9300`—Global (all public AWS Regions)

###### Note

If you do not apply any community tags, prefixes are advertised to all public AWS Regions
(global) by default.

Prefixes that are marked with the same communities, and have identical AS_PATH
attributes are candidates for multi-pathing.

The communities `7224:1` – `7224:65535` are reserved by
Direct Connect.

For outbound routing policies, Direct Connect applies the following BGP communities to
its advertised routes:

- `7224:8100`—Routes that originate from the same AWS Region in
  which the Direct Connect point of presence is associated.
- `7224:8200`—Routes that originate from the same continent with
  which the Direct Connect point of presence is associated.
- No tag—Routes that originate from other continents.

###### Note

To receive all AWS public prefixes do not apply any filter.

Communities that are not supported for an Direct Connect public connection are
removed.

### `NO_EXPORT` BGP

community

For outbound routing policies, the `NO_EXPORT` BGP community tag is
supported for public virtual interfaces.

Direct Connect also provides BGP community tags on advertised Amazon routes. If you use
Direct Connect to access public AWS services, you can create filters based on these
community tags.

For public virtual interfaces, all routes that Direct Connect advertises to customers
are tagged with the NO_EXPORT community tag.

## Private virtual interface and transit virtual interface routing policies

If you're using AWS Direct Connect to access your private AWS resources,
you must specify the IPv4 or IPv6 prefixes to advertise over BGP. These prefixes can be
public or private.

The following outbound routing rules apply based on the prefixes advertised:

- AWS evaluates the longest prefix length first. AWS recommends advertising
  more specific routes using multiple Direct Connect virtual interfaces if the
  desired routing paths are meant for active/passive connections. See [Influencing Traffic over Hybrid Networks using Longest Prefix
  Match](https://aws.amazon.com/blogs/networking-and-content-delivery/influencing-traffic-over-hybrid-networks-using-longest-prefix-match/ "https://aws.amazon.com/blogs/networking-and-content-delivery/influencing-traffic-over-hybrid-networks-using-longest-prefix-match/") for more information.
- Local preference is the BGP attribute recommended to use when desired routing
  paths are meant for active/passive connections and the prefix lengths advertised
  are the same. This value is set per Region to prefer [AWS Direct Connect Locations](https://aws.amazon.com/directconnect/locations/ "https://aws.amazon.com/directconnect/locations/") that have the same
  associated AWS Region using the `7224:7200`—Medium local
  preference community value. Where the local Region is not
  associated with the Direct Connect location, it is set to a lower value. This
  applies only if no local preference community tags are assigned.
- AS_PATH length can be used to determine the routing path when the prefix
  length and local preference are the same.
- Multi-Exit Discriminator (MED) can be used to determine the routing path when
  prefix length, local preference, and AS_PATH are the same. AWS does not
  recommend using MED values given their lower priority in evaluation.
- AWS uses equal-cost multi-path (ECMP) routing across multiple transit or
  private virtual interfaces when prefixes have the same AS_PATH length and BGP
  attributes. The ASNs in the AS_PATH of the prefixes do not need to match.

### Private virtual interface and transit

virtual interface BGP communities

When an AWS Region routes traffic to on-premises locations via Direct Connect
private or transit virtual interfaces, the associated AWS Region of the Direct
Connect location influences the ability to use ECMP. AWS Regions prefer Direct
Connect locations in the same associated AWS Region by default. See [AWS Direct Connect Locations](https://aws.amazon.com/directconnect/locations/ "https://aws.amazon.com/directconnect/locations/") to identify the associated
AWS Region of any Direct Connect location.

When there are no local preference community tags applied, Direct Connect supports
ECMP over private or transit virtual interfaces for prefixes with the same, AS_PATH
length, and MED value over two or more paths in the following scenarios:

- The AWS Region sending traffic has two or more virtual interface paths
  from locations in the same associated AWS Region, whether in the same or
  different colocation facilities.
- The AWS Region sending traffic has two or more virtual interface paths
  from locations not in the same Region.

Fore more information, see [How do I set up an Active/Active or Active/Passive Direct Connect connection to
AWS from a private or transit virtual interface?](https://repost.aws/knowledge-center/direct-connect-private-transit-interface/ "https://repost.aws/knowledge-center/direct-connect-private-transit-interface/")

###### Note

This has no effect on ECMP to an AWS Region from on-premises locations.

To control route preferences, Direct Connect supports local preference BGP
community tags for private virtual interfaces and transit virtual interfaces.

#### Local preference BGP

communities

You can use local preference BGP community tags to achieve load balancing and
route preference for incoming traffic to your network. For each prefix that you
advertise over a BGP session, you can apply a community tag to indicate the
priority of the associated path for returning traffic.

The following local preference BGP community tags are supported:

- `7224:7100`—Low preference
- `7224:7200`—Medium preference
- `7224:7300`—High preference

Local preference BGP community tags are mutually exclusive. To load balance
traffic across multiple Direct Connect connections (active/active) homed to the same
or different AWS Regions, apply the same community tag; for example,
`7224:7200` (medium preference) across the prefixes for the
connections. If one of the connections fails, traffic will be then load balance
using ECMP across the remaining active connections regardless of their home
Region associations . To support failover across multiple
Direct Connect connections (active/passive), apply a community tag with a higher
preference to the prefixes for the primary or active virtual interface and a
lower preference to the prefixes for the backup or passive virtual interface.
For example, set the BGP community tags for your primary or active virtual
interfaces to `7224:7300` (high preference) and
`7224:7100` (low preference) for your passive virtual
interfaces.

Local preference BGP community tags are evaluated before any AS_PATH
attribute, and are evaluated in order from lowest to highest preference (where
highest preference is preferred).
