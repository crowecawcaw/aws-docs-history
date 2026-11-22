

# ADVPERF03-BP03 Use a cloud file system to store shared data between applications

 Use [Amazon EFS](https://aws.amazon.com/efs/) as a cloud file system to store shared log files, configuration files, and other data accessed concurrently by multiple applications or instances across Availability Zones. 

 **Desired outcome:** 
+  Distributed advertising workloads that need shared file access (for example, log processing pipelines, configuration management, or media processing workflows) use a fully managed file system that scales automatically and is available across all Availability Zones in your deployment. 
+  Storage costs are optimized through automated lifecycle management that transitions infrequently accessed files to lower-cost storage tiers. 
+  High availability is supported by creating EFS mount targets in every Availability Zone where your workloads run. 

 **Common anti-patterns:** 
+  Copying shared configuration files, log data, or media assets to each EC2 instance individually, which creates synchronization overhead and consistency risks when files change. 
+  Provisioning an EFS file system in a single Availability Zone to reduce cost, at the price of a single point of failure that takes down every workload sharing that file system. 
+  Using Max IO performance mode for all workloads when General Purpose mode provides lower per-operation latency for most advertising file access patterns. 

 **Benefits of establishing this best practice:** 
+  Amazon EFS removes the need to manage file server infrastructure, provision capacity in advance, or synchronize files across instances manually. 
+  A shared file system simplifies architecture and reduces the operational overhead of keeping shared data consistent across distributed advertising workloads. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Use Amazon EFS for advertising workloads that require shared file access across multiple EC2 instances or containers. 

 Log processing pipelines require concurrent access to the same log files across collection, parsing, enrichment, and archival stages. Stages read and write to shared EFS paths, simplifying pipeline coordination and removing the need to move files between stages through Amazon S3 or Amazon SQS. 

 Advertising application configuration requires multiple service instances to access the same configuration files, such as bidder floor price configs, targeting rule files, and creative policy files. All instances read the same files from EFS without per-instance synchronization. 

 Media asset staging for ad creative processing runs encoding, transcoding, and quality check services on the same source asset concurrently. 

 The EFS performance mode affects latency for each operation. Use General Purpose mode as the default for advertising use cases with latency-sensitive operations such as configuration reads and real-time log processing. Reserve Max IO mode for highly parallelized workloads that need maximum aggregate throughput, such as large-scale media processing with hundreds of concurrent instances. 

 Match throughput mode to your I/O pattern. Use Elastic Throughput for spiky or unpredictable I/O, such as batch log ingestion at irregular intervals. Use Provisioned Throughput when the workload requires consistently high throughput independent of the amount of data stored. 

 EFS lifecycle policies automatically transition files not accessed for a configured period to the EFS Infrequent Access (IA) storage class. Apply lifecycle policies to log archives, completed campaign configuration files, and historical creative assets that must be retained but are rarely read. 

 Create EFS mount targets in every Availability Zone your workloads use. Local mount targets provide network access without cross-AZ charges and protect against Availability Zone-level failures affecting file system access. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Select the right EFS performance mode:** Use General Purpose mode (the default) for latency-sensitive advertising workloads: configuration reads, log processing, and creative asset access where individual file operation latency matters. Consider Max IO mode only for highly parallelized media processing jobs where hundreds of instances access the file system simultaneously and aggregate throughput takes priority over per-operation latency. 

1.  **Choose the throughput mode that matches your I/O profile:** Use Elastic Throughput for advertising workloads with spiky or unpredictable I/O (batch log ingestion at irregular intervals). Use Provisioned Throughput only when the workload requires consistently high throughput independent of file system size, for example, media processing workflows with sustained high I/O rates. 

1.  **Apply EFS lifecycle policies to reduce storage costs:** Enable lifecycle management and configure the transition period (7, 14, 30, 60, or 90 days since last access) based on your advertising data retention requirements. Files transitioned to EFS IA cost significantly less per GB than Standard storage. Configure a transition back to Standard storage when files are accessed again, so frequently accessed files are served at full performance. 

1.  **Create EFS mount targets in every Availability Zone where your workloads run:** In the EFS console or through infrastructure as code, create a mount target in each subnet associated with your advertising workloads. This means instances in any Availability Zone access the file system through a local mount target, delivering low latency, avoiding cross-AZ data transfer charges, and maintaining availability if one Availability Zone experiences an issue. 

1.  **Monitor EFS performance and usage:** Use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) metrics for EFS to monitor BurstCreditBalance (for bursting throughput), ClientConnections, DataReadIOBytes, and DataWriteIOBytes. Set alarms on burst credit balance dropping below a threshold (for file systems using Bursting Throughput mode) to alert before throughput becomes limited. Enable EFS Access Points for application-level access control when multiple advertising services share the same file system. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Create an Amazon EFS file system and mount it on an Amazon EC2 instance using the AWS CLI](https://docs.aws.amazon.com/efs/latest/ug/wt1-getting-started.html) 
+  [Encrypting data in Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/encryption.html) 

 **Related services:** 
+  [Amazon EFS](https://aws.amazon.com/efs/) 