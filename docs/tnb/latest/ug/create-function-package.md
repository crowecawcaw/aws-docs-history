

# Create a function package in AWS TNB
<a name="create-function-package"></a>

Learn how to create a function package in the AWS TNB network functions catalog. Creating a function package is the first step for creating a network in AWS TNB. After you've uploaded a function package, you can create a network package.

------
#### [ Console ]

**To create a function package using the console**

1. Open the AWS TNB console at [https://console.aws.amazon.com/tnb/](https://console.aws.amazon.com/tnb/).

1. In the navigation pane, choose **Function packages**.

1. Choose **Create function package**.

1. Choose **Choose files** and upload each CSAR package as a `.zip` file. You can upload a maximum of 10 files.

1. Choose **Next**.

1. Review the package details.

1. Choose **Create function package**.

------
#### [ AWS CLI ]

**To create a function package using the AWS CLI**

1. Use the [create-sol-function-package](https://docs.aws.amazon.com/cli/latest/reference/tnb/create-sol-function-package.html) command to create a new function package:

   ```
   aws tnb create-sol-function-package
   ```

1. Use the [put-sol-function-package-content](https://docs.aws.amazon.com/cli/latest/reference/tnb/put-sol-function-package-content.html) command to upload the function package content. For example:

   ```
   aws tnb put-sol-function-package-content \
   --vnf-pkg-id {{^fp-[a-f0-9]{17}$}} \
   --content-type application/zip \
   --file "{{fileb://valid-free5gc-udr.zip}}" \
   --endpoint-url "{{https://tnb.us-west-2.amazonaws.com}}" \
   --region {{us-west-2}}
   ```

------