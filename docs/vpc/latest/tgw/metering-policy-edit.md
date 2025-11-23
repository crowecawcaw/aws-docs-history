# Edit an AWS Transit Gateway metering policy

Edit existing metering policies to modify middlebox attachment configurations. Policy modifications take effect at the next billing hour and apply to all future traffic flows through your transit gateway.

## Edit a metering policy using the console

Use the console to modify existing metering policy settings for your transit gateway.

###### To edit an existing metering policy using the console

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Metering policies**.
3. Select the metering policy you want to modify by choosing its policy ID
4. Modify the available policy settings under **Actions**. Console only allow add and remove of Middle box attachments.
   1. **Middlebox attachments** - Add or remove transit gateway attachments that should be treated as middleboxes for specialized billing.

## Edit a metering policy using the AWS CLI

Use the **modify-transit-gateway-metering-policy** command to view and modify metering policies.

Required parameters for modify operations:

- `--transit-gateway-metering-policy-id` - The ID of the metering policy to modify
- `--add-middle-box-attachment-ids` or `--remove-middle-box-attachment-ids` - Supported transit gateway attachment Ids to add or remove from the policy as middlebox

###### To view and edit metering policies using the AWS CLI

1. (Optional) View existing metering policies using the **describe-transit-gateway-metering-policies** command to see current configuration settings:

```
aws ec2 describe-transit-gateway-metering-policies
```

This command returns all metering policies in your account, showing their current state, and attachments enabled as middlebox for each of the metering policy. 2. Modify a metering policy using the **modify-transit-gateway-metering-policy** command to update configuration options:

```
aws ec2 modify-transit-gateway-metering-policy \
    --transit-gateway-metering-policy-id tgw-mp-042d444564d4b2da7 \
    --add-middle-box-attachment-ids tgw-attach-0123456789abcdef1  \
    --remove-middle-box-attachment-ids tgw-attach-0abc123def456789a
```

This command modifies a metering policy by adding and/or removing middlebox attachments. 3. The command returns the following output when the policy is successfully modified:

```
{
    "TransitGatewayMeteringPolicy": {
        "TransitGatewayMeteringPolicyId": "tgw-mp-042d444564d4b2da7",
        "TransitGatewayId": "tgw-07a5946195a67dc47",
        "MiddleboxAttachmentIds":  ["tgw-attach-0123456789abcdef0",
        "tgw-attach-0123456789abcdef1"],
        "State": "modifying",
        "UpdateEffectiveAt": "2025-11-05T21:00:00.000Z"
    }
}
```

The changes can take up to two billing hours to take effect.
