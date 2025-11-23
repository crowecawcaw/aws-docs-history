# Delete an AWS Transit Gateway metering policy

Delete metering policies when they are no longer required for your transit gateway cost allocation strategy. Deleting a policy reverts cost allocation to the default sender-based model where data processing and data transfer charges are allocated to the account that owns the source attachment. All policy entries associated with the deleted metering policy are also removed.

## Delete a metering policy using the console

Use the console to remove metering policies that are no longer needed.

###### To delete a metering policy using the console

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Metering policies**.
3. Select the policy you want to delete by choosing its policy ID.
4. Choose **Actions**, and then **Delete**.
5. Confirm the deletion by typing `delete` in the confirmation dialog.
6. Choose **Delete**.

###### Important

Deleting a metering policy is irreversible. All policy entries and configuration settings will be permanently removed, and cost allocation will revert to the default sender-based model.

## Delete a metering policy using the AWS CLI

Use the **delete-transit-gateway-metering-policy** command to delete metering policies programmatically.

Requirements:

- Transit gateway owner permissions

Required parameters:

- `--transit-gateway-metering-policy-id` - The ID of the metering policy to delete

###### To view and delete metering policies using the AWS CLI

1. (Optional) View existing metering policies using the **describe-transit-gateway-metering-policies** command to see current configuration settings:

```
aws ec2 describe-transit-gateway-metering-policies
```

This command returns all metering policies in your account, showing their current state and configuration. 2. Delete a metering policy using the **delete-transit-gateway-metering-policy** command to permanently remove the policy:

```
aws ec2 delete-transit-gateway-metering-policy \
    --transit-gateway-metering-policy-id tgw-mp-042d444564d4b2da7
```

This command permanently removes the specified metering policy and all associated entries. Cost allocation will revert to the default sender-based model for all future traffic flows. This change also takes 2 billing hours to take effect. 3. The command returns the following output when the policy is successfully deleted:

```
{
    "TransitGatewayMeteringPolicy": {
        "TransitGatewayMeteringPolicyId": "tgw-mp-042d444564d4b2da7",
        "TransitGatewayId": "tgw-07a5946195a67dc47",
        "MiddleboxAttachmentIds":  ["tgw-attach-0123456789abcdef0",
        "tgw-attach-0123456789abcdef1"],
        "State": "deleting",
        "UpdateEffectiveAt": "2025-11-05T21:00:00.000Z"
    }
}
```

The response confirms the policy is being deleted with a `deleting` state while the removal is processed across the transit gateway infrastructure.
