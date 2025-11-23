# Container images for private workflows

HealthOmics supports container images hosted in Amazon ECR private repositories. You can create container images and upload
them to the private repository. You can also use your Amazon ECR private registry as a pull through cache to synchronize the
contents of upstream registries.

Your Amazon ECR repository must reside in the same AWS Region as the account calling the service. A different
AWS account can own the container image, as long as the source image repository provides appropriate permissions.
For more information, see [Policies for cross-account Amazon ECR access](permissions-ecr.md#permissions-cross-account "permissions-ecr.md#permissions-cross-account").

We recommend that you define your Amazon ECR container image URIs as parameters in your
workflow so that access can be verified before the run begins. It also makes it easier to run a workflow in a new
Region by changing the Region parameter.

###### Note

HealthOmics doesn't support ARM containers and doesn't support access to public repositories.

For information about configuring IAM permissions for HealthOmics to access Amazon ECR, see [HealthOmics Resource permissions](permissions-resource.md "permissions-resource.md").

###### Topics

- [Synchronizing with third-party container registries](#ecr-pull-through "#ecr-pull-through")
- [General considerations for Amazon ECR container images](#ecr-considerations "#ecr-considerations")
- [Environment variables for HealthOmics workflows](#ecr-env-vars "#ecr-env-vars")
- [Using Java in Amazon ECR container images](#ecr-java-considerations "#ecr-java-considerations")
- [Add task inputs to an Amazon ECR container image](#ecr-tasks "#ecr-tasks")

## Synchronizing with third-party container registries

You can use Amazon ECR pull through cache rules to synchronize repositories in a supported upstream registry with
your Amazon ECR private repositories. For more information, see [Sync an upstream registry](../../../AmazonECR/latest/userguide/pull-through-cache.md "../../../AmazonECR/latest/userguide/pull-through-cache.md") in the _Amazon ECR User Guide_.

The pull through cache automatically creates the image repository in your private registry when you create the
cache, and it automatically synchronizes with the cached image when there are changes to the upstream image.

HealthOmics supports pull through cache for the following upstream registries:

- Amazon ECR Public
- Kubernetes container image registry
- Quay
- Docker Hub
- Microsoft Azure Container Registry
- GitHub Container Registry
- GitLab Container Registry

HealthOmics doesn't support pull through cache for an upstream Amazon ECR private repository.

Benefits of using Amazon ECR pull through cache include:

1. You avoid having to manually migrate container images to Amazon ECR or to synchronize updates from the third
   party repository.
2. Workflows access the synchronized container images in your private repository, which is more reliable than
   downloading content at run time from a public registry.
3. Because Amazon ECR pull through caches use a predictable URI structure, the HealthOmics service can automatically map
   the Amazon ECR private URI with the upstream registry URI. You aren't required to update and replace URI values in
   the workflow definition.

###### Topics

- [Configuring pull through cache](#ecr-pull-through-configure "#ecr-pull-through-configure")
- [Registry mappings](#ecr-pull-through-registry-mapping "#ecr-pull-through-registry-mapping")
- [Image mappings](#ecr-pull-through-mapping-format "#ecr-pull-through-mapping-format")

### Configuring pull through cache

Amazon ECR provides a registry for your AWS account in each Region. Make sure you create the Amazon ECR
configuration in the same region where you plan to run the workflow.

The following sections describe the configuration tasks for pull through cache.

###### Configuration tasks

- [Create a pull through cache rule](#create-ecr-ptc "#create-ecr-ptc")
- [Registry permissions for upstream registry](#reg-ecr-ptc "#reg-ecr-ptc")
- [Repository creation templates](#repo-create-templates-ptc "#repo-create-templates-ptc")
- [Creating the workflow](#reg-mapping-ecr-ptc "#reg-mapping-ecr-ptc")

#### Create a pull through cache rule

Create an Amazon ECR pull through cache rule for each upstream registry that has images you want to cache. A
rule specifies a mapping between an upstream registry and the Amazon ECR private repository.

For an upstream registry that requires authentication, you provide your credentials using
AWS Secrets Manager.

###### Note

Don't change a pull through cache rule while an active run is using the private repository.
The run could fail or, more critically, result in your pipeline using unexpected images.

For more information, see [Creating a pull through cache
rule](../../../AmazonECR/latest/userguide/pull-through-cache-creating-rule.md "../../../AmazonECR/latest/userguide/pull-through-cache-creating-rule.md") in the _Amazon Elastic Container Registry User Guide_.

##### Create a pull through cache rule using the console

To configure pull through cache, follow these steps using the Amazon ECR console:

1. Open the Amazon ECR console : https://console.aws.amazon.com/ecr
2. From the left menu, under **Private registry**, expand
   **Features & Settings**. then
   choose **Pull through cache**.
3. From the **Pull through cache** page, choose **Add rule**.
4. In the **Upstream registry** panel, choose the upstream registry to sync with
   your private registry, then choose **Next**.
5. If the upstream registry requires authentication, the console opens a new page
   where you specify the SageMaker AI secret that contains your credentials.
   Choose **Next**.
6. Under **Specify namespaces**, in the **Cache namespace** panel,
   choose whether to create the private repositories using a specific repository prefix or with no prefix.
   If you choose to use a prefix, specify the prefix name in **Cache repository prefix**.
7. In the **Upstream namespace** panel,
   choose whether to pull from upstream repositories using a specific repository prefix or with no prefix.
   If you choose to use a prefix, specify the prefix name in **Upstream repository prefix**.

The **Namespace example** panel shows an example pull request, upstream URL, and the
URL of the cache repository that is created. 8. Choose **Next**. 9. Review the configuration and choose **Create** to create the rule.

For more information, see [Create a pull through cache rule (AWS Management Console)](../../../AmazonECR/latest/userguide/pull-through-cache-creating-rule.md#pull-through-cache-creating-rule-console "../../../AmazonECR/latest/userguide/pull-through-cache-creating-rule.md#pull-through-cache-creating-rule-console").

##### Create a pull through cache rule using the CLI

Use the Amazon ECR **create-pull-through-cache-rule** command to create a pull through cache
rule. For upstream registries that require authentication, store the credentials in an Secrets Manager secret.

The following sections provide examples for each supported upstream registry.

The following example creates a pull through cache rule for the Amazon ECR
Public registry. It specifies a repository prefix of
`ecr-public`, which results in each repository created
using the pull through cache rule to have the naming scheme of
`ecr-public/`upstream-repository-name``.

```
`aws ecr create-pull-through-cache-rule \
 --ecr-repository-prefix `ecr-public` \
 --upstream-registry-url public.ecr.aws \
 --region `us-east-1``
```

The following example creates a pull through cache rule for the
Kubernetes public registry. It specifies a repository prefix of
`kubernetes`, which results in each repository created
using the pull through cache rule to have the naming scheme of
`kubernetes/`upstream-repository-name``.

```
`aws ecr create-pull-through-cache-rule \
 --ecr-repository-prefix `kubernetes` \
 --upstream-registry-url registry.k8s.io \
 --region `us-east-1``
```

The following example creates a pull through cache rule for the Quay
public registry. It specifies a repository prefix of `quay`,
which results in each repository created using the pull through cache
rule to have the naming scheme of
`quay/`upstream-repository-name``.

```
`aws ecr create-pull-through-cache-rule \
 --ecr-repository-prefix `quay` \
 --upstream-registry-url quay.io \
 --region `us-east-1``
```

The following example creates a pull through cache rule for the Docker Hub
registry. It specifies a repository prefix of `docker-hub`,
which results in each repository created using the pull through cache
rule to have the naming scheme of
`docker-hub/`upstream-repository-name``.
You must specify the full Amazon Resource Name (ARN) of the secret
containing your Docker Hub credentials.

```
`aws ecr create-pull-through-cache-rule \
 --ecr-repository-prefix `docker-hub` \
 --upstream-registry-url registry-1.docker.io \
 --credential-arn arn:aws:secretsmanager:`us-east-1`:`111122223333`:secret:`ecr-pullthroughcache/example1234` \
 --region `us-east-1``
```

The following example creates a pull through cache rule for the GitHub Container Registry.
It specifies a repository prefix of `github`, which results in
each repository created using the pull through cache rule to have the naming
scheme of
`github/`upstream-repository-name``.
You must specify the full Amazon Resource Name (ARN) of the secret
containing your GitHub Container Registry credentials.

```
`aws ecr create-pull-through-cache-rule \
 --ecr-repository-prefix `github` \
 --upstream-registry-url ghcr.io \
 --credential-arn arn:aws:secretsmanager:`us-east-1`:`111122223333`:secret:`ecr-pullthroughcache/example1234` \
 --region `us-east-1``
```

The following example creates a pull through cache rule for the Microsoft Azure Container Registry.
It specifies a repository prefix of `azure`, which
results in each repository created using the pull through cache rule to
have the naming scheme of
`azure/`upstream-repository-name``.
You must specify the full Amazon Resource Name (ARN) of the secret
containing your Microsoft Azure Container Registry credentials.

```
`aws ecr create-pull-through-cache-rule \
 --ecr-repository-prefix `azure` \
 --upstream-registry-url `myregistry`.azurecr.io \
 --credential-arn arn:aws:secretsmanager:`us-east-1`:`111122223333`:secret:`ecr-pullthroughcache/example1234` \
 --region `us-east-1``
```

The following example creates a pull through cache rule for the GitLab Container Registry.
It specifies a repository prefix of `gitlab`, which
results in each repository created using the pull through cache rule to
have the naming scheme of
`gitlab/`upstream-repository-name``.
You must specify the full Amazon Resource Name (ARN) of the secret
containing your GitLab Container Registry credentials.

```
`aws ecr create-pull-through-cache-rule \
 --ecr-repository-prefix `gitlab` \
 --upstream-registry-url registry.gitlab.com \
 --credential-arn arn:aws:secretsmanager:`us-east-1`:`111122223333`:secret:`ecr-pullthroughcache/example1234` \
 --region `us-east-1``
```

For more information, see [Create a pull through cache rule (CLI)](../../../AmazonECR/latest/userguide/pull-through-cache-creating-rule.md#pull-through-cache-creating-rule-cli "../../../AmazonECR/latest/userguide/pull-through-cache-creating-rule.md#pull-through-cache-creating-rule-cli") in the _Amazon ECR User
Guide_.

You can use the **get-run-task** CLI command to retrieve information about the container image used for a
specific task:

```
 aws omics get-run-task --id 1234567 --task-id <task_id>
```

The output includes the following information about the container image:

```
 "imageDetails": {
    "image": "string",
    "imageDigest": "string",
    "sourceImage": "string",
          ...
 }
```

#### Registry permissions for upstream registry

Use registry permissions to allow HealthOmics to use the pull through cache and to pull the container images into
the Amazon ECR private registry. Add an Amazon ECR Registry policy to the registry that provides the containers used in
runs.

The following policy grants permission for the HealthOmics service to create repositories with the specified pull
through cache prefix(es) and to initiate upstream pulls into these repositories.

1. From the Amazon ECR console, open the left menu, under **Private registry**, expand
   **Registry permissions**. then
   choose **Generate statement**.
2. On the top right side, choose JSON. Enter a policy similar to the following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowPTCinRegPermissions",
 "Effect": "Allow",
 "Principal": {
 "Service": "omics.amazonaws.com"
 },
 "Action": [
 "ecr:CreateRepository",
 "ecr:BatchImportUpstreamImage"
 ],
 "Resource": [
 "arn:aws:ecr:`us-east-1`:`123456789012`:repository/ecr-public/*",
 "arn:aws:ecr:`us-east-1`:`123456789012`:repository/docker-hub/*"
 ]
 }
 ]
}`

```

#### Repository creation templates

To use pull through caching in HealthOmics, the Amazon ECR repository must have a repository creation template. The
template defines configuration settings for when you or Amazon ECR create a private repository for an upstream
registry.

Each template contains a repository namespace prefix, which Amazon ECR uses to match new repositories to a
specific template. Templates specify the configuration for all repository settings including resource-based
access policies, tag immutability, encryption, and lifecycle policies.

For more information, see [Repository creation templates](../../../AmazonECR/latest/userguide/repository-creation-templates.md "../../../AmazonECR/latest/userguide/repository-creation-templates.md") in
the _Amazon Elastic Container Registry User Guide_.

How to create a repository creation template:

1. From the Amazon ECR console, open the left menu, under **Private registry**, expand
   **Features and settings**. then choose
   **Repository creation templates**.
2. Choose **Create template**.
3. In **Template details**, choose **Pull through cache**.
4. Choose whether to apply this template to a specific prefix or to all repositories that don't match another template.

If you choose **A specific prefix**, enter the namespace prefix value in **Prefix**.
You specified this prefix when you created the PTC rule. 5. Choose **Next**. 6. In **Add repository creation configuration** page, enter **Repository
permissions**. Use one of the sample policy statements, or enter one similar to the following
example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "PTCRepoCreationTemplate",
 "Effect": "Allow",
 "Principal": {
 "Service": "omics.amazonaws.com"
 },
 "Action": [
 "ecr:BatchGetImage",
 "ecr:GetDownloadUrlForLayer"
 ],
 "Resource": "*"
 }
 ]
}`

```

7. Optionally, you can add repository settings such as lifecycle policy and tags. Amazon ECR applies these
   rules for all container images created for pull through cache that use the specified prefix.
8. Choose **Next**.
9. Review the configuration and choose **Next**.

#### Creating the workflow

When you create a new workflow or workflow version, review the registry mappings and update them if
required. For details, see [Create a private workflow](create-private-workflow.md "create-private-workflow.md").

### Registry mappings

You define registry mappings to map between prefixes in your private Amazon ECR registry and the upstream
registry names.

For more information about Amazon ECR registry mappings, see [Creating a pull through cache rule in
Amazon ECR](../../../AmazonECR/latest/userguide/pull-through-cache-creating-rule.md "../../../AmazonECR/latest/userguide/pull-through-cache-creating-rule.md").

The following example shows registry mappings to Docker Hub, Quay, and Amazon ECR Public.

```
{
    "registryMappings": [
        {
            "upstreamRegistryUrl": "registry-1.docker.io",
            "ecrRepositoryPrefix": "docker-hub"
        },
        {
            "upstreamRegistryUrl": "quay.io",
            "ecrRepositoryPrefix": "quay"
        },
        {
            "upstreamRegistryUrl": "public.ecr.aws",
            "ecrRepositoryPrefix": "ecr-public"
        }
    ]
}
```

### Image mappings

You define image mappings to map between the image names as defined in your private Amazon ECR workflows and the
image names in the upstream registry.

You can use image mappings with registries that support pull through cache. You can also use image mappings
with upstream registries where HealthOmics doesn't support pull through cache. You need to manually synchronize the
upstream registry with your private repository.

For more information about Amazon ECR image mappings, see [Creating a pull through cache rule in
Amazon ECR](../../../AmazonECR/latest/userguide/pull-through-cache-creating-rule.md "../../../AmazonECR/latest/userguide/pull-through-cache-creating-rule.md").

The following example shows mappings from private Amazon ECR images to a public genomics image and the latest
Ubuntu image.

```
{
    "imageMappings": [
        {
            "sourceImage": "public.ecr.aws/aws-genomics/broadinstitute/gatk:4.6.0.2",
            "destinationImage": "123456789012.dkr.ecr.us-east-1.amazonaws.com/broadinstitute/gatk:4.6.0.2"
        },
        {
            "sourceImage": "ubuntu:latest",
            "destinationImage": "123456789012.dkr.ecr.us-east-1.amazonaws.com/custom/ubuntu:latest",
        }
    ]
}
```

## General considerations for Amazon ECR container images

- Architecture

HealthOmics supports x86_64 containers. If your local machine is ARM-based, such as Apple Mac, use a command such
as the following to build an x86_64 container image:

```
docker build --platform amd64 -t my_tool:latest .
```

- Entrypoint and shell

HealthOmics workflow engines inject bash scripts as a command override to the container images used by workflow tasks.
Thus, container images should be built without a specified ENTRYPOINT such that a bash shell is the default.

- Mounted paths

A shared filesystem is mounted to container tasks at /tmp. Any data or tooling built
into the container image at this location will be overridden.

The workflow definition is available to tasks via a read-only mount at /mnt/workflow.

- Image size

See [HealthOmics workflow fixed size quotas](fixed-quotas.md#fixed-quotas-workflows "fixed-quotas.md#fixed-quotas-workflows") for
the maximum container image sizes.

## Environment variables for HealthOmics workflows

HealthOmics provides environment variables that have information about the workflow running in the container. You can
use the values of these variables in the logic of your workflow tasks.

All HealthOmics workflow variables start with the `AWS_WORKFLOW_` prefix. This prefix is a protected
environment variable prefix. Don't use this prefix for your own variables in workflow containers.

HealthOmics provides the following workflow environment variables:

**AWS_REGION**

This variable is the region where the container is running.

**AWS_WORKFLOW_RUN**

This variable is the name of the current run.

**AWS_WORKFLOW_RUN_ID**

This variable is the run identifier of the current run.

**AWS_WORKFLOW_RUN_UUID**

This variable is the run UUID of the current run.

**AWS_WORKFLOW_TASK**

This variable is the name of the current task.

**AWS_WORKFLOW_TASK_ID**

This variable is the task identifier of the current task.

**AWS_WORKFLOW_TASK_UUID**

This variable is the task UUID of the current task.

The following example shows typical values for each environment variable:

```
AWS Region: us-east-1
Workflow Run: arn:aws:omics:us-east-1:123456789012:run/6470304
Workflow Run ID: 6470304
Workflow Run UUID: f4d9ed47-192e-760e-f3a8-13afedbd4937
Workflow Task: arn:aws:omics:us-east-1:123456789012:task/4192063
Workflow Task ID: 4192063
Workflow Task UUID: f0c9ed49-652c-4a38-7646-60ad835e0a2e
```

## Using Java in Amazon ECR container images

If a workflow task uses a Java application such as GATK, consider the following memory requirements for the
container:

- Java applications use stack memory and heap memory. By default, the maximum heap memory is a percentage of
  the total available memory in the container. This default depends on the specific JVM distribution and JVM
  version, so consult the relevant documentation for your JVM or explicitly set the heap memory maximum using
  Java command line options (such as `-Xmx`).
- Don't set the maximum heap memory to be 100% of the container's memory allocation, because the
  JVM stack also requires memory. Memory is also required for the JVM garbage collector
  and any other operating system processes running in the container.
- Some Java applications, such as GATK, can use native method invocations or other optimizations such as
  memory mapping files. These techniques require memory allocations that are performed “off heap”, which aren't
  controlled by the JVM maximum heap parameter.

If you know (or suspect) that your Java application allocates off-heap memory, make sure your task memory
allocation includes the off-heap memory requirements.

If these off-heap allocations cause the container to run out of memory, you typically won't see a Java
**OutOfMemory** error, because the JVM doesn't control this memory.

## Add task inputs to an Amazon ECR container image

Add all executables, libraries, and scripts needed to run a workflow task
into the Amazon ECR image that's used to run the task.

It's best practice to avoid using scripts, binaries, and libraries that are
external to a tasks container image. This is especially important when using
`nf-core` workflows that use a `bin` directory as part of
the workflow package. While this directory will be available to the workflow task,
it's mounted as a read-only directory. Required resources in this directory should
be copied into the task image and made available at runtime or when building the
container image used for the task.

See [HealthOmics workflow fixed size quotas](fixed-quotas.md#fixed-quotas-workflows "fixed-quotas.md#fixed-quotas-workflows") for the maximum size of
container image that HealthOmics supports.
