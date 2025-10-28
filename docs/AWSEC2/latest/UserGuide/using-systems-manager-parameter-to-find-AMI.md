# Reference AMIs using Systems Manager parameters

When you launch an instance using the EC2 launch instance wizard in the Amazon EC2 console,
you can either select an AMI from the list, or you
can select an AWS Systems Manager parameter that points to an AMI ID (described in this section).
If you use automation code to launch your instances, you can specify the Systems Manager parameter
instead of the AMI ID.

A Systems Manager parameter is a customer-defined key-value pair that you can create in Systems Manager
Parameter Store. The Parameter Store provides a central store to externalize your
application configuration values. For more information, see [AWS Systems Manager Parameter
Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md") in the _AWS Systems Manager User Guide_.

When you create a parameter that points to an AMI ID, make sure that you specify the
data type as `aws:ec2:image`. Specifying this data type ensures that when the
parameter is created or modified, the parameter value is validated as an AMI ID. For
more information, see [Native
parameter support for Amazon Machine Image IDs](../../../systems-manager/latest/userguide/parameter-store-ec2-aliases.md "../../../systems-manager/latest/userguide/parameter-store-ec2-aliases.md") in the _AWS Systems Manager User Guide_.

###### Contents

- [Use cases](#systems-manager-parameter-use-case "#systems-manager-parameter-use-case")
- [Permissions](#systems-manager-permissions "#systems-manager-permissions")
- [Limitations](#AMI-systems-manager-parameter-limitations "#AMI-systems-manager-parameter-limitations")
- [Launch an instance using a Systems Manager parameter](#systems-manager-parameter-launch-instance "#systems-manager-parameter-launch-instance")

## Use cases

When you use Systems Manager parameters to point to AMI IDs, it is easier for your users to
select the correct AMI when launching instances. Systems Manager parameters can also simplify
the maintenance of automation code.

**Easier for users**

If you require instances to be launched using a specific AMI, and the AMI is
regularly updated, we recommend that you require your users to select a Systems Manager
parameter to find the AMI. Requiring your users to select a Systems Manager parameter ensures
that the latest AMI is used to launch instances.

For example, every month in your organization you might create a new version of
your AMI that has the latest operating system and application patches. You also
require your users to launch instances using the latest version of your AMI. To
ensure that your users use the latest version, you can create a Systems Manager parameter (for
example, `golden-ami`) that points to the correct AMI ID. Each time a new
version of the AMI is created, you update the AMI ID value in the parameter so that
it always points to the latest AMI. Your users don't have to know about the periodic
updates to the AMI because they continue to select the same Systems Manager parameter each
time. Using a Systems Manager parameter for your AMI makes it easier for them to select the
correct AMI for an instance launch.

**Simplify automation code maintenance**

If you use automation code to launch your instances, you can specify the Systems Manager
parameter instead of the AMI ID. If a new version of the AMI is created, you can
change the AMI ID value in the parameter so that it points to the latest AMI. The
automation code that references the parameter doesn’t have to be modified each time
a new version of the AMI is created. This simplifies the maintenance of the
automation and helps to drive down deployment costs.

###### Note

Running instances are not affected when you change the AMI ID pointed to by
the Systems Manager parameter.

## Permissions

If you use Systems Manager parameters that point to AMI IDs in the launch instance wizard,
you must add the following permissions to your IAM policy:

- `ssm:DescribeParameters` – Grants permission to view and
  select Systems Manager parameters.
- `ssm:GetParameters` – Grants permission to retrieve the
  values of the Systems Manager parameters.

You can also restrict access to specific Systems Manager parameters. For more information
and example IAM policies, see [Example: Use the EC2 launch instance wizard](iam-policies-ec2-console.md#ex-launch-wizard "iam-policies-ec2-console.md#ex-launch-wizard").

## Limitations

AMIs and Systems Manager parameters are Region specific. To use the same Systems Manager parameter
name across Regions, create a Systems Manager parameter in each Region with the same name (for
example, `golden-ami`). In each Region, point the Systems Manager parameter to an
AMI in that Region.

Parameter names are case-sensitive. Backslashes for the parameter name are only
necessary when the parameter is part of a hierarchy, for example,
`/amis/production/golden-ami`. You can omit the backslash if the
parameter is not part of a hierarchy.

## Launch an instance using a Systems Manager parameter

When you launch an instance, instead of specifying an AMI ID, you can specify
a Systems Manager parameter that points to an AMI ID.

To specify the parameter programmatically, use the following syntax, where
`resolve:ssm` is the standard prefix and `parameter-name`
is the unique parameter name.

```
resolve:ssm:`parameter-name`
```

Systems Manager parameters have version support. Each iteration of a parameter is
assigned a unique version number. You can reference the version of the parameter
as follows, where `version` is the unique version number. By default,
the latest version of the parameter is used when no version is specified.

```
resolve:ssm:`parameter-name`:`version`
```

To launch an instance using a public parameter provided by AWS, see [Reference the latest AMIs using Systems Manager public parameters](finding-an-ami-parameter-store.md "finding-an-ami-parameter-store.md").

Console

###### To find an AMI using a Systems Manager parameter

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. From the navigation bar, select the Region in which to launch
   your instances. You can select any Region that's available to
   you, regardless of your location.
3. From the console dashboard, choose **Launch
   instance**.
4. Under **Application and OS Images (Amazon Machine
   Image)**, choose **Browse more
   AMIs**.
5. Choose the arrow button to the right of the search bar, and
   then choose **Search by Systems Manager
   parameter**.
6. For **Systems Manager parameter**, select a parameter.
   The corresponding AMI ID appears below **Currently
   resolves to**.
7. Choose **Search**. The AMIs that match the
   AMI ID appear in the list.
8. Select the AMI from the list, and choose
   **Select**.

For more information about launching an instance using the launch
instance wizard, see [Launch an EC2 instance using the launch
instance wizard in the console](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md").

AWS CLI

###### To launch an instance using a Systems Manager parameter

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md")
command with the `--image-id` option. This example
uses a Systems Manager parameter named `golden-ami`, which
specifies an AMI ID.

```
--image-id resolve:ssm:/`golden-ami`
```

You can create versions of a Systems Manager parameter. The following example
specifies version 2 of the `golden-ami` parameter.

```
--image-id resolve:ssm:/`golden-ami:2`
```

PowerShell

###### To launch an instance using a Systems Manager parameter

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md")
cmdlet with the `-ImageId` parameter. This example
uses a Systems Manager parameter named `golden-ami`, which
specifies an AMI ID.

```
-ImageId "resolve:ssm:/golden-ami"
```

You can create versions of a Systems Manager parameter. The following example
specifies version 2 of the `golden-ami` parameter.

```
-ImageId "resolve:ssm:/golden-ami:2"
```
