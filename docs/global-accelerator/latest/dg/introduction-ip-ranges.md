# Location and IP address ranges of Global Accelerator Edge servers

For a list of Global Accelerator edge server locations, see _Global Edge Network_
on the [AWS Global Accelerator features](https://aws.amazon.com/global-accelerator/features/ "https://aws.amazon.com/global-accelerator/features/") page.

AWS publishes its current IP address ranges in JSON format. To view the current ranges,
download [ip-ranges.json](https://ip-ranges.amazonaws.com/ip-ranges.json "https://ip-ranges.amazonaws.com/ip-ranges.json"). For more information, see [AWS IP address ranges](../../../general/latest/gr/Welcome.md#aws-ip-ranges "../../../general/latest/gr/Welcome.md#aws-ip-ranges") in the
_Amazon Web Services General Reference_.

Before you work with the `ip-ranges.json` file, first review the following information:

- To find the IP address ranges that are associated with AWS Global Accelerator Edge servers, search
  `ip-ranges.json` for the following string:

`"service": "GLOBALACCELERATOR"`

- Global Accelerator entries that include `"region": "GLOBAL"` refer to the static IP addresses that are allocated to accelerators.
  If you want to filter for traffic through your accelerator that comes from points of presence (POPs) in one area, filter for entries
  that include a specific geographical area, such as `us-*` or `eu-*`. So, for example, if you filter for
  `us-*`, you will see only traffic coming through POPs in the United States (U.S.).
- Global Accelerator supports two ways of routing traffic: using client IP address preservation or using network address translation (NAT).
  The way that traffic is routed determines the client IP address that AWS WAF can apply rules to. When you use client IP address preservation, AWS WAF
  rules target the client IP address—that is, the IP address of the clients who access your service. When you use NAT, AWS WAF
  rules are applied to the global IP addresses that Global Accelerator uses to route traffic.
