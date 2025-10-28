# Step 7: Monitor your outbound

workflow

Monitoring helps you track transformation success, identify issues, and maintain
operational visibility for your outbound EDI generation. AWS B2B Data Interchange integrates with CloudWatch
and EventBridge for comprehensive monitoring.

## Check CloudWatch logs

###### To review outbound transformation logs

1. Open the CloudWatch console.
2. Navigate to **Log groups**.
3. Find the log group named
   `/aws/vendedlogs/b2bi/p-`your-profile-id``.
4. Review transformation logs for success/failure status and EDI generation
   details.

## Set up EventBridge monitoring

(optional)

###### To configure event notifications

1. Open the EventBridge console.
2. Create a rule to capture AWS B2B Data Interchange outbound events.
3. Configure notifications for EDI generation completion.

## Monitor Amazon S3 directories

- Regularly check input directories for JSON file processing status
- Monitor output directories for generated EDI files
- Review any error files that may appear
- Verify EDI file formatting and control number sequences

## Monitoring points

- EDI generation success/failure rates
- Processing time for JSON to EDI transformation
- Control number sequence integrity
- EDI validation errors
- Amazon S3 storage usage
