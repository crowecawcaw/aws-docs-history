

# sagemaker-monitoring-schedule-isolation
<a name="sagemaker-monitoring-schedule-isolation"></a>

Checks if Amazon SageMaker monitoring schedules have network isolation enabled. The rule is NON\_COMPLIANT if configuration.MonitoringScheduleConfig.MonitoringJobDefinition.NetworkConfig.EnableNetworkIsolation is false. 



**Identifier:** SAGEMAKER\_MONITORING\_SCHEDULE\_ISOLATION

**Resource Types:** AWS::SageMaker::MonitoringSchedule

**Trigger type:** Configuration changes

**AWS Region:** Only available in Europe (Stockholm), Middle East (Bahrain), Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Europe (Ireland), Europe (Frankfurt), South America (Sao Paulo), Asia Pacific (Hong Kong), US East (N. Virginia), Asia Pacific (Seoul), Asia Pacific (Osaka), Europe (London), Asia Pacific (Tokyo), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1489c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).