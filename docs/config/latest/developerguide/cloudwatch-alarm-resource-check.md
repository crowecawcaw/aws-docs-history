

# cloudwatch-alarm-resource-check
<a name="cloudwatch-alarm-resource-check"></a>

Checks if a resource type has a CloudWatch alarm for the named metric. For resource type, you can specify EBS volumes, EC2 instances, Amazon RDS clusters, or S3 buckets. The rule is COMPLIANT if the named metric has a resource ID and CloudWatch alarm. 



**Identifier:** CLOUDWATCH\_ALARM\_RESOURCE\_CHECK

**Resource Types:** AWS::EC2::Instance, AWS::RDS::DBCluster, AWS::S3::Bucket, AWS::EC2::Volume

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions

**Parameters:**

resourceTypeType: String  
AWS resource type. The value can be one of the following: AWS::EC2::Volume, AWS::EC2::Instance, AWS::RDS::DBCluster, or AWS::S3::Bucket.

metricNameType: String  
The name for the metric associated with the alarm (for example, 'CPUUtilization' for EC2 instances).

## AWS CloudFormation template
<a name="w2aac20c16c17b7d353c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).