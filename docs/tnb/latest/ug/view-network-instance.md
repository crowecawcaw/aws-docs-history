

# View a network instance in AWS TNB
<a name="view-network-instance"></a>

Learn how to view a network instance.

------
#### [ Console ]

**To view a network instance using the console**

1. Open the AWS TNB console at [https://console.aws.amazon.com/tnb/](https://console.aws.amazon.com/tnb/).

1. In the navigation pane, choose **Network instances**.

1. Use the search box to find the network instance.

------
#### [ AWS CLI ]

**To view a network instance using the AWS CLI**

1. Use the [list-sol-network-instances](https://docs.aws.amazon.com/cli/latest/reference/tnb/list-sol-network-instances.html) command to list your network instances.

   ```
   aws tnb list-sol-network-instances
   ```

1. Use the [get-sol-network-instance](https://docs.aws.amazon.com/cli/latest/reference/tnb/get-sol-network-instance.html) command to view details about a specific network instance.

   ```
   aws tnb get-sol-network-instance --ns-instance-id {{^ni-[a-f0-9]{17}$}}
   ```

------