

# Linux agent installation errors
<a name="agent-install-linux-errors"></a>

This topic covers errors that you might encounter during or after installing the AWS Elastic Disaster Recovery agent on Linux source servers. Each section describes an error message, its cause, and the resolution.

**Topics**
+ [Error: Invalid disk path format](#error-disk-path-format)
+ [Error: Kernel headers version mismatch](#error-kernel-headers-mismatch)
+ [Error: GLIBC version not found](#error-glibc-version)
+ [Error: Unsupported Linux kernel version](#error-unsupported-kernel)
+ [Error: gcc not found](#error-gcc-not-found)
+ [Error: Permission denied when loading kernel driver](#error-selinux-secure-boot)
+ [Error: Failed to create system user](#error-user-creation-failed)
+ [Error: Failed to map segment from shared object](#error-noexec-tmp)
+ [Error: Multipath disk detection failure](#error-multipath)
+ [Error: PowerPath multipath detected](#error-powerpath)
+ [Error: Driver compiled for a different kernel](#error-driver-compiled)
+ [Error: Agent driver build configuration failed](#error-driver-build-config-failed)
+ [Error: Agent driver compilation failed](#error-driver-compile-failed)
+ [Error: SUSE kernel headers package not found](#error-suse-kernel-headers)
+ [Error: Oracle ASM Filter Driver requires a restart](#error-oracle-asmfd)
+ [Error: Invalid driver state location](#error-driver-state-location)

## Error: Invalid disk path format
<a name="error-disk-path-format"></a>

**Error message:** Installation fails when you specify disks to replicate.

**Cause:** Apostrophes, brackets, or non-existent paths were used in the disk list.

**Resolution:** Use comma-separated paths only. Do not include quotes, brackets, or spaces. For example:

```
/dev/sda,/dev/sdb
```

## Error: Kernel headers version mismatch
<a name="error-kernel-headers-mismatch"></a>

**Error message:** Cannot find kernel headers or the driver build fails during installation.

**Cause:** The agent builds a kernel driver at install time. This requires `kernel-devel` (RHEL/CentOS/SUSE) or `linux-headers` (Debian/Ubuntu) matching the exact running kernel version.

**Resolution:** Complete the following steps to install the correct kernel headers.

1. Check the running kernel version:

   ```
   $ uname -r
   ```

1. Check installed headers:
   + **RHEL/CentOS/SUSE:**

     ```
     $ rpm -qa | grep 'kernel.*devel'
     ```
   + **Debian/Ubuntu:**

     ```
     $ dpkg -l | grep linux-headers
     ```

1. Check whether the header directory is a symlink. If it is a symlink, remove it:
   + **RHEL/CentOS/SUSE:**

     ```
     $ ls -l /usr/src/kernels
     ```
   + **Debian/Ubuntu:**

     ```
     $ ls -l /usr/src
     ```

   If a symlink exists, remove it with `rm`.

1. Install the correct headers:
   + **RHEL/CentOS:**

     ```
     $ sudo yum install kernel-devel-$(uname -r)
     ```
   + **SUSE:**

     ```
     $ sudo zypper install kernel-default-devel=$(uname -r | sed "s/-default//")
     ```
   + **Debian/Ubuntu:**

     ```
     $ sudo apt-get install linux-headers-$(uname -r)
     ```

1. If the headers are not available in your configured repositories, download them manually from one of the following sources:
   + **RHEL/CentOS/SUSE:** [rpm.pbone.net](https://rpm.pbone.net)
   + **Debian:** [packages.debian.org](https://packages.debian.org)
   + **Ubuntu:** [packages.ubuntu.com](https://packages.ubuntu.com)

**Note**  
Multiple kernel-headers versions can coexist safely. Installing new headers does not affect the running kernel.

## Error: GLIBC version not found
<a name="error-glibc-version"></a>

**Error message:** version 'GLIBC\_2.7' not found (required by ./aws-replication-installer-64bit)

**Cause:** The operating system is unsupported or too old for the agent binary.

**Resolution:** Verify that your operating system is supported. For more information, see [Supported Linux operating systems](https://docs.aws.amazon.com/drs/latest/userguide/Supported-Operating-Systems-Linux.html).

## Error: Unsupported Linux kernel version
<a name="error-unsupported-kernel"></a>

**Error message:** Your Linux kernel version is not supported

**Cause:** The running kernel is not compatible with the AWS Elastic Disaster Recovery replication driver.

**Resolution:** Check the supported kernels list. If your kernel is listed but the error persists, ensure that the matching kernel headers are installed. For more information, see the [Error: Kernel headers version mismatch](#error-kernel-headers-mismatch) section.

## Error: gcc not found
<a name="error-gcc-not-found"></a>

**Error message:** gcc was not found and could not be automatically fetched from the configured repositories

**Cause:** The `gcc` compiler is required to compile the replication driver, and the installer could not install it.

**Resolution:** Identify which condition prevented the installation and apply the corresponding fix. The following conditions are the most common.

**Unreachable package repositories**  
Check whether the repositories respond:  

```
$ sudo apt-get update
```
On RHEL, CentOS, and Amazon Linux, use the following command instead:  

```
$ sudo yum makecache
```
On SUSE, use the following command instead:  

```
$ sudo zypper refresh
```
If the command fails, restore repository access and run the installer again. If the server reaches the internet through a web proxy, configure that proxy for the package manager as well.

**gcc missing from the repositories**  
Check whether the configured repositories offer `gcc`:  

```
$ apt-cache policy gcc
```
On RHEL, CentOS, and Amazon Linux, use the following command instead:  

```
$ yum info gcc
```
On SUSE, use the following command instead:  

```
$ zypper info gcc
```
If no candidate version is listed, and this server is not permitted to reach an external repository, install `gcc` and `make` from local media or from an internal repository, and then run the installer again.

**Package manager lock contention**  
Check whether another package operation is running:  

```
$ pgrep -af 'apt|dpkg|yum|dnf|zypper|unattended'
```
The pattern covers the package managers and the unattended upgrade service, which is a common holder of the lock. Because the command matches full command lines, it can also list itself; disregard that entry. If it lists a package operation, wait for that operation to finish and then run the installer again.

**Insufficient free space**  
Check the file systems that hold the package cache and the installation target:  

```
$ df -h /var /usr
```
If either is full, delete unneeded files and run the installer again.

If none of the preceding conditions applies, install `gcc` and `make` manually and then run the installer again:
+ **RHEL/CentOS/Amazon Linux:**

  ```
  $ sudo yum install gcc make
  ```
+ **Debian/Ubuntu:**

  ```
  $ sudo apt-get install gcc make
  ```
+ **SUSE:**

  ```
  $ sudo zypper install gcc make
  ```

## Error: Permission denied when loading kernel driver
<a name="error-selinux-secure-boot"></a>

**Error message:** insmod: ERROR: could not insert module ./aws-replication-driver.ko: Permission denied or Operation not permitted

**Cause:** SELinux, Secure Boot, or endpoint protection software is blocking kernel module insertion.

**Resolution:** Identify which mechanism is blocking the module and apply the corresponding fix.

**SELinux**  
Check SELinux status:  

```
$ sestatus
```
Fix the security context on the driver module:  

```
$ restorecon /lib/modules/*/extra/aws-replication-driver.ko
```

**Secure Boot**  
Check Secure Boot status:  

```
$ mokutil --sb-state
```
If Secure Boot is enabled, you must disable it to use the agent.  
Consult your security team before disabling Secure Boot.

**Antivirus or endpoint protection**  
Check your endpoint protection software and add AWS Elastic Disaster Recovery components to the allow list.

## Error: Failed to create system user
<a name="error-user-creation-failed"></a>

**Error message:** Failed to set system user permissions: followed by one of several messages, for example: "getpwnam(): name not found: aws-replication", Unable to change permissions of /var/lib/aws-replication-agent, or sudoers file failed verification ...

**Cause:** The installer cannot create or configure the `aws-replication` system user because of a file-level restriction.

**Resolution:** Identify which restriction is blocking user creation and apply the corresponding fix.

**Immutable user database files**  
Check for the immutable attribute:  

```
$ lsattr /etc/passwd /etc/group /etc/shadow
```
Remove the immutable attribute:  

```
$ sudo chattr -i /etc/passwd /etc/group /etc/shadow
```
Run the agent installer. Re-apply the immutable attribute after installation completes.  
The immutable attribute might be intentional security hardening. Consult your system administrator before removing it. Re-apply the attribute after installation.

**Installation directory not writable or immutable**  
Check whether the file system is mounted read-only:  

```
$ findmnt -T /var/lib/aws-replication-agent
```
If the `OPTIONS` column includes `ro`, remount the file system with write permissions and run the installer again.  
Check whether the directory has the immutable attribute:  

```
$ lsattr -d /var/lib/aws-replication-agent
```
If the output includes `i`, remove the immutable attribute:  

```
$ sudo chattr -i /var/lib/aws-replication-agent
```
Run the installer again after removing the attribute.

**Invalid sudoers file**  
Validate the existing `/etc/sudoers` file:  

```
$ sudo visudo -c
```
Correct any reported syntax errors, then run the installer again. Your existing `/etc/sudoers` file remains unchanged.

## Error: Failed to map segment from shared object
<a name="error-noexec-tmp"></a>

**Error message:** error while loading shared libraries: libz.so.1: failed to map segment from shared object

**Cause:** The `/tmp` directory is mounted with the `noexec` option.

**Resolution:** Use one of the following options:
+ **Option 1:** Temporarily remount `/tmp` with execute permissions:

  ```
  $ sudo mount /tmp -o remount,exec
  ```
+ **Option 2:** Set the `TMPDIR` environment variable to a directory with execute permissions:

  ```
  $ TMPDIR='{{/path/to/exec/dir}}' sudo ./aws-replication-installer-init
  ```

**Note**  
The `noexec` option on `/tmp` is a common security hardening measure. The `TMPDIR` alternative avoids modifying mount options.

## Error: Multipath disk detection failure
<a name="error-multipath"></a>

**Error message:** The installer does not correctly identify disks on a multipath-configured server.

**Cause:** Automatic disk detection cannot resolve multipath device mappings.

**Resolution:** Specify disks explicitly with the `--devices` and `--no-prompt` options:

```
$ sudo ./aws-replication-installer-init \
    --region {{region}} \
    --aws-access-key-id {{key}} \
    --aws-secret-access-key {{secret}} \
    --devices /dev/sda,/dev/mapper/mpatha \
    --no-prompt
```

If the installation still fails, add the `--force-volumes` option.

**Important**  
The `--force-volumes` option disables automatic disk detection. Manually verify that all required disks are included in the `--devices` list.

## Error: PowerPath multipath detected
<a name="error-powerpath"></a>

**Error message:** The installation detects EMC PowerPath.

**Cause:** PowerPath block-level I/O management conflicts with the AWS Elastic Disaster Recovery replication driver.

**Resolution:** Contact AWS Support for guidance on installing the agent on PowerPath-configured servers. Use the `--force-volumes` option as a potential workaround.

## Error: Driver compiled for a different kernel
<a name="error-driver-compiled"></a>

**Error message:** The agent log shows that the driver was compiled for a different kernel version and cannot load.

**Cause:** The kernel was updated (for example, through `yum update` or automated patching) after the agent driver was originally built. This commonly occurs when significant time passes between failover and failback.

**Resolution:** Reboot the server to load the current kernel, then reinstall the agent. On a recovery instance, reboot and reinstall the agent as a recovery instance.

## Error: Agent driver build configuration failed
<a name="error-driver-build-config-failed"></a>

**Error message:** Could not configure the AWS Replication Agent kernel driver build.

**Cause:** The agent builds a kernel driver at install time. The kernel headers are present, but the `configure` step failed before compilation. This usually means the kernel development package (`kernel-devel` or `linux-headers`) for the running kernel is incomplete. It can also mean the kernel build tree at `/lib/modules/$(uname -r)/build` is missing or invalid.

**Resolution:** Complete the following steps.

1. Confirm the kernel build tree exists and resolves to a valid directory:

   ```
   $ ls -l /lib/modules/$(uname -r)/build
   ```

1. Reinstall the complete kernel development package that matches the running kernel version:
   + **RHEL/CentOS:**

     ```
     $ sudo yum install kernel-devel-$(uname -r)
     ```
   + **Debian/Ubuntu:**

     ```
     $ sudo apt-get install --reinstall linux-headers-$(uname -r)
     ```
   + **SUSE/SLES:**

     ```
     $ sudo zypper install kernel-default-devel=$(uname -r | sed "s/-default//") kernel-source
     ```

1. Run the AWS Replication Agent installer again.

1. If the error persists, collect the installation log (`aws_replication_agent_installer.log`), which contains the `configure` output, and contact AWS Support.

## Error: Agent driver compilation failed
<a name="error-driver-compile-failed"></a>

**Error message:** Failed to compile the AWS Replication Agent kernel driver.

**Cause:** The kernel headers are present, but the driver module failed to compile. This error usually occurs when the compiler or toolset is incompatible with the compiler that built the running kernel. For example, a mismatched `gcc` version can cause this error. Insufficient free disk space is another common cause.

**Resolution:** Complete the following steps.

1. Confirm that `gcc` and `make` are installed, and compare the `gcc` version with the compiler that built the running kernel:

   ```
   $ gcc --version
   $ cat /proc/version
   ```

1. If the versions differ, install a compatible compiler toolchain, then run the installer again.

1. Confirm that there is sufficient free disk space:

   ```
   $ df -h /
   ```

1. If the error persists, collect the installation log (`aws_replication_agent_installer.log`), which contains the `make` output, and contact AWS Support.

## Error: SUSE kernel headers package not found
<a name="error-suse-kernel-headers"></a>

**Error message:** Could not find a matching kernel headers package for your SUSE kernel version.

**Cause:** On SUSE Linux Enterprise Server, the installer searches for the `kernel-source` package that matches the running kernel. It then installs the matching `kernel-default-devel` headers. The `zypper` search returned no matching package, which usually means the configured repositories do not include the required package.

**Resolution:** Complete the following steps.

1. Check the running kernel version:

   ```
   $ uname -r
   ```

1. Refresh the repositories and install the matching kernel development packages:

   ```
   $ sudo zypper refresh
   $ sudo zypper install kernel-default-devel=$(uname -r | sed "s/-default//") kernel-source
   ```

1. If your repositories do not include the required packages, register the server with the SUSE Customer Center (SCC) to enable the required module. Then run the installer again. Alternatively, contact your SUSE support representative to obtain the correct packages before running the installer.

1. If the error persists, collect the installation log (`aws_replication_agent_installer.log`) and contact AWS Support.

## Error: Oracle ASM Filter Driver requires a restart
<a name="error-oracle-asmfd"></a>

**Error message:** Oracle ASM Filter Driver detected. Please reboot to start replication.

**Cause:** The Oracle ASM Filter Driver (ASMFD) is loaded, but the AWS Elastic Disaster Recovery replication driver has not loaded yet. Installation completes successfully, but replication cannot start until the replication driver loads.

**Resolution:** Restart the source server. The replication driver loads during startup and replication begins automatically. You do not have to deactivate ASMFD.

## Error: Invalid driver state location
<a name="error-driver-state-location"></a>

**Error message:** The value "{{location}}" provided for parameter "--driver-state-location" has a value for which the location does not exist, or is not on a supported file system type.

**Cause:** The path that you provided for the `--driver-state-location` parameter does not exist. Alternatively, the agent cannot write to that file system early in the boot process. For example, the agent cannot write to a Btrfs subvolume at that stage.

**Resolution:** Use one of the following options:
+ Provide an existing directory on a supported file system, such as ext4 or xfs.
+ Do not point the `--driver-state-location` parameter at a Btrfs subvolume.
+ Omit the `--driver-state-location` parameter so that the installer chooses the location automatically.