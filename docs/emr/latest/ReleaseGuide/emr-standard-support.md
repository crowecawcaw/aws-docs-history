# Amazon EMR standard support

## Understanding Amazon EMR releases

The _Amazon EMR release_ is the vehicle that delivers the necessary software to run your open-source applications on EC2, EKS, or Serverless platforms.
An Amazon EMR release is composed of three pieces: the _Runtime Environment_, _Core Engines_, and _Extras_.

- **Runtime environment** – The runtime environment includes the operating system that’s included as part of the Amazon Machine Image (AMI)
  or other container image when you launch your cluster or container (for example, Amazon Linux 2023). It also includes the language runtimes such as the Amazon Corretto JDK,
  along with other related tools that the image installs.
- **Core engines** – These include the core open-source software such as Apache Hive, and open table formats such as Apache Iceberg.
- **Extras** – These include convenience libraries and Python packages such as `mariadb-connector-java` and open-source software such as Apache Pig.

The Amazon EMR release version that you select bundles all these components into a new version of Amazon Linux (AL) based Amazon Machine Images (AMI) or container images.
Amazon EMR maintains the same AL version for all nodes of a cluster, EKS container, or serverless application. Amazon EMR aims to get the latest _Runtime Environment_ within 90 days
of their release by Amazon Linux, and new open-source versions of _Core Engines_ within 90 days from the upstream release. _Extras_ are released as needed. You can find the list of the
software in release notes for each Amazon EMR release.

## Release versioning

To help you understand the scope of changes in each release, Amazon EMR uses semantic versioning. Semantic versioning follows a format of `<major>.<minor>.<patch>`.
As an example, let’s consider the 7.0.0 release.

The first digit denotes the major version release, or **Major Release**. Major Releases typically bring substantial changes,
improvements, and new features to Runtime Environment or Core Engine that are not backward compatible. For example, the 7.x Major Release uses Amazon Linux 2023
with Amazon Corretto 17 JDK as default. As a result, the release contains several breaking changes compared to 6.x Major Release, which ships on Amazon Linux 2
and with Amazon Corretto 8 JDK as default.

The second digit denotes the minor version release, or **Minor Release**. Minor Releases are non-backward compatible releases that contain incremental changes, improvements,
and features to Core Engines and Extras, and new functionality. For example, 6.15 uses Apache Spark 3.4.1, compared to 6.11.1, which ships with Apache Spark 3.3.2.

The third digit denotes a patch version release, or **Patch Release**. Patch Releases are intended to be backward compatible releases that contain fixes and patch updates to _Core Engine_
and _Extras_, but no new functionality or OSS version upgrades. For example, 6.11.1 and 6.11.0 both contain the same Apache Spark 3.3.2 OSS version. As of 6.6.x, the latest
Patch Release offers the latest _Runtime Environment_ patch available. _Runtime Environment_ does not affect the Patch Release of Amazon EMR.
For example, 6.11.1 launched with AL version 2.0.20240109.0 from December 19, 2023 to January 10, 2024, but with AL version 2.0.20240124.0 from January 11, 2024. Some Amazon EMR on EKS
releases allow you to add tags or suffixes to the sematic versions to provide you with alternate functionalities. For example, the `emr-6.15.0-latest` release of Amazon EMR on EKS
launches an Amazon Corretto 8 JDK enabled release version, whereas the `emr-6.15.0-java17-latest` release of Amazon EMR on EKS allows you to launch an Amazon Corretto 17 JDK enabled release version.

## Support policy

**Introduction**

Amazon EMR aims to issue new Minor Releases at a minimum of once every 90 days, and to provide support for Minor Releases for a period of 24 months starting from the release date.
This support covers _Runtime Environment_ and _Core Engines_ with their associated dependencies, and doesn’t cover _Extras_ or their associated dependencies.
_Runtime Environment_ also includes proprietary platform components and APIs that are needed to start, stop, and operate the clusters and applications. This consistent release
schedule ensures a predictable cycle, making it more convenient for you to plan, test, and transition to a version that provides support and security.

**What to expect with Standard Support**

Standard Support provides fixes on technical support tickets for issues that you encounter for _Runtime Environment_ and _Core Engines_ components under
recommended configurations. All fixes are subject to availability. The recommended configuration is the use of Amazon EMR without any modification, additions, or changes to the binaries
and configurations present in an Amazon EMR release, except those found in the [Amazon EMR Documentation](../../../emr.md "../../../emr.md"). Amazon EMR deploys fixes to the latest patch, minor, or
major version of the Amazon EMR release within 90 days of us verifying the fix. Amazon EMR automatically applies fixes when you launch a new EMR on EC2 cluster, launch a new Amazon EMR on EKS container, or
trigger a new EMR Serverless job. Extra components are provided as a convenience and Amazon EMR does **not** provide fixes related to _Extras_.

**Components**

Standard Support covers _Runtime Environment_ and _Core Engines_ components – for example, operating system, language runtimes, and core open-source software
like Apache Hive and Apache Iceberg. You can find the full list of supported components for each release in [About Amazon EMR Releases](emr-release-components.md "emr-release-components.md") and
[Amazon Linux FAQs](https://aws.amazon.com/linux/amazon-linux-2023/faqs/ "https://aws.amazon.com/linux/amazon-linux-2023/faqs/").

The following list describes the support that we provide for different component types under Standard Support:

- **Runtime Environment components**: _Runtime Environment_ components will receive fixes on technical
  support tickets. Fixes are categorized as (a) critical bugs, (b) critical data corruption issues, and (c) critical security issues. When eligible, Amazon EMR will backport
  fixes for _Runtime Environment_ to older versions. For operational compatibility with the open-source Core Engine components, certain _Runtime Environment_ components
  must remain at specific versions to prevent breaking customer applications. For these components, Amazon EMR is dependent on upstream open-source for availability of fixes. When fixes are
  available in open source, we will provide the latest stable version within 90 days of them being verified by Amazon EMR.
- **Core Engines components**: _Core Engines_ provides the latest versions for many open-source projects, each having hundreds of transitive dependency libraries.
  While the open-source communities managing these projects attempt to address issues and known Common Vulnerabilities and Exposures (CVE) on a frequent basis, the latest versions might still
  contain known bugs and CVEs. Amazon EMR is dependent on upstream open-source for availability of fixes and will provide the latest stable version as part of the _Core Engine_ components within 90 days of them
  being verified by Amazon EMR. In certain cases, Amazon EMR might provide a fix for a CVE in one of the _Core Engine_ components that needs to be addressed ahead of upstream open source. Amazon EMR
  also provides you with technical support and fixes on features that are added on top of open source under recommended configurations. We don’t backport fixes for _Core Engine_
  components to older Patch or Minor versions.
- **Extras components**: Amazon EMR does **not** support _Extras_ components. Extra components are open-source projects
  provided as convenience and Amazon EMR does not provide fixes for issues encountered with them. Any support requests or fixes can be addressed through the open-source
  community supporting these components.

**Standard Support lifecycle**

The following describes the milestones in the Standard Support lifecycle:

- **Standard Support**: Amazon EMR releases are eligible for Standard Support 24 months from the date of release.
  You can create technical support tickets and expect updates for issues that you encounter with these releases.
- **End of Support**: After Standard Support ends,
  Amazon EMR releases enter End of Support (EoS) stage for 12 months. EoS releases are not eligible for technical support and
  you won't be able to create any tickets for clusters, containers, or jobs running on these releases. EoS releases won't receive any fixes, patches or updates. EoS
  releases will be removed from the console, but will continue to be available through the API and AWS CLI. You can always continue
  to run workloads on EoS releases. We strongly recommend that you migrate to the latest Amazon EMR release so that you continue to receive security patches, remain eligible for
  technical support, and can create support tickets when needed.
- **End of Life**: After the End of Support (EoS) term, releases are considered End of Life (EoL).
  Although you can continue to run EoL clusters, Amazon EMR reserves the right to remove EoL
  releases from the API and SDK on a case-by-case basis due to security and operational concerns. We strongly recommend that you migrate to the latest Amazon EMR,
  release because EoL versions can be removed from the API and SDK in exceptional cases.

**Bridge Support**

Amazon EMR announced this new support policy on July 25, 2024. Under this policy, versions of Amazon EMR released on or before July 24th, 2022 are now designated as End of Support.
However, to provide you with additional time to plan and migrate to newer versions, Amazon EMR will offer Bridge Support, equivalent to Standard Support, for these older versions that
released within the two-year period before this announcement.

After July 25, 2024, you can refer to the current status and support timelines in the release notes.

The following table shows the support status for all existing Amazon EMR releases at time of announcement of the policy, July 25, 2024:

| Releases and supported periods                                                                | Amazon EMR release version        | Initial release date                | Standard support end date | End of support start date | End of life start date |
| --------------------------------------------------------------------------------------------- | --------------------------------- | ----------------------------------- | ------------------------- | ------------------------- | ---------------------- |
| 7.2.0                                                                                         | July 25, 2024                     | July 24, 2026                       | July 25, 2026             | July 25, 2027             |
| 7.1.0                                                                                         | April 23, 2024                    | Bridge support until April 30, 2026 | May 1, 2026               | May 1, 2027               |
| 7.0.0                                                                                         | December 19, 2023                 | Bridge support until April 30, 2026 | May 1, 2026               | May 1, 2027               |
| 5.36.x and 6.6.x – 6.15.x                                                                     | May 9, 2022 to November 13, 2023  | Bridge support until April 30, 2026 | May 1, 2026               | May 1, 2027               |
| • 6.x series: 6.5.0 and lower<br>• 5.x series: 5.35.0 and lower<br>• 4.x, 3.x, and 2.x series | January 1, 2013 to March 30, 2022 | Bridge support until April 30, 2026 | May 1, 2026               | May 1, 2027               |

###### Note

Dates for bridge support have been extended to April 30, 2026, for all releases.

You can use Apache Spark Upgrade Agent to upgrade your Apache Spark existing applications on EMR on EC2 and EMR Serverless from older EMR versions to latest EMR version. To learn more, see [What is Apache Spark Upgrade Agent for Amazon EMR](spark-upgrades.md "spark-upgrades.md").

## Considerations

Standard Support is available for all Amazon EMR deployment models (EMR on EC2, Amazon EMR on EKS, and EMR Serverless), in all Regions where Amazon EMR is available, at no additional cost. Clusters
running with recommended configurations are automatically eligible for support as described in the policy, so you don’t need to take any additional actions to activate support.

- Standard Support only supports components required for Amazon EMR clusters. Amazon EMR can’t guarantee security patching and fix availability in the case when _Core Engine_
  open-source components reach EoL upstream, or when security updates are no longer available for dependencies. While you can opt-in to install _Extras_,
  Amazon EMR won't support them or their dependencies. For example, you can install third-party applications in your custom AMI to harden the security of your cluster, install additional
  components or copy objects using bootstrap action scripts, or SSH into your cluster and upgrade the default package versions. Amazon EMR does not support these components. Standard
  Support doesn’t cover customer provided bootstrap actions, packages, libraries, your custom code and bring-your-own custom applications that you can configure Amazon EMR to install for your convenience.
- Your existing clusters won't be impacted, regardless of which Amazon EMR release they're running. You can continue to run existing clusters without disruption.
  You can also continue to launch new clusters and run jobs on any of the existing releases and new releases. All existing releases and new releases at time of the policy
  becoming effective are covered by Standard Support for 24 months from initial date of release of the Amazon EMR release version. Amazon EMR will provide you with bridge support during the initial announcement
  of the policy. To receive uninterrupted support, we advise testing your applications and promptly upgrading to the most recent Amazon EMR release.
- Amazon EMR won't change Standard Support components on existing releases or clusters. However, Amazon EMR reserves the right to honor the upstream End of Life on a case-by-case basis, and remove such
  components in the new releases, or move the existing release to End of Support (EoS), or End of Life (EoL) status in exceptional cases. We'll notify you of any removal through available
  channels.
- When a new Region is launched, Amazon EMR will only support Amazon EMR release versions under Standard Support, released in six months prior to the date of of when new Region becomes generally available.
- Amazon EMR won't automatically update your existing clusters to latest versions. However, you can choose to update new clusters to the latest patch versions if desired.
- The cost of your unsupported Amazon EMR usage will count toward your AWS bill. Even if you are using Amazon EMR in an unsupported way, the costs associated with that usage are still part
  of your overall AWS consumption and will be included in the calculation of your support fees.

For more information, contact [AWS Developer Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").
