

# What Is AWS Transform MGN?
<a name="what-is-mgn"></a>

AWS Transform MGN (MGN) automates the migration of physical, virtual, and cloud servers to AWS with minimal downtime, typically cutover windows of minutes. MGN performs continuous block-level replication of your source servers and converts them for launch on AWS, allowing you to migrate large numbers of servers without compatibility issues or performance disruption.

MGN works across a broad range of operating systems including Windows Server and various Linux distributions, and supports both IPv4 and IPv6 network configurations. You can replicate into standard Availability Zones or AWS Local Zones. For more information about Local Zones, see [Replicating to AWS Local Zones](replication-server-settings.md#local-zone-snapshots).

The service uses three configurable templates (replication, launch, and post-launch) to control how servers are replicated, launched, and configured after migration. Template settings are applied to each newly added server, and you can override settings for individual servers at any time.

To manage migrations at scale, you can group servers into applications and applications into waves. Configuration changes and actions such as launch, cutover, and archival can be performed at the server, application, or wave level, enabling bulk operations across large environments.

After migration, you can use AWS services to replatform or refactor your applications, making rehosting a fast first step toward modernization.

## Accessing the AWS Transform MGN console
<a name="accessing-console"></a>

You can access AWS Transform MGN through the AWS Management Console or through the following link:

[https://console.aws.amazon.com/mgn/home](https://console.aws.amazon.com/mgn/home)

## Supported AWS Regions
<a name="supported-regions"></a>

The following AWS Regions are supported by AWS Transform MGN:



| Region name | Region identity | Support in AWS Transform MGN | 
| --- | --- | --- | 
| US East (Ohio) | us-east-2 | Yes | 
| US East (N. Virginia) | us-east-1 | Yes | 
| US West (N. California) | us-west-1 | Yes | 
| US West (Oregon) | us-west-2 | Yes | 
| Africa (Cape Town) | af-south-1 | Yes | 
| Asia Pacific (Hong Kong) | ap-east-1 | Yes | 
| Asia Pacific (Taipei) | ap-east-2 | Yes | 
| Asia Pacific (Thailand) |  ap-southeast-7 | Yes | 
| Asia Pacific (Jakarta) | ap-southeast-3 | Yes | 
| Asia Pacific (Malaysia) | ap-southeast-5 | Yes | 
| Asia Pacific (New Zealand) | ap-southeast-6 | Yes | 
| Asia Pacific (Melbourne) | ap-southeast-4 | Yes | 
| Asia Pacific (Mumbai) | ap-south-1 | Yes | 
| Asia Pacific (Hyderabad) | ap-south-2 | Yes | 
| Asia Pacific (Osaka) | ap-northeast-3 | Yes | 
| Asia Pacific (Seoul) | ap-northeast-2 | Yes | 
| Asia Pacific (Singapore) | ap-southeast-1 | Yes | 
| Asia Pacific (Sydney) | ap-southeast-2 | Yes | 
| Asia Pacific (Tokyo) | ap-northeast-1 | Yes | 
| Canada (Central) | ca-central-1 | Yes | 
| Canada West (Calgary) | ca-west-1 | Yes | 
| Europe (Frankfurt) | eu-central-1 | Yes | 
| Europe (Zurich) | eu-central-2 | Yes | 
| Europe (Ireland) | eu-west-1 | Yes | 
| Europe (London) | eu-west-2 | Yes | 
| Europe (Paris) | eu-west-3 | Yes | 
| Europe (Milan) | eu-south-1 | Yes | 
| Europe (Spain) | eu-south-2 | Yes | 
| Europe (Stockholm) | eu-north-1 | Yes | 
| Israel (Tel Aviv) | il-central-1 | Yes | 
| Middle East (Bahrain) | me-south-1 | Yes | 
| Middle East (UAE) | me-central-1 | Yes | 
| Mexico (Central) | mx-central-1 | Yes | 
| South America (São Paulo) | sa-east-1 | Yes | 
| AWS GovCloud (US-East) | us-gov-east-1 | Yes | 
| AWS GovCloud (US-West) | us-gov-west-1 | Yes | 

Learn more about [AWS Regional services](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

AWS Transform MGN regional support includes [AWS Local Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-local-zones) associated with the above supported regions.

**Important**  
MGN supports IPv6 in the regions where Amazon EC2 dual-stack endpoints are present. For the list of EC2 dual-stack endpoints, see [Dual-stack (IPv4 and IPv6) endpoints](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-endpoints.html#ipv6) in the *Amazon EC2 Developer Guide*.

## Terminology
<a name="mgn-terminology"></a>

The following terms are used throughout this guide. Italics indicate a term that is defined elsewhere in this list.

Application  
A group of *source servers* that you associate with each other, such as a cluster of servers with dependencies between them. You can monitor the migration status of an application and perform bulk operations on its servers. For more information, see [Associate a Group of Servers with an Application](applications.md).

AWS Replication Agent  
Software that you install on each *source server* to add it to MGN. The agent performs an initial block-level read of the server's volumes, and then captures writes and replicates block-level changes to the *replication server*. For more information, see [Installing the AWS Replication Agent](agent-installation.md).

Conversion server  
A server that MGN launches and manages automatically as part of a launch job. It converts the disks of your *source server* to boot and run on AWS. For more information, see [What does the AWS Transform MGN Machine Conversion Server do?](AWS-Related-FAQ.md#What-Conversion-Server-Do)

Cutover instance  
The instance in AWS that your *source server* migrates to. Each new cutover instance reflects the most up-to-date state of the source server, but it doesn't receive changes that occur on the source server after it launches. For more information, see [Launching cutover instances](launch-cutover.md).

Data replication status  
The current state of data replication for a *source server*, such as **Initial sync**, **Healthy**, **Lagging**, or **Stalled**. For more information, see [Understand data replication status](source-server-migration-metrics.md#source-server-migration-metrics-status).

Finalize cutover  
The action you take after you confirm that a *cutover instance* works as expected. Finalizing the cutover stops data replication, discards all replicated data, terminates the AWS resources used for data replication, and uninstalls the *AWS Replication Agent* from the *source server*. For more information, see [Finalize cutover](server-post-migration.md#server-post-migration-finalize-cutover).

Initial sync  
The initial copying of data from a *source server* to AWS, which begins automatically after you install the *AWS Replication Agent*. The server remains in the **Not ready** lifecycle state until the initial sync completes. For more information, see [Server undergoing initial sync](migration-dashboard.md#initiation).

Launch settings  
The settings that determine how a *test instance* or *cutover instance* is launched for a specific *source server*. They include the general launch settings and the EC2 launch template. For more information, see [Launch settings](launch-settings.md).

Launch template  
The account-level template that controls how MGN launches instances in AWS. Its settings are the default *launch settings* for each newly added *source server*. For more information, see [Launch template](launch-template.md).

MGN connector  
An automation server installed in your environment that lets you run commands on multiple *source servers*, such as verifying installation prerequisites and installing the *AWS Replication Agent*. MGN connectors help with large-scale migrations across multiple operating systems and data centers. For more information, see [MGN Connectors](mgn-connector.md).

Migration lifecycle  
The stage that a *source server* has reached in its migration, from **Not ready** through **Ready for testing**, **Test in progress**, **Ready for cutover**, and **Cutover in progress**, to **Cutover complete**. For more information, see [Understand the migration lifecycle metric](source-server-migration-metrics.md#source-server-migration-metrics-lifecycle).

Post-launch actions  
Actions that MGN performs after a server is launched in AWS, such as disaster recovery configuration, operating system conversion, and license and subscription changes. You control them through the post-launch template, which you must first activate at the account level. For more information, see [Post-launch template](post-launch-settings.md).

Replication server  
A lightweight Amazon EC2 instance that replicates data between your *source servers* and AWS. MGN launches and terminates replication servers automatically in the *staging area subnet*. For more information, see [Replication template reference](replication-server-settings.md).

Replication template  
The account-level template that determines how data is replicated from your *source servers* to AWS. It includes settings such as the replication server instance type, target storage type, and security groups. For more information, see [Replication template](replication-settings-template.md).

Rescan  
An automatic re-read of all the blocks on the replicated disks of a *source server*. For more information, see [What is a rescan and how long does it take?](Replication-Related-FAQ.md#How-Long-Rescan)

Source server  
A physical, virtual, or cloud server that you migrate to AWS. You add a source server to MGN by installing the *AWS Replication Agent* on it. For more information, see [Source Servers in AWS Transform MGN](source-servers.md).

Staging area subnet  
The subnet that MGN uses as a staging area for data replicated from your *source servers*, and in which your *replication servers* are launched. You specify it in the *replication template*, and you can override it for specific source servers. For more information, see [Staging area subnet](replication-server-settings.md#subnet).

Test instance  
An instance that you launch in AWS to verify that a *source server* functions properly before cutover. Each new test deletes any previously launched test instance and launches a new one that reflects the most up-to-date state of the source server. For more information, see [Launching test instances](launching-test-servers.md).

Wave  
A logical group of *source servers* and *applications* that describes your migration plan over time. You can monitor a wave's migration status and perform bulk operations on its applications. For more information, see [Group Source Servers and Applications in Waves](waves.md).

## MGN technical training materials
<a name="mgn-training"></a>

The following technical trainings are available for MGN:
+ [AWS Transform MGN - A Technical Introduction](https://www.aws.training/Details/eLearning?id=71732)
+ [Blog posts related to MGN](https://aws.amazon.com/application-migration-service/resources/#Blog_posts_.26_articles)
+ [MGN video playlist](https://www.youtube.com/playlist?list=PLhr1KZpdzukcQMnw93OpyqLTsx-Y-lC7i)