

# Amazon EMR standard support
<a name="emr-standard-support"></a>

## Understanding Amazon EMR releases
<a name="emr-standard-support-understanding"></a>

The *Amazon EMR release* is the vehicle that delivers the necessary software to run your open-source applications on EC2, EKS, or Serverless platforms. An Amazon EMR release is composed of three pieces: the *Runtime Environment*, *Core Engines*, and *Extras*.
+ **Runtime environment** – The runtime environment includes the operating system that's included as part of the Amazon Machine Image (AMI) or other container image when you launch your cluster or container (for example, Amazon Linux 2023). It also includes the language runtimes such as the Amazon Corretto JDK, along with other related tools that the image installs.
+ **Core engines** – These include the core open-source software such as Apache Hive, and open table formats such as Apache Iceberg.
+ **Extras** – These include convenience libraries and Python packages such as `mariadb-connector-java` and open-source software such as Apache Pig.

The Amazon EMR release version that you select bundles all these components into a new version of Amazon Linux (AL) based Amazon Machine Images (AMI) or container images. Amazon EMR maintains the same AL version for all nodes of a cluster, EKS container, or serverless application. Amazon EMR aims to get the latest *Runtime Environment* within 90 days of their release by Amazon Linux, and new open-source versions of *Core Engines* within 90 days from the upstream release. *Extras* are released as needed. You can find the list of the software in release notes for each Amazon EMR release.

## Release versioning
<a name="emr-standard-support-versioning"></a>

To help you understand the scope of changes in each release, Amazon EMR uses semantic versioning. Semantic versioning follows a format of `<major>.<minor>.<patch>`. As an example, let's consider the 7.0.0 release.

The first digit denotes the major version release, or **Major Release**. Major Releases typically bring substantial changes, improvements, and new features to Runtime Environment or Core Engine that are not backward compatible. For example, the 7.x Major Release uses Amazon Linux 2023 with Amazon Corretto 17 JDK as default. As a result, the release contains several breaking changes compared to 6.x Major Release, which ships on Amazon Linux 2 and with Amazon Corretto 8 JDK as default.

The second digit denotes the minor version release, or **Minor Release**. Minor Releases are non-backward compatible releases that contain incremental changes, improvements, and features to Core Engines and Extras, and new functionality. For example, 6.15 uses Apache Spark 3.4.1, compared to 6.11.1, which ships with Apache Spark 3.3.2.

The third digit denotes a patch version release, or **Patch Release**. Patch Releases are intended to be backward compatible releases that contain fixes and patch updates to *Core Engine* and *Extras*, but no new functionality or OSS version upgrades. For example, 6.11.1 and 6.11.0 both contain the same Apache Spark 3.3.2 OSS version. As of 6.6.x, the latest Patch Release offers the latest *Runtime Environment* patch available. *Runtime Environment* does not affect the Patch Release of Amazon EMR. For example, 6.11.1 launched with AL version 2.0.20240109.0 from December 19, 2023 to January 10, 2024, but with AL version 2.0.20240124.0 from January 11, 2024. Some Amazon EMR on EKS releases allow you to add tags or suffixes to the sematic versions to provide you with alternate functionalities. For example, the `emr-6.15.0-latest` release of Amazon EMR on EKS launches an Amazon Corretto 8 JDK enabled release version, whereas the `emr-6.15.0-java17-latest` release of Amazon EMR on EKS allows you to launch an Amazon Corretto 17 JDK enabled release version.

## Support policy
<a name="emr-stadard-support-policy"></a>

**Introduction**

Amazon EMR aims to issue new Minor Releases at a minimum of once every 90 days, and to provide support for Minor Releases for a period of 24 months starting from the release date. This support covers *Runtime Environment* and *Core Engines* with their associated dependencies, and doesn't cover *Extras* or their associated dependencies. *Runtime Environment* also includes proprietary platform components and APIs that are needed to start, stop, and operate the clusters and applications. This consistent release schedule ensures a predictable cycle, making it more convenient for you to plan, test, and transition to a version that provides support and security.

**What to expect with Standard Support**

Standard Support provides fixes on technical support tickets for issues that you encounter for *Runtime Environment* and *Core Engines* components under recommended configurations. All fixes are subject to availability. The recommended configuration is the use of Amazon EMR without any modification, additions, or changes to the binaries and configurations present in an Amazon EMR release, except those found in the [Amazon EMR Documentation](https://docs.aws.amazon.com/emr/). Amazon EMR deploys fixes to the latest patch, minor, or major version of the Amazon EMR release within 90 days of us verifying the fix. Amazon EMR automatically applies fixes when you launch a new EMR on EC2 cluster, launch a new Amazon EMR on EKS container, or trigger a new EMR Serverless job. Extra components are provided as a convenience and Amazon EMR does **not** provide fixes related to *Extras*.

**Components**

Standard Support covers *Runtime Environment* and *Core Engines* components – for example, operating system, language runtimes, and core open-source software like Apache Hive and Apache Iceberg. You can find the full list of supported components for each release in [About Amazon EMR Releases](emr-release-components.md) and [Amazon Linux FAQs](https://aws.amazon.com/linux/amazon-linux-2023/faqs/).

The following list describes the support that we provide for different component types under Standard Support:
+ **Runtime Environment components**: *Runtime Environment* components will receive fixes on technical support tickets. Fixes are categorized as (a) critical bugs, (b) critical data corruption issues, and (c) critical security issues. When eligible, Amazon EMR will backport fixes for *Runtime Environment* to older versions. For operational compatibility with the open-source Core Engine components, certain *Runtime Environment* components must remain at specific versions to prevent breaking customer applications. For these components, Amazon EMR is dependent on upstream open-source for availability of fixes. When fixes are available in open source, we will provide the latest stable version within 90 days of them being verified by Amazon EMR.
+ **Core Engines components**: *Core Engines* provides the latest versions for many open-source projects, each having hundreds of transitive dependency libraries. While the open-source communities managing these projects attempt to address issues and known Common Vulnerabilities and Exposures (CVE) on a frequent basis, the latest versions might still contain known bugs and CVEs. Amazon EMR is dependent on upstream open-source for availability of fixes and will provide the latest stable version as part of the *Core Engine* components within 90 days of them being verified by Amazon EMR. In certain cases, Amazon EMR might provide a fix for a CVE in one of the *Core Engine* components that needs to be addressed ahead of upstream open source. Amazon EMR also provides you with technical support and fixes on features that are added on top of open source under recommended configurations. We don't backport fixes for *Core Engine* components to older Patch or Minor versions.
+ **Extras components**: Amazon EMR does **not** support *Extras* components. Extra components are open-source projects provided as convenience and Amazon EMR does not provide fixes for issues encountered with them. Any support requests or fixes can be addressed through the open-source community supporting these components.

**Standard Support lifecycle**

The following describes the milestones in the Standard Support lifecycle:
+ **Standard Support**: Amazon EMR releases are eligible for Standard Support 24 months from the date of release. You can create technical support cases and expect updates for issues that you encounter with these releases. 
+ **End of Support**: After Standard Support ends, Amazon EMR releases enter End of Support (EoS) stage for 12 months. EoS releases are not eligible for technical support and you won't be able to create any support cases for clusters, containers, or jobs running on these releases. EoS releases won't receive any fixes, patches or updates. EoS releases will be removed from the console, but will continue to be available through the API and AWS CLI. You can always continue to run workloads on EoS releases. We strongly recommend that you migrate to the latest Amazon EMR release so that you continue to receive security patches, remain eligible for technical support, and can create support cases when needed. 
+ **End of Life**: After the End of Support (EoS) term, releases are considered End of Life (EoL). Although you can continue to run EoL clusters, Amazon EMR reserves the right to remove EoL releases from the API and SDK on a case-by-case basis due to security and operational concerns. We strongly recommend that you migrate to the latest Amazon EMR, release because EoL versions can be removed from the API and SDK in exceptional cases.

### Extended Support
<a name="emr-extended-support"></a>

AWS announced the Standard Support policy on July 25, 2024. Under this policy, versions of Amazon EMR released on or before July 24, 2022 were designated as End of Support. Amazon EMR offers Bridge Support, equivalent to Standard Support, for these releases through August 31, 2026.

Effective August 31, 2026, if you're actively migrating, AWS provides additional time to complete your migration to a supported release at no additional cost. This extension applies to the selected releases listed in the following table. To receive this extension, contact AWS Support and file a ticket with your migration plan and any help you need with the upgrade.

For Amazon EMR release versions 5.36 and 6.6 through 6.15, Amazon EMR extends support on a best-effort basis, limited to critical security fixes only, through June 30, 2027.

Amazon EMR release versions 5.35 and lower, and 6.5 and lower, do not receive Extended Support. These releases transition directly from Bridge Support to End of Support on September 1, 2026.

For Amazon EMR release versions 7.0 through 7.10, Amazon EMR extends Standard Support in full through the dates listed in the following table.


| Amazon EMR release version | Initial release date | Standard support end date | Extended support end date | End of support start date | End of life start date | 
| --- | --- | --- | --- | --- | --- | 
| 2.x | January 1, 2013 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 3.x | January 1, 2014 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 4.x | November 18, 2015 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.x | July 27, 2016 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.1 | November 3, 2016 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.2 | November 21, 2016 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.3 | January 26, 2017 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.4 | March 8, 2017 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.5 | April 26, 2017 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.6 | June 5, 2017 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.7 | July 13, 2017 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.8 | August 10, 2017 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.9 | October 5, 2017 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.10 | October 6, 2017 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.11 | January 22, 2018 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.12 | March 29, 2018 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.13 | May 29, 2018 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.14 | June 4, 2018 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.15 | June 21, 2018 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.16 | July 19, 2018 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.17 | August 30, 2018 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.18 | October 24, 2018 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.19 | November 7, 2018 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.20 | December 18, 2018 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.21 | February 18, 2019 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.22 | March 20, 2019 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.23 | April 1, 2019 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.24 | June 11, 2019 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.25 | July 17, 2019 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.26 | August 8, 2019 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.27 | September 23, 2019 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.28 | November 12, 2019 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.29 | January 17, 2020 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.30 | May 13, 2020 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.31 | October 9, 2020 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.32 | January 8, 2021 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.33 | April 19, 2021 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.34 | January 20, 2022 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.35 | March 30, 2022 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 5.36 | June 15, 2022 | Bridge support until August 31, 2026 | June 30, 2027 | June 30, 2027 | July 1, 2028 | 
| 6.0 | March 10, 2020 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 6.1 | September 4, 2020 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 6.2 | December 9, 2020 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 6.3 | May 12, 2021 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 6.4 | September 20, 2021 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 6.5 | January 20, 2022 | Bridge support until August 31, 2026 | N/A | September 1, 2026 | September 1, 2027 | 
| 6.6 | May 9, 2022 | Bridge support until August 31, 2026 | June 30, 2027 | June 30, 2027 | July 1, 2028 | 
| 6.7 | July 15, 2022 | Bridge support until August 31, 2026 | June 30, 2027 | June 30, 2027 | July 1, 2028 | 
| 6.8 | August 31, 2022 | Bridge support until August 31, 2026 | June 30, 2027 | June 30, 2027 | July 1, 2028 | 
| 6.9 | November 14, 2022 | Bridge support until August 31, 2026 | June 30, 2027 | June 30, 2027 | July 1, 2028 | 
| 6.10 | February 27, 2023 | Bridge support until August 31, 2026 | June 30, 2027 | June 30, 2027 | July 1, 2028 | 
| 6.11 | May 16, 2023 | Bridge support until August 31, 2026 | June 30, 2027 | June 30, 2027 | July 1, 2028 | 
| 6.12 | July 21, 2023 | Bridge support until August 31, 2026 | June 30, 2027 | June 30, 2027 | July 1, 2028 | 
| 6.13 | September 23, 2023 | Bridge support until August 31, 2026 | June 30, 2027 | June 30, 2027 | July 1, 2028 | 
| 6.14 | October 4, 2023 | Bridge support until August 31, 2026 | June 30, 2027 | June 30, 2027 | July 1, 2028 | 
| 6.15 | November 13, 2023 | Bridge support until August 31, 2026 | June 30, 2027 | June 30, 2027 | July 1, 2028 | 
| 7.0 | December 19, 2023 | Bridge support until August 31, 2026 | August 31, 2027 | August 31, 2027 | August 31, 2028 | 
| 7.1 | April 23, 2024 | Bridge support until August 31, 2026 | August 31, 2027 | August 31, 2027 | August 31, 2028 | 
| 7.2 | July 25, 2024 | Bridge support until August 31, 2026 | August 31, 2027 | August 31, 2027 | August 31, 2028 | 
| 7.3 | October 16, 2024 | October 16, 2026 | August 31, 2027 | August 31, 2027 | August 31, 2028 | 
| 7.4 | November 13, 2024 | November 13, 2026 | August 31, 2027 | August 31, 2027 | August 31, 2028 | 
| 7.5 | November 21, 2024 | November 21, 2026 | August 31, 2027 | August 31, 2027 | August 31, 2028 | 
| 7.6 | January 10, 2025 | January 10, 2027 | August 31, 2027 | August 31, 2027 | August 31, 2028 | 
| 7.7 | February 6, 2025 | February 6, 2027 | August 31, 2027 | August 31, 2027 | August 31, 2028 | 
| 7.8 | March 7, 2025 | March 7, 2027 | August 31, 2027 | August 31, 2027 | August 31, 2028 | 
| 7.9 | May 19, 2025 | May 19, 2027 | August 31, 2027 | August 31, 2027 | August 31, 2028 | 
| 7.10 | August 15, 2025 | August 15, 2027 | August 31, 2027 | August 31, 2027 | August 31, 2028 | 
| 7.11 | November 3, 2025 | November 3, 2027 | N/A | November 4, 2027 | November 4, 2028 | 
| 7.12 | November 21, 2025 | November 21, 2027 | N/A | November 22, 2027 | November 22, 2028 | 
| 7.13 | April 21, 2026 | April 20, 2028 | N/A | April 21, 2028 | April 21, 2029 | 
| emr-spark-8.0 | May 21, 2026 | May 20, 2028 | N/A | May 21, 2028 | May 21, 2029 | 

You can use Apache Spark Upgrade Agent to upgrade your Apache Spark existing applications on EMR on EC2 and EMR Serverless from older EMR versions to latest EMR version. To learn more, see [What is Apache Spark Upgrade Agent for Amazon EMR](spark-upgrades.md).

## Considerations
<a name="emr-standard-support-considerations"></a>

Standard Support is available for all Amazon EMR deployment models (EMR on EC2, Amazon EMR on EKS, and EMR Serverless), in all Regions where Amazon EMR is available, at no additional cost. Clusters running with recommended configurations are automatically eligible for support as described in the policy, so you don't need to take any additional actions to activate support.
+ Standard Support only supports components required for Amazon EMR clusters. Amazon EMR can't guarantee security patching and fix availability in the case when *Core Engine* open-source components reach EoL upstream, or when security updates are no longer available for dependencies. While you can opt-in to install *Extras*, Amazon EMR won't support them or their dependencies. For example, you can install third-party applications in your custom AMI to harden the security of your cluster, install additional components or copy objects using bootstrap action scripts, or SSH into your cluster and upgrade the default package versions. Amazon EMR does not support these components. Standard Support doesn't cover customer provided bootstrap actions, packages, libraries, your custom code and bring-your-own custom applications that you can configure Amazon EMR to install for your convenience.
+ Your existing clusters won't be impacted, regardless of which Amazon EMR release they're running. You can continue to run existing clusters without disruption. You can also continue to launch new clusters and run jobs on any of the existing releases and new releases. All existing releases and new releases at time of the policy becoming effective are covered by Standard Support for 24 months from initial date of release of the Amazon EMR release version. Amazon EMR will provide you with bridge support during the initial announcement of the policy. To receive uninterrupted support, we advise testing your applications and promptly upgrading to the most recent Amazon EMR release.
+ Amazon EMR won't change Standard Support components on existing releases or clusters. However, Amazon EMR reserves the right to honor the upstream End of Life on a case-by-case basis, and remove such components in the new releases, or move the existing release to End of Support (EoS), or End of Life (EoL) status in exceptional cases. We'll notify you of any removal through available channels.
+ When a new Region is launched, Amazon EMR will only support Amazon EMR release versions under Standard Support, released in six months prior to the date of when new Region becomes generally available.
+ Amazon EMR won't automatically update your existing clusters to latest versions. However, you can choose to update new clusters to the latest patch versions if desired.
+ The cost of your unsupported Amazon EMR usage will count toward your AWS bill. Even if you are using Amazon EMR in an unsupported way, the costs associated with that usage are still part of your overall AWS consumption and will be included in the calculation of your support fees.

For more information, contact [AWS Developer Support](https://aws.amazon.com/premiumsupport/).

## Support policy change history
<a name="emr-standard-support-change-history"></a>


| Date | Change | Description | 
| --- | --- | --- | 
| August 14, 2026 | Extended Support added | AWS added free Extended Support for releases 5.36 and 6.6 and later. Releases 5.36 and 6.6 through 6.15 receive best-effort critical security fixes; releases 7.0 through 7.10 receive full Standard Support. | 
| July 31, 2026 | Bridge support extended | Bridge support was extended to August 31, 2026 for all eligible releases. | 