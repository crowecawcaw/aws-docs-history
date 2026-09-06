

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Migration at scale using AWS Transform MGN
<a name="migration_at_scale"></a>

## Choose your agent-based vs agentless migration approach
<a name="agent-agentless"></a>

When planning your migration with AWS Transform MGN (MGN), review which approach best suits your environment and goals. MGN offers agentless and agent-based replication to migrate your workloads into AWS EC2. Agent-based replication is supported for both VMware and non-VMware environments, while agentless replication is supported only for VMware environments. 

1. Consider agentless replication if your security policies restrict installing agents at the OS level of your Virtual Machines. 

1. Review the network requirements for both, [agentless replication](https://docs.aws.amazon.com/mgn/latest/ug/installing-vcenter-appliance-mgn.html#client-notes-mgn) and [agent-based replication](https://docs.aws.amazon.com/mgn/latest/ug/preparing-environments.html#Network-Requirements), to determine the best approach for your needs. 

1. Before beginning your migration, ensure your planned operating systems are [supported](https://docs.aws.amazon.com/mgn/latest/ug/Supported-Operating-Systems.html) by your chosen replication method.

1. We recommend reviewing [AWS Prescriptive Guidance ](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-database-rehost-tools/mgn.html) for a rehost migration approach with MGN to ensure it meets your business needs.

## Cost planning
<a name="cost-planning"></a>

Before migrating, review the associated costs of using the service. For full pricing details, see the [MGN pricing page](https://aws.amazon.com/application-migration-service/pricing/). 

1. For each migrated server, MGN can be used free of MGN service charge, for 2,160 hours, which is 90 days when used continuously. Resources that are provisioned in the replication and migration processes, such as EC2, Amazon EBS volumes, and FSx for ONTAP storage, incur charges according to your account rates. 

1. Servers with high-volume workloads may require higher-performance replication resources, potentially increasing costs. Conduct network and storage benchmarking to determine the necessary staging area resources and estimate associated expenses. 

1. Plan your software licensing strategy when migrating servers. Discuss licensing terms with your operating system (OS) and software vendors as needed. 

1. When servers fail to launch, the Support team may request permission to run diagnostics. This iterative process helps the service team address edge cases causing launch failures. Diagnostic launches will incur charges based on the source and conversion server settings. Begin testing at least two weeks before your migration deadline. This allows time to resolve unexpected issues before the final cutover.

## Import/Export
<a name="import-export-at-scale"></a>

When performing large-scale migrations, you can use the [Import/Export](https://docs.aws.amazon.com/mgn/latest/ug/import-export.html) feature in AWS Transform MGN to efficiently stage your servers with the correct configurations. This feature uses a CSV template file with predefined columns that map to attributes of Waves, Applications, and Source Servers in MGN. The template includes columns for Launch Template settings, enabling bulk edits of these configuration options. Additionally, you can specify Tags to assist with cost center association, ensuring your cost planning remains accurate. By using the Import/Export feature, you can streamline your migration process and maintain better control over your server configurations and associated costs. 

## MGN Connector
<a name="mgn-connector-at-scale"></a>

When using AWS Transform MGN (MGN), first verify your servers meet the prerequisites for agent installation, then install the agent on all source servers. The [MGN Connector](https://docs.aws.amazon.com/mgn/latest/ug/mgn-connector.html) assists with these tasks. Before using the MGN Connector, verify its prerequisites and ensure the MGN Connector can communicate with source servers via SSH for Linux and WinRM for Windows to execute commands. 

## Network benchmarking
<a name="network-benchmarking"></a>

Network benchmarking is crucial for estimating data replication performance from a source environment to Amazon Web Services (AWS). The time required to replicate data depends on various factors, with network bandwidth performance being a key consideration. To accurately assess expected performance, we recommend testing the network bandwidth between the source environment and AWS. 

1. For this assessment, we recommend using the SSL connectivity and bandwidth test Amazon Machine Image (AMI). This AMI is preferable to alternatives like iperf because it performs the test with encryption, accurately simulating the replication agent's behavior. Detailed instructions for conducting this test are available for [Windows ](https://docs.aws.amazon.com/mgn/latest/ug/Replication-Related-FAQ.html#perform-connectivity-bandwidth-test) and [Linux ](https://repost.aws/knowledge-center/mgn-linux-fix-replication-lag#:~:text=Check%20replication%20speed%20and%20available%20bandwidth%20from%20the%20source%20server%20to%20the%20staging%20area%20subnet) servers. 

1. To determine whether the bandwidth test results are sufficient for your intended workloads, compare them with the storage benchmarking results discussed in the subsequent section. This comparison will provide a comprehensive view of your system's replication capabilities. After completing the network bandwidth test, proceed to the storage benchmarking section to finalize your performance assessment. Based on these combined results, you can determine if any network or storage optimizations are necessary before initiating data replication. This thorough evaluation ensures that your infrastructure is adequately prepared for efficient data transfer to AWS. 

## Storage benchmarking
<a name="storage-benchmarking"></a>

Performing storage benchmarking, in addition to network benchmarking, helps understand MGN replication resource provisioning and minimize performance issues. By understanding the total amount of storage and the daily change rate per server, you can determine if the network bandwidth will be sufficient for data replication with MGN. To capture storage performance metrics, use [iostat ](https://www.redhat.com/en/blog/io-reporting-linux) on Linux, and [Performance Monitor ](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc749249(v=ws.11)) on Windows. These tools will help you determine if the network bandwidth can keep up with the Writes/s on your disks. Additionally, these tests will reveal if the source storage device is encountering any bottlenecks that could affect replication performance. 

## Dedicated replication servers
<a name="dedicated-replication-servers-at-scale"></a>

After performing your storage benchmarking, you will have a clear understanding of which servers are busy and have a high rate of data change. In these cases, it may be best to set these servers to use [Dedicated Replication server ](https://docs.aws.amazon.com/mgn/latest/ug/replication-server-settings.html#dedicated-replication-server). 

1. This approach allows you to select an EC2 Instance type that can handle the IOPs and throughput from your source server. For a list of instance types and their EBS performance capabilities, refer to [Amazon EBS-optimized instance types ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html). When selecting an instance type, consider your cost planning, as this will incur charges based on the instance type selected. For pricing details, refer to [Amazon EC2 On-Demand Pricing ](https://aws.amazon.com/ec2/pricing/). 

1. To achieve optimum replication resource performance and cost savings, it is recommended to use [AWS Compute Optimizer ](https://docs.aws.amazon.com/compute-optimizer/latest/ug/getting-started.html). This service helps identify over or under provisioned EC2 and EBS resources, allowing you to optimize your setup. Before getting started with Compute Optimizer, review its [pricing ](https://aws.amazon.com/compute-optimizer/pricing/) to ensure it aligns with your budget and needs. 

## Wave planning
<a name="wave-planning-at-scale"></a>

Planning your migration in waves is crucial for successful large-scale migrations. With AWS Transform MGN you can group source servers and applications into waves, allowing you to migrate servers in batches rather than all at once.

1. Migrating servers in [waves ](https://docs.aws.amazon.com/mgn/latest/ug/waves.html) offers several benefits. It allows you to focus on a specific set of servers at a time and ensure the first wave operates as expected before proceeding to the next. 

1. Grouping interdependent servers into [applications ](https://docs.aws.amazon.com/mgn/latest/ug/applications.html) helps prevent issues during migration. For example, migrating member servers before domain controllers could cause authentication problems and other Active Directory-related issues. This approach enables a more controlled and reliable migration process, reducing the risk of widespread disruptions and allowing for adjustments between waves as needed. 

## Cutover planning
<a name="cutover-planning-at-scale"></a>

Planning for your cutover date is crucial for a successful migration. Work backwards from this date to schedule tests and address potential issues, ensuring you meet your migration timelines.

1. Conduct comprehensive [testing ](https://docs.aws.amazon.com/mgn/latest/ug/best_practices_mgn.html#Testing) at least two weeks before your planned migration date. This timeframe allows you to resolve or escalate specific problems with [AWS Support ](https://aws.amazon.com/premiumsupport/). For legacy operating systems or unique server configurations, allocate more than two weeks for testing, as complex issues may require additional time to resolve. 

1. If you need expert support during migration, consider using [AWS Countdown ](https://aws.amazon.com/premiumsupport/aws-countdown/). This service provides designated engineers from a team of AWS specialists who offer proactive guidance and troubleshooting assistance throughout your migration process. 

1. Train your team for AWS Cloud before migration to prepare for the change in the environment as upskilling your team is an important step in the migration journey. 

## Clustered servers
<a name="clustered-servers-at-scale"></a>

Migrating clustered servers to AWS requires careful planning due to its complexity. The AWS Transform MGN operates at the server level and is not cluster-aware, necessitating additional steps after cutover to ensure proper functionality. Consider the following high-level approach for migrating clusters with MGN:

1. Begin by migrating the primary node to AWS. This establishes the foundation for your cluster in the new environment. 

1. For secondary nodes, you have several options. You can use MGN to migrate these nodes after the primary node is operational in AWS. Alternatively, consider performing a native backup and restore, using log shipping, or employing other methods that suit your specific requirements. 

1. Once all nodes are in AWS, recreate the cluster configuration. This step is crucial for restoring the cluster's functionality in the new environment. Pay special attention to clusters with shared storage. In these cases, shared drives will appear as local disks on the cutover EC2 Instance. Depending on your migration plan, it may be more effective to exclude shared drives from MGN replication. Instead, consider migrating this data to an AWS shared-storage solution such as Amazon FSx. 

1. MGN’s lack of cluster awareness means post-cutover steps are often necessary to ensure your clustered servers work as expected. Tailor your migration approach based on your specific cluster configuration and requirements to achieve the best results. 

## Environment updates/changes
<a name="environment-updates-at-scale"></a>

We recommend maintaining a stable environment between the test launch and cutover launch to ensure a smooth migration. However, we recognize that critical updates may be necessary. In such cases, re-test before your cutover date to prevent unexpected issues during migration. The following changes could affect a migration with MGN:

1. Operating System updates or patches. 

1. Server configuration modifications. 

1. Network alterations. 

1. Security software updates. 

## API limits
<a name="api-limits-at-scale"></a>

API limits can cause migration delays during large-scale migrations. It's crucial to review the limits of all services used in AWS migrations, including [MGN ](https://docs.aws.amazon.com/mgn/latest/ug/MGN-service-limits.html), [EC2 ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html), [EBS ](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-resource-quotas.html), [FSx for ONTAP ](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/limits.html), and [VPC ](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html).

1. The default limit for MGN concurrent replicating servers ("Max Active Source Servers") is 150. Increasing this limit requires a detailed justification and migration plan. Contact [AWS Support ](https://aws.amazon.com/premiumsupport/) if you need to request a limit increase. 

1. EC2 and EBS service quotas will be based on your AWS Environment. Some customers may already have workloads running in AWS, while others may have none. Plan for the number of servers and disks being migrated to estimate how many EC2 instances will run in your account at a given time. This includes MGN Replication Server EC2 instances and their associated storage volumes (Amazon EBS or FSx for ONTAP). Additionally, account for the [EBS Snapshots ](https://docs.aws.amazon.com/mgn/latest/ug/Replication-Related-FAQ.html#How-Many-Snapshots) that MGN will create during the replication process. 

1. If you plan to use a single IP address for network traffic from the [staging area ](https://docs.aws.amazon.com/mgn/latest/ug/preparing-environments.html#TCP-443:~:text=tcp%20dpt%3A443-,Communication%20between%20the%20staging%20area%20subnet%20and%20AWS%20Application%20Migration%20Service%20over%20TCP%20port%20443,-Copy%20Plain%20Link) to the MGN endpoints (such as a security appliance or firewall), consult your AWS account team or AWS Support. Migrating in waves can help mitigate API limits or throttling issues. 

It can be challenging to anticipate all AWS service limitations when planning your migration. Testing with the same number of servers you intend to migrate will help identify potential limitations. Developing a comprehensive test and cutover plan will enable you to address these issues promptly, ensuring a smooth migration experience. By following these guidelines and planning carefully, you can effectively navigate API limits and service quotas during your AWS migration.