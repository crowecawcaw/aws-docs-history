

# Configuring access sources and access source rules
<a name="gr-configuring-access-sources"></a>

Access sources control client access based on IP addresses. You create access source rules that specify which IP ranges can query your DNS infrastructure and which protocols they can use.

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

## Understanding rule evaluation and priority
<a name="gr-understanding-rule-evaluation"></a>

Route 53 Global Resolver evaluates access source rules when identifying the correct view to use.
+ Rules are processed from most specific to least specific IP ranges, where the most-specific matching rule takes precedence.
+ If no rules match, the request is denied by default.

Test your access source configuration by querying from different IP addresses to make sure the rules work as expected.