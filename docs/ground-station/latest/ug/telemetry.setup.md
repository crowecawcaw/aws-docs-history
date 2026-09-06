

# Set up telemetry
<a name="telemetry.setup"></a>

 Follow these steps to configure telemetry for your AWS Ground Station contacts. After completing this setup, telemetry data will be delivered to your Kinesis Data Streams stream during contacts that use a telemetry-enabled mission profile. For an in-depth understanding of Kinesis Data Streams please refer to the [Kinesis Data Streams User Guide](https://docs.aws.amazon.com/streams/latest/dev/introduction.html). 

## Step 1: Create prerequisite AWS resources
<a name="telemetry.setup.step1"></a>

 The following CloudFormation snippet demonstrates how to create the prerequisite AWS resources for telemetry delivery. This snippet creates a Kinesis Data Streams stream and an IAM role that grants AWS Ground Station permission to write telemetry data to the stream. 

```
{{TelemetryStream}}:
  Type: AWS::Kinesis::Stream
  Properties:
    Name: {{GroundStationTelemetryStream}}
    StreamModeDetails:
      StreamMode: {{ON_DEMAND}}
    RetentionPeriodHours: {{24}}

{{TelemetryRole}}:
  Type: AWS::IAM::Role
  Properties:
    RoleName: {{GroundStationTelemetryRole}}
    AssumeRolePolicyDocument:
      Version: '2012-10-17'
      Statement:
        - Effect: Allow
          Principal:
            Service: groundstation.amazonaws.com
          Action: sts:AssumeRole
    Policies:
      - PolicyName: {{KinesisWritePolicy}}
        PolicyDocument:
          Version: '2012-10-17'
          Statement:
            - Effect: Allow
              Action:
                - kinesis:DescribeStream
                - kinesis:PutRecord
                - kinesis:PutRecords
              Resource: !GetAtt {{TelemetryStream}}.Arn
```

 The below list calls out unique setup considerations when configuring telemetry delivery for AWS Ground Station. 

 **Kinesis Data Streams stream** - The stream uses on-demand capacity mode, which automatically scales based on throughput. This is recommended for most use cases. The stream is configured to retain data for 24 hours. By default, the stream uses AWS managed encryption. To use customer-managed encryption with AWS Key Management Service, add the `StreamEncryption` property and update the IAM role policy to include `kms:GenerateDataKey` permission. For more information, see [ Data Protection in Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/server-side-encryption.html). 

 **IAM Role** - The IAM role allows the `groundstation.amazonaws.com` service principal to assume the role and write telemetry data to your Kinesis Data Streams stream. The role policy grants permissions for `kinesis:DescribeStream`, `kinesis:PutRecord`, and `kinesis:PutRecords` actions on the stream. See [Telemetry Sink Config](how-it-works.config.md#how-it-works.config-telemetry-sink) for guidance on setting up the trust policy and role policy. 

 **Additional configuration** - Add `iam:PassRole` permissions to the IAM user or role you use for AWS Ground Station API calls. This allows you to pass the telemetry role to AWS Ground Station when creating a TelemetrySinkConfig. 

### Example PassRole Policy
<a name="telemetry-passrole-policy-example"></a>

 For more information on how to update or attach a role policy, see [ Managing IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage.html) in the IAM User Guide. For more information on the `iam:PassRole` permission, see [ Grant a user permissions to pass a role to an AWS service ](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html) 

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
      "Resource": "arn:aws:iam::{{999999999999}}:role/{{your-telemetry-delivery-role-name}}"
    }
  ]
}
```

## Step 2: Create a TelemetrySinkConfig
<a name="telemetry.setup.step2"></a>

 Create a *TelemetrySinkConfig* that defines how AWS Ground Station will deliver telemetry data to your Kinesis Data Streams stream. Use the stream ARN and role ARN from the CloudFormation stack outputs in Step 1. 

**Note**  
 When you create a *TelemetrySinkConfig*, AWS Ground Station will verify access to your Kinesis Data Streams stream by delivering an empty test record with a partition key of `test`. 

 For more information about creating a *TelemetrySinkConfig*, see [Telemetry Sink Config](how-it-works.config.md#how-it-works.config-telemetry-sink). 

## Step 3: Add telemetry to your mission profile
<a name="telemetry.setup.step3"></a>

 Create a mission profile. For more information about creating mission profiles, see [Use AWS Ground Station Mission Profiles](how-it-works-mission-profile.md). Add the `telemetrySinkConfigArn` to your mission profile to enable telemetry delivery during contacts. Use the ARN of the *TelemetrySinkConfig* created in Step 2. 

## Step 4: Schedule a contact
<a name="telemetry.setup.step4"></a>

 Schedule a contact using your telemetry-enabled mission profile. During the contact, AWS Ground Station will stream telemetry data to your Kinesis Data Streams stream. 

 **What to expect during contacts** 
+  **Telemetry start** - Data begins streaming as the contact starts. 
+  **Near real-time delivery** - Telemetry arrives in your Kinesis Data Streams stream in near real-time. 
+  **Contact duration** - Data continues throughout the entire contact. 
+  **Automatic stop** - Telemetry stops streaming when the contact ends. 

 **Monitoring delivery** 

 You can monitor telemetry delivery using: 
+  **Kinesis Data Streams stream metrics** - Check incoming records in CloudWatch. For more information, see [ Monitoring Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/monitoring-with-cloudwatch.html). 
+  **Application logs** - Verify data processing in your applications that consume from the stream. 
+  **Kinesis Data Viewer** - Use the Kinesis Data Streams stream console to view sample records from your stream. 

## Next steps
<a name="telemetry.setup.next-steps"></a>

 After completing the setup, you can: 
+  Learn about the telemetry data format and available telemetry types. See [Understand telemetry data](telemetry.understanding-data.md). 
+  Build applications to process telemetry data from your Kinesis Data Streams stream. For more information, see [ Building Consumers for Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/building-consumers.html). 
+  Create dashboards and alerts using CloudWatch and other AWS services. 
+  Review troubleshooting guidance if you encounter issues. See [Troubleshoot telemetry](troubleshooting-telemetry.md). 