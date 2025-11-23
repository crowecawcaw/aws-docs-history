# Supported operating systems and programming languages for Amazon Inspector

Amazon Inspector can scan software applications that are installed on the following:

- Amazon Elastic Compute Cloud (Amazon EC2) instances

###### Note

For Amazon EC2 instances, Amazon Inspector can scan for package vulnerabilities in operating systems that support agent-based scanning.
Amazon Inspector can also scan for package vulnerabilities in operating systems and programming languages that support hybrid scanning.
Amazon Inspector does not scan for toolchain vulnerabilities.
The version of the programming language compiler used to build the application introduces these vulnerabilities.

- Container images stored in Amazon Elastic Container Registry (Amazon ECR) repositories

###### Note

For ECR container images, Amazon Inspector can scan for operating system and programming language package vulnerabilities.
Amazon Inspector does not scan for toolchain vulnerabilities in Rust.
The version of the programming language compiler used to build the application introduces these vulnerabilities.

- AWS Lambda functions

###### Note

For Lambda functions, Amazon Inspector can scan for programming language package vulnerabilities and code vulnerabilities.
Amazon Inspector does not scan for toolchain vulnerabilities.
The version of the programming language compiler used to build the application introduces these vulnerabilities.

When Amazon Inspector scans resources, Amazon Inspector sources more than 50 data feeds to generate findings for common vulnerabilities and exposures (CVEs).
Examples of these sources include vendor security advisories, data feeds, and threat intelligence feeds, as well as the National Vulnerability Database (NVD) and MITRE.
Amazon Inspector updates vulnerability data from source feeds at least once daily.

For Amazon Inspector to scan a resource, the resource must be running a supported operating system or using a supported programming language.
The topics in this section list the operating systems, programming languages, and runtimes Amazon Inspector supports for different resources and scan types.
They also list discontinued operating systems.

###### Note

Amazon Inspector can provide only limited support for an operating system after a vendor discontinues support for the operating system.

###### Topics

- [Supported operating systems](#supported-os "#supported-os")
- [Discontinued operating systems](#formerly-supported-os "#formerly-supported-os")
- [Supported programming languages](#w2aac64c19 "#w2aac64c19")
- [Supported runtimes](#w2aac64c21 "#w2aac64c21")

## Supported operating systems

This section lists the operating systems Amazon Inspector supports.

### Supported operating systems: Amazon EC2 scanning

The following table lists the operating systems Amazon Inspector supports for the scanning of Amazon EC2 instances.
It specifies the vendor security advisory for each operating system and which operating systems support [agent-based scanning](scanning-ec2.md#agent-based "scanning-ec2.md#agent-based") and [agentless scanning](scanning-ec2.md#agentless "scanning-ec2.md#agentless").

When using the agent-based scanning method, you configure the SSM agent to perform continuous scans on all eligible instances.
Amazon Inspector recommends that you configure a version of the SSM agent that's greater than 3.2.2086.0.
For more information, see [Working with the SSM Agent](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md") in the _Amazon EC2 Systems Manager User Guide_.

Linux operating system detections are supported only for the default package manager repository (rpm and dpkg) and don't include third-party applications, extended support repositories (RHEL EUS, E4S, AUS, and TUS), and optional repositories (application streams).
Amazon Inspector scans the running kernel for vulnerabilities.
For some operating systems, like Ubuntu, a reboot is required for upgrades to show in active findings.

| Operating system                    | Version         | Vendor security advisories             | Agentless scan support | Agent-based scan support |
| ----------------------------------- | --------------- | -------------------------------------- | ---------------------- | ------------------------ |
| AlmaLinux                           | 8               | Errata CVE                             | Yes                    | Yes                      |
| AlmaLinux                           | 9               | Errata CVE                             | Yes                    | Yes                      |
| AlmaLinux                           | 10              | Errata CVE                             | Yes                    | Yes                      |
| Amazon Linux (AL2)                  | AL2             | ALAS Errata CVE                        | Yes                    | Yes                      |
| Amazon Linux 2023 (AL2023)          | AL2023          | ALAS Errata CVE                        | Yes                    | Yes                      |
| Bottlerocket                        | 1.7.0 and later | Errata CVE                             | No                     | Yes                      |
| Debian Server (Bullseye)            | 11              | DSA CVE                                | Yes                    | Yes                      |
| Debian Server (Bookworm)            | 12              | DSA CVE                                | Yes                    | Yes                      |
| Debian Server (Trixie)              | 13              | DSA CVE                                | Yes                    | Yes                      |
| Fedora                              | 40              | Errata CVE                             | Yes                    | Yes                      |
| Fedora                              | 41              | Errata CVE                             | Yes                    | Yes                      |
| Fedora                              | 42              | Errata CVE                             | Yes                    | Yes                      |
| OpenSUSE Leap                       | 15.6            | Errata CVE                             | Yes                    | Yes                      |
| Oracle Linux (Oracle)               | 8               | Errata CVE                             | Yes                    | Yes                      |
| Oracle Linux (Oracle)               | 9               | Errata CVE                             | Yes                    | Yes                      |
| Oracle Linux (Oracle)               | 10              | Errata CVE                             | Yes                    | Yes                      |
| Red Hat Enterprise Linux (RHEL)     | 8               | RHEL VEX CVE                           | Yes                    | Yes                      |
| Red Hat Enterprise Linux (RHEL)     | 9               | RHEL VEX CVE                           | Yes                    | Yes                      |
| Red Hat Enterprise Linux (RHEL)     | 10              | RHEL VEX CVE                           | Yes                    | Yes                      |
| Rocky Linux                         | 8               | Errata CVE                             | Yes                    | Yes                      |
| Rocky Linux                         | 9               | Errata CVE                             | Yes                    | Yes                      |
| Rocky Linux                         | 10              | Errata CVE                             | Yes                    | Yes                      |
| SUSE Linux Enterprise Server (SLES) | 15.6            | SUSE CVE                               | Yes                    | Yes                      |
| SUSE Linux Enterprise Server (SLES) | 15.7            | SUSE CVE                               | Yes                    | Yes                      |
| Ubuntu (Xenial)                     | 16.04           | USN, Ubuntu Pro (esm-infra & esm-apps) | Yes                    | Yes                      |
| Ubuntu (Bionic)                     | 18.04           | USN, Ubuntu Pro (esm-infra & esm-apps) | Yes                    | Yes                      |
| Ubuntu (Focal)                      | 20.04           | USN, Ubuntu Pro (esm-infra & esm-apps) | Yes                    | Yes                      |
| Ubuntu (Jammy)                      | 22.04           | USN, Ubuntu Pro (esm-infra & esm-apps) | Yes                    | Yes                      |
| Ubuntu (Noble Numbat)               | 24.04           | USN, Ubuntu Pro (esm-infra & esm-apps) | Yes                    | Yes                      |
| Ubuntu (Plucky Puffin)              | 25.04           | USN                                    | Yes                    | Yes                      |
| Windows Server                      | 2016            | MSKB                                   | No                     | Yes                      |
| Windows Server                      | 2019            | MSKB                                   | No                     | Yes                      |
| Windows Server                      | 2022            | MSKB                                   | No                     | Yes                      |
| Windows Server                      | 2025            | MSKB                                   | No                     | Yes                      |
| macOS (Mojave)                      | 10.14           | APPLE-SA                               | No                     | Yes                      |
| macOS (Catalina)                    | 10.15           | APPLE-SA                               | No                     | Yes                      |
| macOS (Big Sur)                     | 11              | APPLE-SA                               | No                     | Yes                      |
| macOS (Monterey)                    | 12              | APPLE-SA                               | No                     | Yes                      |
| macOS (Ventura)                     | 13              | APPLE-SA                               | No                     | Yes                      |
| macOS (Sonoma)                      | 14              | APPLE-SA                               | No                     | Yes                      |
| macOS (Sequoia)                     | 15              | APPLE-SA                               | No                     | Yes                      |

### Supported operating systems: Amazon ECR scanning with Amazon Inspector

The following table lists the operating systems Amazon Inspector supports for the scanning of container images in Amazon ECR repositories.
It also specifies the vendor security advisory for each operating system.

| Operating system                    | Version | Vendor security advisories             |
| ----------------------------------- | ------- | -------------------------------------- |
| AlmaLinux                           | 8       | Errata CVE                             |
| AlmaLinux                           | 9       | Errata CVE                             |
| AlmaLinux                           | 10      | Errata CVE                             |
| Alpine Linux (Alpine)               | 3.19    | Errata CVE                             |
| Alpine Linux (Alpine)               | 3.20    | Errata CVE                             |
| Alpine Linux (Alpine)               | 3.21    | Errata CVE                             |
| Alpine Linux (Alpine)               | 3.22    | Errata CVE                             |
| Alpine Linux (Alpine)               | 3.23    | Errata CVE                             |
| Amazon Linux (AL2)                  | AL2     | CVE                                    |
| Amazon Linux 2023 (AL2023)          | AL2023  | CVE                                    |
| BusyBox                             | –       | MITRE CVE                              |
| Chainguard                          | –       | Errata CVE                             |
| Debian Server (Bullseye)            | 11      | DSA CVE                                |
| Debian Server (Bookworm)            | 12      | DSA CVE                                |
| Debian Server (Trixie)              | 13      | DSA CVE                                |
| Fedora                              | 41      | Errata CVE                             |
| Fedora                              | 42      | Errata CVE                             |
| Minimus                             | –       | Errata CVE                             |
| OpenSUSE Leap                       | 15.6    | Errata CVE                             |
| Oracle Linux (Oracle)               | 8       | Errata CVE                             |
| Oracle Linux (Oracle)               | 9       | Errata CVE                             |
| Oracle Linux (Oracle)               | 10      | Errata CVE                             |
| Photon OS                           | 4       | Errata CVE                             |
| Photon OS                           | 5       | Errata CVE                             |
| Red Hat Enterprise Linux (RHEL)     | 8       | RHEL VEX CVE                           |
| Red Hat Enterprise Linux (RHEL)     | 9       | RHEL VEX CVE                           |
| Red Hat Enterprise Linux (RHEL)     | 10      | RHEL VEX CVE                           |
| Rocky Linux                         | 8       | Errata CVE                             |
| Rocky Linux                         | 9       | Errata CVE                             |
| Rocky Linux                         | 10      | Errata CVE                             |
| SUSE Linux Enterprise Server (SLES) | 15.6    | SUSE CVE                               |
| SUSE Linux Enterprise Server (SLES) | 15.7    | SUSE CVE                               |
| Ubuntu (Xenial)                     | 16.04   | USN, Ubuntu Pro (esm-infra & esm-apps) |
| Ubuntu (Bionic)                     | 18.04   | USN, Ubuntu Pro (esm-infra & esm-apps) |
| Ubuntu (Focal)                      | 20.04   | USN, Ubuntu Pro (esm-infra & esm-apps) |
| Ubuntu (Jammy)                      | 22.04   | USN, Ubuntu Pro (esm-infra & esm-apps) |
| Ubuntu (Noble Numbat)               | 24.04   | USN, Ubuntu Pro (esm-infra & esm-apps) |
| Ubuntu (Plucky Puffin)              | 25.04   | USN                                    |
| Wolfi                               | –       | Errata CVE                             |

### Supported operating systems: CIS scanning

The following table lists the operating systems Amazon Inspector supports for CIS scans.
It also specifies the CIS benchmark version for each operating system.

###### Note

CIS standards are intended for x86_64 operating systems.
Some checks may not be evaluated or return invalid remediation instructions on ARM-based resources.

| Operating system                | Version | CIS benchmark version |
| ------------------------------- | ------- | --------------------- |
| Amazon Linux 2                  | AL2     | 3.0.0                 |
| Amazon Linux 2023               | AL2023  | 1.0.0                 |
| Red Hat Enterprise Linux (RHEL) | 8       | 3.0.0                 |
| Red Hat Enterprise Linux (RHEL) | 9       | 2.0.0                 |
| Rocky Linux                     | 8       | 2.0.0                 |
| Rocky Linux                     | 9       | 1.0.0                 |
| SUSE Linux Enterprise Server    | 15      | 2.0.1                 |
| Ubuntu (Bionic)                 | 18.04   | 2.2.0                 |
| Ubuntu (Focal)                  | 20.04   | 3.0.0                 |
| Ubuntu (Jammy)                  | 22.04   | 2.0.0                 |
| Ubuntu (Noble Numbat)           | 24.04   | 1.0.0                 |
| Windows Server                  | 2016    | 3.0.0                 |
| Windows Server                  | 2019    | 4.0.0                 |
| Windows Server                  | 2022    | 4.0.0                 |

### Supported operating systems: Amazon Inspector Scans

The following table lists the supported operating systems for the Amazon Inspector Scan API.
For more information, see [ScanSbom](../../v2/APIReference/API_scan_ScanSbom.md "../../v2/APIReference/API_scan_ScanSbom.md") in the _Amazon Inspector V2 API Reference_.

| Operating system         | Version |
| ------------------------ | ------- |
| AlmaLinux 8              | 8       |
| AlmaLinux                | 9       |
| AlmaLinux                | 10      |
| Alpine Linux             | 3.19    |
| Alpine Linux             | 3.20    |
| Alpine Linux             | 3.21    |
| Alpine Linux             | 3.22    |
| Alpine Linux             | 3.23    |
| Amazon Linux             | 2       |
| Amazon Linux             | 2023    |
| Bottlerocket             | –       |
| BusyBox                  | 1.36.0+ |
| Chainguard               | –       |
| Debian                   | 11      |
| Debian                   | 12      |
| Debian                   | 13      |
| Debian Sid               | –       |
| Fedora                   | 41      |
| Fedora                   | 42      |
| macOS                    | 11+     |
| MinimOS                  | –       |
| OpenSUSE                 | 15.6    |
| Oracle Linux             | 8       |
| Oracle Linux             | 9       |
| Oracle Linux             | 10      |
| Photon OS                | 4       |
| Photon OS                | 5       |
| Red Hat Enterprise Linux | 8       |
| Red Hat Enterprise Linux | 9       |
| Red Hat Enterprise Linux | 10      |
| Rocky Linux              | 8       |
| Rocky Linux              | 9       |
| Rocky Linux              | 10      |
| SUSE Server              | 15.6    |
| SUSE Server              | 15.7    |
| Ubuntu                   | 16.04   |
| Ubuntu                   | 18.04   |
| Ubuntu                   | 20.04   |
| Ubuntu                   | 22.04   |
| Ubuntu                   | 24.04   |
| Ubuntu                   | 25.04   |
| Wolfi Linux              | –       |

## Discontinued operating systems

The following tables list which operating systems have been discontinued and when they were discontinued.

Even though Amazon Inspector doesn't provide full support for the following discontinued operating systems, Amazon Inspector continues to scan the Amazon EC2 instances and Amazon ECR container images running them.
As a security best practice, we recommend moving to the supported version of a discontinued operating system.
Findings that Amazon Inspector generates for a discontinued operating system should be used for informational purposes only.

In accordance with vendor policy, the following operating systems no longer receive patch updates.
New security advisories might not be released for discontinued operating systems.
Vendors can remove existing security advisories and detections from their feeds for operating systems that reach the end of standard support.
As a result, Amazon Inspector can stop generating findings for known CVEs.

**Discontinued operating systems: Amazon EC2 scanning**

| Operating system                    | Version | Discontinued      |
| ----------------------------------- | ------- | ----------------- |
| Amazon Linux (AL1)                  | 2012    | December 31, 2021 |
| CentOS Linux (CentOS)               | 7       | June 30, 2024     |
| CentOS Linux (CentOS)               | 8       | December 31, 2021 |
| Debian Server (Jessie)              | 8       | June 30, 2020     |
| Debian Server (Stretch)             | 9       | June 30, 2022     |
| Debian Server (Buster)              | 10      | June 30, 2024     |
| Fedora                              | 33      | November 30, 2021 |
| Fedora                              | 34      | June 7, 2022      |
| Fedora                              | 35      | December 13, 2022 |
| Fedora                              | 36      | May 16, 2023      |
| Fedora                              | 37      | December 15, 2023 |
| Fedora                              | 38      | May 21, 2024      |
| Fedora                              | 39      | November 26, 2024 |
| Fedora                              | 40      | May 13, 2025      |
| OpenSUSE Leap                       | 15.2    | December 1, 2021  |
| OpenSUSE Leap                       | 15.3    | December 1, 2022  |
| OpenSUSE Leap                       | 15.4    | December 7, 2023  |
| OpenSUSE Leap                       | 15.5    | December 31, 2024 |
| Oracle Linux (Oracle)               | 6       | March 1, 2021     |
| Oracle Linux (Oracle)               | 7       | December 31, 2024 |
| Red Hat Enterprise Linux (RHEL)     | 6       | November 30, 2020 |
| Red Hat Enterprise Linux (RHEL)     | 7       | June 30, 2024     |
| SUSE Linux Enterprise Server (SLES) | 12      | June 30, 2016     |
| SUSE Linux Enterprise Server (SLES) | 12.1    | May 31, 2017      |
| SUSE Linux Enterprise Server (SLES) | 12.2    | March 31, 2018    |
| SUSE Linux Enterprise Server (SLES) | 12.3    | June 30, 2019     |
| SUSE Linux Enterprise Server (SLES) | 12.4    | June 30, 2020     |
| SUSE Linux Enterprise Server (SLES) | 12.5    | October 31, 2024  |
| SUSE Linux Enterprise Server (SLES) | 15      | December 31, 2019 |
| SUSE Linux Enterprise Server (SLES) | 15.1    | January 31, 2021  |
| SUSE Linux Enterprise Server (SLES) | 15.2    | December 31, 2021 |
| SUSE Linux Enterprise Server (SLES) | 15.3    | December 31, 2022 |
| SUSE Linux Enterprise Server (SLES) | 15.4    | December 31, 2023 |
| SUSE Linux Enterprise Server (SLES) | 15.5    | December 31, 2024 |
| Ubuntu (Trusty)                     | 12.04   | April 28, 2017    |
| Ubuntu (Trusty)                     | 14.04   | April 1, 2024     |
| Ubuntu (Groovy)                     | 20.10   | July 22, 2021     |
| Ubuntu (Hirsute)                    | 21.04   | January 20, 2022  |
| Ubuntu (Impish)                     | 21.10   | July 31, 2022     |
| Ubuntu (Kinetic)                    | 22.10   | July 20, 2023     |
| Ubuntu (Lunar Lobster)              | 23.04   | January 25, 2024  |
| Ubuntu (Mantic Minotaur)            | 23.10   | July 11, 2024     |
| Ubuntu (Oracular Oriole)            | 24.10   | July 10, 2025     |
| Windows Server                      | 2012    | October 10, 2023  |
| Windows Server                      | 2012 R2 | October 10, 2023  |

**Discontinued operating systems: Amazon ECR scanning**

| Operating system                    | Version | Discontinued      |
| ----------------------------------- | ------- | ----------------- |
| Alpine Linux (Alpine)               | 3.2     | May 1, 2017       |
| Alpine Linux (Alpine)               | 3.3     | November 1, 2017  |
| Alpine Linux (Alpine)               | 3.4     | May 1, 2018       |
| Alpine Linux (Alpine)               | 3.5     | November 1, 2018  |
| Alpine Linux (Alpine)               | 3.6     | May 1, 2019       |
| Alpine Linux (Alpine)               | 3.7     | November 1, 2019  |
| Alpine Linux (Alpine)               | 3.8     | May 1, 2020       |
| Alpine Linux (Alpine)               | 3.9     | November 1, 2020  |
| Alpine Linux (Alpine)               | 3.10    | May 1, 2021       |
| Alpine Linux (Alpine)               | 3.11    | November 1, 2021  |
| Alpine Linux (Alpine)               | 3.12    | May 1, 2022       |
| Alpine Linux (Alpine)               | 3.13    | November 1, 2022  |
| Alpine Linux (Alpine)               | 3.14    | May 1, 2023       |
| Alpine Linux (Alpine)               | 3.15    | November 1, 2023  |
| Alpine Linux (Alpine)               | 3.16    | May 23, 2024      |
| Alpine Linux (Alpine)               | 3.17    | November 22, 2024 |
| Alpine Linux (Alpine)               | 3.18    | May 09 2025       |
| Amazon Linux (AL1)                  | 2012    | December 31, 2021 |
| CentOS Linux (CentOS)               | 7       | June 30, 2024     |
| CentOS Linux (CentOS)               | 8       | December 31, 2021 |
| Debian Server (Jessie)              | 8       | June 30, 2020     |
| Debian Server (Stretch)             | 9       | June 30, 2022     |
| Debian Server (Buster)              | 10      | June 30, 2024     |
| Fedora                              | 33      | November 30, 2021 |
| Fedora                              | 34      | June 7, 2022      |
| Fedora                              | 35      | December 13, 2022 |
| Fedora                              | 36      | May 16, 2023      |
| Fedora                              | 37      | December 15, 2023 |
| Fedora                              | 38      | May 21, 2024      |
| Fedora                              | 39      | November 26, 2024 |
| Fedora                              | 40      | May 13, 2025      |
| OpenSUSE Leap                       | 15.2    | December 1, 2021  |
| OpenSUSE Leap                       | 15.3    | December 1, 2022  |
| OpenSUSE Leap                       | 15.4    | December 7, 2023  |
| OpenSUSE Leap                       | 15.5    | December 31, 2024 |
| Oracle Linux (Oracle)               | 6       | March 1, 2021     |
| Oracle Linux (Oracle)               | 7       | December 31, 2024 |
| Photon OS                           | 2       | December 2, 2021  |
| Photon OS                           | 3       | March 1, 2024     |
| Red Hat Enterprise Linux (RHEL)     | 6       | June 30, 2020     |
| Red Hat Enterprise Linux (RHEL)     | 7       | June 30, 2024     |
| SUSE Linux Enterprise Server (SLES) | 12      | June 30, 2016     |
| SUSE Linux Enterprise Server (SLES) | 12.1    | May 31, 2017      |
| SUSE Linux Enterprise Server (SLES) | 12.2    | March 31, 2018    |
| SUSE Linux Enterprise Server (SLES) | 12.3    | June 30, 2019     |
| SUSE Linux Enterprise Server (SLES) | 12.4    | June 30, 2020     |
| SUSE Linux Enterprise Server (SLES) | 12.5    | October 31, 2024  |
| SUSE Linux Enterprise Server (SLES) | 15      | December 31, 2019 |
| SUSE Linux Enterprise Server (SLES) | 15.1    | January 31, 2021  |
| SUSE Linux Enterprise Server (SLES) | 15.2    | December 31, 2021 |
| SUSE Linux Enterprise Server (SLES) | 15.3    | December 31, 2022 |
| SUSE Linux Enterprise Server (SLES) | 15.4    | December 31, 2023 |
| SUSE Linux Enterprise Server (SLES) | 15.5    | December 31, 2024 |
| Ubuntu (Trusty)                     | 12.04   | April 28, 2017    |
| Ubuntu (Trusty)                     | 14.04   | April 1, 2024     |
| Ubuntu (Groovy)                     | 20.10   | July 22, 2021     |
| Ubuntu (Hirsute)                    | 21.04   | January 20, 2022  |
| Ubuntu (Impish)                     | 21.10   | July 31, 2022     |
| Ubuntu (Kinetic)                    | 22.10   | July 20, 2023     |
| Ubuntu (Lunar Lobster)              | 23.04   | January 25, 2024  |
| Ubuntu (Mantic Minotaur)            | 23.10   | July 11, 2024     |
| Ubuntu (Oracular Oriole)            | 24.10   | July 10, 2025     |

##

Supported programming languages

This section lists the programming languages Amazon Inspector supports.

### Supported programming languages: Amazon EC2 agentless scanning

Amazon Inspector currently supports the following programming languages when performing agentless scans on eligible Amazon EC2 instances.
For more information, see [agentless scanning](scanning-ec2.md#agentless "scanning-ec2.md#agentless").

###### Note

Amazon Inspector doesn't scan for toolchain vulnerabilities in Go and Rust.
The version of the programming language compiler used to build the application introduces these vulnerabilities.

- C#
- Go
- Java
- JavaScript
- PHP
- Python
- Ruby
- Rust

### Supported programming languages: Amazon EC2 deep inspection

Amazon Inspector currently supports the following programming languages when performing deep inspection scans on Amazon EC2 Linux instances.
For more information, see [Amazon Inspector deep inspection for Linux-based Amazon EC2 instances](scanning-ec2.md#agentles "scanning-ec2.md#agentles").

- Java (.ear, .jar, .par, and .war archive formats)
- JavaScript
- Python

Amazon Inspector uses Systems Manager Distributor to deploy the plugin for deep inspection of your Amazon EC2 instance.

###### Note

Deep inspection is not supported for Bottlerocket operating systems.

To perform deep inspection scans, Systems Manager Distributor and Amazon Inspector must support your Amazon EC2 instance operating system.
For information about supported operating systems in Systems Manager Distributor, see [Supported package platforms and architectures](../../../systems-manager/latest/userguide/distributor.md#what-is-a-package-platforms "../../../systems-manager/latest/userguide/distributor.md#what-is-a-package-platforms") in the _Systems Manager User Guide_.

### Supported programming languages: Amazon ECR scanning

Amazon Inspector currently supports the following programming languages when scanning container images in Amazon ECR repositories:

###### Note

Amazon Inspector doesn't scan for toolchain vulnerabilities in Rust.
The version of the programming language compiler used to build the application introduces these vulnerabilities.
For Python applications using [Chainguard Libraries](https://www.chainguard.dev/libraries "https://www.chainguard.dev/libraries"), Amazon Inspector recognizes back-ported security fixes and excludes them from findings.

- C#
- Go
- Go toolchain
- Java
- Java JDK
- JavaScript
- PHP
- Python (including Chainguard Libraries)
- Ruby
- Rust

## Supported runtimes

This section lists the runtimes Amazon Inspector supports.

### Supported runtimes: Amazon Inspector Lambda standard scanning

Amazon Inspector Lambda standard scanning currently supports the following runtimes for the programming languages it can use when scanning Lambda functions for vulnerabilities in third-party software packages:

###### Note

Amazon Inspector doesn't scan for toolchain vulnerabilities in Rust.
The version of the programming language compiler used to build the application introduces these vulnerabilities.

- Go
  - go1.x

- Java
  - java8
  - java8.al2
  - java11
  - java17
  - java21

- .NET
  - .NET 6
  - .NET 8

- Node.js
  - nodejs12.x
  - nodejs14.x
  - nodejs16.x
  - nodejs18.x
  - nodejs20.x
  - nodejs22.x

- Python
  - python3.7
  - python3.8
  - python3.9
  - python3.10
  - python3.11
  - python3.12
  - python3.13

- Ruby
  - ruby2.7
  - ruby3.2
  - ruby3.3

- Custom runtimes
  - AL2
  - AL2023

### Supported runtimes: Amazon Inspector Lambda code scanning

Amazon Inspector Lambda code scanning currently supports the following runtimes for the programming languages it can use when scanning Lambda functions for vulnerabilities in code:

- Java
  - java8
  - java8.al2
  - java11
  - java17

- .NET
  - .NET 6
  - .NET 8

- Node.js
  - nodejs12.x
  - nodejs14.x
  - nodejs16.x
  - nodejs18.x
  - nodejs20.x

- Python
  - python3.7
  - python3.8
  - python3.9
  - python3.10
  - python3.11
  - python3.12

- Ruby
  - ruby2.7
  - ruby3.2
  - ruby3.3
