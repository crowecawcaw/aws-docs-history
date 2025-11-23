# Delete an AWS Cloud WAN prefix list

association

###### Note

Before you can delete a core network prefix list association you must remove any prefix list alias that is referred to in the associated core network policy before the delete call will work.

## Delete a prefix list

association using the console

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global networks**.
3. On the **Global networks** page, choose the global network ID.
4. Under **Core network** in the navigation pane, choose **Prefix list associations**.
5. Select the prefix list association you want to delete.
6. Choose **Delete**.
7. Confirm the deletion by choosing **Delete**.

## Delete a prefix list

association using the AWS CLI

Use the **delete-core-network-prefix-list-association** command.

Required parameters:

- `--core-network-id` - The ID of your Cloud WAN core network
- `--prefix-list-arn` - The ARN of the prefix list association to delete

The following command deletes a prefix list association for the specified core network and prefix list:

```
aws networkmanager delete-core-network-prefix-list-association \
    --core-network-id core-network-0123456789abcdef0 \
    --prefix-list-arn arn:aws:ec2:us-west-2:123456789012:prefix-list/pl-0123456789abcdef0
```

The command returns the following output:

```
{
    "CoreNetworkPrefixListAssociation": {
        "CoreNetworkId": "core-network-0123456789abcdef0",
        "PrefixListArn": "arn:aws:ec2:us-west-2:123456789012:prefix-list/pl-0123456789abcdef0"
    }
}
```

## Delete a prefix list

association using the API

Use the [DeleteCoreNetworkPrefixListAssociation](../../../networkmanager/latest/APIReference/API_DeleteCoreNetworkPrefixListAssociation.md "../../../networkmanager/latest/APIReference/API_DeleteCoreNetworkPrefixListAssociation.md") operation.

Required parameters:

- `CoreNetworkId` - The ID of your Cloud WAN core network
- `PrefixListArn` - The ARN of the prefix list to delete

The following HTTP request deletes a prefix list association:

```
DELETE /core-networks/core-network-0123456789abcdef0/prefix-list-arn/arn:aws:ec2:us-west-2:123456789012:prefix-list/pl-0123456789abcdef0 HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: NetworkManager.DeleteCoreNetworkPrefixListAssociation
```

The API returns the following response:

```
HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1

{
    "CoreNetworkPrefixListAssociation": {
        "CoreNetworkId": "core-network-0123456789abcdef0",
        "PrefixListArn": "arn:aws:ec2:us-west-2:123456789012:prefix-list/pl-0123456789abcdef0"
    }
}
```
