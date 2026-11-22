

# Create a container image pipeline from the AWS CLI

To create an image pipeline from the AWS CLI, run the **create-image-pipeline** command with the configuration options that apply for your pipeline. You have the option to create a JSON file that contains all of your pipeline configuration, or to specify configuration at runtime. This section uses the JSON configuration file method to simplify the command.

How often your pipeline builds a new image to incorporate any pending updates from your base image and components depends on the `schedule` that you have configured. A `schedule` has the following attributes:
+ `scheduleExpression` – Sets the schedule for when your pipeline runs to evaluate the `pipelineExecutionStartCondition` and determine if it should start a build. The schedule is configured with cron expressions. For more information on how to format a cron expression in Image Builder, see [Use cron expressions in Image Builder](cron-expressions.md).
+ `pipelineExecutionStartCondition` – Determines if your pipeline should start the build. Valid values include:
  + `EXPRESSION_MATCH_ONLY` – your pipeline will build a new image every time the cron expression matches the current time. 
  + `EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE` – your pipeline builds a new image only when the schedule expression matches and there are pending updates to your base image or components. If no updates are pending, the build is skipped. To build immediately without waiting for updates, run the pipeline manually.

Many configuration resources are optional when you run the [create-image-pipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-image-pipeline.html) command in the AWS CLI or the [New-EC2IBImagePipeline](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2IBImagePipeline.html) cmdlet in AWS Tools for PowerShell. However, some of the resources have conditional requirements, depending on what type of image the pipeline creates. The following resources are required for container image pipelines:
+ Container recipe ARN
+ Infrastructure configuration ARN

If you run the **create-image-pipeline** command or the `New-EC2IBImagePipeline` cmdlet without a distribution configuration resource, Image Builder uses your container recipe's target repository. Image Builder stores the output image in that Amazon ECR repository, in the Region where you run the command. If your pipeline includes a distribution configuration resource, Image Builder uses the target repository that you specified for the first Region in the distribution.

------
#### [ AWS CLI ]

1. 

**Create a CLI input JSON file**

   Use a text editor to create a JSON file with the following keys, plus values that are valid for your environment. This example uses a file named `create-image-pipeline.json`:

   ```json
   {
   	"name": "{{my-windows-2019-pipeline}}",
   	"description": "{{Builds Windows Server 2019 container images}}",
   	"enhancedImageMetadataEnabled": true,
   	"containerRecipeArn": "arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:container-recipe/{{my-example-recipe}}/2020.12.03",
   	"infrastructureConfigurationArn": "arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:infrastructure-configuration/{{my-example-infrastructure-configuration}}",
   	"distributionConfigurationArn": "arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:distribution-configuration/{{my-example-distribution-configuration}}",
   	"imageTestsConfiguration": {
   		"imageTestsEnabled": true,
   		"timeoutMinutes": 60
   	},
   	"schedule": {
   		"scheduleExpression": "cron(0 0 * * SUN *)",
   		"pipelineExecutionStartCondition": "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE"
   	},
   	"status": "ENABLED"
   }
   ```
**Note**  
You must include the `file://` notation at the beginning of the JSON file path.
The path for the JSON file should follow the appropriate convention for the base operating system where you are running the command. For example, Windows uses the backslash (\\) to refer to the directory path, while Linux and macOS use the forward slash (/).

1. Run the following command, using the file you created as input:

   ```sh
   aws imagebuilder create-image-pipeline --cli-input-json file://create-image-pipeline.json
   ```

------
#### [ PowerShell ]

Tools for PowerShell doesn't take a JSON input file. Instead, you pass each top-level JSON key as a cmdlet parameter. Each nested setting becomes a parameter that combines the parent object name and the setting name. For example, `schedule.scheduleExpression` becomes `Schedule_ScheduleExpression`, and `imageTestsConfiguration.timeoutMinutes` becomes `ImageTestsConfiguration_TimeoutMinute`. Boolean values are `$true` or `$false`.

The following example shows how to use the [New-EC2IBImagePipeline](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2IBImagePipeline.html) cmdlet to create the pipeline with the same settings as the AWS CLI example:

```ps
New-EC2IBImagePipeline -Name {{my-windows-2019-pipeline}} `
    -Description "{{Builds Windows Server 2019 container images}}" `
    -EnhancedImageMetadataEnabled $true `
    -ContainerRecipeArn arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:container-recipe/{{my-example-recipe}}/2020.12.03 `
    -InfrastructureConfigurationArn arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:infrastructure-configuration/{{my-example-infrastructure-configuration}} `
    -DistributionConfigurationArn arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:distribution-configuration/{{my-example-distribution-configuration}} `
    -ImageTestsConfiguration_ImageTestsEnabled $true `
    -ImageTestsConfiguration_TimeoutMinute 60 `
    -Schedule_ScheduleExpression "cron(0 0 * * SUN *)" `
    -Schedule_PipelineExecutionStartCondition EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE `
    -Status ENABLED
```

------

**Example: Create a container pipeline with image scanning and custom workflows**  
This example configures a container pipeline that checks every Monday at 10:00 AM UTC and runs only when dependency updates are available. The configuration file uses existing resources for the container recipe and infrastructure. It enables [vulnerability scanning](https://docs.aws.amazon.com/imagebuilder/latest/userguide/integ-inspector.html) with Amazon Inspector and ECR integration. The configuration also specifies [custom workflows](https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-image-workflows.html) with an execution role. Parallel groups run security and functional tests at the same time. Pipeline logs are sent to custom [CloudWatch log groups](https://docs.aws.amazon.com/imagebuilder/latest/userguide/monitor-cwlogs.html).

**Container pipeline prerequisites**  
To create a container pipeline with scanning enabled, you must meet the Amazon Inspector and Amazon ECR prerequisites. For more information, see [Amazon Inspector integration in Image Builder](integ-inspector.md). This example specifies custom workflows. Include exactly one `CollectImageScanFindings` step across its test workflows. For more information, see [Create custom images with Image Builder](create-images.md).

------
#### [ AWS CLI ]

1. 

**Create a configuration file**

   Create a JSON file named `create-container-pipeline-with-workflows.json`. This file defines the container pipeline configuration with image scanning enabled and custom test workflows. Replace the placeholder values in the following example with your own resource ARNs:

   ```json
   {
   	"name": "{{my-container-pipeline-with-scanning}}",
   	"description": "{{Container pipeline with vulnerability scanning and custom workflows}}",
   	"containerRecipeArn": "arn:aws:imagebuilder:{{us-east-1}}:{{111122223333}}:container-recipe/{{my-container-recipe}}/1.0.0",
   	"infrastructureConfigurationArn": "arn:aws:imagebuilder:{{us-east-1}}:{{111122223333}}:infrastructure-configuration/{{my-infra-config}}",
   	"distributionConfigurationArn": "arn:aws:imagebuilder:{{us-east-1}}:{{111122223333}}:distribution-configuration/{{my-dist-config}}",
   	"imageScanningConfiguration": {
   		"imageScanningEnabled": true,
   		"ecrConfiguration": {
   			"repositoryName": "{{my-scanning-repo}}",
   			"containerTags": ["{{scan-latest}}"]
   		}
   	},
   	"workflows": [
   		{
   			"workflowArn": "arn:aws:imagebuilder:{{us-east-1}}:{{111122223333}}:workflow/build/{{my-build-workflow}}/1.0.0"
   		},
   		{
   			"workflowArn": "arn:aws:imagebuilder:{{us-east-1}}:{{111122223333}}:workflow/test/{{my-security-scan}}/1.0.0",
   			"onFailure": "ABORT",
   			"parallelGroup": "security"
   		},
   		{
   			"workflowArn": "arn:aws:imagebuilder:{{us-east-1}}:{{111122223333}}:workflow/test/{{my-compliance-check}}/1.0.0",
   			"onFailure": "ABORT",
   			"parallelGroup": "security"
   		},
   		{
   			"workflowArn": "arn:aws:imagebuilder:{{us-east-1}}:{{111122223333}}:workflow/test/{{my-functional-test}}/1.0.0",
   			"onFailure": "CONTINUE",
   			"parallelGroup": "functional"
   		},
   		{
   			"workflowArn": "arn:aws:imagebuilder:{{us-east-1}}:{{111122223333}}:workflow/test/{{my-performance-test}}/1.0.0",
   			"onFailure": "CONTINUE",
   			"parallelGroup": "functional"
   		}
   	],
   	"executionRole": "arn:aws:iam::{{111122223333}}:role/{{image-builder-execution-role}}",
   	"loggingConfiguration": {
   		"imageLogGroupName": "/aws/imagebuilder/{{my-container-pipeline-image-logs}}",
   		"pipelineLogGroupName": "/aws/imagebuilder/{{my-container-pipeline-execution-logs}}"
   	},
   	"imageTestsConfiguration": {
   		"imageTestsEnabled": true,
   		"timeoutMinutes": 120
   	},
   	"schedule": {
   		"scheduleExpression": "cron(0 10 ? * MON *)",
   		"pipelineExecutionStartCondition": "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE"
   	},
   	"status": "ENABLED"
   }
   ```
**Note**  
You must include the `file://` notation at the beginning of the JSON file path.
The path for the JSON file should follow the appropriate convention for the base operating system where you are running the command. For example, Windows uses the backslash (\\) to refer to the directory path, while Linux and macOS use the forward slash (/).

1. 

**Run the command**

   ```
   aws imagebuilder create-image-pipeline --cli-input-json file://create-container-pipeline-with-workflows.json
   ```

------
#### [ PowerShell ]

In Tools for PowerShell, the `workflows` array becomes a list of `WorkflowConfiguration` objects that you pass to the `Workflow` parameter. Each object sets the same `WorkflowArn`, `OnFailure`, and `ParallelGroup` values as the AWS CLI example. The other nested settings use flattened parameters. The Amazon ECR settings in `imageScanningConfiguration.ecrConfiguration` become `EcrConfiguration_RepositoryName` and `EcrConfiguration_ContainerTag`, and `loggingConfiguration.imageLogGroupName` becomes `LoggingConfiguration_ImageLogGroupName`.

The following example shows how to use the [New-EC2IBImagePipeline](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2IBImagePipeline.html) cmdlet to create the pipeline with the same settings as the AWS CLI example:

```ps
Import-Module AWS.Tools.Imagebuilder

$workflows = @(
    [Amazon.Imagebuilder.Model.WorkflowConfiguration]@{
        WorkflowArn = "arn:aws:imagebuilder:{{us-east-1}}:{{111122223333}}:workflow/build/{{my-build-workflow}}/1.0.0"
    },
    [Amazon.Imagebuilder.Model.WorkflowConfiguration]@{
        WorkflowArn   = "arn:aws:imagebuilder:{{us-east-1}}:{{111122223333}}:workflow/test/{{my-security-scan}}/1.0.0"
        OnFailure     = "ABORT"
        ParallelGroup = "security"
    },
    [Amazon.Imagebuilder.Model.WorkflowConfiguration]@{
        WorkflowArn   = "arn:aws:imagebuilder:{{us-east-1}}:{{111122223333}}:workflow/test/{{my-compliance-check}}/1.0.0"
        OnFailure     = "ABORT"
        ParallelGroup = "security"
    },
    [Amazon.Imagebuilder.Model.WorkflowConfiguration]@{
        WorkflowArn   = "arn:aws:imagebuilder:{{us-east-1}}:{{111122223333}}:workflow/test/{{my-functional-test}}/1.0.0"
        OnFailure     = "CONTINUE"
        ParallelGroup = "functional"
    },
    [Amazon.Imagebuilder.Model.WorkflowConfiguration]@{
        WorkflowArn   = "arn:aws:imagebuilder:{{us-east-1}}:{{111122223333}}:workflow/test/{{my-performance-test}}/1.0.0"
        OnFailure     = "CONTINUE"
        ParallelGroup = "functional"
    }
)

New-EC2IBImagePipeline -Name {{my-container-pipeline-with-scanning}} `
    -Description "{{Container pipeline with vulnerability scanning and custom workflows}}" `
    -ContainerRecipeArn arn:aws:imagebuilder:{{us-east-1}}:{{111122223333}}:container-recipe/{{my-container-recipe}}/1.0.0 `
    -InfrastructureConfigurationArn arn:aws:imagebuilder:{{us-east-1}}:{{111122223333}}:infrastructure-configuration/{{my-infra-config}} `
    -DistributionConfigurationArn arn:aws:imagebuilder:{{us-east-1}}:{{111122223333}}:distribution-configuration/{{my-dist-config}} `
    -ImageScanningConfiguration_ImageScanningEnabled $true `
    -EcrConfiguration_RepositoryName {{my-scanning-repo}} `
    -EcrConfiguration_ContainerTag {{scan-latest}} `
    -Workflow $workflows `
    -ExecutionRole arn:aws:iam::{{111122223333}}:role/{{image-builder-execution-role}} `
    -LoggingConfiguration_ImageLogGroupName /aws/imagebuilder/{{my-container-pipeline-image-logs}} `
    -LoggingConfiguration_PipelineLogGroupName /aws/imagebuilder/{{my-container-pipeline-execution-logs}} `
    -ImageTestsConfiguration_ImageTestsEnabled $true `
    -ImageTestsConfiguration_TimeoutMinute 120 `
    -Schedule_ScheduleExpression "cron(0 10 ? * MON *)" `
    -Schedule_PipelineExecutionStartCondition EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE `
    -Status ENABLED
```

------