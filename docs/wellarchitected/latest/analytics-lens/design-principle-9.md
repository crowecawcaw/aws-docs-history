

# 9 – Choose the best-performing storage solution
<a name="design-principle-9"></a>

 **How do you select the best-performing storage options for your workload?** 

 An analytics workload’s optimal storage solution is influenced by several factors such as: 
+  Compute engine (Amazon EMR, Amazon Redshift, Amazon RDS, and so on) 
+  Access patterns (random or sequential) 
+  Required throughput 
+  Access frequency (online, offline, archival) 
+  CRUD (create, read, update, delete) operation requirements 
+  Data durability requirements 
+  Archival requirements 

 Choose the best-performing storage solution for your analytics workload’s own characteristics. 


|  **ID**  |  **Priority**  |  **Best practice**  | 
| --- | --- | --- | 
| ☐ BP 9.1  |  Highly recommended  |  Identify critical performance criteria for your storage workload.  | 
| ☐ BP 9.2  |  Highly recommended  |  Identify and evaluate the available storage options for your compute solution.  | 
| ☐ BP 9.3  |  Recommended  |  Choose the optimal storage based on access patterns, data growth, and the performance requirements.  | 

 For more details, refer to the following information: 
+  Amazon Elastic Compute Cloud User Guide for Linux Instances: [Amazon EBS volume types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html) 
+  Amazon Redshift Database Developer Guide: [Amazon Redshift best practices for loading data PDF](https://docs.aws.amazon.com/redshift/latest/dg/c_loading-data-best-practices.html) 
+  Amazon EMR Management Guide: [Instance storage](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-storage.html) 
+  Amazon Simple Storage Service User Guide: [Best practices design patterns: Optimizing Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html) [performance](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html) 