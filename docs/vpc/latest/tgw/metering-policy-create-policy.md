# Create an AWS Transit Gateway metering policy

To enable metering policies, you must create a metering policy for your transit gateway and configure policy entries that define how metering usage is allocated. The metering policy establishes the framework and default settings, while policy entries contain the specific rules that determine which accounts are metered based on traffic characteristics.

Metering policy entries function as ordered rules that are applied sequentially from lowest to highest rule number for traffic flowing through your transit gateway. Each entry defines matching criteria such as source and destination attachment types, CIDR blocks, protocols, and port ranges, along with the account that should be metered for matching traffic. When a traffic flow matches multiple entries, the entry with the lowest rule number takes precedence. If no entries match a particular flow, the default metered account specified in the policy is charged.

After creating a policy, you'll need to add policy entries to implement your cost allocation logic. For the steps to create a metering policy entry, see [Create a metering policy entry](create-metering-policy-entry.md "create-metering-policy-entry.md").

## Create a metering policy using the console

Create a policy to define flexible cost allocation rules for transit gateway data usage. By default, all flows are metered to the source attachment owner. Create entries to bill specific network flows to different accounts.

###### To create a metering policy

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Metering policies**.
3. Choose **Create metering policy**.
4. For **Transit gateway ID** choose the transit gateway you'd like to create metering policy for.
5. (Optional) For **Middlebox attachment IDs**, choose one or more middlebox attachment. By default, data usage is metered to the middlebox owner. Middlebox attachment support enables metering policy to be applied for traffic traversing middlebox attachments. Additional attachments can be added later.
6. (Optional) In the **Tags** section, add tags to help you identify and organize your metering policy:
   1. Choose **Add new tag**.
   2. Enter a tag **Key** and optionally a tag **Value**.
   3. Choose **Add new tag** to add additional tags, or skip to the next step. You can add up to 50 tags.

7. Choose **Create transit gateway metering policy**.

###### Note

The default metered account is the source attachment owner, and after creating a metering policy, you can add entries that define which account gets charged based on traffic flow properties, noting that the default policy entry (which is the last entry) cannot be modified or deleted like other policy entries.

## Create a metering policy using the AWS CLI

A metering policy defines the default cost allocation behavior and global settings for
your transit gateway. Use the [create-transit-gateway-metering-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-metering-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-metering-policy.html").

Required parameters:

- `--transit-gateway-id` - The ID of the transit gateway to create the policy for

Optional parameters:

- `--middle-box-attachment-ids` - Supported transit gateway attachment Ids to add to the policy as middlebox
- `--tag-specifications` - tags for metering policy

###### To create a metering policy using the AWS CLI

1. Run the **create-transit-gateway-metering-policy** command to create a new metering policy with optional middlebox attachments.

```
aws ec2 create-transit-gateway-metering-policy \
    --transit-gateway-id tgw-07a5946195a67dc47 \
    --middle-box-attachment-ids \
    tgw-attach-0123456789abcdef0 \
    tgw-attach-0abc123def456789a \
    --tag-specifications \
    '[{ "ResourceType": "transit-gateway-metering-policy", \
    "Tags": [ { "Key": "Env", "Value": "Prod" } ] }]'
```

This command creates a metering policy for the specified transit gateway with provided middlebox attachments and tags. 2. The command returns the following output when the policy is successfully created:

```
{
    "TransitGatewayMeteringPolicy": {
        "TransitGatewayMeteringPolicyId": "tgw-mp-042d444564d4b2da7",
        "TransitGatewayId": "tgw-07a5946195a67dc47",
        "MiddleboxAttachmentIds":  ["tgw-attach-0123456789abcdef0",
        "tgw-attach-0abc123def456789a"],
        "State": "pending",
        "UpdateEffectiveAt": "2025-11-05T21:00:00.000Z",
        "Tags": [{"Key": "Env","Value": "Prod"}]
    }
}
```

Note the metering policy ID returned in the response for use in subsequent commands. **describe-transit-gateway-metering-policies** command can be used to get metering policy associated with transit gateway.
