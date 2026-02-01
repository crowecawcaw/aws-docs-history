• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# How patches are installed

Patch Manager, a tool in AWS Systems Manager, uses the operating system built-in package manager
to install updates on managed nodes. For example, it uses the Windows Update API on
Windows Server and `DNF` on Amazon Linux 2023. Patch Manager respects existing package manager
and repository configurations on the nodes, including settings such as repository status,
mirror URLs, GPG verification, and options like `skip_if_unavailable`.

Patch Manager doesn't install a new package that replaces an obsolete package that's
currently installed. (Exceptions: The new package is a dependency of another package
updating being installed, or the new package has the same name as the obsolete
package.) Instead, Patch Manager reports on and installs available updates to installed
packages. This approach helps prevent unexpected changes to your system
functionality that might occur when one package replaces another.

If you need to uninstall a package that has been made obsolete and install its
replacement, you might need to use a custom script or use package manager commands
outside of Patch Manager's standard operations.

Choose from the following tabs to learn how Patch Manager installs
patches on an operating system.

Amazon Linux 2 and Amazon Linux 2023
On Amazon Linux 2 and Amazon Linux 2023 managed nodes, the patch installation
workflow is as follows:

1. If a list of patches is specified using an https URL or an
   Amazon Simple Storage Service (Amazon S3) path-style URL using the
   `InstallOverrideList` parameter for the
   `AWS-RunPatchBaseline` or
   `AWS-RunPatchBaselineAssociation` documents, the
   listed patches are installed and steps 2-7 are skipped.
2. Apply [GlobalFilters](../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters "../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters") as specified in the patch baseline,
   keeping only the qualified packages for further processing.
3. Apply [ApprovalRules](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules") as specified in the patch baseline.
   Each approval rule can define a package as approved.

Approval rules, however, are also subject to whether the **Include nonsecurity
updates** check box was selected when creating or last updating a patch
baseline.

If nonsecurity updates are excluded, an implicit rule is applied in order to select only
packages with upgrades in security repos. For each package, the candidate version of the
package (which is typically the latest version) must be part of a security repo.

If nonsecurity updates are included, patches from other repositories are considered as
well. 4. Apply [ApprovedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches") as specified in the patch
baseline. The approved patches are approved for update even if
they're discarded by [GlobalFilters](../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters "../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters") or if no approval rule
specified in [ApprovalRules](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules") grants it approval. 5. Apply [RejectedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches") as specified in the patch
baseline. The rejected patches are removed from the list of
approved patches and won't be applied. 6. If multiple versions of a patch are approved, the latest
version is applied. 7. The YUM update API (Amazon Linux 2) or the DNF update API
(Amazon Linux 2023) is applied to approved patches as follows:

    * For predefined default patch baselines provided by
     AWS, only patches specified in
     `updateinfo.xml` are applied
     (security updates only). This is because the
     **Include nonsecurity updates**
     check box is not selected. The predefined baselines are
     equivalent to a custom baseline with the
     following:




    	+ The **Include nonsecurity
    	 updates** check box is not
    	 selected
    	+ A SEVERITY list of `[Critical,
    	 Important]`
    	+ A CLASSIFICATION list of `[Security,
    	 Bugfix]`
    For Amazon Linux 2, the equivalent yum command for this
     workflow is:



    ```
    sudo yum update-minimal --sec-severity=Critical,Important --bugfix -y
    ```

    For Amazon Linux 2023, the equivalent dnf command for this
     workflow is:



    ```
    sudo dnf upgrade-minimal --sec-severity=Critical --sec-severity=Important --bugfix -y
    ```

    If the **Include nonsecurity
     updates** check box is selected, patches in
     `updateinfo.xml` and those not in
     `updateinfo.xml` are all applied
     (security and nonsecurity updates).


    For Amazon Linux 2, if a baseline with **Include
     nonsecurity updates** is selected, has a
     SEVERITY list of `[Critical, Important]` and
     a CLASSIFICATION list of `[Security,
     Bugfix]`, the equivalent yum command is:



    ```
    sudo yum update --security --sec-severity=Critical,Important --bugfix -y
    ```

    For Amazon Linux 2023, the equivalent dnf command
     is:



    ```
    sudo dnf upgrade --security --sec-severity=Critical --sec-severity=Important --bugfix -y
    ```

    ###### Note

    New packages that replace now-obsolete packages with different names are installed if
     you run these `yum` or `dnf` commands outside of Patch Manager.
     However, they are *not* installed by the equivalent Patch Manager
     operations.



    ###### Additional patching details for
     Amazon Linux 2023



    Support for severity level 'None'

    Amazon Linux 2023 also supports the patch
     severity level `None`, which is
     recognized by the DNF package manager.



    Support for severity level 'Medium'

    For Amazon Linux 2023, a patch severity level of
     `Medium` is equivalent to a severity of
     `Moderate` that might be defined in
     some external repositories. If you include
     `Medium` severity patches in the patch
     baseline, `Moderate` severity patches
     from external patches are also installed on the
     instances.


    When you query for compliance data using the
     API action [DescribeInstancePatches](../APIReference/API_DescribeInstancePatches.md "../APIReference/API_DescribeInstancePatches.md"),
     filtering for the severity level
     `Medium` reports patches with severity
     levels of both `Medium` and
     `Moderate`.



    Transitive dependency handling for
     Amazon Linux 2023

    For Amazon Linux 2023, Patch Manager might install
     different versions of transitive dependencies than
     the equivalent `dnf` commands install.
     Transitive dependencies are packages that are
     automatically installed to satisfy the
     requirements of other packages (dependencies of
     dependencies).


    For example, `dnf upgrade-minimal
     --security` installs the *minimal* versions of
     transitive dependencies needed to resolve known
     security issues, while Patch Manager installs the
     latest available versions
     of the same transitive dependencies.

8. The managed node is rebooted if any updates were installed.
   (Exception: If the `RebootOption` parameter is set to `NoReboot` in
   the `AWS-RunPatchBaseline` document, the managed node isn't rebooted after
   Patch Manager runs. For more information, see [Parameter name: RebootOption](patch-manager-aws-runpatchbaseline.md#patch-manager-aws-runpatchbaseline-parameters-norebootoption "patch-manager-aws-runpatchbaseline.md#patch-manager-aws-runpatchbaseline-parameters-norebootoption").)

###### Note

A default configuration for a package manager on a Linux
distribution might be set to skip an unreachable package repository
without error. In such cases, the related patching operation
proceeds without installing updates from the repository and
concludes with success. To enforce repository updates, add
`skip_if_unavailable=False` to the repository
configuration.

For more information about the `skip_if_available`
option, see [Connectivity to the patch source](patch-manager-prerequisites.md#source-connectivity "patch-manager-prerequisites.md#source-connectivity").

CentOS Stream
On CentOS Stream managed nodes, the patch installation
workflow is as follows:

1. If a list of patches is specified using an https URL or an
   Amazon Simple Storage Service (Amazon S3) path-style URL using the
   `InstallOverrideList` parameter for the
   `AWS-RunPatchBaseline` or
   `AWS-RunPatchBaselineAssociation` documents, the
   listed patches are installed and steps 2-7 are skipped.

Apply [GlobalFilters](../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters "../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters") as specified in the patch baseline,
keeping only the qualified packages for further processing. 2. Apply [ApprovalRules](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules") as specified in the patch baseline.
Each approval rule can define a package as approved.

Approval rules, however, are also subject to whether the **Include nonsecurity
updates** check box was selected when creating or last updating a patch
baseline.

If nonsecurity updates are excluded, an implicit rule is applied in order to select only
packages with upgrades in security repos. For each package, the candidate version of the
package (which is typically the latest version) must be part of a security repo.

If nonsecurity updates are included, patches from other repositories are considered as
well. 3. Apply [ApprovedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches") as specified in the patch
baseline. The approved patches are approved for update even if
they're discarded by [GlobalFilters](../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters "../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters") or if no approval rule
specified in [ApprovalRules](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules") grants it approval. 4. Apply [RejectedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches") as specified in the patch
baseline. The rejected patches are removed from the list of
approved patches and won't be applied. 5. If multiple versions of a patch are approved, the latest
version is applied. 6. The
DNF
update on CentOS Stream is applied to approved
patches.

###### Note

For CentOS Stream, Patch Manager might install different versions
of transitive dependencies than the equivalent
`dnf` commands install. Transitive
dependencies are packages that are automatically installed
to satisfy the requirements of other packages (dependencies
of dependencies).

For example, `dnf upgrade-minimal
 ‐‐security` installs the _minimal_ versions of transitive
dependencies needed to resolve known security issues, while
Patch Manager installs the _latest
available versions_ of the same transitive
dependencies. 7. The managed node is rebooted if any updates were installed.
(Exception: If the `RebootOption` parameter is set to `NoReboot` in
the `AWS-RunPatchBaseline` document, the managed node isn't rebooted after
Patch Manager runs. For more information, see [Parameter name: RebootOption](patch-manager-aws-runpatchbaseline.md#patch-manager-aws-runpatchbaseline-parameters-norebootoption "patch-manager-aws-runpatchbaseline.md#patch-manager-aws-runpatchbaseline-parameters-norebootoption").)

Debian Server
On Debian Server instances, the patch installation workflow is as
follows:

1. If a list of patches is specified using an https URL or an
   Amazon Simple Storage Service (Amazon S3) path-style URL using the
   `InstallOverrideList` parameter for the
   `AWS-RunPatchBaseline` or
   `AWS-RunPatchBaselineAssociation` documents, the
   listed patches are installed and steps 2-7 are skipped.
2. If an update is available for `python3-apt`
   (a Python library interface to `libapt`), it
   is upgraded to the latest version. (This nonsecurity package is
   upgraded even if you did not select the **Include
   nonsecurity updates** option.)
3. Apply [GlobalFilters](../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters "../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters") as specified in the patch baseline,
   keeping only the qualified packages for further processing.
4. Apply [ApprovalRules](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules") as specified in the patch baseline.
   Each approval rule can define a package as approved.

###### Note

Because it isn't possible to reliably determine the release dates of update
packages for Debian Server, the auto-approval options aren't supported for this
operating system.

Approval rules, however, are also subject to whether the **Include nonsecurity
updates** check box was selected when creating or last updating a patch
baseline.

If nonsecurity updates are excluded, an implicit rule is applied in order to select only
packages with upgrades in security repos. For each package, the candidate version of the
package (which is typically the latest version) must be part of a security repo.

If nonsecurity updates are included, patches from other repositories are considered as
well.

###### Note

For Debian Server, patch candidate versions are limited to
patches included in
`debian-security`. 5. Apply [ApprovedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches") as specified in the patch
baseline. The approved patches are approved for update even if
they're discarded by [GlobalFilters](../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters "../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters") or if no approval rule
specified in [ApprovalRules](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules") grants it approval. 6. Apply [RejectedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches") as specified in the patch
baseline. The rejected patches are removed from the list of
approved patches and won't be applied. 7. The APT library is used to upgrade packages.

###### Note

Patch Manager does not support using the APT
`Pin-Priority` option to assign priorities to
packages. Patch Manager aggregates available updates from all
enabled repositories and selects the most recent update that
matches the baseline for each installed package. 8. The managed node is rebooted if any updates were installed.
(Exception: If the `RebootOption` parameter is set to `NoReboot` in
the `AWS-RunPatchBaseline` document, the managed node isn't rebooted after
Patch Manager runs. For more information, see [Parameter name: RebootOption](patch-manager-aws-runpatchbaseline.md#patch-manager-aws-runpatchbaseline-parameters-norebootoption "patch-manager-aws-runpatchbaseline.md#patch-manager-aws-runpatchbaseline-parameters-norebootoption").)

macOS
On macOS managed nodes, the patch installation workflow is as
follows:

1. The
   `/Library/Receipts/InstallHistory.plist`
   property list is a record of software that has been installed
   and upgraded using the `softwareupdate` and
   `installer` package managers. Using the
   `pkgutil` command line tool (for
   `installer`) and the
   `softwareupdate` package manager, CLI
   commands are run to parse this list.

For `installer`, the response to the CLI
commands includes `package name`,
`version`, `volume`,
`location`, and `install-time`
details, but only the `package name` and
`version` are used by Patch Manager.

For `softwareupdate`, the response to the
CLI commands includes the package name (`display
 name`), `version`, and `date`,
but only the package name and version are used by Patch
Manager.

For Brew and Brew Cask, Homebrew doesn't support its commands
running under the root user. As a result, Patch Manager queries for
and runs Homebrew commands as either the owner of the Homebrew
directory or as a valid user belonging to the Homebrew
directory’s owner group. The commands are similar to
`softwareupdate` and
`installer` and are run through a Python
subprocess to gather package data, and the output is parsed to
identify package names and versions. 2. Apply [GlobalFilters](../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters "../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters") as specified in the patch baseline,
keeping only the qualified packages for further processing. 3. Apply [ApprovalRules](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules") as specified in the patch baseline.
Each approval rule can define a package as approved. 4. Apply [ApprovedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches") as specified in the patch
baseline. The approved patches are approved for update even if
they're discarded by [GlobalFilters](../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters "../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters") or if no approval rule
specified in [ApprovalRules](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules") grants it approval. 5. Apply [RejectedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches") as specified in the patch
baseline. The rejected patches are removed from the list of
approved patches and won't be applied. 6. If multiple versions of a patch are approved, the latest
version is applied. 7. Invokes the appropriate package CLI on the managed node to
process approved patches as follows:

###### Note

`installer` lacks the functionality to
check for and install updates. Therefore, for
`installer`, Patch Manager only reports
which packages are installed. As a result,
`installer` packages are never
reported as `Missing`.

    * For predefined default patch baselines provided by
     AWS, and for custom patch baselines where the
     **Include non-security updates**
     check box is *not*
     selected, only security updates are applied.
    * For custom patch baselines where the **Include
     non-security updates** check box *is* selected, both security
     and nonsecurity updates are applied.

8. The managed node is rebooted if any updates were installed.
   (Exception: If the `RebootOption` parameter is set to `NoReboot` in
   the `AWS-RunPatchBaseline` document, the managed node isn't rebooted after
   Patch Manager runs. For more information, see [Parameter name: RebootOption](patch-manager-aws-runpatchbaseline.md#patch-manager-aws-runpatchbaseline-parameters-norebootoption "patch-manager-aws-runpatchbaseline.md#patch-manager-aws-runpatchbaseline-parameters-norebootoption").)

Oracle Linux
On Oracle Linux managed nodes, the patch installation workflow is as
follows:

1. If a list of patches is specified using an https URL or an
   Amazon Simple Storage Service (Amazon S3) path-style URL using the
   `InstallOverrideList` parameter for the
   `AWS-RunPatchBaseline` or
   `AWS-RunPatchBaselineAssociation` documents, the
   listed patches are installed and steps 2-7 are skipped.
2. Apply [GlobalFilters](../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters "../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters") as specified in the patch baseline,
   keeping only the qualified packages for further processing.
3. Apply [ApprovalRules](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules") as specified in the patch baseline.
   Each approval rule can define a package as approved.

Approval rules, however, are also subject to whether the **Include nonsecurity
updates** check box was selected when creating or last updating a patch
baseline.

If nonsecurity updates are excluded, an implicit rule is applied in order to select only
packages with upgrades in security repos. For each package, the candidate version of the
package (which is typically the latest version) must be part of a security repo.

If nonsecurity updates are included, patches from other repositories are considered as
well. 4. Apply [ApprovedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches") as specified in the patch
baseline. The approved patches are approved for update even if
they're discarded by [GlobalFilters](../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters "../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters") or if no approval rule
specified in [ApprovalRules](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules") grants it approval. 5. Apply [RejectedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches") as specified in the patch
baseline. The rejected patches are removed from the list of
approved patches and won't be applied. 6. If multiple versions of a patch are approved, the latest
version is applied. 7. On version 7 managed nodes, the YUM update API is applied to
approved patches as follows:

    * For predefined default patch baselines provided by
     AWS, and for custom patch baselines where the
     **Include non-security updates**
     check box is *not*
     selected, only patches specified in
     `updateinfo.xml` are applied
     (security updates only).


    The equivalent yum command for this workflow
     is:



    ```
    sudo yum update-minimal --sec-severity=Important,Moderate --bugfix -y
    ```
    * For custom patch baselines where the **Include
     non-security updates** check box *is* selected, both patches
     in `updateinfo.xml` and those not in
     `updateinfo.xml` are applied
     (security and nonsecurity updates).


    The equivalent yum command for this workflow
     is:



    ```
    sudo yum update --security --bugfix -y
    ```

    On version 8 and 9 managed nodes, the DNF update API
     is applied to approved patches as follows:




    	+ For predefined default patch baselines
    	 provided by AWS, and for custom patch baselines
    	 where the **Include non-security
    	 updates** check box is *not* selected, only
    	 patches specified in
    	 `updateinfo.xml` are applied
    	 (security updates only).


    	The equivalent yum command for this workflow
    	 is:



    	```
    	sudo dnf upgrade-minimal --security --sec-severity=Moderate --sec-severity=Important
    	```

    	###### Note

    	For Oracle Linux, Patch Manager might install
    	 different versions of transitive dependencies than
    	 the equivalent `dnf` commands install.
    	 Transitive dependencies are packages that are
    	 automatically installed to satisfy the
    	 requirements of other packages (dependencies of
    	 dependencies).

    	For example, `dnf upgrade-minimal
    	 --security` installs the *minimal* versions of
    	 transitive dependencies needed to resolve known
    	 security issues, while Patch Manager installs the
    	 *latest available
    	 versions* of the same transitive
    	 dependencies.
    	+ For custom patch baselines where the
    	 **Include non-security updates**
    	 check box *is*
    	 selected, both patches in
    	 `updateinfo.xml` and those not
    	 in `updateinfo.xml` are applied
    	 (security and nonsecurity updates).


    	The equivalent yum command for this workflow
    	 is:



    	```
    	sudo dnf upgrade --security --bugfix
    	```

###### Note

New packages that replace now-obsolete packages with different names are installed if
you run these `yum` or `dnf` commands outside of Patch Manager.
However, they are _not_ installed by the equivalent Patch Manager
operations. 8. The managed node is rebooted if any updates were installed.
(Exception: If the `RebootOption` parameter is set to `NoReboot` in
the `AWS-RunPatchBaseline` document, the managed node isn't rebooted after
Patch Manager runs. For more information, see [Parameter name: RebootOption](patch-manager-aws-runpatchbaseline.md#patch-manager-aws-runpatchbaseline-parameters-norebootoption "patch-manager-aws-runpatchbaseline.md#patch-manager-aws-runpatchbaseline-parameters-norebootoption").)

###### Note

A default configuration for a package manager on a Linux
distribution might be set to skip an unreachable package repository
without error. In such cases, the related patching operation
proceeds without installing updates from the repository and
concludes with success. To enforce repository updates, add
`skip_if_unavailable=False` to the repository
configuration.

For more information about the `skip_if_available`
option, see [Connectivity to the patch source](patch-manager-prerequisites.md#source-connectivity "patch-manager-prerequisites.md#source-connectivity").

AlmaLinux, RHEL, and Rocky Linux
On AlmaLinux, Red Hat Enterprise Linux, and Rocky Linux managed nodes, the patch
installation workflow is as follows:

1. If a list of patches is specified using an https URL or an
   Amazon Simple Storage Service (Amazon S3) path-style URL using the
   `InstallOverrideList` parameter for the
   `AWS-RunPatchBaseline` or
   `AWS-RunPatchBaselineAssociation` documents, the
   listed patches are installed and steps 2-7 are skipped.
2. Apply [GlobalFilters](../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters "../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters") as specified in the patch baseline,
   keeping only the qualified packages for further processing.
3. Apply [ApprovalRules](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules") as specified in the patch baseline.
   Each approval rule can define a package as approved.

Approval rules, however, are also subject to whether the **Include nonsecurity
updates** check box was selected when creating or last updating a patch
baseline.

If nonsecurity updates are excluded, an implicit rule is applied in order to select only
packages with upgrades in security repos. For each package, the candidate version of the
package (which is typically the latest version) must be part of a security repo.

If nonsecurity updates are included, patches from other repositories are considered as
well. 4. Apply [ApprovedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches") as specified in the patch
baseline. The approved patches are approved for update even if
they're discarded by [GlobalFilters](../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters "../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters") or if no approval rule
specified in [ApprovalRules](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules") grants it approval. 5. Apply [RejectedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches") as specified in the patch
baseline. The rejected patches are removed from the list of
approved patches and won't be applied. 6. If multiple versions of a patch are approved, the latest
version is applied. 7. The YUM update API (on RHEL 7) or the DNF update API (on
AlmaLinux 8 and 9, RHEL 8, 9, and 10, and Rocky Linux 8 and 9) is
applied to approved patches according to the following
rules:

 

###### Scenario 1: Non-security updates excluded

    * **Applies to**:
     Predefined default patch baselines provided by AWS and
     custom patch baselines.
    * **Include non-security updates**
     check box: *Not*
     selected.
    * **Patches applied**:
     Patches specified in `updateinfo.xml`
     (security updates only) are applied *only* if they both match the
     patch baseline configuration and are found in the
     configured repos.


    In some cases, a patch specified in
     `updateinfo.xml` might no longer
     be available in a configured repo. Configured repos
     usually have only the latest version of a patch, which
     is a cumulative roll-up of all prior updates, but the
     latest version might not match the patch baseline rules
     and is omitted from the patching operation.
    * **Commands**: For RHEL
     7, the equivalent yum command for this workflow is:



    ```
    sudo yum update-minimal --sec-severity=Critical,Important --bugfix -y
    ```

    For AlmaLinux, RHEL 8, and Rocky Linux , the equivalent
     dnf commands for this workflow are:



    ```
    sudo dnf update-minimal --sec-severity=Critical --bugfix -y ; \
    sudo dnf update-minimal --sec-severity=Important --bugfix -y
    ```

    ###### Note

    For AlmaLinux, RHEL, and Rocky LinuxRocky Linux,
     Patch Manager might install different versions of
     transitive dependencies than the equivalent
     `dnf` commands install. Transitive
     dependencies are packages that are automatically
     installed to satisfy the requirements of other
     packages (dependencies of dependencies).

    For example, `dnf upgrade-minimal
     --security` installs the *minimal* versions of
     transitive dependencies needed to resolve known
     security issues, while Patch Manager installs the
     *latest available
     versions* of the same transitive
     dependencies.

###### Scenario 2: Non-security updates included

    * **Apples to**: Custom
     patch baselines.
    * **Include non-security updates**
     check box: Selected.
    * **Patches applied**:
     Patches in `updateinfo.xml`
    *and* those not in
     `updateinfo.xml` are applied
     (security and nonsecurity updates).
    * **Commands**: For RHEL
     7, the equivalent yum command for this workflow
     is:



    ```
    sudo yum update --security --bugfix -y
    ```

    For AlmaLinux 8 and 9, RHEL 8 and 9, and Rocky Linux 8
     and 9, the equivalent dnf command for this workflow
     is:



    ```
    sudo dnf update --security --bugfix -y
    ```

###### Note

New packages that replace now-obsolete packages with different names are installed if
you run these `yum` or `dnf` commands outside of Patch Manager.
However, they are _not_ installed by the equivalent Patch Manager
operations. 8. The managed node is rebooted if any updates were installed.
(Exception: If the `RebootOption` parameter is set to `NoReboot` in
the `AWS-RunPatchBaseline` document, the managed node isn't rebooted after
Patch Manager runs. For more information, see [Parameter name: RebootOption](patch-manager-aws-runpatchbaseline.md#patch-manager-aws-runpatchbaseline-parameters-norebootoption "patch-manager-aws-runpatchbaseline.md#patch-manager-aws-runpatchbaseline-parameters-norebootoption").)

###### Note

A default configuration for a package manager on a Linux
distribution might be set to skip an unreachable package repository
without error. In such cases, the related patching operation
proceeds without installing updates from the repository and
concludes with success. To enforce repository updates, add
`skip_if_unavailable=False` to the repository
configuration.

For more information about the `skip_if_available`
option, see [Connectivity to the patch source](patch-manager-prerequisites.md#source-connectivity "patch-manager-prerequisites.md#source-connectivity").

SLES
On SUSE Linux Enterprise Server (SLES) managed nodes, the patch installation workflow
is as follows:

1. If a list of patches is specified using an https URL or an
   Amazon Simple Storage Service (Amazon S3) path-style URL using the
   `InstallOverrideList` parameter for the
   `AWS-RunPatchBaseline` or
   `AWS-RunPatchBaselineAssociation` documents, the
   listed patches are installed and steps 2-7 are skipped.
2. Apply [GlobalFilters](../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters "../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters") as specified in the patch baseline,
   keeping only the qualified packages for further processing.
3. Apply [ApprovalRules](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules") as specified in the patch baseline.
   Each approval rule can define a package as approved.

Approval rules, however, are also subject to whether the **Include nonsecurity
updates** check box was selected when creating or last updating a patch
baseline.

If nonsecurity updates are excluded, an implicit rule is applied in order to select only
packages with upgrades in security repos. For each package, the candidate version of the
package (which is typically the latest version) must be part of a security repo.

If nonsecurity updates are included, patches from other repositories are considered as
well. 4. Apply [ApprovedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches") as specified in the patch
baseline. The approved patches are approved for update even if
they're discarded by [GlobalFilters](../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters "../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters") or if no approval rule
specified in [ApprovalRules](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules") grants it approval. 5. Apply [RejectedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches") as specified in the patch
baseline. The rejected patches are removed from the list of
approved patches and won't be applied. 6. If multiple versions of a patch are approved, the latest
version is applied. 7. The Zypper update API is applied to approved patches. 8. The managed node is rebooted if any updates were installed.
(Exception: If the `RebootOption` parameter is set to `NoReboot` in
the `AWS-RunPatchBaseline` document, the managed node isn't rebooted after
Patch Manager runs. For more information, see [Parameter name: RebootOption](patch-manager-aws-runpatchbaseline.md#patch-manager-aws-runpatchbaseline-parameters-norebootoption "patch-manager-aws-runpatchbaseline.md#patch-manager-aws-runpatchbaseline-parameters-norebootoption").)

Ubuntu Server
On Ubuntu Server managed nodes, the patch installation workflow is as
follows:

1. If a list of patches is specified using an https URL or an
   Amazon Simple Storage Service (Amazon S3) path-style URL using the
   `InstallOverrideList` parameter for the
   `AWS-RunPatchBaseline` or
   `AWS-RunPatchBaselineAssociation` documents, the
   listed patches are installed and steps 2-7 are skipped.
2. If an update is available for `python3-apt`
   (a Python library interface to `libapt`), it
   is upgraded to the latest version. (This nonsecurity package is
   upgraded even if you did not select the **Include
   nonsecurity updates** option.)
3. Apply [GlobalFilters](../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters "../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters") as specified in the patch baseline,
   keeping only the qualified packages for further processing.
4. Apply [ApprovalRules](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules") as specified in the patch baseline.
   Each approval rule can define a package as approved.

###### Note

Because it's not possible to reliably determine the release dates of update
packages for Ubuntu Server, the auto-approval options aren't supported for this
operating system.

Approval rules, however, are also subject to whether the **Include nonsecurity
updates** check box was selected when creating or last updating a patch
baseline.

If nonsecurity updates are excluded, an implicit rule is applied in order to select only
packages with upgrades in security repos. For each package, the candidate version of the
package (which is typically the latest version) must be part of a security repo.

If nonsecurity updates are included, patches from other repositories are considered as
well.

Approval rules, however, are also subject to whether the
**Include nonsecurity updates** check box
was selected when creating or last updating a patch
baseline.

###### Note

For each version of Ubuntu Server, patch candidate versions
are limited to patches that are part of the associated repo
for that version, as follows:

    * Ubuntu Server 16.04 LTS:
     `xenial-security`
    * Ubuntu Server 18.04 LTS:
     `bionic-security`
    * Ubuntu Server 20.04 LTS):
     `focal-security`
    * Ubuntu Server 22.04 LTS:
     `jammy-security`
    * Ubuntu Server 24.04 LTS
     (`noble-security`)
    * Ubuntu Server 25.04
     (`plucky-security`)

5. Apply [ApprovedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovedPatches") as specified in the patch
   baseline. The approved patches are approved for update even if
   they're discarded by [GlobalFilters](../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters "../APIReference/API_CreatePatchBaseline.md#systemsmanager-CreatePatchBaseline-request-GlobalFilters") or if no approval rule
   specified in [ApprovalRules](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-ApprovalRules") grants it approval.
6. Apply [RejectedPatches](../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches "../APIReference/API_CreatePatchBaseline.md#EC2-CreatePatchBaseline-request-RejectedPatches") as specified in the patch
   baseline. The rejected patches are removed from the list of
   approved patches and won't be applied.
7. The APT library is used to upgrade packages.

###### Note

Patch Manager does not support using the APT
`Pin-Priority` option to assign priorities to
packages. Patch Manager aggregates available updates from all
enabled repositories and selects the most recent update that
matches the baseline for each installed package. 8. The managed node is rebooted if any updates were installed.
(Exception: If the `RebootOption` parameter is set to `NoReboot` in
the `AWS-RunPatchBaseline` document, the managed node isn't rebooted after
Patch Manager runs. For more information, see [Parameter name: RebootOption](patch-manager-aws-runpatchbaseline.md#patch-manager-aws-runpatchbaseline-parameters-norebootoption "patch-manager-aws-runpatchbaseline.md#patch-manager-aws-runpatchbaseline-parameters-norebootoption").)

Windows Server
When a patching operation is performed on a Windows Server managed node, the
node requests a snapshot of the appropriate patch baseline from Systems Manager.
This snapshot contains the list of all updates available in the patch
baseline that were approved for deployment. This list of updates is sent
to the Windows Update API, which determines which of the updates are
applicable to the managed node and installs them as needed. Windows
allows only the latest available version of a KB to be installed.
Patch Manager installs the latest version of a KB when it, or any previous
version of the KB, matches the applied patch baseline. If any updates
are installed, the managed node is rebooted afterwards, as many times as
necessary to complete all necessary patching. (Exception: If the `RebootOption` parameter is set to `NoReboot` in
the `AWS-RunPatchBaseline` document, the managed node isn't rebooted after
Patch Manager runs. For more information, see [Parameter name: RebootOption](patch-manager-aws-runpatchbaseline.md#patch-manager-aws-runpatchbaseline-parameters-norebootoption "patch-manager-aws-runpatchbaseline.md#patch-manager-aws-runpatchbaseline-parameters-norebootoption").) The
summary of the patching operation can be found in the output of the
Run Command request. Additional logs can be found on the managed node in
the
`%PROGRAMDATA%\Amazon\PatchBaselineOperations\Logs`
folder.

Because the Windows Update API is used to download and install KBs,
all Group Policy settings for Windows Update are respected. No Group
Policy settings are required to use Patch Manager, but any settings that you
have defined will be applied, such as to direct managed nodes to a
Windows Server Update Services (WSUS) server.

###### Note

By default, Windows downloads all KBs from Microsoft's Windows
Update site because Patch Manager uses the Windows Update API to drive
the download and installation of KBs. As a result, the managed node
must be able to reach the Microsoft Windows Update site or patching
will fail. Alternatively, you can configure a WSUS server to serve
as a KB repository and configure your managed nodes to target that
WSUS server using Group Policies.

Patch Manager might reference KB IDs when creating custom patch
baselines for Windows Server, such as when an **Approved patches** list or **Rejected patches** list is included the the baseline
configuration. Only updates that are assigned a KB ID in Microsoft
Windows Update or a WSUS server are installed by Patch Manager. Updates
that lack a KB ID are not included in patching operations.

For information about creating custom patch baselines, see the
following topics:

- [Creating
  a custom patch baseline for Windows Server](patch-manager-create-a-patch-baseline-for-windows.md "patch-manager-create-a-patch-baseline-for-windows.md")
- [Create a patch baseline (CLI)](patch-manager-create-a-patch-baseline-for-windows.md "patch-manager-create-a-patch-baseline-for-windows.md")
- [Package name formats for Windows operating systems](patch-manager-approved-rejected-package-name-formats.md#patch-manager-approved-rejected-package-name-formats-windows "patch-manager-approved-rejected-package-name-formats.md#patch-manager-approved-rejected-package-name-formats-windows")
