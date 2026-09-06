

# Step 2: Clone source code
<a name="transform-containers-step-clone"></a>

In this step, you provide your application source code to AWS Transform. You can provide source code from Git repositories or by uploading zip files.

## Option 1: Git repositories
<a name="transform-containers-clone-git"></a>

You can provide your source code from Git repositories. If you have not yet configured AWS CodeConnections, AWS Transform prompts you to provide your CodeConnections ARN at this point. You have two ways to specify your repositories:
+ **Upload a CSV file** — Prepare a CSV file with columns `repo_name` and `branch`. The `repo_name` must be in `owner/repo-name` format. The `branch` column is optional; leave it empty to use the repository's default branch. Example:

  ```
  repo_name,branch
  owner/my-app,main
  owner/api-service,develop
  owner/another-repo,
  ```
+ **Provide repository details in the chat** — Tell AWS Transform the repository name(s) and branch(es) directly in the chat instead of uploading a CSV.

AWS Transform validates that each repository exists and is accessible through your CodeConnections configuration, then clones the repositories.

**Note**  
Individual files must not exceed 1 GB, and the total size of all repositories must not exceed 8 GB. AWS Transform clones multiple repositories concurrently for faster processing.

**Important**  
Applications that span multiple repositories are not supported through the Git clone option. If your application requires source code from multiple repositories, package them together as a zip file and use the zip upload option instead.

## Option 2: Zip file upload
<a name="transform-containers-clone-zip"></a>

If you did not configure CodeConnections, or prefer to upload your source code directly, you can upload zip files.

**To upload source code as zip files**

1. When prompted, upload one zip file per application. You can drag files into the chat or use the attachment button.

1. Each zip file should contain the source code for one application.

1. Individual files must not exceed 1 GB, and the total size of all uploads must not exceed 8 GB.

## Optional: Configure private dependencies
<a name="transform-containers-clone-private-deps"></a>

If your application depends on packages from private registries, you can configure private dependency sources during this step. AWS Transform supports the following private dependency types:
+ **AWS CodeArtifact repositories** — Configure Maven, PyPI, or npm repositories hosted in AWS CodeArtifact. AWS Transform presents a list of available repositories in your account for you to select from.
+ **Private Amazon ECR base images** — If your Dockerfiles use base images from a private Amazon ECR repository, provide the repository details so that the build environment can pull these images.

When you configure private dependencies, AWS Transform prompts you to connect to the AWS account where these resources are hosted. This connector configuration is only required if you use private dependencies.

## Confirming containerization preferences
<a name="transform-containers-clone-confirm"></a>

After your source code is available, AWS Transform asks if you have specific instructions for how the containerization should be done. You can optionally specify:
+ Whether to generate a new Dockerfile or reuse an existing one.
+ Whether to process a specific service in a monorepo, or all services.
+ Any other preferences for the containerization process.

The defaults are:

1. Use Amazon Linux 2023 base image (`public.ecr.aws/amazonlinux/amazonlinux:latest`).

1. Process all applications in the repository.

1. Reuse an existing Dockerfile if present, with minor modifications if needed.

You can confirm to proceed with defaults, or provide specific instructions.