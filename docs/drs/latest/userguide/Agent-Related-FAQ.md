# Agent related

## What does the AWS Replication Agent do?

The AWS Replication Agent performs an initial block-level read of the content of
any volume attached to the server and replicates it to the replication server. The
Agent then acts as an OS-level read filter to capture writes and synchronizes any
block level modifications to the Elastic Disaster Recovery replication server,
ensuring near-zero RPO.

## What kind of data is transferred between the Agent and

the AWS Elastic Disaster Recovery Service Manager?

The AWS Replication Agent sends the following types of information to the AWS Elastic Disaster Recovery Service Manager:

- Monitoring metrics of the Agent itself
- Replication status (started, stalled, resumed)
- Backlog information
- OS and hardware information.

When an Agent is installed on a source server, it collects the following
information on the machine:

- Host name and ID.
- List of CPUs including models and number of cores
- Amount of RAM
- Hardware and OS information.
- Number of disks and their size – in Windows, disk letters; in Linux, block device
  names.
- Installed applications (Windows)
- Installed Packages (Linux)
- Running services.
- Machine's Private IP address.

## Can a proxy server be used between the source server and the

Elastic Disaster Recovery Console?

Yes. You can configure the proxy either by using an environment variable prior to the installation
(Linux and Windows), or by using the `--proxy-address` flag in the Linux installer.

Using the installer:
`./aws-replication-installer-init --proxy-address https://PROXY:PORT/`

Using environment variable:
`export https_proxy=https://PROXY:PORT/;
 ./aws-replication-installer-init`

Make sure the proxy has a trailing forward slash (`/`).

## What are the pre-requisites needed to install the

AWS Replication Agent?

The installation requirements for source server depend on the type of OS that the
server runs – either Linux or Windows.

[View the prerequisites.](installation-requirements.md "installation-requirements.md")

## What ports does the AWS Replication Agent utilize?

The Agent utilizes TCP Port 443 to communicate to the Elastic Disaster Recovery Service
Manager and TCP Port 1500 for replication to AWS.

## What kind of resources does the AWS Replication Agent

utilize?

The AWS Replication Agent is lightweight and nondisruptive. The agent utilizes
approximately 5% CPU and 300 MB of RAM.

## Can Elastic Disaster Recovery migrate containers?

Elastic Disaster Recovery only supports the replication of full servers. Nevertheless,
Elastic Disaster Recovery replicates on a server level and therefore any containers within
the selected servers will be replicated.

## Does the AWS Replication Agent cache any data to

disk?

Elastic Disaster Recovery does not write any cache or do any sort of journalling
to disk. The Agent holds a buffer which is large enough to map all volume's blocks
~250 MB in memory.

The Agent then acts as a sort of write filter and will replicate changed blocks
directly from memory to the replication server. In cases where the data no longer in
memory, the Agent will read the block from the volume directly. This is the case
where you may see backlog in the Elastic Disaster Recovery Console. The cause of
this is the volume of change is greater than the bandwidth available.

## How is communication between the AWS Replication

Agent and the Elastic Disaster Recovery Service Manager secured?

All communication is encrypted using SSL. In addition, each Agent is assigned a key during
installation which is used to encrypt all traffic. All keys are unique and are not shared across
multiple Agents.

## Is it possible to change the port the AWS Replication

Agent utilizes from TCP Port 1500 to a different port?

No. The Elastic Disaster Recovery Agent can only utilize TCP Port 1500 for replication.

## How do I manually uninstall the Elastic Disaster

Recovery Agent from a server?

Please refer to:[Uninstalling the agent](uninstalling-agent.md "uninstalling-agent.md").

## When do I need to reinstall the Agent?

Agent re-installations are required in these cases:

- After adding new volumes if the [Automatic replication of new disks](volumes-drs.md#auto-replicate "volumes-drs.md#auto-replicate") option is not activated for the source server where the volume is added.
- Windows OS upgrades (ex. Windows Server 2012 to Windows Server 2016)
- Some new features require a re-installation to apply. In this case, the feature documentation will specifically state that this is a requirement for the feature to be activated.

## How much bandwidth does the AWS Replication Agent

consume?

The AWS Replication Agent opens up to five connections and will attempt to maximize
available bandwidth.

Throttling can be activated by selecting the specific server and selecting the **Settings** page in the Elastic Disaster Recovery Console.

## How many disks can the AWS Replication Agent

replicate?

The Agent can replicate up to 50 disks from a single server. Ensure that the replication server instance type supports at least the number of disks being replicated.

## Is it possible to add a disk to replication

without a complete resync of any disks that have already been replicated??

When you add a disk to a source server, AWS Elastic Disaster Recovery will automatically identify it
and add it to the **Disk settings** tab in the console.

This feature is activated automatically for newly added servers. [Learn how to deactivate or reactivated this feature.](volumes-drs.md#auto-replicate "volumes-drs.md#auto-replicate")

## Which Windows and Linux OSs support no-rescan upon

reboot?

A shutdown (from the OS menu or CLI) of any supported Linux or Windows
source server no longer causes a rescan in DRS once the source server is restarted.
A rescan means that the agent on the source server rereads all blocks on all replicated disks
and transmits blocks that are different from the previously replicated data.
A rescan is similar to the initial sync but is faster because only blocks that are different need to be
transmitted.

Rescans can still happen following a hard reboot, crashes, or when you add or remove disks to or from
the source server. In addition, a rescan will occur if the underline Storage types do not use static [DUIDs](https://learn.microsoft.com/en-us/windows-hardware/drivers/storage/device-unique-identifiers--duids--for-storage-devices "https://learn.microsoft.com/en-us/windows-hardware/drivers/storage/device-unique-identifiers--duids--for-storage-devices") (such as 3PARdata).
Supported OSs include:

**Windows Server**

- 2012 and newer

**Linux**

- CentOS 6–8
- Oracle 6–8
- RHEL 6–9
- Rocky 8 and 9
- SLES 12 and 15
- Debian 9–11
- Ubuntu 16, 18, 20, and 22
- Amazon Linux 2

## No-Rescan Upon Reboot Limitations

A rescan may still occur in certain circumstances, including:

Hard Reboot or Power Loss.

###### Important

**A rescan duration may impact your RPO**

- While a rescan is conducted, a point of time recovery cannot be made.
- If a disaster occurs during the rescan
  you will only be able to restore point of time from before the rescan began.
  This could affect your ability to meet your RPO.

## How do temporary credentials work?

The temporary credential mechanism was developed specifically to provide an easy
and secure way to install AWS DRS Agents. The main flow of the temporary
credentials' creation process relies on generating a x509 certificate per agent and
then using this x509 certificate to receive temporary IAM credentials. This process
utilizes a similar mechanism to the one used by [IAM Roles Anywhere](../../../rolesanywhere/latest/userguide/introduction.md "../../../rolesanywhere/latest/userguide/introduction.md").

## Where can I find the AWS DRS Replication Agent

logs

The AWS DRS agent logs are stored in agent.log.0:

- **Linux:** /var/lib/aws-replication-agent/agent.log.0
- **Windows 64 bit:** C:\Program Files
  (x86)\AWS Replication Agent\agent.log.0

In addition, you can review the installation log located in:
<install_path>\aws_replication_agent_installer.log
