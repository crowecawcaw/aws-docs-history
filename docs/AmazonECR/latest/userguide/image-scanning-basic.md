# Scan images for OS vulnerabilities in

Amazon ECR

Amazon ECR basic scanning uses AWS native technology to scan your container images for software vulnerabilities. Basic scanning provides vulnerability detection across a broad set of popular operating systems, sourcing more than 50 data feeds to generate findings for common vulnerabilities and exposures (CVEs). These sources include vendor security advisories, data feeds, threat intelligence feeds, as well as the National Vulnerability Database (NVD) and MITRE.

Amazon ECR basic scanning is supported in all regions listed in [AWS
Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/").

Amazon ECR uses the severity for a CVE from the upstream distribution source if available.
Otherwise, the Common Vulnerability Scoring System (CVSS) score is used. The CVSS score
can be used to obtain the NVD vulnerability severity rating. For more information, see [NVD Vulnerability Severity
Ratings](https://nvd.nist.gov/vuln-metrics/cvss "https://nvd.nist.gov/vuln-metrics/cvss").

Amazon ECR basic scanning supports filters to specify which repositories to
scan on push. Any repositories that don't match a scan on push filter are set to the **manual** scan frequency which means you must manually start the scan. An image
can be scanned once per 24 hours. The 24 hours includes the initial scan on push, if
configured, and any manual scans. With basic scanning, you can scan up to 100,000 images
per 24 hours in a given registry.

The last completed image scan findings can be retrieved for each image. When an image
scan is completed, Amazon ECR sends an event to Amazon EventBridge. For more information, see [Amazon ECR events and EventBridge](ecr-eventbridge.md "ecr-eventbridge.md").

## Operating system

support for basic scanning

As a security best practice and for continued coverage, we recommend that you
continue to use supported versions of an operating system. In accordance with vendor
policy, discontinued operating systems are no longer updated with patches and, in
many cases, new security advisories are no longer released for them. In addition,
some vendors remove existing security advisories and detections from their feeds
when an affected operating system reaches the end of standard support. After a
distribution loses support from its vendor, Amazon ECR may no longer support scanning it
for vulnerabilities. Any findings that Amazon ECR does generate for a discontinued
operating system should be used for informational purposes only. For a full list of
supported operating systems and versions, see [Supported operating systems - Amazon Inspector scan](../../../inspector/latest/user/supported.md#supported-os-scan-inspector-scan "../../../inspector/latest/user/supported.md#supported-os-scan-inspector-scan") in the _Amazon Inspector User
Guide_.
