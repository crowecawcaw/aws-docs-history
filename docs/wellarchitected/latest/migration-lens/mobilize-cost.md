

# Mobilize 
<a name="mobilize-cost"></a>

 As you start planning for your migration in the mobilize phase, you need to consider planning for optimizing resource utilization and cost management. To achieve this, use existing automation tools to streamline migration processes effectively. Additionally, minimize data transfer to conserve bandwidth and mitigate data egress costs, ensuring a cost-effective transition. Right-sizing replication servers is essential to prevent bottlenecks without unnecessary over-provisioning. Furthermore, establish robust cost and usage governance through IAM policies and define a customized cost allocation strategy tailored to your organization's financial management needs. These practices collectively contribute to a smooth and cost-efficient mobilization of your migration efforts. 


| MIG-COST-02: Are you using automation efficiently for your migration? | 
| --- | 
|   | 

 AWS and our partners offer a wide variety of tools and services to help perform your migration. Use these tools efficiently to reduce infrastructure and operational costs during the migration.  

## MIG-COST-BP-2.1: Leverage existing tools to automate your migration
<a name="mig-cost-bp-2.1-leverage-existing-tools-to-automate-your-migration"></a>

 This BP applies to the following best practice areas: Cost-effective resources 

### Implementation guidance
<a name="implementation-guidance-78"></a>

 **Suggestion 2.1.1:** Understand the capabilities of each tool available, and select the one best suited to your situation.  

 AWS and our partners offer a [range of tools](https://aws.amazon.com/prescriptive-guidance/migration-tools/) to help migration. For instance, AWS Transform MGN can help with ongoing replication, planning, testing, and cutover for lift and shift server migrations. [AWS Migration Hub](https://docs.aws.amazon.com/migrationhub/latest/ug/migrate-wt-track.html) or [Cloud Migration Factory](https://aws.amazon.com/solutions/implementations/cloud-migration-factory-on-aws/) can provide additional planning and reporting functionality on top of MGN. Some tools are purpose-built for specific workloads, such as [Database Migration Service (DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) and [Kubernetes Migration Factory](https://aws.amazon.com/blogs/opensource/using-kubernetes-migration-factory-kmf-to-migrate-from-google-kubernetes-engine-gke-to-amazon-elastic-kubernetes-service-amazon-eks/). There are also many other tools offered by AWS partners. 

## MIG-COST-BP-2.2: Minimize the number of applications and the amount of data that is migrated
<a name="mig-cost-bp-2.2-minimize-the-number-of-applications-and-the-amount-of-data-that-is-migrated"></a>

 This BP applies to the following best practice areas: Cost-effective resources 

### Implementation guidance
<a name="implementation-guidance-79"></a>

 **Suggestion 2.2.1:** Only migrate what needs to be migrated and minimize ongoing replication.  

 In the analyze and mobilize phases, you may have discovered some applications that are still running but are no longer needed. Those are easy targets to retire to limit how much you're migrating. Consider discarding archival data that is beyond its useful retention period. Non-production servers for applications that are not in active development may also be retired.  

 Additionally, ongoing replication, such as change data capture (CDC) that MGN or AWS DMS uses, can consume a lot of bandwidth when the rate of change in the source server is high. Too much simultaneous replication may require additional bandwidth to avoid network issues. If migrating from another cloud service provider (CSP), you may incur unnecessary data egress costs when you have unnecessary replication. You can [reduce bandwidth requirements](https://docs.aws.amazon.com/mgn/latest/ug/Troubleshooting-Communication-Errors.html#Calculating-Bandwidth) by limiting the time your servers are actively replicating, as well as how many you are replicating simultaneously, especially the source servers with a high rate of change. 

## MIG-COST-BP-2.3: Right-size your replication servers to prevent bottlenecks without over-provisioning
<a name="mig-cost-bp-2.3-right-size-your-replication-servers-to-prevent-bottlenecks-without-over-provisioning"></a>

 This BP applies to the following best practice areas: Cost-effective resources 

### Implementation guidance
<a name="implementation-guidance-80"></a>

 **Suggestion 2.3.1:** Monitor your replication server performance and adjust their size as needed.  

 You can monitor [MGN](https://docs.aws.amazon.com/mgn/latest/ug/instance-type.html) and [DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_BestPractices.SizingReplicationInstance.html) replication server performance in CloudWatch. A replication server with too little performance causes a bottleneck that can increase costs elsewhere, such as operations. A replication server with too much performance can itself cost more than it needs. 


| MIG-COST-03: Have you established standards to measure, monitor and create accountability to manage the cost of operating in the cloud? | 
| --- | 
|   | 

 AWS provides tools and services for measuring, monitoring and creating accountability for your cloud spend. Your organization should establish a financial attribution model for the migrated resources. Creating a financial accountability model allows departments to cross-charge departments for shared resources. 

## MIG-COST-BP-3.1: Plan and set up cost and usage governance of AWS resources with help of IAM policies
<a name="mig-cost-bp-3.1-plan-and-set-up-cost-and-usage-governance-of-resources"></a>

 This BP applies to the following best practice areas: Expenditure and usage awareness 

### Implementation guidance
<a name="implementation-guidance-81"></a>

 **Suggestion 3.1.1:** To effectively manage the costs of your migration, it's essential to have robust control over your AWS resource usage. 

 Before embarking on mass migrations, establish access control standards in AWS by [creating and enforcing policies](https://aws.amazon.com/blogs/security/how-to-use-service-control-policies-to-set-permission-guardrails-across-accounts-in-your-aws-organization/) that are closely tied to migration objectives. These policies can be attached to AWS Identity and Access Management (IAM) principals, including roles or policies, as well as AWS resources. AWS offers various policy types to provide the flexibility needed for cost management within the migration process. 

 Identity-based policies should be employed to [define permissions for IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_iam_multiple-services-console.html). For instance, you can attach a policy to an IAM role, specifying that the role is permitted to launch specific instance types or access particular services. These identity-based policies play a crucial role in setting permissions boundaries, which facilitate governance aimed at cost control. 

 Additionally, resource-based policies should be applied to relevant AWS resources involved in your migration. For example, these policies can be attached to S3 buckets, Amazon SQS queues, VPC endpoints, and AWS Key Management Service encryption keys, aligning security and access controls with migration goals. This keeps cost management tightly integrated with your migration strategy and implementation. 

 For more detail, see the following: 
+  [How to manage cost overruns in your AWS multi-account environment](https://aws.amazon.com/blogs/mt/manage-cost-overruns-part-1/) 
+  [Control developer account costs with AWS CloudFormation and AWS Budgets](https://aws.amazon.com/blogs/mt/control-developer-account-costs-with-aws-cloudformation-and-aws-budgets/) 

## MIG-COST-BP-3.2: Define a cost allocation strategy that meets your organizations specific financial management process
<a name="mig-cost-bp-3.2-define-a-cost-allocation-strategy-that-meets-your-organizations-specific-financial-management-process"></a>

 This BP applies to the following best practice areas: Expenditure and usage awareness 

### Implementation guidance
<a name="implementation-guidance-82"></a>

 **Suggestion 3.2.1:** Migration cost can be optimized by creating a cost awareness culture in your organization.  

 A good way to start this shift is by information teams on how their decisions impact cost. [Cost allocation](https://aws.amazon.com/blogs/aws-cloud-financial-management/cost-allocation-basics-that-you-need-to-know/) is foundational to making informed decisions to best support business outcomes. To do this, you need to define a cost allocation strategy that speaks to your specific financial management process, and ties cost and resources usage data to the business needs and outcomes. 

 Set up [resource tagging for cost allocation](https://aws.amazon.com/blogs/aws-cloud-financial-management/cost-tagging-and-reporting-with-aws-organizations/). [Create your resource tags](https://aws.amazon.com/blogs/aws-cloud-financial-management/gs-create-and-enforce-your-tagging-strategy-for-more-granular-cost-visibility/), and then activate your [cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the Billing and Cost Management console. There are user-defined and AWS-generated cost allocation tags. Based on the types of services you need to tag and the level of customization you require, you can use one of these two cost allocation tags or a hybrid of both. [AWS Cost Categories](https://aws.amazon.com/aws-cost-management/aws-cost-categories/) allows you to logically group accounts and resources with attributes, such as tags, to better map your cost and usage information to your organizational structure. 

 Use four step process to design chargeback for shared services (for example, central compute savings plans, or enterprise support cost at billing account).  

1.  Decide on the cost units to chargeback to. 

1.  Calculate the total cost of the shared services. 

1.  Choose a distribution logic (equitable or proportional). 

1.  Gather the data to chargeback accurately. 

 For more detail, see [Chargeback \| AWS Cloud Financial Management](https://aws.amazon.com/blogs/aws-cloud-financial-management/tag/chargeback/). 

## MIG-COST-BP-3.3: Design a strategy to monitor, track and analyze your AWS cost and usage as you move resources to AWS
<a name="mig-cost-bp-3.3-design-a-strategy-to-monitor-track-and-analyze-your-cost-and-usage-as-you-move-resources"></a>

 This BP applies to the following best practice areas: Expenditure and usage awareness 

### Implementation guidance
<a name="implementation-guidance-83"></a>

 **Suggestion 3.3.1:** Implement appropriate management, tracking and measurement for your migration cost. 

 You can use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to [collect and track metrics](https://aws.amazon.com/aws-cost-management/aws-cost-optimization/monitor-track-and-analyze/), monitor log files, set alarms, and automatically react to changes in your AWS resources. You can also use Amazon CloudWatch to gain system-wide visibility into resource utilization, application performance, and operational health. 

 With [Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/), you can provision your resources following best practices to improve system performance and reliability, increase security, and look for opportunities to save money. You can also turn off non-production instances, and use Amazon CloudWatch and autoscaling to match increases or reductions in demand. 

 [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) has an easy-to-use interface that lets you visualize, understand, and manage your AWS costs and usage over time.  You can get started quickly by creating custom reports that analyze cost and usage data. Analyze your data at a high level (for example, total costs and usage across all accounts), or dive deeper into your cost and usage data to identify trends, pinpoint cost drivers, and detect anomalies. 