

# ADVCOST02-BP04 Use Spot Instances for cost-effective bidding-as-a-service workloads with flexible fault-tolerance mechanisms
<a name="advcost02-bp04"></a>

 For workloads that can be interrupted, Spot Instances can provide high performance for a very low cost per hour. 

## Implementation guidance
<a name="implementation-guidance-62"></a>

 By using Spot Instances and services like Auto Scaling groups and AWS Batch, you can achieve significant cost savings for your bidding-as-a-service workloads. 
+  **Spot Instance pricing:** Spot Instances are typically offered at a substantial discount compared to On-Demand Instance prices. The discount can range from 10% to 90%, depending on the instance type, region, and current demand. On average, you can expect to save around 70% on compute costs by using Spot Instances. 
+  **Auto scaling with Spot Instances:** By configuring your Auto Scaling groups to launch Spot Instances, you can benefit from the cost savings while maintaining the desired level of capacity and availability. Auto Scaling groups automatically replace interrupted Spot Instances, and your workload can continue running without disruption. 
+  **AWS Batch with Spot Instances:** For batch processing workloads, AWS Batch can use Spot Instances as the compute environment for your jobs. This can lead to significant cost savings, especially for compute-intensive or long-running batch jobs. AWS Batch automatically handles job retries and check-pointing, improving fault tolerance and efficient resource utilization. 
+  **Cost optimization strategies:** 
  +  **Instance right-sizing:** Regularly analyze your workload's performance and resource utilization to identify the most cost-effective instance types and sizes. Right-sizing your instances can lead to substantial cost savings without compromising performance. 
  +  **Spot Instance interruption handling:** Implement efficient strategies to handle Spot Instance interruptions, such as check-pointing long-running jobs or gracefully draining and restarting interrupted instances. This can help minimize wasted compute resources and associated costs. 
  +  **Spot Instance advisors:** Use AWS Spot Instance advisors or third-party tools to optimize your Spot Instance selection and bidding strategies. These tools can help you identify the most cost-effective Spot Instance pools based on historical pricing data and demand patterns. 
+  **Cost monitoring and optimization:** Continuously monitor your workload's cost and performance metrics using [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/), [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/), and other monitoring tools. Identify cost optimization opportunities and implement them regularly to maximize your savings. 

 By implementing these strategies, you can potentially achieve significant cost savings while maintaining the scalability and performance of your bidding-as-a-service workloads.  

 It's important to note that while Spot Instances offer substantial cost savings, they are subject to interruptions based on AWS's capacity requirements. Therefore, it's crucial to implement proper fault tolerance mechanisms and have a strategy to handle instance interruptions to ensure the reliability and availability of your bidding-as-a-service workloads. 

## Key AWS services
<a name="key-aws-services-35"></a>
+  [Amazon Elastic Compute Cloud (EC2)](https://aws.amazon.com/ec2/) 
+  [AWS Fargate](https://aws.amazon.com/fargate/) 
+  [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) 

## Resources
<a name="resources-56"></a>
+  [Guidance for Building a Real Time Bidder for Advertising on AWS](https://aws.amazon.com/solutions/guidance/building-a-real-time-bidder-for-advertising-on-aws/) 
+  [Beeswax Uses AWS to Cost-Effectively Process Millions of Bid Requests per Second](https://aws.amazon.com/solutions/case-studies/beeswax-case-study/) 
+  [AWS Fargate for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) 
+  [EC2 instance rebalance recommendations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/rebalance-recommendations.html) 
+  [EC2 Fleet and Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Fleets.html) 