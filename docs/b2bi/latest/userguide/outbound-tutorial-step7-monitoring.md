

# Step 7: Monitor your outbound workflow
<a name="outbound-tutorial-step7-monitoring"></a>

Monitoring helps you track transformation success, identify issues, and maintain operational visibility for your outbound EDI generation. AWS B2B Data Interchange integrates with CloudWatch and EventBridge for comprehensive monitoring.

## Check CloudWatch logs
<a name="outbound-cloudwatch-monitoring"></a>

**To review outbound transformation logs**

1. Open the CloudWatch console.

1. Navigate to **Log groups**.

1. Find the log group named `/aws/vendedlogs/b2bi/p-{{your-profile-id}}`.

1. Review transformation logs for success/failure status and EDI generation details.

## Set up EventBridge monitoring (optional)
<a name="outbound-eventbridge-monitoring"></a>

**To configure event notifications**

1. Open the EventBridge console.

1. Create a rule to capture AWS B2B Data Interchange outbound events.

1. Configure notifications for EDI generation completion.

## Monitor Amazon S3 directories
<a name="outbound-s3-monitoring"></a>
+ Regularly check input directories for JSON file processing status
+ Monitor output directories for generated EDI files
+ Review any error files that may appear
+ Verify EDI file formatting and control number sequences

## Monitoring points
<a name="outbound-monitoring-points"></a>
+ EDI generation success/failure rates
+ Processing time for JSON to EDI transformation
+ Control number sequence integrity
+ EDI validation errors
+ Amazon S3 storage usage