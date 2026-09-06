

# Step 1: Review security disclaimer
<a name="transform-containers-step-disclaimer"></a>

Before the containerization workflow begins, AWS Transform presents a security disclaimer that you must review and accept.

## What the disclaimer covers
<a name="transform-containers-disclaimer-details"></a>

The containerization process requires internet access to download application dependencies (such as packages from public registries like npm, PyPI, or Maven Central). The security disclaimer informs you that:
+ Build environments will have outbound internet access to resolve and download dependencies specified in your application's build configuration.
+ You are responsible for reviewing the dependencies that your application requires and ensuring they meet your organization's security policies.
+ You can optionally configure private dependency sources (such as AWS CodeArtifact repositories or private Amazon ECR base images) in a later step to avoid downloading from public registries.

## What you need to do
<a name="transform-containers-disclaimer-user-actions"></a>

**To review and accept the security disclaimer**

1. Read the security disclaimer that AWS Transform presents.

1. Accept the disclaimer to proceed with the containerization workflow.

After you accept the disclaimer, AWS Transform proceeds to the next step where you provide your source code.

**Note**  
The connector configuration for AWS CodeConnections and Amazon ECR is no longer required upfront. AWS Transform prompts you to configure access to these services later in the workflow, only when needed. For example, you configure CodeConnections when you choose to clone from Git repositories, and you configure Amazon ECR access when you are ready to publish container images.