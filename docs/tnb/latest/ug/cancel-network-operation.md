# Cancel a AWS TNB network operation

Learn how to cancel a network operation.

Console

###### To cancel a network operation using the console

1. Open the AWS TNB console at [https://console.aws.amazon.com/tnb/](https://console.aws.amazon.com/tnb/ "https://console.aws.amazon.com/tnb/").
2. In the navigation pane, choose **Networks**.
3. Select the ID of the network to open its details page.
4. On the **Deployments** tab, choose the Network Operation.
5. Choose **Cancel operation**.

AWS CLI

###### To cancel a network operation using the AWS CLI

Use the [cancel-sol-network-operation](../../../cli/latest/reference/tnb/cancel-sol-network-operation.md "../../../cli/latest/reference/tnb/cancel-sol-network-operation.md") command to cancel a network operation.

```
aws tnb cancel-sol-network-operation --ns-lcm-op-occ-id `^no-[a-f0-9]{17}$`
```
