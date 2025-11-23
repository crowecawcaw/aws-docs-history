Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Specifying runtime environment images

A _runtime environment image_ is a Docker container within which CodeCatalyst
runs workflow actions. The Docker container runs on top of your chosen compute platform, and includes
an operating system and extra tools that a workflow action might need, such as the AWS CLI,
Node.js, and .tar.

By default, workflow actions will run on one of the [active images](#build-curated-images "#build-curated-images") that are supplied and maintained by CodeCatalyst. Only build and test
actions support custom images. For more information, see [Assigning a custom runtime environment Docker
image to an action](#build-images-specify "#build-images-specify").

###### Topics

- [Active images](#build-curated-images "#build-curated-images")
- [What if an active image doesn't include the
  tools I need?](#build-images-more-tools "#build-images-more-tools")
- [Assigning a custom runtime environment Docker
  image to an action](#build-images-specify "#build-images-specify")
- [Examples](#workflows-working-custom-image-ex "#workflows-working-custom-image-ex")

## Active images

_Active images_ are runtime environment images that are fully
supported by CodeCatalyst and include preinstalled tooling. There are currently two sets of
active images: one released in March 2024, and another released in November 2022.

Whether an action uses a March 2024 or November 2022 image depends on the
action:

- Build and test actions that are added to a workflow on or after March 26, 2024
  will include a `Container` section in their YAML definition that
  explicitly specifies a [March 2024
  image](#build.default-image "#build.default-image"). You can optionally remove the `Container` section
  to revert back to the [November 2022
  image](#build.previous-image "#build.previous-image").
- Build and test actions that were added to a workflow prior to March 26, 2024
  will _not_ include a `Container` section in their
  YAML definition, and consequently will use a [November 2022 image](#build.previous-image "#build.previous-image"). You can keep the
  November 2022 image, or you can upgrade it. To upgrade the image, open the
  action in the visual editor, choose the **Configuration** tab,
  and then select the March 2024 image from the **Runtime environment
  docker image** drop-down list. This selection will add a
  `Container` section to the action's YAML definition that is
  populated with the appropriate March 2024 image.
- All other actions will use either a [November 2022 image](#build.previous-image "#build.previous-image") or a [March
  2024 image](#build.default-image "#build.default-image"). For more information, see the action's documentation.

###### Topics

- [March 2024 images](#build.default-image "#build.default-image")
- [November 2022 images](#build.previous-image "#build.previous-image")

### March 2024 images

The March 2024 images are the latest images provided by CodeCatalyst. There is one March
2024 image per compute type/fleet combination.

The following table shows the tools installed on each March 2024 image.

| March 2024 image tools | Tool       | CodeCatalyst Amazon EC2 for Linux x86_64 -<br>`CodeCatalystLinux_x86_64:2024_03` | CodeCatalyst Lambda for Linux x86_64 -<br>`CodeCatalystLinuxLambda_x86_64:2024_03` | CodeCatalyst Amazon EC2 for Linux Arm64 -<br>`CodeCatalystLinux_Arm64:2024_03` | CodeCatalyst Lambda for Linux Arm64 -<br>`CodeCatalystLinuxLambda_Arm64:2024_03` |
| ---------------------- | ---------- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| AWS CLI                | 2.15.17    | 2.15.17                                                                          | 2.15.17                                                                            | 2.15.17                                                                        |
| AWS Copilot CLI        | 1.32.1     | 1.32.1                                                                           | 1.32.1                                                                             | 1.32.1                                                                         |
| Docker                 | 24.0.9     | N/A                                                                              | 24.0.9                                                                             | N/A                                                                            |
| Docker Compose         | 2.23.3     | N/A                                                                              | 2.23.3                                                                             | N/A                                                                            |
| Git                    | 2.43.0     | 2.43.0                                                                           | 2.43.0                                                                             | 2.43.0                                                                         |
| Go                     | 1.21.5     | 1.21.5                                                                           | 1.21.5                                                                             | 1.21.5                                                                         |
| Gradle                 | 8.5        | 8.5                                                                              | 8.5                                                                                | 8.5                                                                            |
| Java                   | Corretto17 | Corretto17                                                                       | Corretto17                                                                         | Corretto17                                                                     |
| Maven                  | 3.9.6      | 3.9.6                                                                            | 3.9.6                                                                              | 3.9.6                                                                          |
| Node.js                | 18.19.0    | 18.19.0                                                                          | 18.19.0                                                                            | 18.19.0                                                                        |
| npm                    | 10.2.3     | 10.2.3                                                                           | 10.2.3                                                                             | 10.2.3                                                                         |
| Python                 | 3.9.18     | 3.9.18                                                                           | 3.9.18                                                                             | 3.9.18                                                                         |
| Python3                | 3.11.6     | 3.11.6                                                                           | 3.11.6                                                                             | 3.11.6                                                                         |
| pip                    | 22.3.1     | 22.3.1                                                                           | 22.3.1                                                                             | 22.3.1                                                                         |
| .NET                   | 8.0.100    | 8.0.100                                                                          | 8.0.100                                                                            | 8.0.100                                                                        |

### November 2022 images

There is one November 2022 image per compute type/fleet combination. There is also
a November 2022 Windows image available with the build action if you've configured a
[provisioned fleet](workflows-working-compute.md#compute.fleets "workflows-working-compute.md#compute.fleets").

The following table shows the tools installed on each November 2022 image.

| November 2022 image tools | Tool       | CodeCatalyst Amazon EC2 for Linux x86_64 -<br>`CodeCatalystLinux_x86_64:2022_11` | CodeCatalyst Lambda for Linux x86_64 -<br>`CodeCatalystLinuxLambda_x86_64:2022_11` | CodeCatalyst Amazon EC2 for Linux Arm64 -<br>`CodeCatalystLinux_Arm64:2022_11` | CodeCatalyst Lambda for Linux Arm64 -<br>`CodeCatalystLinuxLambda_Arm64:2022_11` | CodeCatalyst Amazon EC2 for Windows x86_64 -<br>`CodeCatalystWindows_x86_64:2022_11` |
| ------------------------- | ---------- | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| AWS CLI                   | 2.15.17    | 2.15.17                                                                          | 2.15.17                                                                            | 2.15.17                                                                        | 2.13.19                                                                          |
| AWS Copilot CLI           | 0.6.0      | 0.6.0                                                                            | N/A                                                                                | N/A                                                                            | 1.30.1                                                                           |
| Docker                    | 23.01      | N/A                                                                              | 23.0.1                                                                             | N/A                                                                            | N/A                                                                              |
| Docker Compose            | 2.16.0     | N/A                                                                              | 2.16.0                                                                             | N/A                                                                            | N/A                                                                              |
| Git                       | 2.40.0     | 2.40.0                                                                           | 2.39.2                                                                             | 2.39.2                                                                         | 2.42.0                                                                           |
| Go                        | 1.20.2     | 1.20.2                                                                           | 1.20.1                                                                             | 1.20.1                                                                         | 1.19                                                                             |
| Gradle                    | 8.0.2      | 8.0.2                                                                            | 8.0.1                                                                              | 8.0.1                                                                          | 8.3                                                                              |
| Java                      | Corretto17 | Corretto17                                                                       | Corretto17                                                                         | Corretto17                                                                     | Corretto17                                                                       |
| Maven                     | 3.9.4      | 3.9.4                                                                            | 3.9.0                                                                              | 3.9.0                                                                          | 3.9.4                                                                            |
| Node.js                   | 16.20.2    | 16.20.2                                                                          | 16.19.1                                                                            | 16.14.2                                                                        | 16.20.0                                                                          |
| npm                       | 8.19.4     | 8.19.4                                                                           | 8.19.3                                                                             | 8.5.0                                                                          | 8.19.4                                                                           |
| Python                    | 3.9.15     | 2.7.18                                                                           | 3.11.2                                                                             | 2.7.18                                                                         | 3.9.13                                                                           |
| Python3                   | N/A        | 3.9.15                                                                           | N/A                                                                                | 3.11.2                                                                         | N/A                                                                              |
| pip                       | 22.2.2     | 22.2.2                                                                           | 23.0.1                                                                             | 23.0.1                                                                         | 22.0.4                                                                           |
| .NET                      | 6.0.407    | 6.0.407                                                                          | 6.0.406                                                                            | 6.0.406                                                                        | 6.0.414                                                                          |

## What if an active image doesn't include the

tools I need?

If none of the [active images](#build-curated-images "#build-curated-images") supplied by
CodeCatalyst include the tools you need, you have a couple of options:

- You can provide a custom runtime environment Docker image that includes the
  necessary tools. For more information, see [Assigning a custom runtime environment Docker
  image to an action](#build-images-specify "#build-images-specify").

###### Note

If you want to provide a custom runtime environment Docker image, make
sure that your custom image has Git installed in it.

- You can have your workflow's build or test action install the tools you
  need.

For example, you could include the following instructions in the
`Steps` section of the build or test action's YAML code:

```
Configuration:
  Steps:
    - Run: ./`setup-script`
```

The `setup-script` instruction would then run the
following script to install the Node package manager (npm):

```
#!/usr/bin/env bash
echo "Setting up environment"

touch ~/.bashrc
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash
source ~/.bashrc
nvm install v16.1.0
source ~/.bashrc
```

For more information about the build action YAML, see [Build and test actions YAML](build-action-ref.md "build-action-ref.md").

## Assigning a custom runtime environment Docker

image to an action

If you don't want to use an [Active image](#build-curated-images "#build-curated-images")
supplied by CodeCatalyst, you can provide a custom runtime environment Docker image. If you
want to provide a custom image, make sure it has Git installed in it. The image can
reside in Docker Hub, Amazon Elastic Container Registry, or any public repository.

To learn how to create a custom Docker image, see [Containerize an
application](https://docs.docker.com/get-started/02_our_app/ "https://docs.docker.com/get-started/02_our_app/") in the Docker documentation.

Use the following instructions to assign your custom runtime environment Docker image
to an action. After specifying an image, CodeCatalyst deploys it to your compute platform when
the action starts.

###### Note

The following actions do not support custom runtime environment Docker images:
**Deploy CloudFormation stack**, **Deploy to ECS**, and
**GitHub Actions**. custom runtime environment Docker images
also do not support the **Lambda** compute type.

Visual

###### To assign a custom runtime environment Docker image using the visual

editor

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
3. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
4. Choose **Edit**.
5. Choose **Visual**.
6. In the workflow diagram, choose the action that will use your
   custom runtime environment Docker image.
7. Choose the **Configuration** tab.
8. Near the bottom, fill out the following fields.

**Runtime environment Docker image -
optional**

Specify the registry where your image is stored. Valid values include:

    * `CODECATALYST` (YAML
     editor)


    The image is stored in the CodeCatalyst registry.
    * **Docker Hub** (visual editor) or `DockerHub` (YAML
     editor)


    The image is stored in the Docker Hub image registry.
    * **Other registry** (visual editor) or `Other` (YAML
     editor)


    The image is stored in a custom image registry. Any publicly available registry can be
     used.
    * **Amazon Elastic Container Registry** (visual editor) or `ECR` (YAML editor)


    The image is stored in an Amazon Elastic Container Registry image repository. To use an image in an Amazon ECR
     repository, this action needs access to Amazon ECR. To enable this access, you must create an
     [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md")
     that includes the following permissions and custom trust policy. (You can modify an existing
     role to include the permissions and policy, if you want.)


    The IAM role must include the following permissions in its role policy:




    	+ `ecr:BatchCheckLayerAvailability`
    	+ `ecr:BatchGetImage`
    	+ `ecr:GetAuthorizationToken`
    	+ `ecr:GetDownloadUrlForLayer`
    The IAM role must include the following custom trust policy:


    For more information about creating IAM roles, see [Creating a role using custom
     trust policies (console)](../../../IAM/latest/UserGuide/id_roles_create_for-custom.md "../../../IAM/latest/UserGuide/id_roles_create_for-custom.md") in the *IAM User Guide*.


    Once you have created the role, you must assign it to the action through an environment.
     For more information, see [Associating an environment with
     an action](deploy-environments-add-app-to-environment.md "deploy-environments-add-app-to-environment.md").

**ECR image URL**, **Docker Hub
image** or **Image URL**

Specify one of the following:

    * If you are using a `CODECATALYST` registry, set the image to one of the of
     the following [active
     images](#build-curated-images "#build-curated-images"):




    	+ `CodeCatalystLinux_x86_64:2024_03`
    	+ `CodeCatalystLinux_x86_64:2022_11`
    	+ `CodeCatalystLinux_Arm64:2024_03`
    	+ `CodeCatalystLinux_Arm64:2022_11`
    	+ `CodeCatalystLinuxLambda_x86_64:2024_03`
    	+ `CodeCatalystLinuxLambda_x86_64:2022_11`
    	+ `CodeCatalystLinuxLambda_Arm64:2024_03`
    	+ `CodeCatalystLinuxLambda_Arm64:2022_11`
    	+ `CodeCatalystWindows_x86_64:2022_11`
    * If you are using a Docker Hub registry, set the image to the Docker Hub image name and
     optional tag.


    Example: `postgres:latest`
    * If you are using an Amazon ECR registry, set the image to the Amazon ECR registry URI.


    Example:
     `111122223333.dkr.ecr.us-west-2.amazonaws.com/codecatalyst-ecs-image-repo`
    * If you are using a custom registry, set the image to the value expected by the custom
     registry.

9. (Optional) Choose **Validate** to validate the
   workflow's YAML code before committing.
10. Choose **Commit**, enter a commit message, and
    choose **Commit** again.

YAML

###### To assign a custom runtime environment Docker image using the YAML

editor

1. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
2. Choose the name of your workflow. You can filter by the source
   repository or branch name where the workflow is defined, or filter
   by workflow name or status.
3. Choose **Edit**.
4. Choose **YAML**.
5. Find the action that you want to assign a runtime environment
   Docker image to.
6. In the action, add a `Container` section and underlying
   `Registry` and `Image` properties. For
   more information, see the description of the `Container`,
   `Registry` and `Image` properties in the
   [Actions](workflow-reference.md#actions-reference "workflow-reference.md#actions-reference") for your action.
7. (Optional) Choose **Validate** to validate the
   workflow's YAML code before committing.
8. Choose **Commit**, enter a commit message, and
   choose **Commit** again.

## Examples

The following examples show how to assign a custom runtime environment Docker image to
an action in the workflow definition file.

###### Topics

- [Example: Using a
  custom runtime environment Docker image to add support for Node.js 18 with
  Amazon ECR](#workflows-working-custom-image-ex-ecr-node18 "#workflows-working-custom-image-ex-ecr-node18")
- [Example: Using a
  custom runtime environment Docker image to add support for Node.js 18 with
  Docker Hub](#workflows-working-custom-image-ex-docker-node18 "#workflows-working-custom-image-ex-docker-node18")

### Example: Using a

custom runtime environment Docker image to add support for Node.js 18 with
Amazon ECR

The following example shows how to use a custom runtime environment Docker image
to add support for Node.js 18 with [Amazon ECR](https://gallery.ecr.aws/amazonlinux/amazonlinux "https://gallery.ecr.aws/amazonlinux/amazonlinux").

```
Configuration:
  Container:
    Registry: ECR
    Image: public.ecr.aws/amazonlinux/amazonlinux:2023
```

### Example: Using a

custom runtime environment Docker image to add support for Node.js 18 with
Docker Hub

The following example shows how to use a custom runtime environment Docker image
to add support for Node.js 18 with [Docker
Hub](https://hub.docker.com/_/node "https://hub.docker.com/_/node").

```
Configuration:
  Container:
    Registry: DockerHub
    Image: node:18.18.2
```
