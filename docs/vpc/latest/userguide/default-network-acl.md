# Default network ACL for a VPC

Your virtual private cloud (VPC) automatically comes with a default network ACL.
A default network ACL is configured to allow all traffic to flow in and out of the
subnets with which it is associated. Each network ACL also includes rules where the
rule number is an asterisk (\*). These rules ensure that if a packet doesn't match
any of the other numbered rules, it's denied.

You can modify a default network ACL by adding rules or removing the default
numbered rules. You can't delete a rule where the rule number is an asterisk.

###### Default inbound rules

The following table shows the default inbound rules for a default network ACL.
The rules for IPv6 are added only if you create the VPC with an associated IPv6
CIDR block or associate an IPv6 CIDR block with the VPC. However, if you've
modified the inbound rules of a default network ACL, we do not add the rule that
allows all inbound IPv6 traffic when you associate an IPv6 block with the VPC.

| Rule # | Type             | Protocol | Port range | Source    | Allow/Deny |
| ------ | ---------------- | -------- | ---------- | --------- | ---------- |
| 100    | All IPv4 traffic | All      | All        | 0.0.0.0/0 | ALLOW      |
| 101    | All IPv6 traffic | All      | All        | ::/0      | ALLOW      |
| \*     | All traffic      | All      | All        | 0.0.0.0/0 | DENY       |
| \*     | All IPv6 traffic | All      | All        | ::/0      | DENY       |

###### Default outbound rules

The following table shows the default outbound rules for a default network ACL. The rules
for IPv6 are added only if you create the VPC with an associated IPv6 CIDR block or associate
an IPv6 CIDR block with the VPC. However, if you've modified the outbound rules of a default
network ACL, we do not add the rule that allows all outbound IPv6 traffic when you associate an
IPv6 block with the VPC.

| Rule # | Type             | Protocol | Port range | Destination | Allow/Deny |
| ------ | ---------------- | -------- | ---------- | ----------- | ---------- |
| 100    | All traffic      | All      | All        | 0.0.0.0/0   | ALLOW      |
| 101    | All IPv6 traffic | All      | All        | ::/0        | ALLOW      |
| \*     | All traffic      | All      | All        | 0.0.0.0/0   | DENY       |
| \*     | All IPv6 traffic | All      | All        | ::/0        | DENY       |
