

# View transit gateway policy tables in AWS Transit Gateway
<a name="tgw-policy-tables-view"></a>

You can view your transit gateway policy tables and their entries.

## View policy tables
<a name="tgw-policy-tables-view-tables"></a>

**To view transit gateway policy tables using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Transit Gateways**, choose **Transit Gateway Policy Tables**.

1. To filter by transit gateway, use the search bar and filter on **Transit gateway ID**.

1. The list shows each policy table's **Transit gateway policy table ID**, **Transit gateway ID**, and **State**.

1. Select a policy table to view its details, associations, and entries on the detail page.

To track your entry usage against the per-transit gateway limit, use the Service Quotas console. See [Quotas](transit-gateway-quotas.md) for details.

**To view transit gateway policy tables using the AWS CLI**  
To list all policy tables on your account, use the [describe-transit-gateway-policy-tables](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-transit-gateway-policy-tables.html) command.

```
aws ec2 describe-transit-gateway-policy-tables \
    --filters "Name=transit-gateway-id,Values=tgw-0bc994abffEXAMPLE"
```

Example response:

```
{
    "TransitGatewayPolicyTables": [
        {
            "TransitGatewayPolicyTableId": "tgw-ptb-0ca78a549EXAMPLE",
            "TransitGatewayId": "tgw-0bc994abffEXAMPLE",
            "State": "available",
            "CreationTime": "2026-01-01T00:00:00.000Z",
            "Tags": []
        }
    ]
}
```

## View policy table entries
<a name="tgw-policy-tables-view-entries"></a>

**To view policy table entries using the console**

1. In **Transit Gateway Policy Tables**, select the policy table.

1. Choose the **Entries** tab.

1. The **Entries** tab displays all entries with the following columns: **Rule number**, **State**, **Target route table**, **Source CIDR block**, **Source port**, **Destination CIDR block**, **Destination port**, and **Protocol**. System-managed entries display `*` as their rule number.

1. To filter entries, use the search bar. You can filter by rule number, target route table, source CIDR, destination CIDR, source port, destination port, or protocol.

To check total usage against the per-transit gateway limit, use the Service Quotas console. See [Quotas](transit-gateway-quotas.md) for details.

**To view policy table entries using the AWS CLI**  
Use the [get-transit-gateway-policy-table-entries](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-transit-gateway-policy-table-entries.html) command.

```
aws ec2 get-transit-gateway-policy-table-entries \
    --transit-gateway-policy-table-id tgw-ptb-0ca78a549EXAMPLE
```

Example response:

```
{
    "TransitGatewayPolicyTableEntries": [
        {
            "PolicyRuleNumber": "100",
            "PolicyRule": {
                "SourceCidrBlock": "10.100.0.0/16",
                "SourcePortRange": "*",
                "DestinationCidrBlock": "*",
                "DestinationPortRange": "443",
                "Protocol": "6"
            },
            "TargetRouteTableId": "tgw-rtb-0ca78a549EXAMPLE",
            "State": "active"
        },
        {
            "PolicyRuleNumber": "*",
            "PolicyRule": {
                "SourceCidrBlock": "*",
                "SourcePortRange": "*",
                "DestinationCidrBlock": "*",
                "DestinationPortRange": "*",
                "Protocol": "*",
                "MetaData": {
                    "MetaDataKey": "TgwRouteTable",
                    "MetaDataValue": "tgw-rtb-0ca62a892EXAMPLE"
                }
            },
            "TargetRouteTableId": "tgw-rtb-0ca62a892EXAMPLE",
            "State": "active"
        }
    ]
}
```

**Supported filters**  
The following filters are supported for `GetTransitGatewayPolicyTableEntries`.


**Supported filters**  

| Filter | Description | 
| --- | --- | 
| policy-rule-number | Filter by rule number | 
| target-route-table-id | Filter by target route table ID | 
| policy-rule.source-ip | Filter by source CIDR block | 
| policy-rule.destination-ip | Filter by destination CIDR block | 
| policy-rule.source-port | Filter by source port range | 
| policy-rule.destination-port | Filter by destination port range | 
| policy-rule.protocol | Filter by protocol | 
| policy-rule.meta-data.key | Filter by metadata key | 
| policy-rule.meta-data.value | Filter by metadata value | 