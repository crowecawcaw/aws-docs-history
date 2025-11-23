# Create a custom component with Image Builder

After you've completed your component document, you can use it to create a custom
component that your Image Builder recipes can use. You can create a custom component from the
Image Builder console, from the API or SDKs, or from the command line. For more information
about how to create a custom component with input parameters and use it in your recipes, see
[Tutorial: Create a custom component with input parameters](tutorial-component-parameters.md "tutorial-component-parameters.md").

The following sections show you how to create components from the console or from the AWS CLI.

###### Contents

- [Create a custom component from the console](#create-component-ib-console "#create-component-ib-console")
- [Create a custom component from the AWS CLI](#create-component-ib-cli "#create-component-ib-cli")
- [Import a script to create a component from the AWS CLI](#import-component-cli "#import-component-cli")
- [Automatic build version management](#auto-build-version-management "#auto-build-version-management")
- [Using version references](#using-version-references "#using-version-references")

## Create a custom component from the console

To create an AWSTOE application component from the Image Builder console, follow these steps:

1. Open the EC2 Image Builder console at
   [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/").
2. Select **Components** from the navigation pane.
   Then select **Create component**.
3. On the **Create component** page, under **Component details**, enter the following:
   1. **Image Operating system (OS)**. Specify
      the operating system that the component is compatible with.
   2. **Component category**. From the dropdown, select the type
      of build or test component that you are creating.
   3. **Component name**. Enter a name for the
      component.
   4. **Component version**. Enter the version
      number of the component.
   5. **Description**. Provide an optional
      description to help you identify the component.
   6. **Change description**. Provide an
      optional description to help you understand the changes made to this
      version of the component.

4. In the **Definition document** section, the default option
   is **Define document content**. The component document
   defines the actions that Image Builder performs on the build and test instances
   to create your image.

In the **Content** box, enter your YAML component document content. To
start with a _Hello World_ example for Linux, choose
the **Use example** option. To learn more about how to
create a YAML component document, or to copy and paste the
_UpdateOS_ example from that page, see [Create a YAML component document for custom components in Image Builder](create-component-yaml.md "create-component-yaml.md"). 5. After you enter the component details, select **Create
component**.

###### Note

To see your new component when you create or update a recipe, apply
the **Owned by me** filter to the build or test
component list. The filter is located at the top of the component list,
next to the search box. 6. To delete a component, from the **Components** page, select
the check box next to the component that you want to delete. From the **Actions** dropdown, select **Delete
component**.

###### Update a component

To create a new component version, follow these steps:

1. Depending on where you start:
   - From the **Components** list page – Select the check box next to
     the component name, then select **Create new
     version** from the **Actions** menu.
   - From the component detail page – Choose the **Create new
     version** button in the upper right corner of the heading.

2. The component information is already populated with the current values when the
   **Create Component** page displays. Follow the create a
   component steps to update the component. This ensures that you enter a unique
   semantic version in the **Component version**. To learn more about semantic versioning for Image Builder resources, see
   [Semantic versioning in Image Builder](ibhow-semantic-versioning.md "ibhow-semantic-versioning.md").

## Create a custom component from the AWS CLI

In this section, you'll learn how to set up and use Image Builder commands in the AWS CLI to create an
AWSTOE application component, as follows.

- Upload your YAML component document to an S3 bucket that you can reference
  from the command line.
- Create the AWSTOE application component with the
  **create-component** command.
- List component versions with the **list-components** command
  and a name filter to see what versions already exist. You can use the output to
  determine what the next version should be for updates.

To create an AWSTOE application component from an input YAML document, follow the steps
that match your image operating system platform.

Linux

###### Store your application component document in Amazon S3

You can use an S3 bucket as a repository for your AWSTOE application component
source document. To store your component document, follow these steps:

- ###### Upload the document to Amazon S3

_If your document is smaller than 64 KB,
you can skip this step._ Documents that are
64 KB or larger in size must be stored in Amazon S3.

```
aws s3 cp `update-linux-os.yaml` s3://`amzn-s3-demo-destination-bucket`/`my-path`/`update-linux-os.yaml`
```

###### Create a component from the YAML document

To streamline the **create-component**
command that you use in the AWS CLI, create a JSON file that contains
all of the component parameters that you want to pass into the command.
Include the location of the `update-linux-os.yaml`
document that you created earlier. The `uri` key-value
pair contains the file reference.

###### Note

The naming convention for the data values in the JSON file follows the
pattern that is specified for the Image Builder API operation request parameters. To review the API command
request parameters, see the [CreateComponent](../APIReference/API_CreateComponent.md "../APIReference/API_CreateComponent.md") command in the
_EC2 Image Builder API Reference_.

To provide the data values as command line parameters, refer to the
parameter names specified in the _AWS CLI Command Reference_.

1. ###### Create a CLI input JSON file

Use a file editing tool to create a file named
`create-update-linux-os-component.json`. Include the following
content:

```
{
	"name": "`update-linux-os`",
	"semanticVersion": "1.1.2",
	"description": "`An example component that updates the Linux operating system`",
	"changeDescription": "`Initial version.`",
	"platform": "Linux",
	"uri": "s3://`amzn-s3-demo-destination-bucket`/`my-path`/`update-linux-os.yaml`",
	"kmsKeyId": "arn:aws:kms:us-west-`2:123456789012`:key/`98765432-b123-456b-7f89-0123456f789c`",
	"tags": {
		"`MyTagKey-purpose`": "`security-updates`"
	}
}
```

2. ###### Create the component

Use the following command to create the component, referencing the file name for
the JSON file that you created in the prior step:

```
aws imagebuilder create-component --cli-input-json file://`create-update-linux-os-component.json`
```

###### Note

    * You must include the `file://` notation
     at the beginning of the JSON file path.
    * The path for the JSON file should follow the appropriate
     convention for the base operating system where you are running
     the command. For example, Windows uses the backslash (\) to
     refer to the directory path, while Linux and macOS use the forward slash (/).

Windows

###### Store your application component document in Amazon S3

You can use an S3 bucket as a repository for your AWSTOE application component
source document. To store your component document, follow these steps:

- ###### Upload the document to Amazon S3

_If your document is smaller than 64 KB,
you can skip this step._ Documents that are
64 KB or larger in size must be stored in Amazon S3.

```
aws s3 cp `update-windows-os.yaml` s3://`amzn-s3-demo-destination-bucket`/`my-path`/`update-windows-os.yaml`
```

###### Create a component from the YAML document

To streamline the **create-component**
command that you use in the AWS CLI, create a JSON file that contains
all of the component parameters that you want to pass into the command.
Include the location of the `update-windows-os.yaml`
document that you created earlier. The `uri` key-value
pair contains the file reference.

###### Note

The naming convention for the data values in the JSON file follows the
pattern that is specified for the Image Builder API operation request parameters. To review the API command
request parameters, see the [CreateComponent](../APIReference/API_CreateComponent.md "../APIReference/API_CreateComponent.md") command in the
_EC2 Image Builder API Reference_.

To provide the data values as command line parameters, refer to the
parameter names specified in the _AWS CLI Command Reference_..

1. ###### Create a CLI input JSON file

Use a file editing tool to create a file named
`create-update-windows-os-component.json`. Include the following
content:

```
{
	"name": "`update-windows-os`",
	"semanticVersion": "1.1.2",
	"description": "`An example component that updates the Windows operating system.`",
	"changeDescription": "`Initial version.`",
	"platform": "Windows",
	"uri": "s3://`amzn-s3-demo-destination-bucket`/`my-path`/`update-windows-os.yaml`",
	"kmsKeyId": "arn:aws:kms:us-west-`2:123456789012`:key/`98765432-b123-456b-7f89-0123456f789c`",
	"tags": {
		"`MyTagKey-purpose`": "`security-updates`"
	}
}
```

###### Note

    * You must include the `file://` notation
     at the beginning of the JSON file path.
    * The path for the JSON file should follow the appropriate
     convention for the base operating system where you are running
     the command. For example, Windows uses the backslash (\) to
     refer to the directory path, while Linux and macOS use the forward slash (/).

2. ###### Create the component

Use the following command to create the component, referencing the file name for
the JSON file that you created in the prior step:

```
aws imagebuilder create-component --cli-input-json file://`create-update-windows-os-component.json`
```

###### Note

    * You must include the `file://` notation
     at the beginning of the JSON file path.
    * The path for the JSON file should follow the appropriate
     convention for the base operating system where you are running
     the command. For example, Windows uses the backslash (\) to
     refer to the directory path, while Linux and macOS use the forward slash (/).

macOS

###### Store your application component document in Amazon S3

You can use an S3 bucket as a repository for your AWSTOE application component
source document. To store your component document, follow these steps:

- ###### Upload the document to Amazon S3

_If your document is smaller than 64 KB,
you can skip this step._ Documents that are
64 KB or larger in size must be stored in Amazon S3.

```
aws s3 cp `wget-macos.yaml` s3://`amzn-s3-demo-destination-bucket`/`my-path`/`wget-macos.yaml`
```

###### Create a component from the YAML document

To streamline the **create-component**
command that you use in the AWS CLI, create a JSON file that contains
all of the component parameters that you want to pass into the command.
Include the location of the `wget-macos.yaml`
document that you created earlier. The `uri` key-value
pair contains the file reference.

###### Note

The naming convention for the data values in the JSON file follows the
pattern that is specified for the Image Builder API operation request parameters. To review the API command
request parameters, see the [CreateComponent](../APIReference/API_CreateComponent.md "../APIReference/API_CreateComponent.md") command in the
_EC2 Image Builder API Reference_.

To provide the data values as command line parameters, refer to the
parameter names specified in the _AWS CLI Command Reference_.

1. ###### Create a CLI input JSON file

Use a file editing tool to create a file named
`install-wget-macos-component.json`. Include the following
content:

```
{
	"name": "`install install-wget-macos-component`",
	"semanticVersion": "1.1.2",
	"description": "`An example component that installs and verifies the wget utility on macOS.`",
	"changeDescription": "`Initial version.`",
	"platform": "macOS",
	"uri": "s3://`amzn-s3-demo-destination-bucket`/`my-path`/`wget-macos.yaml`",
	"kmsKeyId": "arn:aws:kms:us-west-`2:123456789012`:key/`98765432-b123-456b-7f89-0123456f789c`",
	"tags": {
		"`MyTagKey-purpose`": "`install-software`"
	}
}
```

2. ###### Create the component

Use the following command to create the component, referencing the file name for
the JSON file that you created in the prior step:

```
aws imagebuilder create-component --cli-input-json file://`install-wget-macos-component.json`
```

###### Note

    * You must include the `file://` notation
     at the beginning of the JSON file path.
    * The path for the JSON file should follow the appropriate
     convention for the base operating system where you are running
     the command. For example, Windows uses the backslash (\) to
     refer to the directory path, while Linux and macOS use the forward slash (/).

### AWSTOE component versioning for updates

from the AWS CLI

AWSTOE component names and versions are embedded in the component's Amazon Resource
Name (ARN), after the component prefix. Each new version of a component has its own
unique ARN. The steps to create a new version are exactly the same as the steps to
create a new component, as long as the semantic version is unique for that component
name. To learn more about semantic versioning for Image Builder resources, see
[Semantic versioning in Image Builder](ibhow-semantic-versioning.md "ibhow-semantic-versioning.md").

To ensure that you assign the next logical version, first get a list of the existing
versions for the component that you want to change. Use the
**list-components** command with the AWS CLI, and filter on the
name.

In this example, you filter on the name of the component that you created in the
prior Linux examples. To list the component that you created, use the value of the
`name` parameter from the JSON file that you used in the
**create-component** command.

```
`aws imagebuilder list-components --filters name="name",values="`update-linux-os`"` `{
 "requestId": "123a4567-b890-123c-45d6-ef789ab0cd1e",
 "componentVersionList": [
 {
 "arn": "arn:aws:imagebuilder:us-west-2:1234560087789012:component/update-linux-os/1.0.0",
 "name": "update-linux-os",
 "version": "1.0.0",
 "platform": "Linux",
 "type": "BUILD",
 "owner": "123456789012",
 "dateCreated": "2020-09-24T16:58:24.444Z"
 },
 {
 "arn": "arn:aws:imagebuilder:us-west-2:1234560087789012:component/update-linux-os/1.0.1",
 "name": "update-linux-os",
 "version": "1.0.1",
 "platform": "Linux",
 "type": "BUILD",
 "owner": "123456789012",
 "dateCreated": "2021-07-10T03:38:46.091Z"
 }
 ]
}`
```

Based on your results, you can determine what the next version should be.

## Import a script to create a component from the AWS CLI

For some scenarios, it might be easier to start with a pre-existing script. For this
scenario, you can use the following example.

This example assumes that you have a file called `import-component.json`
(as shown). Note that the file directly references a PowerShell script called
`AdminConfig.ps1` that is already uploaded to
`amzn-s3-demo-source-bucket`. Currently,
`SHELL` is supported for the component `format`.

```
{
"name": "`MyImportedComponent`",
"semanticVersion": "1.0.0",
"description": "`An example of how to import a component`",
"changeDescription": "`First commit message.`",
"format": "SHELL",
"platform": "Windows",
"type": "BUILD",
"uri": "s3://`amzn-s3-demo-source-bucket`/`AdminConfig.ps1`",
"kmsKeyId": "arn:aws:kms:us-west-``2:123456789012``:key/`60763706-b131-418b-8f85-3420912f020c`"
}
```

To create the component from an imported script, run the following command.

```
aws imagebuilder import-component --cli-input-json file://`import-component.json`
```

## Automatic build version management

When you create a component with the same name and semantic version as an existing component, Image Builder automatically
increments the build version (for example, from `/1` to `/2`, to `/3`, and so on). This allows you to make iterative updates to your
components without manually managing version numbers, which is especially useful in CI/CD pipelines and infrastructure-as-code
deployments. If the component content is identical to the previous build version, Image Builder returns `ResourceAlreadyExistsException`
to prevent duplicate components from consuming your service quota.

## Using version references

When you create or retrieve a component, Image Builder automatically provides pre-constructed ARNs with wildcard
version patterns in the latestVersionReferences object. These references make it easy to use the latest versions of your
components in recipes and pipelines without manually parsing ARNs.

**Choosing the right version reference**

- latestVersionArn (x.x.x) - Always use the absolute latest component version.
- atestMajorVersionArn (1.x.x) - Use the latest minor and patch versions within a major version.
- latestMinorVersionArn (1.2.x) - Use the latest patch version only.
- latestPatchVersionArn (1.2.3) - Reference a specific semantic version, but get the latest build version.
