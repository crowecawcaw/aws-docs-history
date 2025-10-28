# Step 7: Monitor your inbound

workflow

Monitoring helps you track transformation success, identify issues, and maintain
operational visibility for your inbound EDI processing. AWS B2B Data Interchange integrates with CloudWatch
and EventBridge for comprehensive monitoring.

## Check CloudWatch logs

###### To review transformation logs

1. Open the CloudWatch console.
2. Navigate to **Log groups**.
3. Find the log group named
   `/aws/vendedlogs/b2bi/p-`your-profile-id``.
4. Review transformation logs for success/failure status.

## Set up EventBridge monitoring

(optional)

###### To configure event notifications

1. Open the EventBridge console.
2. Create a rule to capture AWS B2B Data Interchange events.
3. Configure notifications for transformation completion.

## Monitor Amazon S3 directories

- Regularly check input directories for processing status
- Monitor output directories for transformed files
- Review any error files that may appear

## Monitoring points

- Transformation success/failure rates
- Processing time for documents
- Error patterns and frequencies
- Amazon S3 storage usage
