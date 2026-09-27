

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Agent questions
<a name="Agent-Related-FAQ"></a>

This section contains answers to questions about the AWS Replication Agent.

**Topics**
+ [What does the AWS Replication Agent do?](#What-Agent-Do)
+ [What kind of data is transferred between the agent and the AWS Transform MGN?](#What-Data-Transferred)
+ [What kind of resources does the AWS Replication Agent use?](#What-Resources-Agent)
+ [How much bandwidth does the AWS Replication Agent consume?](#How-Much-Bandwidth)
+ [What are the prerequisites needed to install the AWS Replication Agent?](#What-Pre-Requisites-Agent)
+ [What privileges does the AWS Replication Agent require?](#Agent-privileges)
+ [What ports does the AWS Replication Agent use?](#What-Ports-Agent)
+ [Can a proxy server be used between the source server and the AWS Transform MGN console?](#Can-Proxy-Used)
+ [Is it possible to install the agent on servers running operating systems that are not listed as supported?](#Agent-installation-on-unsupported-operating-system)
+ [How do temporary credentials work?](#temporary-credentials-operation)
+ [How is communication between the AWS Replication Agent and the AWS Transform MGN secured?](#How-Communication-Secured)
+ [Is it possible to change the port the AWS Replication Agent uses from TCP Port 1500 to a different port?](#Can-Change-Port-TCP)
+ [Does the AWS Replication Agent cache any data to disk?](#Does-Agent-Cache-Data)
+ [Is it possible to add a disk to replication without a complete resync of any disks that have already been replicated?](#What-mgn-Agent-Services)
+ [Which Windows and Linux OSs support no-rescan upon reboot?](#agent-no-rescan)
+ [When do I need to reinstall the agent?](#When-Reinstall-Agent)
+ [How do I manually uninstall the AWS Transform MGN agent from a server?](#How-Manually-Uninstall-Agent)
+ [Is the AWS Replication Agent installed on launched test and cutover instances?](#agent-transfer-instance)

## What does the AWS Replication Agent do?
<a name="What-Agent-Do"></a>

The AWS Replication Agent performs an initial block-level read of the content of any volume attached to the server and replicates it to the replication server. The agent then acts as an OS-level read filter to capture writes and synchronizes any block level modifications to the AWS Transform MGN replication server, ensuring near-zero RPO.

## What kind of data is transferred between the agent and the AWS Transform MGN?
<a name="What-Data-Transferred"></a>

The AWS Replication Agent sends the following types of information to the Service Manager of AWS Transform MGN:
+ Monitoring metrics of the agent itself
+ Replication status (started, stalled, resumed)
+ Backlog information
+ OS and hardware information

When an Agent is installed on a source server, it collects the following information on the machine:
+ Host name and ID
+ List of CPUs including models and number of cores
+ Amount of RAM
+ Hardware and OS information
+ Number of disks and their size – in Windows, disk letters; in Linux, block device names
+ Machine's Private IP address

## What kind of resources does the AWS Replication Agent use?
<a name="What-Resources-Agent"></a>

The AWS Replication Agent is lightweight and nondisruptive. The agent uses approximately 5% CPU and 250 MB of RAM.

## How much bandwidth does the AWS Replication Agent consume?
<a name="How-Much-Bandwidth"></a>

The AWS Replication Agent opens up to five connections and attempts to maximize available bandwidth.

Throttling can be activated in the AWS Transform MGN console by either selecting a specific server and choosing the **Replication settings** tab or by changing the **Replication template** (in this case the change only affects newly added servers). 

## What are the prerequisites needed to install the AWS Replication Agent?
<a name="What-Pre-Requisites-Agent"></a>

The installation requirements for source server depend on the type of OS that the server runs – either Linux or Windows.

For prerequisites, see [Installation requirements](installation-requirements.md).

## What privileges does the AWS Replication Agent require?
<a name="Agent-privileges"></a>

The AWS Replication Agent installer requires root privileges or the use of the sudo command during installation. It creates an "aws-replication" group and user, and attempts to add the "aws-replication" user to the "sudoers" file to grant necessary permissions. Ensure that the user running the installation has sufficient privileges to modify the "sudoers" file. If the installation fails because of insufficient permissions, you might need to manually add the "aws-replication" user to the "sudoers" file before attempting the installation again.

## What ports does the AWS Replication Agent use?
<a name="What-Ports-Agent"></a>

The agent uses TCP Port 443 to communicate with the Service Manager of AWS Transform MGN and TCP Port 1500 for replication to AWS.

## Can a proxy server be used between the source server and the AWS Transform MGN console?
<a name="Can-Proxy-Used"></a>

Yes. The proxy is configured using an environment variable before the install.

https\_proxy=https://PROXY:PORT/

For example: https\_proxy=https://10.0.0.1:8088/

Make sure to set the environment variables `https_proxy`, `http_proxy`, and `no_proxy` (for metadata) according to your environment. The proxy value must end with a trailing forward slash (/).

Ensure that you have allowlisted the [MGN IPs and URLs](preparing-environments.md#TCP-443) for both SSL Interception and Authentication. 

**Note**  
A web proxy cannot be used for communication between the source server and the staging area subnet where replication server launched for replication over TCP Port 1500. To use private routing for data replication, see [Data routing and throttling](replication-server-settings.md#data-routing).

## Is it possible to install the agent on servers running operating systems that are not listed as supported?
<a name="Agent-installation-on-unsupported-operating-system"></a>

AWS Transform MGN supports the agent only on the operating systems listed in [Supported operating systems](Supported-Operating-Systems.md). Installing the agent on an unsupported operating system might work, but MGN does not support it, and support for installation or replication issues is limited to the listed operating systems.

## How do temporary credentials work?
<a name="temporary-credentials-operation"></a>

The temporary credential mechanism was developed specifically to provide an easy and secure way to install MGN Agents. The main flow of the temporary credentials' creation process relies on generating an x509 certificate per agent and then using this x509 certificate to receive temporary IAM credentials. This process uses a similar mechanism to the one used by [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html).

## How is communication between the AWS Replication Agent and the AWS Transform MGN secured?
<a name="How-Communication-Secured"></a>

All communication is encrypted using SSL. In addition, each Agent is assigned a key during installation which is used to encrypt all traffic. All keys are unique and are not shared across multiple agents.

## Is it possible to change the port the AWS Replication Agent uses from TCP Port 1500 to a different port?
<a name="Can-Change-Port-TCP"></a>

No. The AWS Transform MGN Agent can only use TCP Port 1500 for replication. 

## Does the AWS Replication Agent cache any data to disk?
<a name="Does-Agent-Cache-Data"></a>

AWS Transform MGN does not write any cache or do any sort of journalling to disk. The Agent holds a buffer which is large enough to map all volume's blocks \~250 MB in memory.

The agent acts as a write filter and replicates changed blocks directly from memory to the Replication Server. When the data is no longer in memory, the agent reads the block directly from the volume. In this case, you might see backlog in the AWS Transform MGN console, which occurs when the volume of change is greater than the available bandwidth.

## Is it possible to add a disk to replication without a complete resync of any disks that have already been replicated?
<a name="What-mgn-Agent-Services"></a>

When you add a disk to a source server, AWS Transform MGN does not automatically identify the disk or add it to the **Disk settings** section in the console.

To replicate the new disk, reinstall the agent. Before you reinstall, note the current **Total replicated storage** value. After you reinstall the agent, this value changes.

An additional progress bar also appears, which indicates that MGN is rescanning the original volumes. This is a scan, not a resync: it verifies that the blocks on the source still match the blocks on the replication side. The scan is significantly faster than a resync because MGN transfers block data only where a difference exists. The scan is required because reinstalling the agent unloads and resets the driver that performs the I/O tracking, so the sync status can no longer be guaranteed. While the original volumes are rescanned, the agent completes the initial sync of the new volume in parallel.

## Which Windows and Linux OSs support no-rescan upon reboot?
<a name="agent-no-rescan"></a>

When you shut down a supported Linux or Windows source server (from the OS menu or CLI) and then restart it, MGN resumes replication without a rescan.

A rescan means that the agent on the source server rereads all blocks on all replicated disks and transmits blocks that are different from the previously replicated data. A rescan is similar to the initial sync but is faster because only blocks that are different need to be transmitted.

Rescans can still happen following a hard reboot, crashes, or when you add or remove disks to or from the source server.

 Supported OSs include:

**Windows**
+ Windows Server 2012r1
+ Windows Server 2012r2
+ Windows Server 2016
+ Windows Server 2019
+ Windows Server 2022
+ Windows Server 2025
+ Windows 11

**Linux**
+  CentOS 6–8, Stream 9, Stream 10 
+  Oracle 6–8 
+  RHEL 6–9.8, 10, 10.1, 10.2 
+  Rocky Linux 8–9.8, 10, 10.1, 10.2 
+  SLES 12 and 15 
+  Debian 9–12 
+  Ubuntu 16, 18, 20, and 22 
+  Amazon Linux 2 and 2023 
+  AlmaLinux 9.6, 9.7, 9.8, 10, 10.1, 10.2 

**Note**  
For Linux, no-rescan on reboot is supported only on environments that use initramfs.

## When do I need to reinstall the agent?
<a name="When-Reinstall-Agent"></a>

Typically, you need to reinstall the Agent after any major upgrade to the source server.

**Linux**
+ Any kernel upgrade
+ After adding new volumes

**Windows**
+ Any OS upgrade (for example, Windows Server 2012 to Windows Server 2016)
**Note**  
 If you [upgrade using a post-launch action](predefined-post-launch-actions.md#predefined-windows-upgrade), an agent upgrade is not required.
+ After adding new volumes

## How do I manually uninstall the AWS Transform MGN agent from a server?
<a name="How-Manually-Uninstall-Agent"></a>

Follow the steps in the [Uninstalling the Agent](uninstalling-agent.md) section.

## Is the AWS Replication Agent installed on launched test and cutover instances?
<a name="agent-transfer-instance"></a>

During the launch process, either upon test or cutover instance launch, the AWS Replication agent is removed from the test or cutover instance, and does not run on it.