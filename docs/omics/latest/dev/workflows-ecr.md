

# Container images for private workflows
<a name="workflows-ecr"></a>

When you create a workflow, you can specify the container registries and images required by your workflow. HealthOmics runs the container images that your workflow tasks use. You can use images from your own Amazon ECR private repositories and from third-party container registries. HealthOmics supports container images from Amazon ECR Public, Docker Hub, Quay, GitHub Container Registry, Kubernetes container image registry, Microsoft Azure Container Registry, GitLab Container Registry, Seqera Containers, NVIDIA NGC, Google Artifact Registry, and Google Container Registry.

You can select one or more container registries and images for your workflow.
+ **Use your own Amazon ECR images:** You can reference images that you host in Amazon ECR private repositories. To create your own private repository, see [Creating an Amazon ECR private repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html) in the *Amazon Elastic Container Registry User Guide*.

  You can reference these images directly in your workflow definition, pass them as workflow parameters, or map them with image mappings. For more information, see [Image mappings](containers-workflow-creation.md#ecr-pull-through-mapping-format).
+ **Use third-party registries that pull through cache supports:** You can pull images from third-party registries that pull through cache (PTC) supports, such as Docker Hub, Quay, GitHub Container Registry, and Amazon ECR Public. HealthOmics synchronizes them automatically. For more information, see [Using third-party registries supported by pull through cache](containers-ptc-registries.md).
+ **Use third-party registries that pull through cache doesn't support:** You can also use container images from registries that PTC doesn't support, such as Seqera, NVIDIA NGC, and Google Container Registry or Google Artifact Registry. For more information, see [Using third-party registries not supported by pull through cache](containers-non-ptc-registries.md).

## General considerations for Amazon ECR container images
<a name="ecr-considerations"></a>
+ Region – Your Amazon ECR repository resides in the same AWS Region as the account calling the service.
+ Cross-account images – A different AWS account can own the container image, as long as the source image repository provides the appropriate permissions. For more information, see [Policies for cross-account Amazon ECR access](permissions-ecr.md#permissions-cross-account).
+ Image URIs – We recommend that you define your Amazon ECR container image Uniform Resource Identifiers (URIs) as parameters in your workflow, so that access can be verified before the run begins. This also makes it easier to run a workflow in a new Region by changing the Region parameter.
+ Permissions – Your runs need permission to reach Amazon ECR during execution. You configure IAM permissions for HealthOmics to access Amazon ECR. For more information, see [HealthOmics Resource permissions](permissions-resource.md). Also see the following topics:
  + For registries that pull through cache supports: [Policies for Amazon ECR pull through cache](permissions-ecr.md#permissions-ecr-ptc)
  + For registries that pull through cache doesn't support: [Service role policy for non-PTC container support](permissions-ecr.md#permissions-ecr-non-ptc)
+ Architecture – HealthOmics supports x86\_64 containers and doesn't support ARM containers. If your local machine is ARM-based, such as Apple Mac, use a command such as the following to build an x86\_64 container image:

  ```
  docker build --platform amd64 -t my_tool:latest .
  ```
+ Entrypoint and shell – HealthOmics workflow engines inject bash scripts as a command override to the container images used by workflow tasks. Thus, container images should be built without a specified ENTRYPOINT such that a bash shell is the default. 
+ Mounted paths – HealthOmics mounts a shared filesystem to container tasks at `/tmp`. HealthOmics overrides any data or tooling built into the container image at this location.

  The workflow definition is available to tasks via a read-only mount at `/mnt/workflow`.
+ Image size – See [HealthOmics workflow fixed size quotas](fixed-quotas.md#fixed-quotas-workflows) for the maximum container image sizes.
+ Pricing – Standard Amazon ECR storage charges apply to the images in your repositories. For upstream registries that need a credential, Secrets Manager charges also apply.
+ Best practices – Review the best practices guidance at [Best practices for container images](containers-best-practices.md).

**Topics**
+ [General considerations for Amazon ECR container images](#ecr-considerations)
+ [Using third-party registries supported by pull through cache](containers-ptc-registries.md)
+ [Using third-party registries not supported by pull through cache](containers-non-ptc-registries.md)
+ [Adding private or third-party containers during workflow creation](containers-workflow-creation.md)
+ [Best practices for container images](containers-best-practices.md)