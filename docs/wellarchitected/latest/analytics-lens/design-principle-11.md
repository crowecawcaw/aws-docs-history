

# 11 – Choose cost-effective compute and storage solutions based on workload usage patterns
<a name="design-principle-11"></a>

 **How do you select the compute and storage solution for your analytics workload?** Your initial design choice could have significant cost impact. Understand the resource requirements of your workload, including its steady-state and spikiness, and then select the solution and tools that meet your requirements. Avoid over-provisioning to allow more cost optimization opportunities. 


|   **ID**   |   **Priority**   |   **Best practice**   | 
| --- | --- | --- | 
| ☐ BP 11.1  |  Recommended  |  Decouple storage from compute.  | 
| ☐ BP 11.2  |  Recommended  |  Plan and provision capacity for predictable workload usage.  | 
| ☐ BP 11.3  |  Recommended  |  Use On-Demand Instance capacity for unpredictable workload usage.  | 
| ☐ BP 11.4  |  Recommended  |  Use auto scaling where appropriate.  | 

 For more details, refer to the following information: 
+  Amazon Elastic Compute Cloud User Guide for Linux Instances: [Get recommendations for an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recommendations.html) [type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recommendations.html) 
+  AWS Cost Management and Optimization – AWS Cost Optimization: [Right Sizing](https://aws.amazon.com/aws-cost-management/aws-cost-optimization/right-sizing/) 
+  AWS Whitepaper – Right Sizing: Provisioning Instances to Match Workloads: [Tips for Right Sizing](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-right-sizing/tips-for-right-sizing-your-workloads.html) 

## Best practice 11.4 – Use auto scaling where appropriate
<a name="best-practice-11.4---use-auto-scaling-where-appropriate"></a>

 Auto scaling can be used to scale up and down resources based on workload demand. This often leads to cost reductions when applications can scale down during low demand, such as nights and weekends. 

 For more details, see [SUS05-BP01 Use the minimum amount of hardware to meet your needs](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_hardware_a2.html). 

### Suggestion 11.4.1 – Use Amazon Redshift elastic resize and concurrency scaling
<a name="suggestion-11.4.1"></a>

 If your data warehouse uses provisioned Amazon Redshift, you can use one of Amazon Redshift's many scaling options to ensure that your cluster is scaled, for example Elastic resize. You may also be able to size your cluster smaller and leverage concurrency scaling, a Redshift feature that automatically adds more compute capacity to your cluster as needed. 

 For more details, refer to the following information: 
+ [ Scale Amazon Redshift to meet high throughput query requirements ](https://aws.amazon.com/blogs/big-data/scale-amazon-redshift-to-meet-high-throughput-query-requirements/)
+ [ Amazon Redshift: Elastic resize ](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-operations.html#elastic-resize)
+ [ Amazon Redshift: Working with concurrency scaling ](https://docs.aws.amazon.com/redshift/latest/dg/concurrency-scaling.html)

### Suggestion 11.4.2 – Use Amazon EMR managed scaling
<a name="suggestion-11.4.2"></a>

 If you use provisioned Amazon EMR clusters for your data processing, you can use EMR managed scaling to automatically size cluster resources based on the workload for best performance. Amazon EMR managed scaling monitors key metrics, such as CPU and memory usage, and optimizes the cluster size for best resource utilization. 

 For more details, see [Using managed scaling in Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-scaling.html). 

### Suggestion 11.4.3 – Use auto scaling for ETL and streaming jobs in AWS Glue
<a name="suggestion-11.4.3"></a>

 Auto scaling for AWS Glue ETL and streaming jobs enables on-demand scaling up and scaling down of compute resources required for ETL jobs. This helps to allocate only the required computing resources needed, and prevents over- or under-provisioning of resources, which results in time and cost savings. 

 For more details, see [Using auto scaling for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/auto-scaling.html). 

### Suggestion 11.4.4 – Use Application Auto Scaling to monitor and adjust workload capacity
<a name="suggestion-11.4.4"></a>

 Application Auto Scaling can be used to add scaling capabilities to meet application demand and scale down when the demand decreases. This can be used to scale Amazon EMR, Amazon Managed Streaming for Apache Kafka, and EC2 instances. 

 For more details, refer to the following information: 
+ [ Introducing Amazon EMR Managed Scaling – Automatically Resize Clusters to Lower Cost ](https://aws.amazon.com/blogs/big-data/introducing-amazon-emr-managed-scaling-automatically-resize-clusters-to-lower-cost/)
+ [ Adopt Recommendations and Monitor Predictive Scaling for Optimal Compute Capacity ](https://aws.amazon.com/blogs/compute/evaluating-predictive-scaling-for-amazon-ec2-capacity-optimization/)