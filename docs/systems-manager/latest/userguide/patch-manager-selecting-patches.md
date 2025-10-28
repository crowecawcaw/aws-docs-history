# How security patches are

selected

The primary focus of Patch Manager, a tool in AWS Systems Manager, is on installing operating
systems security-related updates on managed nodes. By default, Patch Manager doesn't
install all available patches, but rather a smaller set of patches focused on
security.

By default, Patch Manager doesn't replace a package that has been marked as obsolete in
a package repository with any differently named replacement packages unless this
replacement is required by the installation of another package update. Instead, for
commands that update a package, Patch Manager only reports and installs missing updates
for the package that is installed but obsolete. This is because replacing an
obsolete package typically requires uninstalling an existing package and installing
its replacement. Replacing the obsolete package could introduce breaking changes or
additional functionality that you didn't intend.

This behavior is consistent with YUM and DNF's `update-minimal`
command, which focuses on security updates rather than feature upgrades. For more
information, see [How patches are installed](patch-manager-installing-patches.md "patch-manager-installing-patches.md").

###### Note

When you use the `ApproveUntilDate` parameter or
`ApproveAfterDays` parameter in a patch baseline rule, Patch Manager
evaluates patch release dates using Coordinated Universal Time (UTC).

For example, for `ApproveUntilDate`, if you specify a date such as
`2025-11-16`, patches released between
`2025-11-16T00:00:00Z` and `2025-11-16T23:59:59Z` will
be approved.

Be aware that patch release dates displayed by native package managers on your
managed nodes may show different times based on your system's local timezone,
but Patch Manager always uses the UTC datetime for approval calculations. This
ensures consistency with patch release dates published on official security
advisory websites.

For Linux-based operating system types that report a severity level for patches,
Patch Manager uses the severity level reported by the software publisher for the update
notice or individual patch. Patch Manager doesn't derive severity levels from third-party
sources, such as the [Common Vulnerability
Scoring System](https://www.first.org/cvss/ "https://www.first.org/cvss/") (CVSS), or from metrics released by the [National Vulnerability Database](https://nvd.nist.gov/vuln "https://nvd.nist.gov/vuln")
(NVD).

###### Note

On all Linux-based systems supported by Patch Manager, you can choose a different
source repository configured for the managed node, typically to install
nonsecurity updates. For information, see [How to specify an
alternative patch source repository (Linux)](patch-manager-alternative-source-repository.md "patch-manager-alternative-source-repository.md").

Choose from the following tabs to learn how Patch Manager selects
security patches for your operating system.

Amazon Linux 2 and Amazon Linux 2023
Preconfigured repositories are handled differently on Amazon Linux 2 than on
Amazon Linux 2023.

On Amazon Linux 2, the Systems Manager patch baseline service uses preconfigured
repositories on the managed node. There are usually two preconfigured
repositories (repos) on a node:

###### On Amazon Linux 2

- **Repo ID**:
  `amzn2-core/2/`architecture``

**Repo name**: `Amazon Linux 2
 core repository`

- **Repo ID**:
  `amzn2extra-docker/2/`architecture``

**Repo name**: `Amazon
 Extras repo for docker`

###### Note

`architecture` can be x86_64 or (for
Graviton processors) aarch64.

When you create an Amazon Linux 2023 (AL2023) instance, it contains the
updates that were available in the version of AL2023 and the specific
AMI you selected. Your AL2023 instance doesn't automatically receive
additional critical and important security updates at launch time.
Instead, with the _deterministic upgrades through
versioned repositories_ feature supported for AL2023,
which is turned on by default, you can apply updates based on a schedule
that meets your specific needs. For more information, see [Deterministic
upgrades through versioned repositories](../../../linux/al2023/ug/deterministic-upgrades.md "../../../linux/al2023/ug/deterministic-upgrades.md") in the
_Amazon Linux 2023 User Guide_.

On AL2023, the preconfigured repository is the following:

- **Repo ID**:
  `amazonlinux`

**Repo name**: Amazon Linux 2023
repository

On Amazon Linux 2023 (preview release), the preconfigured repositories are
tied to _locked versions_ of package
updates. When new Amazon Machine Images (AMIs) for AL2023 are released,
they are locked to a specific version. For patch updates, Patch Manager
retrieves the latest locked version of the patch update repository and
then updates packages on the managed node based on the content of that
locked version.

###### Package managers

Amazon Linux 2 managed nodes use Yum as the package manager. Amazon Linux 2023
use DNF as the package manager.

Both package managers use the concept of an _update notice_ as a file named
`updateinfo.xml`. An update notice is simply a
collection of packages that fix specific problems. All packages that are
in an update notice are considered Security by Patch Manager. Individual
packages aren't assigned classifications or severity levels. For this
reason, Patch Manager assigns the attributes of an update notice to the
related packages.

###### Note

If you select the **Include non-security
updates** check box in the **Create patch
baseline** page, then packages that aren't classified
in an `updateinfo.xml` file (or a package that
contains a file without properly formatted Classification, Severity,
and Date values) can be included in the prefiltered list of patches.
However, in order for a patch to be applied, the patch must still
meet the user-specified patch baseline rules.

For more information about the **Include non-security
updates** option, see [How patches are installed](patch-manager-installing-patches.md "patch-manager-installing-patches.md") and [How patch baseline rules work on
Linux-based systems](patch-manager-linux-rules.md "patch-manager-linux-rules.md").

CentOS Stream
On CentOS Stream, the Systems Manager patch baseline service uses
preconfigured repositories (repos) on the managed node. The following
list provides examples for a fictitious CentOS 9.2 Amazon Machine Image
(AMI):

- **Repo ID**:
  `example-centos-9.2-base`

**Repo name**: `Example
 CentOS-9.2 - Base`

- **Repo ID**:
  `example-centos-9.2-extras`

**Repo name**: `Example
 CentOS-9.2 - Extras`

- **Repo ID**:
  `example-centos-9.2-updates`

**Repo name**: `Example
 CentOS-9.2 - Updates`

- **Repo ID**:
  `example-centos-9.x-examplerepo`

**Repo name**: `Example
 CentOS-9.x – Example Repo Packages`

###### Note

All updates are downloaded from the remote repos configured on the
managed node. Therefore, the node must have outbound access to the
internet in order to connect to the repos so the patching can be
performed.

CentOS Stream
nodes use DNF as the package manager. The package manager uses the
concept of an update notice. An update notice is simply a collection of
packages that fix specific problems.

However, CentOS Stream default repos aren't configured
with an update notice. This means that Patch Manager doesn't detect packages
on default CentOS Stream repos. To allow Patch Manager to
process packages that aren't contained in an update notice, you must
turn on the `EnableNonSecurity` flag in the patch baseline
rules.

###### Note

CentOS Stream update notices are supported. Repos
with update notices can be downloaded after launch.

Debian Server
On Debian Server, the Systems Manager patch baseline service uses preconfigured
repositories (repos) on the instance. These preconfigured repos are used
to pull an updated list of available package upgrades. For this, Systems Manager
performs the equivalent of a `sudo apt-get update` command.

Packages are then filtered from `debian-security
 `codename`` repos. This means
that on each version of Debian Server, Patch Manager only identifies upgrades
that are part of the associated repo for that version, as
follows:

- Debian Server 11: `debian-security
bullseye`
- Debian Server 12: `debian-security
bookworm`

Oracle Linux
On Oracle Linux, the Systems Manager patch baseline service uses preconfigured
repositories (repos) on the managed node. There are usually two
preconfigured repos on a node.

**Oracle Linux 7**:

- **Repo ID**:
  `ol7_UEKR5/x86_64`

**Repo name**: `Latest
 Unbreakable Enterprise Kernel Release 5 for Oracle Linux
 7Server (x86_64)`

- **Repo ID**:
  `ol7_latest/x86_64`

**Repo name**:
`Oracle Linux 7Server Latest (x86_64)`

**Oracle Linux 8**:

- **Repo ID**:
  `ol8_baseos_latest`

**Repo name**:
`Oracle Linux 8 BaseOS Latest
 (x86_64)`

- **Repo ID**:
  `ol8_appstream`

**Repo name**:
`Oracle Linux 8 Application Stream
 (x86_64)`

- **Repo ID**:
  `ol8_UEKR6`

**Repo name**: `Latest
 Unbreakable Enterprise Kernel Release 6 for Oracle Linux 8
 (x86_64)`

**Oracle Linux 9**:

- **Repo ID**:
  `ol9_baseos_latest`

**Repo name**:
`Oracle Linux 9 BaseOS Latest
 (x86_64)`

- **Repo ID**:
  `ol9_appstream`

**Repo name**:
`Oracle Linux 9 Application Stream
 Packages(x86_64)`

- **Repo ID**:
  `ol9_UEKR7`

**Repo name**:
`Oracle Linux UEK Release 7
 (x86_64)`

###### Note

All updates are downloaded from the remote repos configured on the
managed node. Therefore, the node must have outbound access to the
internet in order to connect to the repos so the patching can be
performed.

Oracle Linux managed nodes use Yum as the package manager, and Yum uses
the concept of an update notice as a file named
`updateinfo.xml`. An update notice is simply a
collection of packages that fix specific problems. Individual packages
aren't assigned classifications or severity levels. For this reason,
Patch Manager assigns the attributes of an update notice to the related
packages and installs packages based on the Classification filters
specified in the patch baseline.

###### Note

If you select the **Include non-security
updates** check box in the **Create patch
baseline** page, then packages that aren't classified
in an `updateinfo.xml` file (or a package that
contains a file without properly formatted Classification, Severity,
and Date values) can be included in the prefiltered list of patches.
However, in order for a patch to be applied, the patch must still
meet the user-specified patch baseline rules.

AlmaLinux, RHEL, and Rocky Linux
On AlmaLinux, Red Hat Enterprise Linux, and Rocky Linux the Systems Manager patch baseline service
uses preconfigured repositories (repos) on the managed node. There are
usually three preconfigured repos on a node.

All updates are downloaded from the remote repos configured on the
managed node. Therefore, the node must have outbound access to the
internet in order to connect to the repos so the patching can be
performed.

###### Note

If you select the **Include non-security
updates** check box in the **Create patch
baseline** page, then packages that aren't classified
in an `updateinfo.xml` file (or a package that
contains a file without properly formatted Classification, Severity,
and Date values) can be included in the prefiltered list of patches.
However, in order for a patch to be applied, the patch must still
meet the user-specified patch baseline rules.

Red Hat Enterprise Linux 7 managed nodes use Yum as the package manager. AlmaLinux,
Red Hat Enterprise Linux 8, and Rocky Linux managed nodes use DNF as the package manager.
Both package managers use the concept of an update notice as a file
named `updateinfo.xml`. An update notice is simply a
collection of packages that fix specific problems. Individual packages
aren't assigned classifications or severity levels. For this reason,
Patch Manager assigns the attributes of an update notice to the related
packages and installs packages based on the Classification filters
specified in the patch baseline.

RHEL 7

###### Note

The following repo IDs are associated with RHUI 2.
RHUI 3 launched in December 2019 and introduced a
different naming scheme for Yum repository IDs.
Depending on the RHEL-7 AMI you create your managed
nodes from, you might need to update your commands. For
more information, see [Repository IDs for RHEL 7 in AWS Have
Changed](https://access.redhat.com/articles/4599971 "https://access.redhat.com/articles/4599971") on the _Red Hat Customer
Portal_.

- **Repo ID**:
  `rhui-REGION-client-config-server-7/x86_64`

**Repo name**:
`Red Hat Update Infrastructure 2.0 Client
 Configuration Server 7`

- **Repo ID**:
  `rhui-REGION-rhel-server-releases/7Server/x86_64`

**Repo name**:
`Red Hat Enterprise Linux Server 7
 (RPMs)`

- **Repo ID**:
  `rhui-REGION-rhel-server-rh-common/7Server/x86_64`

**Repo name**:
`Red Hat Enterprise Linux Server 7 RH Common
 (RPMs)`

AlmaLinux, 8 RHEL 8, and Rocky Linux 8

- **Repo ID**:
  `rhel-8-appstream-rhui-rpms`

**Repo name**:
`Red Hat Enterprise Linux 8 for x86_64 - AppStream from
 RHUI (RPMs)`

- **Repo ID**:
  `rhel-8-baseos-rhui-rpms`

**Repo name**:
`Red Hat Enterprise Linux 8 for x86_64 - BaseOS from
 RHUI (RPMs)`

- **Repo ID**:
  `rhui-client-config-server-8`

**Repo name**:
`Red Hat Update Infrastructure 3 Client
 Configuration Server 8`

AlmaLinux 9, RHEL 9, and Rocky Linux 9

- **Repo ID**:
  `rhel-9-appstream-rhui-rpms`

**Repo name**:
`Red Hat Enterprise Linux 9 for x86_64 - AppStream from
 RHUI (RPMs)`

- **Repo ID**:
  `rhel-9-baseos-rhui-rpms`

**Repo name**:
`Red Hat Enterprise Linux 9 for x86_64 - BaseOS from
 RHUI (RPMs)`

- **Repo ID**:
  `rhui-client-config-server-9`

**Repo name**:
`Red Hat Enterprise Linux 9 Client
 Configuration`

SLES
On SUSE Linux Enterprise Server (SLES) managed nodes, the ZYPP library gets the list
of available patches (a collection of packages) from the following
locations:

- List of repositories:
  `etc/zypp/repos.d/*`
- Package information:
  `/var/cache/zypp/raw/*`

SLES managed nodes use Zypper as the package manager, and Zypper
uses the concept of a patch. A patch is simply a collection of packages
that fix a specific problem. Patch Manager handles all packages referenced in
a patch as security-related. Because individual packages aren't given
classifications or severity, Patch Manager assigns the packages the
attributes of the patch that they belong to.

Ubuntu Server
On Ubuntu Server, the Systems Manager patch baseline service uses preconfigured
repositories (repos) on the managed node. These preconfigured repos are
used to pull an updated list of available package upgrades. For this,
Systems Manager performs the equivalent of a `sudo apt-get update`
command.

Packages are then filtered from
``codename`-security`  repos, where the codename is unique to the release version, such as
 `trusty` for Ubuntu Server 14. Patch Manager only identifies
upgrades that are part of these repos:

-
- Ubuntu Server 16.04 LTS:
  `xenial-security`
- Ubuntu Server 18.04 LTS:
  `bionic-security`
- Ubuntu Server 20.04 LTS:
  `focal-security`
-
- Ubuntu Server 22.04 LTS
  (`jammy-security`)
-
-
- Ubuntu Server 24.04 LTS
  (`noble-security`)
-
- Ubuntu Server 25.04
  (`plucky-security`)

Windows Server
On Microsoft Windows operating systems, Patch Manager retrieves a list of
available updates that Microsoft publishes to Microsoft Update and are
automatically available to Windows Server Update Services (WSUS).

###### Note

Patch Manager only makes available patches for Windows Server operating
system versions that are supported for Patch Manager. For example,
Patch Manager can't be used to patch Windows RT.

Patch Manager continually monitors for new updates in every AWS Region.
The list of available updates is refreshed in each Region at least once
per day. When the patch information from Microsoft is processed,
Patch Manager removes updates that were replaced by later updates from its
patch list . Therefore, only the most recent update is displayed and
made available for installation. For example, if
`KB4012214` replaces
`KB3135456`, only `KB4012214`
is made available as an update in Patch Manager.

Similarly, Patch Manager can install only patches that are available on the
managed node during the time of the patching operation. By default,
Windows Server 2019 and Windows Server 2022 remove updates that are replaced by
later updates. As a result, if you use the `ApproveUntilDate`
parameter in a Windows Server patch baseline, but the date selected in the
`ApproveUntilDate` parameter is _before_ the date of the latest patch, then the following
scenario occurs:

- The superseded patch is removed from the node and therefore
  can't be installed using Patch Manager.
- The latest, replacement patch is present on the node but not
  yet approved for installation per the
  `ApproveUntilDate` parameter's specified date.

This means that the managed node is compliant in terms of Systems Manager
operations, even though a critical patch from the previous month might
not be installed. This same scenario can occur when using the
`ApproveAfterDays` parameter. Because of the Microsoft
superseded patch behavior, it is possible to set a number (generally
greater than 30 days) so that patches for Windows Server are never installed
if the latest available patch from Microsoft is released before the
number of days in `ApproveAfterDays` has elapsed. Note that
this system behavior doesn't apply if you have modified your Windows
Group Policy Object (GPO) settings to make the superseded patch
available on your managed nodes.

###### Note

In some cases, Microsoft releases patches for applications that don't specify an
updated date and time. In these cases, an updated date and time of
`01/01/1970` is supplied by default.
