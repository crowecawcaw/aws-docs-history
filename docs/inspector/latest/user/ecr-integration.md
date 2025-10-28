# Amazon Inspector integration with Amazon Elastic Container Registry (Amazon ECR)

Amazon Elastic Container Registry is a fully managed container registry that supports Docker and OCI images and AWS artifacts.
If you use Amazon ECR, you can activate [Enhanced Scanning](../../../AmazonECR/latest/userguide/image-scanning-enhanced.md "../../../AmazonECR/latest/userguide/image-scanning-enhanced.md") for your container registry.
When you activate enhanced scanning, Amazon Inspector automatically detects and scans your container images for vulnerable operating system and programming language packages.
This integration allows you to view Amazon Inspector findings for container images and manage the frequency and scope of scans in the Amazon ECR console.
For more information, see [Scanning Amazon ECR container images with Amazon Inspector](scanning-ecr.md "scanning-ecr.md").

## Activating the integration

You can activate the integration by activating Amazon Inspector scanning through the Amazon Inspector console or
API, or by configuring your repository to use **Enhanced scanning** with
Amazon Inspector through the Amazon ECR console or API.

For more information on activating the integration through Amazon Inspector, see [Automated scan types in Amazon Inspector](scanning-resources.md "scanning-resources.md").

For information on activating and configuring **Enhanced scanning** in
Amazon ECR, see
[Enhanced Scanning](../../../AmazonECR/latest/userguide/image-scanning-enhanced.md "../../../AmazonECR/latest/userguide/image-scanning-enhanced.md") in the Amazon ECR user guide.

## Using the integration with a multi-account environment

If you are a member in a multi-account environment, you can activate enhanced scanning
through Amazon ECR. However, once activated, it can only be deactivated by your Amazon Inspector delegated
administrator. If it is deactivated, it reverts to basic scanning. For more information, see
[Deactivating Amazon Inspector](deactivating-best-practices.md "deactivating-best-practices.md").
