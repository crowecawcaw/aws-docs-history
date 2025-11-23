# Refer to resource outputs in another CloudFormation

stack

This walkthrough shows you how to reference outputs from one CloudFormation stack within another
stack to create more modular and reusable templates.

Instead of including all resources in a single stack, you create related AWS resources in
separate stacks. Then, you can refer to required resource outputs from other stacks. By
restricting cross-stack references to outputs, you control the parts of a stack that are
referenced by other stacks.

For example, you might have a network stack with a VPC, a security group, and a subnet for
public web applications, and a separate public web application stack. To ensure that the web
applications use the security group and subnet from the network stack, you create a cross-stack
reference that allows the web application stack to reference resource outputs from the network
stack. With a cross-stack reference, owners of the web application stacks don't need to create
or maintain networking rules or assets.

To create a cross-stack reference, use the `Export` output field to flag the
value of a resource output for export. Then, use the `Fn::ImportValue` intrinsic
function to import the value. For more information, see [Get exported outputs from a deployed CloudFormation
stack](using-cfn-stack-exports.md "using-cfn-stack-exports.md").

###### Note

CloudFormation is a free service. However, you are charged for the AWS resources that you
include in your stacks at the current rate for each one. For more information about AWS
pricing, see [the detail page for each product](http://aws.amazon.com "http://aws.amazon.com").

###### Topics

- [Use a sample template to create a
  network stack](#walkthrough-crossstackref-create-vpc-stack "#walkthrough-crossstackref-create-vpc-stack")
- [Use a sample template to create a
  web application stack](#walkthrough-crossstackref-create-ec2-stack "#walkthrough-crossstackref-create-ec2-stack")
- [Verify the stack works as designed](#walkthrough-crossstackref-verify "#walkthrough-crossstackref-verify")
- [Troubleshoot AMI mapping
  errors](#walkthrough-crossstackref-troubleshooting-ami "#walkthrough-crossstackref-troubleshooting-ami")
- [Clean up your resources](#walkthrough-crossstackref-clean-up "#walkthrough-crossstackref-clean-up")

## Use a sample template to create a

network stack

Before you begin this walkthrough, check that you have IAM permissions to use all of the
following services: Amazon VPC, Amazon EC2, and CloudFormation.

The network stack contains the VPC, security group, and subnet that you will use in the
web application stack. In addition to these resources, the network stack creates an Internet
gateway and routing tables to enable public access.

You must create this stack before you create the web application stack. If you create the
web application stack first, it won't have a security group or subnet.

The stack template is available from the following URL: [https://s3.amazonaws.com/cloudformation-examples/user-guide/cross-stack/SampleNetworkCrossStack.template](https://s3.amazonaws.com/cloudformation-examples/user-guide/cross-stack/SampleNetworkCrossStack.template "https://s3.amazonaws.com/cloudformation-examples/user-guide/cross-stack/SampleNetworkCrossStack.template").
To see the resources that the stack will create, choose the link, which opens the template. In
the `Outputs` section, you can see the networking resources that the sample
template exports. The names of the exported resources are prefixed with the stack's name in
case you export networking resources from other stacks. When users import networking
resources, they can specify from which stack the resources are imported.

###### To create the network

stack

1. Sign in to the AWS Management Console and open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the **Stacks** page, choose **Create stack** at
   top right, and then choose **With new resources (standard)**.
3. Choose **Choose an existing template**, and in the **Specify
   template** section, choose **Amazon S3 URL**.
4. For **Amazon S3 URL**, paste the following URL:
   `https://s3.amazonaws.com/cloudformation-examples/user-guide/cross-stack/SampleNetworkCrossStack.template`.
5. Choose **Next**.
6. For **Stack name**, type
   `SampleNetworkCrossStack`, and then choose
   **Next**.

###### Note

Record the name of this stack. You'll need the stack name when you launch the web
application stack. 7. Choose **Next**. For this walkthrough, you don't need to add tags or
specify advanced settings. 8. Ensure that the stack name and template URL are correct, and then choose
**Create stack**.

It might take several minutes for CloudFormation to create your stack. Wait until all
resources have been successfully created before proceeding to create the web application
stack. 9. To monitor progress, view the stack events. For more information, see [Monitor stack progress](monitor-stack-progress.md "monitor-stack-progress.md").

## Use a sample template to create a

web application stack

The web application stack creates an EC2 instance that uses the security group and subnet
from the network stack.

You must create this stack in the same AWS Region as the network stack.

The stack template is available from the following URL: [https://s3.amazonaws.com/cloudformation-examples/user-guide/cross-stack/SampleWebAppCrossStack.template](https://s3.amazonaws.com/cloudformation-examples/user-guide/cross-stack/SampleWebAppCrossStack.template "https://s3.amazonaws.com/cloudformation-examples/user-guide/cross-stack/SampleWebAppCrossStack.template").
To see the resources that the stack will create, choose the link, which will open the
template. In the `Resources` section, view the EC2 instance's properties. You can
see how the networking resources are imported from another stack by using the
`Fn::ImportValue` function.

###### To create the web

application stack

1. From the **Stacks** page, choose **Create stack** at
   top right, and then choose **With new resources (standard)**.
2. Choose **Choose an existing template**, and in the **Specify
   template** section, choose **Amazon S3 URL**.
3. For **Amazon S3 URL**, paste the following URL:
   `https://s3.amazonaws.com/cloudformation-examples/user-guide/cross-stack/SampleWebAppCrossStack.template`.
4. Choose **Next**.
5. For **Stack name**, type
   `SampleWebAppCrossStack`. In the **Parameters**
   section, use the default value for the **NetworkStackName** parameter,
   and then choose **Next**.

The sample template uses the parameter value to specify from which stack to import
values. 6. Choose **Next**. For this walkthrough, you don't need to add tags or
specify advanced settings. 7. Ensure that the stack name and template URL are correct, and then choose
**Create stack**.

It might take several minutes for CloudFormation to create your stack.

## Verify the stack works as designed

After the stack has been created, view its resources and note the instance ID. For more
information on viewing stack resources, see [View stack information from the
CloudFormation console](cfn-console-view-stack-data-resources.md "cfn-console-view-stack-data-resources.md").

To verify the instance's security group and subnet, view the instance's properties in the
[Amazon EC2 console](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/"). If the instance uses the security
group and subnet from the `SampleNetworkCrossStack` stack, you have successfully
created a cross-stack reference.

Use the console to view the stack outputs and the example website URL to verify that the
web application is running. For more information, see [View stack information from the
CloudFormation console](cfn-console-view-stack-data-resources.md "cfn-console-view-stack-data-resources.md").

## Troubleshoot AMI mapping

errors

If you receive the error `Template error: Unable to get mapping for
 AWSRegionArch2AMI::[region]::HVM64`, the template doesn't include an AMI mapping for
your AWS Region. Instead of updating the mapping, we recommend using Systems Manager public parameters
to dynamically reference the latest AMIs:

1. Download the `SampleWebAppCrossStack` template to your local
   machine from: [https://s3.amazonaws.com/cloudformation-examples/user-guide/cross-stack/SampleWebAppCrossStack.template](https://s3.amazonaws.com/cloudformation-examples/user-guide/cross-stack/SampleWebAppCrossStack.template "https://s3.amazonaws.com/cloudformation-examples/user-guide/cross-stack/SampleWebAppCrossStack.template").
2. Delete the entire `AWSRegionArch2AMI` mapping section.
3. Add the following Systems Manager parameter:

```
"LatestAmiId": {
  "Description": "The latest Amazon Linux 2 AMI from the Parameter Store",
    "Type": "AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>",
    "Default": "/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2"
  }
```

4. Replace the existing `ImageId` reference:

```
"ImageId": { "Fn::FindInMap": [ "AWSRegionArch2AMI", { "Ref": "AWS::Region" } , "HVM64" ] },
```

With:

```
"ImageId": { "Ref": "LatestAmiId" },
```

This parameter automatically resolves to the latest Amazon Linux 2 AMI for the region
where you deploy the stack.

For other Linux distributions, use the appropriate parameter path. For more
information, see [Discovering public parameters in Parameter Store](../../../systems-manager/latest/userguide/parameter-store-finding-public-parameters.md "../../../systems-manager/latest/userguide/parameter-store-finding-public-parameters.md") in the
_AWS Systems Manager User Guide_. 5. Upload the modified template to an S3 bucket in your account:

```
aws s3 cp `SampleWebAppCrossStack.template` `s3://amzn-s3-demo-bucket/`
```

6. When creating the stack, specify your S3 template URL instead of the example
   URL.

## Clean up your resources

To ensure that you are not charged for unwanted services, delete the stacks.

###### To delete the stacks

1. In the CloudFormation console, choose the `SampleWebAppCrossStack`
   stack.
2. Choose **Actions**, and then choose **Delete
   stack**.
3. In the confirmation message, choose **Delete**.
4. After the stack has been deleted, repeat the same steps for the
   `SampleNetworkCrossStack` stack.

###### Note

Wait until CloudFormation completely deletes the `SampleWebAppCrossStack`
stack. If the EC2 instance is still running in the VPC, CloudFormation won't delete the VPC
in the `SampleNetworkCrossStack` stack.
