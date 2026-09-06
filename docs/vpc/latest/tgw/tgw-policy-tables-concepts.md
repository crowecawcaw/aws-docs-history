

# Policy table concepts in AWS Transit Gateway
<a name="tgw-policy-tables-concepts"></a>

This topic describes the key concepts for transit gateway policy tables and Policy-Based Routing (PBR).

## Policy tables and policy rules
<a name="tgw-policy-tables-concepts-rules"></a>

A **policy table** contains an ordered set of rules. Each rule specifies:
+ **Match criteria** — the packet attributes used to classify traffic (source IP CIDR, destination IP CIDR, source port, destination port, and protocol).
+ **Target route table** — the transit gateway route table used to forward traffic that matches the rule criteria.

When traffic arrives on an attachment associated with a policy table, the transit gateway evaluates each rule in order and applies the first matching rule's target route table. If no rule matches, the packet is dropped (implicit deny).

A transit gateway attachment can be associated with either a **policy table** or a **route table**, but not both. By default, all attachments are associated with the default route table.

## Rule evaluation order
<a name="tgw-policy-tables-concepts-order"></a>

Rules in a policy table are evaluated in **ascending numeric order**, starting at rule number 1. The first rule that matches the incoming traffic is applied. No subsequent rules are evaluated after a match. Because evaluation stops at the first match, rule order matters:
+ Place more specific rules (narrow IP ranges, specific ports) at lower rule numbers.
+ Place broader or catch-all rules at higher rule numbers.

We recommend that you leave gaps between rule numbers (for example, 100, 110, 120) rather than using consecutive values, so that you can insert rules later without renumbering.

## System and customer policy table entries
<a name="tgw-policy-tables-concepts-entry-types"></a>

Policy tables support two types of entries: **customer-managed** and **system-managed**. Understanding both types is important for predicting how your traffic is evaluated and routed.

**Customer-managed entries**  
Customer-managed entries are rules that you define to route traffic based on packet attributes. You create these entries using the `CreateTransitGatewayPolicyTableEntry` API or the AWS Management Console.

Each customer-managed entry specifies:
+ **Rule number** — determines evaluation order. Rules are evaluated in ascending order. The lowest-numbered matching rule is applied.
+ **Match conditions** — a combination of source CIDR, destination CIDR, protocol, source port, and destination port. All fields are optional. Omitted fields default to Any (`*`).
+ **Target route table** — the transit gateway route table to which matching traffic is forwarded.

If no customer-managed rule matches and no system-managed rule matches, the traffic is dropped (implicit deny).

**Example** — you have two VPCs connected to a transit gateway: a production VPC and a development VPC. You want to route HTTP traffic destined for `10.0.0.0/16` through a security inspection route table, while all other traffic uses a default route table.


**Example customer-managed entries**  

| Rule number | Source CIDR | Destination CIDR | Protocol | Source port | Dest. port | Target route table | 
| --- | --- | --- | --- | --- | --- | --- | 
| 10 | 0.0.0.0/0 | 10.0.0.0/16 | TCP | 1024-65535 | 80 | tgw-rtb-inspection | 
| 20 | 0.0.0.0/0 | 0.0.0.0/0 | All | All | All | tgw-rtb-default | 

In this configuration, HTTP traffic to `10.0.0.0/16` matches rule 10 and is routed through the inspection route table. All other traffic matches rule 20 and uses the default route table.

**System-managed entries**  
System-managed entries are created and maintained automatically by AWS to support AWS-internal routing functions, such as AWS Cloud WAN dynamic routing and network segment isolation. You cannot create, modify, or delete system-managed entries. System-managed entries appear in your policy table when you use features like AWS Cloud WAN that require segment-level traffic isolation on transit gateway-to-Cloud WAN peering attachments.

How system-managed entries affect your traffic:
+ **Precedence** — system-managed entries are always evaluated before customer-managed entries. If a system-managed entry matches incoming traffic, it is applied regardless of any customer-managed rules you have configured.
+ **Visibility** — system-managed entries are visible in the `GetTransitGatewayPolicyTableEntries` API response and in the console, where their rule number displays as `*`.
+ **No action required** — these entries are managed entirely by AWS and do not require configuration on your part.

**Example** — you use AWS Cloud WAN with two routing segments, production and development. AWS automatically creates system-managed entries on the policy table associated with your transit gateway-to-Cloud WAN peering attachment to ensure traffic stays within its assigned segment. If you also add customer-managed rules to the same policy table, the system-managed segmentation rules take effect first. Your customer-managed rules apply only to traffic that does not match a system-managed entry.


**Comparison of entry types**  

| Created by | Rule number | Evaluated | Can be modified | 
| --- | --- | --- | --- | 
| AWS (for example, transit gateway-to-Cloud WAN peering attachments) | \* | First, before all customer entries | No | 
| You | 1–50,000 | After system entries, in ascending rule number order | Yes | 

Both entry types are returned together by `GetTransitGatewayPolicyTableEntries` and displayed together in the AWS Management Console.

## How policy table evaluation works
<a name="tgw-policy-tables-concepts-evaluation"></a>

When traffic enters a transit gateway attachment that is associated with a policy table, evaluation proceeds as follows:

1. System-managed entries are evaluated first. If a system-managed entry matches the traffic, it is applied and evaluation stops.

1. Customer-managed entries are evaluated next, in ascending rule number order. The first matching rule is applied and evaluation stops.

1. Implicit deny — if no entry matches, the traffic is dropped.

## Best practices
<a name="tgw-policy-tables-concepts-best-practices"></a>
+ **Leave gaps between rule numbers.** Use increments of 10 or 100 (for example, 10, 20, 30 or 100, 200, 300) so you can insert new rules later without renumbering existing entries.
+ **Put the most specific rules first.** Place narrower match conditions at lower rule numbers so they are evaluated before broader catch-all rules. A broad rule at a low number will shadow more specific rules at higher numbers.
+ **Always include a catch-all rule.** Because traffic is dropped if no rule matches, add a default rule at a high rule number if you want unmatched traffic to reach a route table rather than be silently dropped.
+ **Configure protocol before port ranges.** Protocol selection determines whether port range fields are active. Port ranges are only supported for TCP (`6`) and UDP (`17`). For ICMPv4 (`1`), GRE (`47`), or Any (`*`), port ranges are automatically set to Any (`*`).
+ **Account for system-managed entries.** If your policy table includes system-managed entries (for example, from AWS Cloud WAN), your customer-managed rules apply only to traffic that does not match a system-managed entry. Review all entries using `GetTransitGatewayPolicyTableEntries` to confirm your expected evaluation order.
+ **Verify your configuration with the API.** After making changes, use `GetTransitGatewayPolicyTableEntries` to view all entries in both entry types and confirm that rule numbers and match conditions are correct before routing live traffic.