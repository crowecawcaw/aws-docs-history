# Delete a function package from AWS TNB

Learn how to delete a function package from the AWS TNB network functions catalog. To delete a function package, the package must
be in a disabled state.

Console

###### To delete a function package using the console

1. Open the AWS TNB console at [https://console.aws.amazon.com/tnb/](https://console.aws.amazon.com/tnb/ "https://console.aws.amazon.com/tnb/").
2. In the navigation pane, choose **Function
   packages**.
3. Use the search box to find the function package.
4. Choose a function package.
5. Choose **Actions**, **Disable**.
6. Choose **Actions**, **Delete**.

AWS CLI

###### To delete a function package using the AWS CLI

1. Use the [update-sol-function-package](../../../cli/latest/reference/tnb/update-sol-function-package.md "../../../cli/latest/reference/tnb/update-sol-function-package.md") command to disable a function
   package.

```
aws tnb update-sol-function-package --vnf-pkg-id `^fp-[a-f0-9]{17}$` ---operational-state DISABLED
```

2. Use the [delete-sol-function-package](../../../cli/latest/reference/tnb/delete-sol-function-package.md "../../../cli/latest/reference/tnb/delete-sol-function-package.md") command to delete a function
   package.

```
aws tnb delete-sol-function-package \
--vnf-pkg-id `^fp-[a-f0-9]{17}$` \
--endpoint-url "`https://tnb.us-west-2.amazonaws.com`" \
--region `us-west-2`
```
