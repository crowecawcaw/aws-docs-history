# View a network instance in AWS TNB

Learn how to view a network instance.

Console

###### To view a network instance using the console

1. Open the AWS TNB console at [https://console.aws.amazon.com/tnb/](https://console.aws.amazon.com/tnb/ "https://console.aws.amazon.com/tnb/").
2. In the navigation pane, choose **Network
   instances**.
3. Use the search box to find the network instance.

AWS CLI

###### To view a network instance using the AWS CLI

1. Use the [list-sol-network-instances](../../../cli/latest/reference/tnb/list-sol-network-instances.md "../../../cli/latest/reference/tnb/list-sol-network-instances.md") command to list your network
   instances.

```
aws tnb list-sol-network-instances
```

2. Use the [get-sol-network-instance](../../../cli/latest/reference/tnb/get-sol-network-instance.md "../../../cli/latest/reference/tnb/get-sol-network-instance.md") command to view details about a
   specific network instance.

```
aws tnb get-sol-network-instance --ns-instance-id `^ni-[a-f0-9]{17}$`
```
