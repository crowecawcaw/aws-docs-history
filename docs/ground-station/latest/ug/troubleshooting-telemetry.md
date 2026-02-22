# Troubleshoot telemetry

Use the following information to troubleshoot common issues with telemetry.

## Common setup issues

### IAM permission errors

**Symptoms**

When calling `CreateConfig` to create a TelemetrySinkConfig, you receive
an error:

```
Unable to write to Kinesis Data Streams stream. Ensure that Ground Station has
kinesis:PutRecord permissions for the given stream
```

**Causes**

- The IAM role specified in the TelemetrySinkConfig doesn't have the required
  permissions to write to the Kinesis Data Streams stream.
- The trust policy on the IAM role doesn't allow AWS Ground Station to assume the role.
- The Kinesis Data Streams stream ARN in the TelemetrySinkConfig is incorrect or the stream doesn't exist.

**Solutions**

1. Verify the IAM role exists and has the correct permissions. Review
   [Step 2: Create a TelemetrySinkConfig](telemetry.md#telemetry.setup.step2 "telemetry.md#telemetry.setup.step2") and ensure all steps were followed.
2. Check that AWS Ground Station can assume your IAM role:

```
aws iam get-role --role-name GroundStationTelemetryRole
```

Verify the trust policy includes `groundstation.amazonaws.com` as a
trusted service principal. 3. Verify the IAM role has the required Kinesis permissions:

```
aws iam list-attached-role-policies --role-name GroundStationTelemetryRole
```

Ensure the policy includes `kinesis:DescribeStream`,
`kinesis:PutRecord`, and `kinesis:PutRecords` permissions
for your stream. 4. Verify the Kinesis Data Streams stream exists and the ARN is correct:

```
aws kinesis describe-stream \
    --stream-name `your-stream-name` \
    --region `us-east-2`
```

5. If using customer-managed encryption, verify the IAM role has
   `kms:GenerateDataKey` permission for your AWS KMS key.

### PassRole permission errors

**Symptoms**

When calling `CreateConfig`, you receive an error about not having
permission to pass the IAM role.

**Solution**

Ensure your IAM user or role has `iam:PassRole` permission for the
telemetry IAM role. Add the following policy to your user or role:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:GetRole",
        "iam:PassRole"
      ],
      "Resource": "arn:aws:iam::`99999999999`:role/`your-stream-name`"
    }
  ]
}
```

### Kinesis Data Streams stream configuration issues

**Symptoms**

Telemetry delivery fails or is intermittent.

**Causes**

- The Kinesis Data Streams stream has insufficient capacity for the telemetry throughput.
- The stream is being used by other applications, causing write throttling.

**Solutions**

1. Check the stream status:

```
aws kinesis describe-stream \
    --stream-name `your-stream-name` \
    --region `us-east-2`
```

2. Monitor for write throttling using CloudWatch metrics:

```
aws cloudwatch get-metric-statistics \
    --namespace AWS/Kinesis \
    --metric-name WriteProvisionedThroughputExceeded \
    --dimensions Name=StreamName,Value=`your-stream-name` \
    --start-time `2025-12-08T00:00:00Z` \
    --end-time `2025-12-08T23:59:59Z` \
    --period 60 \
    --statistics Sum \
    --region `us-east-2`
```

3. If throttling is detected, consider:
   - Switching to on-demand capacity mode for automatic scaling.
   - Using a dedicated stream for AWS Ground Station telemetry.
   - If using provisioned mode, increasing the number of shards.

## Telemetry delivery problems

### No telemetry data appearing

**Symptoms**

After scheduling a contact with a telemetry-enabled mission profile, no telemetry
data appears in your Kinesis Data Streams stream.

**Possible causes and solutions**

Mission profile doesn't have telemetry enabled

Verify the mission profile used for the contact includes a
`telemetrySinkConfigArn`:

```
aws groundstation get-mission-profile \
    --mission-profile-id `12345678-1234-1234-1234-123456789012` \
    --region `us-east-2`
```

Check the output for the `telemetrySinkConfigArn` field. If it's
not present, the mission profile doesn't have telemetry enabled.

IAM role permissions issue

Review the IAM permission troubleshooting steps in
[IAM permission errors](#troubleshooting-telemetry.iam-permissions "#troubleshooting-telemetry.iam-permissions").

Kinesis Data Streams stream doesn't exist or is in wrong region

Verify the stream exists in the correct region:

```
aws kinesis describe-stream \
    --stream-name `your-stream-name` \
    --region `us-east-2`
```

Contact hasn't started yet

Telemetry delivery begins at contact start time. Verify
the contact has started by checking the contact status:

```
aws groundstation describe-contact \
    --contact-id `12345678-1234-1234-1234-123456789012` \
    --region `us-east-2`
```

### Intermittent telemetry data

**Symptoms**

Telemetry data is delivered inconsistently with gaps or missing records.

**Possible causes**

- Kinesis Data Streams stream capacity issues or throttling. See
  [Kinesis Data Streams stream configuration issues](#troubleshooting-telemetry.kinesis-config "#troubleshooting-telemetry.kinesis-config").
- Network connectivity issues between AWS Ground Station and your Kinesis Data Streams stream.

**Solutions**

- Monitor Kinesis Data Streams stream metrics in CloudWatch for throttling or errors.
- Ensure your stream is using on-demand capacity mode or has sufficient provisioned
  capacity.
- Use a dedicated stream for AWS Ground Station telemetry to avoid contention with other
  applications.

## Data format issues

### JSON parsing errors

**Symptoms**

Your application encounters errors when parsing telemetry records as JSON.

**Solutions**

- **Verify Base64 decoding** - Data in Kinesis Data Streams stream is
  Base64-encoded. Ensure you decode the data before parsing it as JSON. For more
  information, see
  [Reading data from Kinesis Data Streams stream](telemetry.md#telemetry.understanding-data.reading "telemetry.md#telemetry.understanding-data.reading").
- **Check for empty records** - AWS Ground Station may send empty
  validation records when creating a _TelemetrySinkConfig_.
  Your application should handle empty or malformed records gracefully.
- **Implement version-aware parsing** - Parse the
  `telemetryTypeAndVersion`, `telemetryType`, and `telemetryVersion`
  fields first to determine the appropriate schema for each record.

### Unknown telemetry types or versions

**Symptoms**

Your application encounters telemetry types or versions it doesn't recognize.

**Solution**

This is expected behavior as new telemetry types and schema versions may be introduced
over time. Your application should:

- Log unknown types and versions for monitoring.
- Continue processing known types and versions.
- Implement graceful handling for unknown schemas.

For more information about schema versioning, see
[Schema versioning and evolution](telemetry.md#telemetry.understanding-data.schema-evolution "telemetry.md#telemetry.understanding-data.schema-evolution").

## Getting help

If you continue to experience issues after following the troubleshooting steps, contact
AWS Support.

**Information to provide**

When contacting support, provide the following information:

- Contact IDs experiencing issues
- Mission profile ID used
- TelemetrySinkConfig ARN
- Kinesis Data Streams stream ARN
- IAM role ARN and attached policies
- Error messages from CloudWatch Logs or your application
- Timestamps when issues occurred
- Troubleshooting steps already taken

For general AWS Ground Station support, see the
[AWS Ground Station User Guide](what-is.md "what-is.md").
