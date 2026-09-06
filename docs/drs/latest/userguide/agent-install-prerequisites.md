

# Agent installation prerequisites
<a name="agent-install-prerequisites"></a>

Before installing the AWS Replication Agent, verify that your source server meets the following requirements.

**Topics**
+ [Common requirements](#prereq-common)
+ [Linux prerequisites](#prereq-linux)
+ [Windows prerequisites](#prereq-windows)

## Common requirements
<a name="prereq-common"></a>

The following requirements apply to both Linux and Windows source servers.
+ **64-bit operating system** — The AWS Replication Agent supports only 64-bit architectures. 32-bit systems are not compatible.
+ **Supported operating system version** — Verify that your OS is on the supported list. See [Supported Linux operating systems](https://docs.aws.amazon.com/drs/latest/userguide/Supported-Operating-Systems-Linux.html) or [Supported Windows operating systems](https://docs.aws.amazon.com/drs/latest/userguide/Supported-Operating-Systems-Windows.html).
+ **AWS credentials** — You must have an IAM user or role with the `AWSElasticDisasterRecoveryAgentInstallationPolicy` managed policy attached. The installer uses these credentials to register the source server with Elastic Disaster Recovery.
+ **Network connectivity** — The source server must allow outbound TCP 443 to the Elastic Disaster Recovery, Amazon S3, and Amazon EC2 endpoints in your target Region. The agent uses these connections to communicate with the replication infrastructure.
+ **Elastic Disaster Recovery initialized in target Region** — You must initialize AWS Elastic Disaster Recovery in the target Region before installing the agent. See [Initializing Elastic Disaster Recovery](getting-started-initializing.md).
+ **Volume limits** — Each volume can be a maximum of 16 TiB. Each source server can have a maximum of 63 volumes. Volumes that exceed these limits are not replicated.

## Linux prerequisites
<a name="prereq-linux"></a>

Verify the following requirements on Linux source servers before running the installer.
+ **Root or sudo access** — The installer must run as root or with sudo privileges to install kernel modules and system services.
+ **Disk space: 4 GB free on /** — The agent binaries and replication data require at least 4 GB on the root filesystem. Verify with:

  ```
  df -h /
  ```
+ **Disk space: 500 MB free on /tmp** — The installer extracts temporary files to `/tmp` during installation. If `/tmp` is not a separate mount, this space is part of the 4 GB requirement on `/`. Verify with:

  ```
  df -h /tmp
  ```
+ **Kernel headers matching running kernel** — The kernel headers must match the running kernel version exactly.
**Note**  
The agent builds a kernel driver at install time to capture block-level writes. Without matching headers, the driver compilation fails and the agent cannot replicate data.

  Verify the running kernel version:

  ```
  uname -r
  ```

  Then verify matching headers are installed. On RHEL/CentOS/SUSE:

  ```
  rpm -qa | grep 'kernel.*devel'
  ```

  On Debian/Ubuntu:

  ```
  dpkg -l | grep linux-headers
  ```
+ **Required packages: gcc, make** — These packages are required for kernel driver compilation. Verify with:

  ```
  which gcc && which make
  ```
+ **/tmp must allow execution** — The installer runs executables from `/tmp`. If `/tmp` is mounted with `noexec`, the installation fails. Verify with:

  ```
  mount | grep /tmp
  ```

  If the output shows `noexec`, remount temporarily with:

  ```
  sudo mount -o remount,exec /tmp
  ```
+ **No conflicting disk drivers** — Certain disk filter drivers conflict with the replication driver.
  + *Oracle ASM Filter Driver (ASMFD)* — You must deactivate ASMFD before installation. The replication driver cannot coexist with ASMFD on the same volumes.
  + *PowerPath* — PowerPath requires special handling. Contact AWS Support before installing the agent on servers that use PowerPath.

## Windows prerequisites
<a name="prereq-windows"></a>

Verify the following requirements on Windows source servers before running the installer.
+ **Administrator access** — The installer must run with Administrator privileges to install the replication driver and system services.
+ **.NET Framework 3.5 or later** — The agent requires .NET Framework for its Windows components. Verify on Windows Server:

  ```
  Get-WindowsFeature Net-Framework-Core
  ```

  On desktop Windows, check Programs and Features for Microsoft .NET Framework 3.5 or later.
+ **Disk space: 1 GB free on C:\\** — The agent binaries and service files require at least 1 GB on the system drive. Verify with:

  ```
  Get-PSDrive C
  ```
+ **net.exe and sc.exe in system PATH** — The installer uses these utilities to manage Windows services. They are located in `C:\Windows\System32` by default. Verify with:

  ```
  where.exe net.exe
  ```
+ **BitLocker must be disabled** — BitLocker encryption prevents the replication driver from reading block-level data. You must disable BitLocker on all volumes that you want to replicate. Verify with:

  ```
  manage-bde -status
  ```
+ **TLS 1.2 must be enabled** — Elastic Disaster Recovery endpoints require TLS 1.2. Older Windows versions (such as Windows Server 2012) might default to TLS 1.0, which Elastic Disaster Recovery endpoints reject.
**Note**  
If your server uses Windows Server 2012 or earlier, verify that TLS 1.2 is enabled in the Windows Registry before running the installer.
+ **Use PowerShell to run the installer** — Run the installer from PowerShell, not CMD. CMD has known issues with credential pasting that can cause authentication failures during installation.