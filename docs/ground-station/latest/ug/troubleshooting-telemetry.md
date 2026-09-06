

# Troubleshoot telemetry
<a name="troubleshooting-telemetry"></a>

 Use the following information to troubleshoot common issues with telemetry. 

## Common setup issues
<a name="troubleshooting-telemetry.setup-issues"></a>

### IAM permission errors
<a name="troubleshooting-telemetry.iam-permissions"></a>

 **Symptoms** 

 When calling `CreateConfig` to create a TelemetrySinkConfig, you receive an error: 

```
Unable to write to Kinesis Data Streams stream. Ensure that Ground Station has 
kinesis:PutRecord permissions for the given stream
```

 **Causes** 
+  The IAM role specified in the TelemetrySinkConfig doesn't have the required permissions to write to the Kinesis Data Streams stream. 
+  The trust policy on the IAM role doesn't allow AWS Ground Station to assume the role. 
+  The Kinesis Data Streams stream ARN in the TelemetrySinkConfig is incorrect or the stream doesn't exist. 

 **Solutions** 

1.  Verify the IAM role exists and has the correct permissions. Review [Step 2: Create a TelemetrySinkConfig](telemetry.setup.md#telemetry.setup.step2) and ensure all steps were followed. 

1.  Check that AWS Ground Station can assume your IAM role: 

   ```
   aws iam get-role --role-name GroundStationTelemetryRole
   ```

    Verify the trust policy includes `groundstation.amazonaws.com` as a trusted service principal. 

1.  Verify the IAM role has the required Kinesis permissions: 

   ```
   aws iam list-attached-role-policies --role-name GroundStationTelemetryRole
   ```

    Ensure the policy includes `kinesis:DescribeStream`, `kinesis:PutRecord`, and `kinesis:PutRecords` permissions for your stream. 

1.  Verify the Kinesis Data Streams stream exists and the ARN is correct: 

   ```
   aws kinesis describe-stream \
       --stream-name {{your-stream-name}} \
       --region {{us-east-2}}
   ```

1.  If using customer-managed encryption, verify the IAM role has `kms:GenerateDataKey` permission for your AWS KMS key. 

### PassRole permission errors
<a name="troubleshooting-telemetry.passrole"></a>

 **Symptoms** 

 When calling `CreateConfig`, you receive an error about not having permission to pass the IAM role. 

 **Solution** 

 Ensure your IAM user or role has `iam:PassRole` permission for the telemetry IAM role. Add the following policy to your user or role: 

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
      "Resource": "arn:aws:iam::{{123456789012}}:role/{{your-stream-name}}"
    }
  ]
}
```

### Kinesis Data Streams stream configuration issues
<a name="troubleshooting-telemetry.kinesis-config"></a>

 **Symptoms** 

 Telemetry delivery fails or is intermittent. 

 **Causes** 
+  The Kinesis Data Streams stream has insufficient capacity for the telemetry throughput. 
+  The stream is being used by other applications, causing write throttling. 

 **Solutions** 

1.  Check the stream status: 

   ```
   aws kinesis describe-stream \
       --stream-name {{your-stream-name}} \
       --region {{us-east-2}}
   ```

1.  Monitor for write throttling using CloudWatch metrics: 

   ```
   aws cloudwatch get-metric-statistics \
       --namespace AWS/Kinesis \
       --metric-name WriteProvisionedThroughputExceeded \
       --dimensions Name=StreamName,Value={{your-stream-name}} \
       --start-time {{2025-12-08T00:00:00Z}} \
       --end-time {{2025-12-08T23:59:59Z}} \
       --period 60 \
       --statistics Sum \
       --region {{us-east-2}}
   ```

1.  If throttling is detected, consider: 
   +  Switching to on-demand capacity mode for automatic scaling. 
   +  Using a dedicated stream for AWS Ground Station telemetry. 
   +  If using provisioned mode, increasing the number of shards. 

## Telemetry delivery problems
<a name="troubleshooting-telemetry.delivery-problems"></a>

### No telemetry data appearing
<a name="troubleshooting-telemetry.no-data"></a>

 **Symptoms** 

 After scheduling a contact with a telemetry-enabled mission profile, no telemetry data appears in your Kinesis Data Streams stream. 

 **Possible causes and solutions** 

Mission profile doesn't have telemetry enabled  
 Verify the mission profile used for the contact includes a `telemetrySinkConfigArn`:   

```
aws groundstation get-mission-profile \
    --mission-profile-id {{12345678-1234-1234-1234-123456789012}} \
    --region {{us-east-2}}
```
 Check the output for the `telemetrySinkConfigArn` field. If it's not present, the mission profile doesn't have telemetry enabled. 

IAM role permissions issue  
 Review the IAM permission troubleshooting steps in [IAM permission errors](#troubleshooting-telemetry.iam-permissions). 

Kinesis Data Streams stream doesn't exist or is in wrong region  
 Verify the stream exists in the correct region:   

```
aws kinesis describe-stream \
    --stream-name {{your-stream-name}} \
    --region {{us-east-2}}
```

Contact hasn't started yet  
 Telemetry delivery begins at contact start time. Verify the contact has started by checking the contact status:   

```
aws groundstation describe-contact \
    --contact-id {{12345678-1234-1234-1234-123456789012}} \
    --region {{us-east-2}}
```

Contact scheduled on a digital twin ground station  
 Digital twin ground stations do not support telemetry delivery. Contacts scheduled on digital twin antennas do not produce telemetry data. Verify that the ground station used for your contact is not a digital twin by checking the ground station name. Digital twin ground stations have a "Digital Twin " prefix in their name. For more information, see [Use the AWS Ground Station digital twin feature](digital-twin.md). 

### Intermittent telemetry data
<a name="troubleshooting-telemetry.intermittent"></a>

 **Symptoms** 

 Telemetry data is delivered inconsistently with gaps or missing records. 

 **Possible causes** 
+  Kinesis Data Streams stream capacity issues or throttling. See [Kinesis Data Streams stream configuration issues](#troubleshooting-telemetry.kinesis-config). 
+  Network connectivity issues between AWS Ground Station and your Kinesis Data Streams stream. 

 **Solutions** 
+  Monitor Kinesis Data Streams stream metrics in CloudWatch for throttling or errors. 
+  Ensure your stream is using on-demand capacity mode or has sufficient provisioned capacity. 
+  Use a dedicated stream for AWS Ground Station telemetry to avoid contention with other applications. 

## Data format issues
<a name="troubleshooting-telemetry.data-format"></a>

### JSON parsing errors
<a name="troubleshooting-telemetry.json-parsing"></a>

 **Symptoms** 

 Your application encounters errors when parsing telemetry records as JSON. 

 **Solutions** 
+  **Verify Base64 decoding** - Data in Kinesis Data Streams stream is Base64-encoded. Ensure you decode the data before parsing it as JSON. For more information, see [Reading data from Kinesis Data Streams stream](telemetry.understanding-data.md#telemetry.understanding-data.reading). 
+  **Check for empty records** - AWS Ground Station may send empty validation records when creating a *TelemetrySinkConfig*. Your application should handle empty or malformed records gracefully. 
+  **Implement version-aware parsing** - Parse the `telemetryTypeAndVersion`, `telemetryType`, and `telemetryVersion` fields first to determine the appropriate schema for each record. 

### Unknown telemetry types or versions
<a name="troubleshooting-telemetry.unknown-types"></a>

 **Symptoms** 

 Your application encounters telemetry types or versions it doesn't recognize. 

 **Solution** 

 This is expected behavior as new telemetry types and schema versions may be introduced over time. Your application should: 
+  Log unknown types and versions for monitoring. 
+  Continue processing known types and versions. 
+  Implement graceful handling for unknown schemas. 

 For more information about schema versioning, see [Schema versioning and evolution](telemetry.understanding-data.md#telemetry.understanding-data.schema-evolution). 

## Getting help
<a name="troubleshooting-telemetry.getting-help"></a>

 If you continue to experience issues after following the troubleshooting steps, contact AWS Support. 

 **Information to provide** 

 When contacting support, provide the following information: 
+  Contact IDs experiencing issues 
+  Mission profile ID used 
+  TelemetrySinkConfig ARN 
+  Kinesis Data Streams stream ARN 
+  IAM role ARN and attached policies 
+  Error messages from CloudWatch Logs or your application 
+  Timestamps when issues occurred 
+  Troubleshooting steps already taken 

 For general AWS Ground Station support, see the [AWS Ground Station User Guide](https://docs.aws.amazon.com/ground-station/latest/ug/what-is.html). 