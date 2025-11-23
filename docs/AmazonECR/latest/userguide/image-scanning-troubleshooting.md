# Troubleshooting image scanning in

Amazon ECR

The following are common image scan failures. You can view errors like this in the
Amazon ECR console by displaying the image details or through the API or AWS CLI by using the `DescribeImageScanFindings` API.

UnsupportedImageError

You may get an `UnsupportedImageError` error when attempting to
perform a basic scan on an image that was built using an operating system
that Amazon ECR doesn't support basic image scanning for. Amazon ECR supports package
vulnerability scanning for major versions of Amazon Linux, Amazon Linux 2, Debian, Ubuntu,
CentOS, Oracle Linux, Alpine, and RHEL Linux distributions. Once a
distribution loses support from its vendor, Amazon ECR may no longer support
scanning it for vulnerabilities. Amazon ECR does not support scanning images
built from the [Docker
scratch](https://hub.docker.com/_/scratch "https://hub.docker.com/_/scratch") image.

###### Important

When using enhanced scanning, Amazon Inspector supports scanning for specific
operating systems and media types. For a full list, see [Supported
operating systems and media types](../../../inspector/latest/user/enable-disable-scanning-ecr.md#ecr-supported-media "../../../inspector/latest/user/enable-disable-scanning-ecr.md#ecr-supported-media") in the _Amazon Inspector User
Guide_.

An `UNDEFINED` severity level is returned

You may receive a scan finding that has a severity level of `UNDEFINED`. The following are the common causes for this:

- The vulnerability was not assigned a priority by the CVE
  source.
- The vulnerability was assigned a priority that Amazon ECR did not
  recognize.

To determine the severity and description of a vulnerability, you can view
the CVE directly from the source.

## Understanding scan

status `SCAN_ELIGIBILITY_EXPIRED`

When enhanced scanning using Amazon Inspector is enabled for your private registry and
you are viewing your scan vulnerabilities, you may see a scan status of `SCAN_ELIGIBILITY_EXPIRED`. The following are the most common causes of this.

- When you initially turn on enhanced scanning for your private registry,
  Amazon Inspector only recognizes images pushed to Amazon ECR in the last 30 days, based on
  the image push timestamp. Older images will have the `SCAN_ELIGIBILITY_EXPIRED` scan status. If you'd like these images to
  be scanned by Amazon Inspector you should push them again to your repository.
- If the **ECR re-scan duration** is changed in the Amazon Inspector
  console and that time elapses, the scan status of the image is changed to `inactive` with a reason code of `expired`, and all
  associated findings for the image are scheduled to be closed. This results
  in the Amazon ECR console listing the scan status as `SCAN_ELIGIBILITY_EXPIRED`.
