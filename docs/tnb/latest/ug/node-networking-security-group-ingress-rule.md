# AWS.Networking.SecurityGroupIngressRule

AWS TNB supports security group ingress rules to automate the provisioning of Amazon EC2
Security Group Ingress Rules which can be attached to AWS.Networking.SecurityGroup. Note
that you must provide a cidr_ip/source_security_group/source_prefix_list as the source for
ingress traffic.

## Syntax

```
AWS.Networking.SecurityGroupIngressRule
  properties:
    ip_protocol: String
    from_port: Integer
    to_port: Integer
    description: String
    source_prefix_list: String
    cidr_ip: String
    cidr_ipv6: String
  requirements:
    security_group: String
    source_security_group: String
```

## Properties

`cidr_ip`

The IPv4 address range in CIDR format. You must specify a CIDR range that
allows ingress traffic.

Required: No

Type: String

`cidr_ipv6`

The IPv6 address range in CIDR format, for ingress traffic. You must specify
a source security group (`source_security_group` or
`source_prefix_list`) or a CIDR range (`cidr_ip` or
`cidr_ipv6`).

Required: No

Type: String

`description`

The description of an ingress (inbound) security group rule. You can use up
to 255 characters to describe the rule.

Required: No

Type: String

`source_prefix_list`

The prefix list ID of an existing Amazon VPC managed prefix list. This is the
source from which node group instances associated with the security group will
be allowed to receive traffic from. For more information on managed prefix
lists, see [Managed prefix
lists](../../../vpc/latest/userguide/managed-prefix-lists.md "../../../vpc/latest/userguide/managed-prefix-lists.md") in the _Amazon VPC User Guide_.

Required: No

Type: String

`from_port`

If the protocol is TCP or UDP, this is the start of the port range. If the
protocol is ICMP or ICMPv6, this is the type number. A value of -1 indicates
all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify
all ICMP/ICMPv6 codes.

Required: No

Type: Integer

`ip_protocol`

The IP protocol name (tcp, udp, icmp, icmpv6) or protocol number. Use -1 to
specify all protocols. When authorizing security group rules, specifying -1 or
a protocol number other than tcp, udp, icmp, or icmpv6 allows traffic on all
ports, regardless of any port range you specify. For tcp, udp, and icmp, you
must specify a port range. For icmpv6, the port range is optional; if you omit
the port range, traffic for all types and codes is allowed.

Required: Yes

Type: String

`to_port`

If the protocol is TCP or UDP, this is the end of the port range. If the
protocol is ICMP or ICMPv6, this is the code. A value of -1 indicates all
ICMP/ICMPv6 codes. If you specify all ICMP/ICMPv6 types, you must specify all
ICMP/ICMPv6 codes.

Required: No

Type: Integer

## Requirements

`security_group`

The ID of the security group to which this rule is to be added.

Required: Yes

Type: String

`source_security_group`

The ID or TOSCA reference of the source security group from which ingress
traffic is to be allowed.

Required: No

Type: String

## Example

```
SampleSecurityGroupIngressRule:
      type: tosca.nodes.AWS.Networking.SecurityGroupIngressRule
      properties:
        ip_protocol: `"tcp"`
        from_port: `8000`
        to_port: `9000`
        description: `"Ingress Rule for free5GC cluster on IPv6"`
        cidr_ipv6: "`2600`:`1f14`:`3758`:`ca00`::/`64`"
      requirements:
        security_group: `SampleSecurityGroup1`
        source_security_group: `SampleSecurityGroup2`
```
