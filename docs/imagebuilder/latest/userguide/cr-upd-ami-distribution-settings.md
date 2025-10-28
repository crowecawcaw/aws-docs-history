# Create and update AMI distribution configurations

This section covers creating and updating distribution configurations for an Image Builder AMI.

###### Contents

- [AMI distribution prerequisites](#ami-distribution-config-prereqs "#ami-distribution-config-prereqs")
- [Create an AMI distribution
  configuration](#create-ami-distribution-config "#create-ami-distribution-config")
- [Update an AMI distribution configuration](#update-ami-distribution-config "#update-ami-distribution-config")
- [Example: Enable EC2 Fast Launch with a launch template for
  output AMIs](#create-ami-dist-win-fast-launch "#create-ami-dist-win-fast-launch")
- [Example: Create
  distribution settings for output VM disks from the AWS CLI](#cli-create-vm-dist-config "#cli-create-vm-dist-config")

## AMI distribution prerequisites

Some distribution settings have prerequisites, as follows:

###### Topics

- [SSM output parameter prerequisites](#ami-distribution-prereqs-ssm-param "#ami-distribution-prereqs-ssm-param")
- [EC2 Fast Launch prerequisites](#ami-distribution-prereqs-fast-launch "#ami-distribution-prereqs-fast-launch")

### Prerequisites for SSM output parameters

Before you create a new AMI distribution configuration that sets an AWS Systems Manager Parameter Store parameter
(SSM parameter), ensure that you've met the following prerequisites.

**Execution role**

When you create a pipeline or use the create-image command in the AWS CLI, you
can only specify one Image Builder execution role. If you have defined an Image Builder workflow
execution role, you would add any additional feature permissions to that role.
Otherwise, you would create a new custom role that includes the required permissions.

- To store the output AMI ID in an SSM parameter during distribution,
  you must specify the `ssm:PutParameter` action in your Image Builder execution
  role, with the parameter listed as a resource.
- When you set the parameter data type to `AWS EC2 Image` to signal
  Systems Manager to validate the parameter value as an AMI ID, you must also add the
  `ec2:DescribeImages` action.

### Prerequisites for EC2 Fast Launch

Before you create a new distribution configuration for EC2 Fast Launch for Windows AMIs, ensure
that you've met the following prerequisites.

- If you provide a custom launch template when you configure EC2 Fast Launch,
  the service uses the VPC and other configuration settings that you've defined in
  the launch template. For more information, see [Use a launch template when you set up EC2 Fast Launch](../../../AWSEC2/latest/UserGuide/win-fast-launch-configure.md#win-fast-launch-with-template "../../../AWSEC2/latest/UserGuide/win-fast-launch-configure.md#win-fast-launch-with-template").
- If you don't use a custom launch template to configure your settings, you must
  attach the [EC2FastLaunchFullAccess](../../../AWSEC2/latest/UserGuide/security-iam-awsmanpol-EC2FastLaunchFullAccess.md "../../../AWSEC2/latest/UserGuide/security-iam-awsmanpol-EC2FastLaunchFullAccess.md") policy to the IAM role that
  Image Builder uses to create your image. When you create a pipeline or use the create-image command in the AWS CLI, you
  can only specify one Image Builder execution role. If you have defined an Image Builder workflow
  execution role, you would add any additional feature permissions to that role.
  Otherwise, you would create a new custom role that includes the required permissions.

Then, when Image Builder copies your image, EC2 Fast Launch automatically
creates an AWS CloudFormation stack with the following resources in your AWS account.

    + A virtual private cloud (VPC)
    + Private subnets across multiple Availability Zones
    + A launch template configured with Instance Metadata Service Version 2 (IMDSv2)
    + A security group with no inbound or outbound rules

###### Note

Image Builder doesn't support cross-account distribution for AMIs with EC2 Fast Launch
pre-enabled. EC2 Fast Launch must be enabled from the destination account.

## Create an AMI distribution

configuration

Distribution configurations include the output AMI name, specific Region settings
for encryption, launch permissions, and AWS accounts, organizations, and organizational units (OUs)
that can launch the output AMI, and license configurations.

A distribution configuration allows you to specify the name and description of
your output AMI, authorize other AWS accounts to launch the AMI, copy the AMI to
other accounts, and replicate the AMI to other AWS Regions. It also allows you to
export the AMI to Amazon Simple Storage Service (Amazon S3), or configure EC2 Fast Launch for output Windows
AMIs. To make an AMI public, set the launch permission authorized accounts to
`all`. See the examples for making an AMI public at EC2 **[ModifyImageAttribute](../../../AWSEC2/latest/APIReference/API_ModifyImageAttribute.md "../../../AWSEC2/latest/APIReference/API_ModifyImageAttribute.md")**.

Console
Follow these steps to create a new AMI distribution configuration in
the AWS Management Console:

1.  Open the EC2 Image Builder console at
    [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/").
2.  Choose **Distribution settings**
    from the navigation pane. This shows a list of the
    distribution configurations that are created under your account.
3.  Choose **Create distribution settings** near the
    top of the **Distribution settings** panel.
4.  In the **Image type** section, choose the
    **Amazon Machine Image (AMI)** output type.
5.  In the **General** section, enter a **Name**
    for your distribution configuration, and optional description.
6.  In the **Region settings** section, enter the following
    details for each Region where you are distributing your AMI:
    1. The AMI is distributed to the current Region (**Region 1**),
       by default. **Region 1** is the source for the
       distribution. Some settings for **Region 1** are not open
       for editing. For any Regions that you add, you can choose a Region from the
       **Region** dropdown list.

    The **Kms key** identifies the AWS KMS key that's
    used to encrypt the EBS volumes for your image in the target Region. It's
    important to note that this doesn't apply for the original AMI that the build
    creates under your account in the source Region (**Region 1**).
    Encryption that runs during the distribution phase of the build is only
    for images that are distributed to other accounts or Regions.

    To encrypt the EBS volumes for the AMI that's created in the source
    Region for your account, you must set the KMS key in the image recipe
    block device mapping (**Storage (volumes)** in the console).

    Image Builder copies the AMI to the **Target accounts** that
    you specify for the Region.

    ###### Prerequisite

    To copy an image across accounts, you must create the
    `EC2ImageBuilderDistributionCrossAccountRole` role in all
    of the distribution target accounts, and attach the
    [Ec2ImageBuilderCrossAccountDistributionAccess policy](security-iam-awsmanpol.md#sec-iam-manpol-Ec2ImageBuilderCrossAccountDistributionAccess "security-iam-awsmanpol.md#sec-iam-manpol-Ec2ImageBuilderCrossAccountDistributionAccess")
    managed policy to the role.

    The **Output AMI name** is optional. If you provide a name, the
    final output AMI name includes an appended timestamp of when the AMI
    is built. If you do not specify a name, Image Builder appends the build
    timestamp to the recipe name. This ensures unique AMI names for each
    build.

        1. With AMI sharing, you can grant access for specified AWS Principals to
         launch instances from your AMI. If you expand the **AMI sharing**
         section, you can enter the following details:




        	* **Launch permissions** – Select
        	 **Private** if you want to keep your AMI private,
        	 and allow access for specific AWS Principals to launch an instance
        	 from your private AMI. Select **Public** if you
        	 want to make your AMI public. Any AWS Principal can launch an instance
        	 from your public AMI.
        	* **Principals** – You can grant access for
        	 the following types of AWS Principals to launch
        	 instances:




        		+ **AWS account** – Grant
        		 access to a specific AWS account
        		+ **Organizational unit (OU)** –
        		 Grant access to an OU, and all of its child entities. Child
        		 entities include OUs and AWS accounts.
        		+ **Organization** – Grant
        		 access to your AWS Organizations, and all of its child entities. Child
        		 entities include OUs and AWS accounts.


        		First, select the Principal type. Then enter the ID for the
        		 AWS Principal to which you want to grant access in the box to
        		 the right of the drop-down list. You can enter multiple IDs of
        		 different types.
        2. You can expand the **License configuration** section to
         attach license configurations created with AWS License Manager to your Image Builder images.
         License configurations contain licensing rules based on the terms of your
         enterprise agreements. Image Builder automatically includes license configurations
         that were associated with your base AMI.
        3. You can expand the **Launch template configuration**
         section to specify an EC2 launch template to use for launching instances
         from the AMI you create.


        If you are using an EC2 launch template, you can instruct Image Builder to create
         a new version of your launch template that includes the latest AMI ID after
         the build completes. To update the launch template, configure the settings
         as follows:




        	* **Launch template name** – Select
        	 the name of the launch template that you want Image Builder to update.
        	* **Set the default version** – Select
        	 this check box to update the launch template default version to the
        	 new version.
        To add another launch template configuration, choose **Add launch
         template configuration**. You can have up to
         five launch template configurations per Region.
        4. You can expand the **SSM parameter configurations**
         section to configure an SSM parameter that will store the output AMI ID
         for the image that's distributed to the destination Region. You can
         optionally specify a distribution account in the Region.


        **Parameter name** – Enter the
         name for your parameter. For example `/output/image/param`.


        **Data type** – Keep the default
         value (`AWS EC2 Image`). This tells Systems Manager to validate the
         parameter value to ensure that it's a valid AMI ID.

    2. To add distribution settings for another Region, choose
       **Add Region**.

7.  Choose **Create settings** when you are done.

AWS CLI
The following example shows how to use the **create-distribution-configuration**
command to create a new distribution configuration for your AMI, using the AWS CLI.

1. ###### Create a CLI input JSON file

Use a file-editing tool to create a JSON file with keys shown in one of the
following examples, and values that are valid for your environment. These
examples define which AWS accounts, AWS Organizations or organizational units (OUs)
have permission to launch the AMI you distribute to the specified Regions.
Name the file
`create-ami-distribution-configuration.json`, for use
in the next step:

###### Example 1: Distribute to AWS accounts

This example distributes an AMI to two Regions, and specifies
AWS accounts that have launch permissions in each Region.

```
{
	"name": "MyExampleAccountDistribution",
	"description": "Copies AMI to eu-west-1, and specifies accounts that can launch instances in each Region.",
	"distributions": [
		{
			"region": "us-west-2",
			"amiDistributionConfiguration": {
				"name": "Name {{imagebuilder:buildDate}}",
				"description": "An example image name with parameter references",
				"amiTags": {
					"KeyName": "Some Value"
				},
				"launchPermission": {
					"userIds": [
						"987654321012"
					]
				}
			}
		},
		{
			"region": "eu-west-1",
			"amiDistributionConfiguration": {
				"name": "My {{imagebuilder:buildVersion}} image {{imagebuilder:buildDate}}",
				"amiTags": {
					"KeyName": "Some value"
				},
				"launchPermission": {
					"userIds": [
						"100000000001"
					]
				}
			}
		}
	]
}
```

###### Example 2: Distribute to Organizations and OUs

This example distributes an AMI to the source Region, and specifies
organization and OU launch permissions.

```
{
	"name": "MyExampleAWSOrganizationDistribution",
	"description": "Shares AMI with the Organization and OU",
	"distributions": [
		{
			"region": "us-west-2",
			"amiDistributionConfiguration": {
				"name": "Name {{ imagebuilder:buildDate }}",
				"launchPermission": {
					"organizationArns": [
						"arn:aws:organizations::123456789012:organization/o-myorganization123"
					],
					"organizationalUnitArns": [
						"arn:aws:organizations::123456789012:ou/o-123example/ou-1234-myorganizationalunit"
					]
				}
			}
		}
	]
}
```

###### Example 3: Store the output AMI ID in an SSM parameter

This example stores the output AMI ID in an AWS Systems Manager Parameter
Store parameter in the distribution Region.

```
{
	"name": "`SSMParameterOutputAMI`",
	"description": "`Updates an SSM parameter with the output AMI ID for the distribution.`",
	"distributions": [
		{
			"region": "`us-west-2`",
			"amiDistributionConfiguration": {
				"name": "Name {{ imagebuilder:buildDate }}"
			},
			"ssmParameterConfigurations": [
				{
					"amiAccountId": "`111122223333`",
					"parameterName": "`/output/image/param`",
					"dataType": "`aws:ec2:image`"
				}
			]
		}
	]
}
```

2. ###### Run the following command, using the file you created as input.

```
`aws imagebuilder create-distribution-configuration --cli-input-json file://`create-ami-distribution-configuration.json``
```

###### Note

    * You must include the `file://` notation
     at the beginning of the JSON file path.
    * The path for the JSON file should follow the appropriate
     convention for the base operating system where you are running
     the command. For example, Windows uses the backslash (\) to
     refer to the directory path, while Linux and macOS use the forward slash (/).

For more detailed information, see **[create-distribution-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-distribution-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-distribution-configuration.html")**
in the _AWS CLI Command Reference_.

## Update an AMI distribution configuration

You can change your AMI distribution configuration. However, the changes you make do
not apply to any resources that Image Builder has already distributed. For example, if you have
distributed an AMI to a Region that you later remove from your distribution, the AMI that
was already distributed remains in that Region until you remove it manually.

AWS Management Console
Follow these steps to an AMI distribution configuration in the AWS Management Console:

1. Open the EC2 Image Builder console at
   [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/").
2. Choose **Distribution settings**
   from the navigation pane. This shows a list of the
   distribution configurations that are created under your account.
3. To view details or update a distribution configuration, choose
   the **Configuration name** link. This opens the
   detail view for the distribution settings.

###### Note

You can also select the check box next to the
**Configuration name**, then choose
**View details**. 4. To edit distribution configuration, choose **Edit**
from the upper right corner of the **Distribution
details** section. Some fields are locked, such as the
**Name** of the distribution configuration, and the
default **Region** that is displayed as
**Region 1**. For more information about the distribution
configuration settings, see [Create an AMI distribution
configuration](#create-ami-distribution-config "#create-ami-distribution-config"). 5. Choose **Save changes** when you are done.

AWS CLI
The following example shows how to use the **[update-distribution-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/update-distribution-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/update-distribution-configuration.html")**
command to update distribution settings for your AMI, using the AWS CLI.

1. ###### Create a CLI input JSON file

Use a file-editing tool to create a JSON file with the keys shown in
the following example, and values that are valid for your environment. This
example uses a file named
`update-ami-distribution-configuration.json`.

```
{
	"distributionConfigurationArn": "arn:aws:imagebuilder:us-west-2:123456789012:distribution-configuration/update-ami-distribution-configuration.json",
	"description": "Copies AMI to eu-west-2, and specifies accounts that can launch instances in each Region.",
	"distributions": [
	  {
			"region": "us-west-2",
			"amiDistributionConfiguration": {
				"name": "Name {{imagebuilder:buildDate}}",
				"description": "An example image name with parameter references",
				"launchPermissions": {
					"userIds": [
						"987654321012"
					]
				}
			}
		},
		{
			"region": "eu-west-2",
			"amiDistributionConfiguration": {
				"name": "My {{imagebuilder:buildVersion}} image {{imagebuilder:buildDate}}",
				"tags": {
					"KeyName": "Some value"
				},
				"launchPermissions": {
					"userIds": [
						"100000000001"
					]
				}
			}
		}
	]
}
```

2. ###### Run the following command, using the file you created as input.

```
`aws imagebuilder update-distribution-configuration --cli-input-json file://`update-ami-distribution-configuration.json``
```

###### Note

    * You must include the `file://` notation
     at the beginning of the JSON file path.
    * The path for the JSON file should follow the appropriate
     convention for the base operating system where you are running
     the command. For example, Windows uses the backslash (\) to
     refer to the directory path, while Linux and macOS use the forward slash (/).

For more detailed information, see **[update-distribution-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/update-distribution-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/update-distribution-configuration.html")**
in the _AWS CLI Command Reference_. To update tags for your distribution configuration
resource, see the [Tag resources](tag-resources.md "tag-resources.md") section.

## Example: Enable EC2 Fast Launch with a launch template for

output AMIs

The following example shows how to use the **[create-distribution-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-distribution-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-distribution-configuration.html")**
command with a launch template to create distribution settings that have EC2 Fast Launch
configured for your AMI, from the AWS CLI.

To configure EC2 Fast Launch settings without a launch template, ensure that you've met all
of the [EC2 Fast Launch prerequisites](#ami-distribution-prereqs-fast-launch "#ami-distribution-prereqs-fast-launch") before you create your distribution
configuration.

1. ###### Create a CLI input JSON file

Use a file editing tool to create a JSON file with keys as shown in the
following example, plus values that are valid for your environment.

This example launches instances for all of its target resources simultaneously,
because the maximum number of parallel launches is greater than the target
resource count. This file is named
`ami-dist-config-win-fast-launch.json` in the command
example shown in the next step.

```
{
"name": "WinFastLaunchDistribution",
"description": "An example of Windows AMI EC2 Fast Launch settings in the distribution configuration.",
"distributions": [
	{
		"region": "us-west-2",
		"amiDistributionConfiguration": {
			"name": "Name {{imagebuilder:buildDate}}",
			"description": "Includes Windows AMI EC2 Fast Launch settings.",
			"amiTags": {
				"KeyName": "Some Value"
			}
		},
		"fastLaunchConfigurations": [{
			"enabled": true,
			"snapshotConfiguration": {
				"targetResourceCount": 5
			},
			"maxParallelLaunches": 6,
			"launchTemplate": {
				"launchTemplateId": "lt-0ab1234c56d789012",
				"launchTemplateVersion": "1"
			 }
		}],
		"launchTemplateConfigurations": [{
				   "launchTemplateId": "lt-0ab1234c56d789012",
				   "setDefaultVersion": true
		  }]
	}]
}
```

###### Note

You can specify the `launchTemplateName` instead of the
`launchTemplateId` in the `launchTemplate` section,
but you can't specify both the name and Id. 2. ###### Run the following command, using the file you created as input.

```
`aws imagebuilder create-distribution-configuration --cli-input-json file://`ami-dist-config-win-fast-launch.json``
```

###### Note

    * You must include the `file://` notation
     at the beginning of the JSON file path.
    * The path for the JSON file should follow the appropriate
     convention for the base operating system where you are running
     the command. For example, Windows uses the backslash (\) to
     refer to the directory path, while Linux and macOS use the forward slash (/).

For more detailed information, see **[create-distribution-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-distribution-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-distribution-configuration.html")**
in the _AWS CLI Command Reference_.

## Example: Create

distribution settings for output VM disks from the AWS CLI

The following example shows how to use the **create-distribution-configuration**
command to create distribution settings that will export VM image disks to Amazon S3 with every image build.

1. ###### Create a CLI input JSON file

You can streamline the
**create-distribution-configuration** command that you
use in the AWS CLI. To do this, create a JSON file that contains all of the
export configuration that you want to pass into the command.

###### Note

The naming convention for the data values in the JSON file follows the
pattern that is specified for the Image Builder API operation request parameters. To review the API operation request
parameters, see the **[CreateDistributionConfiguration](../APIReference/API_CreateDistributionConfiguration.md "../APIReference/API_CreateDistributionConfiguration.md")** command in
the _EC2 Image Builder API Reference_.

To provide the data values as command line parameters, refer to the
parameter names specified in the _AWS CLI Command Reference_. to the
**create-distribution-configuration** command as
options.

Here is a summary of the parameters that we specify in the
`s3ExportConfiguration` JSON object for this example:

    * roleName (string, required)
     – The name of the role that grants VM Import/Export permission to
     export images to your S3 bucket.
    * diskImageFormat (string, required)
     – Export the updated disk image to one of the following
     supported formats:




    	+ **Virtual Hard Disk (VHD)**
    	 – Compatible with Citrix Xen and Microsoft Hyper-V
    	 virtualization products.
    	+ **Stream-optimized ESX Virtual Machine
    	 Disk (VMDK)** – Compatible with VMware
    	 ESX and VMware vSphere versions 4, 5, and 6.
    	+ **Raw** – Raw
    	 format.
    * s3Bucket (string, required)
     – The S3 bucket in which to store the output disk images for
     your VM.

Save the file as `export-vm-disks.json`. Use the file
name in the **create-distribution-configuration**
command.

```
{
	"name": "example-distribution-configuration-with-vm-export",
	"description": "example",
	"distributions": [
		{
			"region": "us-west-2",
			"amiDistributionConfiguration": {
				"description": "example-with-vm-export"

			},
			"s3ExportConfiguration": {
				"roleName": "vmimport",
				"diskImageFormat": "RAW",
				"s3Bucket": "vm-bucket-export"
			}
		}],
	"clientToken": "abc123def4567ab"
}
```

2. ###### Run the following command, using the file you created as input.

```
`aws imagebuilder create-distribution-configuration --cli-input-json file://`export-vm-disks.json``
```

###### Note

    * You must include the `file://` notation
     at the beginning of the JSON file path.
    * The path for the JSON file should follow the appropriate
     convention for the base operating system where you are running
     the command. For example, Windows uses the backslash (\) to
     refer to the directory path, while Linux and macOS use the forward slash (/).

For more detailed information, see **[create-distribution-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-distribution-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-distribution-configuration.html")**
in the _AWS CLI Command Reference_.
