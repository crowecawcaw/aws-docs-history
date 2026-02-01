• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Package name

formats for approved and rejected patch lists

The formats of package names you can add to lists of approved patches and rejected
patches depend on the type of operating system you're patching.

## Package name formats for Linux operating systems

The formats you can specify for approved and rejected patches in your patch
baseline vary by Linux type. More specifically, the formats that are supported
depend on the package manager used by the type of Linux operating system.

###### Topics

- [Amazon Linux 2, Amazon Linux 2023, Oracle Linux, and Red Hat Enterprise Linux (RHEL)](#patch-manager-approved-rejected-package-name-formats-standard "#patch-manager-approved-rejected-package-name-formats-standard")
- [Debian Server and Ubuntu Server](#patch-manager-approved-rejected-package-name-formats-ubuntu "#patch-manager-approved-rejected-package-name-formats-ubuntu")
- [SUSE Linux Enterprise Server (SLES)](#patch-manager-approved-rejected-package-name-formats-sles "#patch-manager-approved-rejected-package-name-formats-sles")

### Amazon Linux 2, Amazon Linux 2023, Oracle Linux, and Red Hat Enterprise Linux (RHEL)

**Package manager**: YUM, except for
Amazon Linux 2023, and RHEL 8, which use DNF as the package manager.

**Approved patches**: For approved patches,
you can specify any of the following:

- Bugzilla IDs, in the format `1234567` (The
  system processes numbers-only strings as Bugzilla IDs.)
- CVE IDs, in the format
  `CVE-2018-1234567`
- Advisory IDs, in formats such as
  `RHSA-2017:0864` and
  `ALAS-2018-123`
- Package names that are constructed using one or more of the
  available components for package naming. To illustrate, for the
  package named
  `dbus.x86_64:1:1.12.28-1.amzn2023.0.1`, the
  components are as follows:

      + `name`: `dbus`
      + `architecture`:
       `x86_64`
      + `epoch`: `1`
      + `version`: `1.12.28`
      + `release`:
       `1.amzn2023.0.1`

  Package names with the following constructions are
  supported:

      + `name`
      + `name.arch`
      + `name-version`
      + `name-version-release`
      + `name-version-release.arch`
      + `version`
      + `version-release`
      + `epoch:version-release`
      + `name-epoch:version-release`
      + `name-epoch:version-release.arch`
      + `epoch:name-version-release.arch`
      + `name.arch:epoch:version-release`

  Some examples:

      + `dbus.x86_64`
      + `dbus-1.12.28`
      + `dbus-1.12.28-1.amzn2023.0.1`
      + `dbus-1:1.12.28-1.amzn2023.0.1.x86_64`

- We also support package name components with a single wild card in
  the above formats, such as the following:
  - `dbus*`
  - `dbus-1.12.2*`
  - `dbus-*:1.12.28-1.amzn2023.0.1.x86_64`

**Rejected patches**: For rejected patches,
you can specify any of the following:

- Package names that are constructed using one or more of the
  available components for package naming. To illustrate, for the
  package named
  `dbus.x86_64:1:1.12.28-1.amzn2023.0.1`, the
  components are as follows:

      + `name`: `dbus`
      + `architecture`;
       `x86_64`
      + `epoch`: `1`
      + `version`: `1.12.28`
      + `release`:
       `1.amzn2023.0.1`

  Package names with the following constructions are
  supported:

      + `name`
      + `name.arch`
      + `name-version`
      + `name-version-release`
      + `name-version-release.arch`
      + `version`
      + `version-release`
      + `epoch:version-release`
      + `name-epoch:version-release`
      + `name-epoch:version-release.arch`
      + `epoch:name-version-release.arch`
      + `name.arch:epoch:version-release`

  Some examples:

      + `dbus.x86_64`
      + `dbus-1.12.28`
      + `dbus-1.12.28-1.amzn2023.0.1`
      + `dbus-1:1.12.28-1.amzn2023.0.1.x86_64`

- We also support package name components with a single wild card in
  the above formats, such as the following:
  - `dbus*`
  - `dbus-1.12.2*`
  - `dbus-*:1.12.28-1.amzn2023.0.1.x86_64`

### Debian Server and Ubuntu Server

**Package manager**: APT

**Approved patches** and **rejected patches**: For both approved and rejected
patches, specify the following:

- Package names, in the format
  `ExamplePkg33`

###### Note

For Debian Server lists, and Ubuntu Server lists, don't include
elements such as architecture or versions. For example, you
specify the package name `ExamplePkg33` to
include all the following in a patch list:

    + `ExamplePkg33.x86.1`
    + `ExamplePkg33.x86.2`
    + `ExamplePkg33.x64.1`
    + `ExamplePkg33.3.2.5-364.noarch`

### SUSE Linux Enterprise Server (SLES)

**Package manager**: Zypper

**Approved patches** and **rejected patches**: For both approved and rejected
patch lists, you can specify any of the following:

- Full package names, in formats such as:
  - `SUSE-SLE-Example-Package-15-2023-123`
  - `example-pkg-2023.15.4-46.17.1.x86_64.rpm`

- Package names with a single wildcard, such as:
  - `SUSE-SLE-Example-Package-15-2023-*`
  - `example-pkg-2023.15.4-46.17.1.*.rpm`

## Package name formats for macOS

**Supported package managers**: softwareupdate,
installer, Brew, Brew Cask

**Approved patches** and **rejected patches**: For both approved and rejected patch lists,
you specify full package names, in formats such as:

- `XProtectPlistConfigData`
- `MRTConfigData`

Wildcards aren't supported in approved and rejected patch lists for
macOS.

## Package name formats for Windows operating systems

For Windows operating systems, specify patches using Microsoft Knowledge Base
IDs and Microsoft Security Bulletin IDs; for example:

```
KB2032276,KB2124261,MS10-048
```
