# Example: Steering traffic to a security appliance in AWS Transit Gateway

The following example steers traffic from a specific internal subnet to a firewall VPC for
inspection, while routing all other traffic directly.

###### Scenario

Consider the following requirements.

- Traffic from `10.1.10.0/24` (sensitive workload subnet) must pass
  through a firewall in a VPC before forwarding.
- All other traffic forwards using the standard route table.

###### Policy table configuration

Configure the policy table with the following entries.

Policy table configuration| Rule # | Entry type | Source CIDR block | Destination CIDR block | Protocol | Source port range | Destination port range | Target route table |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 100 | customer-managed | `10.1.10.0/24` | Any | Any | Any | Any | `tgw-rtb-firewall` |
| 200 | customer-managed | Any | Any | Any | Any | Any | `tgw-rtb-default` |

###### How it works

Traffic is evaluated as follows.

- Traffic from `10.1.10.0/24` arrives on the transit gateway attachment associated
  with the policy table.
- The transit gateway evaluates rule 100 first. The source CIDR matches
  `10.1.10.0/24`, so the traffic is forwarded using route table
  `tgw-rtb-firewall`.
- Route table `tgw-rtb-firewall` contains routes that send traffic to the
  firewall VPC attachment.
- The firewall inspects the traffic and forwards it back to the transit gateway.
- On return, the transit gateway re-evaluates the traffic for onward routing using
  destination-based lookup on the route table associated with the firewall VPC
  attachment.
  All other traffic (not from `10.1.10.0/24`) does not match rule 100 and falls
  through to rule 200, which forwards it using the default route table without
  inspection.

###### AWS CLI commands to create this configuration

Use the following commands to create the policy table, add the rules, and associate
the table with the source VPC attachment.

```
# Create the policy table
aws ec2 create-transit-gateway-policy-table \
    --transit-gateway-id tgw-0bc994abffEXAMPLE

# Add rule 100: steer sensitive traffic to firewall route table
aws ec2 create-transit-gateway-policy-table-entry \
    --transit-gateway-policy-table-id tgw-ptb-0ca78a549EXAMPLE \
    --policy-rule-number 100 \
    --policy-rule '{"SourceCidrBlock": "10.1.10.0/24"}' \
    --target-route-table-id tgw-rtb-firewall

# Add rule 200: catch-all for remaining traffic
aws ec2 create-transit-gateway-policy-table-entry \
    --transit-gateway-policy-table-id tgw-ptb-0ca78a549EXAMPLE \
    --policy-rule-number 200 \
    --policy-rule '{}' \
    --target-route-table-id tgw-rtb-default

# Associate policy table with the source VPC attachment
aws ec2 associate-transit-gateway-policy-table \
    --transit-gateway-policy-table-id tgw-ptb-0ca78a549EXAMPLE \
    --transit-gateway-attachment-id tgw-attach-0def6EXAMPLE
```
