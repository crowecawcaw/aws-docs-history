# Update a function instance in AWS TNB

After a network instance is instantiated, you can update a function package in the
network instance.

Console

###### To update a function instance using the console

1. Open the AWS TNB console at [https://console.aws.amazon.com/tnb/](https://console.aws.amazon.com/tnb/ "https://console.aws.amazon.com/tnb/").
2. In the navigation pane, choose **Networks**.
3. Select the network instance. You can update a network instance only if
   its state is `Instantiated`.

The network instance page appears. 4. From the **Functions** tab, select the function instance
to update. 5. Choose **Update**. 6. Enter your update overrides. 7. Choose **Update**.

AWS CLI

###### Use the CLI to update a function instance

Use the [update-sol-network-instance](../../../cli/latest/reference/tnb/update-sol-network-instance.md "../../../cli/latest/reference/tnb/update-sol-network-instance.md") command with the
`MODIFY_VNF_INFORMATION` update type to update a function
instance in a network instance.

```
aws tnb update-sol-network-instance --ns-instance-id `^ni-[a-f0-9]{17}$` --update-type MODIFY_VNF_INFORMATION --modify-vnf-info ...
```
