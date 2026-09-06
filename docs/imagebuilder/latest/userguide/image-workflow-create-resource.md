

# Create an image workflow
<a name="image-workflow-create-resource"></a>

When you create an image workflow, you have more control over your image creation process. You can specify the workflow that runs when Image Builder builds your image, the workflows that run when it tests the image, and the workflow that runs when it distributes the image. You can also specify a customer managed key to encrypt your workflow resources. To learn more about encryption for your workflow resources, see [Encryption and key management in Image Builder](data-protection.md#ib-encryption).

For image creation, you can specify one build stage workflow, one or more test stage workflows, and one distribution stage workflow. You can even skip a stage entirely, depending on your needs. You configure the actions that your workflow takes in the YAML definition document that your workflow uses. For more information about syntax for your YAML document, see [Create a YAML workflow document](image-workflow-create-document.md).

To create a new build, test, or distribution workflow, select the tab that matches your environment.

------
#### [ AWS Management Console ]

You can use the following process to create a new workflow in the Image Builder console.

1. Open the EC2 Image Builder console at [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/).

1. Choose **Image workflows** from the navigation pane. This displays a list of image workflows that your account owns or has access to.
**Note**  
The list always includes the Amazon managed workflow resources that Image Builder uses for its default workflows. To view details for those workflows, select the **Workflow** link.

1. To create a new workflow, choose **Create image workflow**. This displays the **Create image workflow** page.

1. Configure the details for your new workflow. Select the workflow type near the top of the form: choose **Build** to create a build workflow, **Test** to create a test workflow, or **Distribution** to create a distribution workflow. The workflow type maps to the `Type` value in the API (`BUILD`, `TEST`, or `DISTRIBUTION`). Image Builder populates the **Templates** list based on this option. All other steps are the same for build, test, and distribution workflows.

**General**  
The general section includes settings that apply to your workflow resource, such as name and description. The general settings include the following:
   + **Image workflow name** (required) – The name for your image workflow. The name must be unique in your account. The name can be up to 128 characters in length. Valid characters include letters, numbers, spaces, `-`, and `_`.
   + **Version** (required) – The semantic version for the workflow resource to create (*major.minor.patch*).
   + **Description** (optional) – Optionally add a description for your workflow.
   + **KMS key** (optional) – You can encrypt your workflow resources with an customer managed key. For more information, see [Encrypt image workflows with a customer managed key](data-protection.md#ib-workflow-encrypt-cmk).

**Definition document**  
The YAML workflow document contains all of the configuration for your workflow.

**Get started**
   + To start with an Image Builder default template as a baseline for your workflow, select the **Start from templates** option. This option is selected by default. After you choose what template to use from the **Templates** list, this copies the default configuration from the template you selected into the **Content** for your new workflow document, where you can make changes.
   + To define your workflow document from scratch, select the **Start from scratch** option. This populates the **Content** with a short outline of some important parts of the document format to help you get started.

   The **Content** panel includes a status bar at the bottom that shows warnings or errors for your YAML document. For more information about how to create a YAML workflow document, see [Create a YAML workflow document](image-workflow-create-document.md).

1. When you've completed your workflow, or if you want to save progress and come back to it later, choose **Create workflow**.

------
#### [ AWS CLI ]

Before you run the **[create-workflow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-workflow.html)** command in the AWS CLI, you must create the YAML document that contains all of the configuration for your workflow. For more information, see [Create a YAML workflow document](image-workflow-create-document.md).

The following example shows how to create a build workflow with the [create-workflow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-workflow.html) AWS CLI command. The `--data` parameter refers to a YAML document that contains the build configuration for the workflow you create.

**Example: Create workflow**

```
aws imagebuilder create-workflow --name {{example-build-workflow}} --semantic-version {{1.0.0}} --type BUILD --data {{file://example-build-workflow.yml}}
```

**Output:**

```
{
	"workflowBuildVersionArn": "arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:workflow/build/example-build-workflow/{{1.0.0}}/1",
	"clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
}
```

The following example shows how to create a test workflow with the [create-workflow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-workflow.html) AWS CLI command. The `--data` parameter refers to a YAML document that contains the test configuration for the workflow you create.

**Example: Create test workflow**

```
aws imagebuilder create-workflow --name {{example-test-workflow}} --semantic-version {{1.0.0}} --type TEST --data {{file://example-test-workflow.yml}}
```

**Output:**

```
{
	"workflowBuildVersionArn": "arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:workflow/test/example-test-workflow/{{1.0.0}}/1",
	"clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
}
```

The following example shows how to create a distribution workflow with the [create-workflow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-workflow.html) AWS CLI command. The `--data` parameter refers to a YAML document that contains the distribution configuration for the workflow you create.

**Example: Create distribution workflow**

```
aws imagebuilder create-workflow --name {{example-distribution-workflow}} --semantic-version {{1.0.0}} --type DISTRIBUTION --data {{file://example-distribution-workflow.yml}}
```

**Output:**

```
{
	"workflowBuildVersionArn": "arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:workflow/distribution/example-distribution-workflow/{{1.0.0}}/1",
	"clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222"
}
```

------