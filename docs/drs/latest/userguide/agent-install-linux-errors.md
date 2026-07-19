# Linux agent installation errors

This topic covers errors that you might encounter during or after installing the
AWS Elastic Disaster Recovery agent on Linux source servers. Each section describes an error
message, its cause, and the resolution.

###### Topics

- [Error: Root privileges required](#error-root-privileges "#error-root-privileges")
- [Error: Invalid disk path format](#error-disk-path-format "#error-disk-path-format")
- [Error: Kernel headers version mismatch](#error-kernel-headers-mismatch "#error-kernel-headers-mismatch")
- [Error: Connection timed out during installation](#error-connection-timeout "#error-connection-timeout")
- [Error: GLIBC version not found](#error-glibc-version "#error-glibc-version")
- [Error: Unsupported Linux kernel version](#error-unsupported-kernel "#error-unsupported-kernel")
- [Error: gcc not found](#error-gcc-not-found "#error-gcc-not-found")
- [Error: Permission denied when loading kernel driver](#error-selinux-secure-boot "#error-selinux-secure-boot")
- [Error: Failed to create system user](#error-user-creation-failed "#error-user-creation-failed")
- [Error: Failed to map segment from shared object](#error-noexec-tmp "#error-noexec-tmp")
- [Error: Multipath disk detection failure](#error-multipath "#error-multipath")
- [Error: PowerPath multipath detected](#error-powerpath "#error-powerpath")
- [Error: Driver compiled for a different kernel](#error-driver-compiled "#error-driver-compiled")
- [Error: Agent driver build configuration failed](#error-driver-build-config-failed "#error-driver-build-config-failed")
- [Error: Agent driver compilation failed](#error-driver-compile-failed "#error-driver-compile-failed")
- [Error: SUSE kernel headers package not found](#error-suse-kernel-headers "#error-suse-kernel-headers")
- [Error: Oracle ASM Filter Driver conflict](#error-oracle-asmfd "#error-oracle-asmfd")

## Error: Root privileges required

**Error message:**
**`You need to have root privileges to run this script`**

**Cause:** You ran the installer without root or
sudo privileges.

**Resolution:** Run the installer with
`sudo`:

```
`$` sudo ./aws-replication-installer-init
```

## Error: Invalid disk path format

**Error message:** Installation fails when you specify
disks to replicate.

**Cause:** Apostrophes, brackets, or non-existent paths
were used in the disk list.

**Resolution:** Use comma-separated paths only. Do not
include quotes, brackets, or spaces. For example:

```
/dev/sda,/dev/sdb
```

## Error: Kernel headers version mismatch

**Error message:**
**`Cannot find kernel headers`** or the driver build fails during
installation.

**Cause:** The agent builds a kernel driver at install
time. This requires `kernel-devel` (RHEL/CentOS/SUSE) or
`linux-headers` (Debian/Ubuntu) matching the exact running kernel
version.

**Resolution:** Complete the following steps to install
the correct kernel headers.

1. Check the running kernel version:

```
`$` uname -r
```

2. Check installed headers:

   - **RHEL/CentOS/SUSE:**

   ```
   `$` rpm -qa | grep 'kernel.*devel'
   ```
   - **Debian/Ubuntu:**

   ```
   `$` dpkg -l | grep linux-headers
   ```

3. Check whether the header directory is a symlink. If it is a symlink, remove
   it:

   - **RHEL/CentOS/SUSE:**

   ```
   `$` ls -l /usr/src/kernels
   ```
   - **Debian/Ubuntu:**

   ```
   `$` ls -l /usr/src
   ```

If a symlink exists, remove it with `rm`. 4. Install the correct headers:

    * **RHEL/CentOS:**



    ```
    `$` sudo yum install kernel-devel-$(uname -r)
    ```
    * **SUSE:**



    ```
    `$` sudo zypper install kernel-default-devel=$(uname -r | sed "s/-default//")
    ```
    * **Debian/Ubuntu:**



    ```
    `$` sudo apt-get install linux-headers-$(uname -r)
    ```

5. If the headers are not available in your configured repositories, download them
manually from one of the following sources:

    * **RHEL/CentOS/SUSE:**
    [rpm.pbone.net](https://rpm.pbone.net "https://rpm.pbone.net")
    * **Debian:**
    [packages.debian.org](https://packages.debian.org "https://packages.debian.org")
    * **Ubuntu:**
    [packages.ubuntu.com](https://packages.ubuntu.com "https://packages.ubuntu.com")

###### Note

Multiple kernel-headers versions can coexist safely. Installing new headers does
not affect the running kernel.

## Error: Connection timed out during installation

**Error message:**
**`urlopen error [Errno 110] Connection timed out`**

**Cause:** Outbound TCP port 443 is blocked between the
source server and AWS Elastic Disaster Recovery endpoints.

**Resolution:** Verify that your firewall or security
group allows outbound traffic on port 443 to the following endpoints:

- `drs.`region`.amazonaws.com`
- `s3.`region`.amazonaws.com`

Test connectivity with the following command:

```
`$` curl -v https://drs.`region`.amazonaws.com
```

## Error: GLIBC version not found

**Error message:**
**`version 'GLIBC_2.7' not found (required by ./aws-replication-installer-64bit)`**

**Cause:** The operating system is unsupported or too
old for the agent binary.

**Resolution:** Verify that your operating system is
supported. For more information, see
[Supported Linux operating systems](Supported-Operating-Systems-Linux.md "Supported-Operating-Systems-Linux.md").

## Error: Unsupported Linux kernel version

**Error message:**
**`Your Linux kernel version is not supported`**

**Cause:** The running kernel is not compatible with the
AWS Elastic Disaster Recovery replication driver.

**Resolution:** Check the supported kernels list. If
your kernel is listed but the error persists, ensure that the matching kernel headers are
installed. For more information, see the
[Error: Kernel headers version mismatch](#error-kernel-headers-mismatch "#error-kernel-headers-mismatch")
section.

## Error: gcc not found

**Error message:**
**`gcc was not found and could not be automatically fetched`**

**Cause:** The `gcc` compiler is required to
compile the replication driver but is not installed, and the installer could not fetch it
from the configured repositories.

**Resolution:** Install `gcc`
manually:

- **RHEL/CentOS/Amazon Linux:**

```
`$` sudo yum install gcc
```

- **Debian/Ubuntu:**

```
`$` sudo apt-get install gcc
```

- **SUSE:**

```
`$` sudo zypper install gcc
```

## Error: Permission denied when loading kernel driver

**Error message:**
**`insmod: ERROR: could not insert module ./aws-replication-driver.ko: Permission denied`**
or **`Operation not permitted`**

**Cause:** SELinux, Secure Boot, or endpoint protection
software is blocking kernel module insertion.

**Resolution:** Identify which mechanism is blocking the
module and apply the corresponding fix.

**SELinux**

Check SELinux status:

```
`$` sestatus
```

Fix the security context on the driver module:

```
`$` restorecon /lib/modules/*/extra/aws-replication-driver.ko
```

**Secure Boot**

Check Secure Boot status:

```
`$` mokutil --sb-state
```

If Secure Boot is enabled, you must disable it to use the agent.

###### Important

Consult your security team before disabling Secure Boot.

**Antivirus or endpoint protection**

Check your endpoint protection software and add AWS Elastic Disaster Recovery
components to the allow list.

## Error: Failed to create system user

**Error message:**
**`Failed to set system user permissions: "getpwnam(): name not found: aws-replication"`**

**Cause:** The agent cannot create the
`aws-replication` user because `/etc/passwd`,
`/etc/group`, or `/etc/shadow` have the immutable
attribute set.

**Resolution:** Remove the immutable attribute, install
the agent, then re-apply the attribute.

1. Check for the immutable attribute:

```
`$` lsattr /etc/passwd /etc/group /etc/shadow
```

2. Remove the immutable attribute:

```
`$` sudo chattr -i /etc/passwd /etc/group /etc/shadow
```

3. Run the agent installer.
4. Re-apply the immutable attribute after the installation completes.

###### Important

The immutable attribute might be intentional security hardening. Consult your
system administrator before removing it. Re-apply the attribute after
installation.

## Error: Failed to map segment from shared object

**Error message:**
**`error while loading shared libraries: libz.so.1: failed to map segment from shared object`**

**Cause:** The `/tmp` directory is
mounted with the `noexec` option.

**Resolution:** Use one of the following options:

- **Option 1:** Temporarily remount
  `/tmp` with execute permissions:

```
`$` sudo mount /tmp -o remount,exec
```

- **Option 2:** Set the `TMPDIR`
  environment variable to a directory with execute permissions:

```
`$` TMPDIR='`/path/to/exec/dir`' sudo ./aws-replication-installer-init
```

###### Note

The `noexec` option on `/tmp` is a common security
hardening measure. The `TMPDIR` alternative avoids modifying mount
options.

## Error: Multipath disk detection failure

**Error message:** The installer does not correctly
identify disks on a multipath-configured server.

**Cause:** Automatic disk detection cannot resolve
multipath device mappings.

**Resolution:** Specify disks explicitly with the
`--devices` and `--no-prompt` options:

```
`$` sudo ./aws-replication-installer-init \
    --region `region` \
    --aws-access-key-id `key` \
    --aws-secret-access-key `secret` \
    --devices /dev/sda,/dev/mapper/mpatha \
    --no-prompt
```

If the installation still fails, add the `--force-volumes` option.

###### Important

The `--force-volumes` option disables automatic disk detection.
Manually verify that all required disks are included in the
`--devices` list.

## Error: PowerPath multipath detected

**Error message:** The installation detects EMC
PowerPath.

**Cause:** PowerPath block-level I/O management
conflicts with the AWS Elastic Disaster Recovery replication driver.

**Resolution:** Contact AWS Support for guidance on
installing the agent on PowerPath-configured servers. Use the
`--force-volumes` option as a potential workaround.

## Error: Driver compiled for a different kernel

**Error message:** The agent log shows that the driver
was compiled for a different kernel version and cannot load.

**Cause:** The kernel was updated (for example, through
`yum update` or automated patching) after the agent driver was originally
built. This commonly occurs when significant time passes between failover and
failback.

**Resolution:** Reboot the server to load the current
kernel, then reinstall the agent. On a recovery instance, reboot and reinstall the agent
as a recovery instance.

## Error: Agent driver build configuration failed

**Error message:**
**`Could not configure the AWS Replication Agent kernel driver build.`**

**Cause:** The agent builds a kernel driver at install
time. The kernel headers are present, but the `configure` step failed before
compilation. This usually means the kernel development package
(`kernel-devel` or `linux-headers`) for the running kernel is
incomplete. It can also mean the kernel build tree at
`/lib/modules/$(uname -r)/build` is missing or invalid.

**Resolution:** Complete the following steps.

1. Confirm the kernel build tree exists and resolves to a valid directory:

```
`$` ls -l /lib/modules/$(uname -r)/build
```

2. Reinstall the complete kernel development package that matches the running
   kernel version:

   - **RHEL/CentOS:**

   ```
   `$` sudo yum install kernel-devel-$(uname -r)
   ```
   - **Debian/Ubuntu:**

   ```
   `$` sudo apt-get install --reinstall linux-headers-$(uname -r)
   ```
   - **SUSE/SLES:**

   ```
   `$` sudo zypper install kernel-default-devel=$(uname -r | sed "s/-default//") kernel-source
   ```

3. Run the AWS Replication Agent installer again.
4. If the error persists, collect the installation log
   (`aws_replication_agent_installer.log`), which contains the
   `configure` output, and contact AWS Support.

## Error: Agent driver compilation failed

**Error message:**
**`Failed to compile the AWS Replication Agent kernel driver.`**

**Cause:** The kernel headers are present, but the driver
module failed to compile. This error usually occurs when the compiler or toolset is
incompatible with the compiler that built the running kernel. For example, a mismatched
`gcc` version can cause this error. Insufficient free disk space is another
common cause.

**Resolution:** Complete the following steps.

1. Confirm that `gcc` and `make` are installed, and compare the
   `gcc` version with the compiler that built the running kernel:

```
`$` gcc --version
`$` cat /proc/version
```

2. If the versions differ, install a compatible compiler toolchain, then run the
   installer again.
3. Confirm that there is sufficient free disk space:

```
`$` df -h /
```

4. If the error persists, collect the installation log
   (`aws_replication_agent_installer.log`), which contains the
   `make` output, and contact AWS Support.

## Error: SUSE kernel headers package not found

**Error message:**
**`Could not find a matching kernel headers package for your SUSE kernel version.`**

**Cause:** On SUSE Linux Enterprise Server, the installer
searches for the `kernel-source` package that matches the running kernel. It then
installs the matching `kernel-default-devel` headers. The `zypper`
search returned no matching package, which usually means the configured repositories do
not include the required package.

**Resolution:** Complete the following steps.

1. Check the running kernel version:

```
`$` uname -r
```

2. Refresh the repositories and install the matching kernel development packages:

```
`$` sudo zypper refresh
`$` sudo zypper install kernel-default-devel=$(uname -r | sed "s/-default//") kernel-source
```

3. If your repositories do not include the required packages, register the server with
   the SUSE Customer Center (SCC) to enable the required module. Then run the installer
   again. Alternatively, contact your SUSE support representative to obtain the correct
   packages before running the installer.
4. If the error persists, collect the installation log
   (`aws_replication_agent_installer.log`) and contact AWS Support.

## Error: Oracle ASM Filter Driver conflict

**Error message:**
**`The agent cannot be installed on this server because Oracle ASM Filter Driver is active`**

**Cause:** Oracle ASM Filter Driver (ASMFD) conflicts
with the AWS Elastic Disaster Recovery replication driver at the block device level.

**Resolution:** Deactivate ASM Filter Driver, reboot
the server, then run the installer. You can reactivate ASMFD after replication is
active.

###### Important

Consult your DBA before disabling ASMFD.
