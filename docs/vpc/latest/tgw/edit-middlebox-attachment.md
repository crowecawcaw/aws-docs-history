# Remove AWS Transit Gateway metering policy middlebox

attachments

By default, metering costs are attributed to the middlebox attachment owner. However, you can modify these assignments to ensure costs are properly allocated to the actual source or destination of the traffic. You can add or remove up to 10 total middlebox attachment for a metering policy.

## Remove middlebox attachments using the console

Use the Amazon VPC console to remove middlebox attachments from your metering policy configuration.

###### To remove middlebox attachments

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Transit gateways**, **Metering policies**.
3. Select the metering policy that you want to modify.
4. Choose the **Middlebox attachments** tab.
5. Select up to 10 middlebox attachments to remove from the metering policy.
6. Choose **Remove**.
7. When prompted, you can update your chosen middlebox attachments to remove. Traffic through removed attachments will be metered to the middlebox attachment owner.
8. Choose **Remove middlebox attachments**.

## Remove middlebox attachments using the AWS CLI

Use the **modify-transit-gateway-metering-policy** command to remove attachments.

Before you begin, ensure you have the following required parameters:

- `--transit-gateway-metering-policy-id` - The ID of the existing metering policy
- `--remove-middle-box-attachment-ids` - One or more attachment IDs to remove from the policy (for removing attachments)

###### To remove middlebox attachments from an existing policy using the AWS CLI

1. In the following example, **modify-transit-gateway-metering-policy** is used to remove two specific middlebox attachments from an existing metering policy. The command removes only the specified attachment IDs while preserving the remaining attachments:

```
aws ec2 modify-transit-gateway-metering-policy \
    --transit-gateway-metering-policy-id tgw-mp-0123456789abcdefg \
    --remove-middle-box-attachment-ids tgw-attach-0456789012345abcd tgw-attach-0fedcba0987654321
```

2. In the following example response, the JSON output shows the updated policy configuration with the specified attachments removed and the remaining attachments still active:

```
{
    "TransitGatewayMeteringPolicy": {
        "TransitGatewayMeteringPolicyId": "tgw-mp-0123456789abcdefg",
        "TransitGatewayId": "tgw-0ecec6433f4bfe55a",
        "MiddleBoxAttachmentIds": [
            "tgw-attach-0bdc681c211bf71f3",
            "tgw-attach-0987654321fedcba0"
        ],
        "State": "available",
        "UpdateEffectiveAt": "2024-09-05T16:00:00.000Z"
    }
}
```
