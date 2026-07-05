NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Agent related

This section contains answers to questions about the AWS Replication Agent.

###### Topics

- [What does the AWS Replication Agent do?](#What-Agent-Do "#What-Agent-Do")
- [What kind of data is transferred between the agent and the AWS Transform MGN?](#What-Data-Transferred "#What-Data-Transferred")
- [Can a proxy server be used between the source server and the AWS Transform MGN console?](#Can-Proxy-Used "#Can-Proxy-Used")
- [What are the prerequisites needed to install the AWS Replication Agent?](#What-Pre-Requisites-Agent "#What-Pre-Requisites-Agent")
- [What ports does the AWS Replication Agent use?](#What-Ports-Agent "#What-Ports-Agent")
- [What privileges does the AWS Replication Agent require?](#Agent-privileges "#Agent-privileges")
- [Is it possible to install the agent on servers running operating systems that are not listed as supported?](#Agent-installation-on-unsupported-operating-system "#Agent-installation-on-unsupported-operating-system")
- [What kind of resources does the AWS Replication Agent use?](#What-Resources-Agent "#What-Resources-Agent")
- [Can AWS Transform MGN migrate containers?](#Can-Containers "#Can-Containers")
- [Does the AWS Replication Agent cache any data to disk?](#Does-Agent-Cache-Data "#Does-Agent-Cache-Data")
- [How is communication between the AWS Replication Agent and the AWS Transform MGN secured?](#How-Communication-Secured "#How-Communication-Secured")
- [Is it possible to change the port the AWS Replication Agent uses from TCP Port 1500 to a different port?](#Can-Change-Port-TCP "#Can-Change-Port-TCP")
- [How do I manually uninstall the AWS Transform MGN agent from a server?](#How-Manually-Uninstall-Agent "#How-Manually-Uninstall-Agent")
- [When do I need to reinstall the agent?](#When-Reinstall-Agent "#When-Reinstall-Agent")
- [How much bandwidth does the AWS Replication Agent consume?](#How-Much-Bandwidth "#How-Much-Bandwidth")
- [How many disks can the AWS Replication Agent replicate?](#How-Many-Disks-Agent-Replicate "#How-Many-Disks-Agent-Replicate")
- [Is it possible to add a disk to replication without a complete resync of any disks that have already been replicated?](#What-mgn-Agent-Services "#What-mgn-Agent-Services")
- [Is the AWS Replication Agent installed on launched test and cutover instances?](#agent-transfer-instance "#agent-transfer-instance")
- [How do temporary credentials work?](#temporary-credentials-operation "#temporary-credentials-operation")
- [Which Windows and Linux OSs support no-rescan upon reboot?](#agent-no-rescan "#agent-no-rescan")

## What does the AWS Replication Agent do?

The AWS Replication Agent performs an initial block-level read of the content of any volume
attached to the server and replicates it to the replication server. The agent then acts as
an OS-level read filter to capture writes and synchronizes any block level modifications to
the AWS Transform MGN replication server, ensuring near-zero RPO.

## What kind of data is transferred between the agent and the AWS Transform MGN?

The AWS Replication Agent sends the following types of information to the Service Manager
of AWS Transform MGN:

- Monitoring metrics of the agent itself
- Replication status (started, stalled, resumed)
- Backlog information
- OS and hardware information

When an Agent is installed on a source server, it collects the following information on the
machine:

- Host name and ID
- List of CPUs including models and number of cores
- Amount of RAM
- Hardware and OS information
- Number of disks and their size – in Windows, disk letters; in Linux, block device
  names
- Machine's Private IP address

## Can a proxy server be used between the source server and the AWS Transform MGN console?

Yes. The proxy is configured using an environment variable before the install.

https\_proxy=https://PROXY:PORT/

For example: https\_proxy=https://10.0.0.1:8088/

Make sure the proxy has a trailing forward slash.

Ensure that you have allowlisted the [MGN IPs and URLs](preparing-environments.md#TCP-443 "preparing-environments.md#TCP-443") for
both SSL Interception and Authentication.

###### Note

A web proxy cannot be used for communication between the source server and the staging
area subnet where replication server launched for replication over TCP Port 1500. To use
private routing for data replication, please see [Data routing
and throttling](replication-server-settings.md#data-routing "replication-server-settings.md#data-routing").

## What are the prerequisites needed to install the AWS Replication Agent?

The installation requirements for source server depend on the type of OS that the server
runs – either Linux or Windows.

Prerequisites [can be found here](installation-requirements.md "installation-requirements.md").

## What ports does the AWS Replication Agent use?

The Agent uses TCP Port 443 to communicate with the Service Manager of Application
Migration Service and TCP Port 1500 for replication to AWS.

## What privileges does the AWS Replication Agent require?

The AWS Replication Agent installer requires root privileges or the use of the sudo command during installation.
It creates an "aws-replication" group and user, and attempts to add the "aws-replication" user to the "sudoers" file to grant necessary permissions. Ensure that the user running the installation has sufficient privileges to modify the "sudoers" file.
If the installation fails due to insufficient permissions, you may need to manually add the "aws-replication" user to the "sudoers" file before attempting the installation again.

## Is it possible to install the agent on servers running operating systems that are not listed as supported?

The agent is designed and tested to work on the officially supported operating systems listed in the documentation. Installing the agent on other unsupported operating systems may be possible but is not recommended.
Any installation or replication issues encountered when using unsupported operating systems will need to be handled through your own troubleshooting or support channels, as the AWS engineering team will be limited in their ability to assist.
We advise using the agent only on supported OS versions to ensure the best experience. Please refer to [Supported operating systems](Supported-Operating-Systems.md "Supported-Operating-Systems.md").

## What kind of resources does the AWS Replication Agent use?

The AWS Replication Agent is lightweight and nondisruptive. The agent uses
approximately 5% CPU and 250 MB of RAM.

## Can AWS Transform MGN migrate containers?

AWS Transform MGN only supports the replication of full servers.
Nevertheless, MGN replicates on a server level and therefore any containers within the
selected servers will be replicated.

## Does the AWS Replication Agent cache any data to disk?

AWS Transform MGN does not write any cache or do any sort of journalling to
disk. The Agent holds a buffer which is large enough to map all volume's blocks ~250 MB in
memory.

The agent then acts as a sort of write filter and will replicate changed blocks directly
from memory to the Replication Server. In cases where the data is no longer in memory, the
agent will read the block from the volume directly. This is the case where you may see
backlog in the AWS Transform MGN console. The cause of this is the volume of
change is greater than the bandwidth available.

## How is communication between the AWS Replication Agent and the AWS Transform MGN secured?

All communication is encrypted using SSL. In addition, each Agent is assigned a key during
installation which is used to encrypt all traffic. All keys are unique and are not shared
across multiple agents.

## Is it possible to change the port the AWS Replication Agent uses from TCP Port 1500 to a different port?

No. The AWS Transform MGN Agent can only use TCP Port 1500 for replication.

## How do I manually uninstall the AWS Transform MGN agent from a server?

Follow the steps in the [Uninstalling the Agent](uninstalling-agent.md "uninstalling-agent.md") section.

## When do I need to reinstall the agent?

Typically, you need to reinstall the Agent after any major upgrade to the source
server.

**Linux**

- Any kernel upgrade
- After adding new volumes

**Windows**

- Any OS upgrade (for example, Windows Server 2012 to Windows Server 2016)

###### Note

If you [upgrade using a post-launch
action](predefined-post-launch-actions.md#predefined-windows-upgrade "predefined-post-launch-actions.md#predefined-windows-upgrade"), an agent upgrade is not required.

- After adding new volumes

## How much bandwidth does the AWS Replication Agent consume?

The AWS Replication Agent opens up to five connections and will attempt to maximize
available bandwidth.

Throttling can be activated via the AWS Transform MGN console by either
selecting a specific server and choosing the **Replication
settings** tab or by changing the **Replication
template** (in this case the change will only affect newly added servers).

## How many disks can the AWS Replication Agent replicate?

The agent can replicate up to 50 disks from a single server. Ensure that the replication
server instance type supports at least the number of disks being replicated.

## Is it possible to add a disk to replication without a complete resync of any disks that have already been replicated?

When you are adding a disk to a source server, AWS Transform MGN will not automatically identify this
disk and add it to the **Disk settings** section in the
console.

The only way to get this disk to replicate is to reinstall the agent. Before
reinstalling, you can note the current **Total replicated storage**. When you reinstall the
agent, you will notice the value of replicated storage changes.

You will also notice an additional progress bar appear, which indicates that we are
rescanning the original volumes. This is not a resync, but a scan, to verify that all the
blocks on the source still match the blocks on the replication side. This process is
significantly quicker than a resync, as there is no actual block data transferred, unless there
is a difference. This is needed, as a reinstall results in the driver which performs the IO
tracking being unloaded and reset, so we have no way of being certain of the sync status. Whilst
the rescan on the original volumes is happening, the agent is also ensuring that the initial
sync of the new volume is being completed in parallel.

## Is the AWS Replication Agent installed on launched test and cutover instances?

During the launch process, either upon test or cutover instance launch, the AWS
Replication agent is removed from the test or cutover instance, and will not run on
it.

## How do temporary credentials work?

The temporary credential mechanism was developed specifically to provide an easy and
secure way to install MGN Agents. The main flow of the temporary credentials' creation
process relies on generating an x509 certificate per agent and then using this x509
certificate to receive temporary IAM credentials. This process uses a similar mechanism
to the one used by [IAM
Roles Anywhere](../../../rolesanywhere/latest/userguide/introduction.md "../../../rolesanywhere/latest/userguide/introduction.md").

## Which Windows and Linux OSs support no-rescan upon reboot?

A shutdown (from the OS menu or CLI) of any supported Linux or Windows source server no
longer causes a rescan in MGN once the source server is restarted.

A rescan means that the agent on the source server rereads all blocks on all replicated disks
and transmits blocks that are different from the previously replicated data. A rescan is similar to
the initial sync but is faster because only blocks that are different need to be transmitted.

Rescans can still happen following a hard reboot, crashes, or when you add or remove disks to or
from the source server.

Supported OSs include:

**Windows Server**

- 2012r1
- 2012r2
- 2016
- 2019
- 2022
- 2025
- Windows 11

**Linux**

- CentOS 6–8, Stream 9, Stream 10
- Oracle 6–8
- RHEL 6–9.7, 10, 10.1
- Rocky 8–9.7, 10, 10.1
- SLES 12 and 15
- Debian 9–11
- Ubuntu 16, 18, 20, and 22
- Amazon Linux 2
- AlmaLinux 9.6, 9.7, 10, 10.1

###### Note

For Linux, no-rescan on reboot is supported only on environments that use
initramfs.
