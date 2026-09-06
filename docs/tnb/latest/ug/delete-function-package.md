

# Delete a function package from AWS TNB
<a name="delete-function-package"></a>

Learn how to delete a function package from the AWS TNB network functions catalog. To delete a function package, the package must be in a disabled state.

------
#### [ Console ]

**To delete a function package using the console**

1. Open the AWS TNB console at [https://console.aws.amazon.com/tnb/](https://console.aws.amazon.com/tnb/).

1. In the navigation pane, choose **Function packages**.

1. Use the search box to find the function package.

1. Choose a function package.

1. Choose **Actions**, **Disable**.

1. Choose **Actions**, **Delete**.

------
#### [ AWS CLI ]

**To delete a function package using the AWS CLI**

1. Use the [update-sol-function-package](https://docs.aws.amazon.com/cli/latest/reference/tnb/update-sol-function-package.html) command to disable a function package.

   ```
   aws tnb update-sol-function-package --vnf-pkg-id {{^fp-[a-f0-9]{17}$}} ---operational-state DISABLED
   ```

1. Use the [delete-sol-function-package](https://docs.aws.amazon.com/cli/latest/reference/tnb/delete-sol-function-package.html) command to delete a function package.

   ```
   aws tnb delete-sol-function-package \
   --vnf-pkg-id {{^fp-[a-f0-9]{17}$}} \
   --endpoint-url "{{https://tnb.us-west-2.amazonaws.com}}" \
   --region {{us-west-2}}
   ```

------