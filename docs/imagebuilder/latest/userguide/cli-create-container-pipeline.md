

# Create a container image pipeline from the AWS CLI
<a name="cli-create-container-pipeline"></a>

To create an image pipeline from the AWS CLI, run the **create-image-pipeline** command with the configuration options that apply for your pipeline. You have the option to create a JSON file that contains all of your pipeline configuration, or to specify configuration at runtime. This section uses the JSON configuration file method to simplify the command.

How often your pipeline builds a new image to incorporate any pending updates from your base image and components depends on the `schedule` that you have configured. A `schedule` has the following attributes:
+ `scheduleExpression` – Sets the schedule for when your pipeline runs to evaluate the `pipelineExecutionStartCondition` and determine if it should start a build. The schedule is configured with cron expressions. For more information on how to format a cron expression in Image Builder, see [Use cron expressions in Image Builder](cron-expressions.md).
+ `pipelineExecutionStartCondition` – Determines if your pipeline should start the build. Valid values include:
  + `EXPRESSION_MATCH_ONLY` – your pipeline will build a new image every time the cron expression matches the current time. 
  + `EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE` – your pipeline builds a new image only when the schedule expression matches and there are pending updates to your base image or components. If no updates are pending, the build is skipped. To build immediately without waiting for updates, run the pipeline manually.

When you run the **create-image-pipeline** command in the AWS CLI, many of the configuration resources are optional. However, some of the resources have conditional requirements, depending on what type of image the pipeline creates. The following resources are required for container image pipelines:
+ Container recipe ARN
+ Infrastructure configuration ARN

If you do not include a distribution configuration resource when you run the **create-image-pipeline** command, the output image is stored in the ECR repository that you specify as the target repository in your container recipe in the Region where you run the command. If you include a distribution configuration resource for your pipeline, the target repository that you have specified for the first Region in the distribution is used.

1. 

**Create a CLI input JSON file**

   Use your favorite file editing tool to create a JSON file with the following keys, plus values that are valid for your environment. This example uses a file named `create-image-pipeline.json`:

   ```
   {
   	"name": "{{MyWindows2019Pipeline}}",
   	"description": "{{Builds Windows 2019 Images}}",
   	"enhancedImageMetadataEnabled": true,
   	"containerRecipeArn": "arn:aws:imagebuilder:us-west-{{2:123456789012}}:container-recipe/{{my-example-recipe}}/2020.12.03",
   	"infrastructureConfigurationArn": "arn:aws:imagebuilder:us-west-{{2:123456789012}}:infrastructure-configuration/{{my-example-infrastructure-configuration}}",
   	"distributionConfigurationArn": "arn:aws:imagebuilder:us-west-{{2:123456789012}}:distribution-configuration/{{my-example-distribution-configuration}}",
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

1. Run the following command, using the file you created as input.

   ```
   aws imagebuilder create-image-pipeline --cli-input-json file://create-image-pipeline.json
   ```

**Example: Create a container pipeline with image scanning and custom workflows**  
This example configures a container pipeline that checks every Monday at 10:00 AM UTC and runs only when dependency updates are available. The configuration file uses existing resources for the container recipe and infrastructure. It enables [vulnerability scanning](https://docs.aws.amazon.com/imagebuilder/latest/userguide/integ-inspector.html) with Amazon Inspector and ECR integration. The configuration also specifies [custom workflows](https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-image-workflows.html) with an execution role. Parallel groups run security and functional tests at the same time. Pipeline logs are sent to custom [CloudWatch log groups](https://docs.aws.amazon.com/imagebuilder/latest/userguide/monitor-cwlogs.html).

1. 

**Create a configuration file**

   Create a JSON file named `create-container-pipeline-with-workflows.json`. This file defines the container pipeline configuration with image scanning enabled and custom test workflows. Replace the placeholder values with your own resource ARNs.

   ```
   {
   	"name": "{{MyContainerPipelineWithScanning}}",
   	"description": "{{Container pipeline with vulnerability scanning and custom workflows}}",
   	"containerRecipeArn": "arn:aws:imagebuilder:{{us-east-1}}:{{123456789012}}:container-recipe/{{my-container-recipe}}/1.0.0",
   	"infrastructureConfigurationArn": "arn:aws:imagebuilder:{{us-east-1}}:{{123456789012}}:infrastructure-configuration/{{my-infra-config}}",
   	"distributionConfigurationArn": "arn:aws:imagebuilder:{{us-east-1}}:{{123456789012}}:distribution-configuration/{{my-dist-config}}",
   	"imageScanningConfiguration": {
   		"imageScanningEnabled": true,
   		"ecrConfiguration": {
   			"repositoryName": "{{my-scanning-repo}}",
   			"containerTags": ["{{scan-latest}}"]
   		}
   	},
   	"workflows": [
   		{
   			"workflowArn": "arn:aws:imagebuilder:{{us-east-1}}:{{123456789012}}:workflow/build/{{my-build-workflow}}/1.0.0"
   		},
   		{
   			"workflowArn": "arn:aws:imagebuilder:{{us-east-1}}:{{123456789012}}:workflow/test/{{my-security-scan}}/1.0.0",
   			"onFailure": "ABORT",
   			"parallelGroup": "security"
   		},
   		{
   			"workflowArn": "arn:aws:imagebuilder:{{us-east-1}}:{{123456789012}}:workflow/test/{{my-compliance-check}}/1.0.0",
   			"onFailure": "ABORT",
   			"parallelGroup": "security"
   		},
   		{
   			"workflowArn": "arn:aws:imagebuilder:{{us-east-1}}:{{123456789012}}:workflow/test/{{my-functional-test}}/1.0.0",
   			"onFailure": "CONTINUE",
   			"parallelGroup": "functional"
   		},
   		{
   			"workflowArn": "arn:aws:imagebuilder:{{us-east-1}}:{{123456789012}}:workflow/test/{{my-performance-test}}/1.0.0",
   			"onFailure": "CONTINUE",
   			"parallelGroup": "functional"
   		}
   	],
   	"executionRole": "arn:aws:iam::{{123456789012}}:role/{{ImageBuilderExecutionRole}}",
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