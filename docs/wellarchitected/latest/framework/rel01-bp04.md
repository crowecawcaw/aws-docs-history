

# REL01-BP04 Monitor and manage quotas

 Quota usage changes as a workload grows, and an increase request takes time to approve. Monitor consumption against each quota and raise quotas ahead of demand to support planned growth. Without monitoring, the first sign that you have run out of headroom is a failed operation in production. 

 **Desired outcome:** 
+  You monitor usage against quotas for the services your workload depends on, across every account and Region. 
+  Your alerts fire while there is still time to request and receive an increase before the quota is reached. 
+  You have a defined response for each alert, so a threshold breach leads to action rather than a silent notification. 
+  You track consumption trends and raise quotas to match planned growth. 

 **Common anti-patterns:** 
+  Teams set no monitoring for quota thresholds and discover exhaustion only when an operation fails. 
+  Teams assume a soft quota increase is granted immediately and plan no lead time. 
+  Teams configure alarms but define no process for responding when one fires. 
+  Teams monitor only the services supported by automated quota checks and ignore the rest. 
+  Teams overlook the extra quota that multi-Region resilience designs require during a failover. 

 **Benefits of establishing this best practice:** 
+  Tracking usage against quotas shows you are approaching a quota while there is still time to act. 
+  A defined response process turns each alert into a timely increase request rather than a missed warning. 
+  Accounting for approval lead time prevents increases that arrive after the workload has already been throttled. 
+  Trend data supports capacity planning for growth and for multi-Region failover. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 To monitor a quota, compare current usage against the quota value. Read usage through service APIs and metrics, then combine the two to get headroom as a percentage you can alert on. [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) does this for a subset of services. To cover the rest, use [AWS Config](https://aws.amazon.com/config/), [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), or scheduled functions. Metric filters on log data can surface usage that approaches a threshold when a direct metric is not available. 

 AWS publishes [usage metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AWS-API-Usage-Metrics.html) for many services in Amazon CloudWatch. For a subset, it [integrates Service Quotas with CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Quotas-Visualize-Alarms.html) so you can alarm on usage against the quota directly. Where that integration does not yet exist, set an alarm threshold from the published quota (or your increased value), and build your own integration between Service Quotas and usage metrics to automate the comparison. Start from the inventory of services the workload uses and confirm each service has some form of usage tracking, even if that means a custom check rather than a built-in report. Fixed quotas belong in this coverage too. You cannot raise a fixed quota, but knowing you are near one means you can shift load or trigger a redesign before usage reaches it. 

 Every threshold you monitor needs a defined response that names who acts and what they do, such as filing an increase request, shedding load, or escalating. Small increases are often approved automatically, but larger requests are reviewed by Support and can take time, and several requests submitted together may take longer. Set alert thresholds well below the quota to leave room for that delay. 

 In a multi-Region workload, a passive Region can look comfortably under its quotas until a failover concentrates load there. For guidance on reconciling quotas across Regions and accounts, see [REL01-BP02 Manage service quotas across accounts and regions](rel01-bp02.md). 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Capture current resource consumption:** Read current usage from service APIs, such as the Amazon EC2 DescribeInstances operation, to establish what the workload consumes now. Collect this per account and Region. 

1.  **Record the quotas that apply:** Gather the current values for the quotas that matter to your workload from [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html), [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/), service documentation, and the AWS CLI or SDKs. Include fixed quotas so monitoring covers them as well. 

1.  **Configure usage monitoring and alarms:** Set alarms that compare usage against each quota and notify the owning team as consumption approaches the quota. For services outside automated coverage, add [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) rules, scheduled functions, or [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) metric filters. 

1.  **Set thresholds that account for approval lead time:** Place alert thresholds far enough below each quota that an increase request can be submitted and approved before usage reaches the ceiling. Use the [service quota history](https://docs.aws.amazon.com/servicequotas/latest/userguide/) to review past increases per Region. 

1.  **Define a response for every alert:** For each monitored threshold, document who responds and what they do, including submitting an increase request, shedding load, or escalating. Make the response part of your operational runbooks. 

1.  **Reconcile quotas and usage across Regions:** For workloads that span multiple Regions, see [REL01-BP02 Manage service quotas across accounts and regions](rel01-bp02.md) for the approach to keeping quotas aligned across locations. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL01-BP05 Automate quota management](rel01-bp05.md) 
+  [REL01-BP02 Manage service quotas across accounts and regions](rel01-bp02.md) 
+  [REL01-BP01 Aware of service quotas and constraints](rel01-bp01.md) 
+  [REL01-BP06 Verify that a sufficient gap exists between the current quotas and the maximum usage to accommodate failover](rel01-bp06.md) 

 **Related documents:** 
+  [Availability and recovery objectives](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-availability-and-recovery-objectives.html) 
+  [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) 
+  [What is Service Quotas?](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) 
+  [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) 
+  [Using Service Quotas request templates](https://docs.aws.amazon.com/servicequotas/latest/userguide/organization-templates.html) 
+  [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) 
+  [Amazon EC2 service quotas](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html) 
+  [Service Authorization Reference](https://docs.aws.amazon.com/service-authorization/latest/reference/) 
+  [AWS Trusted Advisor check reference](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor-check-reference.html) 
+  [Managing and monitoring API throttling in your workloads](https://aws.amazon.com/blogs/mt/managing-monitoring-api-throttling-in-workloads/) 
+  [View AWS Trusted Advisor recommendations at scale with AWS Organizations](https://aws.amazon.com/blogs/mt/organizational-view-for-trusted-advisor/) 

 **Related videos:** 
+  [How do I manage my service quotas for my AWS services?](https://www.youtube.com/watch?v=Ddf5WG5I0Qo) 

 **Related tools:** 
+  [Quota Monitor for AWS](https://docs.aws.amazon.com/solutions/quota-monitor/) 
+  [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) 
+  [AWS Config](https://aws.amazon.com/config/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [Using CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 