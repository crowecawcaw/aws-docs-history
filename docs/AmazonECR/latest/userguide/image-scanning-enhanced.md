# Scan images for OS and programming language package vulnerabilities in Amazon ECR

Amazon ECR enhanced scanning is an integration with Amazon Inspector which provides vulnerability
scanning for your container images. Your container images are scanned for both operating
systems and programming language package vulnerabilities. You can view the scan findings
with both Amazon ECR and with Amazon Inspector directly. For more information about Amazon Inspector, see [Scanning
container images with Amazon Inspector](../../../inspector/latest/user/enable-disable-scanning-ecr.md "../../../inspector/latest/user/enable-disable-scanning-ecr.md") in the _Amazon Inspector User
Guide_.

With enhanced scanning, you can choose which repositories are configured for
automatic, continuous scanning and which are configured for scan on push. This is done
by setting scan filters.

## Considerations for enhanced scanning

Consider the following before enabling Amazon ECR enhanced scanning.

- There is no additional cost from Amazon ECR to use this feature, however there
  is a cost from Amazon Inspector to scan your images. This feature is available in
  Regions where Amazon Inspector is supported. For more information, see:
  - Amazon Inspector pricing – [Amazon Inspector pricing](https://aws.amazon.com/inspector/pricing/ "https://aws.amazon.com/inspector/pricing/").
  - Amazon Inspector supported Regions – [Regions and
    endpoints](../../../inspector/latest/user/inspector_regions.md "../../../inspector/latest/user/inspector_regions.md").

- Amazon ECR enhanced scanning shows how images are used on Amazon EKS and Amazon ECS. You
  can see when images were last used and identify how many clusters use each
  image. This information helps you prioritize vulnerability remediation for
  actively used images. You can quickly determine which clusters might be
  affected by newly discovered vulnerabilities. For more information about how
  to request these information and view the response, see [`DescribeImageScanFindings`](../APIReference/API_DescribeImageScanFindings.md "../APIReference/API_DescribeImageScanFindings.md").
- Amazon Inspector supports scanning for specific operating systems. For a full list,
  see [Supported
  operating systems - Amazon ECR scanning](../../../inspector/latest/user/supported.md#supported-os "../../../inspector/latest/user/supported.md#supported-os") in the _Amazon Inspector User
  Guide_.
- Amazon Inspector uses a service-linked IAM role, which provides the permissions
  needed to provide enhanced scanning for your repositories. The
  service-linked IAM role is created automatically by Amazon Inspector when enhanced
  scanning is turned on for your private registry. For more information, see [Using
  service-linked roles for Amazon Inspector](../../../inspector/latest/user/using-service-linked-roles.md "../../../inspector/latest/user/using-service-linked-roles.md") in the _Amazon Inspector User
  Guide_.
- When you initially turn on enhanced scanning for your private registry,
  Amazon Inspector only recognizes images pushed to Amazon ECR in the last 14 days, based on
  the image push timestamp. Older images will have the `SCAN_ELIGIBILITY_EXPIRED` scan status. If you'd like these images to
  be scanned by Amazon Inspector you should push them again to your repository.
- When enhanced scanning is turned on for your Amazon ECR private registry,
  repositories matching the scan filters are scanned using enhanced scanning
  only. Any repositories that don't match a filter will have an `Off`
  scan frequency and won't be scanned. Manual scans using enhanced scanning
  aren't supported. For more information, see [Filters to choose which repositories are scanned in Amazon ECR](image-scanning-filters.md "image-scanning-filters.md").
- If you specify separate filters for scan on push and continuous scanning
  where multiple filters match the same repository, then Amazon ECR enforces the
  continuous scanning filter over the scan on push filter for that
  repository.
- When enhanced scanning is turned on, Amazon ECR sends an event to EventBridge when the
  scan frequency for a repository is changed. Amazon Inspector emits events to EventBridge when
  an initial scan is completed and when an image scan finding is created,
  updated, or closed.

## Changing the enhanced scanning duration for images in Amazon Inspector

After enabling enhanced scanning, Amazon ECR continually scans newly pushed images for
the configured duration. By default, Amazon Inspector monitors your repositories until
images are deleted or enhanced scanning is disabled. You can configure both push
date duration (up to Lifetime) and re-scan duration in the Amazon Inspector console to suit
your environment's needs. When the scan duration for a repository elapses, the scan
status shows as `SCAN_ELIGIBILITY_EXPIRED`. For more information about
configuring re-scan duration settings for Amazon ECR in Amazon Inspector, see [Configuring
the Amazon ECR re-scan duration](../../../inspector/latest/user/enable-disable-scanning-ecr.md#scan-duration-setting "../../../inspector/latest/user/enable-disable-scanning-ecr.md#scan-duration-setting") in the _Amazon Inspector User Guide_.
