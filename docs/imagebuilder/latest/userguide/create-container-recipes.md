# Create a new version of a container recipe

This section shows you how to create a container recipe or a new version of an existing
recipe. A container recipe defines three key elements: the base image, the build components, and
the target repository. Use this recipe to produce Docker container images that Image Builder stores in
Amazon ECR.

###### Contents

- [Create a new container recipe version with the console](#create-container-recipe-version "#create-container-recipe-version")
- [Create a container recipe with the AWS CLI](#create-container-recipe-cli "#create-container-recipe-cli")

## Create a new container recipe version with the console

Creating a new version of a container recipe is virtually the same as creating a new
recipe. The difference is that certain details are pre-selected to match the base
recipe, in most cases. The following list describes the differences between creating a
new recipe and creating a new version of an existing recipe.

###### Recipe details

- **Name** – _not
  editable_.
- **Version** – Required. This detail isn't pre-filled
  with the current version or any kind of a sequence. Enter the version number
  that you want to create in the format _major.minor.patch_. If
  the version already exists, Image Builder returns an error.

###### Base image

- **Select image** option – Pre-selected, but editable.
  If you change your choice for the source of your base image, you might lose
  other details that depend on the original option that you chose.

For Docker container images, you can choose from public images hosted on DockerHub,
existing container images in Amazon ECR, or Amazon-managed container images. To see details
that are associated with your base image selection, choose the tab that matches
your selection.

Managed images

    + **Image Operating System (OS)** –
     *Not editable*.
    + **Image name** – Pre-selected,
     based on the combination of base image choices that you made
     for the existing recipe. However, if you change the
     **Select image** option, you lose the
     pre-selected **Image name**.
    + **Auto-versioning options** – Does
     *not* match your base recipe.
     Auto-versioning options defaults to the **Use
     selected OS version** option.


    ###### Important

    If you're using semantic versioning to kick off
     pipeline builds, make sure that you change this value to
     **Use latest available OS
     version**. To learn more about semantic versioning for Image Builder resources, see
     [Semantic versioning in Image Builder](ibhow-semantic-versioning.md "ibhow-semantic-versioning.md").

ECR image

    + **Image Operating System (OS)** –
     Pre-selected, but editable.
    + **OS version** – Pre-selected,
     but editable.
    + **ECR image ID** – Pre-filled,
     but editable.

Docker Hub image

    + **Image Operating System (OS)** –
     *Not editable*.
    + **OS version** – Pre-selected,
     but editable.
    + **Docker image ID** – Pre-filled,
     but editable.

###### Instance configuration

- **AMI source** (Required) – Identify a custom AMI to use as
  the base image for your container build and test instance. This can be an AMI ID or an
  AWS Systems Manager (SSM) Parameter Store parameter that contains an AMI ID.

  - **AMI ID** – This setting is not
    pre-filled with your original entry. Enter the AMI ID for
    your base image. Example: `ami-1234567890abcdef1`.
  - **SSM parameter** – Enter the name or ARN
    of the SSM Parameter Store parameter that contains the AMI ID for
    your base image. Example: `/ib/test/param` or
    `arn:aws:ssm:`us-east-1`:`111122223333`:parameter`/ib/test/param``.

- ###### Storage (volumes)

**EBS volume 1 (AMI root)** – Pre-filled. You can't edit
the root volume **Device name**,
**Snapshot**, or **IOPS** selections.
However, you can change all of the remaining settings, such as the
**Size**. You can also add new volumes.

###### Note

If you specified a base AMI that was shared with you from
another account, the snapshots for any secondary volumes that are
specified must also be shared with your account.

###### Working directory

- **Working directory path** – Pre-filled,
  but editable.

###### Components

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

###### Dockerfile template

- **Dockerfile template** – Pre-filled,
  but editable. You can specify any of the following contextual variables
  that Image Builder replaces with build information at runtime.

 

**parentImage (required)**

At build time, this variable resolves to the base image for your
recipe.

Example:

```
FROM
{{{ imagebuilder:parentImage }}}
```

**environments (required if components are specified)**

At build time, this variable resolves to the Dockerfile directives that
stage your components in the build context. These directives copy the component
scripts into the image and set the environment variables that those scripts use.
It prepares the environment but doesn't run the components that you specify. Place this
variable before the `components` variable.

Example:

```
{{{ imagebuilder:environments }}}
```

**components (optional)**

At build time, this variable resolves to the command that runs the build
and test component scripts for the components that the container recipe
includes, and then removes those scripts from the image. This is the
variable that runs your components. Place it after the
`environments` variable.

Example:

```
{{{ imagebuilder:components }}}
```

###### Target repository

- **Target repository name** – The Amazon ECR repository where your
  output image is stored if there is no other repository specified in your
  pipeline's distribution configuration for the Region where the pipeline runs
  (Region 1).

###### To create a new container recipe version:

1. On the container recipe details page, choose **Create
   new version** at the top of the page. The console opens the **Create
   recipe** page for container recipes.
2. To create the new version, make your changes, and then choose
   **Create recipe**.

For more information about creating a container recipe when you create an image
pipeline, see [Step 2: Choose recipe](start-build-container-pipeline.md#start-build-container-step2 "start-build-container-pipeline.md#start-build-container-step2") in the **Get
started** section of this guide.

## Create a container recipe with the AWS CLI

To create an Image Builder container recipe with the `imagebuilder
 create-container-recipe` command in the AWS CLI, follow these steps:

###### Prerequisites

Before you run the Image Builder commands in this section to create a container recipe with
the AWS CLI, you must create the components that the recipe will use. The container
recipe example in the following step refers to example components that are created
in the [Create a custom component from the AWS CLI](create-component.md#create-component-ib-cli "create-component.md#create-component-ib-cli")
section of this guide.

After you create your components, or if you are using existing components, note the
ARNs that you want to include in the recipe.

1. ###### Create a CLI input JSON file

You can provide all of the input for the
**create-container-recipe** command with inline command
parameters. However, the resulting command can be quite long. To streamline the
command, you can instead provide a JSON file that contains all of the container
recipe settings

###### Note

The naming convention for the data values in the JSON file follows the
pattern that is specified for the Image Builder API operation request parameters. To review the API operation request
parameters, see the [CreateContainerRecipe](../APIReference/API_CreateContainerRecipe.md "../APIReference/API_CreateContainerRecipe.md") command in the
_EC2 Image Builder API Reference_.

To provide the data values as command line parameters, refer to the
parameter names specified in the _AWS CLI Command Reference_.

Here is a summary of the parameters in this example:

    * components (array of objects, optional)
     – Contains an array of `ComponentConfiguration`
     objects. Components are optional for container recipes. You can customize the
     output image with BUILD components, with instructions in your Dockerfile
     template (for example, `RUN` or `COPY` statements), or
     both. TEST components validate the image but don't modify it.


    ###### Note

    Image Builder installs components in the order that you specified them in the recipe.
     However, CIS hardening components always run last to ensure that the benchmark
     tests run against your output image.




    	+ componentARN (string, required)
    	 – The component ARN.


    	###### Tip

    	To use the example to create your own container recipe,
    	 replace the example ARNs with the ARNs for the components
    	 that you are using for your recipe,. These include the
    	 AWS Region, name, and the version number for each.
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
    * containerType (string, required)
     – The type of container to create. Valid values include
     `DOCKER`.
    * dockerfileTemplateData (string)
     – The inline Dockerfile template for building your image. Inline
     data is limited to 16,000 characters. You must specify either
     `dockerfileTemplateData` or `dockerfileTemplateUri`,
     but not both.


    Your Dockerfile template can include contextual variables (placeholders that Image Builder
     replaces with build information at runtime). Include at least the
     `parentImage` variable. If your recipe includes components, also include the
     `environments` variable and the `components` variable.




    **parentImage (required)**

    At build time, this variable resolves to the base image for your
     recipe.


    Example:



    ```
    FROM
    {{{ imagebuilder:parentImage }}}
    ```


    **environments (required if components are specified)**

    At build time, this variable resolves to the Dockerfile directives that
     stage your components in the build context. These directives copy the component
     scripts into the image and set the environment variables that those scripts use.
     It prepares the environment but doesn't run the components that you specify. Place this
     variable before the `components` variable.


    Example:



    ```
    {{{ imagebuilder:environments }}}
    ```


    **components (optional)**

    At build time, this variable resolves to the command that runs the build
     and test component scripts for the components that the container recipe
     includes, and then removes those scripts from the image. This is the
     variable that runs your components. Place it after the
     `environments` variable.


    Example:



    ```
    {{{ imagebuilder:components }}}
    ```



    To store the template in Amazon S3 instead, use the
     dockerfileTemplateUri parameter with a valid
     Amazon S3 URI (for example,
     `s3://`my-bucket`/templates/Dockerfile`).
    * name (string, required) – The
     name of the container recipe.
    * description (string) – The
     description of the container recipe.
    * parentImage (string, required) –
     The Docker container image to use in the container recipe as a baseline
     for your customized image.




    	+ Public images hosted on DockerHub
    	+ Existing container images in Amazon ECR
    	+ Amazon-managed container images
    * platformOverride (string) –
     Specifies the operating system platform when you use a custom base image. We
     recommend that you set this value when you use a Docker Hub or Amazon ECR image. If
     you omit it, Image Builder attempts to detect the platform from the container manifest,
     which might not always be available. You can't specify `platformOverride`
     when your parent image is an Image Builder image ARN. Valid values are `Linux`
     and `Windows`. Container recipes don't support the macOS platform.
    * semanticVersion (string, required)
     – The semantic version of the container recipe specified in the
     following format, with numeric values in each position to indicate a
     specific version:
     *<major>.<minor>.<patch>*. An
     example would be `1.0.0`. To learn more about semantic versioning for Image Builder resources, see
     [Semantic versioning in Image Builder](ibhow-semantic-versioning.md "ibhow-semantic-versioning.md").
    * tags (string map) – Tags that
     are attached to the container recipe.
    * instanceConfiguration (object) –
     A group of options that can be used to configure an instance for
     building and testing container images.




    	+ image (string) – The base image
    	 for a container build and test instance. This can contain an AMI ID or it
    	 can specify an AWS Systems Manager (SSM) Parameter Store parameter, prefixed by
    	 `ssm:`, followed by the parameter name or ARN. If you use an SSM
    	 parameter, the parameter value must contain an AMI ID. If you don't specify
    	 a base image, Image Builder uses the appropriate Amazon ECS optimized AMI as a base image.
    	+ blockDeviceMappings (array of
    	 objects) – Defines the block devices to attach for
    	 building an instance from the Image Builder AMI specified in the
    	 **image** parameter.




    		- deviceName (string)
    		 – The device that these mappings apply to.
    		- ebs (object) –
    		 Used to manage Amazon EBS specific configuration for this
    		 mapping.




    			* deleteOnTermination (Boolean) –
    			 Used to configure delete on termination of the
    			 associated device.
    			* encrypted
    			 (Boolean) – Used to configure device
    			 encryption.
    			* volumeSize
    			 (integer) – Used to override the device's
    			 volume size.
    			* volumeType
    			 (string) – Used to override the device's
    			 volume type.
    * targetRepository (object, required)
     – The destination repository for the container image if there is
     no other repository specified in your pipeline's distribution
     configuration for the Region where the pipeline runs (Region 1).




    	+ repositoryName (string,
    	 required) – The name of the container repository where
    	 the output container image is stored. This name is prefixed by
    	 the repository location.
    	+ service (string, required)
    	 – Specifies the repository service that stores the output image. The
    	 valid value is `ECR`. The target repository must already
    	 exist.
    * workingDirectory (string) – The
     working directory for use during build and test workflows.

The following example shows a complete container recipe input file that defines a Linux Docker container with build components. Save it as
`create-container-recipe.json`, and use it in the
**create-container-recipe** command.

```
{
	"components": [
	  {
		 "componentArn": "arn:aws:imagebuilder:`us-west-2`:`111122223333`:component/helloworldal2/x.x.x"
	  }
	],
	"containerType": "DOCKER",
	"description": "My Linux Docker container image",
	"dockerfileTemplateData": "FROM {{{ imagebuilder:parentImage }}}\n{{{ imagebuilder:environments }}}\n{{{ imagebuilder:components }}}",
	"name": "amazonlinux-container-recipe",
	"parentImage": "amazonlinux:latest",
	"platformOverride": "Linux",
	"semanticVersion": "1.0.2",
	"tags": {
	  "sometag" : "Tag detail"
	},
	"instanceConfiguration": {
	  "image": "ami-1234567890abcdef1",
	  "blockDeviceMappings": [
		 {
			"deviceName": "/dev/xvda",
			"ebs": {
				"deleteOnTermination": true,
				"encrypted": false,
				"volumeSize": 8,
				"volumeType": "gp2"
			 }
		  }
	  ]
	},
	"targetRepository": {
	  "repositoryName": "myrepo",
	  "service": "ECR"
	},
	"workingDirectory": "/tmp"
}
```

2. ###### Create the recipe

Use the following command to create the recipe. Provide the name of the JSON file that you
created in the prior step in the `--cli-input-json` parameter:

```
aws imagebuilder create-container-recipe --cli-input-json file://`create-container-recipe.json`
```

###### Note

    * You must include the `file://` notation
     at the beginning of the JSON file path.
    * The path for the JSON file should follow the appropriate
     convention for the base operating system where you are running
     the command. For example, Windows uses the backslash (\) to
     refer to the directory path, while Linux and macOS use the forward slash (/).

The following example output shows the ARN of the newly created container recipe,
along with the request ID and client token for the request.

```
{
	"requestId": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`",
	"clientToken": "`a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`",
	"containerRecipeArn": "arn:aws:imagebuilder:us-west-2:`123456789012`:container-recipe/`my-container-recipe`/1.0.2"
}
```

### Container recipe constraints

Review the following constraints before you create a container recipe:

- You must specify a target Amazon ECR repository that already exists.
- AWS Marketplace components aren't supported in container recipes.
- Components are optional. You can customize the output image with BUILD
  components, with instructions in your Dockerfile template (for example,
  `RUN` or `COPY` statements), or both. TEST components
  validate the image but don't modify it.
- Container recipes don't support the macOS platform.
- For the Dockerfile template, provide either inline data (up to 16,000
  characters) or an Amazon S3 URI. You can't specify both.
- The cumulative recipe size can't exceed 25 KB. If you receive a size error,
  reduce the number of component parameters or shorten parameter values. This limit
  is separate from the Dockerfile template size limits.
- When you set `platformOverride` to `Windows`, you must also
  specify `imageOsVersionOverride`. This applies to any non-Image Builder parent
  image, such as an Amazon ECR image or a Docker Hub image.

### Common errors and troubleshooting

The following table lists common errors that you might encounter when you create a
container recipe, along with how to resolve them.

| Error                                                                                                                   | Cause                                                  | Resolution                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| "Container Recipes must not contain marketplace components"                                                             | A AWS Marketplace component in a container recipe.     | Use only non-AWS Marketplace components.                                                         |
| "Container recipes don't currently support the macOS platform"                                                          | `platformOverride` is set to macOS.                    | Use `Linux` or `Windows`.                                                                        |
| "You must specify either dockerfileTemplateData or a<br>dockerfileTemplateUri"                                          | You specified both or neither.                         | Provide exactly one.                                                                             |
| "Invalid S3 URI"                                                                                                        | A malformed Amazon S3 path in `dockerfileTemplateUri`. | Use the format<br>`s3://`bucket`/`key``.                                                         |
| "You cannot specify a platform override when using an Image Builder<br>Image as your parent"                            | `platformOverride` with an Image Builder image ARN.    | Remove `platformOverride`. Image Builder detects the platform from the<br>parent image metadata. |
| "You must specify an image OsVersion override when using ECR Repositories<br>as your parent image for Windows Platform" | A Windows `platformOverride` without an OS version.    | Add the `imageOsVersionOverride` field.                                                          |
