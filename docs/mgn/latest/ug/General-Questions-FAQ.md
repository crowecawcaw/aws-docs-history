

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# General questions
<a name="General-Questions-FAQ"></a>

This section contains answers to general questions about AWS Transform MGN.

**Topics**
+ [Why was AWS Application Migration Service renamed to AWS Transform MGN?](#mgn-rebranding)
+ [What data is stored on and transmitted through MGN service?](#What-Data-Stored)
+ [Can MGN protect or migrate physical servers?](#Can-CloudEndure-Protect-Migrate-Servers)
+ [What is there to note regarding SAN/NAS support?](#SAN-NAS-Support)
+ [What should I consider when replicating Active Directory?](#What-Active-Directory)
+ [Does AWS Transform MGN support Windows License migration?](#Does-Windows-License-Migration)
+ [Can you perform an OS (Operating System) upgrade with AWS Transform MGN?](#Can-OS-Upgrade)
+ [Can I use AWS Transform MGN to migrate servers from VMware Cloud on AWS (VMC) to Amazon EC2?](#vmc)
+ [When should I use AWS Elastic Disaster Recovery (AWS DRS) for migration?](#using-drs)
+ [What are the AWS Transform MGN quota limits?](#MGN-service-limits-faq)
+ [What are the Private APIs used by MGN to define actions in the IAM Policy?](#mgn-apis)
+ [How does AWS Transform MGN interact with Interface VPC Endpoints?](#mgn-and-vpc)
+ [How do I use MGN with CloudWatch and EventBridge dashboards?](#mgn-and-monitoring)
+ [What happens if I use a custom DNS?](#custom-DNS)

## Why was AWS Application Migration Service renamed to AWS Transform MGN?
<a name="mgn-rebranding"></a>

AWS Application Migration Service has been renamed to AWS Transform MGN. The new name reflects the close link between MGN and AWS Transform. AWS Transform uses MGN replication technology to rehost servers.

You can access AWS Transform MGN in two ways:
+ Use the MGN console directly in the AWS console for a hands-on experience.
+ Use the AWS Transform workflow, which automates discovery, wave planning, network setup, landing zone creation, rehosting and containerization.

At the rehosting stage, you can continue with the agentic workflow or switch to the MGN console if you prefer a more hands-on experience.

AWS Transform is also available through Kiro, Claude, Cursor, and Codex through the AWS Transform MCP server.

## What data is stored on and transmitted through MGN service?
<a name="What-Data-Stored"></a>

MGN stores only configuration and log data. This data is kept in an encrypted database. Your replicated data stays in your own VPC. All data in transit is encrypted.

## Can MGN protect or migrate physical servers?
<a name="Can-CloudEndure-Protect-Migrate-Servers"></a>

Yes. MGN can migrate both virtual and physical servers. The replication process works at the OS level, so it handles both server types the same way.

## What is there to note regarding SAN/NAS support?
<a name="SAN-NAS-Support"></a>

If the disks are represented as block devices on the machine, as most SAN are, AWS Transform MGN replicates them transparently, just like actual local disks.

If the disks are mounted over the network, such as an NFS share, as most NAS implementations are, the AWS Replication Agent would need to be installed on the actual NFS server to replicate the disk.

## What should I consider when replicating Active Directory?
<a name="What-Active-Directory"></a>

There are two main approaches when it comes to migrating Active Directory or domain controllers from a disaster:

1. Replicating the entire environment, including the AD server(s) – in this approach it is recommended to launch the test or cutover AD servers first, wait until it's up and running, and then launch the other test or cutover instances, to make sure the AD servers are ready to authenticate them.

1. Leaving the AD server(s) in the source environment – in this approach, the test or cutover instances communicate back to the AD server in the source environment and take the source server's place in the AD automatically.

   In this case, it is important to conduct any tests using an isolated subnet in the AWS cloud, so to avoid having the test or cutover instances communicate into the source AD server outside of a cutover.

## Does AWS Transform MGN support Windows License migration?
<a name="Does-Windows-License-Migration"></a>

AWS Transform MGN conforms to the [Microsoft Licensing on AWS](https://aws.amazon.com/windows/resources/licensing/) guidelines. 

## Can you perform an OS (Operating System) upgrade with AWS Transform MGN?
<a name="Can-OS-Upgrade"></a>

Yes. AWS Transform MGN allows you to [perform an OS upgrade](predefined-post-launch-actions.md#predefined-windows-upgrade) using a predefined action. The action clones your machine and upgrades the clone. After the upgrade, verify that the cloned machine is working well, and then you can begin using it.

## Can I use AWS Transform MGN to migrate servers from VMware Cloud on AWS (VMC) to Amazon EC2?
<a name="vmc"></a>

 Yes, you can. For migrations of source servers from [VMC](https://aws.amazon.com/vmware/) to EC2 you have two options. You can install the agentless appliance in your VMC environment, and migrate your servers using [agentless replication](agentless-mgn.md), or install the [AWS replication agent](agent-installation.md) on each of your source servers, and use agent-based replication for your migration. 

## When should I use AWS Elastic Disaster Recovery (AWS DRS) for migration?
<a name="using-drs"></a>

 In cases that DRS supports a feature that does not exist in MGN, DRS can be used for migration. You can install the DRS replication agent on your source servers. Following replication, you can launch recovery instances in your target environment, to complete the migration. 

 DRS can be used for migration, as the DRS and MGN services use shared technology for performing block level replication. Both MGN and DRS have a replication agent, for replicating servers into a staging area in AWS. MGN supports launching test and cutover instances from the staging area. DRS supports launching recovery instances from the staging area. The technology used by both of these services for launching instances in AWS is very similar. DRS also has the capability to failback to the source environment, after the source environment has recovered. This capability does not exist in MGN. 

 Note that you cannot install the DRS and MGN agents on the same server at the same time. If you already installed the MGN agent on a server, and want to use DRS for migration, you must uninstall the MGN agent before installing the DRS agent. 

 Note that there are costs associated with using the DRS service. For DRS pricing information see [AWS Elastic Disaster Recovery pricing](https://aws.amazon.com/disaster-recovery/pricing/). 

## What are the AWS Transform MGN quota limits?
<a name="MGN-service-limits-faq"></a>

The following are the AWS Transform MGN service quota limits:


| Name | Default | Description | 
| --- | --- | --- | 
| Concurrent jobs in progress | Each supported AWS Region: 20 | Launching a test or cutover instance, or a cleanup action is considered a job. Multiple servers launched together count as a single job. This parameter is the maximum number of Jobs that can be run concurrently. Jobs that are Completed are not counted against this quota. | 
| Max active source servers | Each supported AWS Region: 150 | The maximum number of servers that can be actively replicating at any time. For larger migrations contact Support. | 
| Max non-archived source servers | Each supported AWS Region: 4,000 | This parameter is used for agentless migrations. This is the max number of servers that can be managed by MGN, in non-archived state. This includes the servers that are actively replicating, as well as any servers whose replication has not yet started. The number of actively replicating servers is controlled by the parameter Max active source servers. | 
| Max source servers in a single job | Each supported AWS Region: 200 | Launching a test or cutover instance, or a cleanup action is considered a job. If you select multiple servers, and perform one of these actions, they are grouped into a single job. This is the maximum number of servers that can be grouped into a single Job. | 
| Max source servers in all jobs | Each supported AWS Region: 200 | Launching a test or cutover instance, or a cleanup action is considered a job. This is the maximum total number of servers that can be configured in all active Jobs. Jobs that are Completed are not counted against this quota. | 
| Max total source servers per AWS account | Each supported AWS Region: 50,000 | This parameter is the maximum total servers, both active and archived, that can be migrated in a single account in each AWS Region. Servers that are deleted, are not counted against this quota. | 
| Max concurrent jobs per source server | Each supported AWS Region: 1 | Launching a test or cutover instance, or a cleanup action is considered a job. This is the maximum number of active Jobs, that can be configured per server. Jobs that are Completed are not counted against this quota. | 

 You can learn about the AWS Transform MGN limits in the [AWS General Reference](https://docs.aws.amazon.com/general/latest/gr/mgn.html).

## What are the Private APIs used by MGN to define actions in the IAM Policy?
<a name="mgn-apis"></a>

MGN uses the following Private API resources as actions in the IAM Policy. [Learn more about Actions, resources, and condition keys for MGN. ](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsapplicationmigrationservice.html)
+ BatchCreateVolumeSnapshotGroupForMgn – Grants permission to create volume snapshot group.
+ BatchDeleteSnapshotRequestForMgn – Grants permission to batch delete snapshot request.
+ DescribeReplicationServerAssociationsForMgn – Grants permission to describe replication server associations.
+ DescribeSnapshotRequestsForMgn – Grants permission to describe snapshots requests.
+ GetAgentCommandForMgn – Grants permission to get agent command.
+ GetAgentConfirmedResumeInfoForMgn – Grants permission to get agent confirmed resume info.
+ GetAgentInstallationAssetsForMgn – Grants permission to get agent installation assets.
+ GetAgentReplicationInfoForMgn – Grants permission to get agent replication info.
+ GetAgentRuntimeConfigurationForMgn – Grants permission to get agent runtime configuration.
+ GetAgentSnapshotCreditsForMgn – Grants permission to get agent snapshots credits.
+ GetChannelCommandsForMgn – Grants permission to get channel commands.
+ NotifyAgentAuthenticationForMgn – Grants permission to notify agent authentication.
+ NotifyAgentConnectedForMgn – Grants permission to notify agent is connected.
+ NotifyAgentDisconnectedForMgn – Grants permission to notify agent is disconnected
+ NotifyAgentReplicationProgressForMgn – Grants permission to notify agent replication progress.
+ RegisterAgentForMgn – Grants permission to register agent.
+ SendAgentLogsForMgn – Grants permission to send agent logs.
+ SendAgentMetricsForMgn – Grants permission to send agent metrics.
+ SendChannelCommandResultForMgn – Grants permission to send channel command result.
+ SendClientLogsForMgn – Grants permission to send client logs.
+ SendClientMetricsForMgn – Grants permission to send client metrics.
+ UpdateAgentBacklogForMgn – Grants permission to update agent backlog.
+ UpdateAgentConversionInfoForMgn – Grants permission to update agent conversion info.
+ UpdateAgentReplicationInfoForMgn – Grants permission to update agent replication info.
+ UpdateAgentReplicationProcessStateForMgn – Grants permission to update agent replication process state.
+ UpdateAgentSourcePropertiesForMgn – Grants permission to update agent source properties.
+ CreateVcenterClientForMgn – Grants permission to create a vCenter client.
+ GetVcenterClientCommandsForMgn – Grants permission to get vCenter client commands.
+ SendVcenterClientCommandResultForMgn – Grants permission to send vCenter client command result.
+ SendVcenterClientLogsForMgn – Grants permission to send vCenter client logs.
+ SendVcenterClientMetricsForMgn – Grants permission to send vCenter client metrics.
+ NotifyVcenterClientStartedForMgn – Grants permission to notify vCenter client started.
+ IssueAgentCertificateForMgn – Grants permission to send certificate signing request.



## How does AWS Transform MGN interact with Interface VPC Endpoints?
<a name="mgn-and-vpc"></a>

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish a private connection between your VPC and AWS Transform MGN. You can use this connection to allow AWS Transform MGN to communicate with your resources on your VPC without going through the public internet.

Amazon VPC is an AWS service that you can use to launch AWS resources in a virtual network that you define. With a VPC, you have control over your network settings, such as the IP address range, subnets, route tables, and network gateways. With VPC endpoints, the routing between the VPC and AWS services is handled by the AWS network, and you can use IAM policies to control access to service resources.

To connect your VPC to AWS Transform MGN, you define an *interface VPC endpoint* for AWS Transform MGN. An interface endpoint is an elastic network interface with a private IP address that serves as an entry point for traffic destined to a supported AWS service. The endpoint provides reliable, scalable connectivity to AWS Transform MGN without requiring an internet gateway, network address translation (NAT) instance, or VPN connection. For more information, see [What is Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/) in the *Amazon VPC User Guide*.

Interface VPC endpoints are powered by AWS PrivateLink, an AWS technology that allows private communication between AWS services using an elastic network interface with private IP addresses. For more information, see [AWS PrivateLink](https://aws.amazon.com/privatelink/).

For more information, see [Getting Started](https://docs.aws.amazon.com/vpc/latest/userguide/GetStarted.html) in the *Amazon VPC User Guide*.

## How do I use MGN with CloudWatch and EventBridge dashboards?
<a name="mgn-and-monitoring"></a>

You can monitor AWS Transform MGN using CloudWatch, which collects raw data and processes it into readable, near real-time metrics. AWS Transform MGN sends events to Amazon EventBridge whenever a source server launch has completed, a source server reaches the READY\_FOR\_TEST lifecycle state for the first time, and when the data replication state becomes stalled or when the data replication state is no longer Stalled. You can use EventBridge and these events to write rules that take actions, such as notifying you, when a relevant event occurs. 

You can see MGN in CloudWatch automatic dashboards: 

![CloudWatch cross service dashboard showing metrics for MGN and EC2.](https://docs.aws.amazon.com/mgn/latest/ug/images/cw1.png)




![MGN dashboard showing metric graphs for lag duration, backlog, duration since last test, elapsed replication duration, and server counts.](https://docs.aws.amazon.com/mgn/latest/ug/images/cw2.png)


MGN events can be selected when defining a rule from the EventBridge console:

![Event source dropdown showing MGN filter with three MGN event types listed below.](https://docs.aws.amazon.com/mgn/latest/ug/images/EB-cw3.jpg)


[Learn more about monitoring MGN](monitoring-overview.md). 

## What happens if I use a custom DNS?
<a name="custom-DNS"></a>

Custom DNS settings can cause issues in the replication servers.

Therefore, if you are using a custom DNS, you need to add a TCP port 53 to the security group outbound rules, for replication and conversion servers.