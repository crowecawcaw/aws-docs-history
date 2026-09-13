

# SMREL02-BP01 Design processing workflows with redundancy and automatic error recovery
<a name="smrel02-bp01"></a>

Implement processing workflows that can withstand individual component failures through redundant processing pipelines, automatic retry mechanisms, and quality validation at each stage.

**Desired outcome:**
+ Content processing continues without interruption when individual encoding or packaging components fail, with consistent output quality and automatic recovery from transient errors.

**Benefits of establishing this best practice:**
+ Removes single points of failure in content processing
+ Maintains consistent output quality across all content
+ Enables automatic scaling to meet processing demand
+ Provides early detection of quality issues before distribution
+ Reduces manual intervention for common processing errors

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

Deploy processing components across multiple Availability Zones (AZs) with automatic failover capabilities. Use serverless architectures for batch processing to automatically scale based on demand. Implement quality validation checkpoints throughout the processing pipeline to catch issues early. Design workflows to be idempotent so operations can be safely retried without negative impact.

### Implementation steps
<a name="implementation-steps"></a>

1. **Configure redundant live encoding with AWS Elemental MediaLive:** Deploy standard channels with dual-pipeline architecture across different AZs. Configure automatic input failover between redundant sources. Set up output redundancy to multiple packaging origins. Enable embedded timecode for smooth pipeline switching.

1. **Implement resilient video on demand (VOD) processing using serverless workflows:** Use AWS Step Functions to orchestrate processing workflows with automatic retry logic. Deploy AWS Elemental MediaConvert jobs across multiple AZs. Configure dead letter queues for failed processing jobs. Implement exponential backoff for transient failures.

1. **Set up quality validation at each processing stage:** Validate input files before processing begins. Check encoding output for technical compliance and quality metrics. Verify packaging integrity and manifest accuracy. Implement automated quality scoring using AWS Elemental MediaPackage MQCS (Media Quality Confidence Scores).

1. **Configure cross-region processing for disaster recovery:** Replicate processing workflows in secondary AWS regions. Set up automatic failover for processing when the primary region fails. Keep processing templates and configurations consistent across regions.

1. **Implement processing monitoring and alerting:** Monitor MediaLive channel health and pipeline status. Track MediaConvert job success rates and processing times. Set up CloudWatch alarms for processing failures and quality degradation. Configure Amazon Simple Notification Service (SNS) notifications for immediate response to critical issues.