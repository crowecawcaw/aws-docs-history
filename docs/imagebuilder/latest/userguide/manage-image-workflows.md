

# Manage build, test, and distribution workflows for Image Builder images
<a name="manage-image-workflows"></a>

An image workflow defines the sequence of steps that EC2 Image Builder runs during one stage of the image creation process. You author a workflow as a YAML document and create it as a versioned, reusable resource. Image Builder then runs your workflows when it builds, tests, and distributes your images.

Workflows give you direct control over the image creation process. You decide which steps run, in what order, what each step does when it fails, and whether Image Builder rolls back a failed step. You can start from an Amazon managed workflow, clone and customize it, or write your own from scratch.

**Image workflow benefits**
+ With image workflows, you have more flexibility, visibility, and control over the image creation process.
+ You can add customized workflow steps when you define your workflow document, or you can choose to use the Image Builder default workflow.
+ You can exclude workflow steps that Image Builder includes in default image workflows.
+ You can create test-only workflows that skip the build process entirely. You can do the same to create build-only or distribution-only workflows.

**Note**  
You can't modify an existing workflow, but you can clone it or create a new version.

**Tip**  
For information about deployable workflow examples, including approval gates and AWS Step Functions integration, see the [workflow samples](https://github.com/aws-samples/amazon-ec2-image-builder-samples/tree/HEAD/workflows) on GitHub. For more information, see [Explore Image Builder sample projects on GitHub](sample-projects.md).

**Topics**
+ [Workflow framework: Stages](#wf-stages)
+ [How a workflow runs](#wf-how-runs)
+ [Monitor workflow runs with Amazon EventBridge](#wf-monitor-eventbridge)
+ [Workflow resource constraints](#wf-constraints)
+ [Service access](#wf-service-access)
+ [Use managed workflows for your images](#use-managed-workflows)
+ [List image workflows](list-image-workflows.md)
+ [Create an image workflow](image-workflow-create-resource.md)
+ [Create a YAML workflow document](image-workflow-create-document.md)

## Workflow framework: Stages
<a name="wf-stages"></a>

Image Builder organizes the image creation process into three stages. Each stage runs a workflow of the matching *type*. Stages run in a fixed order, and a stage starts only after the previous stage finishes successfully.

The following table lists the default behavior of each stage. Because you define the steps in each workflow, you can customize what a stage does.


**Image Builder workflow stages**  

|  Order  |  Stage  |  Workflow type  |  What it does (default)  | 
| --- | --- | --- | --- | 
| 1 | **Build** | `BUILD` | Launches a build instance, runs your build components, and creates an image (AMI or container image) from the instance. | 
| 2 | **Test** | `TEST` | Launches a test instance from the new image, runs your test components, and optionally collects image scan findings. | 
| 3 | **Distribution** | `DISTRIBUTION` | Copies the image to target Regions and accounts, modifies image attributes, and applies post-distribution configurations such as launch templates and license configurations. | 

You can run a workflow for only some stages. For example, you can skip the build stage to test or distribute an image that already exists, or skip the test stage to build and distribute without testing. To skip the build or test stage, omit a workflow of that type from your pipeline or image request.

**Note**  
The distribution workflow is optional. If you omit it, Image Builder does not skip distribution – it still distributes your AMI by running the distribution configuration that you attach to the pipeline or image. Add a distribution workflow when you want to override that distribution configuration with different distribution settings, or to gain more visibility into the distribution process. To skip distribution entirely, provide a null or empty distribution configuration.

**Note**  
An image pipeline or image request can include at most one build workflow and one distribution workflow. It can also include one or more test workflows. The total number of workflows cannot exceed ten. For example, you can pair one build workflow and one distribution workflow with up to eight test workflows.

## How a workflow runs
<a name="wf-how-runs"></a>

A workflow runs its steps in the order you define them in the YAML document. Each step performs one action, such as launching an instance or running components.

**Step outcomes**  
Each step ends in one of the following states.


**Workflow step outcomes**  

|  State  |  Meaning  | 
| --- | --- | 
| `COMPLETED` | The step finished successfully. | 
| `SKIPPED` | A conditional `if` statement on the step evaluated to `false`, so Image Builder skipped the step. | 
| `FAILED` | The step did not finish successfully. | 
| `WAITING` | A `WaitForAction` step is paused, waiting for an external action. | 
| `TIMED_OUT` | The step ran longer than its `timeoutSeconds` value. | 

**Failure handling**  
The `onFailure` attribute on each step controls what happens when a step fails.
+ `Abort` (default) – Image Builder fails the step, fails the workflow, and runs no further steps. If rollback is enabled, the rollback begins at the failed step and works backward through prior steps.
+ `Continue` – Image Builder fails the step but runs the remaining steps. No rollback occurs.

**Rollback**  
When a step fails with `onFailure: Abort` and `rollbackEnabled: true` (the default), Image Builder rolls back completed steps in reverse order, starting with the step that failed. Not every action can be rolled back. An action that has no rollback records a status of `NO_ROLLBACK`.

## Monitor workflow runs with Amazon EventBridge
<a name="wf-monitor-eventbridge"></a>

Image Builder emits Amazon EventBridge events as your workflows run, so you can react to progress and to steps that need attention. For example, a `WaitForAction` step publishes an event with the detail type `EC2 Image Builder Workflow Step Waiting` to your default event bus. You can route this event to a target such as a Lambda function or an Amazon SNS topic to drive an approval process. For more information about how Image Builder works with EventBridge, see [Amazon EventBridge integration in Image Builder](integ-eventbridge.md).

To track step-level progress programmatically, use the `ListWorkflowExecutions`, `GetWorkflowExecution`, `ListWorkflowStepExecutions`, and `GetWorkflowStepExecution` API operations.

## Workflow resource constraints
<a name="wf-constraints"></a>

Your workflow documents and configurations must stay within the following default limits.


**Workflow resource constraints**  

|  Constraint  |  Default limit  |  Notes  | 
| --- | --- | --- | 
| Steps per workflow document | 15 | Steps run in document order. | 
| Outputs per workflow document | 25 | Outputs pass values to later workflows. | 
| Parameters per workflow document | 25 | Inputs the caller can set. | 
| Parameter value length | 1,024 characters | Per parameter value. | 
| Inline document size (`data`) | 16,000 bytes | Use the `uri` (Amazon S3) option for larger documents. | 
| Workflows per image or pipeline | 10 | At most 1 build and 1 distribution, plus test workflows, for a combined total of 10. | 

Workflow resources are immutable. To change a workflow, create a new version or clone it. Image Builder keeps every version, so you can trace which workflow produced each image.

## Service access
<a name="wf-service-access"></a>

To run image workflows, Image Builder needs permission to perform workflow actions. You grant this permission with an execution role that Image Builder assumes on your behalf. You assign the execution role as follows.

**Important**  
We recommend that you don't pass the [AWSServiceRoleForImageBuilder](security-iam-awsmanpol.md#sec-iam-manpol-AWSServiceRoleForImageBuilder) service-linked role as your execution role. Instead, create a custom IAM role and attach the [EC2ImageBuilderExecutionPolicy](security-iam-awsmanpol.md#sec-iam-manpol-EC2ImageBuilderExecutionPolicy) AWS managed policy. This policy grants the same permissions that Image Builder needs to call AWS services on your behalf. Using a custom role gives you full control over the permissions that Image Builder uses. It also keeps your service control policies (SCPs) and resource control policies (RCPs) in effect for operations that Image Builder performs on your behalf.
+ **Console** – In the pipeline wizard **Step 3 Define image creation process**, select your custom role from the **IAM role** list in the **Service access** panel.
+ **Image Builder API** – In the [CreateImage](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateImage.html) action request, specify your custom role as the value for the `executionRole` parameter.

To create a custom execution role, see [Creating a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html) in the *AWS Identity and Access Management User Guide*.

## Use managed workflows for your images
<a name="use-managed-workflows"></a>

AWS creates and maintains managed workflows. When you use managed workflows in your image pipelines or for one-off image creation, you can select the Amazon Resource Name (ARN) of the managed workflow that you want to use. Amazon provides the latest versions that have patches and other updates applied. To get a list of managed workflows, see [List image workflows](list-image-workflows.md), and filter on **Owner = Amazon** (console).

You can choose a managed workflow based on your build speed and validation requirements. The following are examples of managed workflow types:

Standard managed workflows (default)  
Standard managed workflows include comprehensive steps for building, testing, and validating your images with full EC2 status checks.  
The following are standard managed workflows:  
+ **build-image** – Default Amazon-managed AMI build workflow.
+ **test-image** – Default Amazon-managed AMI test workflow.
+ **build-container** – Default Amazon-managed container build workflow.
+ **test-container** – Default Amazon-managed container test workflow.

Express managed workflows  
Express managed workflows include only essential steps and reduce image creation time.  
The following are express managed workflows:  
+ **express-build-image** – Express Amazon-managed AMI build workflow that reduces build time. Waits only for the instance running state instead of full EC2 status checks, and skips image metadata collection.
+ **express-build-container** – Express Amazon-managed container build workflow that reduces build time. Waits only for the instance running state instead of full EC2 status checks.
+ **express-test-image** – Express Amazon-managed AMI test workflow that reduces test time. Waits only for the instance running state instead of full EC2 status checks, and skips security scan findings collection.