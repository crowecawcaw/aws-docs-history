# Create an AMI image

pipeline from the AWS CLI

To create an image pipeline from the AWS CLI, run the
**create-image-pipeline** command with the configuration options
that apply for your pipeline. You have the option to create a JSON file that contains
all of your pipeline configuration, or to specify configuration at runtime. This
section uses the JSON configuration file method to simplify the command.

How often your pipeline builds a new image to incorporate
any pending updates from your base image and components
depends on the `schedule` that you have configured.
A `schedule` has the following attributes:

- `scheduleExpression` – Sets the
  schedule for when your pipeline runs to evaluate the
  `pipelineExecutionStartCondition` and
  determine if it should start a build. The schedule
  is configured with cron expressions. For more information
  on how to format a cron expression in Image Builder, see
  [Use cron expressions in Image Builder](cron-expressions.md "cron-expressions.md").
- `pipelineExecutionStartCondition` –
  Determines if your pipeline should start the build.
  Valid values include:

      + `EXPRESSION_MATCH_ONLY` –
       your pipeline will build a new image every time the cron
       expression matches the current time.
      + `EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE`
       – your pipeline will not start a new image build unless
       there are pending changes to your base image or components.

  When you run the **create-image-pipeline** command in the AWS CLI,
  many of the configuration resources are optional. However, some of the resources
  have conditional requirements, depending on what type of image the pipeline creates.
  The following resource identifiers are required for AMI image pipelines:

- Image recipe ARN
- Infrastructure configuration ARN

 

###### Example: Create a Windows 2019 image

This example configures a pipeline that is scheduled to run once a week
on Sunday. The configuration file shown in the first step uses existing resources
for the image recipe, infrastructure, and distribution configuration, along with
other settings to create a Windows 2019 image.

1. ###### Create a configuration file (optional)

This example uses a configuration file named
`create-image-pipeline.json` to configure the settings
in one place. Alternatively, you can use command line options when you run
the command to specify all of the details that are shown here in the
configuration file.

```
{
	"name": "`ExampleWindows2019Pipeline`",
	"description": "`Builds Windows 2019 Images`",
	"enhancedImageMetadataEnabled": true,
	"imageRecipeArn": "arn:aws:imagebuilder:us-west-`2:123456789012`:image-recipe/`my-example-recipe`/2020.12.03",
	"infrastructureConfigurationArn": "arn:aws:imagebuilder:us-west-`2:123456789012`:infrastructure-configuration/`my-example-infrastructure-configuration`",
	"distributionConfigurationArn": "arn:aws:imagebuilder:us-west-`2:123456789012`:distribution-configuration/`my-example-distribution-configuration`",
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

###### Note

    * You must include the `file://` notation
     at the beginning of the JSON file path.
    * The path for the JSON file should follow the appropriate
     convention for the base operating system where you are running
     the command. For example, Windows uses the backslash (\) to
     refer to the directory path, while Linux and macOS use the forward slash (/).

2. ###### Run the command to create an image

This example uses the configuration file created in the first step as input to
the `create-image-pipeline` command. Alternatively, you can specify the
settings and resources for your pipeline directly when you run the command. For
more information, see [create-image-pipeline](../../../cli/latest/reference/imagebuilder/create-image-pipeline.md "../../../cli/latest/reference/imagebuilder/create-image-pipeline.md")
in the _AWS CLI Reference_.

```
aws imagebuilder create-image-pipeline --cli-input-json file://create-image-pipeline.json
```
