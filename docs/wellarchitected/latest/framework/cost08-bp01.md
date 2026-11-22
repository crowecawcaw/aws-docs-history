

# COST08-BP01 Perform an analysis on the workload demand

 A workload's resource needs rise and fall with usage. Match provisioned capacity to that demand to control cost while meeting performance targets. Focus analysis on workloads where demand varies most and costs the most. 

 **Desired outcome:** 
+  You understand the predictability, rate of change, and magnitude of change in your workload's demand across a full business cycle. 
+  Your analysis covers seasonal variation, so periodic peaks such as end-of-month processing or holiday traffic are reflected in provisioning decisions. 
+  Your analysis effort is proportional to workload value, concentrated on high-value workloads with the largest demand swings. 
+  Your resource provisioning aligns with measured demand, so you meet performance requirements without persistent overprovisioning. 

 **Common anti-patterns:** 
+  Forecasting demand from historical data alone, ignoring future changes in the business, industry, or technology. 
+  Analyzing low-impact, stable workloads in depth while neglecting high-value, dynamic workloads that offer greater optimization potential. 
+  Sampling demand over a window too short to capture seasonal peaks, so provisioning misses predictable spikes. 
+  Provisioning for peak demand without knowing the response time the workload actually requires. 

 **Benefits of establishing this best practice:** 
+  Resource allocation matches actual demand, which reduces waste from idle capacity. 
+  Costs fall, because provisioning no longer defaults to peak-sized capacity. 
+  Performance requirements are met consistently, because provisioning decisions start from measured demand. 
+  Planning and budgeting improve, because demand patterns produce a data-based forecast. 
+  Resources adapt as demand changes, because the scaling strategy is grounded in known patterns. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Demand analysis describes both the pattern and the volume of a workload's resource use over time. Three characteristics matter most: how predictable the demand is, how fast it changes, and how large the swings are. These characteristics decide which scaling approach fits and how much capacity headroom you need. Use response-time targets as the reference point. If measured demand meets those targets, current supply is adequate. If it does not, adjust supply. 

 A short observation window is the most common source of a wrong conclusion. Many workloads look steady across a week and spike at the end of a month, a quarter, or a holiday period. Analyze a full business cycle so these periodic peaks appear in the data. Demand also shifts for reasons history can't predict, such as a planned campaign or entry into a new segment. 

 Spend analysis effort where variable demand and total cost are highest, because that is where better provisioning returns most. Deep study rarely pays for stable, low-cost workloads, but it pays for high-value workloads with sharp peaks. Before deciding how deeply to analyze, weigh a component's expected total cost and projected usage change over the workload's lifetime. 

 Utilization and performance metrics such as latency, throughput, and error rate show how hard resources work. User traffic patterns explain what drives that load. Workload type matters too, because batch processing, real-time streaming, and databases each carry a different resource profile. Service-level agreements set the performance the workload must hold, so compare measured behavior against them to find gaps. 

 [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) collects and tracks these metrics, monitors log files, and provides system-wide visibility into resource utilization and operational health. [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) and [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) evaluate your resources against best practices and identify where to resize or stop capacity to match demand. For advanced analysis, [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) and [AWS Quick](https://aws.amazon.com/quick/) work with your AWS Data Exports or application logs to correlate demand with cost. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Analyze existing workload data:** Gather usage data from the current workload, earlier versions, or comparable systems, and examine it with [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) metrics and log data. Cover a full business cycle so seasonal events such as end-of-month or end-of-year peaks appear in the results. Match effort to workload value by studying high-value workloads with large demand swings closely, and spend little on low-value workloads with flat demand. Record the predictability, rate of change, and magnitude of change you observe. 

1.  **Forecast external influences:** Meet with the teams that can change workload demand, such as sales, marketing, and business development. Learn the cycles they operate within, and identify upcoming events such as campaigns, launches, or expansions that will move demand beyond what history shows. Combine these inputs with the trend baseline to produce a forward-looking forecast. 

1.  **Validate demand against response time requirements:** Compare projected demand against the response times defined in your service-level agreements. Where measured demand meets those targets, current supply is adequate. Where it falls short, mark the workload for a change in supply, and use the gaps to prioritize which workloads move on to buffering, throttling, or dynamic scaling. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [COST08-BP02 Implement a buffer or throttle to manage demand](cost08-bp02.md) 
+  [COST08-BP03 Deploy resources dynamically](cost08-bp03.md) 
+  [COST06-BP02 Select resource type, size, and number based on data](cost06-bp02.md) 

 **Related documents:** 
+  [Getting started with Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html) 
+  [AWS Instance Scheduler](https://docs.aws.amazon.com/solutions/instance-scheduler-on-aws/) 
+  [Monitor, track, and analyze for cost optimization](https://aws.amazon.com/aws-cost-management/) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) 
+  [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) 
+  [Application Observability (APM)](https://aws.amazon.com/cloudwatch/features/application-observability-apm/) 
+  [AWS Auto Scaling](https://aws.amazon.com/autoscaling/) 
+  [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) 
+  [AWS Quick](https://aws.amazon.com/quick/) 