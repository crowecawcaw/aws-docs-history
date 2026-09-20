

# Find the cause of a failed image build with failure context
<a name="image-failure-context"></a>

When an image build fails, Image Builder reports the failure in the image `state`. The state carries a message that describes the failure in `reason`, and structured **failure context** in `failureContext`.

Failure context is a set of fields that name the workflow, the workflow step, the component step, and the destination Regions involved in the failure. Because the fields are structured, your automation can branch on them directly, and you can pass their values to other Image Builder API operations to get more detail.

Image Builder returns failure context from the [GetImage](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetImage.html), [ListImageBuildVersions](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListImageBuildVersions.html), and [ListImagePipelineImages](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListImagePipelineImages.html) API operations, and displays it in the Image Builder AWS Management Console.

**Topics**
+ [What failure context contains](#image-failure-context-fields)
+ [View failure context for a failed image](#image-failure-context-view)
+ [Trace a failure to its root cause](#image-failure-context-rca)
+ [Use failure context with AI agents](#image-failure-context-ai)
+ [Considerations](#image-failure-context-considerations)

## What failure context contains
<a name="image-failure-context-fields"></a>

Failure context describes a failure at three levels. Every member is optional, and Image Builder returns only the members that apply to the failure. For the members, their types, and their constraints, see [ImageState](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ImageState.html) in the *EC2 Image Builder API Reference*.

The image  
Which stage the image was in when it failed, and which workflow and workflow step were running. The workflow and step execution identifiers are the same values that [ListWorkflowStepExecutions](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListWorkflowStepExecutions.html) and [GetWorkflowStepExecution](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetWorkflowStepExecution.html) take, so you can pass them straight to those operations.

The component step  
For a build or test failure that a component caused, the component that ran, the phase and step within its document, the AWSTOE action module that the step ran, and the error the step reported. Image Builder identifies the component by build version, so it names the exact revision that ran even when your recipe references a wildcard version. For the action modules, see [Action modules supported by AWSTOE component manager](toe-action-modules.md).

The destination Regions  
For a distribution or integration failure, a summary error for the distribution as a whole, and one entry for each destination that failed. Each entry carries its , how the distribution ended there, the error from the service that Image Builder called, and, for a cross-account distribution, the target AWS account that Image Builder distributed to. When the AMI copy succeeded but a step that follows it didn't, the entry also names that step – associating license configurations, updating launch templates, putting SSM parameters, updating Amazon EC2 Fast Launch configurations, or exporting the AMI. Destinations that succeeded are omitted.

**Note**  
Which members Image Builder returns depends on how far the build progressed. A failure that happens before Image Builder starts a workflow has no workflow to name. For example, if the parent image in your recipe no longer exists, failure context identifies the stage and nothing more.

The examples in [View failure context for a failed image](#image-failure-context-view) show the members that Image Builder returns for a component failure and for a distribution failure.

## View failure context for a failed image
<a name="image-failure-context-view"></a>

**View failure context in the Image Builder console**  
Image Builder displays the failure details for an image wherever it displays a `Failed` image status.

1. Open the EC2 Image Builder console at [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/).

1. Choose **Images** from the navigation pane, and then choose the failed image build version. You can also open the **Output images** list for a pipeline.

1. Choose the `Failed` image status. Image Builder displays the failure details for the image, and links the failed workflow step to its runtime detail.

**Get failure context with the AWS CLI**  
Run the **get-image** command with the build version ARN of the failed image.

```
aws imagebuilder get-image \
    --image-build-version-arn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image/{{my-example-recipe}}/1.0.0/1 \
    --query "image.state"
```

The following example output shows a build that failed because a component step ran a script that exited with a non-zero status.

```
{
    "status": "FAILED",
    "reason": "Workflow Execution ID: 'wf-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111' failed with reason: Document arn:aws:imagebuilder:us-west-2:123456789012:component/my-example-component/1.0.0/1 failed!",
    "failureContext": {
        "imageStatus": "BUILDING",
        "workflowExecutionId": "wf-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "workflowArn": "arn:aws:imagebuilder:us-west-2:aws:workflow/build/build-image/{{x.x.x/x}}",
        "stepExecutionId": "step-a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "failedStep": "ApplyBuildComponents",
        "componentFailure": {
            "componentArn": "arn:aws:imagebuilder:us-west-2:123456789012:component/my-example-component/1.0.0/1",
            "phaseName": "build",
            "stepName": "InstallPackages",
            "action": "ExecuteBash",
            "errorMessage": "exit status 1"
        }
    }
}
```

The next example output shows an image that built and tested successfully, then failed while Image Builder updated launch templates in three destination Regions. The build succeeded in every other destination, so only the three failed Regions appear.

```
{
    "status": "FAILED",
    "reason": "Integration failed with JobId 'a1b2c3d4-5678-90ab-cdef-EXAMPLE33333', status = 'Failed' for ARN 'arn:aws:imagebuilder:us-west-2:123456789012:image/my-example-recipe/1.0.0/1'. …",
    "failureContext": {
        "imageStatus": "INTEGRATING",
        "distributionFailure": {
            "errorMessage": "In region 'eu-west-1' - 'EC2 Client Error: 'The launch-template ID 'lt-0a1b2c3d4EXAMPLE' does not exist'' …",
            "regionFailures": [
                {
                    "region": "eu-west-1",
                    "status": "FAILED",
                    "imageConfigurationStep": "UPDATE_LAUNCH_TEMPLATES",
                    "errorMessage": "EC2 Client Error: 'The launch-template ID 'lt-0a1b2c3d4EXAMPLE' does not exist'"
                },
                {
                    "region": "us-east-1",
                    "status": "FAILED",
                    "imageConfigurationStep": "UPDATE_LAUNCH_TEMPLATES",
                    "errorMessage": "EC2 Client Error: 'The launch-template ID 'lt-1a2b3c4d5EXAMPLE' does not exist'"
                },
                {
                    "region": "us-east-2",
                    "status": "FAILED",
                    "imageConfigurationStep": "UPDATE_LAUNCH_TEMPLATES",
                    "errorMessage": "EC2 Client Error: 'The launch-template ID 'lt-2a3b4c5d6EXAMPLE' does not exist'"
                }
            ]
        }
    }
}
```

To find the failed builds in an account without inspecting each one, list image build versions and filter on the image status. The following example returns the failed builds for an image, with the failure context for each.

```
aws imagebuilder list-image-build-versions \
    --image-version-arn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image/{{my-example-recipe}}/1.0.0 \
    --query "imageSummaryList[?state.status=='FAILED'].[arn, state.failureContext]"
```

## Trace a failure to its root cause
<a name="image-failure-context-rca"></a>

Failure context narrows a failure down to a single step. Use the following steps to go from that step to the evidence that explains it.

1. **Read `imageStatus` to find the stage that failed.** A value of `BUILDING` or `TESTING` means the failure happened on the Amazon EC2 instance that Image Builder launched, so the component logs are the next place to look. A value of `DISTRIBUTING` or `INTEGRATING` means the image was built and the failure is in your distribution settings or in a destination account or .

1. **Read the member that describes the specific failure.** If `componentFailure` is present, it identifies the failing step in your component document, along with the action the step ran and the error it reported. If `distributionFailure` is present, each entry in `regionFailures` gives you a destination and its own error.

1. **Inspect the workflow runtime detail.** Call [ListWorkflowStepExecutions](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_ListWorkflowStepExecutions.html) with `workflowExecutionId` to see every step in the workflow and where the failed step falls in the sequence. Call [GetWorkflowStepExecution](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_GetWorkflowStepExecution.html) with `stepExecutionId` for the inputs, outputs, and rollback status of the failed step itself.

   The following example lists the steps for a failed workflow execution.

   ```
   aws imagebuilder list-workflow-step-executions \
       --workflow-execution-id wf-{{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}
   ```

1. **Read the logs for the failed step.** Use `workflowExecutionId` and `failedStep` to go directly to the log path for that step. For more information, see [Get the full component output from the logs](#image-failure-context-logs).

1. **Reproduce the failure if you need to.** To keep the build instance running so that you can connect to it, clear the **Terminate instance on failure** setting in the infrastructure configuration that your pipeline uses. For more information, see [Troubleshoot pipeline builds](troubleshooting.md#troubleshooting-pipelines).

### Get the full component output from the logs
<a name="image-failure-context-logs"></a>

Failure context reports the error that a component step raised, but not the standard output and standard error of the script that the step ran. Image Builder keeps that output in the component logs.

When a component fails, AWSTOE writes the details of the first failed step to the console log, followed by the complete standard error output for that step.

```
  Document: MyExampleDocument
  ComponentArn: arn:aws:imagebuilder:us-west-2:123456789012:component/my-example-component/1.0.0/1
  Phase: build
  Step: InstallPackages
  Action: ExecuteBash
  ErrorMessage: exit status 1
  Stderr: {{the full standard error output of the step}}
```

`ComponentArn` is the same value that `componentFailure.componentArn` reports, so use it to match the log block to the failure context for an image. `Document` is the `name` that the component document declares, which the author chooses independently of the component resource, so the two can differ and `Document` alone doesn't identify which component failed.

AWSTOE writes `ErrorMessage` and `Stderr` only when the failed step produced them.

Image Builder streams the component logs to Amazon CloudWatch Logs when the build completes. If you specified an Amazon S3 bucket in your infrastructure configuration, Image Builder also writes them there. For the log group and stream names, see [Monitor Image Builder logs with Amazon CloudWatch Logs](monitor-cwlogs.md). For the files that AWSTOE produces and what each one contains, see [Component logging](toe-use-documents.md#component-logging).

## Use failure context with AI agents
<a name="image-failure-context-ai"></a>

Failure context is designed to be read by automation as well as by people. An AI agent that troubleshoots a failed build reads the named fields and uses their values as arguments to the next API call it makes. That makes a diagnosis repeatable, and it keeps the agent from guessing which component or to investigate.

You can use failure context in either of the following ways:
+ **Troubleshoot in the Image Builder AWS Management Console** – The Troubleshoot feature, powered by AWS DevOps Agent, uses failure context to scope its investigation to the workflow step and component that failed before it examines logs and related resources. For more information, see [Troubleshoot failed builds with AI - Preview](devops-agent-troubleshooting.md).
+ **Your own AI coding agent** – An agent that calls `GetImage` receives failure context in the response and can follow it the same way. To give your agent the broader Image Builder knowledge it needs to act on what it finds, see [Troubleshoot builds with an AI coding agent](agent-toolkit-skill.md).

If you build your own automation on failure context, treat every member as optional and check for the members you use rather than for the presence of `failureContext` itself. Which members Image Builder returns depends on the failure, and Image Builder can add members over time.

## Considerations
<a name="image-failure-context-considerations"></a>

Note the following when you use failure context:
+ Image Builder returns failure context only for images that failed. A successful image and an image that you cancelled don't have it.
+ A failed image carries both `reason` and `failureContext`. Use `reason` for a readable summary of the failure, and `failureContext` to locate it.
+ If a component uses the `ExecuteDocument` action to run a nested document, failure context identifies the component that Image Builder ran from your recipe, not the nested document.
+ Error messages in failure context are bounded in length and can be truncated. The component logs hold the complete output.
+ Failure context reports the first step that failed. If more than one step failed, review the workflow step executions and the component logs for the rest.
+ Error messages can contain text that a component or another AWS service produced. Treat them as untrusted input if you render them or pass them to another system.