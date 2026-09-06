

# redshift-serverless-publish-logs-to-cloudwatch
<a name="redshift-serverless-publish-logs-to-cloudwatch"></a>

Checks if Amazon Redshift Serverless Namespace is configured to publish the following logs to Amazon CloudWatch Logs. This rule is NON\_COMPLIANT if the Namespace is not configured to publish the following logs to Amazon CloudWatch Logs. 



**Identifier:** REDSHIFT\_SERVERLESS\_PUBLISH\_LOGS\_TO\_CLOUDWATCH

**Resource Types:** AWS::RedshiftServerless::Namespace

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Middle East (Bahrain), Africa (Cape Town), Asia Pacific (Hyderabad), Asia Pacific (Osaka), Asia Pacific (Melbourne), Europe (Milan), AWS GovCloud (US-East), AWS GovCloud (US-West), Canada West (Calgary) Region

**Parameters:**

logType (Optional)Type: CSV  
Comma-separated list of log types to be published to CloudWatch Logs. Valid values are 'connectionlog', 'userlog' Default value is 'connectionlog', 'userlog'. 

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1323c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).