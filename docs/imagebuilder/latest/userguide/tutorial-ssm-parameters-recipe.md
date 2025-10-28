# Use a base image parameter in your recipe

When you create a recipe for image customizations, there are several ways to identify
the base image that you start with. If you specify the Amazon Machine Image (AMI) ID for
your base image and that base image is updated, its AMI ID might change and you would need
to update your recipe to match.

Instead of changing your recipe each time the base image ID changes, you can define an
AWS Systems Manager Parameter Store parameter (SSM parameter) to store the value of your base image AMI ID, and then
use the parameter to specify the base image in your recipe. For AWS managed AMIs, you can
use a public parameter for the latest version.

This tutorial walks you through the process of creating an AMI ID parameter
and using it in an image recipe. Image Builder steps in this tutorial are console-based.

###### Contents

- [Step 1: Find or create a Parameter Store
  parameter](#tutorial-ssm-create-parameter "#tutorial-ssm-create-parameter")
- [Step 2: Configure IAM permissions (optional)](#tutorial-ssm-configure-iam "#tutorial-ssm-configure-iam")
- [Step 3: Create an Image Recipe that uses the
  parameter](#tutorial-ssm-create-recipe "#tutorial-ssm-create-recipe")

## Step 1: Find or create a Parameter Store

parameter

The process for this step depends on the type of AMI that you specify for your base image.
For AWS managed AMIs, you can use a public parameter that refers to the current version. Some
parameters might not be available in all AWS Regions.

To begin, open the tab that corresponds to your AMI.

AWS managed AMI
If your base image is an AWS managed AMI, you can use public parameters to specify
the AMI ID, rather than creating your own parameter. To find the public parameter for
your AMI, see [Discovering public parameters](../../../systems-manager/latest/userguide/parameter-store-finding-public-parameters.md "../../../systems-manager/latest/userguide/parameter-store-finding-public-parameters.md") in the _AWS Systems Manager User Guide_.

Custom AMI
To create an AMI ID parameter, follow the instructions for [Creating
Parameter Store parameters in Systems Manager](../../../systems-manager/latest/userguide/sysman-paramstore-su-create.md "../../../systems-manager/latest/userguide/sysman-paramstore-su-create.md") with the console, AWS CLI, or PowerShell.
Provide the following values to ensure that the parameter value is an AMI ID.

**Parameter tier**: `Standard`

**Type**: `String`

**Data type**: Select `aws:ec2:image`. When you
specify this type, the system validates the value that's entered to ensure that
it's an AMI ID.

**Value**: Enter a valid AMI ID (for example, `ami-1234567890abcdef1`).

## Step 2: Configure IAM permissions (optional)

To use a Systems Manager Parameter Store parameter (SSM parameter), whether public or private,
the following Systems Manager Parameter Store actions must be specified in an IAM role,
with the parameter listed as a resource. The Image Builder service-linked role grants permission to get
public parameters, or to get or update private parameters that have an `/imagebuilder/`
prefix. For private parameters that don't have that prefix, you can add permission to your
execution role.

- `ssm:GetParameter` – This action allows you to use an SSM parameter
  to specify the base image in your recipe.
- `ssm:PutParameter` – This action allows you to store the output
  AMI ID in an SSM parameter during distribution. Policy definition looks the same, but
  this tutorial does not include the put action in the example policy.

1. ###### Create a custom role (optional)

When you create a pipeline or use the create-image command in the AWS CLI, you
can only specify one Image Builder execution role. If you have defined an Image Builder workflow
execution role, you would add any additional feature permissions to that role.
Otherwise, you would create a new custom role that includes the required permissions. If you already have a custom execution role defined,
you can skip this step.

Follow the process for [Creating a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the
_AWS Identity and Access Management User Guide_. 2. ###### Add permissions to your custom role

To add the SSM parameter permissions to your custom role, follow the
[Update the permissions policy for a role](../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md#id_roles_update-role-permissions-policy "../../../IAM/latest/UserGuide/id_roles_update-role-permissions.md#id_roles_update-role-permissions-policy") process in the
_AWS Identity and Access Management User Guide_.

The following policy example shows the `ssm:GetParameter` action
with a parameter that's created in your account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "PrivateParameterCustomRole",
 "Effect": "Allow",
 "Action": "ssm:GetParameter",
 "Resource": "arn:aws:ssm:*:`111122223333`:parameter/`parameter-name`"
 }
 ]
}`

```

For more information about public parameter resources, see [Calling AMI public parameters](../../../systems-manager/latest/userguide/parameter-store-public-parameters-ami.md "../../../systems-manager/latest/userguide/parameter-store-public-parameters-ami.md") in the _AWS Systems Manager User Guide_.

## Step 3: Create an Image Recipe that uses the

parameter

1. Open the EC2 Image Builder console at
   [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/").
2. Choose **Image recipes**, then choose **Create image
   recipe** from the list page.
3. Fill out the **Base image** section, as follows:
   1. Choose the **Use
      custom AMI** option. This displays additional fields where you
      can enter the AMI ID or an SSM parameter that contains the AMI ID.
   2. Choose the **SSM parameter** option.
   3. In the **SSM parameter** field, enter the parameter
      name or Amazon Resource Name (ARN) of the parameter that you created in
      Step 1. If you enter the name, it will **_not_** have the prefix in the console.

4. Complete the remaining recipe configuration as needed.

###### Note

If you set the parent image through other interfaces, such as the AWS CLI, the
parameter name must have a prefix of `ssm:` (for example,
`ssm:`/ImageBuilder-Tutorial/BaseAMI``.
