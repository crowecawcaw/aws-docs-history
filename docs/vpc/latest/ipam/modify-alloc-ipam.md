# Modify an IPAM pool allocation

You can modify the description of an IPAM pool allocation using the console or
the AWS CLI. Refer to the [modify-ipam-pool-allocation](../../../cli/latest/reference/ec2/modify-ipam-pool-allocation.md "../../../cli/latest/reference/ec2/modify-ipam-pool-allocation.md") documentation for more API details.

AWS Management Console

###### To modify an IPAM pool allocation

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Pools**.
3. By default, the default private scope is selected. If you don't want
   to use the default private scope, from the dropdown menu at the top of
   the content pane, choose the scope you want to use. For more information
   about scopes, see [How IPAM works](how-it-works-ipam.md "how-it-works-ipam.md").
4. In the content pane, choose the pool that contains the allocation you
   want to modify.
5. Choose the **Allocations** tab.
6. Select the allocation and choose **Actions**,
   **Modify allocation**.
7. Modify the description.

###### Note

To remove the description, leave the field blank. 8. Choose **Save**.

Command line
The commands in this section link to the _AWS CLI Command Reference_.
The documentation provides detailed descriptions of the options that you can use
when you run the commands.

Use the following AWS CLI commands to modify an IPAM pool allocation:

1. Get the allocation ID: [get-ipam-pool-allocations](../../../cli/latest/reference/ec2/get-ipam-pool-allocations.md "../../../cli/latest/reference/ec2/get-ipam-pool-allocations.md")
2. Modify the allocation description: [modify-ipam-pool-allocation](../../../cli/latest/reference/ec2/modify-ipam-pool-allocation.md "../../../cli/latest/reference/ec2/modify-ipam-pool-allocation.md")

```
aws ec2 modify-ipam-pool-allocation --ipam-pool-allocation-id `ipam-pool-alloc-0e6186d73999e1f12` --description "`Updated description`"
```

###### Note

To remove the description, pass a null value. To manage tags on an allocation, use the [create-tags](../../../cli/latest/reference/ec2/create-tags.md "../../../cli/latest/reference/ec2/create-tags.md") and [delete-tags](../../../cli/latest/reference/ec2/delete-tags.md "../../../cli/latest/reference/ec2/delete-tags.md") commands.

To release an allocation, see [Release an allocation](release-alloc-ipam.md "release-alloc-ipam.md").
