AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# SSM Command

document for patching: `AWS-RunPatchBaselineAssociation`

Like the `AWS-RunPatchBaseline` document,
`AWS-RunPatchBaselineAssociation` performs patching operations on
instances for both security related and other types of updates. You can also use the
document `AWS-RunPatchBaselineAssociation` to apply patches for both
operating systems and applications. (On Windows Server, application support is limited to
updates for applications released by Microsoft.)

This document supports Amazon Elastic Compute Cloud (Amazon EC2) instances for Linux, macOS, and
Windows Server. It does not support non-EC2 nodes in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment. The
document will perform the appropriate actions for each platform, invoking a Python
module on Linux and macOS instances, and a PowerShell module on Windows
instances.

`AWS-RunPatchBaselineAssociation`, however, differs from
`AWS-RunPatchBaseline` in the following ways:

- `AWS-RunPatchBaselineAssociation` is intended for use primarily
  with State Manager associations created using [Quick Setup](systems-manager-quick-setup.md "systems-manager-quick-setup.md"), a tool in
  AWS Systems Manager. Specifically, when you use the Quick Setup Host Management
  configuration type, if you choose the option **Scan instances for
  missing patches daily**, the system uses
  `AWS-RunPatchBaselineAssociation` for the operation.

In most cases, however, when setting up your own patching operations, you
should choose [AWS-RunPatchBaseline](patch-manager-aws-runpatchbaseline.md "patch-manager-aws-runpatchbaseline.md") or [AWS-RunPatchBaselineWithHooks](patch-manager-aws-runpatchbaselinewithhooks.md "patch-manager-aws-runpatchbaselinewithhooks.md") instead of
`AWS-RunPatchBaselineAssociation`.

- When you use the `AWS-RunPatchBaselineAssociation` document,
  you can specify a tag key pair in the document's `BaselineTags`
  parameter field. If a custom patch baseline in your AWS account shares
  these tags, Patch Manager, a tool in AWS Systems Manager, uses that tagged baseline when it
  runs on the target instances instead of the currently specified "default"
  patch baseline for the operating system type.

###### Note

If you choose to use `AWS-RunPatchBaselineAssociation` in
patching operations other than those set up using Quick Setup, and you want
to use its optional `BaselineTags` parameter, you must
provide some additional permissions to the [instance profile](setup-instance-permissions.md "setup-instance-permissions.md") for
Amazon Elastic Compute Cloud (Amazon EC2) instances. For more information, see [Parameter name: BaselineTags](#patch-manager-aws-runpatchbaselineassociation-parameters-baselinetags "#patch-manager-aws-runpatchbaselineassociation-parameters-baselinetags").

Both of the following formats are valid for your `BaselineTags`
parameter:

`Key=`tag-key`,Values=`tag-value``

`Key=`tag-key`,Values=`tag-value1`,`tag-value2`,`tag-value3``

###### Important

Tag keys and values can't contain the following characters: backtick
(`), single quote ('), double quote ("), and dollar sign ($).

- When `AWS-RunPatchBaselineAssociation` runs, the patch
  compliance data it collects is recorded using the
  `PutComplianceItems` API command instead of the
  `PutInventory` command, which is used by
  `AWS-RunPatchBaseline`. This difference means that the patch
  compliance information that is stored and reported per a specific _association_. Patch compliance data generated
  outside of this association isn't overwritten.
- The patch compliance information reported after running
  `AWS-RunPatchBaselineAssociation` indicates whether or not an
  instance is in compliance. It doesn't include patch-level details, as
  demonstrated by the output of the following AWS Command Line Interface (AWS CLI) command. The
  command filters on `Association` as the compliance type:

```
aws ssm list-compliance-items \
    --resource-ids "i-02573cafcfEXAMPLE" \
    --resource-types "ManagedInstance" \
    --filters "Key=ComplianceType,Values=Association,Type=EQUAL" \
    --region us-east-2
```

The system returns information like the following.

```
{
    "ComplianceItems": [
        {
            "Status": "NON_COMPLIANT",
            "Severity": "UNSPECIFIED",
            "Title": "MyPatchAssociation",
            "ResourceType": "ManagedInstance",
            "ResourceId": "i-02573cafcfEXAMPLE",
            "ComplianceType": "Association",
            "Details": {
                "DocumentName": "AWS-RunPatchBaselineAssociation",
                "PatchBaselineId": "pb-0c10e65780EXAMPLE",
                "DocumentVersion": "1"
            },
            "ExecutionSummary": {
                "ExecutionTime": 1590698771.0
            },
            "Id": "3e5d5694-cd07-40f0-bbea-040e6EXAMPLE"
        }
    ]
}
```

If a tag key pair value has been specified as a parameter for the
`AWS-RunPatchBaselineAssociation` document, Patch Manager searches for a
custom patch baseline that matches the operating system type and has been tagged
with that same tag-key pair. This search isn't limited to the current specified
default patch baseline or the baseline assigned to a patch group. If no baseline is
found with the specified tags, Patch Manager next looks for a patch group, if one was
specified in the command that runs `AWS-RunPatchBaselineAssociation`. If
no patch group is matched, Patch Manager falls back to the current default patch baseline
for the operating system account.

If more than one patch baseline is found with the tags specified in the
`AWS-RunPatchBaselineAssociation` document, Patch Manager returns an error
message indicating that only one patch baseline can be tagged with that key-value
pair in order for the operation to proceed.

###### Note

On Linux nodes, the appropriate package manager for each node type is used to
install packages:

- Amazon Linux 2, Oracle Linux, and RHEL instances use YUM. For YUM operations,
  Patch Manager requires `Python 2.6` or a later supported version
  (2.6 - 3.12). Amazon Linux 2023 uses DNF.
  For DNF operations, Patch Manager requires a supported version of
  `Python 2` or `Python 3`
  (2.6 - 3.12)
- Debian Server and Ubuntu Server instances use APT. For APT operations,
  Patch Manager requires a supported version of `Python 3` (3.0 -
  3.12).
  After a scan is complete, or after all approved and applicable updates have been
  installed, with reboots performed as necessary, patch compliance information is
  generated on an instance and reported back to the Patch Compliance service.

###### Note

If the `RebootOption` parameter is set to `NoReboot` in
the `AWS-RunPatchBaselineAssociation` document, the instance isn't
rebooted after Patch Manager runs. For more information, see [Parameter name: RebootOption](#patch-manager-aws-runpatchbaselineassociation-parameters-norebootoption "#patch-manager-aws-runpatchbaselineassociation-parameters-norebootoption").

For information about viewing patch compliance data, see [About patch compliance](compliance-about.md#compliance-monitor-patch "compliance-about.md#compliance-monitor-patch").

## `AWS-RunPatchBaselineAssociation` parameters

`AWS-RunPatchBaselineAssociation` supports five parameters. The
`Operation` and `AssociationId` parameters are
required. The `InstallOverrideList`, `RebootOption`, and
`BaselineTags` parameters are optional.

###### Parameters

- [Parameter name: Operation](#patch-manager-aws-runpatchbaselineassociation-parameters-operation "#patch-manager-aws-runpatchbaselineassociation-parameters-operation")
- [Parameter name: BaselineTags](#patch-manager-aws-runpatchbaselineassociation-parameters-baselinetags "#patch-manager-aws-runpatchbaselineassociation-parameters-baselinetags")
- [Parameter name: AssociationId](#patch-manager-aws-runpatchbaselineassociation-parameters-association-id "#patch-manager-aws-runpatchbaselineassociation-parameters-association-id")
- [Parameter name: InstallOverrideList](#patch-manager-aws-runpatchbaselineassociation-parameters-installoverridelist "#patch-manager-aws-runpatchbaselineassociation-parameters-installoverridelist")
- [Parameter name: RebootOption](#patch-manager-aws-runpatchbaselineassociation-parameters-norebootoption "#patch-manager-aws-runpatchbaselineassociation-parameters-norebootoption")

### Parameter name: `Operation`

**Usage**: Required.

**Options**: `Scan` |
`Install`.

Scan

When you choose the `Scan` option,
`AWS-RunPatchBaselineAssociation` determines the
patch compliance state of the instance and reports this
information back to Patch Manager. `Scan` doesn't prompt
updates to be installed or instances to be rebooted. Instead,
the operation identifies where updates are missing that are
approved and applicable to the instance.

Install

When you choose the `Install` option,
`AWS-RunPatchBaselineAssociation` attempts to
install the approved and applicable updates that are missing
from the instance. Patch compliance information generated as
part of an `Install` operation doesn't list any
missing updates, but might report updates that are in a failed
state if the installation of the update didn't succeed for any
reason. Whenever an update is installed on an instance, the
instance is rebooted to ensure the update is both installed and
active. (Exception: If the `RebootOption` parameter
is set to `NoReboot` in the
`AWS-RunPatchBaselineAssociation` document, the
instance isn't rebooted after Patch Manager runs. For more
information, see [Parameter name: RebootOption](#patch-manager-aws-runpatchbaselineassociation-parameters-norebootoption "#patch-manager-aws-runpatchbaselineassociation-parameters-norebootoption").)

###### Note

If a patch specified by the baseline rules is installed
_before_ Patch Manager updates the
instance, the system might not reboot as expected. This can
happen when a patch is installed manually by a user or
installed automatically by another program, such as the
`unattended-upgrades` package on
Ubuntu Server.

### Parameter name: `BaselineTags`

**Usage**: Optional.

`BaselineTags` is a unique tag key-value pair that you choose
and assign to an individual custom patch baseline. You can specify one or
more values for this parameter. Both of the following formats are
valid:

`Key=`tag-key`,Values=`tag-value``

`Key=`tag-key`,Values=`tag-value1`,`tag-value2`,`tag-value3``

###### Important

Tag keys and values can't contain the following characters: backtick
(`), single quote ('), double quote ("), and dollar sign ($).

The `BaselineTags` value is used by Patch Manager to ensure that a
set of instances that are patched in a single operation all have the exact
same set of approved patches. When
the patching operation runs, Patch Manager checks
to see if a patch baseline for the operating system type is tagged with the
same key-value pair you specify for `BaselineTags`. If there is a
match, this custom patch baseline is used. If there isn't a match, a patch
baseline is identified according to any patch group specified for the
patching operating. If there is none, the AWS managed predefined patch
baseline for that operating system is used.

###### Additional permission requirements

If you use `AWS-RunPatchBaselineAssociation` in patching
operations other than those set up using Quick Setup, and you want to use
the optional `BaselineTags` parameter, you must add the
following permissions to the [instance profile](setup-instance-permissions.md "setup-instance-permissions.md") for Amazon Elastic Compute Cloud (Amazon EC2) instances.

###### Note

Quick Setup and `AWS-RunPatchBaselineAssociation` don't
support on-premises servers and virtual machines (VMs).

```
{
    "Effect": "Allow",
    "Action": [
        "ssm:DescribePatchBaselines",
        "tag:GetResources"
    ],
    "Resource": "*"
},
{
    "Effect": "Allow",
    "Action": [
        "ssm:GetPatchBaseline",
        "ssm:DescribeEffectivePatchesForPatchBaseline"
    ],
    "Resource": "`patch-baseline-arn`"
}
```

Replace `patch-baseline-arn` with the Amazon
Resource Name (ARN) of the patch baseline to which you want to provide
access, in the format
`arn:aws:ssm:us-east-2:123456789012:patchbaseline/pb-0c10e65780EXAMPLE`.

### Parameter name: `AssociationId`

**Usage**: Required.

`AssociationId` is the ID of an existing association in
State Manager, a tool in AWS Systems Manager. It's used by Patch Manager to add compliance data
to a specified association. This association is related to a patch
`Scan` operation enabled in a [Host Management configuration
created in Quick Setup](quick-setup-host-management.md "quick-setup-host-management.md"). By sending patching results as association
compliance data instead of inventory compliance data, existing inventory
compliance information for your instances isn't overwritten after a patching
operation, nor for other association IDs.
If you don't already
have an association you want to use, you can create one by running
[create-association](../../../cli/latest/reference/ssm/create-association.md "../../../cli/latest/reference/ssm/create-association.md") the command. For example:

Linux & macOS

```
aws ssm create-association \
    --name "AWS-RunPatchBaselineAssociation" \
    --association-name "MyPatchHostConfigAssociation" \
    --targets "Key=instanceids,Values=[i-02573cafcfEXAMPLE,i-07782c72faEXAMPLE,i-07782c72faEXAMPLE]" \
    --parameters "Operation=Scan" \
    --schedule-expression "cron(0 */30 * * * ? *)" \
    --sync-compliance "MANUAL" \
    --region us-east-2
```

Windows Server

```
aws ssm create-association ^
    --name "AWS-RunPatchBaselineAssociation" ^
    --association-name "MyPatchHostConfigAssociation" ^
    --targets "Key=instanceids,Values=[i-02573cafcfEXAMPLE,i-07782c72faEXAMPLE,i-07782c72faEXAMPLE]" ^
    --parameters "Operation=Scan" ^
    --schedule-expression "cron(0 */30 * * * ? *)" ^
    --sync-compliance "MANUAL" ^
    --region us-east-2
```

### Parameter name: `InstallOverrideList`

**Usage**: Optional.

Using `InstallOverrideList`, you specify an https URL or an
Amazon Simple Storage Service (Amazon S3) path-style URL to a list of patches to be installed. This
patch installation list, which you maintain in YAML format, overrides the
patches specified by the current default patch baseline. This provides you
with more granular control over which patches are installed on your
instances.

###### Important

The `InstallOverrideList` file name can't contain the
following characters: backtick (`), single quote ('), double quote ("),
and dollar sign ($).

The patching operation behavior when using the
`InstallOverrideList` parameter differs between Linux & macOS
managed nodes and Windows Server managed nodes. On Linux & macOS, Patch Manager
attempts to apply patches included in the `InstallOverrideList`
patch list that are present in any repository enabled on the node, whether
or not the patches match the patch baseline rules. On Windows Server nodes,
however, patches in the `InstallOverrideList` patch list are
applied _only_ if they also match the patch
baseline rules.

Be aware that compliance reports reflect patch states according to what’s
specified in the patch baseline, not what you specify in an
`InstallOverrideList` list of patches. In other words, Scan
operations ignore the `InstallOverrideList` parameter. This is to
ensure that compliance reports consistently reflect patch states according
to policy rather than what was approved for a specific patching operation.

**Valid URL formats**

###### Note

If your file is stored in a publicly available bucket, you can specify
either an https URL format or an Amazon S3 path-style URL. If your file is
stored in a private bucket, you must specify an Amazon S3 path-style
URL.

- **https URL format example**:

```
https://s3.amazonaws.com/amzn-s3-demo-bucket/my-windows-override-list.yaml
```

- **Amazon S3 path-style URL
  example**:

```
s3://amzn-s3-demo-bucket/my-windows-override-list.yaml
```

**Valid YAML content formats**

The formats you use to specify patches in your list depends on the
operating system of your instance. The general format, however, is as
follows:

```
patches:
    -
        id: '{patch-d}'
        title: '{patch-title}'
        {`additional-fields`}:{`values`}
```

Although you can provide additional fields in your YAML file, they're
ignored during patch operations.

In addition, we recommend verifying that the format of your YAML file is
valid before adding or updating the list in your S3 bucket. For more
information about the YAML format, see [yaml.org](http://www.yaml.org "http://www.yaml.org"). For validation tool options, perform a web search for
"yaml format validators".

- Microsoft Windows

###### id

The **id** field is required. Use
it to specify patches using Microsoft Knowledge Base IDs (for
example, KB2736693) and Microsoft Security Bulletin IDs (for
example, MS17-023).

Any other fields you want to provide in a patch list for Windows
are optional and are for your own informational use only. You can
use additional fields such as **title**, **classification**,
**severity**, or anything else for
providing more detailed information about the specified
patches.

- Linux

###### id

The **id** field is required. Use
it to specify patches using the package name and architecture.
For example: `'dhclient.x86_64'`. You can use
wildcards in id to indicate multiple packages. For example:
`'dhcp*'` and `'dhcp*1.*'`.

###### title

The **title** field is optional,
but on Linux systems it does provide additional filtering
capabilities. If you use **title**,
it should contain the package version information in the one of
the following formats:

YUM/Red Hat Enterprise Linux (RHEL):

```
{name}.{architecture}:{epoch}:{version}-{release}
```

APT

```
{name}.{architecture}:{version}
```

For Linux patch titles, you can use one or more wildcards in any
position to expand the number of package matches. For example:
`'*32:9.8.2-0.*.rc1.57.amzn1'`.

For example:

    + apt package version 1.2.25 is currently installed on your
     instance, but version 1.2.27 is now available.
    + You add apt.amd64 version 1.2.27 to the patch list. It
     depends on apt utils.amd64 version 1.2.27, but
     apt-utils.amd64 version 1.2.25 is specified in the list.

In this case, apt version 1.2.27 will be blocked from installation
and reported as “Failed-NonCompliant.”

###### Other fields

Any other fields you want to provide in a patch list for Linux are
optional and are for your own informational use only. You can use
additional fields such as **classification**, **severity**, or anything else for providing more detailed
information about the specified patches.

**Sample patch lists**

- **Windows**

```
patches:
    -
        id: 'KB4284819'
        title: '2018-06 Cumulative Update for Windows Server 2016 (1709) for x64-based Systems (KB4284819)'
    -
        id: 'KB4284833'
    -
        id: 'KB4284835'
        title: '2018-06 Cumulative Update for Windows Server 2016 (1803) for x64-based Systems (KB4284835)'
    -
        id: 'KB4284880'
    -
        id: 'KB4338814'

```

- **APT**

```
patches:
    -
        id: 'apparmor.amd64'
        title: '2.10.95-0ubuntu2.9'
    -
        id: 'cryptsetup.amd64'
        title: '*2:1.6.6-5ubuntu2.1'
    -
        id: 'cryptsetup-bin.*'
        title: '*2:1.6.6-5ubuntu2.1'
    -
        id: 'apt.amd64'
        title: '*1.2.27'
    -
        id: 'apt-utils.amd64'
        title: '*1.2.25'

```

- **Amazon Linux 2**

```
patches:
    -
        id: 'kernel.x86_64'
    -
        id: 'bind*.x86_64'
        title: '39.11.4-26.P2.amzn2.5.2'

        id: 'glibc*'
    -
        id: 'dhclient*'
        title: '*4.2.5-58.amzn2'
    -
        id: 'dhcp*'
        title: '*4.2.5-77.amzn2'

```

- **Red Hat Enterprise Linux (RHEL)**

```
patches:
    -
        id: 'NetworkManager.x86_64'
        title: '*1:1.10.2-14.el7_5'
    -
        id: 'NetworkManager-*.x86_64'
        title: '*1:1.10.2-14.el7_5'
    -
        id: 'audit.x86_64'
        title: '*0:2.8.1-3.el7'
    -
        id: 'dhclient.x86_64'
        title: '*.el7_5.1'
    -
        id: 'dhcp*.x86_64'
        title: '*12:5.2.5-68.el7'

```

- **SUSE Linux Enterprise Server (SLES)**

```
patches:
    -
        id: 'amazon-ssm-agent.x86_64'
    -
        id: 'binutils'
        title: '*0:2.26.1-9.12.1'
    -
        id: 'glibc*.x86_64'
        title: '*2.19*'
    -
        id: 'dhcp*'
        title: '0:4.3.3-9.1'
    -
        id: 'lib*'


```

- **Ubuntu Server**

```
patches:
    -
        id: 'apparmor.amd64'
        title: '2.10.95-0ubuntu2.9'
    -
        id: 'cryptsetup.amd64'
        title: '*2:1.6.6-5ubuntu2.1'
    -
        id: 'cryptsetup-bin.*'
        title: '*2:1.6.6-5ubuntu2.1'
    -
        id: 'apt.amd64'
        title: '*1.2.27'
    -
        id: 'apt-utils.amd64'
        title: '*1.2.25'

```

- **Windows**

```
patches:
    -
        id: 'KB4284819'
        title: '2018-06 Cumulative Update for Windows Server 2016 (1709) for x64-based Systems (KB4284819)'
    -
        id: 'KB4284833'
    -
        id: 'KB4284835'
        title: '2018-06 Cumulative Update for Windows Server 2016 (1803) for x64-based Systems (KB4284835)'
    -
        id: 'KB4284880'
    -
        id: 'KB4338814'

```

### Parameter name: `RebootOption`

**Usage**: Optional.

**Options**: `RebootIfNeeded` |
`NoReboot`

**Default**:
`RebootIfNeeded`

###### Warning

The default option is `RebootIfNeeded`. Be sure to select
the correct option for your use case. For example, if your instances
must reboot immediately to complete a configuration process, choose
`RebootIfNeeded`. Or, if you need to maintain instances
availability until a scheduled reboot time, choose
`NoReboot`.

###### Important

The `NoReboot` option only prevents operating system-level
restarts. Service-level restarts can still occur as part of the patching
process. For example, when Docker is updated, dependent services such as
Amazon Elastic Container Service might automatically restart even with `NoReboot`
enabled. If you have critical services that must not be disrupted,
consider additional measures such as temporarily removing instances from
service or scheduling patching during maintenance windows.

###### Important

We don’t recommend using Patch Manager for patching cluster instances in Amazon EMR
(previously called Amazon Elastic MapReduce). In particular, don’t select the
`RebootIfNeeded` option for the `RebootOption` parameter.
(This option is available in the SSM Command documents for patching
`AWS-RunPatchBaseline`, `AWS-RunPatchBaselineAssociation`, and
`AWS-RunPatchBaselineWithHooks`.)

The underlying commands for patching using Patch Manager use `yum` and
`dnf` commands. Therefore, the operations result in incompatibilities
because of how packages are installed. For information about the preferred methods for
updating software on Amazon EMR clusters, see [Using the default AMI for
Amazon EMR](../../../emr/latest/ManagementGuide/emr-default-ami.md "../../../emr/latest/ManagementGuide/emr-default-ami.md") in the _Amazon EMR Management Guide_.

RebootIfNeeded

When you choose the `RebootIfNeeded` option, the
instance is rebooted in either of the following cases:

- Patch Manager installed one or more patches.

Patch Manager doesn't evaluate whether a reboot is
_required_ by the
patch. The system is rebooted even if the patch doesn't
require a reboot.

- Patch Manager detects one or more patches with a status of
  `INSTALLED_PENDING_REBOOT` during the
  `Install` operation.

The `INSTALLED_PENDING_REBOOT` status can
mean that the option `NoReboot` was selected
the last time the `Install` operation was
run, or that a patch was installed outside of Patch Manager
since the last time the managed node was
rebooted.

Rebooting instances in these two cases ensures that updated
packages are flushed from memory and keeps patching and
rebooting behavior consistent across all operating
systems.

NoReboot

When you choose the `NoReboot` option, Patch Manager
doesn't reboot an instance even if it installed patches during
the `Install` operation. This option is useful if you
know that your instances don't require rebooting after patches
are applied, or you have applications or processes running on an
instance that shouldn't be disrupted by a patching operation
reboot. It's also useful when you want more control over the
timing of instance reboots, such as by using a maintenance
window.

**Patch installation tracking file**: To
track patch installation, especially patches that have been installed since
the last system reboot, Systems Manager maintains a file on the managed
instance.

###### Important

Don't delete or modify the tracking file. If this file is deleted or
corrupted, the patch compliance report for the instance is inaccurate.
If this happens, reboot the instance and run a patch Scan operation to
restore the file.

This tracking file is stored in the following locations on your managed
instances:

- Linux operating systems:
  - `/var/log/amazon/ssm/patch-configuration/patch-states-configuration.json`
  - `/var/log/amazon/ssm/patch-configuration/patch-inventory-from-last-operation.json`

- Windows Server operating system:
  - `C:\ProgramData\Amazon\PatchBaselineOperations\State\PatchStatesConfiguration.json`
  - `C:\ProgramData\Amazon\PatchBaselineOperations\State\PatchInventoryFromLastOperation.json`
