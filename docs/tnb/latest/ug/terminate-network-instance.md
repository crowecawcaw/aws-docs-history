

# Terminate and delete a network instance from AWS TNB
<a name="terminate-network-instance"></a>

To delete a network instance, the instance must be in a terminated state.

------
#### [ Console ]

**To terminate and delete a network instance using the console**

1. Open the AWS TNB console at [https://console.aws.amazon.com/tnb/](https://console.aws.amazon.com/tnb/).

1. In the navigation pane, choose **Networks**.

1. Select the ID of the network instance.

1. Choose **Terminate**.

1. When prompted for confirmation, enter the ID and choose **Terminate**.

1. Refresh to track the status of your network instance.

1. (Optional) Select the network instance and choose **Delete**.

------
#### [ AWS CLI ]

**To terminate and delete a network instance using the AWS CLI**

1. Use the [terminate-sol-network-instance](https://docs.aws.amazon.com/cli/latest/reference/tnb/terminate-sol-network-instance.html) command to terminate a network instance.

   ```
   aws tnb terminate-sol-network-instance --ns-instance-id {{^ni-[a-f0-9]{17}$}}
   ```

1. (Optional) Use the [delete-sol-network-instance](https://docs.aws.amazon.com/cli/latest/reference/tnb/delete-sol-network-instance.html) command to delete a network instance.

   ```
   aws tnb delete-sol-network-instance --ns-instance-id {{^ni-[a-f0-9]{17}$}}
   ```

------