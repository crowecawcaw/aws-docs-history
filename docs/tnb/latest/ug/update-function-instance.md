

# Update a function instance in AWS TNB
<a name="update-function-instance"></a>

After a network instance is instantiated, you can update a function package in the network instance.

------
#### [ Console ]

**To update a function instance using the console**

1. Open the AWS TNB console at [https://console.aws.amazon.com/tnb/](https://console.aws.amazon.com/tnb/).

1. In the navigation pane, choose **Networks**.

1. Select the network instance. You can update a network instance only if its state is `Instantiated`.

   The network instance page appears.

1. From the **Functions** tab, select the function instance to update.

1. Choose **Update**.

1. Enter your update overrides.

1. Choose **Update**.

------
#### [ AWS CLI ]

**Use the CLI to update a function instance**  
Use the [update-sol-network-instance](https://docs.aws.amazon.com/cli/latest/reference/tnb/update-sol-network-instance.html) command with the `MODIFY_VNF_INFORMATION` update type to update a function instance in a network instance.

```
aws tnb update-sol-network-instance --ns-instance-id {{^ni-[a-f0-9]{17}$}} --update-type MODIFY_VNF_INFORMATION --modify-vnf-info ...
```

------