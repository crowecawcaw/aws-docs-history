# View a function package in AWS TNB

Learn how to view the content of a function package.

Console

###### To view a function package using the console

1. Open the AWS TNB console at [https://console.aws.amazon.com/tnb/](https://console.aws.amazon.com/tnb/ "https://console.aws.amazon.com/tnb/").
2. In the navigation pane, choose **Function
   packages**.
3. Use search box to find the function package

AWS CLI

###### To view a function package using the AWS CLI

1. Use the [list-sol-function-packages](../../../cli/latest/reference/tnb/list-sol-function-packages.md "../../../cli/latest/reference/tnb/list-sol-function-packages.md") command to list your function
   packages.

```
aws tnb list-sol-function-packages
```

2. Use the [get-sol-function-package](../../../cli/latest/reference/tnb/get-sol-function-package.md "../../../cli/latest/reference/tnb/get-sol-function-package.md") command to view details about a
   function package.

```
aws tnb get-sol-function-package \
--vnf-pkg-id `^fp-[a-f0-9]{17}$` \
--endpoint-url "`https://tnb.us-west-2.amazonaws.com`" \
--region `us-west-2`
```
