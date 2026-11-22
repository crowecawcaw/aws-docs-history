

# ADVREL06-BP09 Monitor format-specific error rates and implement automated format suspension

 Innovative ad format failures can be intermittent and device-specific. Without format-level monitoring, a rendering issue affecting 20% of viewers on a specific device type might go undetected for hours, costing ad revenue for that segment. 

 **Desired outcome:** 
+  Format rendering health is monitored in real time per format and device combination. 
+  Formats that exceed error thresholds are automatically suspended for affected device types, falling back to standard creatives. 
+  Automated re-enablement after successful probes confirms the issue is resolved. 

 **Common anti-patterns:** 
+  No per-format, per-device error rate monitoring, failures aggregated at too high a level to detect device-specific issues 
+  Manual format suspension requiring operations team intervention, hours of revenue loss before action 
+  No automated re-enablement, formats remain suspended long after issues are resolved 
+  No revenue impact visibility, team unaware of the financial cost of format failures 

 **Benefits of establishing this best practice:** 
+  Automated format suspension limits revenue loss to minutes (detection \+ suspension time) rather than hours (manual investigation \+ intervention). 
+  Automated re-enablement helps formats recover without operations team overhead. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 When a single format breaks on one device type, the overall error rate barely moves even as the affected segment loses every impression. Coarse monitoring obscures this phenomenon because failures span a large matrix of format types, device types, player versions, and OS versions, and each combination can fail alone. 

 Monitor each format-device combination to isolate failures. Narrow slices are more sensitive to transient CDN blips and short-lived player bugs, so use a longer observation window to filter out short-lived noise. 

 Suspension takes inventory offline. Set the error threshold high enough to avoid suspending a format for its normal error rate, while still low enough to suspend it during a sustained failure. 

 Without automatic re-enablement, a suspended format keeps losing inventory after the issue clears. Ad operations owns re-enablement, absorbs the false positives, and tunes thresholds continuously. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Deploy Kinesis Data Streams for format event collection:** Configure player SDK to publish format rendering events to Kinesis with format type, device type, player version, error code, and content title dimensions. Size shards for peak event throughput. Enable enhanced fan-out for real-time processing. 

1.  **Implement Flink streaming aggregation for rolling error rates:** Deploy a Managed Service for Apache Flink application that computes rolling 10-minute error rates per (format type × device type) combination. Publish results as CloudWatch custom metrics with format and device dimensions. 

1.  **Configure automated format suspension through Lambda:** Create a Lambda function triggered by CloudWatch alarm (format error rate exceeds 15% for 10 minutes). The function: updates DynamoDB format configuration table to disable the format for the affected device type, logs the suspension with timestamp and affected metrics, and sends SNS notification to the ad operations team. 

1.  **Implement automated format re-enablement:** Schedule a Lambda function that runs every 30 minutes to check suspended formats. Send synthetic ad requests from test devices. If 10 consecutive probes succeed, re-enable the format for that device type and send a recovery notification. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL01-BP05 Through your CI/CD pipeline, implement regression, performance, and canary tests](advrel01-bp05.md) 
+  [ADVREL08-BP01 Implement redundant ad verification systems with automated failover mechanisms](advrel08-bp01.md) 

 **Related documents:** 
+  [Optimizing AdTech end-user experiences using Amazon CloudWatch Internet Monitor](https://aws.amazon.com/blogs/networking-and-content-delivery/optimizing-adtech-end-user-experiences-using-amazon-cloudwatch-internet-monitor/) 
+  [Reducing the Scope of Impact with Cell-Based Architecture](https://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/reducing-scope-of-impact-with-cell-based-architecture.html) 

 **Related services:** 
+  [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) 
+  [Amazon Managed Service for Apache Flink](https://aws.amazon.com/managed-service-apache-flink/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [Amazon Timestream](https://aws.amazon.com/timestream/) 
+  [Amazon Managed Grafana](https://aws.amazon.com/grafana/) 