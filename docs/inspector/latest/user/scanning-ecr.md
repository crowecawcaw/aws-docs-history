# Scanning Amazon Elastic Container Registry container images with Amazon Inspector

Amazon Inspector scans container images stored in Amazon Elastic Container Registry for software vulnerabilities to generate package vulnerability findings.
When you activate Amazon ECR scanning, you set Amazon Inspector as the preferred scanning service for your private registry.

###### Note

Amazon ECR uses a registry policy to grant permissions to an AWS principal.
This principal has the required permissions to call Amazon Inspector APIs for scanning.
When setting the scope of your registry policy, you must not add the `ecr:*` action or `PutRegistryScanningConfiguration` in `deny`.
This results in errors at the registry level when enabling and disabling scanning for Amazon ECR.

With basic scanning, you can configure your repositories to scan on push or perform manual scans.
With enhanced scanning, you scan for operating system and programming language package vulnerabilities at the registry level.
For a side-by-side comparison of the differences between basic and enhanced scanning, see the [Amazon Inspector FAQ](https://aws.amazon.com/inspector/faqs/ "https://aws.amazon.com/inspector/faqs/").

###### Note

Basic scanning is provided and billed through Amazon ECR.
For more information, see [Amazon Elastic Container Registry pricing](https://aws.amazon.com/ecr/pricing/ "https://aws.amazon.com/ecr/pricing/").
Enhanced scanning is provided and billed through Amazon Inspector.
For more information, see [Amazon Inspector pricing](https://aws.amazon.com/inspector/pricing/ "https://aws.amazon.com/inspector/pricing/").

For information about how to activate Amazon ECR scanning, see [Activating a scan type](activate-scans.md "activate-scans.md").
For information about how to view findings, see [Viewing Amazon Inspector findings](findings-understanding-locating-analyzing.md "findings-understanding-locating-analyzing.md").
For information about how to view findings within Amazon ECR at the image level, see [Image scanning](../../../AmazonECR/latest/userguide/image-scanning.md "../../../AmazonECR/latest/userguide/image-scanning.md") in the _Amazon Elastic Container Registry User Guide_.
You can manage findings using AWS services not available for basic scanning, like [AWS Security Hub and Amazon EventBridge](integrations.md "integrations.md").

You can view the scan configuration for each repository in Amazon Inspector through coverage pages and APIs.
However, the configuration settings for basic scanning versus continuous scanning can only be modified in Amazon ECR.
Amazon Inspector provides visibility into these settings but does not offer direct modification capabilities.
For more information, see [Scan images for software vulnerabilities in Amazon ECR](../../../AmazonECR/latest/userguide/image-scanning.md "../../../AmazonECR/latest/userguide/image-scanning.md") in the _Amazon ECR User Guide_.

This section provides information about Amazon ECR scanning and describes how to configure enhanced scanning for Amazon ECR repositories.

## Scan behaviors for Amazon ECR scanning

When you first activate Amazon ECR scanning, Amazon Inspector detects images pushed within the last 14 days.
Amazon Inspector then scans the images and sets the scan statuses to `active`.
If continuous scanning is enabled, Amazon Inspector monitors images as long as they were pushed within 14 days (by default), the last-in-use date is within 14 days (by default), or the images are scanned within the configured re-scan duration.
For Amazon Inspector accounts that were created prior to May 16th, 2025, the default configuration is for re-scan to monitor images if they were pushed or pulled within the last 90 days.
For more information, see [Configuring the Amazon ECR re-scan duration](scanning_resources_configure_duration_setting_ecr.md "scanning_resources_configure_duration_setting_ecr.md").

For continuous scanning, Amazon Inspector initiates new vulnerability scans of container
images in the following situations:

- Whenever a new container image is pushed.
- Whenever Amazon Inspector adds a new common vulnerabilities and exposures (CVE) item
  to its database, and that CVE is relevant to that container image
  (continuous scanning only).

If you configure your repository for on push scanning, images are only scanned
when you push them.

You can check when a container image was last checked for vulnerabilities from the
**Container images** tab on the **Account
management** page or by using the [ListCoverage](../../v2/APIReference/API_ListCoverage.md "../../v2/APIReference/API_ListCoverage.md") API. Amazon Inspector updates the **Last
scanned at** field of an Amazon ECR image in response to the following
events:

- When Amazon Inspector completes an initial scan of a container image.
- When Amazon Inspector re-scans a container image because a new common vulnerabilities
  and exposures (CVE) item that impacts that container image was added to the
  Amazon Inspector database.

## Mapping container images to running containers

Amazon Inspector provides comprehensive container security management by mapping container images to running containers across Amazon Elastic Container Service (Amazon ECS) and Amazon Elastic Kubernetes Service (Amazon EKS).
These mappings provide insights into vulnerabilities for images on running containers.

###### Note

The managed policy `AWSReadOnlyAccess` alone does not provide sufficient permissions to view the mapping between Amazon ECR images and running containers.
You need both the `AWSReadOnlyAccess` and `AWSInspector2ReadOnlyAccess` managed policies to view container image mapping information.

You can prioritize remediation efforts based on operational risks and maintain security coverage across the entire container ecosystem.
You can view how many container images are currently in use and which container images were last used on an Amazon ECS or Amazon EKS cluster in the past 24 hours.
You can also view how many Amazon ECS tasks and Amazon EKS pods are deployed.
This information can be found in the Amazon Inspector console on the details screen for container image findings and with the `ecrImageInUseCount` and `ecrImageLastInUseAt` filters for the [`FilterCriteria`](../../v2/APIReference/API_FilterCriteria.md "../../v2/APIReference/API_FilterCriteria.md") data type.
For new container images or accounts, it can take up to 36 hours for data to be available.
Afterwards, this data is updated once every 24 hours.
For more information, see [Viewing Amazon Inspector findings](findings-understanding-locating-analyzing.md "findings-understanding-locating-analyzing.md") and [Viewing details for Amazon Inspector findings](findings-understanding-details.md "findings-understanding-details.md").

###### Note

This data is automatically sent to Amazon ECR findings when you activate Amazon ECR scanning and configure your repository for continuous scanning.
Continuous scanning must be configured at the Amazon ECR repository level.
For more information, see [Enhanced scanning](../../../AmazonECR/latest/userguide/image-scanning-enhanced.md "../../../AmazonECR/latest/userguide/image-scanning-enhanced.md") in the _Amazon Elastic Container Registry User Guide_.

You can also [re-scan container images](scanning_resources_configure_duration_setting_ecr.md "scanning_resources_configure_duration_setting_ecr.md") from clusters based on their last-in-use date.

This feature is also supported on Fargate with Amazon ECS and Amazon EKS.

## Supported operating systems and media types

For information about supported operating systems, see [Supported operating systems: Amazon ECR scanning with Amazon Inspector](supported.md#supported-os-ecr "supported.md#supported-os-ecr").

Amazon Inspector scans of Amazon ECR repositories cover the following supported media types:

###### Image manifest

- `"application/vnd.oci.image.manifest.v1+json"`
- `"application/vnd.docker.distribution.manifest.v2+json"`

###### Image configuration

- `"application/vnd.docker.container.image.v1+json"`
- `"application/vnd.oci.image.config.v1+json"`

###### Image layers

- `"application/vnd.docker.image.rootfs.diff.tar"`
- `"application/vnd.docker.image.rootfs.diff.tar.gzip"`
- `"application/vnd.docker.image.rootfs.foreign.diff.tar.gzip"`
- `"application/vnd.oci.image.layer.v1.tar"`
- `"application/vnd.oci.image.layer.v1.tar+gzip"`
- `"application/vnd.oci.image.layer.v1.tar+zstd"`
- `"application/vnd.oci.image.layer.nondistributable.v1.tar"`
- `"application/vnd.oci.image.layer.nondistributable.v1.tar+gzip"`

###### Note

Amazon Inspector does not support the `"application/vnd.docker.distribution.manifest.list.v2+json"` media type for the scanning of Amazon ECR repositories.
