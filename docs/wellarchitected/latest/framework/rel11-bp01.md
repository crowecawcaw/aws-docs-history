

# REL11-BP01 Monitor all components of the workload to detect failures

 You cannot heal, fail over, or scale a component until you know it has failed. Monitor every layer of your workload continuously and measure both technical health and business outcomes. When detection is fast and complete, automated and human responses have time to limit customer impact. 

 **Desired outcome:** 
+  You monitor every workload component independently across the application, infrastructure, and network layers. 
+  Your collection interval is short enough to detect failures within your recovery time objective (RTO). 
+  You track business key performance indicators (KPIs), not only technical metrics, so degraded customer outcomes raise alerts. 
+  You measure the real user experience with synthetic tests that run continuously from multiple locations. 
+  Your alarm thresholds give operators time to react before customers are affected. 

 **Common anti-patterns:** 
+  Teams run workloads without alarms, so problems surface only when customers complain. 
+  Alarms fire at thresholds that leave no time to react before impact. 
+  Teams collect metrics too infrequently to meet the recovery time objective. 
+  Monitoring covers only customer-facing interfaces and ignores internal components. 
+  Teams collect technical metrics but no business or user-experience metrics. 
+  Teams create so many monitors that real signals are lost in the noise. 

 **Benefits of establishing this best practice:** 
+  Recovery time drops because time to detection drops. 
+  Partial and gray failures become visible before they affect customers. 
+  Business KPI monitoring reveals problems that technical metrics alone miss. 
+  Synthetic testing detects customer-facing failures even when internal telemetry looks healthy. 
+  Operators investigate from dashboards and traces instead of guessing at root cause. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 The mean time to detection (MTTD) is the interval between a failure and when repair begins. Every second of that interval adds directly to your recovery time, so faster detection is the most direct way to meet an RTO. A shorter interval detects faults sooner but produces more data and costs more to store and process. Choose the interval by working backward from the recovery time you must meet, not from collection cost. 

 Complete coverage matters as much as speed. A workload fails through its weakest observed layer, so monitoring only the customer-facing endpoint hides faults in the application, infrastructure, and network beneath it. A *gray failure* is a degradation where the component still responds to health checks but serves slow or incorrect results, so simple up and down monitoring reports it as healthy. To detect gray failures, measure behavior that the component's own status does not reveal, such as latency percentiles, error ratios, and the experience of an outside caller. 

 Measure availability by the business value your workload delivers. A fleet can be entirely healthy while customers cannot complete a purchase because a downstream dependency is broken. Instrument the business functions that represent value, such as orders placed or sessions started, and treat those KPIs as first-class signals alongside CPU and disk. Synthetic canaries run real customer paths from outside the workload and catch failures that internal telemetry cannot see. 

 Excessive alarms produce fatigue, and operators start ignoring a channel that cries wolf. Aim for a small set of alarms that each map to a condition a human or an automation must act on. Send the rest to dashboards for investigation rather than paging. Replicate your monitoring and its data into a separate Region and account so that the failure you are trying to detect cannot also disable the tool that detects it. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Set the collection interval from your recovery target:** Determine how quickly each component must be recovered, then set the metric collection frequency to detect a fault within that window. Account for the RTO when deciding between standard and higher-resolution collection. 

1.  **Enable detailed monitoring for components and managed services:** Turn on the appropriate depth of monitoring for each service in the stack. Evaluate [detailed monitoring for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) and [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-cloudwatch-monitoring.html), [enhanced monitoring for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Monitoring.html), serverless and container metrics for [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics.html), [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/monitoring_automated_manual.html), [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/eks-observe.html), and [load balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-monitoring.html), and storage metrics for [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/monitoring-overview.html), [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/monitoring_overview.html), and [Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/monitoring-volume-checks.html). 

1.  **Instrument business KPIs:** Publish [custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) for the business functions the workload performs, such as transactions completed or items shipped. These metrics reveal indirect problems that infrastructure metrics do not expose. 

1.  **Measure the user experience with canaries:** Create [synthetic canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) that simulate customer behavior and run continuously against your endpoints from diverse locations. Publish [custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) that capture experience signals such as page latency and error rate. 

1.  **Configure alarms on the signals that require action:** [Set alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) that detect when a component is unhealthy and, where appropriate, trigger automated recovery. For guidance on designing effective alarms, routing notifications, and managing alert fatigue, see [REL11-BP06 Send notifications when events impact availability](rel11-bp06.md). 

1.  **Build dashboards for investigation:** Create [dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) that surface trends, outliers, and correlations so operators can locate a root cause quickly once an alarm fires. 

1.  **Monitor resilience posture as a signal:** Use [AWS Resilience Hub](https://docs.aws.amazon.com/resilience-hub/latest/userguide/what-is.html) to assess your application's resilience posture and run tests that validate recovery capabilities. Treat declining posture assessment results or failed tests as early signals that configuration changes have weakened your fault tolerance, and surface these findings alongside operational metrics in your dashboards. 

1.  **Detect gray failures with agentic analysis:** Use [AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent.html) to reason about correlated multi-signal degradations that rule-based alarms miss, such as where a component still responds to health checks but serves slow or incorrect results. The agent correlates metrics, logs, and traces across service boundaries to surface gray failures that no single threshold captures. 

1.  **Add distributed tracing:** Enable [distributed tracing](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) across your services to follow a request through its dependencies and isolate where latency or errors originate. 

1.  **Isolate monitoring from the failure it detects:** Collect and display metrics from a [separate Region and account](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create_xaxr_dashboard.html), and integrate [AWS Health Aware](https://aws.amazon.com/blogs/mt/aws-health-aware-customize-aws-health-alerts-for-organizational-and-personal-aws-accounts/) to gain visibility into AWS resource degradations that affect your workload. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL11-BP03 Automate healing on all layers](rel11-bp03.md) 
+  [REL11-BP06 Send notifications when events impact availability](rel11-bp06.md) 
+  [REL11-BP07 Architect your product to meet availability targets and uptime service level agreements (SLAs)](rel11-bp07.md) 
+  [REL06-BP01 Monitor all components for the workload (Generation)](rel06-bp01.md) 

 **Related documents:** 
+  [Understanding availability](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-availability-and-recovery-objectives.html) 
+  [Synthetic monitoring (canaries)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) 
+  [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) 
+  [Monitoring OS metrics with Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html) 
+  [Monitor CloudWatch metrics for your Auto Scaling groups and instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-cloudwatch-monitoring.html) 
+  [Publish custom metrics (PutMetricData / EMF)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) 
+  [Using Amazon CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) 
+  [Using Amazon CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) 
+  [Creating a CloudWatch cross-account cross-Region dashboard with the AWS Management Console](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create_xaxr_dashboard.html) 
+  [What is AWS Resilience Hub?](https://docs.aws.amazon.com/resilience-hub/latest/userguide/what-is.html) 
+  [About AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent.html) 
+  [Implementing AWS Health Aware (AHA)](https://aws.amazon.com/blogs/mt/aws-health-aware-customize-aws-health-alerts-for-organizational-and-personal-aws-accounts/) 

 **Related examples:** 
+  [One Observability Workshop: Explore AWS X-Ray](https://catalog.workshops.aws/observability/en-US/aws-native/xray/explore-xray) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [What is AWS X-Ray?](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) 