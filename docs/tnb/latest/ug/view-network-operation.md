# View a AWS TNB network operation

View the details of a network operation, including the tasks involved in the network operation and the status of the tasks.

Console

###### To view a network operation using the console

1. Open the AWS TNB console at [https://console.aws.amazon.com/tnb/](https://console.aws.amazon.com/tnb/ "https://console.aws.amazon.com/tnb/").
2. In the navigation pane, choose **Network instances**.
3. Use the search box to find the network instance.
4. On the **Deployments** tab, choose the network operation.

AWS CLI

###### To view a network operation using the AWS CLI

1. Use the [list-sol-network-operations](../../../cli/latest/reference/tnb/list-sol-network-operations.md "../../../cli/latest/reference/tnb/list-sol-network-operations.md") command to list all network
   operations.

```
aws tnb list-sol-network-operations
```

2. Use the [get-sol-network-operation](../../../cli/latest/reference/tnb/get-sol-network-operation.md "../../../cli/latest/reference/tnb/get-sol-network-operation.md") command to view details about a network operation.

```
aws tnb get-sol-network-operation --ns-lcm-op-occ-id `^no-[a-f0-9]{17}$`
```
