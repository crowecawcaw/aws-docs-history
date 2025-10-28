# Distributor package managed component application install for Image Builder Windows images

AWS Systems Manager Distributor helps you package and publish software to AWS Systems Manager managed nodes.
You can package and publish your own software or use Distributor to find and publish
AWS-provided agent software packages. For more information about Systems Manager Distributor, see
[AWS Systems Manager Distributor](../../../systems-manager/latest/userguide/distributor.md "../../../systems-manager/latest/userguide/distributor.md") in the
_AWS Systems Manager User Guide_.

###### Managed components for Distributor

The following Image Builder managed components use AWS Systems Manager Distributor to install application
packages on Windows instances.

- The `distributor-package-windows` managed component uses AWS Systems Manager
  Distributor to install application packages that you specify on your Windows image
  build instance. To configure parameters when you include this component in your
  recipe, see [Configure distributor-package-windows
  as a standalone component](#mgdcomponent-distributor-config-standalone "#mgdcomponent-distributor-config-standalone").
- The `aws-vss-components-windows` component uses AWS Systems Manager Distributor
  to install the `AwsVssComponents` package on your Windows image build
  instance. To configure parameters when you include this component in your recipe,
  see [Configure aws-vss-components-windows
  as a standalone component](#mgdcomponent-vss-config-standalone "#mgdcomponent-vss-config-standalone").
  For more information about how to use managed components in your Image Builder recipe, see
  [Create a new version of an image recipe](create-image-recipes.md "create-image-recipes.md") for image recipes or
  [Create a new version of a container recipe](create-container-recipes.md "create-container-recipes.md") for container
  recipes. For more information about the `AwsVssComponents` package, see [Create a VSS application-consistent
  snapshot](../../../AWSEC2/latest/UserGuide/application-consistent-snapshots.md "../../../AWSEC2/latest/UserGuide/application-consistent-snapshots.md") in the _Amazon EC2 User Guide_.

## Prerequisites

Before you use Image Builder components that rely on Systems Manager Distributor to install application
packages, you must ensure that the following prerequisites are met.

- Image Builder components that use Systems Manager Distributor to install application packages
  on your instance need permission to call the Systems Manager API. Before you use the
  components in an Image Builder recipe, you must create the IAM policy and role that
  grant permission. To configure permissions, see [Configure Systems Manager Distributor permissions](#mgdcomponent-distributor-permissions "#mgdcomponent-distributor-permissions").

###### Note

Image Builder doesn't currently support Systems Manager Distributor packages that reboot the instance. For
example, the `AWSNVMe`, `AWSPVDrivers`, and `AwsEnaNetworkDriver`
Distributor packages reboot the instance, and so are not allowed.

## Configure Systems Manager Distributor permissions

The `distributor-package-windows` component and other components that use it,
such as `aws-vss-components-windows`, require additional permission on the build
instance to run. The build instance must be able to call the Systems Manager API to begin a Distributor
installation and poll for the result.

Follow these procedures in the AWS Management Console to create a custom IAM policy and role that grant
permission for Image Builder components to install Systems Manager Distributor packages from the build instance.

###### Step 1: Create a policy

Create an IAM policy for Distributor permissions.

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**, and then choose
   **Create policy**.
3. On the **Create policy** page, choose the **JSON**
   tab, and then replace the default content with the following JSON policy, substituting
   partition, Region, and account ID as necessary, or using wildcards.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowDistributorSendCommand",
 "Effect": "Allow",
 "Action": "ssm:SendCommand",
 "Resource": [
 "arn:aws:ssm:*::document/AWS-ConfigureAWSPackage",
 "arn:aws:ec2:*:`111122223333`:instance/*"
 ]
 },
 {
 "Sid": "AllowGetCommandInvocation",
 "Effect": "Allow",
 "Action": "ssm:GetCommandInvocation",
 "Resource": "*"
 }
 ]
}`

```

4. Choose **Review policy**.
5. For **Name**, enter a name to identify the policy, such
   as `InvokeDistributor` or another name
   that you prefer.
6. (Optional) For **Description**, enter a description of
   the role's purpose.
7. Choose **Create policy**.

###### Step 2: Create a role

Create an IAM role for Distributor permissions.

1. From the IAM console navigation pane, choose **Roles**,
   and then choose **Create role**.
2. Under **Select type of trusted entity**, choose
   **AWS service**.
3. Immediately under **Choose the service that will use this role**,
   choose **EC2**, and then choose
   **Next: Permissions**.
4. Under **Select your use case**, choose **EC2**,
   and then choose **Next: Permissions**.
5. In the list of policies, select the check box next to
   **AmazonSSMManagedInstanceCore**. (Type `SSM` in the
   search box if you need to narrow the list.)
6. In this list of policies, choose the box next to
   **EC2InstanceProfileForImageBuilder**. (Type `ImageBuilder`
   in the search box if you need to narrow the list.)
7. Choose **Next: Tags**.
8. (Optional) Add one or more tag key value pairs to organize, track, or control
   access for this role, and then choose **Next: Review**.
9. For **Role name**, enter a name for the role, such as
   `InvokeDistributor` or another name
   that you prefer.
10. (Optional) For **Role description**, replace the default text
    with a description of this role's purpose.
11. Choose **Create role**. The system returns you to the
    **Roles** page.

###### Step 3: Attach the policy to the role

The final step to set up your Distributor permissions is to attach the
IAM policy to the IAM role.

1. From the **Roles** page in the IAM console, choose the
   role that you just created. The role **Summary page** opens.
2. Choose **Attach policies**.
3. Search for the policy that you created in the previous procedure and select the
   check box next to the name.
4. Choose **Attach policy**.

Use this role in the Image Builder Infrastructure Configuration resource for any image that
includes components that use Systems Manager Distributor. For more information, see
[Create an infrastructure configuration](create-infra-config.md "create-infra-config.md").

## Configure `distributor-package-windows`

as a standalone component

To use the `distributor-package-windows` component in a
recipe, set the following parameters that configure the package to install.

###### Note

Before you use the `distributor-package-windows` component in a recipe,
you must ensure that all of the [Prerequisites](#mgdcomponent-distributor-prereq "#mgdcomponent-distributor-prereq") are met.

- **Action** (Required) – Specify whether to
  install or uninstall the package. Valid values include `Install` and
  `Uninstall`. The value defaults to `Install`.
- **PackageName** (Required) – The name of
  the Distributor package to install or uninstall. For a list of valid package
  names, see [Find Distributor packages](#mgdcomponent-distributor-find-pkg "#mgdcomponent-distributor-find-pkg").
- **PackageVersion** (Optional) – The
  version of the Distributor package to install. PackageVersion defaults to the
  recommended version.
- **AdditionalArguments** (Optional) – A
  JSON string that contains the additional parameters to provide to your script to
  install, uninstall, or update a package. For more information, see
  **additionalArguments** in the [aws:configurePackage](../../../systems-manager/latest/userguide/documents-command-ssm-plugin-reference.md#aws-configurepackage "../../../systems-manager/latest/userguide/documents-command-ssm-plugin-reference.md#aws-configurepackage")
  **Inputs** section of the
  **Systems Manager Command document plugin reference** page.

## Configure `aws-vss-components-windows`

as a standalone component

When you use the `aws-vss-components-windows` component in a
recipe, you can optionally set the `PackageVersion` parameter to use a
specific version of the `AwsVssComponents` package. When you leave out
this parameter, the component defaults to use the recommended version of the
`AwsVssComponents` package.

###### Note

Before you use the `aws-vss-components-windows` component in a recipe,
you must ensure that all of the [Prerequisites](#mgdcomponent-distributor-prereq "#mgdcomponent-distributor-prereq") are met.

## Find Distributor packages

Amazon and third parties provide public packages that you can install with
Systems Manager Distributor.

To view available packages in the AWS Management Console, log into the
[AWS Systems Manager console](https://console.aws.amazon.com/systems-manager/; "https://console.aws.amazon.com/systems-manager/;") and choose
**Distributor** from the navigation pane. The **Distributor**
page shows all of the packages that are available to you. For more information about listing
available packages with the AWS CLI, see [View packages
(command line)](../../../systems-manager/latest/userguide/distributor-view-packages.md "../../../systems-manager/latest/userguide/distributor-view-packages.md") in the _AWS Systems Manager User Guide_.

You can also create your own private Systems Manager Distributor packages. For more information, see
[Create a package](../../../systems-manager/latest/userguide/distributor-working-with-packages-create.md "../../../systems-manager/latest/userguide/distributor-working-with-packages-create.md")
in the _AWS Systems Manager User Guide_.
