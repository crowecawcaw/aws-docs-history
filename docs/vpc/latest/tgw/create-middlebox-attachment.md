

# Add AWS Transit Gateway metering policy middlebox attachments
<a name="create-middlebox-attachment"></a>

You can add middlebox attachments to integrate network appliances into your Transit Gateway metering policy. This allows you to route specific traffic through security appliances, load balancers, or other network functions while maintaining granular cost allocation control.

**Important**  
Ensure middlebox appliances are properly configured and accessible
Test traffic routing before applying to production workloads
Monitor middlebox performance to avoid introducing latency
Configure appropriate failover behavior for high availability

## Add middlebox attachments using the console
<a name="create-middlebox-console"></a>

**To add a middlebox attachment entry**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Metering policies**.

1. Select the metering policy ID link to view its details.

1. Choose the **Middlebox attachments** tab.

1. Choose **Add**.

1. When prompted, Select the middlebox attachment IDs that should be treated as middleboxes for specialized billing. You can select up to 10 middlebox attachments.

1. Choose **Add middlebox attachments** to save the configuration.

## Add middlebox attachments using the AWS CLI
<a name="create-middlebox-cli"></a>

Use the **modify-transit-gateway-metering-policy** command to add attachments.

Before you begin, ensure you have the following required parameters:
+ `--transit-gateway-metering-policy-id` - The ID of the existing metering policy
+ `--add-middle-box-attachment-ids` - One or more attachment IDs to add to the policy (for adding attachments)

**To add middlebox attachments to an existing policy using the AWS CLI**

1. In the following example, **modify-transit-gateway-metering-policy** is used to add four middlebox attachments to an existing metering policy. The command adds the specified attachment IDs to the existing list without removing current attachments:

   ```
   aws ec2 modify-transit-gateway-metering-policy \
       --transit-gateway-metering-policy-id tgw-mp-0123456789abcdefg \
       --add-middle-box-attachment-ids tgw-attach-0bdc681c211bf71f3 tgw-attach-0987654321fedcba0 tgw-attach-0456789012345abcd tgw-attach-0fedcba0987654321
   ```

1. In the following example response, the JSON output shows the updated policy configuration with all four middlebox attachments now included:

   ```
   {
       "TransitGatewayMeteringPolicy": {
           "TransitGatewayMeteringPolicyId": "tgw-mp-0123456789abcdefg",
           "TransitGatewayId": "tgw-0ecec6433f4bfe55a",
           "MiddleBoxAttachmentIds": [
               "tgw-attach-0bdc681c211bf71f3",
               "tgw-attach-0987654321fedcba0",
               "tgw-attach-0456789012345abcd",
               "tgw-attach-0fedcba0987654321"
           ],
           "State": "available",
           "UpdateEffectiveAt": "2024-09-05T16:00:00.000Z"
       }
   }
   ```