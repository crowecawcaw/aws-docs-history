# Create a new version of an image recipe

This section describes how to create a new version of an image recipe.

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
- **Version** – Required. This base detail isn't
  pre-filled with the current version or any kind of a sequence. Enter the version
  number that you want to create in the format
  _<major>.<minor>.<patch>_. If the version already exists, you
  encounter an error.
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
    box to control installation of the Systems Manager agent on the new image. The
    check box is cleared by default to include the Systems Manager agent in your new
    image. To remove the Systems Manager agent from the final image, select the check
    box so that the agent isn't included in your AMI.
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

###### To create a new image recipe version:

1. At the top of the recipe details page, choose **Create new
   version**. This takes you to the **Create image
   recipe** page.
2. To create the new version, make your changes, and then choose
   **Create recipe**.

Your final image can contain up to four product codes from AWS Marketplace image products and
components. If your selected base image and components contain more than four product
codes, Image Builder returns an error when you try to create the recipe.

For more information on how to create an image recipe when you create an image
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




    	+ AMI ID
    	+ Image Builder image resource ARN
    	+ AWS Systems Manager (SSM) Parameter Store parameter, prefixed by `ssm:`,
    	 followed by the parameter name or ARN.
    	+ AWS Marketplace product ID
    ###### Note

    The Linux and macOS examples use an Image Builder AMI, and the Windows example uses an ARN.
    * semanticVersion (string, required) – The semantic
     version of the image recipe, expressed in the following format, with
     numeric values in each position to indicate a specific version:
     *<major>.<minor>.<patch>*. For
     example a value might be `1.0.0`.
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
    * additionalInstanceConfiguration (object) –
     Specify additional settings and launch scripts for your build instances.




    	+ systemsManagerAgent (object) –
    	 Contains settings for the Systems Manager agent on your build instance.




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

Your final image can contain up to four product codes from AWS Marketplace image products and
components. If your selected base image and components contain more than four product
codes, Image Builder returns an error when run the `create-image-recipe` command.

## Import a VM as your base image in the console

In this section, we focus on how to import a virtual machine (VM) as the base image for
your image recipe. We don't cover other steps involved with creating a recipe or
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

#### Advanced settings –

_optional_

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
see Working with AWS License Manager

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
