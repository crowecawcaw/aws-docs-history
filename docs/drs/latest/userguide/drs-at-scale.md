

# Disaster recovery at scale
<a name="drs-at-scale"></a>

When protecting a large number of servers (100\+) with AWS Elastic Disaster Recovery, additional planning is required to ensure reliable replication, successful recovery, and manageable operations. This section provides guidance for operating Elastic Disaster Recovery at scale.

**Topics**
+ [Account and Region planning](#at-scale-account-planning)
+ [Network planning and benchmarking](#at-scale-network-planning)
+ [Storage benchmarking](#at-scale-storage-benchmarking)
+ [Agent deployment at scale](#at-scale-agent-deployment)
+ [DR readiness and compliance monitoring](#at-scale-dr-readiness)
+ [Service quotas and API limits](#at-scale-service-quotas)
+ [Recovery planning at scale](#at-scale-recovery-planning)

## Account and Region planning
<a name="at-scale-account-planning"></a>

A single AWS account supports up to 300 concurrently replicating source servers. For larger environments, distribute source servers across multiple staging accounts or target AWS Regions.
+ Use [multiple staging accounts](multi-account.md) to scale beyond the 300-server limit per account.
+ Plan your account structure early — moving source servers between accounts requires reinstalling the agent.
+ When using multiple accounts, ensure that EBS encryption keys (KMS) are shared across accounts if you use custom encryption.
+ Establish a consistent IAM policy management strategy across all accounts. Use AWS Organizations and Service Control Policies (SCPs) to enforce guardrails.

## Network planning and benchmarking
<a name="at-scale-network-planning"></a>

Network bandwidth is a critical factor for replication performance at scale. Before deploying agents, benchmark your network to ensure it can sustain the required throughput.

1. **Benchmark network bandwidth:** Test the bandwidth between your source environment and the staging area subnet using the SSL connectivity and bandwidth test AMI. This test uses encryption, accurately simulating the replication agent's behavior. Instructions are available for [performing the bandwidth test](https://docs.aws.amazon.com/drs/latest/userguide/Replication-Related-FAQ.html#perform-connectivity-bandwidth-test).

1. **Plan for aggregate bandwidth:** Calculate the total write throughput across all source servers (see [calculating required bandwidth](comm-bandwidth-planning.md#Calculating-Bandwidth)). Ensure your network connection (Direct Connect, VPN, or internet) can sustain this aggregate throughput with headroom for spikes.

1. **IP planning:** Plan your staging area and recovery VPC CIDR ranges to accommodate the number of replication servers, recovery instances, and any network infrastructure (NAT gateways, transit gateways, load balancers). Ensure there is no IP overlap between source and recovery environments if using VPN or Direct Connect.

## Storage benchmarking
<a name="at-scale-storage-benchmarking"></a>

Understanding the storage write patterns of your source servers helps you provision appropriate replication resources and avoid replication lag.

1. Capture storage performance metrics on your source servers using `iostat` on Linux or Performance Monitor on Windows. Focus on write IOPS and write throughput (MB/s) per disk.

1. Servers with high write rates (such as database servers) may require [dedicated replication servers](https://docs.aws.amazon.com/drs/latest/userguide/replication-server-settings.html#dedicated-replication-server) with an instance type that can handle the required EBS IOPS and throughput.

1. Consider excluding high-churn volumes that are not needed for disaster recovery (such as database tempdb or backup disks) using the `--devices` installer parameter to reduce replication load.

## Agent deployment at scale
<a name="at-scale-agent-deployment"></a>

Deploying the AWS Replication Agent across hundreds of servers requires automation. Consider the following approaches:
+ Use configuration management tools (such as AWS Systems Manager Run Command, Ansible, or Chef) to deploy the agent across multiple servers simultaneously.
+ Use the `--no-prompt` installer parameter for unattended installation. Combine with `--devices` to specify disks explicitly when automatic detection is not suitable.
+ Deploy agents in batches rather than all at once to avoid overwhelming the staging area network and to stay within API limits.
+ Verify that all source servers meet the [installation prerequisites](agent-installation-instructions.md) before beginning deployment.

## DR readiness and compliance monitoring
<a name="at-scale-dr-readiness"></a>

At scale, manually monitoring replication health and drill compliance is impractical. Implement automated monitoring to maintain DR readiness.

1. **Replication health:** Use the Elastic Disaster Recovery API (`describe-source-servers`) or [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/) to monitor replication state across all source servers. Alert on servers in **Stalled**, **Disconnected**, or **Lag** states.

1. **Drill compliance:** Track when each source server was last tested. Use the `describe-source-servers` API to retrieve the last launch date and type (drill or recovery) from the `lifeCycle.lastLaunch` field. Flag servers that have not been drilled within your organization's required interval.

1. **Dashboard:** For multi-account environments, consider building a centralized dashboard using AWS Organizations and cross-account IAM roles to aggregate replication status across all accounts.

## Service quotas and API limits
<a name="at-scale-service-quotas"></a>

Large-scale deployments can encounter service quota limits. Review and plan for the following:
+ **Elastic Disaster Recovery quotas:** Maximum 300 concurrently replicating source servers per account, 100 source servers per recovery job, 500 source servers across all active jobs, and 20 concurrent jobs. See [Elastic Disaster Recovery service quotas](https://docs.aws.amazon.com/general/latest/gr/drs.html#limits_drs).
+ **Amazon EC2 quotas:** Plan for the number of replication server instances, recovery instances, and associated EBS volumes that will run concurrently. Request quota increases in advance.
+ **EBS snapshot limits:** Elastic Disaster Recovery creates EBS snapshots for point-in-time recovery. At scale, the number of snapshots can grow significantly based on your retention policy.
+ **API throttling:** When using automation to manage large numbers of servers, implement exponential backoff and retry logic to handle API throttling gracefully.

## Recovery planning at scale
<a name="at-scale-recovery-planning"></a>

Recovering hundreds of servers simultaneously requires careful orchestration:
+ **Group servers by application:** Identify dependencies between servers and group them so that dependent servers are recovered together in the correct order.
+ **Stagger recovery jobs:** Launch recovery instances in batches to stay within the concurrent job limits (20 concurrent jobs, 100 servers per job, 500 servers across all active jobs) and to avoid overwhelming the target environment.
+ **Automate recovery orchestration:** Use the Elastic Disaster Recovery API and AWS Step Functions or similar orchestration tools to automate the recovery sequence, including post-launch validation.
+ **Plan VPC capacity:** Ensure your recovery VPCs have sufficient IP addresses, subnets, and network resources for all recovery instances.