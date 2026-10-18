

# Create custom images with Image Builder
<a name="create-images"></a>

There are several different ways that you can create a new Image Builder image. For example, you can use one of the following methods to create an image with the AWS Management Console or AWS CLI. You can also use the [CreateImage](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateImage.html) API action or run a build pipeline to create the image. For the SDK request associated with the API action, you can refer to the [See Also](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CreateImage.html#API_CreateImage_SeeAlso) link for that command in the *EC2 Image Builder API Reference*.

------
#### [ Console ]

To create a new image from an existing pipeline, you can manually run the pipeline, as follows. You can also use the pipeline wizard to create a new image from scratch. See [Pipeline wizard: Create AMI](start-build-image-pipeline.md) or [Pipeline wizard: Create container image](start-build-container-pipeline.md), depending on the type of image you want to create.

1. Open the EC2 Image Builder console at [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/).

1. Choose **Image pipelines** from the navigation pane.

1. Select the check box next to the **Pipeline name** that you want to run.

1. To create the image, select **Run pipeline** from the **Actions** menu. This starts the pipeline.

You can also specify a schedule to run your pipeline, or use Amazon EventBridge to run your pipeline based on rules that you configure.

------
#### [ AWS CLI ]

Before you run the [create-image](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-image.html) command in the AWS CLI, you must create the following resources if they don't already exist:

**Required resources**
+ **Recipe** – You must specify exactly one recipe for your image, as follows:  
Image recipe  
Specify the Amazon Resource Name (ARN) for your image recipe resource with the `--image-recipe-arn` parameter.  
Container recipe  
Specify the ARN for your container recipe resource with the `--container-recipe-arn` parameter.
+ **Infrastructure configuration** – Specify the ARN for your infrastructure configuration resource with the `--infrastructure-configuration-arn` parameter.

You can also specify any of the following resources that your image requires:

**Optional resources and configuration**
+ **Distribution configuration** – By default, Image Builder distributes the output image resource to your account in the Region where you run the **create-image** command. To provide additional destinations or configuration for your distribution, specify the ARN for your distribution configuration resource with the `--distribution-configuration-arn` parameter.
+ **Image scanning** – To scan your image with Amazon Inspector during the test stage of the build, use the `--image-scanning-configuration` parameter. By default, image scanning is off. When scanning is on, Image Builder waits for Amazon Inspector to scan the test instance, or pushes a copy of your container image to Amazon ECR for Amazon Inspector to scan. Image Builder then saves a snapshot of the findings with your image, so the findings remain available after the scanned resource no longer exists. If you specify a scanning configuration, the **get-image** response includes it, but image list responses don't. For an image that a pipeline builds, **get-image** returns the scanning configuration that the pipeline had when the build started. The **get-image-pipeline** and **list-image-pipelines** responses include the current scanning configuration of the pipeline. The `--image-scanning-configuration` parameter accepts the following fields:
  + **imageScanningEnabled** (boolean) – Set to `true` to scan your image with Amazon Inspector during the test stage of the build. Set to `false`, or omit the field, to turn off scanning.
  + **ecrConfiguration** (object) – Applies only to requests that specify a `containerRecipeArn`. Sets the Amazon ECR repository and tags for the copy of the container image that Image Builder pushes for Amazon Inspector to scan. If you turn on scanning and specify `repositoryName` or `containerTags` in `ecrConfiguration` for a request that specifies an `imageRecipeArn`, the request fails with an `InvalidParameterCombinationException`.
    + **repositoryName** (string) – The name of an existing Amazon ECR repository for the scanned image, 1–1024 characters. For repository requirements, see [Amazon Inspector integration in Image Builder](integ-inspector.md). If you omit it, Image Builder uses `image-builder-image-scanning-repository`, creates it if it doesn't exist, and removes the image after it collects the findings. The image stays in the repository if Image Builder doesn't finish collecting the findings, or if you name your own repository.
    + **containerTags** (list of strings) – Additional tags that Image Builder applies to the container image that it pushes for scanning. Image Builder also applies its own version tags to that image. Each tag must be from 1–1024 characters in length.
**Test stage requirements**  
If you turn on scanning and set `imageTestsEnabled` to `false` in the `--image-tests-configuration` parameter, the request fails with an `InvalidParameterCombinationException`. This requirement applies to the **create-image**, **create-image-pipeline**, and **update-image-pipeline** commands.  
If you use the `--workflows` parameter, include exactly one `CollectImageScanFindings` step across the test workflows for an image. Image Builder doesn't check for this step, and without it Image Builder saves no findings. The AWS managed `express-test-image` workflow doesn't include this step.
+ **Image tests** – To suppress the Image Builder test stage, use the `--image-tests-configuration` parameter. You can't set `imageTestsEnabled` to `false` when you enable image scanning.
+ **Image tags** – Use the `--tags` parameter to add tags to your output image resource.
+ **Image workflows** – If you don't specify any build or test workflows, Image Builder creates your image with its default image workflow. To specify workflows that you've created, use the `--workflows` parameter.
**Note**  
If you specify image workflows, you must also provide the name or ARN of the IAM role that Image Builder uses to run your workflow actions in the `--execution-role` parameter.

The following example shows how to create an image with the [create-image](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-image.html) AWS CLI command. For more information, see the *AWS CLI Command Reference*.

**Example: Create a basic image with default distribution**

```
aws imagebuilder create-image --image-recipe-arn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image-recipe/{{simple-recipe-linux}}/{{1.0.0}} --infrastructure-configuration-arn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:infrastructure-configuration/{{simple-infra-config-linux}}
```

**Output:**

```
{
"requestId": "1abcd234-e567-8fa9-0123-4567b890cd12",
"imageVersionList": [
    {
        "arn": "arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image/{{simple-recipe-linux}}/{{1.0.0}}",
        "name": "{{simple-recipe-linux}}",
        ...
    }
]
}
```

------
#### [ PowerShell ]

The following example shows how to use the [New-EC2IBImage](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2IBImage.html) cmdlet to create an image. This example uses default distribution settings:

```
New-EC2IBImage `
    -ImageRecipeArn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image-recipe/{{simple-recipe-linux}}/{{1.0.0}} `
    -InfrastructureConfigurationArn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:infrastructure-configuration/{{simple-infra-config-linux}}
```

------

## Cancel image creation
<a name="cli-cancel-image-creation"></a>

------
#### [ AWS CLI ]

To cancel an in-progress image build, use the **cancel-image-creation** command, as follows:

```
aws imagebuilder cancel-image-creation --image-build-version-arn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image/{{my-example-recipe}}/2019.12.03/1
```

------
#### [ PowerShell ]

The following example shows how to use the [Stop-EC2IBImageCreation](https://docs.aws.amazon.com/powershell/latest/reference/items/Stop-EC2IBImageCreation.html) cmdlet to cancel an in-progress image build:

```
Stop-EC2IBImageCreation -ImageBuildVersionArn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image/{{my-example-recipe}}/2019.12.03/1
```

------