# Scan images for OS vulnerabilities in

Amazon ECR

Amazon ECR provides two versions of basic scanning that use the Common Vulnerabilities and
Exposures (CVEs) database:

- **AWS native basic scanning** – Uses AWS native technology, which is now GA and recommended. This improved basic scanning is designed to provide customers with better scanning results and vulnerability detection across a broad set of popular operating systems. This allows customers to further strengthen the security of their container images. All new customer registries are opted into this improved version by default.
- **Clair basic scanning** – The previous basic scanning version, which uses the open source Clair project (see [Clair](https://github.com/quay/clair "https://github.com/quay/clair") on GitHub). Clair is now deprecated and will no longer be supported as of February 2, 2026.
  Both AWS native and Clair basic scanning are supported in all regions listed in [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/"), except that Clair is not supported for those that were added after September, 2024. See [Clair Deprecation](#clair-deprecation "#clair-deprecation") for more information.

Amazon ECR uses the severity for a CVE from the upstream distribution source if available.
Otherwise, the Common Vulnerability Scoring System (CVSS) score is used. The CVSS score
can be used to obtain the NVD vulnerability severity rating. For more information, see
[NVD Vulnerability Severity
Ratings](https://nvd.nist.gov/vuln-metrics/cvss "https://nvd.nist.gov/vuln-metrics/cvss").

Both versions of Amazon ECR basic scanning support filters to specify which repositories to
scan on push. Any repositories that don't match a scan on push filter are set to the
**manual** scan frequency which means you must manually start the
scan. An image can be scanned once per 24 hours. The 24 hours includes the initial scan
on push, if configured, and any manual scans. With basic scanning, you can scan up to
100,000 images per 24 hours in a given registry. The 100,000 limit includes both initial
scan on push and manual scans, across both Clair and improved version of basic scanning.

The last completed image scan findings can be retrieved for each image. When an image
scan is completed, Amazon ECR sends an event to Amazon EventBridge. For more information, see [Amazon ECR events and EventBridge](ecr-eventbridge.md "ecr-eventbridge.md").

## Clair Deprecation

Clair in Amazon ECR is deprecated. Clair will still be available for use until February 2, 2026. However, we strongly recommend that you transition your Clair use to AWS native basic scanning as soon as possible. Here is what you should know about Clair Deprecation:

- Clair will not be supported in new regions as they are added and will no longer be supported in any regions as of February 2, 2026.
- You will not be able to do any Clair scans starting February 2, 2026, and any scans you did before then will not be available after that date. You will have to trigger a new scan of your images to regenerate the scan findings after you switch to the new version.
- Before February 2, 2026 you can switch back and forth between Clair and native basic scanning.
- If you have Clair set up currently, you will automatically be switched to native basic scanning starting February 2, 2026 if you don't do so before.

AWS Native basic scanning offers the following additional features over Clair scanning:

- When native basic scanning scans resources, it sources more than 50 data feeds to generate findings for common vulnerabilities and exposures (CVEs). Examples of these sources include vendor security advisories, data feeds, and threat intelligence feeds, as well as the National Vulnerability Database (NVD) and MITRE.
- Native basic scanning updates vulnerability data from source feeds at least once daily.
- Scanning results and vulnerability detection are available across a broad set of popular operating systems (see below).

To switch to the improved basic scanning, see instruction at [Switching to the improved basic
scanning for images in Amazon ECR](image-scanning-improved-basic-enabling.md "image-scanning-improved-basic-enabling.md").

## Operating system

support for basic scanning and improved basic scanning

As a security best practice and for continued coverage, we recommend that you
continue to use supported versions of an operating system. In accordance with vendor
policy, discontinued operating systems are no longer updated with patches and, in
many cases, new security advisories are no longer released for them. In addition,
some vendors remove existing security advisories and detections from their feeds
when an affected operating system reaches the end of standard support. After a
distribution loses support from its vendor, Amazon ECR may no longer support scanning it
for vulnerabilities. Any findings that Amazon ECR does generate for a discontinued
operating system should be used for informational purposes only. Listed below are
the current supported operating systems and versions.

| Operating System                    | Version     | AWS native basic | Clair basic |
| ----------------------------------- | ----------- | ---------------- | ----------- |
| Alpine Linux (Alpine)               | 3.19        | Yes              | Yes         |
| Alpine Linux (Alpine)               | 3.20        | Yes              | Yes         |
| Alpine Linux (Alpine)               | 3.21        | Yes              | No          |
| Alpine Linux (Alpine)               | 3.22        | Yes              | No          |
| Alpine Linux (Alpine)               | 3.23        | Yes              | No          |
| AlmaLinux                           | 8           | Yes              | No          |
| AlmaLinux                           | 9           | Yes              | No          |
| AlmaLinux                           | 10          | Yes              | No          |
| Amazon Linux 2 (AL2)                | AL2         | Yes              | Yes         |
| Amazon Linux 2023(AL2023)           | AL2023      | Yes              | Yes         |
| Debian Server (Bullseye)            | 11          | Yes              | Yes         |
| Debian Server (Bookworm)            | 12          | Yes              | Yes         |
| Debian Server (Trixie)              | 13          | Yes              | No          |
| Fedora                              | 41          | Yes              | No          |
| OpenSUSE Leap                       | 15.6        | Yes              | No          |
| Oracle Linux (Oracle)               | 8           | Yes              | Yes         |
| Oracle Linux (Oracle)               | 9           | Yes              | Yes         |
| Photon OS                           | 4           | Yes              | No          |
| Photon OS                           | 5           | Yes              | No          |
| Red Hat Enterprise Linux (RHEL)     | 8           | Yes              | Yes         |
| Red Hat Enterprise Linux (RHEL)     | 9           | Yes              | Yes         |
| Red Hat Enterprise Linux (RHEL)     | 10          | Yes              | No          |
| Rocky Linux                         | 8           | Yes              | No          |
| Rocky Linux                         | 9           | Yes              | No          |
| SUSE Linux Enterprise Server (SLES) | 15.6        | Yes              | No          |
| Ubuntu (Xenial)                     | 16.04 (ESM) | Yes              | Yes         |
| Ubuntu (Bionic)                     | 18.04 (ESM) | Yes              | Yes         |
| Ubuntu (Focal)                      | 20.04 (LTS) | Yes              | Yes         |
| Ubuntu (Jammy)                      | 22.04 (LTS) | Yes              | Yes         |
| Ubuntu (Noble Numbat)               | 24.04       | Yes              | No          |
| Ubuntu (Oracular Oriole))           | 24.10       | Yes              | No          |
