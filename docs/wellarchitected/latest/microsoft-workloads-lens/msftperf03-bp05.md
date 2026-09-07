

# MSFTPERF03-BP05 Leverage instance store temporary block storage for EC2 instances
<a name="msftperf03-bp05"></a>

 An instance store is a form of temporary block-level storage for EC2 instances, provided by disks physically attached to the host computer. It is well-suited for storing frequently changing data such as buffers, caches, and scratch data, as well as temporary data replicated across multiple instances like in a load-balanced web server pool, and Microsoft SQL Server TempDB data. The capacity and number of instance store volumes available vary depending on the instance type and size, with some instance types not offering instance stores at all. 

 **Desired outcome:** Maximize I/O performance for temporary and cache data in Microsoft workloads by leveraging instance store volumes that provide the highest possible storage performance through direct attachment to the host computer, particularly beneficial for SQL Server TempDB, application caches, and high-performance computing scenarios. 

 **Common anti-patterns:** 
+  Using EBS volumes for temporary data and caches when instance store volumes are available, missing opportunities for maximum I/O performance and potentially increasing storage costs. 
+  Storing persistent or critical data on instance store volumes without understanding their temporary nature, risking data loss during instance stops or failures. 
+  Choosing instance types without instance store when workloads could benefit from high-performance temporary storage, limiting application performance potential. 

 **Benefits of establishing this best practice:** 
+  Maximum I/O performance through direct-attached storage that provides the highest possible throughput and lowest latency for temporary data operations. 
+  Cost optimization by using included instance store volumes for appropriate use cases instead of provisioning additional EBS volumes for temporary storage needs. 
+  Enhanced application performance for Microsoft workloads that heavily utilize temporary storage, such as SQL Server TempDB operations and application-level caching. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 Implementing instance store volumes requires careful planning to ensure appropriate use cases and data management practices. Focus on temporary, cache, and scratch data that can benefit from maximum I/O performance while ensuring critical data remains on persistent storage. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Identify Microsoft workload components that generate temporary data, caches, or scratch files that could benefit from high-performance instance store volumes. 

1.  Evaluate EC2 instance families that include instance store volumes and assess their capacity and performance characteristics for your workload requirements. 

1.  Plan data placement strategies to ensure only appropriate temporary data is stored on instance store volumes while maintaining persistent data on EBS. 

1.  Configure applications to utilize instance store volumes for SQL Server TempDB, application caches, temporary files, and other high-I/O temporary data. 

1.  Implement data management procedures that account for the temporary nature of instance store volumes, including startup initialization and data replication strategies. 

1.  Monitor instance store utilization and performance to validate expected benefits and optimize usage patterns for maximum efficiency. 

1.  Establish operational procedures for instance lifecycle management that properly handle instance store data during maintenance and scaling operations. 

1.  Document instance store usage patterns and include in application deployment and disaster recovery procedures. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) 
+  [Make instance store volume available for use on an EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/making-instance-stores-available-on-your-instances.html) 

 **Related tools:** 
+  [Instance store volumes limits for EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-volumes.html) 