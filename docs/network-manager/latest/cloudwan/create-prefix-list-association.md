# Create a AWS Cloud WAN prefix list association

## Create a prefix list association using the console

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. Under **Connectivity**, choose **Global networks**.
3. On the **Global networks** page, choose the global network ID.
4. Under **Core network** in the navigation pane, choose **Prefix list associations**.
5. Choose **Create prefix list association**.
6. For **Prefix list ARN**, enter the ARN of the prefix list
   you want to create an association for.
7. For **Core Network Id** field, enter the id of the core network
   you want to associate a prefix list to.
8. In the **Prefix list alias** field, enter a name you want
   associated with the prefix list ARN.
9. Choose **Create prefix list association**.

## Create a prefix list association using the AWS CLI

Use the **create-core-network-prefix-list-association** command.

Required parameters:

- `--core-network-id` - The ID of your Cloud WAN core network
- `--prefix-list-arn` - The ARN of the prefix list to associate
- `--prefix-list-alias` - A human-readable alias for the prefix list association

The following command creates a prefix list association for the specified core network and prefix list:

```
aws networkmanager create-core-network-prefix-list-association \
    --core-network-id core-network-0123456789abcdef0 \
    --prefix-list-arn arn:aws:ec2:us-west-2:123456789012:prefix-list/pl-0123456789abcdef0 \
    --prefix-list-alias "corporate-networks"
```

The command returns the following output:

```
{
    "CoreNetworkPrefixListAssociation": {
        "CoreNetworkId": "core-network-0123456789abcdef0",
        "PrefixListArn": "arn:aws:ec2:us-west-2:123456789012:prefix-list/pl-0123456789abcdef0",
        "PrefixListAlias": "corporate-networks"
    }
}
```

## Create a prefix list association using the API

Use the [CreateCoreNetworkPrefixListAssociation](../../../networkmanager/latest/APIReference/API_CreateCoreNetworkPrefixListAssociation.md "../../../networkmanager/latest/APIReference/API_CreateCoreNetworkPrefixListAssociation.md") operation.

Required parameters:

- `CoreNetworkId` - The ID of your Cloud WAN core network
- `PrefixListArn` - The ARN of the prefix list to associate
- `PrefixListAlias` - A human-readable alias for the prefix list association

The following HTTP request creates a prefix list association:

```
POST /core-networks/core-network-0123456789abcdef0/prefix-list-arn/arn:aws:ec2:us-west-2:123456789012:prefix-list/pl-0123456789abcdef0/prefix-list-alias/corporate-networks HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: NetworkManager.CreateCoreNetworkPrefixListAssociation

{
    "CoreNetworkId": "core-network-0123456789abcdef0",
    "PrefixListArn": "arn:aws:ec2:us-west-2:123456789012:prefix-list/pl-0123456789abcdef0",
    "PrefixListAlias": "corporate-networks"
}
```

The API returns the following response:

```
HTTP/1.1 200 OK
Content-Type: application/x-amz-json-1.1

{
    "CoreNetworkPrefixListAssociation": {
        "CoreNetworkId": "core-network-0123456789abcdef0",
        "PrefixListArn": "arn:aws:ec2:us-west-2:123456789012:prefix-list/pl-0123456789abcdef0",
        "PrefixListAlias": "corporate-networks"
    }
}
```
