

# SUS03-BP01 Optimize workloads for high resource usage efficiency

 Optimizing workloads to use resources efficiently and eliminate waste is fundamental to sustainable cloud operations. By implementing a cycle of measurement, optimization, and validation, you can identify and eliminate inefficiencies such as idle resources, over-provisioning, or inefficient processes. The goal is to maximize the business value per resource consumed, reducing both environmental impact and operational costs. 

 **Desired outcome:** 
+  Workloads operate at high efficiency, using the minimum resources necessary to meet business requirements. 
+  You keep resources appropriately sized and actively utilized. 
+  You decommission resources when no longer needed, minimizing waste across your cloud environment. 

 **Common anti-patterns:** 
+  Provisioning resources based on default settings, infrequent peaks, theoretical requirements, excessive SLAs, or unrealistic scenarios rather than actual needs. 
+  Failing to monitor resource utilization and identify optimization opportunities. 
+  Not taking action to reduce unused or underutilized cloud resources. 
+  Not retiring or refactoring inefficient application components. 
+  Treating optimization as a one-time project rather than an ongoing process. 
+  Optimizing only for cost, and not optimizing usage where there is no cost difference. 
+  Limiting optimization to compute only, and not considering other resources or components. 

 **Benefits of establishing this best practice:** 
+  Lowers the share of hardware-related impacts from raw material extraction to end-of-life treatment (Scope 3 emissions). 
+  Lowers the share of required energy for operating infrastructure (Scope 2 emissions). 
+  Optimization for resource usage efficiency complements cost- and performance-based approaches. Commercial discounts skew cost-based perspectives. Performance considerations focus on high or peak load scenarios. 
+  Contributes to a culture of efficiency and continuous improvement. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Optimizing workloads to reduce waste requires a systematic approach to monitoring, analysis, and improvement. By implementing a continuous optimization cycle, you can identify inefficiencies, implement improvements, and validate their impact on both performance and sustainability. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Establish baseline metrics for your workload: 
   +  Define [SUS01-BP01 Understand your resource usage efficiency](sus01-bp01.md) metrics that reflect both business outcomes and resource usage. 
   +  Implement monitoring using [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/). 
   +  Create dashboards that visualize efficiency metrics alongside performance metrics. 
   +  Maintain a resource inventory using AWS Resource Explorer, and track changes using [AWS Config](https://aws.amazon.com/config/). 
   +  Implement and enforce tagging with [tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) to establish clear ownership of resources. 

1.  Identify optimization opportunities: 
   +  Use [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) to identify right-sizing opportunities and idle resources across compute, storage, databases, and machine learning endpoints. 
   +  Analyze AWS Cost Explorer, Amazon CloudWatch Metrics, and [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) data to identify underutilized resources. 
   +  Identify services that provide on-demand capacity modes (such as [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode.html)), auto scaling features (such as [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Managing.Performance.html)), or [integrate with Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/integrated-services-list.html). 
   +  Conduct regular reviews of resource utilization and efficiency metrics. 
   +  Use [Application Observability (APM)](https://aws.amazon.com/cloudwatch/features/application-observability-apm/) traces to identify bottlenecks and inefficiencies in distributed applications. 
   +  Review resource inventory and recent changes. 
   +  Identify unattached or redundant components. 

1.  Implement targeted optimizations: 
   +  Decommission unused, obsolete, or unattached resources. 
   +  Refactor inefficient applications, application components, or processes. 
   +  Right-size over-provisioned resources based on actual utilization patterns. 
   +  Review auto-scaling policies and performance against observed demand. 

1.  Validate improvements and measure impact: 
   +  Compare pre-optimization and post-optimization RUE metrics to quantify improvements. 
   +  Verify that performance requirements continue to be met after optimizations. 
   +  Document lessons learned and successful optimization patterns. 

1.  Establish a continuous optimization process: 
   +  Schedule regular optimization reviews and activities. 
   +  Automate recurring optimizations where possible, such as removing unattached volumes or upgrading to latest-generation volume types on a schedule with [AWS Compute Optimizer automation rules](https://docs.aws.amazon.com/compute-optimizer/latest/ug/automation-rules.html). 
   +  Build optimization considerations into your development and deployment processes. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SUS01-BP01 Understand your resource usage efficiency](sus01-bp01.md) 
+  [SUS02-BP04 Define the baseload for predictable and steady-state workloads](sus02-bp04.md) 
+  [SUS02-BP01 Implement elasticity for variable workloads](sus02-bp01.md) 
+  [SUS04-BP01 Eliminate unnecessary data](sus04-bp01.md) 
+  [COST06-BP01 Perform cost modeling](cost06-bp01.md) 
+  [COST04-BP01 Define network and data transfer infrastructure costs](cost04-bp01.md) 
+  [COST02-BP01 Implement granular resource tagging for workload cost allocation](cost02-bp01.md) 

 **Related documents:** 
+  [What is Application Auto Scaling?](https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html) 
+  [What is Amazon EC2 Auto Scaling?](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) 
+  [What is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) 
+  [Viewing Compliance and Inventory Data in the Aggregator Dashboard for AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/viewing-the-aggregate-dashboard.html) 
+  [Use resharding, scaling, and parallel processing to change the number of shards](https://docs.aws.amazon.com/streams/latest/dev/kinesis-record-processor-scaling.html) 

 **Related blog posts:** 
+  [Introducing Automated Amazon EBS Volume Optimization in AWS Compute Optimizer](https://aws.amazon.com/blogs/aws-cloud-financial-management/introducing-automated-amazon-ebs-volume-optimization-in-aws-compute-optimizer/) 

 **Related videos:** 
+  [AWS re:Invent 2023 - Capacity, availability, cost efficiency: Pick three (CMP207)](https://www.youtube.com/watch?v=E0dYLPXrX_w) 
+  [AWS re:Invent 2023 - Sustainable compute: Reducing costs and carbon emissions with AWS (CMP212)](https://www.youtube.com/watch?v=0Bl1SDU2HxI) 

 **Related examples:** 
+  [Optimize Hardware Patterns and Observe Sustainability KPIs](https://catalog.workshops.aws/well-architected-sustainability/en-US/4-hardware-and-services/optimize-hardware-patterns-observe-sustainability-kpis) 