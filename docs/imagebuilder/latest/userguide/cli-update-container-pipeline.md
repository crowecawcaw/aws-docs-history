

# Update container image pipelines from the AWS CLI

To update a container image pipeline, use a JSON file as input to the [update-image-pipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/update-image-pipeline.html) command in the AWS CLI. In AWS Tools for PowerShell, run the [Update-EC2IBImagePipeline](https://docs.aws.amazon.com/powershell/latest/reference/items/Update-EC2IBImagePipeline.html) cmdlet. To configure the update, you must have Amazon Resource Names (ARNs) to reference the following existing resources:
+ Image pipeline to update
+ Container recipe
+ Infrastructure configuration
+ Distribution settings (if included in the current pipeline)

**Note**  
If the distribution settings resource is included, then the ECR repository that's specified as the target repository in the distribution settings for the Region where the command runs (Region 1) takes precedence over the target repository that's specified in the container recipe.

Follow these steps to update a container image pipeline using the **update-image-pipeline** command in the AWS CLI, or the `Update-EC2IBImagePipeline` cmdlet:

**Note**  
The **update-image-pipeline** command and the `Update-EC2IBImagePipeline` cmdlet replace the entire pipeline configuration. You must specify all required properties in the update request. Include all properties—both properties you want to change and properties that should stay the same. Properties that you omit are reset to default values or are removed.  
To prevent unintended removal of existing settings, use the **get-image-pipeline** command to retrieve the current configuration. Then modify only the fields you want to change:  

```
aws imagebuilder get-image-pipeline --image-pipeline-arn arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:image-pipeline/{{my-container-pipeline}}
```
Use the output as the basis for your update request JSON file.  
With Tools for PowerShell, run the [Get-EC2IBImagePipeline](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2IBImagePipeline.html) cmdlet instead:  

```ps
Get-EC2IBImagePipeline -ImagePipelineArn arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:image-pipeline/{{my-container-pipeline}}
```
Use the returned values as the basis for the parameters that you pass to the `Update-EC2IBImagePipeline` cmdlet.

------
#### [ AWS CLI ]

1. 

**Create a CLI input JSON file**

   Use a text editor to create a JSON file with the following keys, plus values that are valid for your environment. This example uses a file named `update-image-pipeline.json`:

   ```json
   {
   	"imagePipelineArn": "arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:image-pipeline/{{my-example-pipeline}}",
   	"containerRecipeArn": "arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:container-recipe/{{my-example-recipe}}/2020.12.08",
   	"infrastructureConfigurationArn": "arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:infrastructure-configuration/{{my-example-infrastructure-configuration}}",
   	"distributionConfigurationArn": "arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:distribution-configuration/{{my-example-distribution-configuration}}",
   	"imageTestsConfiguration": {
   		"imageTestsEnabled": true,
   		"timeoutMinutes": 120
   	},
   	"schedule": {
   		"scheduleExpression": "cron(0 0 * * MON *)",
   		"pipelineExecutionStartCondition": "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE"
   	},
   	"status": "DISABLED"
   }
   ```
**Note**  
You must include the `file://` notation at the beginning of the JSON file path.
The path for the JSON file should follow the appropriate convention for the base operating system where you are running the command. For example, Windows uses the backslash (\\) to refer to the directory path, while Linux and macOS use the forward slash (/).

1. Run the following command, using the file you created as input:

   ```sh
   aws imagebuilder update-image-pipeline --cli-input-json file://{{update-image-pipeline.json}}
   ```

------
#### [ PowerShell ]

Tools for PowerShell doesn't take a JSON input file. Instead, you pass each top-level JSON key as a cmdlet parameter, and nested settings use flattened parameters, such as `Schedule_ScheduleExpression` for `schedule.scheduleExpression`. The ARN of the pipeline to update goes in the `ImagePipelineArn` parameter.

The following example shows how to use the [Update-EC2IBImagePipeline](https://docs.aws.amazon.com/powershell/latest/reference/items/Update-EC2IBImagePipeline.html) cmdlet to update the pipeline with the same settings as the AWS CLI example:

```ps
Update-EC2IBImagePipeline -ImagePipelineArn arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:image-pipeline/{{my-example-pipeline}} `
    -ContainerRecipeArn arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:container-recipe/{{my-example-recipe}}/2020.12.08 `
    -InfrastructureConfigurationArn arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:infrastructure-configuration/{{my-example-infrastructure-configuration}} `
    -DistributionConfigurationArn arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:distribution-configuration/{{my-example-distribution-configuration}} `
    -ImageTestsConfiguration_ImageTestsEnabled $true `
    -ImageTestsConfiguration_TimeoutMinute 120 `
    -Schedule_ScheduleExpression "cron(0 0 * * MON *)" `
    -Schedule_PipelineExecutionStartCondition EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE `
    -Status DISABLED
```

------