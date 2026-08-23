# Create a new version of an image recipe

This section shows you how to create an image recipe or a new version of an existing recipe.
An image recipe defines the base AMI, the build components, and the configuration. Use this recipe
to create Amazon Machine Images (AMIs) with Image Builder. You can create image recipes from the Image Builder
console or with the AWS CLI.

###### Contents

- [Create a new image recipe version from the console](#create-image-recipe-version-console "#create-image-recipe-version-console")
- [Create an image recipe with the AWS CLI](#create-image-recipe-cli "#create-image-recipe-cli")
- [Import a VM as your base image in the console](#import-vm-recipes "#import-vm-recipes")

## Create a new image recipe version from the console

When you create a new recipe version, it's virtually the same as creating a new recipe. The
difference is that certain details are pre-selected to match the base recipe, in most cases.
The following list describes the differences between creating a new recipe and creating a
new version of an existing recipe.

###### Base recipe details in the new version

- **Name** – _Not editable_.
- **Version** – Required. Enter the version number that you want to create
  in the format _<major>.<minor>.<patch>_. Image Builder supports automatic version incrementing for
  recipes, allowing you to use wildcard patterns in your recipe versions. When you create a recipe with
  a wildcard version such as `1.0.x`, Image Builder automatically increments the version
  (for example, `1.0.1`, `1.0.2`, `1.0.3`, and so on). This eliminates the need to manually track
  and increment recipe versions.
- The **Select image** option – Pre-selected, but you
  can edit it. If you change your choice for the source of your base image, you
  might lose other details that depend on the original option that you
  chose.

To see details that are associated with your base image selection, choose
the tab that matches your selection.

Managed image

    + **Image Operating System (OS)** –
     *Not editable*.
    + **Image name** – Pre-selected,
     based on the combination of base image choices that you made
     for the existing recipe. However, if you change the
     **Select image** option, you lose the
     pre-selected **Image name**.
    + **Auto-versioning options** – Does
     *not* match your base recipe. This
     image option defaults to the **Use selected OS
     version** option.


    ###### Important

    If you're using semantic versioning to kick off
     pipeline builds, make sure that you change this value to
     **Use latest available OS
     version**. To learn more about semantic versioning for Image Builder resources, see
     [Semantic versioning in Image Builder](ibhow-semantic-versioning.md "ibhow-semantic-versioning.md").

AWS Marketplace image

    + **Subscriptions** – This tab should
     be open, and the subscribed image from AWS Marketplace should be
     pre-selected to match your base recipe. If you change the
     image that your recipe uses as its base image, you might
     lose other details that depend on the original image that
     you chose.

For more information about AWS Marketplace products, see [Buying products](../../../marketplace/latest/buyerguide/buyer-subscribing-to-products.md "../../../marketplace/latest/buyerguide/buyer-subscribing-to-products.md")
in the _AWS Marketplace Buyer Guide_.

Custom AMI
**AMI source** (Required) - Enter the AMI ID or an AWS Systems Manager (SSM)
Parameter Store parameter that contains an AMI ID to use as the base image.
The SSM Agent must be pre-installed in the selected AMI.

    + **AMI ID** – This setting is not
     pre-filled with your original entry. Enter the AMI ID for
     your base image. Example: ``ami-1234567890abcdef1``.
    + **SSM parameter** – Enter the name or ARN
     of the SSM Parameter Store parameter that contains the AMI ID for
     your base image. Example: ``/ib/test/param`` or
     `arn:aws:ssm:`us-east-1`:`111122223333`:parameter`/ib/test/param``.

- **Instance configuration** – Settings are pre-selected,
  but you can edit them.

  - **Systems Manager agent** – You can select or clear this check
    box to control installation of the Systems Manager agent on the new image. By
    default, this check box stays clear, and Image Builder keeps the Systems Manager agent in your
    final AMI. To remove the Systems Manager agent from the final image, select the check
    box.
  - **User data** – You can use this area to provide
    commands, or a command script to run, when you launch your build
    instance. However, this value replaces any commands that Image Builder might have
    added to ensure that Systems Manager is installed. These commands include the
    clean-up script that Image Builder normally runs for Linux images prior to
    creating the new image.

  When Image Builder launches an instance, user data scripts run during the cloud-init
  phase, before component execution begins. This step is logged to the following
  file on the instance: `var/log/cloud-init.log`.

  ###### Note

        - If you enter user data, make sure that the Systems Manager agent is pre-installed
         on your base image, or that you include the install in your user data.
        - For Linux images, ensure that clean-up steps run by including a command to
         create an empty file named `perform_cleanup` in your user data script.
         Image Builder detects this file, and runs the clean-up script prior to creating the new image.
         For more information and a sample script, see [Security best practices for Image Builder](security-best-practices.md "security-best-practices.md").

- **Working directory** – Pre-selected, but
  you can edit it.
- **Components** – Components that are already
  included in the recipe are displayed in the **Selected components**
  section at the end of each of the component lists (build and test). You can remove
  or reorder the selected components to suit your needs.

CIS hardening components don't follow the standard component ordering rules in Image Builder
recipes. The CIS hardening components always run last to ensure that the benchmark tests run
against your output image.

###### Note

Build and test component lists display available components based
on the component owner type. To add a component, choose
**Add build components**, and select the ownership
filter that applies. For example, to add a build component that's
associated with an AWS Marketplace product, select `AWS Marketplace`. This opens
a selection panel on the right side of the console interface that lists AWS Marketplace
components.

For the CIS component, select `Third party managed`.

You can configure the
following settings for your selected component:

    + **Versioning options** – Pre-selected, but you
     can change them. We recommend that you choose the **Use latest available
     component version** option to ensure that your image builds
     always pick up the latest version of the component. If you need to use a
     specific component version in your recipe, you can choose **Specify
     component version**, and enter the version in the
     **Component version** box that appears.
    + **Input parameters** – Displays input parameters
     that the component accepts. The **Value** is pre-filled with
     the value from the prior version of the recipe. If you are using this component for the first time in this recipe, and
     a default value was defined for the input parameter, the default value appears in the
     **Value** box with greyed-out text. If no other value is entered, Image Builder
     uses the default value.


    If an input parameter is required, but doesn't have a
     default value defined in the component, you must provide a value. Image Builder won't
     create the recipe version if there are any required parameters that are missing
     and don't have a default value defined.


    ###### Important

    Component parameters are plain text values, and are logged
     in AWS CloudTrail. We recommend that you use AWS Secrets Manager or the AWS Systems Manager Parameter Store to store
     your secrets. For more information about Secrets Manager, see [What
     is Secrets Manager?](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") in the *AWS Secrets Manager User Guide*. For more information about
     AWS Systems Manager Parameter Store, see [AWS Systems Manager
     Parameter Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md") in the *AWS Systems Manager User Guide*.

To expand settings for **Versioning options**
or **Input parameters**, you can choose the arrow
next to the name of the setting. To expand all of the settings for
all selected components, you can toggle the **Expand all**
switch off and on.

- **Storage (volumes)** – are pre-filled. The root
  volume **Device name**, **Snapshot**, and
  **IOPS** selections, are not editable. However, you can
  change all of the remaining settings, such as the **Size**. You
  can also add new volumes, and encrypt new or existing volumes.

To encrypt volumes for the images that Image Builder creates under your account in the
source Region (where the build runs), you must use the storage volume encryption
in the image recipe. Encryption that runs during the distribution phase of the build
is only for images that are distributed to other accounts or Regions.

###### Note

If you use encryption for your volumes, you must select the key for each
volume separately, even if the key is the same one that's used for the root
volume.

###### Note

If you don't have an existing recipe, use the Image Builder pipeline wizard, or choose
**Image recipes** from the navigation pane and then choose
**Create image recipe**. The fields described in this section apply
to both new recipes and new versions.

###### To create a new image recipe version:

1. At the top of the recipe details page, choose **Create new
   version**. This opens the **Create image
   recipe** page.
2. To create the new version, make your changes, and then choose
   **Create recipe**.

Your final image can contain up to nine product codes from AWS Marketplace image products and
components. Image Builder returns an error during recipe creation if your base image and
components exceed this limit.

Review the following constraints before you create an image recipe:

- Your final image can contain at most nine AWS Marketplace product codes, combined from
  the base image and components. A product code is an identifier that AWS Marketplace attaches
  to a paid or supported AMI for billing and licensing.

###### Tip

Components published through AWS Marketplace can also carry product codes.
Image Builder reads the product codes from each component's metadata. It counts the distinct
product code IDs, along with the product codes on the base AMI, toward the limit.

To check the product codes on a base AMI, run the Amazon EC2
[describe-images](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-images.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-images.html")
command and query the `ProductCodes` field, as shown in the following
example:

```
aws ec2 describe-images --image-ids `ami-example12345` --query "Images[].ProductCodes"
```

- You can include up to 20 components (build and test combined). This is the
  default limit, which you can request to increase through AWS Support.
- The same component can't appear more than once in a recipe.
- All components must match the platform (Linux, Windows, or macOS) of your base
  image. Components must also support the OS version when that metadata is available.

For more information about creating an image recipe when you create an image
pipeline, see [Step 2: Choose recipe](start-build-image-pipeline.md#start-build-image-step2 "start-build-image-pipeline.md#start-build-image-step2") in the **Get
started** section of this guide.

## Create an image recipe with the AWS CLI

To create an image recipe with the Image Builder `create-image-recipe`
command in the AWS CLI, follow these steps:

###### Prerequisites

Before you run the Image Builder commands in this section to create an image recipe from the
AWS CLI, you can optionally create components that the recipe uses. The image recipe example
in the following step refers to example components that are created in the [Create a custom component from the AWS CLI](create-component.md#create-component-ib-cli "create-component.md#create-component-ib-cli") section
of this guide.

If you want to include components in your recipe, note the ARNs that you want to include.
You can also create recipes without any components for testing existing AMIs or distribution-only
workflows.

1. ###### Create a CLI input JSON file

You can provide all of the input for the **create-image-recipe** command
with inline command parameters. However, the resulting command can be quite
long. To streamline the command, you can instead provide a JSON file that
contains all of the recipe settings.

###### Note

The naming convention for the data values in the JSON file follows the
pattern that is specified for the Image Builder API operation request parameters. To review the API operation request
parameters, see the [CreateImageRecipe](../APIReference/API_CreateImageRecipe.md "../APIReference/API_CreateImageRecipe.md") command in the
_EC2 Image Builder API Reference_.

To provide the data values as command line parameters, refer to the
parameter names specified in the _AWS CLI Command Reference_.

Here is a summary of the parameters that these examples specify:

    * name (string, required) –
     The name of the image recipe.
    * description (string) –
     The description of the image recipe.
    * parentImage (string, required) – The image that
     the image recipe uses as a base for your customized image. You can specify the parent
     image using one of the following options:




    	+ **AMI ID** – Use when you have a
    	 specific AMI (for example, `ami-1234567890abcdef1`) that you want to
    	 customize. Because an AMI ID is static, we recommend an Image Builder image ARN or an SSM
    	 parameter instead when you want your recipe to pick up newer base images
    	 automatically.
    	+ **Image Builder image resource ARN** – Use when
    	 you want to build on top of an Image Builder image. This includes Amazon-managed images
    	 that Image Builder provides for the most popular operating systems, as well as images that
    	 you previously created. Specify the image ARN with a semantic version, or use a
    	 version wildcard to always get the latest version.
    	+ **AWS Systems Manager (SSM) Parameter Store parameter**
    	 – Use when you want your recipe to automatically pick up new AMI IDs
    	 without creating a new recipe version. Prefix the parameter with
    	 `ssm:`, followed by the parameter name or ARN. This is ideal for
    	 pipelines that should always use the latest Amazon Linux or Windows base
    	 image.
    	+ **AWS Marketplace product ID** – Use when you
    	 subscribe to an AMI product in AWS Marketplace and want to customize it further. You
    	 can specify the product ID in either of the following formats:




    		- A universally unique identifier (UUID), for example
    		 `722e1255-be34-4bbe-9ce6-80634c9d01f7`.
    		- A product ID with the `prod-` prefix, for example
    		 `prod-example12345`.
    	Subscribe to the product before you use it as a parent image. For more
    	 information, see [AWS Marketplace integration in Image Builder](integ-marketplace.md "integ-marketplace.md").
    ###### Note



    	+ When you use an AMI ID or an SSM parameter that resolves to an AMI, you
    	 must have access to that AMI in your account. The AMI must also exist in the
    	 same Region where Image Builder runs the build.
    	+ The Linux and macOS examples specify an AMI ID, and the Windows example uses
    	 an Image Builder image ARN.
    	+ The `parentImage` parameter accepts an AMI ID, an Image Builder image ARN,
    	 an `ssm:` parameter reference, or an AWS Marketplace product ID. If the value
    	 doesn't match one of these formats, Image Builder returns an
    	 `InvalidParameterValueException` for the `parentImage`
    	 parameter.
    * semanticVersion (string, required) – Enter the version number that you want to create
     in the format *<major>.<minor>.<patch>*. Image Builder supports automatic version incrementing for
     recipes, allowing you to use wildcard patterns in your recipe versions. When you create a recipe with
     a wildcard version such as `1.0.x`, Image Builder automatically increments the version
     (for example, `1.0.1`, `1.0.2`, `1.0.3`, and so on). This eliminates the need to manually track
     and increment recipe versions.
     To learn more about semantic versioning for Image Builder resources, see
     [Semantic versioning in Image Builder](ibhow-semantic-versioning.md "ibhow-semantic-versioning.md").
    * components (array, optional) –
     Contains an array of `ComponentConfiguration` objects. Components
     are optional - you can create recipes without any components for testing or
     distribution workflows:


    ###### Note

    Image Builder installs components in the order that you specified them in the recipe.
     However, CIS hardening components always run last to ensure that the benchmark
     tests run against your output image.




    	+ componentARN (string, required)
    	 – The component ARN.


    	###### Tip

    	To use one of the examples to create your own image recipe, you must replace the
    	 example ARNs with the ARNs for the components that you are
    	 using for your recipe.
    	+ parameters (array of objects)
    	 – Contains an array of `ComponentParameter` objects.
    	 If an input parameter is required, but doesn't have a
    	 default value defined in the component, you must provide a value. Image Builder won't
    	 create the recipe version if there are any required parameters that are missing
    	 and don't have a default value defined.


    	###### Important

    	Component parameters are plain text values, and are logged
    	 in AWS CloudTrail. We recommend that you use AWS Secrets Manager or the AWS Systems Manager Parameter Store to store
    	 your secrets. For more information about Secrets Manager, see [What
    	 is Secrets Manager?](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") in the *AWS Secrets Manager User Guide*. For more information about
    	 AWS Systems Manager Parameter Store, see [AWS Systems Manager
    	 Parameter Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md") in the *AWS Systems Manager User Guide*.




    		- name (string, required)
    		 – The name of the component parameter to set.
    		- value (array of strings, required)
    		 – Contains an array of strings to set the value
    		 for the named component parameter. If there is a default value defined for the component,
    		 and no other value is provided, AWSTOE uses the default value.
    * amiWatermarks (array of strings, optional) –
     A list of watermark names to attach to output AMIs built from this recipe.
     Watermarks are lineage markers that help you trace the history
     of your images. Specify 1 to 5 names. Each name must be 3 to 128 characters,
     and can include letters, numbers, spaces, and the following special characters:
     `( ) [ ] . / - ' @ _`. For more information, see
     [Track AMI lineage with watermarks](ami-watermarks.md "ami-watermarks.md").
    * additionalInstanceConfiguration (object) –
     Specify additional settings and launch scripts for your build instances.




    	+ systemsManagerAgent (object) –
    	 Contains settings for the Systems Manager agent on your build instance.


    	###### Note

    	Windows recipes don't support the `systemsManagerAgent`
    	 configuration. If you include it with a Windows parent image, the request
    	 fails.




    		- uninstallAfterBuild (Boolean) – Controls
    		 whether the Systems Manager agent is removed from your final build
    		 image prior to creating the new AMI. If this option is
    		 set to `true`, then the agent is removed from
    		 the final image. If the option is set to
    		 `false`, then the agent is left in so
    		 that it is included in the new AMI. The default value is
    		 `false`.


    		###### Note

    		If the `uninstallAfterBuild` attribute isn't included in the JSON file,
    		 and the following conditions are true, then Image Builder
    		 removes the Systems Manager agent from the final image so that
    		 it isn't available in the AMI:



    			* The `userDataOverride` is empty or has been omitted from the JSON
    			 file.
    			* Image Builder automatically installed the Systems Manager agent on the build instance for an
    			 operating system that didn't have the agent
    			 pre-installed on the base image.
    	+ userDataOverride (string) –
    	 Provide commands or a command script to run when you launch your
    	 build instance.


    	###### Note

    	The user data is always base 64 encoded. For example, the
    	 following commands are encoded as `IyEvYmluL2Jhc2gKbWtkaXIgLXAgL3Zhci9iYi8KdG91Y2ggL3Zhcg==`:


    	```
    	#!/bin/bash
    	mkdir -p /var/bb/
    	touch /var
    	```
    	The Linux example uses this encoded value.

Linux
The base image (`parentImage` property) in the following example
is an AMI. When you use an AMI, you must have access to the AMI, and the AMI
must be in the source Region (the same Region where Image Builder runs the command).
Save the file as `create-image-recipe.json`, and use it in
the **create-image-recipe** command.

```
{
"name": "`BB Ubuntu Image recipe`",
"description": "`Hello World image recipe for Linux.`",
"parentImage": "`ami-1234567890abcdef1`",
"semanticVersion": "1.0.0",
"components": [
	{
		"componentArn": "arn:aws:imagebuilder:`us-west-2`:`111122223333`:component/`bb$`"
	}
],
"additionalInstanceConfiguration": {
	"systemsManagerAgent": {
	 	"uninstallAfterBuild": true
	},
	"userDataOverride": "IyEvYmluL2Jhc2gKbWtkaXIgLXAgL3Zhci9iYi8KdG91Y2ggL3Zhcg=="
}
}
```

Windows
The following example refers to the latest version of the Windows Server 2016 English
Full Base image. The ARN in this example references the latest image
based on the semantic version filters that you've specified:
`arn:aws:imagebuilder:`us-west-2`:aws:image/`windows-server-2016-english-full-base-x86/x.x.x``.

```
{
"name": "`MyBasicRecipe`",
"description": "`This example image recipe creates a Windows 2016 image.`",
"parentImage": "arn:aws:imagebuilder:`us-west-2`:aws:image/`windows-server-2016-english-full-base-x86/x.x.x`",
"semanticVersion": "1.0.0",
"components": [
	{
		"componentArn": "arn:aws:imagebuilder:`us-west-2`:`111122223333`:component/`my-example-component/2019.12.02/1`"
	},
	{
		"componentArn": "arn:aws:imagebuilder:`us-west-2`:`111122223333`:component/`my-imported-component/1.0.0/1`"
	}
]
}
```

###### Note

To learn more about semantic versioning for Image Builder resources, see
[Semantic versioning in Image Builder](ibhow-semantic-versioning.md "ibhow-semantic-versioning.md").

macOS
The base image (`parentImage` property) in the following example
is an AMI. When you use an AMI, you must have access to the AMI, and the AMI
must be in the source Region (the same Region where Image Builder runs the command).
Save the file as `create-image-recipe.json`, and use it in
the **create-image-recipe** command.

```
{
"name": "`macOS Catalina Image recipe`",
"description": "`Hello World image recipe for macOS.`",
"parentImage": "`ami-1234567890abcdef1`",
"semanticVersion": "1.0.0",
"components": [
	{
		"componentArn": "arn:aws:imagebuilder:`us-west-2`:`111122223333`:component/`catalina$`"
	}
],
"additionalInstanceConfiguration": {
	"systemsManagerAgent": {
	 	"uninstallAfterBuild": true
	},
	"userDataOverride": "IyEvYmluL2Jhc2gKbWtkaXIgLXAgL3Zhci9iYi8KdG91Y2ggL3Zhcg=="
}
}
```

**Example: Recipe without components**

You can create recipes without any components for testing existing AMIs or
distribution-only workflows. The following example shows a recipe that uses
an existing AMI without applying any additional components:

```
{
	"name": "`Test Distribution Recipe`",
	"description": "`Recipe for testing and distributing existing AMI without modifications.`",
	"parentImage": "`ami-1234567890abcdef1`",
	"semanticVersion": "1.0.0",
	"additionalInstanceConfiguration": {
		"systemsManagerAgent": {
		 	"uninstallAfterBuild": true
		}
	}
}
```

2. ###### Create the recipe

Use the following command to create the recipe. Provide the name of the JSON file that you
created in the prior step in the `--cli-input-json` parameter:

```
aws imagebuilder create-image-recipe --cli-input-json file://`create-image-recipe.json`
```

###### Note

    * You must include the `file://` notation
     at the beginning of the JSON file path.
    * The path for the JSON file should follow the appropriate
     convention for the base operating system where you are running
     the command. For example, Windows uses the backslash (\) to
     refer to the directory path, while Linux and macOS use the forward slash (/).

Your final image can contain up to nine product codes from AWS Marketplace image products and
components. Image Builder returns an error during recipe creation if your base image and
components exceed this limit when you run the `create-image-recipe` command.

The command returns the ARN of the new image recipe, as shown in the following
example output.

```
{
	"requestId": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`",
	"clientToken": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`",
	"imageRecipeArn": "arn:aws:imagebuilder:us-west-2:`123456789012`:image-recipe/`my-recipe`/1.0.1"
}
```

3. ###### Verify your recipe

To confirm that Image Builder created your recipe as expected, run the
**get-image-recipe** command with the ARN that the previous step
returned.

```
aws imagebuilder get-image-recipe --image-recipe-arn arn:aws:imagebuilder:us-west-2:`123456789012`:image-recipe/`my-recipe`/1.0.1
```

### Working directory

The working directory specifies the filesystem path on the build instance where Image Builder
runs build and test operations. Image Builder passes this path to AWS Systems Manager as the working
directory for command execution.

If you don't specify a working directory, Image Builder uses the following defaults:

- Linux: `/tmp`
- macOS: `/tmp`
- Windows: `C:/`

For Windows, the path can't contain the double-quote (`"`)
character.

###### Tip

Set the working directory to a path on a larger attached volume when your
components need more temporary disk space during installation than the default
directory provides.

### AMI tags

You can apply tags to the AMI that Image Builder creates during the build phase, before image
distribution. Image Builder applies these tags to the AMI, separate from the resource tags
on the recipe itself. Specify AMI tags with the `amiTags` parameter in
your JSON input file.

###### Note

You can't use the reserved tag keys `CreatedBy` or
`Ec2ImageBuilderArn`. Image Builder manages these keys automatically.

```
{
	"name": "`tagged-recipe`",
	"semanticVersion": "1.0.0",
	"parentImage": "arn:aws:imagebuilder:us-west-2:aws:image/`amazon-linux-2023-x86`/x.x.x",
	"components": [
		{
			"componentArn": "arn:aws:imagebuilder:us-west-2:aws:component/`update-linux`/x.x.x"
		}
	],
	"amiTags": {
		"Environment": "Production",
		"Team": "Platform",
		"CostCenter": "12345"
	}
}
```

### Common errors and troubleshooting

The following table lists common errors that you might encounter when you create an
image recipe, along with how to resolve them.

| Error                                                                                         | Cause                                                                        | Resolution                                                                                        |
| --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| "A component may be specified in an image recipe at most once"                                | A duplicate component (even with a different version).                       | Remove the duplicate. Use only one version of each component.                                     |
| "Component ARN does not match the Parent Image Platform"                                      | A platform mismatch.                                                         | Verify your base image platform. Use Linux components with Linux AMIs,<br>and so on.              |
| "Component ARN does not support the Parent Image OS Version"                                  | An OS version incompatibility.                                               | Check the component's supported OS versions. Use a compatible component<br>version.               |
| "Image Builder does not support configuring the SSM Agent on<br>Windows"                      | You specified `systemsManagerAgent` with a Windows parent<br>image.          | Remove the<br>`additionalInstanceConfiguration.systemsManagerAgent`<br>block.                     |
| "You've exceeded the maximum cumulative component size of 25 KB"                              | Too many or too-large parameters.                                            | Reduce the parameter count or shorten parameter values.                                           |
| "Recipe can contain at most 9 marketplace products"                                           | Too many AWS Marketplace product codes.                                      | Reduce the number of AWS Marketplace components, or use a base image with fewer<br>product codes. |
| "Recipes with marketplace components must contain at least 1 build<br>component"              | The recipe references AWS Marketplace components but has no build component. | Add at least one build component to the recipe.                                                   |
| "The supplied semantic version does not follow the required<br>format"                        | An invalid version string.                                                   | Use the *major.minor.patch<br>• format with one optional<br>`x` wildcard.                         |
| "Component ARN ... is deprecated and cannot be included in new<br>recipes" (or "is disabled") | A referenced component has a `DEPRECATED` or<br>`DISABLED` status.           | Update to a current component version.                                                            |

## Import a VM as your base image in the console

This section shows you how to import a virtual machine (VM) as the base image for
your image recipe. It doesn't cover other steps involved with creating a recipe or
recipe version here. For additional steps to create a new image recipe with the
pipeline creation wizard in the Image Builder console, see [Pipeline wizard: Create AMI](start-build-image-pipeline.md "start-build-image-pipeline.md"). For additional steps to
create a new image recipe or recipe version, see [Create a new version of an image recipe](create-image-recipes.md "create-image-recipes.md").

To import a VM as the base image for your image recipe in the Image Builder console, follow these
steps, along with any other required steps, to create your recipe or recipe
version.

1. In the **Select image** section for the base image, select
   the **Import base image** option.
2. Choose the **Image Operating System (OS)** and **OS
   version** as you normally would.

### VM import configuration

When you export your VM from its virtualization environment, that process creates a set
of one or more disk container files that act as snapshots of your VM environment,
settings, and data. You can use these files to import your VM as the base image for
your image recipe. For more information about importing VMs in Image Builder, see [Import and export VM images](vm-import-export.md "vm-import-export.md")

To specify the location of your import source, follow these steps:

###### Import source

Specify the source for the first VM image disk container or snapshot to import in
the **Disk container 1** section.

1. **Source** – This can be either an S3 bucket or an
   EBS snapshot.
2. **Select S3 location of disk** – Enter
   the location in Amazon S3 where your disk images are stored. To browse for the location,
   choose **Browse S3**.
3. To add a disk container, choose **Add disk container**.

###### IAM role

To associate an IAM role with your VM import configuration, select the role from the
**IAM role** dropdown list, or choose **Create new role**
to create a new one. If you create a new role, the IAM Roles console page opens in a
separate tab.

#### Advanced settings – _optional_

The following settings are optional. With these settings, you can configure
encryption, licensing, tags, and more for the base image that the import
creates.

###### General

1. Specify a unique **Name** for the base image. If you
   do not enter a value, the base image inherits the recipe name.
2. Specify a **Version** for the base image. Use the following format:
   `*<major>.<minor>.<patch>*`.
   If you do not enter a value, the base image inherits the recipe
   version.
3. You can also enter a **Description** for the base
   image.

###### Base image architecture

To specify the architecture of your VM import source, select a value
from the **Architecture** list.

###### Encryption

If your VM disk images are encrypted, you must provide a key to use for the import
process. To specify an AWS KMS key for the import, select a value from
the **Encryption (KMS key)** list. The list contains
KMS keys that your account has access to in the current Region.

###### License management

When you import a VM, the import process automatically detects the VM OS and applies
the appropriate license to the base image. Depending on your OS
platform, the license types are as follows:

- **License included** – An appropriate AWS
  license for your platform is applied to your base image.
- **Bring your own license (BYOL)** – Retains
  the license from your VM, if applicable.

To attach license configurations created with AWS License Manager to your base image, select from
the **License configuration name** list. For more information about License Manager,
see [Working with license
configurations](../../../license-manager/latest/userguide/license-configurations.md "../../../license-manager/latest/userguide/license-configurations.md") in the _License Manager User Guide_.

###### Note

- License configurations contain licensing rules based on the terms of your
  enterprise agreements.
- Linux only supports BYOL licenses.

###### Tags (base image)

Tags use key-value pairs to assign searchable text to your Image Builder resource. To specify
tags for the imported base image, enter key-value pairs with the
**Key** and **Value** boxes.

To add a tag, choose **Add tag**. To remove a tag, choose
**Remove tag**.
