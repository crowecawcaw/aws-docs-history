# Amazon Inspector VM Scanner

## Overview

Amazon Inspector uses the Amazon Inspector VM Scanner to perform vulnerability assessments on Amazon EC2 instances.
Amazon Inspector VM Scanner leverages the inventory collection capabilities of [Amazon Inspector SBOM Generator](sbom-generator.md "sbom-generator.md") to generate a Software Bill of Materials (SBOM) and submits the SBOM for evaluation through the Inspector Telemetry channel.
When you enable Enhanced EC2 Scanning on your account, Inspector VM Scanner replaces [Inspector SSM Plugin](inspector-ssm-plugin.md "inspector-ssm-plugin.md").

###### Recommendation

We recommend the Amazon Inspector VM Scanner over the legacy Amazon Inspector SSM plugin.
The VM Scanner uses the same scan mechanism across all supported operating systems and produces more consistent findings, and it uses fewer compute resources.
On Windows in particular, it avoids the per‐query timeouts that can cause the Amazon Inspector SSM plugin to report findings inconsistently.

Amazon Inspector provides two approaches for deploying the VM Scanner:

- **Automatic installation (recommended)** – When you enable Enhanced EC2 Scanning in the Amazon Inspector console, Amazon Inspector uses Amazon EC2 Systems Manager (SSM) to automatically install and manage the VM Scanner on your Amazon EC2 instances. This is the simplest approach and requires no manual intervention. For more information, see [Enabling Inspector VM Scanner](inspector-vm-scanner-enabling.md "inspector-vm-scanner-enabling.md").
- **Manual installation** – You can manually install the VM Scanner using standard package managers (RPM, DEB, APK, MSI, PKG). This approach does not require SSM. For more information, see [Manual installation and configuration](inspector-vm-scanner-using.md "inspector-vm-scanner-using.md").

## Benefits

Inspector VM Scanner provides the following benefits over the previous Inspector SSM Plugin:

- **Reduced resource usage** – Requires less compute during operation
- **More granular package collection** – Provides detailed package-level inventory for high fidelity evaluation
- **Improved scanning mechanism** – Uses Inspector SBOM Generator for consistent behavior with other Inspector supported resources
- **Separation of duties** – Security teams can enable scanning at the account level, while instance administrators retain control over manual installation and configuration on individual instances

## Deep inspection

###### Enhanced scanning support

Enhanced scanning allows deep inspection paths on Windows, Linux, and macOS.

With Enhanced EC2 Scanning, the Amazon Inspector VM Scanner extends Amazon EC2 scanning coverage to include deep inspection.
With deep inspection, Amazon Inspector detects package vulnerabilities for application programming language packages in addition to operating system packages.
Amazon Inspector scans default locations for programming language package libraries, and you can configure custom paths in addition to the locations that Amazon Inspector scans by default.

###### Important

Amazon Inspector scans a default set of locations that varies by operating system.
Software in a non-standard location – such as a database or application server on a non-system drive like `D:\` – is scanned only if you add it as a custom path.
For more information, see [Custom paths for Amazon Inspector deep inspection](scanning-resources.md#deep-inspection-paths "scanning-resources.md#deep-inspection-paths").

For the programming languages that deep inspection supports, see [Supported programming languages: Amazon EC2 deep inspection](supported.md#supported-programming-languages-deep-inspection "supported.md#supported-programming-languages-deep-inspection").

## Frequently asked questions

Why should I migrate to Inspector VM Scanner? How is Inspector VM Scanner different from Inspector SSM Plugin?

Inspector VM Scanner uses Amazon Inspector SBOM Generator for system package scanning and deep inspection, providing a consistent scan mechanism regardless of how packages were installed.
This scan mechanism is also more performant, with the biggest performance gain being seen on Windows.
This mechanism is fully owned and maintained by Inspector, which allows Inspector to respond quickly to any issues that arise, as well as expand detections into new ecosystems.

How is Inspector VM Scanner different from Inspector SBOM Generator? Why not use SBOM Generator directly?

Inspector VM Scanner uses SBOM Generator under the hood for inventory collection, but it also contains extra features specifically designed for Inspector EC2 Scanning.
Inspector VM Scanner can communicate through the Inspector Telemetry channel, whereas Inspector SBOM Generator cannot.
Additionally, Inspector VM Scanner comes with orchestration to be invoked regularly for scheduled scanning.

How will Center for Internet Security (CIS) scans be managed? Will Inspector VM Scanner be used for CIS?

CIS scans will be kept in Inspector SSM Plugin. At this time, there is no intention to migrate CIS support to Inspector VM Scanner.

Does Inspector VM Scanner require SSM?

No. SSM is used for the automatic installation when you enable Enhanced EC2 Scanning in the console, but it is not a hard dependency. You can manually install the VM Scanner using standard package managers without SSM. For more information, see [Manual installation and configuration](inspector-vm-scanner-using.md "inspector-vm-scanner-using.md").

Does Inspector VM Scanner scan the same locations as Inspector SSM Plugin?

Not necessarily. Inspector VM Scanner scans a default set of locations that varies by operating system and can differ from Inspector SSM Plugin.
Software installed in a custom location is scanned only if you add it as a custom path.
With Enhanced EC2 Scanning, you can set custom paths for Linux, Windows, and macOS instances.
If you are activating or re-activating Amazon Inspector, review your custom paths before you rely on the results.
For more information, see [Custom paths for Amazon Inspector deep inspection](scanning-resources.md#deep-inspection-paths "scanning-resources.md#deep-inspection-paths").

## Third-party software attribution

Inspector VM Scanner includes third-party software components that are licensed under open source licenses.
In accordance with the terms of those licenses, the following attribution document lists the third-party components, their licenses, and the applicable license text.

```
https://inspector-vm-scanner.s3.amazonaws.com/latest/THIRD-PARTY-LICENSES.txt
```
