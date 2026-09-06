

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# How patch baseline rules work on Linux-based systems
<a name="patch-manager-linux-rules"></a>

The rules in a patch baseline for Linux distributions operate differently based on the distribution type. Unlike patch updates on Windows Server managed nodes, rules are evaluated on each node to take the configured repos on the instance into consideration. Patch Manager uses the native package manager to drive the installation of patches approved by the patch baseline.

For Linux-based operating system types that report a severity level for patches, Patch Manager uses the severity level reported by the software publisher for the update notice or individual patch. Patch Manager doesn't derive severity levels from third-party sources, such as the [Common Vulnerability Scoring System](https://www.first.org/cvss/) (CVSS), or from metrics released by the [National Vulnerability Database](https://nvd.nist.gov/vuln) (NVD).

## How patch baseline rules work on Amazon Linux 2 and Amazon Linux 2023
<a name="linux-rules-amazon-linux"></a>

**Note**  
Amazon Linux 2023 (AL2023) uses versioned repositories that can be locked to a specific version through one or more system settings. For all patching operations on AL2023 EC2 instances, Patch Manager uses the latest repository versions, independent of the system configuration. For more information, see [Deterministic upgrades through versioned repositories](https://docs.aws.amazon.com/linux/al2023/ug/deterministic-upgrades.html) in the *Amazon Linux 2023 User Guide*.

On Amazon Linux 2 and Amazon Linux 2023, the patch selection process is as follows:

1. On the managed node, the YUM library (Amazon Linux 2) or the DNF library (Amazon Linux 2023) accesses the `updateinfo.xml` file for each configured repo. 

   If no `updateinfo.xml` file is found, whether patches are installed depend on settings for **Include non-security updates** and **Auto-approval**. For example, if non-security updates are permitted, they're installed when the auto-approval time arrives.

1. Each update notice in `updateinfo.xml` includes several attributes that denote the properties of the packages in the notice, as described in the following table.  
**Update notice attributes**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-linux-rules.html)

   For information about accepted formats for lists of approved patches and rejected patches, see [Package name formats for approved and rejected patch lists](patch-manager-approved-rejected-package-name-formats.md).

1. The product of the managed node is determined by SSM Agent. This attribute corresponds to the value of the Product key attribute in the patch baseline's [PatchFilter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html) data type.

1. Packages are selected for the update according to the following guidelines.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-linux-rules.html)

For information about patch compliance status values, see [Patch compliance state values](patch-manager-compliance-states.md).

## How patch baseline rules work on CentOS Stream
<a name="linux-rules-centos"></a>

The CentOS Stream default repositories do not include an `updateinfo.xml` file. However, custom repositories that you create or use might include this file. In this topic, references to `updateinfo.xml` apply only to these custom repositories.

On CentOS Stream, the patch selection process is as follows:

1. On the managed node, the DNF library accesses the `updateinfo.xml` file, if it exists in a custom repository, for each configured repo.

   If there is no `updateinfo.xml` found, which always includes the default repos, whether patches are installed depends on settings for **Include non-security updates** and **Auto-approval**. For example, if non-security updates are permitted, they're installed when the auto-approval time arrives.

1. If `updateinfo.xml` is present, each update notice in the file includes several attributes that denote the properties of the packages in the notice, as described in the following table.  
**Update notice attributes**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-linux-rules.html)

   For information about accepted formats for lists of approved patches and rejected patches, see [Package name formats for approved and rejected patch lists](patch-manager-approved-rejected-package-name-formats.md).

1. In all cases, the product of the managed node is determined by SSM Agent. This attribute corresponds to the value of the Product key attribute in the patch baseline's [PatchFilter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html) data type.

1. Packages are selected for the update according to the following guidelines.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-linux-rules.html)

For information about patch compliance status values, see [Patch compliance state values](patch-manager-compliance-states.md).

## How patch baseline rules work on Debian Server
<a name="linux-rules-debian"></a>

On Debian Server , the patch baseline service offers filtering on the *Priority* and *Section *fields. These fields are typically present for all Debian Server packages. To determine whether a patch is selected by the patch baseline, Patch Manager does the following:

1. On Debian Server systems, the equivalent of `sudo apt-get update` is run to refresh the list of available packages. Repos aren't configured and the data is pulled from repos configured in a `sources` list.

1. If an update is available for `python3-apt` (a Python library interface to `libapt`), it is upgraded to the latest version. (This nonsecurity package is upgraded even if you did not select the **Include nonsecurity updates** option.)

1. Next, the [GlobalFilters](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreatePatchBaseline.html#systemsmanager-CreatePatchBaseline-request-GlobalFilters), [ApprovalRules](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreatePatchBaseline.html#EC2-CreatePatchBaseline-request-ApprovalRules), [ApprovedPatches](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreatePatchBaseline.html#EC2-CreatePatchBaseline-request-ApprovedPatches) and [RejectedPatches](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreatePatchBaseline.html#EC2-CreatePatchBaseline-request-RejectedPatches) lists are applied.
**Note**  
Because it isn't possible to reliably determine the release dates of update packages for Debian Server, the auto-approval options aren't supported for this operating system.

   Approval rules, however, are also subject to whether the **Include nonsecurity updates** check box was selected when creating or last updating a patch baseline.

   If nonsecurity updates are excluded, an implicit rule is applied in order to select only packages with upgrades in security repos. For each package, the candidate version of the package (which is typically the latest version) must be part of a security repo. In this case, for Debian Server, patch candidate versions are limited to patches included in the following repos:

   These repos are named as follows:
   + Debian Server 11: `debian-security bullseye`
   + Debian Server 12: `debian-security bookworm`

   If nonsecurity updates are included, patches from other repositories are considered as well.

   For information about accepted formats for lists of approved patches and rejected patches, see [Package name formats for approved and rejected patch lists](patch-manager-approved-rejected-package-name-formats.md).

To view the contents of the *Priority* and *Section *fields, run the following `aptitude` command: 

**Note**  
You might need to first install Aptitude on Debian Server systems.

```
aptitude search -F '%p %P %s %t %V#' '~U'
```

In the response to this command, all upgradable packages are reported in this format: 

```
name, priority, section, archive, candidate version
```

For information about patch compliance status values, see [Patch compliance state values](patch-manager-compliance-states.md).

## How patch baseline rules work on macOS
<a name="linux-rules-macos"></a>

On macOS, the patch selection process is as follows:

1. On the managed node, Patch Manager accesses the parsed contents of the `InstallHistory.plist` file and identifies package names and versions. 

   For details about the parsing process, see the **macOS** tab in [How patches are installed](patch-manager-installing-patches.md).

1. The product of the managed node is determined by SSM Agent. This attribute corresponds to the value of the Product key attribute in the patch baseline's [PatchFilter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html) data type.

1. Packages are selected for the update according to the following guidelines.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-linux-rules.html)

For information about patch compliance status values, see [Patch compliance state values](patch-manager-compliance-states.md).

## How patch baseline rules work on Oracle Linux
<a name="linux-rules-oracle"></a>

On Oracle Linux, the patch selection process is as follows:

1. On the managed node, the YUM library accesses the `updateinfo.xml` file for each configured repo.
**Note**  
The `updateinfo.xml` file might not be available if the repo isn't one managed by Oracle. If there is no `updateinfo.xml` found, whether patches are installed depend on settings for **Include non-security updates** and **Auto-approval**. For example, if non-security updates are permitted, they're installed when the auto-approval time arrives.

1. Each update notice in `updateinfo.xml` includes several attributes that denote the properties of the packages in the notice, as described in the following table.  
**Update notice attributes**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-linux-rules.html)

   For information about accepted formats for lists of approved patches and rejected patches, see [Package name formats for approved and rejected patch lists](patch-manager-approved-rejected-package-name-formats.md).

1. The product of the managed node is determined by SSM Agent. This attribute corresponds to the value of the Product key attribute in the patch baseline's [PatchFilter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html) data type.

1. Packages are selected for the update according to the following guidelines.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-linux-rules.html)

For information about patch compliance status values, see [Patch compliance state values](patch-manager-compliance-states.md).

## How patch baseline rules work on AlmaLinux, RHEL, and Rocky Linux
<a name="linux-rules-rhel"></a>

On AlmaLinux, Red Hat Enterprise Linux (RHEL), and Rocky Linux, the patch selection process is as follows:

1. On the managed node, the YUM library (RHEL 7) or the DNF library (AlmaLinux 8 and 9, RHEL 8, 9, and 10, and Rocky Linux 8 and 9) accesses the `updateinfo.xml` file for each configured repo.
**Note**  
The `updateinfo.xml` file might not be available if the repo isn't one managed by Red Hat. If there is no `updateinfo.xml` found, whether patches are installed depend on settings for **Include non-security updates** and **Auto-approval**. For example, if non-security updates are permitted, they're installed when the auto-approval time arrives.

1. Each update notice in `updateinfo.xml` includes several attributes that denote the properties of the packages in the notice, as described in the following table.  
**Update notice attributes**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-linux-rules.html)

   For information about accepted formats for lists of approved patches and rejected patches, see [Package name formats for approved and rejected patch lists](patch-manager-approved-rejected-package-name-formats.md).

1. The product of the managed node is determined by SSM Agent. This attribute corresponds to the value of the Product key attribute in the patch baseline's [PatchFilter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html) data type.

1. Packages are selected for the update according to the following guidelines.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-linux-rules.html)

For information about patch compliance status values, see [Patch compliance state values](patch-manager-compliance-states.md).

## How patch baseline rules work on SUSE Linux Enterprise Server
<a name="linux-rules-sles"></a>

On SLES, each patch includes the following attributes that denote the properties of the packages in the patch:
+ **Category**: Corresponds to the value of the **Classification** key attribute in the patch baseline's [PatchFilter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html) data type. Denotes the type of patch included in the update notice.

  You can view the list of supported values by using the AWS CLI command **[describe-patch-properties](https://docs.aws.amazon.com/cli/latest/reference/ssm/describe-patch-properties.html)** or the API operation **[DescribePatchProperties](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribePatchProperties.html)**. You can also view the list in the **Approval rules** area of the **Create patch baseline** page or **Edit patch baseline** page in the Systems Manager console.
+ **Severity**: Corresponds to the value of the **Severity** key attribute in the patch baseline's [PatchFilter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html) data type. Denotes the severity of the patches.

  You can view the list of supported values by using the AWS CLI command **[describe-patch-properties](https://docs.aws.amazon.com/cli/latest/reference/ssm/describe-patch-properties.html)** or the API operation **[DescribePatchProperties](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribePatchProperties.html)**. You can also view the list in the **Approval rules** area of the **Create patch baseline** page or **Edit patch baseline** page in the Systems Manager console.

The product of the managed node is determined by SSM Agent. This attribute corresponds to the value of the **Product** key attribute in the patch baseline's [PatchFilter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PatchFilter.html) data type. 

For each patch, the patch baseline is used as a filter, allowing only the qualified packages to be included in the update. If multiple packages are applicable after applying the patch baseline definition, the latest version is used. 

For information about accepted formats for lists of approved patches and rejected patches, see [Package name formats for approved and rejected patch lists](patch-manager-approved-rejected-package-name-formats.md).

## How patch baseline rules work on Ubuntu Server
<a name="linux-rules-ubuntu"></a>

On Ubuntu Server, the patch baseline service offers filtering on the *Priority* and *Section *fields. These fields are typically present for all Ubuntu Server packages. To determine whether a patch is selected by the patch baseline, Patch Manager does the following:

1. On Ubuntu Server systems, the equivalent of `sudo apt-get update` is run to refresh the list of available packages. Repos aren't configured and the data is pulled from repos configured in a `sources` list.

1. If an update is available for `python3-apt` (a Python library interface to `libapt`), it is upgraded to the latest version. (This nonsecurity package is upgraded even if you did not select the **Include nonsecurity updates** option.)

1. Next, the [GlobalFilters](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreatePatchBaseline.html#systemsmanager-CreatePatchBaseline-request-GlobalFilters), [ApprovalRules](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreatePatchBaseline.html#EC2-CreatePatchBaseline-request-ApprovalRules), [ApprovedPatches](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreatePatchBaseline.html#EC2-CreatePatchBaseline-request-ApprovedPatches) and [RejectedPatches](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreatePatchBaseline.html#EC2-CreatePatchBaseline-request-RejectedPatches) lists are applied.
**Note**  
Because it's not possible to reliably determine the release dates of update packages for Ubuntu Server, the auto-approval options aren't supported for this operating system.

   Approval rules, however, are also subject to whether the **Include nonsecurity updates** check box was selected when creating or last updating a patch baseline.

   If nonsecurity updates are excluded, an implicit rule is applied in order to select only packages with upgrades in security repos. For each package, the candidate version of the package (which is typically the latest version) must be part of a security repo. In this case, for Ubuntu Server, patch candidate versions are limited to patches included in the following repos:
   + Ubuntu Server 18.04 LTS: `bionic-security`
   + Ubuntu Server 20.04 LTS: `focal-security`
   + Ubuntu Server 22.04 LTS: `jammy-security`
   + Ubuntu Server 24.04 LTS: `noble-security`
   + Ubuntu Server 25.04: `plucky-security`

   If nonsecurity updates are included, patches from other repositories are considered as well.

   For information about accepted formats for lists of approved patches and rejected patches, see [Package name formats for approved and rejected patch lists](patch-manager-approved-rejected-package-name-formats.md).

To view the contents of the *Priority* and *Section *fields, run the following `aptitude` command: 

**Note**  
You might need to first install Aptitude on Ubuntu Server 16 systems.

```
aptitude search -F '%p %P %s %t %V#' '~U'
```

In the response to this command, all upgradable packages are reported in this format: 

```
name, priority, section, archive, candidate version
```

For information about patch compliance status values, see [Patch compliance state values](patch-manager-compliance-states.md).