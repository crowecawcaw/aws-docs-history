# List images and build versions

On the **Images** page in the Image Builder console, you can see lists of all
of the Image Builder image resources that you own, that are shared with you, and that you have
access to. The list results include some key details about those resources.

You can also see all of the images in your account that have pending workflow actions.

###### Contents

- [List images](#list-images "#list-images")
- [List images waiting for action](#list-images-waiting-for-action "#list-images-waiting-for-action")
- [List image build versions](#list-image-build-versions "#list-image-build-versions")

## List images

This section describes the different ways that you can list information about your
images.

You can use one of the following methods to list Image Builder image resources that you have
access to. For the API action, see [ListImages](../APIReference/API_ListImages.md "../APIReference/API_ListImages.md") in the _EC2 Image Builder API Reference_. For the
associated SDK request, refer to the [See Also](../APIReference/API_ListImages.md#API_ListImages_SeeAlso "../APIReference/API_ListImages.md#API_ListImages_SeeAlso")
link on the same page.

###### Contents

- [List images in the console](#list-images-console "#list-images-console")
- [List images with AWS CLI commands](#list-images-cli "#list-images-cli")

### List images in the console

To open the **Images** list page in the console, follow these steps:

1. Open the EC2 Image Builder console at
   [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/").
2. Choose **Images** from the navigation
   pane.

The **Images** page in the console is divided into tabs, based on image
ownership or workflow actions that are pending. This section covers the first three tabs that
show images that you own or have access to.

In the **Owned by me** tab, you can use the following filters to
streamline the image list results.

- You can search for all or part of the name in the search bar.
- You can filter images based on their operating system platform (Windows,
  Linux, or macOS).
- You can filter images based on the type of output they produce (AMI or
  container image).
- You can use **Filter source** to find images that were
  imported from a virtual machine (VMIE), or from an ISO disk image.
  Following the filter controls, the **Owned by me** tab shows a list
  of Image Builder images that you created, with the following details for the listed resources:

**Name / Version**

Image Builder image resource names start with the recipe name and version that they're
built from. Select the link to see all of the related image build versions.

**Type**

The type of output image that Image Builder creates for this image resource (an AMI
or a container image).

**Platform**

The operating system platform of the image resource, for example,
"Linux", "Windows", or "macOS".

**Image source**

The origin of the base image that Image Builder used to build this image
resource. This is primarily used to filter results for images that
were imported from a virtual machine (**VMIE**).

**Creation time**

The date and time when Image Builder created the current version of the image resource.

**ARN**

The Amazon Resource Name (ARN) of the current version of the image resource.

In the **Shared with me** tab, you can use the following filters to
streamline the image list results.

- You can search for all or part of the name in the search bar.
- You can filter images based on their operating system platform (Windows,
  Linux, or macOS).
- You can filter images based on the type of output they produce (AMI or
  container image).
- You can use **Filter source** to find images that were
  imported from a virtual machine (VMIE), or from an ISO disk image.
  Following the filter controls, the **Shared with me** tab shows a list
  of Image Builder images that were shared with you, with the following details for the listed resources:

**Image name**

The name of the image resource that was shared with you. To use a shared
image in a recipe, you select the **Select managed images**
option, and change the **Image origin** to
**Images shared with me**.

**Type**

The type of output image that Image Builder creates for this image resource (an AMI
or a container image).

**Version**

The version of the operating system platform for the image resource, usually
a numeric field in the following format: <major>.<minor>.<patch>.

**Image source**

The origin of the base image that Image Builder used to build this image resource,
if applicable. This is primarily used to filter results for images that
were imported from a virtual machine (**VMIE**).

**Platform**

The operating system platform of the image resource, for example,
"Linux", "Windows", or "macOS".

**Creation time**

The date and time when Image Builder created the version of the image resource
that was shared with you.

**Owner**

The owner of the shared image resource.

**ARN**

The Amazon Resource Name (ARN) of the image resource version that was
shared with you.

In the **Managed by Amazon** tab, you can use the following filters to
streamline the image list results.

- You can search for all or part of the name in the search bar.
- You can filter images based on their operating system platform (Windows,
  Linux, or macOS).
- You can filter images based on the type of output they produce (AMI or
  container image).
- You can use **Filter source** to find images that were
  imported from a virtual machine (VMIE), or from an ISO disk image.
  Following the filter controls, the **Managed by Amazon** tab shows a list
  of Amazon managed Image Builder images that you can use as base images for your recipes. Image Builder
  displays the following details for listed resources:

**Image name**

The name of the managed image. When you create a recipe, the default for
your base image is **Quick start (Amazon managed)**. The
images that are listed in this tab populate the **Image name**
list associated with the operating system platform you choose for your base
image when you create a recipe.

**Type**

The type of output image that Image Builder creates for this image resource (an AMI
or a container image).

**Version**

The version of the operating system platform for the image resource, usually a
numeric field in the following format: <major>.<minor>.<patch>.

**Platform**

The operating system platform of the image resource, for example,
"Linux", "Windows", or "macOS".

**Creation time**

The date and time when Image Builder created the version of the image resource
that was shared with you.

**Owner**

Amazon owns the managed images.

**ARN**

The Amazon Resource Name (ARN) of the image resource version that was
shared with you.

### List images with AWS CLI commands

When you run the
**[list-images](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-images.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-images.html")**
command in the AWS CLI, you can get a list of images that you own or have access to.

The following command example shows how to use the **list-images**
command without filters to list all of the Image Builder image resources that you
own.

**Example: list all images**

```
`aws imagebuilder list-images`
```

**Output:**

```
`{
 "requestId": "1abcd234-e567-8fa9-0123-4567b890cd12",
 "imageVersionList": [
 {
 "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image/image-recipe-name/1.0.0",
 "name": "image-recipe-name",
 "type": "AMI",
 "version": "1.0.0",
 "platform": "Linux",
 "owner": "123456789012",
 "dateCreated": "2022-04-28T01:38:23.286Z"
 },
 {
 "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image/image-recipe-win/1.0.1",
 "name": "image-recipe-win",
 "type": "AMI",
 "version": "1.0.1",
 "platform": "Windows",
 "owner": "123456789012",
 "dateCreated": "2022-04-28T01:38:23.286Z"
 },
 {
 "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image/image-recipe-macos/1.1.1",
 "name": "image-recipe-macos",
 "type": "AMI",
 "version": "1.1.1",
 "platform": "macOS",
 "owner": "123456789012",
 "dateCreated": "2022-04-28T01:38:23.286Z"
 }
 ]
}`
```

When you run the **list-images** command, you can apply filters to
streamline the results, as the following example shows. For more information
about how to filter your results, see the [list-images](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-images.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-images.html") command in the
_AWS CLI Command Reference_.

**Example: filter for Linux images**

```
`aws imagebuilder list-images --filters name="`platform`",values="`Linux`"`
```

**Output:**

```
`{
 "requestId": "1abcd234-e567-8fa9-0123-4567b890cd12",
 "imageVersionList": [
 {
 "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image/image-recipe-name/1.0.0",
 "name": "image-recipe-name",
 "type": "AMI",
 "version": "1.0.0",
 "platform": "Linux",
 "owner": "123456789012",
 "dateCreated": "2022-04-28T01:38:23.286Z"
 }
 ]
}`
```

## List images waiting for action

When you use the `WaitForAction` step action in your image workflow,
it pauses the workflow until you send it a signal to resume processing or fail the
workflow. You can use this step action if you have an external process that needs
to run before you continue. You can then use the `SendWorkflowStepAction`
to send a signal to the paused step to `RESUME` or `STOP`. You
can also stop or resume your workflow from the console.

The following tabs show how to get a list of all of the image resources in your
account with workflow steps that are currently paused to wait for a signal to resume
or stop. The tabs cover console steps and the AWS CLI command.

You can also use the API or an SDK to get a list of workflow steps that
are waiting for action. For the API action, see [ListWaitingWorkflowSteps](../APIReference/API_ListWaitingWorkflowSteps.md "../APIReference/API_ListWaitingWorkflowSteps.md")
in the _EC2 Image Builder API Reference_. For the associated SDK request, refer to
the [See Also](../APIReference/API_ListWaitingWorkflowSteps.md#API_ListWaitingWorkflowSteps_SeeAlso "../APIReference/API_ListWaitingWorkflowSteps.md#API_ListWaitingWorkflowSteps_SeeAlso") link on the same page.

Console
To get to the **Waiting for action** tab in the console,
follow these steps:

1. Open the EC2 Image Builder console at
   [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/").
2. Choose **Images** from the navigation
   pane. This opens the **Images** list page.
3. Select the **Waiting for action** tab from
   the list page.
4. (optional) To stop or resume a step, select the check box next to
   the name, and then choose **Stop step** or
   **Resume step**. You can select more than one check
   box to perform the same action for all selected steps.

###### Pending workflow step details

Workflow details for the pending step include the following:

- **Image name** – The name of the image
  resource that has the pending step. You can select the name link to
  display the detail page for that image.
- **Pending step name** – The name of the
  workflow step that's waiting for action.
- **Step execution Id** – Uniquely identifies
  the runtime instance of the workflow step. You can select the linked ID
  to display runtime details for the step.
- **Step start** – The timestamp when
  the runtime instance of the workflow step started.
- **Workflow ARN** – The Amazon Resource
  Name (ARN) of the workflow with the pending step.
- **Actions** – The step action that's
  in a wait state.

AWS CLI
When you run the **[list-waiting-workflow-steps](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-waiting-workflow-steps.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-waiting-workflow-steps.html")**
command in the AWS CLI, you'll get a list of all of the images in your account that
have workflow steps that are waiting for action before completing the image creation
process.

The following command example shows how to use the
**list-waiting-workflow-steps** command to list all of
the images in your account with workflow steps that are waiting for action.

**Example: list images in your account with waiting workflow
steps**

```
`aws imagebuilder list-waiting-workflow-steps`
```

**Output:**

The output for this example shows one image in the account with a step that's
waiting for action.

```
`{
 "steps": [
 {
 "imageBuildVersionArn": "arn:aws:imagebuilder:`us-west-2`:`111122223333`:image/`example-image`/`1.0.0`/8",
 "name": "`WaitForAction`",
 "workflowExecutionId": "wf-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
 "stepExecutionId": "step-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
 "workflowBuildVersionArn": "arn:aws:imagebuilder:`us-west-2`:`111122223333`:workflow/test/`wait-for-action`/`1.0.0`/1",
 "startTime": "2023-11-21T23:21:23.609Z",
 "action": "WaitForAction"
 }
 ]
}`
```

## List image build versions

On the **Image build versions** page of the Image Builder console, you can see
a list of build versions and additional details for an image resource that you own. You
can also use commands or actions with the Image Builder API, SDKs, or AWS CLI to list image build
versions.

You can use one of the following methods to list image build versions for image
resources that you own. For the API action, see [ListImageBuildVersions](../APIReference/API_ListImageBuildVersions.md "../APIReference/API_ListImageBuildVersions.md")
in the _EC2 Image Builder API Reference_. For the associated SDK request, refer to
the [See Also](../APIReference/API_ListImageBuildVersions.md#API_ListImageBuildVersions_SeeAlso "../APIReference/API_ListImageBuildVersions.md#API_ListImageBuildVersions_SeeAlso") link on the same page.

Console

###### Version details

Details on the **Image build versions** page in the Image Builder console
include the following:

- **Version** – The image resource build
  version. In the Image Builder console, the version links to an image detail
  page.
- **Type** – The type of output that Image Builder
  distributed when it created this image resource (an AMI or a
  container image).
- **Date created** –
  The date and time when Image Builder created the image build version.
- **Image status** –
  The current status of the image build version.
  Status can relate to the image build or disposition. For example,
  during the build process, you might see a status of `Building` or
  `Distributing`. For disposition of the image, you might see a status
  of `Deprecated` or `Deleted`.
- **Reason for failure** –
  The reason for the image status.
  The Image Builder console only displays the reason when the build fails
  (**Image status** equals `Failed`).
- **Security findings** – The aggregated
  image scan findings for the referenced image build version.
- **ARN** – The Amazon Resource Name (ARN)
  for the referenced version of the image resource.
- **Log stream** – A link to the log stream
  detail for the referenced image build version.

###### List versions

To list image build versions in the Image Builder console, perform the following
steps:

1. Open the EC2 Image Builder console at
   [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/").
2. Choose **Images** from the navigation
   pane. By default, the image list shows the current version
   of each of the images that you own.
3. To see a list of all the versions for an image, choose the current
   version link. The link opens the **Image build versions**
   page that lists all of the build versions for a specific image.

AWS CLI
When you run the **[list-image-build-versions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-image-build-versions.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-image-build-versions.html")**
command in the AWS CLI, you'll get a full list of build versions for
the specified image resource. You must own the image to run this command.

The following command example shows how to use the
**list-image-build-versions** command to list all of
the build versions for the specified image.

**Example: list build versions for a specific image**

```
`aws imagebuilder list-image-build-versions --image-version-arn arn:aws:imagebuilder:`us-west-2`:`123456789012`:image/`image-recipe-name`/`1.0.0``
```

**Output:**

The output for this example includes two build versions for the
specified image recipe.

```
`{
 "requestId": "12f3e45d-67cb-8901-af23-45ed678c9b01",
 "imageSummaryList": [
 {
 "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image/image-recipe-name/1.0.0/2",
 "name": "image-recipe-name",
 "type": "AMI",
 "version": "1.0.0/2",
 "platform": "Linux",
 "osVersion": "Amazon Linux 2",
 "state": {
 "status": "AVAILABLE"
 },
 "owner": "123456789012",
 "dateCreated": "2023-03-10T01:04:40.609Z",
 "outputResources": {
 "amis": [
 {
 "region": "us-west-2",
 "image": "ami-012b3456789012c3d",
 "name": "image-recipe-name 2023-03-10T01-05-12.541Z",
 "description": "First verison of image-recipe-name",
 "accountId": "123456789012"
 }
 ]
 },
 "tags": {}
 },
 {
 "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image/image-recipe-name/1.0.0/1",
 "name": "image-recipe-name",
 "type": "AMI",
 "version": "1.0.0/1",
 "platform": "Linux",
 "osVersion": "Amazon Linux 2",
 "state": {
 "status": "AVAILABLE"
 },
 "owner": "123456789012",
 "dateCreated": "2023-03-10T00:07:16.384Z",
 "outputResources": {
 "amis": [
 {
 "region": "us-west-2",
 "image": "ami-0d1e23456789f0a12",
 "name": "image-recipe-name 2023-03-10T00-07-18.146132Z",
 "description": "First verison of image-recipe-name",
 "accountId": "123456789012"
 }
 ]
 },
 "tags": {}
 }
 ]
}`
```

###### Note

Output from the **list-image-build-versions** command doesn't
include security findings or log streams at this time.
