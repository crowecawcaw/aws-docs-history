

# Delete a network package from AWS TNB
<a name="delete-network-package"></a>

Learn how to delete a network package from the AWS TNB network service catalog. To delete a network package, the package must be in a disable state.

------
#### [ Console ]

**To delete a network package using the console**

1. Open the AWS TNB console at [https://console.aws.amazon.com/tnb/](https://console.aws.amazon.com/tnb/).

1. In the navigation pane, choose **Network packages**.

1. Use the search box to find the network package

1. Choose network package

1. Choose **Actions**, **Disable**.

1. Choose **Actions**, **Delete**.

------
#### [ AWS CLI ]

**To delete a network package using the AWS CLI**

1. Use the [update-sol-network-package](https://docs.aws.amazon.com/cli/latest/reference/tnb/update-sol-network-package.html) command to disable a network package.

   ```
   aws tnb update-sol-network-package --nsd-info-id {{^np-[a-f0-9]{17}$}} --nsd-operational-state DISABLED
   ```

1. Use the [delete-sol-network-package](https://docs.aws.amazon.com/cli/latest/reference/tnb/delete-sol-network-package.html) command to delete a network package.

   ```
   aws tnb delete-sol-network-package \
   --nsd-info-id {{^np-[a-f0-9]{17}$}} \
   --endpoint-url "{{https://tnb.us-west-2.amazonaws.com}}" \
   --region {{us-west-2}}
   ```

------