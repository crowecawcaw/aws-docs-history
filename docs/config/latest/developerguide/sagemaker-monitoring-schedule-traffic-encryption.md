

# sagemaker-monitoring-schedule-traffic-encryption
<a name="sagemaker-monitoring-schedule-traffic-encryption"></a>

Checks if SageMaker monitoring schedules have inter-container traffic encryption enabled. The rule is NON\_COMPLIANT if MonitoringJobDefinition exists and does not have NetworkConfig defined, or EnableInterContainerTrafficEncryption is not set to true. 



**Identifier:** SAGEMAKER\_MONITORING\_SCHEDULE\_TRAFFIC\_ENCRYPTION

**Resource Types:** AWS::SageMaker::MonitoringSchedule

**Trigger type:** Configuration changes

**AWS Region:** Only available in Europe (Stockholm), China (Beijing), Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Europe (Frankfurt), South America (Sao Paulo), Asia Pacific (Hong Kong), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Asia Pacific (Tokyo), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central), China (Ningxia) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1491c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).