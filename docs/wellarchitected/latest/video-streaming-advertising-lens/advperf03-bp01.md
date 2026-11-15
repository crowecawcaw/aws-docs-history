

# ADVPERF03-BP01 Choose appropriate block storage options to power your advertising workload
<a name="advperf03-bp01"></a>

 Choose the block storage service that fits each workload's performance and stability requirements. Mismatched block storage configuration is a common source of latency spikes and throttling events in production advertising systems. 

 **Desired outcome:** 
+  Every component in your advertising stack uses the EBS volume type that matches its specific performance, durability, and cost profile. 
+  Encryption, snapshot management, and elastic volume scaling are configured at deployment time. 
+  Storage performance is monitored continuously with CloudWatch metrics, and alarms detect degradation before it affects bid response times. 

 **Common anti-patterns:** 
+  Using GP2 EBS volumes (older generation with burst-based IOPS that can be exhausted) for latency-sensitive advertising databases where consistent IOPS delivery is required. 
+  Using a single EBS volume type across all workload components regardless of their I/O profile. 
+  Skipping encryption and snapshot automation during initial deployment, which increases recovery risk. 
+  Using EBS for real-time database workloads (Aerospike) where Instance Store's locally attached NVMe provides significantly lower latency. 

 **Benefits of establishing this best practice:** 
+  Matching block storage configuration to workload requirements delivers consistent, predictable performance for latency-sensitive advertising operations. 
+  Built-in encryption, automated snapshots, and elastic volume scaling reduce operational risk without adding management overhead. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 [Amazon EBS](https://aws.amazon.com/ebs/) provides persistent block-level storage for EC2 instances. In advertising platforms, EBS stores databases for ad servers, bid management systems, and campaign data stores. The choice of EBS volume type directly affects the latency profile of these workloads. 

 GP3 (General Purpose SSD) is the default for most advertising workloads, including application servers, ad decision engines, and logging infrastructure. With GP3, you provision IOPS and throughput independently from storage capacity. 

 io2 Block Express fits high-performance workloads that require consistent, low-latency IOPS. Use it for MySQL or PostgreSQL databases in bid management systems and ad servers where I/O variability affects response times. io2 provides up to 256,000 IOPS per volume and sub-millisecond latency at any I/O size. 

 EC2 Instance Store uses locally attached NVMe with throughput and IOPS that exceed any network-attached EBS volume. Choose it for Aerospike and similar real-time databases where sub-millisecond storage access is a hard requirement. Instance Store data is ephemeral, so use it only for data that is replicated or reconstructible from another source. 

 EBS-optimized instances provide dedicated bandwidth between EC2 instances and EBS volumes. Enable EBS optimization on latency-sensitive advertising databases to keep storage I/O from competing with network traffic under heavy load. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Select the right EBS volume type for each workload component:** Use GP3 as the default for application servers, creative serving, and logging infrastructure. Use io2 for RDBMS databases supporting bid management and campaign data with consistent IOPS requirements. Use Instance Store for real-time NoSQL databases (Aerospike) requiring sub-millisecond NVMe access. Document the volume type rationale for each component. 

1.  **Use EBS-optimized instances for dedicated storage throughput:** When launching EC2 instances for advertising databases, confirm the instance type supports EBS optimization and enable it at launch. EBS-optimized instances provide dedicated bandwidth for EBS I/O, keeping storage operations from competing with network traffic during peak load. 

1.  **Enable EBS encryption by default across all volumes:** Enable encryption by default at the AWS account level so that every new EBS volume (including root volumes and snapshots) is encrypted automatically. Advertising workloads handle two categories of data with specific regulatory exposure: user behavioral data and device identifiers subject to privacy regulations (GDPR and CCPA), and campaign financial data (bid prices, spend rates, advertiser contracts) that is commercially sensitive. Account-level encryption by default means neither category can land on an unencrypted volume because of a misconfigured deployment, satisfying compliance requirements without per-volume configuration overhead. 

1.  **Automate snapshot management with [AWS Data Lifecycle Manager](https://aws.amazon.com/ebs/data-lifecycle-manager/):** Create lifecycle policies that take EBS snapshots on a schedule aligned with your RPO requirements. For bid management databases, a 1-hour snapshot interval is the appropriate starting point. Losing more than one hour of campaign pacing data, frequency cap state, or bid log history during a recovery event has measurable revenue impact as campaigns overspend or underdeliver before state is restored. For lower-criticality advertising databases (creative asset metadata, historical reporting), a 4-hour interval is typically sufficient. Configure retention policies to expire snapshots after they are no longer needed for point-in-time recovery to avoid orphaned snapshots accumulating storage cost. 

1.  **Monitor EBS performance with [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) and set alarms:** Enable CloudWatch metrics for VolumeReadOps, VolumeWriteOps, VolumeQueueLength, and BurstBalance (for GP2 volumes). In advertising, storage I/O degradation translates directly to bid response latency. A queue depth above 1 on a bid management database means I/O requests are waiting behind each other, adding milliseconds to every database read on the auction critical path. Set alarms on VolumeQueueLength exceeding 1 to catch I/O saturation before it affects bid response times, and on BurstBalance dropping below 30% to detect GP2 volumes approaching burst exhaustion under sustained advertising load (a pattern common during primetime dayparts when bid volume is highest). Use Elastic Volumes to increase capacity, IOPS, or change volume type on live volumes without downtime when alarms indicate the current configuration is insufficient. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVPERF03-BP04 Use single-zone high-performance object storage for latency-sensitive ad serving and model artifact retrieval](advperf03-bp04.md) 

 **Related documents:** 
+  [Amazon EBS volume types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html) 
+  [Automate backups with Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html) 

 **Related services:** 
+  [Amazon EBS](https://aws.amazon.com/ebs/) 
+  [AWS Data Lifecycle Manager](https://aws.amazon.com/ebs/data-lifecycle-manager/) 