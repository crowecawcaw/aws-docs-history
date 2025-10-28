# Using EC2 Image Builder to build customized Amazon ECS-optimized AMIs

AWS recommends that you use the Amazon ECS-optimized AMIs because they are preconfigured with
the requirements and recommendations to run your container workloads. There might be times
when you need to customize your AMI to add additional software. You can use EC2 Image Builder for the
creation, management, and deployment of your server images. You retain ownership of the
customized images created in your account. You can use EC2 Image Builder pipelines to automate
updates and system patching for your images, or use a stand-alone command to create an image
with your defined configuration resources.

You create a recipe for your image. The recipe includes a parent image, and any additional
components. You also create a pipeline which distributes your customized AMI.

You create a recipe for your image. An Image Builder image recipe is a document that
defines the base image and the components that are applied to the base image to produce the
desired configuration for the output AMI image. You also create a pipeline which distributes
your customized AMI. For more information, see [How EC2 Image Builder
works](../../../imagebuilder/latest/userguide/how-image-builder-works.md "../../../imagebuilder/latest/userguide/how-image-builder-works.md") in the _EC2 Image Builder User Guide_.

We recommend that you use one of the following Amazon ECS-optimized AMIs as your "Parent image"
in EC2 Image Builder:

- Linux
  - Amazon ECS-optimized AL2023 x86
  - Amazon ECS-optimized Amazon Linux 2023 (arm64) AMI
  - Amazon ECS-optimized Amazon Linux 2 kernel 5 AMI
  - Amazon ECS-optimized Amazon Linux 2 x86 AMI

- Windows

      + Amazon ECS-optimized Windows 2022 Full x86
      + Amazon ECS-optimized Windows 2022 Core x86
      + Amazon ECS-optimized Windows 2019 Full x86
      + Amazon ECS-optimized Windows 2019 Core x86
      + Amazon ECS-optimized Windows 2016 Full x86

  We also recommend that you select "Use latest available OS version". The pipeline will use
  semantic versioning for the parent image, which helps detect the dependency updates in
  automatically scheduled jobs. For more information, see [Semantic
  versioning](../../../imagebuilder/latest/userguide/ibhow-semantic-versioning.md "../../../imagebuilder/latest/userguide/ibhow-semantic-versioning.md") in the _EC2 Image Builder User Guide_.

AWS regularly updates Amazon ECS-optimized AMI images with security patches and the new
container agent version. When you use an AMI ID as your parent image in your image recipe,
you need to regularly check for updates to the parent image. If there are updates, you must
create a new version of your recipe with the updated AMI. This ensures that your custom
images incorporate the latest version of the parent image. For information about how to
create a workflow to automatically update your EC2 instances in your Amazon ECS cluster with the newly
created AMIs, see [How to create an AMI hardening pipeline and automate updates to your ECS instance
fleet](https://aws.amazon.com/blogs/security/how-to-create-an-ami-hardening-pipeline-and-automate-updates-to-your-ecs-instance-fleet/ "https://aws.amazon.com/blogs/security/how-to-create-an-ami-hardening-pipeline-and-automate-updates-to-your-ecs-instance-fleet/").

You can also specify the Amazon Resource Name (ARN) of a parent image that's published through a managed
EC2 Image Builder pipeline. Amazon routinely publishes Amazon ECS-optimized AMI images through managed
pipelines. These images are publicly accessible. You must have the correct permissions to
access the image. When you use an image ARN instead of an AMI in your Image Builder recipe, your
pipeline automatically uses the most recent version of the parent image each time it runs.
This approach eliminates the need to manually create new recipe versions for each update.

## Clean up the Amazon ECS-optimized AMI

When using an Amazon ECS-optimized AMI as a parent image, you must clean up the image to prevent
transient issues. The Amazon ECS-optimized AMI is preconfigured for the Amazon ECS agent to
auto-start and register as a container instance with Amazon ECS. Using it as a base image
without proper cleanup can cause problems in your custom AMI.

To clean up the image for future use, create a component that runs the following commands to
stop the ecs-init package and Docker processes:

```
sudo systemctl stop ecs
sudo systemctl stop docker
```

Remove all the log files from the current instance to prevent preserving them when saving
the image. Use the example script in [Security best
practices for EC2 Image Builder](../../../imagebuilder/latest/userguide/security-best-practices.md "../../../imagebuilder/latest/userguide/security-best-practices.md") to clean up the various files from the instance.

To clean up the Amazon ECS specific data, run the following commands:

```
sudo rm -rf /var/log/ecs/*
sudo rm /var/lib/ecs/data/agent.db
```

For more information about creating custom Amazon ECS-optimized AMIs, see [How do I create
a custom AMI from an Amazon ECS-optimized AMI?](https://forums.aws.amazon.com/knowledge-center/ecs-create-custom-amis/ "https://forums.aws.amazon.com/knowledge-center/ecs-create-custom-amis/") in the AWS Knowledge
Center.

## Using the image ARN with infrastructure as code

(IaC)

You can configure the recipe using the EC2 Image Builder console, or infrastructure as code (for
example, AWS CloudFormation), or the AWS SDK. When you specify a parent image in your recipe, you
can specify an EC2 AMI ID, Image Builder image ARN, AWS Marketplace product ID, or container image. AWS
publishes both AMI IDs and Image Builder image ARNs of Amazon ECS-Optimized AMIs publicly. The
following is the ARN format for the image:

```
arn:${Partition}:imagebuilder:${Region}:${Account}:image/${ImageName}/${ImageVersion}
```

The `ImageVersion` has the following format. Replace
`major`, `minor` and
`patch` with the latest values.

```
<`major`>.<`minor`>.<`patch`>
```

You can replace `major`, `minor` and `patch` to specific
values or you can use Versionless ARN of an image, so your pipeline remains up-to-date
with the latest version of the parent image. A versionless ARN uses wildcard format
‘x.x.x’ to represent the image version. This approach allows the Image Builder service to
automatically resolve to the most recent version of the image. Using versionless ARN
ensures that your reference always point to the latest image available, streamlining the
process of maintaining up to date images in your deployment. When you create a recipe
with the console, EC2 Image Builder automatically identifies the ARN for your parent image.
When you use IaC to create the recipe, you must identify the ARN and select the
desired image version or use versionless arn to indicate latest available image. We
recommend that you create an automated script to filter and only display images that
align with your criteria. The following Python script shows how to retrieve a list of
Amazon ECS-optimized AMIs.

The script accepts two optional arguments: `owner` and
`platform`, with default values of “Amazon”, and “Windows” respectively.
The valid values for the owner argument are: `Self`, `Shared`,
`Amazon`, and `ThirdParty`. The valid values for the platform
argument are `Windows` and `Linux`. For example, if you run the
script with the `owner` argument set to `Amazon` and the
`platform` set to `Linux`, the script generates a list of
images published by Amazon including Amazon ECS-Optimized images.

```
import boto3
import argparse

def list_images(owner, platform):
    # Create a Boto3 session
    session = boto3.Session()

    # Create an EC2 Image Builder client
    client = session.client('imagebuilder')

    # Define the initial request parameters
    request_params = {
        'owner': owner,
        'filters': [
            {
                'name': 'platform',
                'values': [platform]
            }
        ]
    }

    # Initialize the results list
    all_images = []

    # Get the initial response with the first page of results
    response = client.list_images(**request_params)

    # Extract images from the response
    all_images.extend(response['imageVersionList'])

    # While 'nextToken' is present, continue paginating
    while 'nextToken' in response and response['nextToken']:
        # Update the token for the next request
        request_params['nextToken'] = response['nextToken']

        # Get the next page of results
        response = client.list_images(**request_params)

        # Extract images from the response
        all_images.extend(response['imageVersionList'])

    return all_images

def main():
    # Initialize the parser
    parser = argparse.ArgumentParser(description="List AWS images based on owner and platform")

    # Add the parameters/arguments
    parser.add_argument("--owner", default="Amazon", help="The owner of the images. Default is 'Amazon'.")
    parser.add_argument("--platform", default="Windows", help="The platform type of the images. Default is 'Windows'.")

    # Parse the arguments
    args = parser.parse_args()

    # Retrieve all images based on the provided owner and platform
    images = list_images(args.owner, args.platform)

    # Print the details of the images
    for image in images:
        print(f"Name: {image['name']}, Version: {image['version']}, ARN: {image['arn']}")

if __name__ == "__main__":
    main()
```

## Using the image ARN with AWS CloudFormation

An Image Builder image recipe is a blueprint that specifies the parent image and components
required to achieve the intended configuration of the output image. You use the
`AWS::ImageBuilder::ImageRecipe` resource. Set the
`ParentImage` value to the image ARN. Use the versionless ARN of your
desired image to ensure your pipeline always uses the most recent version of the image.
For example,
`arn:aws:imagebuilder:us-east-1:aws:image/amazon-linux-2023-ecs-optimized-x86/x.x.x`.
The following `AWS::ImageBuilder::ImageRecipe` resource definition uses an
Amazon managed image ARN:

```
ECSRecipe:
    Type: AWS::ImageBuilder::ImageRecipe
    Properties:
      Name: MyRecipe
      Version: '1.0.0'
      Components:
        - ComponentArn: [<The component arns of the image recipe>]
      ParentImage: "arn:aws:imagebuilder:us-east-1:aws:image/amazon-linux-2023-ecs-optimized-x86/x.x.x"

```

For more information about the [`AWS::ImageBuilder::ImageRecipe`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagerecipe.md") resource see in the
_AWS CloudFormation User Guide_.

You can automate the creation of new images in your pipeline by setting the
`Schedule` property of the `AWS::ImageBuilder::ImagePipeline`
resource. The schedule includes a start condition and cron expression. For more
information, see [`AWS::ImageBuilder::ImagePipeline`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-imagebuilder-imagepipeline.md") in the _AWS CloudFormation User Guide_.

The following of `AWS::ImageBuilder::ImagePipeline` example has the pipeline run a
build at 10:00AM Coordinated Universal Time (UTC) every day. Set the following
`Schedule` values:

- Set `PipelineExecutionStartCondition` to
  `EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE`. The build
  initiates only if dependent resources like the parent image or components, which
  use the wildcard ‘x’ in their semantic versions, are updated. This ensures the
  build incorporates the latest updates of those resources.
- Set ScheduleExpression to the cron expression `(0 10 * * ?
*)`.

```
ECSPipeline:
    Type: AWS::ImageBuilder::ImagePipeline
    Properties:
      Name: my-pipeline
      ImageRecipeArn: <arn of the recipe you created in previous step>
      InfrastructureConfigurationArn: <ARN of the infrastructure configuration associated with this image pipeline>
      Schedule:
        PipelineExecutionStartCondition: EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE
        ScheduleExpression: 'cron(0 10 * * ? *)'
```

## Using the image ARN with Terraform

The approach for specifying your pipeline's parent image and schedule in Terraform aligns
with that in AWS CloudFormation. You use the `aws_imagebuilder_image_recipe` resource.
Set the `parent_image` value to the image ARN. Use the versionless ARN of
your desired image to ensure your pipeline always uses the most recent version of the
image. For more information, see [`aws_imagebuilder_image_recipe`](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/imagebuilder_image_recipe#argument-reference "https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/imagebuilder_image_recipe#argument-reference")in the Terraform documentation.

In the schedule configuration block of the `aws_imagebuilder_image_pipeline
 resource`, set the `schedule_expression` argument value to a cron
expression of your choice to specify how often the pipeline runs, and set the
`pipeline_execution_start_condition` to
`EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE`. For more
information, see [`aws_imagebuilder_image_pipeline`](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/imagebuilder_image_pipeline#argument-reference "https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/imagebuilder_image_pipeline#argument-reference")in the Terraform documentation.
