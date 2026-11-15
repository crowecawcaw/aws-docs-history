

# ADVREL06-BP06 Implement proactive schedule validation and channel health monitoring
<a name="advrel06-bp06"></a>

 FAST channel failures usually come from scheduling errors, not infrastructure faults. Common causes include missing assets, incorrect timing, or gaps between programs. Pre-flight validation and synthetic monitoring catch these issues before they reach viewers. 

 **Desired outcome:** 
+  Every scheduled asset is validated for availability and format conformance at least 60 minutes before playout. 
+  Synthetic viewer probes detect issues before viewers do, enabling preemptive remediation. 
+  Operations teams have complete visibility into uptime, failover events, and scheduling issues through automated daily health reports. 

 **Common anti-patterns:** 
+  No pre-playout validation, asset unavailability discovered only at broadcast time 
+  Relying solely on infrastructure metrics, which misses application-level issues (stale manifests, expired segments) 
+  No synthetic monitoring, so infrastructure health is assumed to equal viewer experience health 
+  Manual channel health tracking, no systematic reporting of uptime or incident trends 

 **Benefits of establishing this best practice:** 
+  Proactive validation avoids the majority of FAST channel failures (which originate from scheduling errors, not infrastructure). 
+  Synthetic probes detect issues before viewers do, enabling preemptive remediation. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A schedule references an asset that was deleted, a wrong duration leaves a gap, or a rendition is missing for one program. These issues are visible ahead of playout. Automated pre-flight checks catch them before viewers report them. 

 Set the validation lead time to allow enough time to replace missing assets, close gaps, and re-transcode content before air. Longer lead times freeze the schedule earlier and constrain late programming changes. 

 Infrastructure metrics can look healthy while viewers are experiencing a black screen. A manifest can go stale, a segment can expire, or an Amazon S3 or CDN configuration change can break segment access after the validation pass succeeds. Pre-flight validation can't catch this drift because the problem appears after the check runs, but synthetic probes can. 

 The programming team owns the schedule and its timing. Operations owns the channel once it's live. A validation gate at the handoff catches scheduling mistakes before operations inherits them. Leadership needs trends in uptime and incidents. A steady record of failover events and scheduling gaps shows whether reliability is improving over time. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Deploy EPG validation pipeline triggered on schedule updates:** Implement a Lambda function triggered by schedule change events (through EventBridge when schedule files are written to S3). Validate: all asset IDs exist in S3, durations are within 5-second tolerance of scheduled slot, no gaps between program entries, all required renditions are present. Publish ScheduleValidationFailures metric to CloudWatch. 

1.  **Run validation 60 minutes before scheduled playout:** Configure an additional EventBridge scheduled rule that runs the validator 60 minutes before each scheduling window. For gaps detected within this window, automatically insert fallback content and notify operations. 

1.  **Implement synthetic viewer probes:** Deploy a Lambda function running every 5 minutes that fetches the channel's manifest URL and validates: HTTP 200 response, current segment timestamps within expected range, and segment URLs resolve. Alert when 3 consecutive checks fail, this indicates a viewer-facing issue even when infrastructure metrics appear healthy. 

1.  **Generate automated daily channel health reports:** Maintain daily channel health reports tracking: uptime percentage, failover events, slate insertion duration, and scheduling gap incidents. Store in Amazon Timestream and visualize in Amazon Managed Grafana for trend analysis. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL01-BP05 Through your CI/CD pipeline, implement regression, performance, and canary tests](advrel01-bp05.md) 
+  [ADVREL01-BP04 Implement chaos engineering practices](advrel01-bp04.md) 

 **Related documents:** 
+  [Monitoring channels using Amazon CloudWatch metrics](https://docs.aws.amazon.com/medialive/latest/ug/monitoring-eml-metrics.html) 

 **Related services:** 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 
+  [Amazon Timestream](https://aws.amazon.com/timestream/) 
+  [Amazon SNS](https://aws.amazon.com/sns/) 