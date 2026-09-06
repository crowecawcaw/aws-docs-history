

# Create a policy table entry in AWS Transit Gateway
<a name="tgw-policy-tables-entry-create"></a>

Add one or more rules to the policy table. Each rule specifies match criteria and a target route table. All match attributes are optional; omitting an attribute defaults it to Any (`*`).

**To create a policy table entry using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In **Transit Gateway Policy Tables**, select the policy table you created.

1. Choose the **Entries** tab, and then choose **Create entry**.

1. Under **Entry details**, configure the required fields.

   1. **Rule number** — enter an integer from 1 to 50,000. Rules are evaluated lowest-number-first. Leave gaps between numbers (for example, 100, 110, 120) so you can insert rules later without renumbering.

   1. **Target transit gateway route table** — select the transit gateway route table to use for matching traffic.

1. Under **Rule conditions**, configure the optional match criteria. Leave any field empty to match all values. All specified conditions must match for the rule to apply.

   1. **Source CIDR block** — IPv4 or IPv6 CIDR (for example, `10.0.0.0/16`). Leave blank for all.

   1. **Destination CIDR block** — IPv4 or IPv6 CIDR. Leave blank for all.

   1. **Protocol** — select a supported protocol. Supported values: `1` (ICMPv4), `6` (TCP), `17` (UDP), `47` (GRE), or Any to match all protocols (`*`). Port range fields are only available when Protocol is TCP (`6`) or UDP (`17`). For all other protocols — ICMPv4, GRE, or Any — port ranges are automatically set to Any (`*`) and cannot be configured.

   1. **Source port range** — single port (`443`) or range (`1024-65535`). Leave blank for all. Available only when Protocol is TCP (`6`) or UDP (`17`).

   1. **Destination port range** — single port (`443`) or range (`1024-65535`). Leave blank for all. Available only when Protocol is TCP (`6`) or UDP (`17`).

1. Choose **Create entry**.

**To create a policy table entry using the AWS CLI**  
Use the [create-transit-gateway-policy-table-entry](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-transit-gateway-policy-table-entry.html) command. Replace the policy table ID, rule number, policy rule values, and route table ID with your values.

```
aws ec2 create-transit-gateway-policy-table-entry \
    --transit-gateway-policy-table-id tgw-ptb-0ca78a549EXAMPLE \
    --policy-rule-number 100 \
    --policy-rule '{"SourceCidrBlock": "10.100.0.0/16", "Protocol": "6", "DestinationPortRange": "443"}' \
    --target-route-table-id tgw-rtb-0a823edbdeEXAMPLE
```

## Policy rule match attributes
<a name="tgw-policy-tables-entry-create-attributes"></a>

The following table describes the policy rule match attributes.


**Policy rule match attributes**  

| Attribute | Description | Valid values | Default | 
| --- | --- | --- | --- | 
| SourceCidrBlock | Source IP address or CIDR block | IPv4 or IPv6 CIDR (for example, 10.0.0.0/16), or omit for any | \* (any) | 
| SourcePortRange | Source port or range. Only evaluated when Protocol is TCP (6) or UDP (17). Automatically set to \* for all other protocols. | Single port (443) or range (1024-65535); valid range 0–65535, start ≤ end | \* (any) | 
| DestinationCidrBlock | Destination IP address or CIDR block | IPv4 or IPv6 CIDR, or omit for any | \* (any) | 
| DestinationPortRange | Destination port or range. Only evaluated when Protocol is TCP (6) or UDP (17). Automatically set to \* for all other protocols. | Single port or range; valid range 0–65535, start ≤ end | \* (any) | 
| Protocol | IANA protocol number. Determines whether port range fields are evaluated. | 1 (ICMPv4), 6 (TCP), 17 (UDP), 47 (GRE), or \* for any. Port ranges are only supported for TCP and UDP. | \* (any) | 

Both IPv4 and IPv6 CIDR formats are supported.