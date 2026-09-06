

# kinesis-video-stream-minimum-data-retention
<a name="kinesis-video-stream-minimum-data-retention"></a>

Checks if an Amazon Kinesis Video stream is configured with a value greater than or equal to the specified minimum data retention. The rule is NON\_COMPLIANT if DataRetentionInHours is less than the value specified in the required rule parameter. 



**Identifier:** KINESIS\_VIDEO\_STREAM\_MINIMUM\_DATA\_RETENTION

**Resource Types:** AWS::KinesisVideo::Stream

**Trigger type:** Configuration changes

**AWS Region:** Only available in Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Europe (Frankfurt), South America (Sao Paulo), Asia Pacific (Hong Kong), US East (N. Virginia), Asia Pacific (Seoul), Europe (London), Asia Pacific (Tokyo), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

minDataRetentionInHoursType: int  
The minimum data retention in hours of the Amazon Kinesis Video stream for the rule to check. The rule is NON\_COMPLIANT if the data retention in hours is less than the value specified in this parameter. Valid values are 0 to 87600.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1049c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).