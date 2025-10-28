# Create a network instance using AWS TNB

You create a network instance after creating a network package. After you create a
network instance, instantiate it.

Console

###### To create a network instance using the console

1. Open the AWS TNB console at [https://console.aws.amazon.com/tnb/](https://console.aws.amazon.com/tnb/ "https://console.aws.amazon.com/tnb/").
2. In the navigation pane, choose **Networks**.
3. Choose **Create network instance**.
4. Enter a name and description for the instance and then choose
   **Next**.
5. Select the network package, verify the details, and choose
   **Next**.
6. Choose **Create network instance**.

The new network instance appears on the **Networks**
page. Next, instantiate this network instance.

AWS CLI

###### To create a network instance using the AWS CLI

- Use the [create-sol-network-instance](../../../cli/latest/reference/tnb/create-sol-network-instance.md "../../../cli/latest/reference/tnb/create-sol-network-instance.md") command to create a network
  instance.

```
aws tnb create-sol-network-instance --nsd-info-id `^np-[a-f0-9]{17}$` --ns-name "`SampleNs`" --ns-description "`Sample`"
```

Next, instantiate this network instance.
