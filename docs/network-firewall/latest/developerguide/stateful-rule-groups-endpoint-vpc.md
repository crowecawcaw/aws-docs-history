

# Filtering traffic by firewall endpoint VPC

You can write stateful rules that match traffic based on the firewall endpoint it entered through. To do this, use the `aws_firewall_endpoint_vpc` rule option and name the VPC that contains the endpoint. AWS Network Firewall finds that VPC's endpoints on your firewall and applies the rule to them.

This is useful when your firewall has endpoints in several VPCs through VPC endpoint associations, and those VPCs use overlapping CIDR ranges. In that case, IP addresses alone can't tell the VPCs' traffic apart, but the firewall endpoint can.

For example, VPC A and VPC B both use 10.0.0.0/16. The following rules block SSH from client 10.0.5.17 when its traffic comes through the firewall endpoint in VPC A. They allow it when the traffic comes through the firewall endpoint in VPC B.

```
drop tcp 10.0.5.17/32 any -> $EXTERNAL_NET 22 (aws_firewall_endpoint_vpc:[vpc-0a1b2c3d4e5f60001]; msg:"Block SSH from firewall endpoints in VPC A"; sid:1;)
pass tcp 10.0.5.17/32 any -> $EXTERNAL_NET 22 (aws_firewall_endpoint_vpc:[vpc-0a1b2c3d4e5f60002]; msg:"Allow SSH from firewall endpoints in VPC B"; sid:2;)
```

**Important**  
The `aws_firewall_endpoint_vpc` option matches the VPC that contains the firewall endpoint the traffic entered through. It doesn't match the VPC the traffic came from. Suppose VPC A has no firewall endpoint and sends its traffic through a firewall endpoint in VPC B, for example over VPC peering. That traffic matches vpc-B, not vpc-A. To write rules for VPC A on its own, create a VPC endpoint association in VPC A and route VPC A's traffic through it.

## Key concepts
<a name="w2aac23c23c13c25c13"></a>
+ **Firewall endpoint**: The endpoint that traffic enters the firewall through. A firewall has one primary endpoint per Availability Zone in the VPC where you created it, plus one endpoint for each VPC endpoint association.
+ **Endpoint VPC**: The VPC that contains the firewall endpoint the traffic came through. This is the value that `aws_firewall_endpoint_vpc` takes.
+ **Endpoint VPC compared with source VPC**: The endpoint VPC and the client's VPC can be different. For example, if you use a centralized inspection VPC behind a transit gateway, all spoke VPC traffic enters through the inspection VPC's endpoints. That traffic matches the inspection VPC's ID, not the spoke VPC's ID.
+ **Endpoint VPC filtering compared with context-aware rules**: Context-aware rules describe where traffic comes from or goes to, and they work on firewalls natively attached to a transit gateway. `aws_firewall_endpoint_vpc` describes the firewall endpoint and works on VPC-attached firewalls. These are separate features.

## How it works
<a name="w2aac23c23c13c25c15"></a>

1. You add `aws_firewall_endpoint_vpc:[vpc-id]` to a rule in a stateful rule group, or inline in a firewall policy.

1. When you save the rule group, Network Firewall checks the option's syntax and the rule's size. It doesn't check that the VPCs exist, because a rule group isn't tied to a single firewall and can be shared.

1. When the rule group is deployed to a firewall, Network Firewall finds that firewall's endpoints in the named VPCs in each Availability Zone and applies the rule to them.

1. When the firewall's endpoints change, Network Firewall updates the rule automatically: When an endpoint is added, the rule is updated to include the new endpoint before the endpoint starts carrying traffic (the VPC endpoint association might take a little longer to reach the READY state). When an endpoint is removed, the endpoint stops carrying traffic first, and then the rule is updated.

1. If a named VPC has no endpoint on the firewall in an Availability Zone, the rule isn't deployed in that Availability Zone. The rest of the rule group deploys normally, and no error is returned. The rule never expands to match all traffic. If a rule names several VPCs and only some have endpoints, the rule applies to the endpoints that exist.

## Console support
<a name="w2aac23c23c13c25c17"></a>

There is no new console field for `aws_firewall_endpoint_vpc`. You add it in either of two ways:
+ As a rule option on a standard stateful rule. In the `StatefulRule` `RuleOptions`, set `Keyword` to `aws_firewall_endpoint_vpc` and `Settings` to the bracketed VPC list, for example `["[vpc-0a1b2c3d4e5f60001]"]`.
+ Directly in a Suricata compatible rule string. Put it in `RulesString`, for example:

  ```
  drop tcp any any -> $EXTERNAL_NET 22 (aws_firewall_endpoint_vpc:[vpc-0a1b2c3d4e5f60001]; sid:1;)
  ```

## Where you can use it
<a name="w2aac23c23c13c25c19"></a>

You can use `aws_firewall_endpoint_vpc` in the following places:
+ Stateful rule groups that use Suricata compatible rule strings.
+ Stateful rule groups that use standard stateful rules. Add it as a rule option with the keyword `aws_firewall_endpoint_vpc` and the settings [vpc-id-1,vpc-id-2].
+ Firewall and IPS rule groups in Next Generation firewall policies, both as shareable rule groups and as inline rules in the policy.
+ Rule groups shared through AWS RAM. Each firewall resolves the VPC IDs against its own endpoints.
+ VPC endpoint associations in other accounts. A rule can name a VPC owned by another account if that VPC has an endpoint association on the firewall.
+ NAT/Proxy firewalls. A NAT/Proxy firewall keeps the client's endpoint for proxied traffic, so rules match the client's endpoint VPC. Add the option in stateful rule groups for a Classic Network Firewall policy, or in firewall or IPS rule groups for a Next Generation policy.

You can't use `aws_firewall_endpoint_vpc` in these places:
+ Stateless rule groups or domain list rule groups.
+ Firewalls natively attached to a transit gateway. Use context-aware rules instead.

The option also doesn't support:
+ Negation (`!aws_firewall_endpoint_vpc`).
+ Endpoint IDs (`vpce-...`). The value is always a VPC ID.
+ Targeting a single endpoint in a VPC. The option matches all of that VPC's endpoints on the firewall.

## TLS inspection
<a name="w2aac23c23c13c25c21"></a>

On firewalls that use TLS inspection with VPC endpoint associations, rules that use the `aws_firewall_endpoint_vpc` keyword also match decrypted traffic. This applies to both routed firewalls and NAT/Proxy firewalls. For more information about TLS inspection, see [Inspecting SSL/TLS traffic with TLS inspection configurations in AWS Network Firewall](tls-inspection-configurations.md).

TLS inspection isn't supported with VPC endpoint associations in other accounts, so you can't combine the keyword with TLS inspection for VPCs owned by other accounts.

## Syntax
<a name="w2aac23c23c13c25c23"></a>

```
aws_firewall_endpoint_vpc:[vpc-id-1, vpc-id-2];
```
+ The value is a list of VPC IDs in square brackets. Brackets are required, even for a single VPC.
+ The rule matches traffic through an endpoint in any of the listed VPCs. The option is combined with the rest of the rule using AND logic.
+ You can use the option once in each rule.
+ Each value must be a valid VPC ID: `vpc-` followed by hexadecimal characters. Whitespace around values is ignored, and duplicate values are removed.
+ The option name isn't case sensitive.

### Examples
<a name="w2aac23c23c13c25c23b7"></a>

Suricata compatible rule:

```
drop tls any any -> $EXTERNAL_NET 443 (aws_firewall_endpoint_vpc:[vpc-0a1b2c3d4e5f60001]; tls.sni; content:"example.com"; sid:1;)
```

Several VPCs in one rule:

```
alert http any any -> any any (aws_firewall_endpoint_vpc:[vpc-0a1b2c3d4e5f60001, vpc-0a1b2c3d4e5f60002]; msg:"HTTP from VPC A or B"; sid:2;)
```

Next Generation firewall rule group:

```
drop:flow tcp:all any any -> any 80 (alert; aws_firewall_endpoint_vpc:[vpc-0a1b2c3d4e5f60001]; sid:3;)
```

AWS CLI:

```
aws network-firewall create-rule-group \
    --rule-group-name block-ssh-vpc-a \
    --type STATEFUL \
    --capacity 100 \
    --rules 'drop tcp any any -> $EXTERNAL_NET 22 (aws_firewall_endpoint_vpc:[vpc-0a1b2c3d4e5f60001]; sid:1;)'
```

## High level steps
<a name="w2aac23c23c13c25c25"></a>

1. Create a firewall. Then create a VPC endpoint association in each VPC whose traffic you want to identify separately. The firewall's own VPC already has its primary endpoints. For VPCs in other accounts, first share the firewall through AWS RAM. Then have the other account create the association.

1. Update route tables so that each VPC's traffic goes through its own firewall endpoint.

1. Write rules that use `aws_firewall_endpoint_vpc` with those VPC IDs, in a rule group or inline in the firewall policy.

1. Add the rule group to your firewall policy and associate the policy with the firewall.

## Quotas
<a name="w2aac23c23c13c25c27"></a>


| Limit | Value | 
| --- | --- | 
| aws\_firewall\_endpoint\_vpc options per rule | 1 | 
| Size reserved per option during rule validation | 992 bytes | 

The 992 bytes count toward the existing limits of 8,192 bytes per rule and 2 MB per rules string. Network Firewall reserves this size for every use of the option, even if the named VPCs have few endpoints. Because of this, a very long rule can be rejected for size.

## Considerations
<a name="w2aac23c23c13c25c29"></a>
+ **Endpoint VPC, not client VPC**: The option matches the VPC of the firewall endpoint, not the VPC where the client is.
+ **Rules that can't apply are silent**: If a named VPC has no endpoint on the firewall, or a VPC ID is mistyped, the rule isn't active and you don't get a notification. Check your VPC IDs and endpoint associations carefully.
+ **Shared rule groups**: A shared rule group resolves VPC IDs separately on each firewall where it's used, so it can apply to different endpoints on each firewall.