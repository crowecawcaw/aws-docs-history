

# MLCOST04-BP13 Enable data and compute proximity
<a name="mlcost04-bp13"></a>

 Positioning data and compute resources in the same AWS Region reduces data transfer costs and improves processing speeds for machine learning workloads. By minimizing the physical distance between data storage and compute resources, you can significantly decrease latency and avoid cross-region data transfer fees. 

 **Desired outcome:** You achieve cost-efficient and high-performance machine learning operations by placing your data and compute resources in the same AWS Region. You experience faster training times, reduced latency, and avoid unnecessary data transfer costs that can significantly impact your ML project budgets. 

 **Common anti-patterns:** 
+  Storing data in one Region and running compute resources in another Region. 
+  Repeatedly transferring large datasets across Regions for training or inference. 
+  Failing to consider the impact of data transfer costs on overall ML project budgets. 

 **Benefits of establishing this best practice:** 
+  Decreased latency for data access during model training and inference. 
+  Improved overall machine learning workflow performance. 
+  Simplified management of data compliance and sovereignty requirements. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Data transfer costs between AWS Regions can significantly impact your machine learning project's budget, especially when working with large datasets that are repeatedly accessed during model training. By keeping your compute resources in the same Region as your data storage, you minimize these costs and improve performance. 

 When planning your machine learning infrastructure on AWS, consider data locality as a primary design principle. For example, if your organization stores datasets in Amazon S3 buckets in the US West (Oregon) Region, you should provision EC2 instances, SageMaker AI notebooks, or other ML compute resources in that same Region. 

 This principle applies to various machine learning scenarios, including model training, data preprocessing, and inference. Even though AWS provides high-speed network connections between Regions, the laws of physics still impose latency limitations, and cross-Region data transfers incur additional costs that can be avoided. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify data storage locations**. Determine where your primary data is stored on AWS. Check which Regions contain your Amazon S3 buckets, Amazon EFS file systems, or other storage services holding your training data. Use the AWS Management Console, AWS CLI, or infrastructure as code tools to inventory your data storage resources across Regions. 

1.  **Audit compute resource placement**. Review your current machine learning compute resources, including Amazon EC2 instances, Amazon SageMaker AI notebooks, and training jobs. Verify if they are in the same Regions as your data sources. Use AWS Cost Explorer and AWS Trusted Advisor to identify cross-Region data transfer costs that may indicate misaligned resources. 

1.  **Consolidate resources by Region**. When creating new compute resources for machine learning workloads, consistently provision them in the same Region as your data. For example, if using [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/), create your notebook instances, training jobs, and endpoints in the Region where your training data is stored in Amazon S3. 

1.  **Use Regional data transfer analysis**. Review your AWS billing information to identify and quantify cross-Region data transfer costs. The [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) service can assist you in analyzing data transfer costs between AWS services and across Regions. Set up cost allocation tags to track expenses related to machine learning projects specifically. 

1.  **Consider data replication for specific use cases**. In scenarios requiring multi-Region deployments for high availability or disaster recovery, implement a data replication strategy to maintain copies of datasets in each Region where compute resources exist. Services like [Amazon S3 Cross-Region Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) can automate this process while managing costs. 

1.  **Leverage edge computing for distributed ML workloads**. When working with data that exists at the edge of the network, consider using [AWS Outposts](https://aws.amazon.com/outposts/), [AWS Wavelength](https://aws.amazon.com/wavelength/), or [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) to bring compute resources closer to your data sources, especially for applications requiring low-latency inference. 

1.  **Implement data caching strategies**. For frequently accessed data, implement caching solutions like [Amazon ElastiCache](https://aws.amazon.com/elasticache/) or [Amazon DynamoDB Accelerator (DAX)](https://aws.amazon.com/dynamodb/dax/) in the same Region as your compute resources to further reduce latency and data transfer costs. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) 
+  [Replicating objects within and across Regions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) 
+  [AWS Data Transfer Pricing](https://aws.amazon.com/ec2/pricing/on-demand/#Data_Transfer) 
+  [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) 
+  [AWS Outposts](https://aws.amazon.com/outposts/) 
+  [Regions and Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) 
+  [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/) 