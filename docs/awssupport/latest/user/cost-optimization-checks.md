

# Cost optimization
<a name="cost-optimization-checks"></a>

You can use the following checks for the cost optimization category.

**Contents**
+ [AWS account not part of AWS Organizations](#account-not-part-of-organizations)
+ [Amazon Aurora cost optimization recommendations for DB cluster storage](#aurora-cost-opt-db-cluster-storage)
+ [Amazon Comprehend underutilized endpoints](#amazon-comprehend-underutilized-endpoints)
+ [Amazon DynamoDB reserved capacity purchase recommendations](#dynamodb-reserved-capacity-purchase-rec)
+ [Amazon EBS cost optimization recommendations for volumes](#ebs-cost-opt-for-volumes)
+ [Amazon EBS over-provisioned volumes](#amazon-ebs-over-provisioned-volumes)
+ [Amazon EC2 cost optimization recommendations for Amazon EC2 Auto Scaling groups](#ec2-cost-opt-for-autoscaling)
+ [Amazon EC2 cost optimization recommendations for instances](#ec2-cost-opt-for-instances)
+ [Amazon EC2 instances consolidation for Microsoft SQL Server](#ec2-instances-consolidation-sql-server)
+ [Amazon EC2 instances over-provisioned for Microsoft SQL Server](#ec2-instance-over-provisioned-microsoft-sql-server)
+ [Amazon EC2 instances stopped](#ec2-instance-stopped-for-thirty-days)
+ [Amazon EC2 Reserved Instance lease expiration](#amazon-ec2-reserved-instances-lease-expiration)
+ [Amazon EC2 Reserved Instance optimization](#amazon-ec2-reserved-instances-optimization)
+ [Amazon ECR Repository without lifecycle policy configured](#amazon-ecr-repository-without-lifecycle-policy)
+ [Amazon ElastiCache reserved node purchase recommendations](#elasticache-reserved-node-purchase-recommendations)
+ [AWS Fargate cost optimization recommendations for Amazon ECS](#fargate-cost-opt-for-ecs)
+ [Amazon MemoryDB reserved node purchase recommendations](#memorydb-reserved-node-purchase-recommendations)
+ [Amazon OpenSearch Service Reserved Instance purchase recommendations](#os-ri-purchase-recommendations)
+ [Amazon RDS cost optimization recommendations for DB instances](#rds-cost-opt-for-db-instances)
+ [Amazon RDS cost optimization recommendations for DB instance storage](#rds-cost-opt-for-db-instance-storage)
+ [Amazon RDS idle DB instances](#amazon-rds-idle-dbs-instances)
+ [Amazon RDS Reserved Instance purchase recommendations](#rds-ri-purchase-recommendations)
+ [Amazon Redshift reserved node purchase recommendations](#redshift-reserved-node-purchase-recommendations)
+ [Amazon Route 53 Latency Resource Record Sets](#amazon-route-53-latency-resource-record-sets)
+ [Amazon S3 Bucket Lifecycle Policy Configured](#amazon-s3-bucket-lifecycle-policy-configured)
+ [Amazon S3 Incomplete Multipart Upload Abort Configuration](#s3-incomplete-multipart-upload-abort-config)
+ [Amazon S3 version-enabled buckets without lifecycle policies configured](#amazon-s3-version-enabled-buckets-no-lifecycle-policy)
+ [AWS Lambda cost optimization recommendations for functions](#lambda-cost-opt-for-functions)
+ [AWS Lambda functions with excessive timeouts](#aws-lambda-functions-excessive-timeouts)
+ [AWS Lambda functions with high error rates](#aws-lambda-functions-with-high-error-rates)
+ [AWS Lambda over-provisioned functions for memory size](#aws-lambda-over-provisioned-functions-memory-size)
+ [AWS Savings Plans purchase recommendations for compute](#savings-plans-purchase-recommendations-compute)
+ [AWS Savings Plans purchase recommendations for Amazon SageMaker AI](#savings-plans-purchase-recommendations-sagemaker)
+ [AWS Well-Architected high risk issues for cost optimization](#well-architected-high-risk-issues-cost-optimization)
+ [Idle Load Balancers](#idle-load-balancers)
+ [Idle NAT gateways](#idle-nat-gateways)
+ [Inactive AWS Network Firewall](#inactive-network-firewall)
+ [Inactive VPC interface endpoints](#inactive-vpc-interface-endpoints)
+ [Inactive Gateway Load Balancer endpoints](#inactive-gateway-load-balancer)
+ [Inactive NAT Gateways](#inactive-nat-gateways)
+ [Low utilization Amazon EC2 instances](#low-utilization-amazon-ec2-instances)
+ [Unassociated Elastic IP Addresses](#unassociated-elastic-ip-addresses)
+ [Underutilized Amazon EBS volumes](#underutilized-amazon-ebs-volumes)
+ [Underutilized Amazon Redshift Clusters](#underutilized-amazon-redshift-clusters)

## AWS account not part of AWS Organizations
<a name="account-not-part-of-organizations"></a>

**Description**  
Checks if an AWS account is part of AWS Organizations under the appropriate management account.  
AWS Organizations is an account management service for consolidating multiple AWS accounts into a centrally-managed organization. This enables you to centrally structure accounts for billing consolidation and implement ownership and security policies as your workloads scale on AWS.  
You can specify the management account id using the **MasterAccountId** parameter of the AWS Config rules.  
For more information, see [What is AWS Organizations?](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz127`

**Source**  
`AWS Config Managed Rule: account-part-of-organizations`

**Alert criteria**  
Yellow: This AWS account is not part of AWS Organizations.

**Recommended action**  
Add this AWS account as part of AWS Organizations.  
For more information, see [Tutorial: Creating and configuring an organization.](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tutorials_basic.html)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Amazon Aurora cost optimization recommendations for DB cluster storage
<a name="aurora-cost-opt-db-cluster-storage"></a>

**Description**  
Checks your Amazon Aurora DB cluster storage configurations and usage patterns to provide recommendations for potential cost savings.  
For each resource, Trusted Advisor shows only the top recommended action from AWS Cost Optimization Hub.  
To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1z7kmr17n`

**Source**  
`AWS Cost Optimization Hub`

**Alert criteria**  
Yellow: An Aurora DB cluster storage has a cost savings action identified by Cost Optimization Hub.

**Recommended action**  
Consider implementing the recommendation. The recommendation is one of the recommendation types listed in [Understanding cost optimization strategies](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-optimization-strategies.html) in the *AWS Cost Management User Guide*. For more information on implementing these recommendations, see the AWS Cloud Financial Management (CFM) [Service Cost Optimization Playbook](https://catalog.workshops.aws/awscff/en-US/playbooks).  
Use the detailed recommendations in AWS Compute Optimizer to understand the potential impact of these changes on cost and performance.

**Additional resources**  
+ [Viewing Aurora and RDS database recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-rds-recommendations.html)
+ [Recommendations from Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/monitoring-recommendations.html)
+ [Settings for Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Modifying.html#Aurora.Modifying.Settings)

**Report columns**  
+ Status
+ Region
+ Resource ID
+ Recommended Action
+ Current Resource Summary
+ Recommended Resource Summary
+ Estimated Monthly Cost
+ Estimated Monthly Savings
+ Last Refresh Time stamp

## Amazon Comprehend underutilized endpoints
<a name="amazon-comprehend-underutilized-endpoints"></a>

**Description**  
Checks the throughput configuration of your endpoints. This check alerts you when endpoints are not actively used for real-time inference requests. An endpoint that isn’t used for more than 15 consecutive days is considered underutilized. All endpoints accrue charges based on both the throughput set, and the length of time that the endpoint is active.   
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`Cm24dfsM12`

**Alert criteria**  
Yellow: The endpoint is active, but hasn’t been used for real-time inference requests in the past 15 days.

**Recommended action**  
If the endpoint hasn’t been used in the past 15 days, we recommend that you define a scaling policy for the resource by using [Application Autoscaling.](https://docs.aws.amazon.com/comprehend/latest/dg/comprehend-autoscaling.html)  
If the endpoint has a scaling policy defined and hasn’t been used in the past 30 days, consider deleting the endpoint and using asynchronous inference. For more information, see [Deleting an endpoint with Amazon Comprehend](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints-delete.html).

**Report columns**  
+ Status
+ Region
+ Endpoint ARN
+ Provisioned Inference Unit
+ AutoScaling Status
+ Reason
+ Last Updated Time

## Amazon DynamoDB reserved capacity purchase recommendations
<a name="dynamodb-reserved-capacity-purchase-rec"></a>

**Description**  
Checks your Amazon DynamoDB usage patterns and provides recommendations for potential cost savings through reserved capacity purchases.  
This check generates recommendations at [payer scope for the payer account and at linked scope for a linked account](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html).  
Trusted Advisor shows only the top recommended action from AWS Cost Optimization Hub.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1z7kmr15n`

**Source**  
`AWS Cost Optimization Hub`

**Alert criteria**  
Yellow: Account has a cost savings action identified by Cost Optimization Hub for DynamoDB.

**Recommended action**  
Consider [implementing the recommendation](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-optimization-strategies.html). For more information on implementing these recommendations, see the AWS Cloud Financial Management (CFM) [Service Cost Optimization Playbook](https://catalog.workshops.aws/awscff/en-US/playbooks).

**Additional resources**  
+ [DynamoDB reserved capacity](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/reserved-capacity.html)
+ [Accessing reservation recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ri-recommendations.html)
+ [Amazon DynamoDB Reserved Capacity](https://aws.amazon.com/dynamodb/reserved-capacity/)

**Report columns**  
+ Status
+ Region
+ Recommended Resource Summary
+ Estimated Monthly Cost
+ Estimated Monthly Savings
+ Last Refresh Time stamp

## Amazon EBS cost optimization recommendations for volumes
<a name="ebs-cost-opt-for-volumes"></a>

**Description**  
Checks your Amazon EBS volume configurations and usage patterns to provide recommendations for potential cost savings.  
For each resource, Trusted Advisor shows only the top recommended action from AWS Cost Optimization Hub.  
To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1z7kmr02n`

**Source**  
`AWS Cost Optimization Hub`

**Alert criteria**  
Yellow: EBS volume has a cost savings action identified by Cost Optimization Hub.

**Recommended action**  
Consider implementing the recommendation. The recommendation is one of the recommendation types listed in [Understanding cost optimization strategies](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-optimization-strategies.html) in the *AWS Cost Management User Guide*. For more information on implementing these recommendations, see the AWS Cloud Financial Management (CFM) [Service Cost Optimization Playbook](https://catalog.workshops.aws/awscff/en-US/playbooks).  
Use the detailed recommendations in AWS Compute Optimizer to understand the potential impact of these changes on cost and performance.

**Additional resources**  
+ [Viewing Amazon EBS volume recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-ebs-recommendations.html)
+ [EBS volume metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/ebs-metrics-analyzed.html)
+ [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)
+ [Request Amazon EBS volume modifications](https://docs.aws.amazon.com/ebs/latest/userguide/requesting-ebs-volume-modifications.html)

**Report columns**  
+ Status
+ Region
+ Resource ID
+ Recommended Action
+ Current Resource Summary
+ Recommended Resource Summary
+ Estimated Monthly Cost
+ Estimated Monthly Savings
+ Last Refresh Time stamp

## Amazon EBS over-provisioned volumes
<a name="amazon-ebs-over-provisioned-volumes"></a>

**Description**  
This is a legacy check. We recommend using the new check (Check ID: [c1z7kmr02n](#ebs-cost-opt-for-volumes)) that offers additional customized recommendations.
Checks the Amazon Elastic Block Store (Amazon EBS) volumes that were running at any time during the lookback period. This check alerts you if any EBS volumes were over-provisioned for your workloads. When you have over-provisioned volumes, you’re paying for unused resources. Although some scenarios can result in low optimization by design, you can often lower your costs by changing the configuration of your EBS volumes. Estimated monthly savings are calculated by using the current usage rate for EBS volumes. Actual savings vary if the volume isn’t present for a full month.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`COr6dfpM03`

**Alert Criteria**  
 Yellow: An EBS volume that was over-provisioned during the lookback period. To determine if a volume is over-provisioned, we consider all default CloudWatch metrics (including IOPS and throughput). The algorithm used to identify over-provisioned EBS volumes follows AWS best practices. The algorithm is updated when a new pattern has been identified.

**Recommended action**  
Consider downsizing volumes that have low utilization.  
For more information, see [Opt in AWS Compute Optimizer for Trusted Advisor checks](compute-optimizer-with-trusted-advisor.md).

**Report columns**  
+ Status
+ Region
+ Volume ID
+ Volume Type
+ Volume Size (GB)
+ Volume Baseline IOPS
+ Volume Burst IOPS
+ Volume Burst Throughput
+ Recommended Volume Type
+ Recommended Volume Size (GB)
+ Recommended Volume Baseline IOPS
+ Recommended Volume Burst IOPS
+ Recommended Volume Baseline Throughput
+ Recommended Volume Burst Throughput
+ Lookback Period (days)
+ Savings Opportunity (%)
+ Estimated Monthly Savings
+ Estimated Monthly Savings Currency
+ Last Updated Time

## Amazon EC2 cost optimization recommendations for Amazon EC2 Auto Scaling groups
<a name="ec2-cost-opt-for-autoscaling"></a>

**Description**  
Checks your Amazon EC2 Auto Scaling group configurations and usage patterns to provide recommendations for potential cost savings.  
For each resource, Trusted Advisor shows only the top recommended action from AWS Cost Optimization Hub.  
To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1z7kmr01n`

**Source**  
`AWS Cost Optimization Hub`

**Alert criteria**  
Yellow: Amazon EC2 Auto Scaling group has a cost savings action identified by Cost Optimization Hub.

**Recommended action**  
Consider implementing the recommendation. The recommendation is one of the recommendation types listed in [Understanding cost optimization strategies](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-optimization-strategies.html) in the *AWS Cost Management User Guide*. For more information on implementing these recommendations, see the AWS Cloud Financial Management (CFM) [Service Cost Optimization Playbook](https://catalog.workshops.aws/awscff/en-US/playbooks).  
Use the detailed recommendations in AWS Compute Optimizer to understand the potential impact of these changes on cost and performance.

**Additional resources**  
+ [Viewing Amazon EC2 Auto Scaling volume recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-asg-recommendations.html)
+ [Amazon EC2 Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html)
+ [What is Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)

**Report columns**  
+ Status
+ Region
+ Resource ID
+ Recommended Action
+ Current Resource Summary
+ Recommended Resource Summary
+ Estimated Monthly Cost
+ Estimated Monthly Savings
+ Last Refresh Time stamp

## Amazon EC2 cost optimization recommendations for instances
<a name="ec2-cost-opt-for-instances"></a>

**Description**  
Checks your Amazon EC2 instance configurations and usage patterns to provide recommendations for potential cost savings.  
For each resource, Trusted Advisor shows only the top recommended action from AWS Cost Optimization Hub.  
To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1z7kmr00n`

**Source**  
`AWS Cost Optimization Hub`

**Alert criteria**  
Yellow: EC2 instance has a cost savings action identified by Cost Optimization Hub.

**Recommended action**  
Consider implementing the recommendation. The recommendation is one of the recommendation types listed in [Understanding cost optimization strategies](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-optimization-strategies.html) in the *AWS Cost Management User Guide*. For more information on implementing these recommendations, see the AWS Cloud Financial Management (CFM) [Service Cost Optimization Playbook](https://catalog.workshops.aws/awscff/en-US/playbooks).  
Use the detailed recommendations in AWS Compute Optimizer to understand the potential impact of these changes on cost and performance.

**Additional resources**  
+ [Viewing EC2 instance recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-ec2-recommendations.html)
+ [EC2 instance metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/ec2-metrics-analyzed.html)
+ [Amazon EC2 instance type changes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-resize.html)

**Report columns**  
+ Status
+ Region
+ Resource ID
+ Recommended Action
+ Current Resource Summary
+ Recommended Resource Summary
+ Estimated Monthly Cost
+ Estimated Monthly Savings
+ Last Refresh Time stamp

## Amazon EC2 instances consolidation for Microsoft SQL Server
<a name="ec2-instances-consolidation-sql-server"></a>

**Description**  
Checks your Amazon Elastic Compute Cloud (Amazon EC2) instances that are running SQL Server in the past 24 hours. This check alerts you if your instance has less than the minimum number of SQL Server licenses. From the Microsoft SQL Server Licensing Guide, you are paying 4 vCPU licenses even if an instance has only 1 or 2 vCPUs. You can consolidate smaller SQL Server instances to help lower costs.   
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`Qsdfp3A4L2`

**Alert criteria**  
Yellow: An instance with SQL Server has less than 4 vCPUs.

**Recommended Action**  
Consider consolidating smaller SQL Server workloads into instances with at least four vCPUs.

**Additional resources**  
+ [Microsoft SQL Server on AWS](https://aws.amazon.com/sql/)
+ [Microsoft Licensing on AWS](https://aws.amazon.com/windows/resources/licensing/)
+ [Microsoft SQL Server Licensing Guide](https://www.microsoft.com/en-us/sql-server/sql-server-2019-pricing)

**Report columns**  
+ Status
+ Region
+ Instance ID
+ Instance Type
+ vCPU
+ Minimum vCPU
+ SQL Server Edition
+ Last Updated Time

## Amazon EC2 instances over-provisioned for Microsoft SQL Server
<a name="ec2-instance-over-provisioned-microsoft-sql-server"></a>

**Description**  
Checks your Amazon Elastic Compute Cloud (Amazon EC2) instances that are running SQL Server in the past 24 hours. An SQL Server database has a compute capacity limit for each instance. An instance with SQL Server Standard edition can use up to 48 vCPUs. An instance with SQL Server Web can use up to 32 vCPUs. This check alerts you if an instance exceeds this vCPU limit.  
If your instance is over-provisioned, you pay full price without realizing an improvement in performance. You can manage the number and size of your instances to help lower costs.  
Estimated monthly savings are calculated by using the same instance family with the maximum number of vCPUs that an SQL Server instance can use and the On-Demand pricing. Actual savings will vary if you’re using Reserved Instances (RI) or if the instance isn’t running for a full day.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`Qsdfp3A4L1`

**Alert criteria**  
+ Red: An instance with SQL Server Standard edition has more than 48 vCPUs.
+ Red: An instance with SQL Server Web edition has more than 32 vCPUs.

**Recommended action**  
For SQL Server Standard edition, consider changing to an instance in the same instance family with 48 vCPUs. For SQL Server Web edition, consider changing to an instance in the same instance family with 32 vCPUs. If it is memory intensive, consider changing to memory optimized R5 instances.

**Additional resources**  
+ [Microsoft SQL Server on AWS](https://aws.amazon.com/sql)
+  You can use [Launch Wizard](https://aws.amazon.com/launchwizard) to simplify your SQL Server deployment on EC2.

**Report columns**  
+ Status
+ Region
+ Instance ID
+ Instance Type
+ vCPU
+ SQL Server Edition
+ Maximum vCPU
+ Recommended Instance Type
+ Estimated Monthly Savings
+ Last Updated Time

## Amazon EC2 instances stopped
<a name="ec2-instance-stopped-for-thirty-days"></a>

**Description**  
Checks if there are Amazon EC2 instances that have been stopped for more than 30 days.  
You can specify the allowed number of days value in the **AllowedDays** of AWS Config parameters.  
For more information, see [Why am I being charged for Amazon EC2 when all my instances were terminated?](https://repost.aws/knowledge-center/ec2-billing-terminated)  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz150`

**Source**  
`AWS Config Managed Rule: ec2-stopped-instance `

**Alert criteria**  
+ Yellow: There are Amazon EC2 instances stopped for more than the allowed number of days.

**Recommended action**  
Review the Amazon EC2 instances that have been stopped for 30 days or more. To avoid incuring unnecessary costs, terminate any instances that are no longer needed.  
For more information, see [Terminate your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html).

**Additional resources**  
+ [Amazon EC2 On-Demand Pricing](https://aws.amazon.com/ec2/pricing/on-demand/)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Amazon EC2 Reserved Instance lease expiration
<a name="amazon-ec2-reserved-instances-lease-expiration"></a>

**Description**  
Checks for Amazon EC2 Reserved Instances that are scheduled to expire within the next 30 days, or have expired in the preceding 30 days.   
Reserved Instances don't renew automatically. You can continue using an Amazon EC2 instance covered by the reservation without interruption, but you will be charged On-Demand rates. New Reserved Instances can have the same parameters as the expired ones, or you can purchase Reserved Instances with different parameters.   
The estimated monthly savings is the difference between the On-Demand and Reserved Instance rates for the same instance type. 

**Check ID**  
`1e93e4c0b5`

**Alert criteria**  
+ Yellow: The Reserved Instance lease expires in less than 30 days. 
+ Yellow: The Reserved Instance lease expired in the preceding 30 days.

**Recommended action**  
Consider purchasing a new Reserved Instance to replace the one that is nearing the end of its term. For more information, see [How to Purchase Reserved Instances](https://aws.amazon.com/ec2/purchasing-options/reserved-instances/buyer/) and [Buying Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-market-concepts-buying.html).

**Additional resources**  
+ [Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts-on-demand-reserved-instances.html)
+ [Instance Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html)

**Report columns**  
+ Status
+ Zone
+ Instance Type
+ Platform
+ Instance Count
+ Current Monthly Cost
+ Estimated Monthly Savings
+ Expiration Date
+ Reserved Instance ID
+ Reason

## Amazon EC2 Reserved Instance optimization
<a name="amazon-ec2-reserved-instances-optimization"></a>

**Description**  
An important part of using AWS involves balancing your Reserved Instance (RI) purchase against your On-Demand Instance usage. This check provides recommendations on which RIs will help reduce the costs incurred from using On-Demand Instances.   
We create these recommendations by analyzing your On-Demand usage for the past 30 days. We then categorizing the usage into eligible categories for reservations. We simulate every combination of reservations in the generated category of usage to identify the recommended number of each type of RI to purchase. This process of simulation and optimization allows us to maximize your cost savings. This check covers recommendations based on Standard Reserved Instances with the partial upfront payment option.  
This check is not available to accounts linked in consolidated billing. The recommendations for this check are only available for the paying account.

**Check ID**  
`cX3c2R1chu`

**Alert criteria**  
Yellow: Optimizing the use of partial upfront RIs can help reduce costs.

**Recommended action**  
See the [Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) page for more detailed and customized recommendations. Additionally, refer to the [buying guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ri-market-general.html#ri-market-buying-guide) to understand how to purchase RIs and the options available. 

**Additional resources**  
+ Information on RIs and how they can save you money can be found [here](https://aws.amazon.com/ec2/pricing/reserved-instances/). 
+ For more information on this recommendation, see [Reserved Instance Optimization Check Questions](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/faqs/#Reserved_Instance_Optimization_Check_Questions) in the Trusted Advisor FAQs.

**Report columns**  
+ Region
+ Instance Type
+ Platform
+ Recommended Number of RIs to Purchase
+ Expected Average RI Utilization
+ Estimated Savings with Recommendations (Monthly)
+ Upfront Cost of RIs
+ Estimated costs of RIs (Monthly)
+ Estimated On-Demand Cost Post Recommended RI Purchase (Monthly)
+ Estimated Break Even (Months)
+ Lookback Period (Days)
+ Term (Years)

## Amazon ECR Repository without lifecycle policy configured
<a name="amazon-ecr-repository-without-lifecycle-policy"></a>

**Description**  
Checks if a private Amazon ECR repository has at least one lifecycle policy configured. Lifecycle policies allow you to define a set of rules to automatically clean up old or unused container images. This gives you control over the lifecycle management of the images, allows Amazon ECR repositories to be better organized, and helps to lower overall storage costs.  
For more information, see [Lifecycle policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html).

**Check ID**  
`c18d2gz128`

**Source**  
`AWS Config Managed Rule: ecr-private-lifecycle-policy-configured`

**Alert criteria**  
Yellow: An Amazon ECR private repository doesn’t have any lifecycle policies configured.

**Recommended action**  
Consider creating at least one lifecycle policy for your private Amazon ECR repository.  
For more information, see [Creating a lifecycle policy](https://docs.aws.amazon.com/AmazonECR/latest/userguide/lp_creation.html).

**Additional resources**  
+  [Lifecycle policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html).
+  [Creating a lifecycle policy](https://docs.aws.amazon.com/AmazonECR/latest/userguide/lp_creation.html).
+  [Examples of lifecycle policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/lifecycle_policy_examples.html).

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## Amazon ElastiCache reserved node purchase recommendations
<a name="elasticache-reserved-node-purchase-recommendations"></a>

**Description**  
Checks your Amazon ElastiCache usage patterns to provide recommendations for potential cost savings through reserved node purchases.  
This check generates recommendations at [payer scope for the payer account and at linked scope for a linked account](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html).  
Trusted Advisor shows only the top recommended action from AWS Cost Optimization Hub.  
To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) .  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1z7kmr13n`

**Source**  
`AWS Cost Optimization Hub`

**Alert criteria**  
Yellow: Account has a cost savings action identified by Cost Optimization Hub for Amazon ElastiCache.

**Recommended action**  
Consider [implementing the recommendation](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-optimization-strategies.html) For more information on implementing these recommendations, see the AWS Cloud Financial Management (CFM) [Service Cost Optimization Playbook](https://catalog.workshops.aws/awscff/en-US/playbooks).

**Additional resources**  
+ [Reserved nodes](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.Reserved.html)
+ [Accessing reservation recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ri-recommendations.html)
+ [Amazon ElastiCache Reserved Nodes](https://aws.amazon.com/elasticache/reserved-cache-nodes/)

**Report columns**  
+ Status
+ Region
+ Recommended Resource Summary
+ Estimated Monthly Cost
+ Estimated Monthly Savings
+ Last Refresh Time stamp

## AWS Fargate cost optimization recommendations for Amazon ECS
<a name="fargate-cost-opt-for-ecs"></a>

**Description**  
Checks your AWS Fargate for Amazon ECS configurations and usage patterns to provide recommendations for potential cost savings.  
For each resource, Trusted Advisor shows only the top recommended action from AWS Cost Optimization Hub.  
To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1z7kmr06n`

**Source**  
`AWS Cost Optimization Hub`

**Alert criteria**  
Yellow:Amazon ECS services on AWS Fargate have a cost savings action identified by Cost Optimization Hub.

**Recommended action**  
Consider implementing the recommendation. The recommendation is one of the recommendation types listed in [Understanding cost optimization strategies](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-optimization-strategies.html) in the *AWS Cost Management User Guide*. For more information on implementing these recommendations, see the AWS Cloud Financial Management (CFM) [Service Cost Optimization Playbook](https://catalog.workshops.aws/awscff/en-US/playbooks).  
Use the detailed recommendations in AWS Compute Optimizer to understand the potential impact of these changes on cost and performance.

**Additional resources**  
+ [Viewing Amazon ECS services on Fargate recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-ecs-recommendations.html)
+ [Metrics for Amazon ECS services on Fargate](https://docs.aws.amazon.com/compute-optimizer/latest/ug/ecs-fargate-metrics-analyzed.html)
+ [AWS Fargate for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html#fargate-task-sizing)
+ [Updating an Amazon ECS service using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html)

**Report columns**  
+ Status
+ Region
+ Resource ID
+ Recommended Action
+ Current Resource Summary
+ Recommended Resource Summary
+ Estimated Monthly Cost
+ Estimated Monthly Savings
+ Last Refresh Time stamp

## Amazon MemoryDB reserved node purchase recommendations
<a name="memorydb-reserved-node-purchase-recommendations"></a>

**Description**  
Checks your Amazon MemoryDB usage patterns to provide recommendations for potential cost savings through reserved node purchases.  
This check generates recommendations at [payer scope for the payer account and at linked scope for a linked account](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html).  
For each resource, Trusted Advisor shows only the top recommended action from AWS Cost Optimization Hub.  
To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1z7kmr16n`

**Source**  
`AWS Cost Optimization Hub`

**Alert criteria**  
Yellow: Account has a cost savings action identified by Cost Optimization Hub for MemoryDB.

**Recommended action**  
Consider [implementing the recommendation](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-optimization-strategies.html). For more information on implementing these recommendations, see the AWS Cloud Financial Management (CFM) [Service Cost Optimization Playbook](https://catalog.workshops.aws/awscff/en-US/playbooks).

**Additional resources**  
+ [MemoryDB reserved nodes](https://docs.aws.amazon.com/memorydb/latest/devguide/nodes.reservednodes.html)
+ [Accessing reservation recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ri-recommendations.html)
+ [Working with reserved nodes](https://docs.aws.amazon.com/memorydb/latest/devguide/reserved-nodes-working-with.html)

**Report columns**  
+ Status
+ Region
+ Recommended Resource Summary
+ Estimated Monthly Cost
+ Estimated Monthly Savings
+ Last Refresh Time stamp

## Amazon OpenSearch Service Reserved Instance purchase recommendations
<a name="os-ri-purchase-recommendations"></a>

**Description**  
Checks your Amazon OpenSearch Service usage patterns to provide recommendations for potential cost savings through Reserved Instance (RI) purchases.  
This check generates recommendations at [payer scope for the payer account and at linked scope for a linked account](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html).  
Trusted Advisor shows only the top recommended action from AWS Cost Optimization Hub.  
To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1z7kmr14n`

**Source**  
`AWS Cost Optimization Hub`

**Alert criteria**  
Yellow: Account has a cost savings action identified by Cost Optimization Hub for Amazon OpenSearch Service.

**Recommended action**  
Consider [implementing the recommendation](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-optimization-strategies.html). For more information on implementing these recommendations, see the AWS Cloud Financial Management (CFM) [Service Cost Optimization Playbook](https://catalog.workshops.aws/awscff/en-US/playbooks).

**Additional resources**  
+ [Reserved Instances in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ri.html)
+ [Accessing reservation recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ri-recommendations.html)
+ [Purchasing Reserved Instances (AWS CLI)](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ri-cli.html)

**Report columns**  
+ Status
+ Region
+ Recommended Resource Summary
+ Estimated Monthly Cost
+ Estimated Monthly Savings
+ Last Refresh Time stamp

## Amazon RDS cost optimization recommendations for DB instances
<a name="rds-cost-opt-for-db-instances"></a>

**Description**  
Checks your Amazon RDS DB instance configurations and usage patterns to provide recommendations for potential cost savings.  
For each resource, Trusted Advisor shows only the top recommended action from AWS Cost Optimization Hub.  
To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1z7kmr03n`

**Source**  
`AWS Cost Optimization Hub`

**Alert criteria**  
Yellow: RDS DB instance has a cost savings action identified by Cost Optimization Hub.

**Recommended action**  
Consider implementing the recommendation. The recommendation is one of the recommendation types listed in [Understanding cost optimization strategies](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-optimization-strategies.html) in the *AWS Cost Management User Guide*. For more information on implementing these recommendations, see the AWS Cloud Financial Management (CFM) [Service Cost Optimization Playbook](https://catalog.workshops.aws/awscff/en-US/playbooks).  
Use the detailed recommendations in AWS Compute Optimizer to understand the potential impact of these changes on cost and performance.

**Additional resources**  
+ [Viewing RDS database recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-rds-recommendations.html.html)
+ [RDS database metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/rds-metrics-analyzed.html)
+ [DB instance classes](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.DBInstanceClass.html)
+ [Modifying an Amazon RDS DB instance ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.DBInstance.Modifying.html)

**Report columns**  
+ Status
+ Region
+ Resource ID
+ Recommended Action
+ Current Resource Summary
+ Recommended Resource Summary
+ Estimated Monthly Cost
+ Estimated Monthly Savings
+ Last Refresh Time stamp

## Amazon RDS cost optimization recommendations for DB instance storage
<a name="rds-cost-opt-for-db-instance-storage"></a>

**Description**  
Checks your Amazon RDS DB instance storage configurations and usage patterns to provide recommendations for potential cost savings.  
For each resource, Trusted Advisor shows only the top recommended action from AWS Cost Optimization Hub.  
To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1z7kmr04n`

**Source**  
`AWS Cost Optimization Hub`

**Alert criteria**  
Yellow: RDS DB storage has a cost savings action identified by Cost Optimization Hub.

**Recommended action**  
Consider implementing the recommendation. The recommendation is one of the recommendation types listed in [Understanding cost optimization strategies](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-optimization-strategies.html) in the *AWS Cost Management User Guide*. For more information on implementing these recommendations, see the AWS Cloud Financial Management (CFM) [Service Cost Optimization Playbook](https://catalog.workshops.aws/awscff/en-US/playbooks).  
Use the detailed recommendations in AWS Compute Optimizer to understand the potential impact of these changes on cost and performance.

**Additional resources**  
+ [Viewing RDS database recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-rds-recommendations.html)
+ [Amazon RDS DB instance storage](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Storage.html)

**Report columns**  
+ Status
+ Region
+ Resource ID
+ Recommended Action
+ Current Resource Summary
+ Recommended Resource Summary
+ Estimated Monthly Cost
+ Estimated Monthly Savings
+ Last Refresh Time stamp

## Amazon RDS idle DB instances
<a name="amazon-rds-idle-dbs-instances"></a>

**Description**  
This is a legacy check. We recommend using the new check (Check ID: [c1z7kmr03n](#rds-cost-opt-for-db-instances)) that offers additional customized recommendations.
Checks the configuration of your Amazon Relational Database Service (Amazon RDS) for any database (DB) instances that appear to be idle.  
If a DB instance has not had a connection for a prolonged period of time, you can delete the instance to reduce costs. A DB instance is considered idle if the instance hasn't had a connection in the past 7 days. If persistent storage is needed for data on the instance, you can use lower-cost options such as taking and retaining a DB snapshot. Manually created DB snapshots are retained until you delete them.  
This check reports the resources that are flagged by the criteria and the total number of resources evaluated, including `OK` resources. The resources table lists only the flagged resources.

**Check ID**  
`Ti39halfu8`

**Alert Criteria**  
Yellow: An active DB instance has not had a connection in the last 7 days.

**Recommended action**  
 Consider taking a snapshot of the idle DB instance and then either stopping it or deleting it. Stopping the DB instance removes some of the costs for it, but does not remove storage costs. A stopped instance keeps all automated backups based upon the configured retention period. Stopping a DB instance usually incurs additional costs when compared to deleting the instance and then retaining only the final snapshot. See [Stopping an Amazon RDS instance temporarily](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_StopInstance.html) and [Deleting a DB Instance with a Final Snapshot](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html).

**Additional resources**  
[Back Up and Restore](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.BackupRestore.html)

**Report columns**  
+ Region
+ DB Instance Name
+ Multi-AZ
+ Instance Type
+ Storage Provisioned (GB)
+ Days Since Last Connection
+ Estimated Monthly Savings (On Demand)

## Amazon RDS Reserved Instance purchase recommendations
<a name="rds-ri-purchase-recommendations"></a>

**Description**  
Checks your Amazon RDS usage patterns to provide recommendations for potential cost savings through Reserved Instance (RI) purchases.  
This check generates recommendations at [payer scope for the payer account and at linked scope for a linked account](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html).  
Trusted Advisor shows only the top recommended action from AWS Cost Optimization Hub.  
To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1z7kmr11n`

**Source**  
`AWS Cost Optimization Hub`

**Alert criteria**  
Yellow: EBS volume has a cost savings action identified by Cost Optimization Hub.

**Recommended action**  
Consider [implementing the recommendation](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-optimization-strategies.html). For more information on implementing these recommendations, see the AWS Cloud Financial Management (CFM) [Service Cost Optimization Playbook](https://catalog.workshops.aws/awscff/en-US/playbooks).

**Additional resources**  
+ [Reserved DB instance for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html)
+ [Accessing reservation recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ri-recommendations.html)
+ [Purchasing reserved DB instances for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.WorkingWith.html)

**Report columns**  
+ Status
+ Region
+ Recommended Resource Summary
+ Estimated Monthly Cost
+ Estimated Monthly Savings
+ Last Refresh Time stamp

## Amazon Redshift reserved node purchase recommendations
<a name="redshift-reserved-node-purchase-recommendations"></a>

**Description**  
Checks your Amazon Redshift usage patterns to provide recommendations for potential cost savings through reserved node purchases.  
This check generates recommendations at [payer scope for the payer account and at linked scope for a linked account](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html).  
Trusted Advisor shows only the top recommended action from AWS Cost Optimization Hub.  
To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1z7kmr12n`

**Source**  
`AWS Cost Optimization Hub`

**Alert criteria**  
Yellow: Account has a cost savings action identified by Cost Optimization Hub for Amazon Redshift.

**Recommended action**  
Consider [implementing the recommendation](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-optimization-strategies.html). For more information on implementing these recommendations, see the AWS Cloud Financial Management (CFM) [Service Cost Optimization Playbook](https://catalog.workshops.aws/awscff/en-US/playbooks).

**Additional resources**  
+ [Reserved nodes](https://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-instance.html)
+ [Accessing reservation recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ri-recommendations.html)
+ [Purchasing a reserved node](https://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-offering-console.html)

**Report columns**  
+ Status
+ Region
+ Recommended Resource Summary
+ Estimated Monthly Cost
+ Estimated Monthly Savings
+ Last Refresh Time stamp

## Amazon Route 53 Latency Resource Record Sets
<a name="amazon-route-53-latency-resource-record-sets"></a>

**Description**  
Checks for Amazon Route 53 latency record sets that are configured inefficiently.   
To allow Amazon Route 53 to route queries to the AWS Region with the lowest network latency, you should create latency resource record sets for a particular domain name (such as example.com) in different Regions. If you create only one latency resource record set for a domain name, all queries are routed to one Region, and you pay extra for latency-based routing without getting the benefits.   
Hosted zones created by AWS services won’t appear in your check results.   
This check reports the resources that are flagged by the criteria and the total number of resources evaluated, including `OK` resources. The resources table lists only the flagged resources.

**Check ID**  
`51fC20e7I2`

**Alert Criteria**  
Yellow: Only one latency resource record set is configured for a particular domain name.

**Recommended Action**  
If you have resources in multiple regions, be sure to define a latency resource record set for each region. See [Latency-Based Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency).  
If you have resources in only one AWS Region, consider creating resources in more than one AWS Region and define latency resource record sets for each; see [Latency-Based Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-latency).  
If you don't want to use multiple AWS Regions, you should use a simple resource record set. See [Working with Resource Record Sets](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/rrsets-working-with.html). 

**Additional Resources**  
+ [Amazon Route 53 Developer Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/)
+ [Amazon Route 53 Pricing](https://aws.amazon.com/route53/pricing/)

**Report columns**  
+ Hosted Zone Name
+ Hosted Zone ID
+ Resource Record Set Name
+ Resource Record Set Type

## Amazon S3 Bucket Lifecycle Policy Configured
<a name="amazon-s3-bucket-lifecycle-policy-configured"></a>

**Description**  
Checks if an Amazon S3 bucket has a lifecycle policy configured. An Amazon S3 lifecycle policy ensures that Amazon S3 objects inside the bucket are stored cost-effectively throughout their lifecycle. This is important for meeting regulatory requirements for data retention and storage. The policy configuration is a set of rules that define actions applied by the Amazon S3 service to a group of objects. A lifecycle policy allows you to automate transitioning objects to lower-cost storage classes or deleting them as they age. For example, you can transition an object to Amazon S3 Standard-IA storage 30 days after creation, or to Amazon Glacier after 1 year.  
You can also define object expiration so that Amazon S3 deletes the object on your behalf after a certain period of time.  
You can adjust the check configuration using the parameters in your AWS Config rules  
For more information, see [Managing your storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz100`

**Source**  
`AWS Config Managed Rule: s3-lifecycle-policy-check`

**Alert Criteria**  
 Yellow: Amazon S3 bucket has no lifecycle policy configured.

**Recommended Action**  
Make sure that you have a lifecycle policy configured in your Amazon S3 bucket.  
If your organization does not have a retention policy in place, consider using Amazon S3 Intelligent-Tiering to optimize cost.  
For information on how to define your Amazon S3 lifecycle policy, see [Setting lifecycle configuration on a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html).  
For information on Amazon S3 Intelligent-Tiering, see [Amazon S3 Intelligent-Tiering storage class](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) 

**Additional Resources**  
[Setting lifecycle configuration on a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html)  
[Examples of S3 Lifecycle configuration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameteres

## Amazon S3 Incomplete Multipart Upload Abort Configuration
<a name="s3-incomplete-multipart-upload-abort-config"></a>

**Description**  
Checks that each Amazon S3 bucket is configured with a lifecycle rule to abort multipart uploads that remain incomplete after 7 days. Using a lifecycle rule to abort these incomplete uploads and delete the associated storage is recommended.  
Results for this check are automatically refreshed one or more times each day, and refresh requests are not allowed. It might take a few hours for changes to appear. It might take a few hours for changes to appear. For Business, Enterprise On-Ramp, or Enterprise Support customers, you can use the `BatchUpdateRecommendationResourceExclusion` API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1cj39rr6v`

**Alert criteria**  
Yellow: The lifecycle configuration bucket does not contain a lifecycle rule to abort all multipart uploads that remain incomplete after 7 days. 

**Recommended action**  
Review lifecycle configuration for buckets without a lifecycle rule that would cleanup all incomplete multipart uploads. Uploads that are not completed after 24 hours are unlikely to be completed. Click [here](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html#lc-expire-mpu) to follow instructions to create a lifecycle rule. It is recommended that this is applied to all objects in your bucket. If you have a need to apply other lifecycle actions to selected objects in your bucket, you can have multiple rules with different filters. Check the storage lens dashboard or call the ListMultipartUpload API for more information. 

**Additional Resources**  
[Creating a lifecycle configuration ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html#lifecycle-config-overview-how)  
[Discovering and Deleting Incomplete Multipart Uploads to Lower Amazon S3 Costs](https://aws.amazon.com/blogs/aws-cloud-financial-management/discovering-and-deleting-incomplete-multipart-uploads-to-lower-amazon-s3-costs/)  
[Uploading and copying objects using multipart upload](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpuoverview.html)  
[Lifecycle configuration elements](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intro-lifecycle-rules.html)  
[Elements to describe lifecycle actions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intro-lifecycle-rules.html#intro-lifecycle-rules-actions)  
[Lifecycle configuration to abort multipart uploads](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html#lc-expire-mpu)

**Report columns**  
+ Status
+ Region
+ Bucket Name
+ Bucket ARN
+ Lifecycle rule for deleting incomplete MPU
+ Days After Initiation
+ Last Updated Time

## Amazon S3 version-enabled buckets without lifecycle policies configured
<a name="amazon-s3-version-enabled-buckets-no-lifecycle-policy"></a>

**Description**  
Checks if Amazon S3 version-enabled buckets have a lifecycle policy configured..  
For more information, see [Managing your storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html).  
You can specify the bucket names that you want to check using the **bucketNames** parameters in your AWS Config rules.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c18d2gz171`

**Source**  
`AWS Config Managed Rule: s3-version-lifecycle-policy-check`

**Alert criteria**  
Yellow: An Amazon S3 version-enabled bucket with doesn't have a lifecycle policy configured.

**Recommended action**  
Configure lifecycle policies for your Amazon S3 buckets to manage your objects so that they are stored cost effectively throughout their lifecycle.  
For more information, see [Setting lifecycle configuration on a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html).

**Additional resources**  
[Managing your storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)  
[Setting lifecycle configuration on a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html)

**Report columns**  
+ Status
+ Region
+ Resource
+ AWS Config Rule
+ Input Parameters
+ Last Updated Time

## AWS Lambda cost optimization recommendations for functions
<a name="lambda-cost-opt-for-functions"></a>

**Description**  
Checks your AWS Lambda configurations and usage patterns to provide recommendations for potential cost savings.  
For each resource, Trusted Advisor shows only the top recommended action from AWS Cost Optimization Hub.  
To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1z7kmr05n`

**Source**  
`AWS Cost Optimization Hub`

**Alert criteria**  
Yellow: Lambda function has a cost savings action identified by Cost Optimization Hub.

**Recommended action**  
Consider implementing the recommendation. The recommendation is one of the recommendation types listed in [Understanding cost optimization strategies](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-optimization-strategies.html) in the *AWS Cost Management User Guide*. For more information on implementing these recommendations, see the AWS Cloud Financial Management (CFM) [Service Cost Optimization Playbook](https://catalog.workshops.aws/awscff/en-US/playbooks).  
Use the detailed recommendations in AWS Compute Optimizer to understand the potential impact of these changes on cost and performance.

**Additional resources**  
+ [Viewing Lambda function recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-lambda-recommendations.html)
+ [Lambda function metrics](https://docs.aws.amazon.com/compute-optimizer/latest/ug/lambda-metrics-analyzed.html)
+ [Configuring AWS Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-functions.html)

**Report columns**  
+ Status
+ Region
+ Resource ID
+ Recommended Action
+ Current Resource Summary
+ Recommended Resource Summary
+ Estimated Monthly Cost
+ Estimated Monthly Savings
+ Last Refresh Time stamp

## AWS Lambda functions with excessive timeouts
<a name="aws-lambda-functions-excessive-timeouts"></a>

**Description**  
Checks for Lambda functions with high timeout rates that might result in high cost.   
Lambda charges based on run time and number of requests for your function. Function timeouts result in errors that may cause retries. Retrying functions will incur additionally request and run time charges.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`L4dfs2Q3C3`

**Alert criteria**  
Yellow: Functions where > 10% of invocations end in an error due to a timeout on any given day within the last 7 days.

**Recommended action**  
Inspect function logging and X-ray traces to determine the contributor to the high function duration. Implement logging in your code at relevant parts, such as before or after API calls or database connections. By default, AWS SDK clients timeouts may be longer than the configured function duration. Adjust API and SDK connection clients to retry or fail within the function timeout. If the expected duration is longer than the configured timeout, you can increase the timeout setting for the function. For more information, see [Monitoring and troubleshooting Lambda applications](https://docs.aws.amazon.com/lambda/latest/dg/lambda-monitoring.html).

**Additional resources**  
+ [Monitoring and troubleshooting Lambda applications](https://docs.aws.amazon.com/lambda/latest/dg/lambda-monitoring.html)
+ [Lambda Function Retry Timeout SDK](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-function-retry-timeout-sdk/)
+ [Using AWS Lambda with AWS X-Ray](https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html)
+ [Accessing Amazon CloudWatch logs for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html)
+ [Error Processor Sample Application for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/samples-errorprocessor.html)

**Report columns**  
+ Status
+ Region
+ Function ARN
+ Max Daily Timeout Rate
+ Date of Max Daily Timeout Rate
+ Average Daily Timeout Rate
+ Function Timeout Settings (millisecond)
+ Lost Daily Compute Cost
+ Average Daily Invokes
+ Current Day Invokes
+ Current Day Timeout Rate
+ Last Updated Time

## AWS Lambda functions with high error rates
<a name="aws-lambda-functions-with-high-error-rates"></a>

**Description**  
Checks for Lambda functions with high error rates that might result in higher costs.   
Lambda charges are based on the number of requests and aggregate run time for your function. Function errors may cause retries that incur additional charges.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`L4dfs2Q3C2`

**Alert criteria**  
Yellow: Functions where > 10% of invocations end in error on any given day within the last 7 days.

**Recommended action**  
Consider the following guidelines to reduce errors. Function errors include errors returned by the function's code and errors returned by the function's runtime.   
To help you troubleshoot Lambda errors, Lambda integrates with services like Amazon CloudWatch and AWS X-Ray. You can use a combination of logs, metrics, alarms, and X-Ray tracing to quickly detect and identify issues in your function code, API, or other resources that support your application. For more information, see [Monitoring and troubleshooting Lambda applications](https://docs.aws.amazon.com/lambda/latest/dg/lambda-monitoring.html).   
For more information on handling errors with specific runtimes, see [Error handling and automatic retries in AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/invocation-retries.html).   
For additional troubleshooting, see [Troubleshooting issues in Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-troubleshooting.html).   
You can also choose from an ecosystem of monitoring and observability tools provided by AWS Lambda partners. For more information, see [AWS Lambda Partners](https://aws.amazon.com/lambda/partners/?partner-solutions-cards.sort-by=item.additionalFields.partnerNameLower&partner-solutions-cards.sort-order=asc).

**Additional resources**  
+ [Error Handling and Automatic Retries in AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/invocation-retries.html)
+ [Monitoring and Troubleshooting Lambda applications](https://docs.aws.amazon.com/lambda/latest/dg/lambda-monitoring.html)
+ [Lambda Function Retry Timeout SDK](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-function-retry-timeout-sdk/)
+ [Troubleshooting issues in Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-troubleshooting.html)
+ [API Invoke Errors](https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html#API_Invoke_Errors)
+ [Error Processor Sample Application for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/samples-errorprocessor.html)

**Report columns**  
+ Status
+ Region
+ Function ARN
+ Max Daily Error Rate
+ Date for Max Error Rate
+ Average Daily Error Rate
+ Lost Daily Compute Cost
+ Current Day Invokes
+ Current Day Error Rate
+ \*Average Daily Invokes
+ Last Updated Time

## AWS Lambda over-provisioned functions for memory size
<a name="aws-lambda-over-provisioned-functions-memory-size"></a>

**Description**  
This is a legacy check. We recommend using the new check (Check ID: [c1z7kmr05n](#lambda-cost-opt-for-functions)) that offers additional customized recommendations.
Checks the AWS Lambda functions that were invoked at least once during the lookback period. This check alerts you if any of your Lambda functions were over-provisioned for memory size. When you have Lambda functions that are over-provisioned for memory sizes, you’re paying for unused resources. Although some scenarios can result in low utilization by design, you can often lower your costs by changing the memory configuration of your Lambda functions. Estimated monthly savings are calculated by using the current usage rate for Lambda functions.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`COr6dfpM05`

**Alert criteria**  
 Yellow: A Lambda function that was over-provisioned for memory size during the lookback period. To determine if a Lambda function is over-provisioned, we consider all default CloudWatch metrics for that function. The algorithm used to identify over-provisioned Lambda functions for memory size follows AWS best practices. The algorithm is updated when a new pattern has been identified.

**Recommended action**  
 Consider reducing the memory size of your Lambda functions.  
For more information, see [Opt in AWS Compute Optimizer for Trusted Advisor checks](compute-optimizer-with-trusted-advisor.md).

**Report columns**  
+ Status
+ Region
+ Function Name
+ Function Version
+ Memory Size (MB)
+ Recommended Memory Size (MB)
+ Lookback Period (days)
+ Savings Opportunity (%)
+ Estimated Monthly Savings
+ Estimated Monthly Savings Currency
+ Last Updated Time

## AWS Savings Plans purchase recommendations for compute
<a name="savings-plans-purchase-recommendations-compute"></a>

**Description**  
Checks your AWS compute usage patterns across Amazon EC2, AWS Fargate, andAWS Lambda and provides Savings Plans purchase recommendations. With these recommendations, you can commit to a consistent usage amount measured in dollars per hour in exchange for discounted rates.  
This check generates recommendations at [payer scope for the payer account and at linked scope for a linked account](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html).  
Trusted Advisor shows only the top recommended action from AWS Cost Optimization Hub.  
To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1z7kmr09n`

**Source**  
`AWS Cost Optimization Hub`

**Alert criteria**  
Yellow: Account has a cost savings action identified by Cost Optimization Hub for compute resources.

**Recommended action**  
Consider [implementing the recommendation](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-optimization-strategies.html). For more information on implementing these recommendations, see the AWS Cloud Financial Management (CFM) [Service Cost Optimization Playbook](https://catalog.workshops.aws/awscff/en-US/playbooks).

**Additional resources**  
+ [What are Savings Plans?](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html)
+ [Savings Plans types](https://docs.aws.amazon.com/savingsplans/latest/userguide/plan-types.html)
+ [Purchasing Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-purchase.html)

**Report columns**  
+ Status
+ Region
+ Recommended Resource Summary
+ Estimated Monthly Cost
+ Estimated Monthly Savings
+ Last Refresh Time stamp

## AWS Savings Plans purchase recommendations for Amazon SageMaker AI
<a name="savings-plans-purchase-recommendations-sagemaker"></a>

**Description**  
Checks your usage of Amazon SageMaker AI and provides Savings Plans purchase recommendations. With these recommendations, you can commit to a consistent usage amount measured in dollars per hour in exchange for discounted rates.  
This check generates recommendations at [payer scope for the payer account and at linked scope for a linked account](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html).  
Trusted Advisor shows only the top recommended action from AWS Cost Optimization Hub.  
To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html).  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`c1z7kmr08n`

**Source**  
`AWS Cost Optimization Hub`

**Alert criteria**  
Yellow: Account has a cost savings action identified by Cost Optimization Hub for Amazon SageMaker AI.

**Recommended action**  
Consider [implementing the recommendation](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-optimization-strategies.html). For more information on implementing these recommendations, see the AWS Cloud Financial Management (CFM) [Service Cost Optimization Playbook](https://catalog.workshops.aws/awscff/en-US/playbooks).

**Additional resources**  
+ [What are Savings Plans?](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html)
+ [Savings Plans types](https://docs.aws.amazon.com/savingsplans/latest/userguide/plan-types.html)
+ [Purchasing Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-purchase.html)

**Report columns**  
+ Status
+ Region
+ Recommended Resource Summary
+ Estimated Monthly Cost
+ Estimated Monthly Savings
+ Last Refresh Time stamp

## AWS Well-Architected high risk issues for cost optimization
<a name="well-architected-high-risk-issues-cost-optimization"></a>

**Description**  
Checks for high risk issues (HRIs) for your workloads in the cost optimization pillar. This check is based on your AWS-Well Architected reviews. Your check results depend on whether you completed the workload evaluation with AWS Well-Architected.  
Results for this check are automatically refreshed several times daily, and refresh requests are not allowed. It might take a few hours for changes to appear.  
For AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan customers, you can use the [BatchUpdateRecommendationResourceExclusion](https://docs.aws.amazon.com/trustedadvisor/latest/APIReference/API_BatchUpdateRecommendationResourceExclusion.html) API to include or exclude one or more resources from your Trusted Advisor results.

**Check ID**  
`Wxdfp4B1L1`

**Alert Criteria**  
+ Red: At least one active high risk issue was identified in the cost optimization pillar for AWS Well-Architected.
+ Green: No active high risk issues were detected in the cost optimization pillar for AWS Well-Architected.

**Recommended Action**  
AWS Well-Architected detected high risk issues during your workload evaluation. These issues present opportunities to reduce risk and save money. Sign in to the [AWS Well-Architected](https://console.aws.amazon.com/wellarchitected) tool to review your answers and take action to resolve your active issues.

**Report columns**  
+ Status
+ Region
+ Workload ARN
+ Workload Name
+ Reviewer Name
+ Workload Type
+ Workload Started Date
+ Workload Last Modified Date
+ Number of identified HRIs for Cost Optimization
+ Number of HRIs resolved for Cost Optimization
+ Number of questions answered for Cost Optimization
+ Total number of questions in Cost Optimization pillar
+ Last Updated Time

## Idle Load Balancers
<a name="idle-load-balancers"></a>

**Description**  
Checks your Elastic Load Balancing configuration for load balancers that are idle.   
Any load balancer that is configured accrues charges. If a load balancer has no associated back-end instances, or if network traffic is severely limited, the load balancer is not being used effectively. This check currently only checks for Classic Load Balancer type within ELB service. It does not include other ELB types (Application Load Balancer, Network Load Balancer).  
This check reports the resources that are flagged by the criteria and the total number of resources evaluated, including `OK` resources. The resources table lists only the flagged resources.

**Check ID**  
`hjLMh88uM8`

**Alert Criteria**  
+ Yellow: A load balancer has no active back-end instances.
+ Yellow: A load balancer has no healthy back-end instances.
+ Yellow: A load balancer has had less than 100 requests per day for the last 7 days.

**Recommended Action**  
If your load balancer has no active back-end instances, consider registering instances or deleting your load balancer. See [Registering Your Amazon EC2 Instances with Your Load Balancer](https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/US_DeReg_Reg_Instances.html#RegisteringInstances) or [Delete Your Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-getting-started.html#delete-load-balancer).  
If your load balancer has no healthy back-end instances, see [Troubleshooting Elastic Load Balancing: Health Check Configuration](https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/ts-elb-healthcheck.html).  
If your load balancer has had a low request count, consider deleting your load balancer. See [Delete Your Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-getting-started.html#delete-load-balancer).

**Additional Resources**  
+ [Managing Load Balancers](https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/UserScenarios.html)
+ [Troubleshoot Elastic Load Balancing](https://docs.aws.amazon.com/ElasticLoadBalancing/latest/DeveloperGuide/elb-troubleshooting.html)

**Report columns**  
+ Region
+ Load Balancer Name
+ Reason
+ Estimated Monthly Savings

## Idle NAT gateways
<a name="idle-nat-gateways"></a>

**Description**  
Checks your NAT gateway configurations and usage patterns to identify idle or underutilized NAT gateways that might be candidates for cost optimization.  
For each resource, Trusted Advisor shows only the top recommended action from AWS Cost Optimization Hub.  
To use this check, you must opt in to [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) and [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/account-opt-in.html).

**Check ID**  
`c1z7kmr18n`

**Source**  
`AWS Cost Optimization Hub`

**Alert criteria**  
Yellow: NAT gateway has a cost savings action identified by Cost Optimization Hub.

**Recommended action**  
Consider implementing the recommendation to delete the idle NAT gateway. For more information on implementing this recommendation, see the AWS Cloud Financial Management [Service Cost Optimization Playbook](https://catalog.workshops.aws/awscff/en-US/playbooks).

**Additional resources**  
+ [Viewing idle resource recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-idle-recommendations.html)
+ [Work with NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-working-with.html)
+ [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)

**Report columns**  
+ Status
+ Region
+ Resource ID
+ Recommended Action
+ Current Resource Summary
+ Recommended Resource Summary
+ Estimated Monthly Cost
+ Estimated Monthly Savings
+ Last Refresh Timestamp

## Inactive AWS Network Firewall
<a name="inactive-network-firewall"></a>

**Description**  
Checks your AWS Network Firewall endpoints and alerts you when the Network Firewall appears to be inactive.   
A Network Firewall is considered to be inactive if all its endpoints have no data processed the last 30 days. Network Firewall endpoints incur hourly charges. This check alerts you to Network Firewall with no data processed in the last 30 days. It’s a best practice to either remove unused Network Firewalls or update your architecture.

**Check ID**  
`c2vlfg0bfw`

**Alert Criteria**  
+ Yellow: The Network Firewall processed 0 bytes in the last 30 days.
+ Green: The Network Firewall processed more than 0 bytes in the last 30 days.

**Recommended Action**  
If the Network Firewall wasn’t used in the last 30 days, then consider deleting the Network Firewall.  
If a Transit Gateway is used for inter-VPC communication, then consider deploying your Network Firewalls in a centralized network inspection architectures. This can reduce the hourly charges on inactive Network Firewalls.

**Additional Resources**  
[AWS Network Firewall Pricing](https://aws.amazon.com/network-firewall/pricing/)  
[Inspection Deployment Models with AWS Network Firewall](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/inspection-deployment-models-with-AWS-network-firewall-ra.pdf)

**Report columns**  
+ Status
+ Region
+ Network Firewall Arn
+ VPC Id
+ Subnets
+ TotalBytesProcessed
+ Last Updated Time

## Inactive VPC interface endpoints
<a name="inactive-vpc-interface-endpoints"></a>

**Description**  
Checks your VPC interface endpoints and alerts you when the endpoints appear to be inactive. A VPC interface endpoint is considered to be inactive if it has no data processed in the last 30 days. VPC interface endpoints have hourly charges and data processing costs. This check alerts you about VPC interface endpoints with 0 data processed in the last 30 days. It’s a best practice to either remove unused VPC interface endpoints or update your architecture. 

**Check ID**  
`c2vlfg0jp6`

**Alert Criteria**  
+ Yellow: VPC interface endpoint has processed 0 bytes in the last 30 days.
+ Green: VPC interface endpoint has processed more than 0 bytes in the last 30 days

**Recommended Action**  
If the VPC interface endpoint had not been used in the last 30 days, consider deleting the VPC interface endpoint.  
If Transit Gateway is used for inter-VPC communication, then consider deploying your VPC interface endpoints in a centralized architecture to reduce the hourly charges on inactive VPC interface endpoints. 

**Additional Resources**  
+ [AWS PrivateLink Pricing](https://aws.amazon.com/privatelink/pricing/)
+ [Centralized access to VPC private endpoints](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-access-to-vpc-private-endpoints.html)

**Report columns**  
+ Status
+ Region
+ VPC Endpoint Id
+ VPC Id
+ Subnet Ids
+ Service Name
+ TotalBytesProcessed
+ Last Updated Time

## Inactive Gateway Load Balancer endpoints
<a name="inactive-gateway-load-balancer"></a>

**Description**  
Checks your Gateway Load Balancer endpoints and warns when they appear to be inactive. A Gateway Load Balancer endpoint is considered to be underutilized if it has no data processed in the last 30 days. Gateway Load Balancer endpoints have hourly charges and data processed charges. This check alerts you to Gateway Load Balancer endpoints with 0 data processed in the last 30 days. We recommend that you either remove unused Gateway Load Balancer endpoints, or update your architecture.

**Check ID**  
`c2vlfg0k35`

**Alert Criteria**  
+ Yellow: Gateway Load Balancer endpoint processed 0 bytes in the last 30 days
+ Green: Gateway Load Balancer endpoint processed more than 0 bytes in the last 30 days

**Recommended Action**  
If the Gateway Load Balancer endpoint has not been used in the last 30 days, consider deleting the VPC endpoint.  
If Transit Gateway is used for inter-VPC communication, consider deploying your Gateway Load Balancer endpoints in a centralized network inspection architecture to reduce the hourly charges on inactive Gateway Load Balancer endpoints. 

**Additional Resources**  
[AWS PrivateLink Pricing](https://aws.amazon.com/vpc/pricing/)  
[Centralized inspection architecture with AWS Gateway Load Balancer and AWS Transit Gateway](https://aws.amazon.com/blogs/networking-and-content-delivery/centralized-inspection-architecture-with-aws-gateway-load-balancer-and-aws-transit-gateway)

**Report columns**  
+ Status
+ Region
+ VPC Endpoint Id
+ VPC Id
+ Subnet Id
+ Service Name
+ TotalBytesProcessed
+ Last Updated Time

## Inactive NAT Gateways
<a name="inactive-nat-gateways"></a>

**Description**  
Checks your NAT Gateways for inactive gateways. A NAT Gateway is considered to be inactive if no data (0 bytes) was processed in the last 30 days. NAT Gateways have hourly charges and data processed charges.

**Check ID**  
`c2vlfg022t`

**Alert Criteria**  
+ Yellow: The NAT Gateway processed 0 bytes in the last 30 days
+ Green: The NAT Gateway processed more than 0 bytes in the last 30 days

**Recommended Action**  
Consider deleting any NAT Gateways that weren’t used in the last 30 days and that aren’t required for external network access outside the VPC.  
If a Transit Gateway is used for inter-VPC communication, then consider deploying a centralized NAT Gateway for egress to internet architecture. This can reduce the hourly cost from inactive NAT Gateways. 

**Additional Resources**  
[NAT Gateway Pricing](https://aws.amazon.com/vpc/pricing/)  
[Centralized egress to internet](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-egress-to-internet.html)

**Report columns**  
+ Status
+ Region
+ NAT Gateway Id
+ Subnet Id
+ VPC Id
+ TotalBytesFromDest
+ TotalBytesFromSrc
+ TotalBytes
+ Last Updated Time

## Low utilization Amazon EC2 instances
<a name="low-utilization-amazon-ec2-instances"></a>

**Description**  
This is a legacy check. We recommend using the new check (Check ID: [c1z7kmr00n](#ec2-cost-opt-for-instances)) that offers additional customized recommendations.
Checks the Amazon Elastic Compute Cloud (Amazon EC2) instances that were running at any time during the last 14 days. This check alerts you if the daily CPU utilization was 10% or less and network I/O was 5 MB or less for at least 4 days.  
Running instances generate hourly usage charges. Although some scenarios can result in low utilization by design, you can often lower your costs by managing the number and size of your instances.   
Estimated monthly savings are calculated by using the current usage rate for On-Demand Instances and the estimated number of days the instance might be underutilized. Actual savings will vary if you are using Reserved Instances or Spot Instances, or if the instance is not running for a full day. To get daily utilization data, download the report for this check.   
This check reports the resources that are flagged by the criteria and the total number of resources evaluated, including `OK` resources. The resources table lists only the flagged resources.

**Check ID**  
`Qch7DwouX1`

**Alert Criteria**  
Yellow: An instance had 10% or less daily average CPU utilization and 5 MB or less network I/O on at least 4 of the previous 14 days.

**Recommended Action**  
Consider stopping or terminating instances that have low utilization, or scale the number of instances by using Auto Scaling. For more information, see [Stop and Start Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html), [Terminate Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html), and [What is Auto Scaling?](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/WhatIsAutoScaling.html)

**Additional Resources**  
+ [Monitoring Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-monitoring.html)
+ [Instance Metadata and User Data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AESDG-chapter-instancedata.html)
+ [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/)
+ [Auto Scaling Developer Guide](https://docs.aws.amazon.com/AutoScaling/latest/DeveloperGuide/WhatIsAutoScaling.html)

**Report columns**  
+ Region/AZ
+ Instance ID
+ Instance Name
+ Instance Type
+ Estimated Monthly Savings
+ CPU Utilization 14-day Average
+ Network I/O 14-Day Average
+ Number of Days Low Utilization

## Unassociated Elastic IP Addresses
<a name="unassociated-elastic-ip-addresses"></a>

**Description**  
Checks for Elastic IP addresses (EIPs) that are not associated with a running Amazon Elastic Compute Cloud (Amazon EC2) instance.   
EIPs are static IP addresses designed for dynamic cloud computing. Unlike traditional static IP addresses, EIPs mask the failure of an instance or Availability Zone by remapping a public IP address to another instance in your account. A nominal charge is imposed for an EIP that is not associated with a running instance.  
This check reports the resources that are flagged by the criteria and the total number of resources evaluated, including `OK` resources. The resources table lists only the flagged resources.

**Check ID**  
`Z4AUBRNSmz`

**Alert Criteria**  
Yellow: An allocated Elastic IP address (EIP) is not associated with a running Amazon EC2 instance.

**Recommended Action**  
 Associate the EIP with a running active instance, or release the unassociated EIP. For more information, see [Associating an Elastic IP Address with a Different Running Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html#using-instance-addressing-eips-associating-different) and [Releasing an Elastic IP Address](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html#using-instance-addressing-eips-releasing).

**Additional Resources**  
[Elastic IP Addresses](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)

**Report columns**  
+ Region
+ IP Address

## Underutilized Amazon EBS volumes
<a name="underutilized-amazon-ebs-volumes"></a>

**Description**  
Checks Amazon Elastic Block Store (Amazon EBS) volume configurations and warns when volumes appear to be underutilized.   
Charges begin when a volume is created. If a volume remains unattached or has very low write activity (excluding boot volumes) for a period of time, the volume is underutilized. We recommend that you remove underutilized volumes to reduce costs.  
This check reports the resources that are flagged by the criteria and the total number of resources evaluated, including `OK` resources. The resources table lists only the flagged resources.

**Check ID**  
`DAvU99Dc4C`

**Alert Criteria**  
Yellow: A volume is unattached or had less than 1 IOPS per day for the past 7 days.

**Recommended Action**  
Consider creating a snapshot and deleting the volume to reduce costs. For more information, see [Creating an Amazon EBS Snapshot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-snapshot.html) and [Deleting an Amazon EBS Volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-deleting-volume.html).

**Additional Resources**  
+ [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html)
+ [Monitoring the Status of Your Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-volume-status.html)

**Report columns**  
+ Region
+ Volume ID
+ Volume Name
+ Volume Type
+ Volume Size
+ Monthly Storage Cost
+ Snapshot ID
+ Snapshot Name
+ Snapshot Age

**Note**  
If you opted in your account for AWS Compute Optimizer, we recommend that you use the Amazon EBS over-provisioned volumes check instead. For more information, see [Opt in AWS Compute Optimizer for Trusted Advisor checks](compute-optimizer-with-trusted-advisor.md).

## Underutilized Amazon Redshift Clusters
<a name="underutilized-amazon-redshift-clusters"></a>

**Description**  
Checks your Amazon Redshift configuration for clusters that appear to be underutilized.   
If an Amazon Redshift cluster has not had a connection for a prolonged period of time, or is using a low amount of CPU, you can use lower-cost options such as downsizing the cluster, or shutting down the cluster and taking a final snapshot. Final snapshots are retained even after you delete your cluster.

**Check ID**  
`G31sQ1E9U`

**Alert Criteria**  
+ Yellow: A running cluster has not had a connection in the last 7 days.
+ Yellow: A running cluster had less than 5% cluster-wide average CPU utilization for 99% of the last 7 days.

**Recommended Action**  
Consider shutting down the cluster and taking a final snapshot, or downsizing the cluster. See [Shutting Down and Deleting Clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#rs-mgmt-shutdown-delete-cluster) and [Resizing a Cluster](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#cluster-resize-intro).

**Additional Resources**  
[Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/)

**Report columns**  
+ Status
+ Region
+ Cluster
+ Instance Type
+ Reason
+ Estimated Monthly Savings