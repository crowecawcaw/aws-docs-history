

# COST07-BP01 Perform pricing model analysis

 Workload components differ in how long they run, how predictable their usage is, and whether they tolerate interruption. Match each component to the pricing model that suits its usage pattern, and revisit the match as demand changes. 

 **Desired outcome:** 
+  Each of your workload components runs on the pricing model that matches its usage pattern, whether steady, variable, or interruptible. 
+  You cover predictable, long-running usage with commitment-based discounts sized to actual utilization. 
+  You run interruptible and fault-tolerant work on discounted spare capacity rather than full-price capacity. 
+  You review commitments on a regular cadence and adjust them as usage patterns shift. 

 **Common anti-patterns:** 
+  Committing to long-term discounts for short-lived or bursting workloads that cannot use the commitment. 
+  Running steady, predictable workloads entirely at on-demand rates with no commitment discounts. 
+  Purchasing a commitment for a resource or usage type the discount does not apply to. 
+  Buying commitments once and never revisiting them as workloads grow or change shape. 
+  Treating capacity reservations as a discount rather than an availability guarantee. 

 **Benefits of establishing this best practice:** 
+  Each component runs at the lowest rate that fits its usage pattern. 
+  Commitments sized to real utilization reduce waste from unused discounts. 
+  Interruptible work runs at a fraction of on-demand cost. 
+  Regular review keeps the pricing mix aligned with changing demand. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Three questions sort a component into the right model: 
+  How predictable is its usage? 
+  How long does it run? 
+  Can it tolerate interruption? 

 A batch job that runs for an hour a day has different economics from a database that runs every hour of the year. Place each component on the model that charges the least for its pattern, and different components in the same workload often use different models. 

 *On-Demand Instances* charge for compute or database capacity by the hour or second with no commitment. The per-unit price is the highest, and the flexibility is the greatest. This model fits unpredictable, spiky, or short-lived usage where you cannot forecast demand and do not want to commit. 

 *Savings Plans* lower the rate in exchange for a commitment to a consistent amount of spend, measured in dollars per hour, over a one-year or three-year term. Compute Savings Plans apply across instance family, size, Region, and across Amazon EC2, AWS Fargate, and AWS Lambda, which keeps the discount flexible. The trade-off is commitment risk: usage that drops below the committed level is paid for regardless. Match the commitment to the floor of your steady usage, not its peak. 

 *Database Savings Plans* extend the same commitment model to managed database services, lowering the rate in exchange for a consistent dollars-per-hour commitment over a one-year term with a no-upfront payment option. They apply across Amazon Aurora, Amazon RDS, Amazon DynamoDB, Amazon ElastiCache, Amazon DocumentDB, Amazon Timestream, Amazon Neptune, Amazon Keyspaces (for Apache Cassandra), AWS DMS, and Amazon OpenSearch Service. They cover the latest provisioned instance generations and serverless usage regardless of engine, instance family, size, Availability Zone, or Region. The commitment applies to the highest-discount usage first and coexists with Reserved Instances and other Savings Plans. Size the commitment to the baseline of steady database usage. 

 *Reserved Instances* discount a specific set of instance attributes in exchange for a commitment. They are less flexible than Savings Plans, but they cover services that Savings Plans do not, including Amazon RDS, Amazon Redshift, Amazon ElastiCache, and Amazon OpenSearch Service. Savings Plans and Reserved Instances both offer all-upfront, partial-upfront, and no-upfront payment options, which trade discount depth against cash flow. For a broader treatment of commitment discounts, see [Optimizing costs with reservations](https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/aws-cost-optimization.html). 

 Buying commitments is usually an organization-level decision, not a workload-level one. Purchasing Savings Plans and Reserved Instances centrally from the management account applies the discount across the whole billing family. [Discount sharing](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ri-turn-off.html) is on by default, so unused commitment in one account offsets eligible usage in another. At the workload level, forecast the steady-state usage a central team can commit to, keep steady components eligible for the discount, and monitor how much of the workload's usage a commitment covers. Treat the central FinOps or cloud finance team as the buyer and the workload team as the source of the demand signal. 

 *Spot Instances* sell spare Amazon EC2 capacity at up to 90 percent off the on-demand price. The trade-off is interruption: AWS can reclaim the capacity with short notice. This model fits fault-tolerant and flexible work such as stateless web servers, containerized workloads, big-data and analytics jobs, and CI/CD pipelines. For serverless containers, AWS Fargate Spot runs interruptible tasks at a comparable discount. It does not fit stateful work that cannot checkpoint or resume. See [Spot Instances](https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/). 

 Two patterns are often confused with pricing models. Scheduling: many non-production resources run only during working hours, so stopping Amazon EC2 and Amazon RDS instances after hours and on weekends, or pausing Amazon Redshift clusters, cuts compute charges without any commitment. Capacity reservations: On-Demand Capacity Reservations (ODCR) reserve capacity when you need it, but they are billed at the on-demand rate whether you run instances or not. They are not a discount. Reserve capacity when availability matters, and layer a Savings Plan on top to discount the reserved usage. 

 Pricing also varies by resource type. Amazon S3 applies [tiered pricing](https://aws.amazon.com/s3/pricing/) across storage classes, so the effective rate falls as stored volume crosses defined thresholds and as data moves to colder classes. AWS publishes the full set of [pricing models](https://aws.amazon.com/pricing/) so you can compare options per service. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Analyze workload usage patterns:** Use the hourly granularity in [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) or a custom dashboard to examine how the number of running instances changes over time. Look for steady baselines that suit commitment discounts and for regular periods of elasticity that suit on-demand or Spot. Instances that run for short, interruptible periods are candidates for Spot Instances or Spot Fleet. 

1.  **Review existing contracts and commitments:** Analyze current commitments and how much of each is in use before buying more. Account for pre-existing contractual discounts and enterprise agreements so you do not commit twice. [Enterprise Agreements](https://aws.amazon.com/pricing/enterprise/) let you tailor terms to your needs for long-term commitments. 

1.  **Model commitments and share the recommendation:** Review the Savings Plans and [Reserved Instance recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ri-recommendations.html), and model a purchase with the [Savings Plans Purchase Analyzer](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-analyzer.html) before committing. Size the recommendation to your steady usage, confirm the discount covers the resource and usage type, and pass it to the team that owns central purchasing rather than buying in isolation. The same recommendations and Purchase Analyzer cover Database Savings Plans, so model database commitments there alongside compute. 

1.  **Identify Spot candidates:** From the elasticity analysis, select fault-tolerant and flexible components that can tolerate interruption, and move them to Spot capacity. Keep stateful or non-interruptible components on on-demand or commitment models. 

1.  **Schedule non-production resources:** Stop Amazon EC2 and Amazon RDS instances outside working hours, and pause Amazon Redshift clusters that are only needed at specific times. Compute billing halts while these resources are stopped, and only storage charges continue. 

1.  **Consolidate Amazon S3 storage under consolidated billing:** Combine linked account usage under a management account so all Amazon S3 usage counts toward the same tiered-pricing total. Aggregated volume reaches lower per-unit rates faster than isolated account usage. 

1.  **Monitor commitment coverage and utilization for the workload:** Track how much of the workload's eligible usage a commitment covers, and how fully those commitments are used, with the coverage and utilization reports in AWS Cost Explorer and [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html). Report uncovered steady usage back to the central purchasing team so future commitments track real demand. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST05-BP01 Identify workload requirements for cost](cost05-bp01.md) 
+  [COST06-BP02 Select resource type, size, and number based on data](cost06-bp02.md) 
+  [COST07-BP02 Choose Regions based on cost](cost07-bp02.md) 

 **Related documents:** 
+  [AWS pricing](https://aws.amazon.com/pricing/) 
+  [What are Savings Plans?](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html) 
+  [Savings Plans types](https://docs.aws.amazon.com/savingsplans/latest/userguide/plan-types.html) 
+  [How AWS Pricing Works](https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/abstract-and-introduction.html) 
+  [Savings Plans Purchase Analyzer](https://docs.aws.amazon.com/savingsplans/latest/userguide/sp-analyzer.html) 
+  [Accessing Reserved Instance recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ri-recommendations.html) 
+  [Turn off shared Reserved Instances and Savings Plans discounts](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ri-turn-off.html) 
+  [On-Demand Capacity Reservations pricing and billing](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-pricing-billing.html) 
+  [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/) 
+  [AWS Enterprise pricing](https://aws.amazon.com/pricing/enterprise/) 

 **Related examples:** 
+  [Consolidate optimization recommendations in Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html) 

 **Related workshops:** 
+  [CFM Technical Implementation Playbooks (CFM TIPs): Service cost optimization playbooks](https://catalog.workshops.aws/awscff/) 

 **Related services:** 
+  [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) 
+  [Savings Plans](https://aws.amazon.com/savingsplans/) 
+  [Reserved Instances](https://aws.amazon.com/aws-cost-management/aws-cost-optimization/reserved-instances/) 
+  [Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot/) 