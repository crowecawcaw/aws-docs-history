

# Modify an IPAM pool allocation
<a name="modify-alloc-ipam"></a>

You can modify the description of an IPAM pool allocation using the console or the AWS CLI. Refer to the [modify-ipam-pool-allocation](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-ipam-pool-allocation.html) documentation for more API details. 

------
#### [ AWS Management Console ]

**To modify an IPAM pool allocation**

1. Open the IPAM console at [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/). 

1. In the navigation pane, choose **Pools**.

1. By default, the default private scope is selected. If you don't want to use the default private scope, from the dropdown menu at the top of the content pane, choose the scope you want to use. For more information about scopes, see [How IPAM works](how-it-works-ipam.md).

1. In the content pane, choose the pool that contains the allocation you want to modify.

1. Choose the **Allocations** tab.

1. Select the allocation and choose **Actions**, **Modify allocation**.

1. Modify the description.
**Note**  
To remove the description, leave the field blank.

1. Choose **Save**.

------
#### [ Command line ]

The commands in this section link to the *AWS CLI Command Reference*. The documentation provides detailed descriptions of the options that you can use when you run the commands.

Use the following AWS CLI commands to modify an IPAM pool allocation:

1. Get the allocation ID: [get-ipam-pool-allocations](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-ipam-pool-allocations.html)

1. Modify the allocation description: [modify-ipam-pool-allocation](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-ipam-pool-allocation.html)

   ```
   aws ec2 modify-ipam-pool-allocation --ipam-pool-allocation-id {{ipam-pool-alloc-0e6186d73999e1f12}} --description "{{Updated description}}"
   ```

**Note**  
To remove the description, pass a null value. To manage tags on an allocation, use the [create-tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-tags.html) and [delete-tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-tags.html) commands.

------

To release an allocation, see [Release an allocation](release-alloc-ipam.md).