# Manage build and test workflows for Image Builder images

An image workflow defines the sequence of steps that EC2 Image Builder performs during the
build and test stages of the image creation process. This is part of the overall Image Builder
workflow framework.

###### Image workflow benefits

- With image workflows, you have more flexibility, visibility, and control over the
  image creation process.
- You can add customized workflow steps when you define your workflow document, or you
  can choose to use the Image Builder default workflow.
- You can exclude workflow steps that are included in default image workflows.
- You can create test-only workflows that skip the build process entirely. You can
  do the same to create build-only workflows.

###### Note

You can't modify an existing workflow, but you can clone it or create a new version.

###### Workflow topics

- [Workflow framework: Stages](#wf-stages "#wf-stages")
- [Service access](#wf-service-access "#wf-service-access")
- [Use managed workflows for your images](#use-managed-workflows "#use-managed-workflows")
- [List image workflows](list-image-workflows.md "list-image-workflows.md")
- [Create an image workflow](image-workflow-create-resource.md "image-workflow-create-resource.md")
- [Create a YAML workflow document](image-workflow-create-document.md "image-workflow-create-document.md")

## Workflow framework: Stages

To customize image workflows, it's important to understand the workflow stages that
make up the image creation workflow framework.

The image creation workflow framework includes the following distinct stages.

1. Build stage (pre-snapshot) –
   During the build stage, you make changes to the Amazon EC2 build instance
   that's running your base image, to create the baseline for your new
   image. For example, your recipe can include components
   that install an application or modify the operating system firewall settings.

After this stage completes successfully, Image Builder creates a snapshot or
container image that it uses for the test stage and beyond. 2. Test stage (post-snapshot) – During the
test stage, there are some differences between images that create AMIs and container images. For
AMI workflows, Image Builder launches an EC2 instance from the snapshot that it created
as the final step of the build stage. Tests run on the new instance to validate
settings and ensure that the instance is functioning as expected. For container workflows, the
tests run on the same instance that was used for building.

The workflow framework also includes a distribution stage. However, Image Builder handles
the workflows for that stage.

## Service access

To run image workflows, Image Builder needs permission to perform
workflow actions. You can specify the [AWSServiceRoleForImageBuilder](security-iam-awsmanpol.md#sec-iam-manpol-AWSServiceRoleForImageBuilder "security-iam-awsmanpol.md#sec-iam-manpol-AWSServiceRoleForImageBuilder") service-linked role, or
you can specify your own custom role for service access, as follows.

- **Console** – In the pipeline wizard
  **Step 3 Define image creation process**, select the
  service-linked role or your own custom role from the **IAM role**
  list in the **Service access** panel.
- **Image Builder API** – In the [CreateImage](../APIReference/API_CreateImage.md "../APIReference/API_CreateImage.md") action request,
  specify the service-linked role or your own custom role as the value for the
  `executionRole` parameter.

To learn more about how to create a service role, see
[Creating a role to delegate permissions to an AWS service](../../../IAM/latest/UserGuide/id_roles_create_for-service.md "../../../IAM/latest/UserGuide/id_roles_create_for-service.md") in the
_AWS Identity and Access Management User Guide_.

## Use managed workflows for your images

Managed workflows are created and maintained by AWS. When you use managed workflows
in your image pipelines or for one-off image creation, you can select the Amazon Resource
Name (ARN) of the managed workflow that you want to use. Amazon provides the latest
versions that have patches and other updates applied. To get a list of managed workflows,
see [List image workflows](list-image-workflows.md "list-image-workflows.md"), and
filter on **Owner = Amazon** (console).
