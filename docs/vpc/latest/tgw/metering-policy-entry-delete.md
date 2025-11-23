# Delete an AWS Transit Gateway metering policy entry

Delete metering policy entries when specific cost allocation rules are no longer required for your network traffic flows. Entry deletion helps simplify policy management by removing outdated or unnecessary rules while maintaining the overall policy structure. When you delete an entry, traffic that previously matched the deleted rule will be evaluated against remaining entries in rule number order, or fall back to the default policy behavior if no other entries match.

Before deleting entries, consider the impact on current billing arrangements and traffic flows. Once deleted, the change takes upto 2 billing hours to get effective and cannot be undone, so coordinate changes with affected account owners and finance teams. Review remaining entries to ensure proper traffic coverage and billing allocation after the deletion. The rule evaluation order for remaining entries stays unchanged, maintaining predictable cost allocation behavior for continuing traffic flows.

###### Important

- Deletion is irreversible
- Traffic previously matching this entry will be re-evaluated against remaining entries
- Review remaining entries to ensure proper traffic coverage

## Delete a metering policy entry using the console

Use the console to remove policy entries through an intuitive interface that provides confirmation dialogs to prevent accidental deletions.

###### To delete a policy entry using the console

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Metering policies**.
3. Select the metering policy containing the entry you want to delete.
4. Select the entry you want to remove and choose **Delete**.
5. In the confirmation dialog, review the entry details and type `delete` to confirm the removal.
6. Choose **Delete** to permanently remove the entry.

## Delete a metering policy entry using the AWS CLI

Use the **delete-transit-gateway-metering-policy-entry** command to remove policy entries programmatically.

Requirements:

- Transit gateway owner permissions
- Valid metering policy ID and entry rule number

Required parameters:

- `--transit-gateway-metering-policy-id` - The ID of the metering policy
- `--policy-rule-number` - The rule number of the entry to delete

###### To view and delete policy entries using the AWS CLI

1. (Optional) View existing policy entries using the **get-transit-gateway-metering-policy-entries** command to see current configuration settings:

```
aws ec2 get-transit-gateway-metering-policy-entries \
    --transit-gateway-metering-policy-id tgw-mp-0123456789abcdefg
```

This command returns all entries for the specified policy, showing their rule numbers, matching criteria, and metered accounts. 2. Delete a policy entry using the **delete-transit-gateway-metering-policy-entry** command to permanently remove the entry:

```
aws ec2 delete-transit-gateway-metering-policy-entry \
    --transit-gateway-metering-policy-id tgw-mp-0123456789abcdefg \
    --policy-rule-number 100
```

This command permanently removes the specified entry from the policy. Traffic that previously matched this entry will be immediately re-evaluated against remaining entries or fall back to the default policy behavior. 3. The command returns the following output when the entry is successfully deleted:

```
{
    "TransitGatewayMeteringPolicyEntry": [
        {
            "PolicyRuleNumber": 100,
            "MeteredAccount": "destination-attachment-owner",
            "UpdateEffectiveAt": "2024-01-01T01:00:00+00:00",
            "state": "deleted",
            "MeteringPolicyRule": {
                "DestinationTransitGatewayAttachmentType": "vpc"
            }
        }
}
```

The response confirms the entry is being deleted with a "deleted" state while the removal is processed across the transit gateway infrastructure.
