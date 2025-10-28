# Scan images for software vulnerabilities in Amazon ECR

Amazon ECR image scanning helps to identify software vulnerabilities in your container images.
The following scanning types are offered.

###### Important

Switching between the **Enhanced scanning**, **Basic
scanning**, and the **Improved basic scanning** versions
will cause previously established scans to no longer be available. You will have to set
up your scans again. However, if you switch back to your previous scanning version the
established scans will be available.

- **Enhanced scanning** – Amazon ECR integrates with Amazon Inspector to
  provide automated, continuous scanning of your repositories. Your container images
  are scanned for both operating systems and programming language package
  vulnerabilities. As new vulnerabilities appear, the scan results are updated and
  Amazon Inspector emits an event to EventBridge to notify you. Enhanced scanning provides the
  following:
  - OS and programming languages package vulnerabilities
  - Two scanning frequencies: Scan on push and continuous scan

- **Basic scanning** – Amazon ECR provides two versions of basic
  scanning which use the Common Vulnerabilities and Exposures (CVEs) database:.

      + **AWS native basic scanning** – Uses AWS
       native technology, which is now GA and recommended. All new customer registries are opted into this improved version by default.
      + **Clair basic scanning** – Uses the open source Clair project. Clair is now deprecated. See [Clair Deprecation](image-scanning-basic.md#clair-deprecation "image-scanning-basic.md#clair-deprecation") for details.

  With basic scanning, you configure your repositories to scan on push or you can perform manual scans and
  Amazon ECR provides a list of scan findings. Basic scanning provides the
  following:

      + OS scans
      + Two scanning frequencies: Manual and scan on push

###### Important

The new version of Amazon ECR Basic Scanning doesn't use the
`imageScanFindingsSummary` and `imageScanStatus`
attributes from the `DescribeImages` API response to return scan
results. Use the `DescribeImageScanFindings` API instead. For more
information, see [`DescribeImageScanFindings`](../APIReference/API_DescribeImageScanFindings.md "../APIReference/API_DescribeImageScanFindings.md").
