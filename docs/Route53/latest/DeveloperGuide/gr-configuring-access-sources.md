

# Configuring access sources and access source rules

Access sources control which clients can query your DNS infrastructure and which protocols they can use. You define an access source in one of two ways: by an IP address range (CIDR) or by an AWS Cloud WAN (Cloud WAN) core network segment. You create access source rules that specify the IP ranges or segments that can query your DNS infrastructure and the protocols they can use.

A segment-based access source is available only after you connect the Cloud WAN core network to your global resolver with a core network endpoint. For more information about core network endpoints and segment-based access sources, see [Connecting a global resolver to a core network](gr-core-network-endpoints.md) and [Using a Cloud WAN segment as an access source](#gr-segment-based-access-sources).

## Creating access source rules
<a name="gr-creating-access-source-rules"></a>

Follow these steps to create an access source rule that allows specific IP ranges to query your DNS infrastructure.

1. Open the Route 53 Global Resolver console and navigate to your DNS view.

1. In the **Access source** section, choose **Create access source rule**.

1. For **Rule name**, enter a descriptive name that identifies the purpose of this rule, such as `office-network` or `vpn-users`.

1. For **IP address type**, choose **IPV4** or **IPV6**.

1. For **CIDR block**, specify the IP addresses that should have access. You can use CIDR notation for IP ranges: `203.0.113.0/24` or `2001:db8::/112`, or individual IP addresses: `203.0.113.5/32` or `2001:db8::1/128`.

1. For **Protocol**, select the DNS protocols this rule applies to:
   + **Do53** - Standard DNS over UDP/TCP (port 53)
   + **DoT** - DNS over TLS (port 853)
   + **DoH** - DNS over HTTPS (port 443)

1. Choose **Create access source rule**.

Client devices from the specified IP ranges can now query your DNS infrastructure using the selected protocols.

## Using a Cloud WAN segment as an access source
<a name="gr-segment-based-access-sources"></a>

Instead of an IP address range, you can define an access source by an AWS Cloud WAN (Cloud WAN) core network segment. Clients that reach the global resolver from that segment are authorized the same way as clients that match an IP-based access source.

Before you can use a segment as an access source, you must connect the Cloud WAN core network to your global resolver with a core network endpoint. After you connect the core network, its segments become available as access sources in the AWS Regions where your global resolver runs. For the steps to connect a core network and the full details of core network endpoints, see [Connecting a global resolver to a core network](gr-core-network-endpoints.md).

Follow these steps to create an access source rule that uses a Cloud WAN segment.

1. Open the Route 53 Global Resolver console and navigate to your DNS view.

1. In the **Access source** section, choose **Create access source rule**.

1. For **Rule name**, enter a descriptive name that identifies the purpose of this rule, such as `cloudwan-production`.

1. For **IP address type**, choose **NONE**. A segment-based access source isn't defined by an IP range, so you don't choose IPV4 or IPV6.

1. For **Segment**, select the Cloud WAN core network segment that should have access instead of entering a CIDR block. Only segments from core networks that you have connected with a core network endpoint are available.

1. For **Protocol**, select the DNS protocols this rule applies to:
   + **Do53** - Standard DNS over UDP/TCP (port 53)
   + **DoT** - DNS over TLS (port 853)
   + **DoH** - DNS over HTTPS (port 443)

1. Choose **Create access source rule**.

Client devices that reach the global resolver from the selected segment can now query your DNS infrastructure using the selected protocols. If you delete the core network endpoint for that core network, its segments are no longer available as access sources.

## Understanding rule evaluation and priority
<a name="gr-understanding-rule-evaluation"></a>

Route 53 Global Resolver evaluates access source rules when identifying the correct view to use.
+ Rules are processed from most specific to least specific IP ranges, where the most-specific matching rule takes precedence.
+ If no rules match, the request is denied by default.

Test your access source configuration by querying from different IP addresses to make sure the rules work as expected.