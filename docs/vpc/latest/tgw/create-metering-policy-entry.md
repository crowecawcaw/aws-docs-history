# Create an AWS Transit Gateway metering policy entry

By default, all flows are metered to the source attachment owner. To meter specific flows to different accounts, create individual policy entries that define which account gets charged based on traffic flow properties.

Metering policy entries function as conditional rules that are evaluated in sequential order based on their rule numbers when traffic flows through your transit gateway. Each entry acts as an "if-then" statement: if the traffic matches the specified criteria (such as source attachment type, destination CIDR block, or protocol), then charge the designated account. The system evaluates entries from lowest to highest rule number, and the first matching entry determines the billing account for that traffic flow.

Entries support a wide range of matching criteria including attachment types (VPC, VPN, Direct Connect Gateway), specific attachment IDs, source and destination CIDR blocks, protocol types, and port ranges. You can combine multiple criteria within a single entry to create precise targeting rules. For example, you might create an entry that matches all HTTPS traffic (port 443) from VPC attachments to a specific destination CIDR range and charges those flows to a security team's account. If no entries match a particular traffic flow, the default metered account specified in the parent metering policy is charged, ensuring all traffic is properly billed. Creating an entry takes 2 billing hours to take effect.

###### Important

- Plan rule numbers carefully - Leave gaps (e.g., 10, 20, 30) to allow for future insertions
- Test entries with less specific conditions first before adding more restrictive rules
- Use specific matching conditions to avoid unintended billing

## Create a metering policy entry using the console

A metering policy defines the default cost allocation behavior and global settings for your transit gateway.

###### To create a metering policy entry using the console

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Metering policies**.
3. Select the metering policy ID link to view its details.
4. Choose the **Metering policy entries** tab.
5. Choose **Create metering policy entry**.
6. **Policy rule number** -This should be a unique number (1- 32,766) that determines evaluation order. Lower numbers have higher priority.
7. **Metered account** - Choose one of the following account types to be charged for matching traffic flows:
   1. **Source Attachment Owner**
   2. **Destination Attachment Owner**
   3. **Transit Gateway Attachment Owner**

8. (Optional) Choose **Rule conditions** - These optional conditions define criteria to match specific traffic:
   - **Source attachment type or ID** - Filter by attachment type (VPC, VPN, Direct Connect Gateway, Peering) or ID.
   - **Destination attachment type or ID** - Filter by destination attachment type or ID
   - **Source CIDR block** - Match traffic from specific IP ranges
   - **Destination CIDR block** - Match traffic to specific IP ranges
   - **Source port range** - Match specific source ports
   - **Destination port range** - Match specific destination ports
   - **Protocol** - Filter by protocol for the rule (1, 6, 17, etc.)

9. Choose **Create metering policy entry** to save the configuration.

## Create a metering policy entry using the AWS CLI

Policy entries define specific rules for cost allocation based on traffic characteristics. Rules are evaluated in order from lowest to highest rule number.

Required parameters:

- `--transit-gateway-metering-policy-id` - The ID of the metering policy to add the entry to
- `--policy-rule-number` - A unique number (1-32,766) that determines evaluation order
- `--metered-account` - payer type (source-attachment-owner/ destination-attachment-owner / transit-gateway-owner)

Optional parameters:

These optional parameters that define criteria to match specific traffic:

- `--source-transit-gateway-attachment-id` - The ID of the source transit gateway attachment.
- `--source-transit-gateway-attachment-type` - The type of the source transit gateway attachment.
- `--source-cidr-block` - The source CIDR block for the rule.
- `--source-port-range` - The source port range for the rule.
- `--destination-transit-gateway-attachment-id` - The ID of the destination transit gateway attachment.
- `--destination-transit-gateway-attachment-type` - The type of the destination transit gateway attachment.
- `--destination-cidr-block` - The destination CIDR block for the rule.
- `--destination-port-range` - The destination port range for the rule.
- `--protocol` - The protocol number for the rule

###### To create a metering policy entry using the AWS CLI

1. Use the **create-transit-gateway-metering-policy-entry** command to create a new policy entry that routes VPC traffic to a specific metered account:

```
aws ec2 create-transit-gateway-metering-policy-entry \
    --transit-gateway-metering-policy-id tgw-mp-042d444564d4b2da7 \
    --policy-rule-number 100 \
    --destination-transit-gateway-attachment-type vpc \
    --metered-account destination-attachment-owner
```

This command creates a policy entry with rule number 100 that matches traffic destined for VPC attachments and charges the destination attachment owner for those flows. 2. The command returns the following output when the entry is successfully created:

```
{
    "TransitGatewayMeteringPolicyEntry": {
        "MeteredAccount": "destination-attachment-owner",
        "MeteringPolicyRule": {
            "DestinationTransitGatewayAttachmentType": "vpc"
        },
        "PolicyRuleNumber": 100,
        "State": "available",
        "UpdateEffectiveAt": "2025-11-06T02:00:00.000Z"
    }
}
```

The response confirms the entry was created with a "available" state while it's being activated across the transit gateway infrastructure.
