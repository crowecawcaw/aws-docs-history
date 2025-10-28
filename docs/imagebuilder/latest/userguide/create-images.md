# Create custom images with Image Builder

There are several different ways that you can create a new Image Builder image.
For example, you can use one of the following methods to create an image with
the AWS Management Console or AWS CLI. You can also use the [CreateImage](../APIReference/API_CreateImage.md "../APIReference/API_CreateImage.md") API action or
run a build pipeline to create the image. For the SDK request associated with the
API action, you can refer to the [See Also](../APIReference/API_CreateImage.md#API_CreateImage_SeeAlso "../APIReference/API_CreateImage.md#API_CreateImage_SeeAlso")
link for that command in the _EC2 Image Builder API Reference_.

AWS Management Console
To create a new image from an existing pipeline, you can manually run the
pipeline, as follows. You can also use the pipeline wizard to create a new
image from scratch. See [Pipeline wizard: Create AMI](start-build-image-pipeline.md "start-build-image-pipeline.md") or
[Pipeline wizard: Create container image](start-build-container-pipeline.md "start-build-container-pipeline.md"),
depending on the type of image you want to create.

1. Open the EC2 Image Builder console at
   [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/ "https://console.aws.amazon.com/imagebuilder/").
2. Choose **Image pipelines** from the
   navigation pane.
3. Select the check box next to the **Pipeline
   name** that you want to run.
4. To create the image, select **Run pipeline**
   from the **Actions** menu. This starts
   the pipeline.

You can also specify a schedule to run your pipeline, or use Amazon EventBridge
to run your pipeline based on rules that you configure.

AWS CLI
Before you run the **[create-image](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-image.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-image.html")** command in the AWS CLI, you must
create the following resources if they don't already exist:

###### Required resources

- **Recipe** – You must specify
  exactly one recipe for your image, as follows:

Image recipe

Specify the Amazon Resource Name (ARN) for your image
recipe resource with the `--image-recipe-arn`
parameter.

Container recipe

Specify the ARN for your container recipe resource
with the `--container-recipe-arn`
parameter.

- **Infrastructure configuration** – Specify the ARN
  for your infrastructure configuration resource with the
  `--infrastructure-configuration-arn`
  parameter.

You can also specify any of the following resources that your image requires:

###### Optional resources and configuration

- **Distribution configuration**
  – By default, Image Builder distributes the output image resource to
  your account in the Region where you run the
  **create-image** command. To provide additional
  destinations or configuration for your distribution, specify the ARN
  for your distribution configuration resource with the
  `--distribution-configuration-arn` parameter.
- **Image scanning** – To
  configure snapshots for Amazon Inspector findings on your image or container
  test instance, use the `--image-scanning-configuration`
  parameter. For container images you also specify the ECR repository
  that Amazon Inspector uses for its scans.
- **Image tests** – To suppress
  the Image Builder test stage, use the `--image-tests-configuration`
  parameter. Alternatively, you can set a timeout for how long it can run.
- **Image tags** – Use the
  `--tags` parameter to add tags to your output
  image resource.
- **Image workflows** – If you don't
  specify any build or test workflows, Image Builder creates your image with its
  default image workflow. To specify workflows that you've created, use the
  `--workflows` parameter.

###### Note

If you specify image workflows, you must also provide the name or ARN
of the IAM role that Image Builder uses to run your workflow actions in the
`--execution-role` parameter.

The following example shows how to create an image with the
[create-image](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-image.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-image.html")
AWS CLI command. For more information, see the
_AWS CLI Command Reference_.

**Example: Create a basic image with default distribution**

```
`aws imagebuilder create-image --image-recipe-arn arn:aws:imagebuilder:`us-west-2`:`123456789012`:image-recipe/`simple-recipe-linux`/`1.0.0` --infrastructure-configuration-arn arn:aws:imagebuilder:`us-west-2`:`123456789012`:infrastructure-configuration/`simple-infra-config-linux``
```

**Output:**

```
`{
"requestId": "1abcd234-e567-8fa9-0123-4567b890cd12",
"imageVersionList": [
 {
 "arn": "arn:aws:imagebuilder:`us-west-2`:`123456789012`:image/`simple-recipe-linux`/`1.0.0`",
 "name": "`simple-recipe-linux`",
 ...
 }
]
}`
```

## Cancel image

creation from the AWS CLI

To cancel an in-progress image build, use the
**cancel-image-creation** command, as follows:

```
aws imagebuilder cancel-image-creation --image-build-version-arn arn:aws:imagebuilder:us-west-`2:123456789012`:image/`my-example-recipe`/2019.12.03/1
```
