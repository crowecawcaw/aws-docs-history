

# Modify a policy table entry in AWS Transit Gateway
<a name="tgw-policy-tables-entry-modify"></a>

`ModifyTransitGatewayPolicyTableEntry` is a **PATCH-style update**. Only the fields you explicitly include in the request are modified. Fields you omit are left unchanged. They are **not** reset to Any (`*`).

**Important**  
To change a field back to match any value (Any), you must explicitly pass `*` for that field. Omitting the field has no effect on its current value. For example, if a rule has `"SourceCidrBlock": "10.0.0.0/16"` and you want it to match any source IP, you must pass `"SourceCidrBlock": "*"`. Omitting `SourceCidrBlock` leaves the `10.0.0.0/16` restriction in place.

At least one of `--target-route-table-id` or `--policy-rule` must be included in the request.

**To modify a policy table entry using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Transit Gateways**, choose **Transit Gateway Policy Tables**.

1. In **Transit Gateway Policy Tables**, select the policy table.

1. Choose the **Entries** tab.

1. Select the entry you want to modify. System entries (rule number `*`) are read-only and cannot be selected for editing.

1. Choose **Modify entry**.

1. The **Rule number** is displayed as read-only — it identifies the entry and cannot be changed. To change a rule number, delete the entry and recreate it with the new number.

1. Update only the fields you want to change. All other fields are pre-populated with current values. CIDR fields provide an autosuggest dropdown with common prefixes.

   1. To reset a field to Any (match any), clear the field — the console substitutes `*` for any empty field. Leaving it as-is retains the current value.

1. Choose **Save changes**.

The console returns the fully merged entry, reflecting both updated and retained field values.

**To modify a policy table entry using the AWS CLI**  
Use the [modify-transit-gateway-policy-table-entry](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-transit-gateway-policy-table-entry.html) command.

```
aws ec2 modify-transit-gateway-policy-table-entry \
    --transit-gateway-policy-table-id tgw-ptb-0ca78a549EXAMPLE \
    --policy-rule-number 100 \
    --policy-rule '{"SourceCidrBlock":"11.0.0.0/16","Protocol":"17"}' \
    --target-route-table-id tgw-rtb-0a823edbdeEXAMPLE
```

The response returns the fully merged entry. Only `SourceCidrBlock`, `Protocol`, and `TargetRouteTableId` were updated — `SourcePortRange`, `DestinationCidrBlock`, and `DestinationPortRange` retain their previous values unchanged:

```
{
    "TransitGatewayPolicyTableEntry": {
        "PolicyRuleNumber": "100",
        "PolicyRule": {
            "SourceCidrBlock": "11.0.0.0/16",
            "SourcePortRange": "1024-65535",
            "DestinationCidrBlock": "192.168.0.0/16",
            "DestinationPortRange": "443",
            "Protocol": "17"
        },
        "TargetRouteTableId": "tgw-rtb-0a823edbdeEXAMPLE",
        "State": "active"
    }
}
```

**Example: Reset a field to Any (match any)**  
To remove the destination port restriction set in the example above and allow any destination port, explicitly pass `*` for `DestinationPortRange`. Omitting the field would leave `443` in place.

```
aws ec2 modify-transit-gateway-policy-table-entry \
    --transit-gateway-policy-table-id tgw-ptb-0ca78a549EXAMPLE \
    --policy-rule-number 100 \
    --policy-rule '{"DestinationPortRange":"*"}'
```

```
{
    "TransitGatewayPolicyTableEntry": {
        "PolicyRuleNumber": "100",
        "PolicyRule": {
            "SourceCidrBlock": "11.0.0.0/16",
            "SourcePortRange": "1024-65535",
            "DestinationCidrBlock": "192.168.0.0/16",
            "DestinationPortRange": "*",
            "Protocol": "17"
        },
        "TargetRouteTableId": "tgw-rtb-0a823edbdeEXAMPLE",
        "State": "active"
    }
}
```