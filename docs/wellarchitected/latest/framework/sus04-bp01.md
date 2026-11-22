

# SUS04-BP01 Eliminate unnecessary data

 Eliminate data that no longer serves a business purpose. Whether redundant, obsolete, trivial, or simply unknown - aim to reduce storage requirements and the associated environmental impact of your workload. 

 **Desired outcome:** 
+  You maintain a lean data environment that stores only valuable, actively used data and uses storage resources efficiently. 
+  You give all data a clear business purpose with appropriate retention policies, minimizing unnecessary storage consumption and processing overhead. 

 **Common anti-patterns:** 
+  Storing all data indefinitely without a clear purpose. 
+  Storing multiple copies of the same data across different systems. 
+  Failing to establish data retention policies based on business value. 
+  Not regularly auditing data usage and identifying obsolete assets. 
+  Storing intermediate or temporary data without cleanup mechanisms. 

 **Benefits of establishing this best practice:** 
+  Lowers the required share on hardware related impacts, from raw material extraction to end of life treatment (Scope 3 emissions). 
+  Lowers the required share on energy for operating infrastructure (Scope 2 emissions). 
+  Provides operational insight into data stored and options on life-cycle management. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 To eliminate unnecessary data in your AWS environment, you need to implement processes to identify, classify, and manage data throughout its lifecycle. This includes regular audits to identify dark, obsolete, redundant, or trivial data and automated mechanisms to enforce data lifecycle policies. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Conduct a comprehensive data inventory. 

   1.  Use AWS Resource Explorer to discover and catalog data assets across your AWS accounts. 

   1.  Implement an AWS Glue Data Catalog to maintain metadata about your data assets. 

   1.  Identify data ownership and establish business context for data assets, for example with Amazon DataZone. 

1.  Implement data classification and tagging. 

   1.  Develop a classification scheme based on data criticality and business value. 

   1.  Use AWS Resource Groups and Tag Editor to tag data assets with relevant metadata. 

   1.  Classify data based on access patterns, age, and business relevance. 

1.  Establish and enforce data lifecycle policies. 

   1.  Configure Amazon S3 Lifecycle policies for object storage. 

   1.  Use Amazon Data Lifecycle Manager for EBS snapshots and AMIs. 

   1.  Implement Amazon RDS automated backups with appropriate retention periods. 

   1.  Shorten the log retention of your [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) log groups, which is indefinite by default. 

1.  Identify and remove redundant or unnecessary data. 

   1.  Use Amazon S3 Storage Lens to identify optimization opportunities. 

   1.  Implement de-duplication mechanisms where appropriate. 

   1.  Create automated cleanup processes for temporary or intermediate data. 

1.  Monitor and continuously improve data management. 

   1.  Regularly audit data usage and access patterns. 

   1.  Review and update data lifecycle policies based on changing business needs. 

   1.  Establish a governance process for ongoing data management and optimization. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SUS04-BP02 Select appropriate file formats, compression, and software implementation](sus04-bp02.md) 
+  [COST04-BP01 Define network and data transfer infrastructure costs](cost04-bp01.md) 
+  [COST04-BP02 Perform data transfer modeling](cost04-bp02.md) 

 **Related documents:** 
+  [Optimizing your AWS Infrastructure for Sustainability, Part II: Storage](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-ii-storage/) 
+  [How do I remove active resources that I no longer need in my AWS account?](https://repost.aws/knowledge-center/terminate-resources-account-closure) 

 **Related videos:** 
+  [AWS re:Invent 2023 - Sustainable architecture: Past, present, and future (SUS302)](https://www.youtube.com/watch?v=2xpUQ-Q4QcM) 
+  [AWS re:Invent 2023 - Optimize costs in your multi-account environments (COP333)](https://www.youtube.com/watch?v=ie_Mqb-eC4A) 