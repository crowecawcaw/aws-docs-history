• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# How patch baseline rules work on

Linux-based systems

The rules in a patch baseline for Linux distributions operate differently based on
the distribution type. Unlike patch updates on Windows Server managed nodes, rules are
evaluated on each node to take the configured repos on the instance into
consideration. Patch Manager, a tool in AWS Systems Manager, uses the native package manager to
drive the installation of patches approved by the patch baseline.

For Linux-based operating system types that report a severity level for patches,
Patch Manager uses the severity level reported by the software publisher for the update
notice or individual patch. Patch Manager doesn't derive severity levels from third-party
sources, such as the [Common Vulnerability
Scoring System](https://www.first.org/cvss/ "https://www.first.org/cvss/") (CVSS), or from metrics released by the [National Vulnerability Database](https://nvd.nist.gov/vuln "https://nvd.nist.gov/vuln")
(NVD).

###### Topics

- [How patch baseline rules work on
  Amazon Linux 2 and Amazon Linux 2023](#linux-rules-amazon-linux "#linux-rules-amazon-linux")
- [How patch baseline rules work on
  CentOS Stream](#linux-rules-centos "#linux-rules-centos")
- [How patch baseline rules work on
  Debian Server](#linux-rules-debian "#linux-rules-debian")
- [How patch baseline rules work on
  macOS](#linux-rules-macos "#linux-rules-macos")
- [How patch baseline rules work on
  Oracle Linux](#linux-rules-oracle "#linux-rules-oracle")
- [How patch baseline rules work on AlmaLinux,
  RHEL, and Rocky Linux](#linux-rules-rhel "#linux-rules-rhel")
- [How patch baseline rules work on
  SUSE Linux Enterprise Server](#linux-rules-sles "#linux-rules-sles")
- [How patch baseline rules work on
  Ubuntu Server](#linux-rules-ubuntu "#linux-rules-ubuntu")

## How patch baseline rules work on

Amazon Linux 2 and Amazon Linux 2023

###### Note

Amazon Linux 2023 (AL2023) uses versioned repositories that can be locked to
a specific version through one or more system settings. For all patching
operations on AL2023 EC2 instances, Patch Manager uses the latest repository
versions, independent of the system configuration. For more information, see
[Deterministic upgrades
through versioned repositories](../../../linux/al2023/ug/deterministic-upgrades.md "../../../linux/al2023/ug/deterministic-upgrades.md") in the _Amazon Linux 2023
User Guide_.

On Amazon Linux 2 and Amazon Linux 2023, the patch selection process is as follows:

1. On the managed node, the YUM library (Amazon Linux 2) or the DNF library
   (Amazon Linux 2023) accesses the `updateinfo.xml` file for
   each configured repo.

If no `updateinfo.xml` file is found, whether
patches are installed depend on settings for **Include
non-security updates** and
**Auto-approval**. For example, if non-security
updates are permitted, they're installed when the auto-approval time
arrives. 2. Each update notice in `updateinfo.xml` includes
several attributes that denote the properties of the packages in the
notice, as described in the following table.

| Update notice attributes | Attribute                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| type                     | Corresponds to the value of the Classification key<br>attribute in the patch baseline's [PatchFilter](../APIReference/API_PatchFilter.md "../APIReference/API_PatchFilter.md")<br>data type. Denotes the type of package included in<br>the update notice. You can view the list of supported values by using the AWS CLI command<br>**[describe-patch-properties](../../../cli/latest/reference/ssm/describe-patch-properties.md "../../../cli/latest/reference/ssm/describe-patch-properties.md")\*<br>• or the API operation<br>**[DescribePatchProperties](../APIReference/API_DescribePatchProperties.md "../APIReference/API_DescribePatchProperties.md")**. You can also view the list in the<br>**Approval rules*<br>• area of the \*\*Create patch<br>baseline*<br>• page or \*_Edit patch baseline_<br>• page in the Systems Manager<br>console.                                                                      |
| severity                 | Corresponds to the value of the Severity key<br>attribute in the patch baseline's [PatchFilter](../APIReference/API_PatchFilter.md "../APIReference/API_PatchFilter.md")<br>data type. Denotes the severity of the packages<br>included in the update notice. Usually only<br>applicable for _Security<br>• update notices.<br>You can view the list of supported values by using the AWS CLI command<br>\*\*[describe-patch-properties](../../../cli/latest/reference/ssm/describe-patch-properties.md "../../../cli/latest/reference/ssm/describe-patch-properties.md")_<br>• or the API operation<br>**[DescribePatchProperties](../APIReference/API_DescribePatchProperties.md "../APIReference/API_DescribePatchProperties.md")**. You can also view the list in the<br>**Approval rules\*<br>• area of the **Create patch<br>baseline*<br>• page or \*\*Edit patch baseline*<br>• page in the Systems Manager<br>console. |
| update_id                | Denotes the advisory ID, such as _ALAS-2017-867_. The<br>advisory ID can be used in the<br>[ApprovedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches") or [RejectedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches")<br>attribute in the patch baseline.                                                                                                                                                                                                                                                                                                                                                                         |
| references               | Contains additional information about the update<br>notice, such as a CVE ID (format: _CVE-2017-1234567_). The<br>CVE ID can be used in the [ApprovedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches") or<br>[RejectedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches") attribute in the patch<br>baseline.                                                                                                                                                                                                                                                                                                                     |
| updated                  | Corresponds to [ApproveAfterDays](../APIReference/API_PatchRule.md#EC2-Type-PatchRule-ApproveAfterDays "../APIReference/API_PatchRule.md#EC2-Type-PatchRule-ApproveAfterDays") in the<br>patch baseline. Denotes the released date (updated<br>date) of the packages included in the update notice.<br>A comparison between the current timestamp and the<br>value of this attribute plus the<br>`ApproveAfterDays` is used to determine<br>if the patch is approved for deployment.                                                                                                                                                                                                                                                                                                                                                                                                                                            |

For information about accepted formats for lists of approved patches and rejected patches,
see [Package name
formats for approved and rejected patch lists](patch-manager-approved-rejected-package-name-formats.md "patch-manager-approved-rejected-package-name-formats.md"). 3. The product of the managed node is determined by SSM Agent. This
attribute corresponds to the value of the Product key attribute in the
patch baseline's [PatchFilter](../APIReference/API_PatchFilter.md "../APIReference/API_PatchFilter.md") data type. 4. Packages are selected for the update according to the following
guidelines.

| Security option                                                                                                                                                                                                   | Patch selection                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pre-defined default patch baselines provided by<br>AWS and custom patch baselines where the<br>**Include non-security updates**<br>check box is _not_<br>selected                                                 | For each update notice in<br>`updateinfo.xml`, the patch<br>baseline is used as a filter, allowing only the<br>qualified packages to be included in the update. If<br>multiple packages are applicable after applying the<br>patch baseline definition, the latest version is<br>used.<br>For Amazon Linux 2, the equivalent yum command for this<br>workflow is:<br>`<br>sudo yum update-minimal --sec-severity=Critical,Important --bugfix -y<br>`<br>For Amazon Linux 2023, the equivalent dnf command for<br>this workflow is:<br>`<br>sudo dnf upgrade-minimal --sec-severity=Critical --sec-severity=Important --bugfix -y<br>`                                                                                                                                                                     |
| Custom patch baselines where the \*_Include<br>non-security updates_<br>• check box<br>\*is<br>• selected<br>with a SEVERITY list of `[Critical, Important]` and a CLASSIFICATION list of `[Security,<br>Bugfix]` | In addition to applying the security updates that<br>were selected from<br>`updateinfo.xml`, Patch Manager<br>applies nonsecurity updates that otherwise meet the<br>patch filtering rules.<br>For Amazon Linux 2, the equivalent yum command for this<br>workflow is:<br>`<br>sudo yum update --security --sec-severity=Critical,Important --bugfix -y<br>`<br>For Amazon Linux 2023, the equivalent dnf command for<br>this workflow is:<br>`<br>sudo dnf upgrade --security --sec-severity=Critical --sec-severity=Important --bugfix -y<br>`<br>NoteNew packages that replace now-obsolete packages with different names are installed if<br>you run these `yum` or `dnf` commands outside of Patch Manager.<br>However, they are \*not<br>• installed by the equivalent Patch Manager<br>operations. |

For information about patch compliance status values, see [Patch compliance state
values](patch-manager-compliance-states.md "patch-manager-compliance-states.md").

## How patch baseline rules work on

CentOS Stream

The CentOS Stream default repositories do not include an
`updateinfo.xml` file. However, custom repositories that
you create or use might include this file. In this topic, references to
`updateinfo.xml` apply only to these custom
repositories.

On CentOS Stream, the patch selection process is as
follows:

1. On the managed node,
   the DNF library
   accesses the
   `updateinfo.xml` file, if it exists in a custom
   repository, for each configured repo.

If there is no `updateinfo.xml` found, which always
includes the default repos, whether patches are installed depends on
settings for **Include non-security updates** and
**Auto-approval**. For example, if non-security
updates are permitted, they're installed when the auto-approval time
arrives. 2. If `updateinfo.xml` is present, each update notice
in the file includes several attributes that denote the properties of
the packages in the notice, as described in the following table.

| Update notice attributes | Attribute                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| type                     | Corresponds to the value of the Classification key<br>attribute in the patch baseline's [PatchFilter](../APIReference/API_PatchFilter.md "../APIReference/API_PatchFilter.md")<br>data type. Denotes the type of package included in<br>the update notice. You can view the list of supported values by using the AWS CLI command<br>**[describe-patch-properties](../../../cli/latest/reference/ssm/describe-patch-properties.md "../../../cli/latest/reference/ssm/describe-patch-properties.md")\*<br>• or the API operation<br>**[DescribePatchProperties](../APIReference/API_DescribePatchProperties.md "../APIReference/API_DescribePatchProperties.md")**. You can also view the list in the<br>**Approval rules*<br>• area of the \*\*Create patch<br>baseline*<br>• page or \*_Edit patch baseline_<br>• page in the Systems Manager<br>console.                                                                      |
| severity                 | Corresponds to the value of the Severity key<br>attribute in the patch baseline's [PatchFilter](../APIReference/API_PatchFilter.md "../APIReference/API_PatchFilter.md")<br>data type. Denotes the severity of the packages<br>included in the update notice. Usually only<br>applicable for _Security<br>• update notices.<br>You can view the list of supported values by using the AWS CLI command<br>\*\*[describe-patch-properties](../../../cli/latest/reference/ssm/describe-patch-properties.md "../../../cli/latest/reference/ssm/describe-patch-properties.md")_<br>• or the API operation<br>**[DescribePatchProperties](../APIReference/API_DescribePatchProperties.md "../APIReference/API_DescribePatchProperties.md")**. You can also view the list in the<br>**Approval rules\*<br>• area of the **Create patch<br>baseline*<br>• page or \*\*Edit patch baseline*<br>• page in the Systems Manager<br>console. |
| update_id                | Denotes the advisory ID, such as _CVE-2019-17055_. The<br>advisory ID can be used in the<br>[ApprovedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches") or [RejectedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches")<br>attribute in the patch baseline.                                                                                                                                                                                                                                                                                                                                                                        |
| references               | Contains additional information about the update<br>notice, such as a CVE ID (format: _CVE-2019-17055_) or a<br>Bugzilla ID (format: _1463241_). The CVE ID and Bugzilla ID<br>can be used in the [ApprovedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches") or<br>[RejectedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches") attribute in the patch<br>baseline.                                                                                                                                                                                                                                                               |
| updated                  | Corresponds to [ApproveAfterDays](../APIReference/API_PatchRule.md#EC2-Type-PatchRule-ApproveAfterDays "../APIReference/API_PatchRule.md#EC2-Type-PatchRule-ApproveAfterDays") in the<br>patch baseline. Denotes the released date (updated<br>date) of the packages included in the update notice.<br>A comparison between the current timestamp and the<br>value of this attribute plus the<br>`ApproveAfterDays` is used to determine<br>if the patch is approved for deployment.                                                                                                                                                                                                                                                                                                                                                                                                                                            |

For information about accepted formats for lists of approved patches and rejected patches,
see [Package name
formats for approved and rejected patch lists](patch-manager-approved-rejected-package-name-formats.md "patch-manager-approved-rejected-package-name-formats.md"). 3. In all cases, the product of the managed node is determined by
SSM Agent. This attribute corresponds to the value of the Product key
attribute in the patch baseline's [PatchFilter](../APIReference/API_PatchFilter.md "../APIReference/API_PatchFilter.md") data type. 4. Packages are selected for the update according to the following
guidelines.

| Security option                                                                                                                                                                                                      | Patch selection                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pre-defined default patch baselines provided by<br>AWS and custom patch baselines where the<br>**Include non-security updates**<br>check box is _not_<br>selected                                                    | For each update notice in<br>`updateinfo.xml`, if it exists<br>in a custom repository, the patch baseline is used<br>as a filter, allowing only the qualified packages to<br>be included in the update. If multiple packages are<br>applicable after applying the patch baseline<br>definition, the latest version is used.<br>For CentOS Stream where<br>`updateinfo.xml` is present,<br>the equivalent dnf command for this workflow<br>is:<br>`<br>sudo dnf upgrade-minimal ‐‐sec-severity=Critical ‐‐sec-severity=Important ‐‐bugfix -y<br>`                                                                                                                                                                                                                                                                                                                                                                     |
| Custom patch baselines where the \*_Include<br>non-security updates_<br>• check box<br>\*is<br>• selected<br>with a SEVERITY list of `[Critical,<br>Important]` and a CLASSIFICATION list of<br>`[Security, Bugfix]` | In addition to applying the security updates that<br>were selected from<br>`updateinfo.xml`, if it exists<br>in a custom repository, Patch Manager applies nonsecurity<br>updates that otherwise meet the patch filtering<br>rules.<br>For CentOS Stream where<br>`updateinfo.xml` is present,<br>the equivalent dnf command for this workflow<br>is:<br>`<br>sudo dnf upgrade ‐‐security ‐‐sec-severity=Critical ‐‐sec-severity=Important ‐‐bugfix -y<br>`<br>For default repos and custom repos without<br>`updateinfo.xml`, you *must<br>• select the<br>**Include non-security updates**<br>check box in order to update operating system (OS)<br>packages. NoteNew packages that replace now-obsolete packages with different names are installed if<br>you run these `yum` or `dnf` commands outside of Patch Manager.<br>However, they are *not<br>• installed by the equivalent Patch Manager<br>operations. |

For information about patch compliance status values, see [Patch compliance state
values](patch-manager-compliance-states.md "patch-manager-compliance-states.md").

## How patch baseline rules work on

Debian Server

On Debian Server , the patch baseline service offers filtering on the _Priority_ and _Section_ fields. These fields are typically present for all Debian Server
packages. To determine whether a patch is selected by the patch baseline,
Patch Manager does the following:

1. On Debian Server systems, the equivalent of `sudo apt-get
update` is run to refresh the list of available packages.
   Repos aren't configured and the data is pulled from repos configured in
   a `sources` list.
2. If an update is available for `python3-apt` (a
   Python library interface to `libapt`), it is upgraded
   to the latest version. (This nonsecurity package is upgraded even if you
   did not select the **Include nonsecurity updates**
   option.)
3. Next, the [GlobalFilters](../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters "../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters"), [ApprovalRules](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules"),
   [ApprovedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches") and [RejectedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches") lists are
   applied.

###### Note

Because it isn't possible to reliably determine the release dates of update
packages for Debian Server, the auto-approval options aren't supported for this
operating system.

Approval rules, however, are also subject to whether the
**Include nonsecurity updates** check box was
selected when creating or last updating a patch baseline.

If nonsecurity updates are excluded, an implicit rule is applied in
order to select only packages with upgrades in security repos. For each
package, the candidate version of the package (which is typically the
latest version) must be part of a security repo. In this case, for
Debian Server, patch candidate versions are limited to patches included in
the following repos:

These repos are named as follows:

    * Debian Server 11: `debian-security
     bullseye`
    * Debian Server 12: `debian-security
     bookworm`

If nonsecurity updates are included, patches from other repositories
are considered as well.

For information about accepted formats for lists of approved patches and rejected patches,
see [Package name
formats for approved and rejected patch lists](patch-manager-approved-rejected-package-name-formats.md "patch-manager-approved-rejected-package-name-formats.md").

To view the contents of the _Priority_ and
_Section_ fields, run the following
`aptitude` command:

###### Note

You might need to first install Aptitude on Debian Server systems.

```
aptitude search -F '%p %P %s %t %V#' '~U'
```

In the response to this command, all upgradable packages are reported in this
format:

```
name, priority, section, archive, candidate version
```

For information about patch compliance status values, see [Patch compliance state
values](patch-manager-compliance-states.md "patch-manager-compliance-states.md").

## How patch baseline rules work on

macOS

On macOS, the patch selection process is as follows:

1. On the managed node, Patch Manager accesses the parsed contents of the
   `InstallHistory.plist` file and identifies
   package names and versions.

For details about the parsing process, see the
**macOS** tab in [How patches are installed](patch-manager-installing-patches.md "patch-manager-installing-patches.md"). 2. The product of the managed node is determined by SSM Agent. This
attribute corresponds to the value of the Product key attribute in the
patch baseline's [PatchFilter](../APIReference/API_PatchFilter.md "../APIReference/API_PatchFilter.md") data type. 3. Packages are selected for the update according to the following
guidelines.

| Security option                                                                                                                                                   | Patch selection                                                                                                                                                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pre-defined default patch baselines provided by<br>AWS and custom patch baselines where the<br>**Include non-security updates**<br>check box is _not_<br>selected | For each available package update, the patch<br>baseline is used as a filter, allowing only the<br>qualified packages to be included in the update. If<br>multiple packages are applicable after applying the<br>patch baseline definition, the latest version is<br>used. |
| Custom patch baselines where the \*_Include<br>non-security updates_<br>• check box<br>_is_<br>selected                                                           | In addition to applying the security updates that<br>were identified by using<br>`InstallHistory.plist` , Patch<br>Manager applies nonsecurity updates that otherwise<br>meet the patch filtering rules.                                                                   |

For information about patch compliance status values, see [Patch compliance state
values](patch-manager-compliance-states.md "patch-manager-compliance-states.md").

## How patch baseline rules work on

Oracle Linux

On Oracle Linux, the patch selection process is as follows:

1. On the managed node, the YUM library accesses the
   `updateinfo.xml` file for each configured
   repo.

###### Note

The `updateinfo.xml` file might not be
available if the repo isn't one managed by Oracle. If
there is no `updateinfo.xml` found, whether
patches are installed depend on settings for **Include
non-security updates** and
**Auto-approval**. For example, if non-security
updates are permitted, they're installed when the auto-approval time
arrives. 2. Each update notice in `updateinfo.xml` includes
several attributes that denote the properties of the packages in the
notice, as described in the following table.

| Update notice attributes | Attribute                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| type                     | Corresponds to the value of the Classification key<br>attribute in the patch baseline's [PatchFilter](../APIReference/API_PatchFilter.md "../APIReference/API_PatchFilter.md")<br>data type. Denotes the type of package included in<br>the update notice. You can view the list of supported values by using the AWS CLI command<br>**[describe-patch-properties](../../../cli/latest/reference/ssm/describe-patch-properties.md "../../../cli/latest/reference/ssm/describe-patch-properties.md")\*<br>• or the API operation<br>**[DescribePatchProperties](../APIReference/API_DescribePatchProperties.md "../APIReference/API_DescribePatchProperties.md")**. You can also view the list in the<br>**Approval rules*<br>• area of the \*\*Create patch<br>baseline*<br>• page or \*_Edit patch baseline_<br>• page in the Systems Manager<br>console.                                                                      |
| severity                 | Corresponds to the value of the Severity key<br>attribute in the patch baseline's [PatchFilter](../APIReference/API_PatchFilter.md "../APIReference/API_PatchFilter.md")<br>data type. Denotes the severity of the packages<br>included in the update notice. Usually only<br>applicable for _Security<br>• update notices.<br>You can view the list of supported values by using the AWS CLI command<br>\*\*[describe-patch-properties](../../../cli/latest/reference/ssm/describe-patch-properties.md "../../../cli/latest/reference/ssm/describe-patch-properties.md")_<br>• or the API operation<br>**[DescribePatchProperties](../APIReference/API_DescribePatchProperties.md "../APIReference/API_DescribePatchProperties.md")**. You can also view the list in the<br>**Approval rules\*<br>• area of the **Create patch<br>baseline*<br>• page or \*\*Edit patch baseline*<br>• page in the Systems Manager<br>console. |
| update_id                | Denotes the advisory ID, such as _CVE-2019-17055_. The<br>advisory ID can be used in the<br>[ApprovedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches") or [RejectedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches")<br>attribute in the patch baseline.                                                                                                                                                                                                                                                                                                                                                                        |
| references               | Contains additional information about the update<br>notice, such as a CVE ID (format: _CVE-2019-17055_) or a<br>Bugzilla ID (format: _1463241_). The CVE ID and Bugzilla ID<br>can be used in the [ApprovedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches") or<br>[RejectedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches") attribute in the patch<br>baseline.                                                                                                                                                                                                                                                               |
| updated                  | Corresponds to [ApproveAfterDays](../APIReference/API_PatchRule.md#EC2-Type-PatchRule-ApproveAfterDays "../APIReference/API_PatchRule.md#EC2-Type-PatchRule-ApproveAfterDays") in the<br>patch baseline. Denotes the released date (updated<br>date) of the packages included in the update notice.<br>A comparison between the current timestamp and the<br>value of this attribute plus the<br>`ApproveAfterDays` is used to determine<br>if the patch is approved for deployment.                                                                                                                                                                                                                                                                                                                                                                                                                                            |

For information about accepted formats for lists of approved patches and rejected patches,
see [Package name
formats for approved and rejected patch lists](patch-manager-approved-rejected-package-name-formats.md "patch-manager-approved-rejected-package-name-formats.md"). 3. The product of the managed node is determined by SSM Agent. This
attribute corresponds to the value of the Product key attribute in the
patch baseline's [PatchFilter](../APIReference/API_PatchFilter.md "../APIReference/API_PatchFilter.md") data type. 4. Packages are selected for the update according to the following
guidelines.

| Security option                                                                                                                                                                                                      | Patch selection                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Pre-defined default patch baselines provided by<br>AWS and custom patch baselines where the<br>**Include non-security updates**<br>check box is _not_<br>selected                                                    | For each update notice in<br>`updateinfo.xml`, the patch<br>baseline is used as a filter, allowing only the<br>qualified packages to be included in the update. If<br>multiple packages are applicable after applying the<br>patch baseline definition, the latest version is<br>used.<br>For version 7 managed nodes, the equivalent yum<br>command for this workflow is:<br>`<br>sudo yum update-minimal --sec-severity=Important,Moderate --bugfix -y<br>`<br>For version 8 and 9 managed nodes, the equivalent<br>dnf command for this workflow is:<br>`<br>sudo dnf upgrade-minimal --security --sec-severity=Moderate --sec-severity=Important<br>`                                                                                                                                                                      |
| Custom patch baselines where the \*_Include<br>non-security updates_<br>• check box<br>\*is<br>• selected<br>with a SEVERITY list of `[Critical,<br>Important]` and a CLASSIFICATION list of<br>`[Security, Bugfix]` | In addition to applying the security updates that<br>were selected from<br>`updateinfo.xml`, Patch Manager<br>applies nonsecurity updates that otherwise meet the<br>patch filtering rules.<br>For version 7 managed nodes, the equivalent yum<br>command for this workflow is:<br>`<br>sudo yum update --security --sec-severity=Critical,Important --bugfix -y<br>`<br>For version 8 and 9 managed nodes, the equivalent<br>dnf command for this workflow is:<br>`<br>sudo dnf upgrade --security --sec-severity=Critical, --sec-severity=Important --bugfix y<br>`<br>NoteNew packages that replace now-obsolete packages with different names are installed if<br>you run these `yum` or `dnf` commands outside of Patch Manager.<br>However, they are \*not<br>• installed by the equivalent Patch Manager<br>operations. |

For information about patch compliance status values, see [Patch compliance state
values](patch-manager-compliance-states.md "patch-manager-compliance-states.md").

## How patch baseline rules work on AlmaLinux,

RHEL, and Rocky Linux

On AlmaLinux, Red Hat Enterprise Linux (RHEL), and Rocky Linux, the patch selection process is
as follows:

1. On the managed node, the YUM library (RHEL 7) or the DNF library
   (AlmaLinux 8 and 9, RHEL 8, 9, and 10, and Rocky Linux 8 and 9) accesses
   the `updateinfo.xml` file for each configured
   repo.

###### Note

The `updateinfo.xml` file might not be
available if the repo isn't one managed by Red Hat. If there is no
`updateinfo.xml` found, no patch will be
applied. 2. Each update notice in `updateinfo.xml` includes
several attributes that denote the properties of the packages in the
notice, as described in the following table.

| Update notice attributes | Attribute                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| type                     | Corresponds to the value of the Classification key<br>attribute in the patch baseline's [PatchFilter](../APIReference/API_PatchFilter.md "../APIReference/API_PatchFilter.md")<br>data type. Denotes the type of package included in<br>the update notice. You can view the list of supported values by using the AWS CLI command<br>**[describe-patch-properties](../../../cli/latest/reference/ssm/describe-patch-properties.md "../../../cli/latest/reference/ssm/describe-patch-properties.md")\*<br>• or the API operation<br>**[DescribePatchProperties](../APIReference/API_DescribePatchProperties.md "../APIReference/API_DescribePatchProperties.md")**. You can also view the list in the<br>**Approval rules*<br>• area of the \*\*Create patch<br>baseline*<br>• page or \*_Edit patch baseline_<br>• page in the Systems Manager<br>console.                                                                      |
| severity                 | Corresponds to the value of the Severity key<br>attribute in the patch baseline's [PatchFilter](../APIReference/API_PatchFilter.md "../APIReference/API_PatchFilter.md")<br>data type. Denotes the severity of the packages<br>included in the update notice. Usually only<br>applicable for _Security<br>• update notices.<br>You can view the list of supported values by using the AWS CLI command<br>\*\*[describe-patch-properties](../../../cli/latest/reference/ssm/describe-patch-properties.md "../../../cli/latest/reference/ssm/describe-patch-properties.md")_<br>• or the API operation<br>**[DescribePatchProperties](../APIReference/API_DescribePatchProperties.md "../APIReference/API_DescribePatchProperties.md")**. You can also view the list in the<br>**Approval rules\*<br>• area of the **Create patch<br>baseline*<br>• page or \*\*Edit patch baseline*<br>• page in the Systems Manager<br>console. |
| update_id                | Denotes the advisory ID, such as _RHSA-2017:0864_. The<br>advisory ID can be used in the<br>[ApprovedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches") or [RejectedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches")<br>attribute in the patch baseline.                                                                                                                                                                                                                                                                                                                                                                        |
| references               | Contains additional information about the update<br>notice, such as a CVE ID (format: _CVE-2017-1000371_) or a<br>Bugzilla ID (format: _1463241_). The CVE ID and Bugzilla ID<br>can be used in the [ApprovedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches") or<br>[RejectedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches") attribute in the patch<br>baseline.                                                                                                                                                                                                                                                             |
| updated                  | Corresponds to [ApproveAfterDays](../APIReference/API_PatchRule.md#EC2-Type-PatchRule-ApproveAfterDays "../APIReference/API_PatchRule.md#EC2-Type-PatchRule-ApproveAfterDays") in the<br>patch baseline. Denotes the released date (updated<br>date) of the packages included in the update notice.<br>A comparison between the current timestamp and the<br>value of this attribute plus the<br>`ApproveAfterDays` is used to determine<br>if the patch is approved for deployment.                                                                                                                                                                                                                                                                                                                                                                                                                                            |

For information about accepted formats for lists of approved patches and rejected patches,
see [Package name
formats for approved and rejected patch lists](patch-manager-approved-rejected-package-name-formats.md "patch-manager-approved-rejected-package-name-formats.md"). 3. The product of the managed node is determined by SSM Agent. This
attribute corresponds to the value of the Product key attribute in the
patch baseline's [PatchFilter](../APIReference/API_PatchFilter.md "../APIReference/API_PatchFilter.md") data type. 4. Packages are selected for the update according to the following
guidelines.

| Security option                                                                                                                                                                                                      | Patch selection                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pre-defined default patch baselines provided by<br>AWS and custom patch baselines where the<br>**Include non-security updates**<br>check box is _not_<br>selected in any rule                                        | For each update notice in<br>`updateinfo.xml`, the patch<br>baseline is used as a filter, allowing only the<br>qualified packages to be included in the update. If<br>multiple packages are applicable after applying the<br>patch baseline definition, the latest version is<br>used.<br>For RHEL 7, the equivalent yum command for this<br>workflow is:<br>`<br>sudo yum update-minimal --sec-severity=Critical,Important --bugfix -y<br>`<br>For AlmaLinux 8 and 9, RHEL 8, 9, and 10, and<br>Rocky Linux 8 and 9, the equivalent dnf command for this<br>workflow is:<br>`<br>sudo dnf upgrade-minimal --sec-severity=Critical --sec-severity=Important --bugfix -y<br>`                                                                                                                                                          |
| Custom patch baselines where the \*_Include<br>non-security updates_<br>• check box<br>\*is<br>• selected<br>with a SEVERITY list of `[Critical,<br>Important]` and a CLASSIFICATION list of<br>`[Security, Bugfix]` | In addition to applying the security updates that<br>were selected from<br>`updateinfo.xml`, Patch Manager<br>applies nonsecurity updates that otherwise meet the<br>patch filtering rules.<br>For RHEL 7, the equivalent yum command for this<br>workflow is:<br>`<br>sudo yum update --security --sec-severity=Critical,Important --bugfix -y<br>`<br>For AlmaLinux 8 and 9, RHEL 8, 9, and 10, and<br>Rocky Linux 8 and 9, the equivalent dnf command for this<br>workflow is:<br>`<br>sudo dnf upgrade --sec-severity=Critical --sec-severity=Important --bugfix -y<br>`<br>NoteNew packages that replace now-obsolete packages with different names are installed if<br>you run these `yum` or `dnf` commands outside of Patch Manager.<br>However, they are \*not<br>• installed by the equivalent Patch Manager<br>operations. |

For information about patch compliance status values, see [Patch compliance state
values](patch-manager-compliance-states.md "patch-manager-compliance-states.md").

## How patch baseline rules work on

SUSE Linux Enterprise Server

On SLES, each patch includes the following attributes that denote the
properties of the packages in the patch:

- **Category**: Corresponds to the value of
  the **Classification** key attribute in the
  patch baseline's [PatchFilter](../APIReference/API_PatchFilter.md "../APIReference/API_PatchFilter.md") data type. Denotes the type of patch
  included in the update notice.

You can view the list of supported values by using the AWS CLI command
**[describe-patch-properties](../../../cli/latest/reference/ssm/describe-patch-properties.md "../../../cli/latest/reference/ssm/describe-patch-properties.md")** or the API operation
**[DescribePatchProperties](../APIReference/API_DescribePatchProperties.md "../APIReference/API_DescribePatchProperties.md")**. You can also view the list in the
**Approval rules** area of the **Create patch
baseline** page or **Edit patch baseline** page in the Systems Manager
console.

- **Severity**: Corresponds to the value of
  the **Severity** key attribute in the patch
  baseline's [PatchFilter](../APIReference/API_PatchFilter.md "../APIReference/API_PatchFilter.md") data type. Denotes the severity of the
  patches.

You can view the list of supported values by using the AWS CLI command
**[describe-patch-properties](../../../cli/latest/reference/ssm/describe-patch-properties.md "../../../cli/latest/reference/ssm/describe-patch-properties.md")** or the API operation
**[DescribePatchProperties](../APIReference/API_DescribePatchProperties.md "../APIReference/API_DescribePatchProperties.md")**. You can also view the list in the
**Approval rules** area of the **Create patch
baseline** page or **Edit patch baseline** page in the Systems Manager
console.

The product of the managed node is determined by SSM Agent. This attribute
corresponds to the value of the **Product** key
attribute in the patch baseline's [PatchFilter](../APIReference/API_PatchFilter.md "../APIReference/API_PatchFilter.md") data type.

For each patch, the patch baseline is used as a filter, allowing only the
qualified packages to be included in the update. If multiple packages are
applicable after applying the patch baseline definition, the latest version is
used.

For information about accepted formats for lists of approved patches and rejected patches,
see [Package name
formats for approved and rejected patch lists](patch-manager-approved-rejected-package-name-formats.md "patch-manager-approved-rejected-package-name-formats.md").

## How patch baseline rules work on

Ubuntu Server

On Ubuntu Server, the patch baseline service offers filtering on the _Priority_ and _Section_ fields. These fields are typically present for all Ubuntu Server
packages. To determine whether a patch is selected by the patch baseline,
Patch Manager does the following:

1. On Ubuntu Server systems, the equivalent of `sudo apt-get
update` is run to refresh the list of available packages.
   Repos aren't configured and the data is pulled from repos configured in
   a `sources` list.
2. If an update is available for `python3-apt` (a
   Python library interface to `libapt`), it is upgraded
   to the latest version. (This nonsecurity package is upgraded even if you
   did not select the **Include nonsecurity updates**
   option.)
3. Next, the [GlobalFilters](../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters "../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters"), [ApprovalRules](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules"),
   [ApprovedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches") and [RejectedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches") lists are
   applied.

###### Note

Because it's not possible to reliably determine the release dates of update
packages for Ubuntu Server, the auto-approval options aren't supported for this
operating system.

Approval rules, however, are also subject to whether the
**Include nonsecurity updates** check box was
selected when creating or last updating a patch baseline.

If nonsecurity updates are excluded, an implicit rule is applied in
order to select only packages with upgrades in security repos. For each
package, the candidate version of the package (which is typically the
latest version) must be part of a security repo. In this case, for
Ubuntu Server, patch candidate versions are limited to patches included in
the following repos:

    * Ubuntu Server 16.04 LTS:
     `xenial-security`
    * Ubuntu Server 18.04 LTS:
     `bionic-security`
    * Ubuntu Server 20.04 LTS:
     `focal-security`
    * Ubuntu Server 22.04 LTS
     (`jammy-security`)
    * Ubuntu Server 24.04 LTS
     (`noble-security`)
    * Ubuntu Server 25.04
     (`plucky-security`)

If nonsecurity updates are included, patches from other repositories
are considered as well.

For information about accepted formats for lists of approved patches and rejected patches,
see [Package name
formats for approved and rejected patch lists](patch-manager-approved-rejected-package-name-formats.md "patch-manager-approved-rejected-package-name-formats.md").

To view the contents of the _Priority_ and
_Section_ fields, run the following
`aptitude` command:

###### Note

You might need to first install Aptitude on Ubuntu Server 16 systems.

```
aptitude search -F '%p %P %s %t %V#' '~U'
```

In the response to this command, all upgradable packages are reported in this
format:

```
name, priority, section, archive, candidate version
```

For information about patch compliance status values, see [Patch compliance state
values](patch-manager-compliance-states.md "patch-manager-compliance-states.md").
