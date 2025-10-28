# Create a function package in AWS TNB

Learn how to create a function package in the AWS TNB network functions catalog. Creating a function package is the first step
for creating a network in AWS TNB. After you've uploaded a function package, you can create
a network package.

Console

###### To create a function package using the console

1. Open the AWS TNB console at [https://console.aws.amazon.com/tnb/](https://console.aws.amazon.com/tnb/ "https://console.aws.amazon.com/tnb/").
2. In the navigation pane, choose **Function
   packages**.
3. Choose **Create function package**.
4. Choose **Choose files** and upload each CSAR package as a `.zip` file. You can upload a maximum of 10 files.
5. Choose **Next**.
6. Review the package details.
7. Choose **Create function package**.

AWS CLI

###### To create a function package using the AWS CLI

1. Use the [create-sol-function-package](../../../cli/latest/reference/tnb/create-sol-function-package.md "../../../cli/latest/reference/tnb/create-sol-function-package.md") command to create a new function
   package:

```
aws tnb create-sol-function-package
```

2. Use the [put-sol-function-package-content](../../../cli/latest/reference/tnb/put-sol-function-package-content.md "../../../cli/latest/reference/tnb/put-sol-function-package-content.md") command to upload the
   function package content. For example:

```
aws tnb put-sol-function-package-content \
--vnf-pkg-id `^fp-[a-f0-9]{17}$` \
--content-type application/zip \
--file "`fileb://valid-free5gc-udr.zip`" \
--endpoint-url "`https://tnb.us-west-2.amazonaws.com`" \
--region `us-west-2`
```
