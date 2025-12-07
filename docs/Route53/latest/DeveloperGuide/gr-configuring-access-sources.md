# Configuring access sources and access source

rules

Access sources control client access based on IP addresses. You create access source rules
that specify which IP ranges can query your DNS infrastructure and which protocols they can
use.

## Creating access source rules

Follow these steps to create an access source rule that allows specific IP ranges to query
your DNS infrastructure.

1. Open the Route 53 Global Resolver console and navigate to your DNS view.
2. In the **Access source** section, choose **Create access source rule**.
3. For **Name**, enter a descriptive name that identifies the
   purpose of this rule, such as `office-network` or `vpn-users`.
4. For **IP address range**, specify the IP addresses that
   should have access. You can use CIDR notation for IP ranges: `192.168.1.0/24` or
   individual IP addresses: `203.0.113.5/32`.
5. For **Protocol**, select the DNS protocols this rule applies
   to:
   - **Do53** - Standard DNS over UDP/TCP (port 53)
   - **DoT** - DNS over TLS (port 853)
   - **DoH** - DNS over HTTPS (port 443)

6. Choose **Create access source rule**.

Client devices from the specified IP ranges can now
query your DNS infrastructure using the selected protocols.

## Understanding rule evaluation and priority

Route 53 Global Resolver evaluates access source rules when identifying the correct view to use.

- Rules are processed from most specific to least specific IP ranges, where the most-specific matching rule takes precedence.
- If no rules match, the request is denied by default.

Test your access source configuration by querying from different IP addresses to ensure the
rules work as expected.
