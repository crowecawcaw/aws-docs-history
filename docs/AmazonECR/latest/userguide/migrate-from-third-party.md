

# Migrate container images from a third-party registry
<a name="migrate-from-third-party"></a>

Use this guide to perform a one-time copy of container images from an external registry into your Amazon ECR private registry where ECR Pull Through Cache is not supported.

If your source is [a supported upstream registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/pull-through-cache-creating-rule.html), you do not need to perform a one-time copy. See [Sync an upstream registry with an Amazon ECR private registry](pull-through-cache.md) to configure automatic caching.

**Note**  
Amazon ECR stores the image version you copied. Newer versions from the source registry are not pulled automatically. To update an image, push the new version to your Amazon ECR repository.

## Migration overview
<a name="migrate-overview"></a>

Migrating your container images involves the following six steps:

1. Identify external image references in your build and deployment files.

1. Plan your Amazon ECR repository structure.

1. Copy images to Amazon ECR.

1. Verify image integrity.

1. Update your deployment configurations.

1. Monitor and validate.

## Prerequisites
<a name="migrate-prerequisites"></a>

Before you begin, verify the following:
+ Install and configure the AWS CLI version 2. For more information, see [Install or update to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
+ Install Docker Engine or Docker Desktop version 20.10 or later. For more information, see [Install Docker Engine](https://docs.docker.com/engine/install/) in the Docker documentation.
+ (Optional) Install `skopeo`, an open source tool for copying container images between registries without a local Docker daemon. For installation instructions, see [Skopeo](https://github.com/containers/skopeo) on GitHub.
+ Verify that your IAM identity has permissions to authenticate to your registry, create repositories, and push images. Attach the `AmazonEC2ContainerRegistryFullAccess` managed policy to the IAM user or role that you use to run these commands. For more information, see [AWS managed policies for Amazon Elastic Container Registry](security-iam-awsmanpol.md).

## Step 1: Identify external image references
<a name="migrate-identify-references"></a>

Search the files you use to build and deploy container images for references to third-party registries.

The following commands use Linux and macOS shell syntax. On Windows, use Windows Subsystem for Linux (WSL) or Git Bash.

### Identify references in deployment manifests
<a name="migrate-identify-manifests"></a>

Search your Amazon ECS task definitions or Amazon EKS manifests for non-ECR image references.

**For Kubernetes manifests:**

```
grep -rnH --include="*.yaml" --include="*.yml" "image:" . | grep -iv "dkr.ecr"
```

**For running Amazon EKS workloads:**

```
kubectl get pods --all-namespaces -o jsonpath='{range .items[*]}{range .spec.containers[*]}{.image}{"\n"}{end}{range .spec.initContainers[*]}{.image}{"\n"}{end}{end}' | sort -u | grep -iv "dkr.ecr"
```

**For Amazon ECS task definitions:**

```
aws ecs list-task-definitions --status ACTIVE --query 'taskDefinitionArns' --output text | \
  tr '\t' '\n' | \
  xargs -I {} aws ecs describe-task-definition --task-definition {} \
  --query 'taskDefinition.containerDefinitions[].image' --output text | \
  tr '\t' '\n' | sort -u | grep -iv "dkr.ecr"
```

### Identify references in Dockerfiles
<a name="migrate-identify-dockerfiles"></a>

To find `FROM` directives that reference external registries across your build directories:

```
grep -rnH --include="Dockerfile*" "FROM" . | grep -iv "dkr.ecr"
```

The output shows files and line numbers that reference images outside of Amazon ECR. For example:

```
./app/Dockerfile:1:FROM python:3.11-slim
./service/Dockerfile:1:FROM nginx:1.25
./worker/Dockerfile:3:FROM redis:7-alpine
```

### Identify pull frequency (optional)
<a name="migrate-identify-pull-frequency"></a>

To understand how frequently your workloads pull from third-party registries, review your upstream registry's usage analytics (for example, Docker Hub provides pull rate data in the account dashboard). High pull frequency increases your risk of hitting rate limits. For Docker Hub rate limits, see [Docker Hub rate limiting](https://docs.docker.com/docker-hub/download-rate-limit/) in the Docker documentation.

## Step 2: Plan your repository structure
<a name="migrate-plan-structure"></a>

Before you copy images, decide how to organize them in Amazon ECR.

**Repository naming** - Amazon ECR supports namespace prefixes with forward slashes. Use namespaces to group related images by team, environment, or application. Namespaces also enable scoped IAM policies per prefix. For example:

```
base-images/python
base-images/nginx
team-a/web-app
team-b/api-service
```

**Tag immutability** - For production images, enable tag immutability to prevent image tags from being overwritten. For more information, see [Preventing image tags from being overwritten in Amazon ECR](image-tag-mutability.md).

**Encryption** - Choose your encryption configuration before creating repositories. You cannot change the encryption configuration after repository creation. For more information, see [Encryption at rest](encryption-at-rest.md).

**Storage costs** - Amazon ECR de-duplicates image layers within each repository. If multiple images share the same base layers, you are billed for those layers only once per repository. Factor this into your cost estimates when planning which images to migrate.

**Repository creation templates** - If you are migrating many images, configure a repository creation template for create-on-push actions with your preferred settings (tag immutability, encryption, lifecycle policies). Amazon ECR applies the template settings when it creates repositories on your behalf during the first push. For more information, see [Templates to control repositories created during a pull through cache, create on push, or replication action](repository-creation-templates.md).

**Managed signing** - If you plan to sign images with managed signing, configure your signing rules before you push images. Signing occurs at push time only. For more information, see [Sign images in Amazon ECR](image-signing.md).

**Cross-Region replication** - If your workloads run in multiple AWS Regions, configure replication rules before you push images. Replication only copies images pushed after the rule is configured. For more information, see [Private image replication in Amazon ECR](replication.md).

**Note**  
Multi-architecture images (manifest lists) require that you copy all platform-specific manifests in addition to the manifest list. If you use Docker, the **docker pull** and **docker push** commands handle only the platform that matches your local architecture. Use **skopeo copy --all** to copy multi-architecture images with all platforms intact.

## Step 3: Copy images to Amazon ECR
<a name="migrate-copy-images"></a>

Before you copy images, authenticate to your Amazon ECR private registry. Your registry URL follows the format `{{account-id}}.dkr.ecr.{{region}}.amazonaws.com`. Replace `111122223333` with your AWS account ID and `us-east-1` with your Region in the examples below. In the `aws-cn` partition, the registry URL suffix is `.amazonaws.com.cn`. In all other partitions (`aws`, `aws-us-gov`), the suffix is `.amazonaws.com`.

**To find your account ID, run:**

```
aws sts get-caller-identity --query Account --output text
```

For more information about authentication methods, see [Private registry authentication in Amazon ECR](registry_auth.md).

**If you use Docker (Option A)**, authenticate with:

```
aws ecr get-login-password --region {{us-east-1}} | \
docker login --username AWS --password-stdin {{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com
```

**If you use skopeo (Option B)**, authenticate with **skopeo login** instead. Skopeo maintains its own credential store separate from Docker:

```
aws ecr get-login-password --region {{us-east-1}} | \
skopeo login {{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com --username AWS --password-stdin
```

Choose one of the following methods to copy your images.

### Option A: Copy with Docker CLI
<a name="migrate-copy-docker"></a>

Use this method for a *very* small number of single-platform images. For a detailed walk-through of the push workflow, see [Moving an image through its lifecycle in Amazon ECR](getting-started-cli.md).

1. Create the destination repository (skip this step if the repository already exists):

   ```
   aws ecr create-repository \
     --repository-name {{base-images/nginx}} \
     --region {{us-east-1}} \
     --image-tag-mutability IMMUTABLE \
     --encryption-configuration encryptionType=AES256
   ```

1. If you pull from Docker Hub with an authenticated account to avoid rate limits, run **docker login docker.io** first. Pull the image from the third-party registry:

   ```
   docker pull nginx:1.25
   ```

1. Tag the image for your Amazon ECR repository:

   ```
   docker tag nginx:1.25 {{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com/{{base-images/nginx}}:1.25
   ```

1. Push the image to Amazon ECR:

   ```
   docker push {{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com/{{base-images/nginx}}:1.25
   ```

1. To retrieve the repository URI after creation, run:

   ```
   aws ecr describe-repositories --repository-names {{base-images/nginx}} --query 'repositories[0].repositoryUri' --output text
   ```

**Note**  
The Docker CLI copies only the platform that matches your local machine. To copy multi-architecture images, use Option B with **skopeo**.

### Option B: Copy with skopeo (recommended for bulk migration)
<a name="migrate-copy-skopeo"></a>

The **skopeo** tool copies images directly between registries without pulling them to your local machine. This approach is faster for bulk operations and supports multi-architecture images. Skopeo uses transport prefixes to identify image locations. Use `docker://` for remote registries.

1. Authenticate to the source registry if required. For example, for Docker Hub:

   ```
   echo YOUR_TOKEN | skopeo login docker.io --username YOUR_USERNAME --password-stdin
   ```

1. Create the destination repository:

   ```
   aws ecr create-repository \
     --repository-name {{base-images/nginx}} \
     --region {{us-east-1}}
   ```

1. Copy the image (single platform):

   ```
   skopeo copy docker://docker.io/library/nginx:1.25 \
     docker://{{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com/{{base-images/nginx}}:1.25
   ```

1. To copy a multi-architecture image with all platforms, add the `--all` flag:

   ```
   skopeo copy --all docker://docker.io/library/nginx:1.25 \
     docker://{{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com/{{base-images/nginx}}:1.25
   ```

**Note**  
**skopeo copy** does not copy OCI referrer artifacts (signatures, SBOMs, attestations) associated with an image. If your source images have associated referrer artifacts, copy them separately or re-sign images after migration using managed signing.

**Bulk copy with a script**

To migrate multiple images, create a text file that lists source and destination pairs, then use a script to copy them.

Create a file named `images-to-migrate.txt`:

```
docker.io/library/nginx:1.25 base-images/nginx:1.25
docker.io/library/python:3.11-slim base-images/python:3.11-slim
docker.io/library/redis:7-alpine base-images/redis:7-alpine
ghcr.io/org/custom-app:v2.1.0 team-a/custom-app:v2.1.0
```

Run the following script:

```
#!/usr/bin/env bash
set -euo pipefail
ACCOUNT_ID="{{111122223333}}"
REGION="{{us-east-1}}"
REGISTRY="${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com"

aws ecr get-login-password --region ${REGION} | \
  skopeo login ${REGISTRY} --username AWS --password-stdin

while IFS=' ' read -r SOURCE DEST; do
  REPO_NAME=$(echo "${DEST}" | cut -d: -f1)

  # Create repository if it does not exist
  aws ecr create-repository \
    --repository-name "${REPO_NAME}" \
    --region "${REGION}" 2>/dev/null || true

  echo "Copying ${SOURCE} to ${REGISTRY}/${DEST}"
  skopeo copy --all "docker://${SOURCE}" "docker://${REGISTRY}/${DEST}"
done < images-to-migrate.txt
```

**Note**  
Amazon ECR enforces API rate limits on push operations. For large migrations, add retry logic with exponential backoff if you encounter throttling. Authorization tokens expire after 12 hours. If your migration takes longer, re-run the authentication command before continuing.

## Step 4: Verify image integrity
<a name="migrate-verify-integrity"></a>

After copying images, verify that the image digests in Amazon ECR match the source.

1. Get the digest of the image in Amazon ECR:

   ```
   aws ecr describe-images \
     --repository-name {{base-images/nginx}} \
     --image-ids imageTag={{1.25}} \
     --query 'imageDetails[0].imageDigest' \
     --output text
   ```
**Note**  
For single-platform images, compare digests directly. For multi-architecture images copied with `--all`, the `imageDigest` in Amazon ECR represents the manifest list. Use **skopeo inspect --raw** (shown below) to compare manifest list contents instead.

1. Compare the digest with the source registry. Use **skopeo** to inspect the source:

   ```
   skopeo inspect docker://docker.io/library/nginx:1.25 | grep Digest
   ```

1. The digests must match for single-platform images copied with **skopeo**. If they do not match, the copy did not complete successfully. Retry the copy operation. If you used Docker (Option A), the digest may differ because Docker can reprocess layers during pull and push. For exact digest preservation, use **skopeo**.

1. For multi-architecture images, **aws ecr describe-images** returns both the manifest list and individual platform manifests. To compare the manifest list digest directly, use **skopeo inspect --raw** on both source and destination:

   ```
   skopeo inspect --raw docker://{{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com/{{base-images/nginx}}:1.25
   ```

1. (Optional) Run an image scan on the migrated images to identify vulnerabilities. For more information, see [Scan images for software vulnerabilities in Amazon ECR](image-scanning.md).

## Step 5: Update deployment configurations
<a name="migrate-update-deployments"></a>

After you verify the images, update your deployment configurations to pull from Amazon ECR and update your CI/CD build pipelines to push newly built images to ECR. This ensures future image versions are available without additional manual copies.

### Amazon ECS task definitions
<a name="migrate-update-ecs"></a>

Create a new revision of your task definition with the updated image URI:

```
{
  "containerDefinitions": [
    {
      "name": "web",
      "image": "{{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com/{{base-images/nginx}}:1.25"
    }
  ]
}
```

For more information, see [Updating a task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-task-definition.html) in the *Amazon ECS Developer Guide*.

### Amazon EKS or Kubernetes manifests
<a name="migrate-update-eks"></a>

Update the `image` field in your pod specifications:

```
spec:
  containers:
    - name: web
      image: {{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com/{{base-images/nginx}}:1.25
```

Verify that your nodes can authenticate to Amazon ECR. Amazon EKS nodes use the Amazon ECR credential helper by default if the `AmazonEC2ContainerRegistryReadOnly` managed policy is attached to the node IAM role.

### Dockerfiles
<a name="migrate-update-dockerfiles"></a>

Update `FROM` directives in your Dockerfiles:

```
FROM {{111122223333}}.dkr.ecr.{{us-east-1}}.amazonaws.com/{{base-images/python}}:3.11-slim
```

## Step 6: Monitor and validate
<a name="migrate-monitor"></a>

After redeploying your workloads, verify that all image pulls now come from Amazon ECR.
+ Check CloudWatch metrics for your repositories. The `RepositoryPullCount` metric confirms that pulls are occurring. For more information, see [Amazon ECR repository metrics](ecr-repository-metrics.md).
+ Review CloudTrail for `BatchGetImage` and `GetDownloadUrlForLayer` events to confirm that your workloads pull from the expected repositories.
+ (Optional) Set up lifecycle policies to automate cleanup of old image versions. For more information, see .

## Considerations
<a name="migrate-considerations"></a>
+ **Unsupported upstream registries** - Pull Through Cache supports a specific set of upstream registries. For registries not in that list (such as JFrog Artifactory, Harbor, or Sonatype Nexus), use the Docker CLI or **skopeo** to copy images directly.
+ **Large-scale or cross-partition transfers** - For migrations across AWS partitions (for example, `aws` to `aws-cn`) or transfers involving thousands of images, see [Guidance for Data Transfer Hub on AWS](https://aws.amazon.com/solutions/guidance/data-transfer-hub-on-aws/).
+ **Lambda** - Lambda requires container images to reside in Amazon ECR and cannot pull directly from third-party registries. Use Option A or Option B to copy images to ECR before configuring your Lambda function.

## Related approaches
<a name="migrate-related-approaches"></a>

**Pull Through Cache** - If your source registry is one of the supported upstream registries and you want Amazon ECR to automatically pull and cache images rather than performing a one-time copy, see [Sync an upstream registry with an Amazon ECR private registry](pull-through-cache.md).