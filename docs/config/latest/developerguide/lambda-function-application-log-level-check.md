

# lambda-function-application-log-level-check
<a name="lambda-function-application-log-level-check"></a>

Checks if AWS Lambda functions with JSON structured logs are configured with a specified application log level. The rule is NON\_COMPLIANT if configuration.loggingConfig.applicationLogLevel is not a value specified in the required rule parameter. 



**Identifier:** LAMBDA\_FUNCTION\_APPLICATION\_LOG\_LEVEL\_CHECK

**Resource Types:** AWS::Lambda::Function

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Ningxia) Region

**Parameters:**

logLevelType: String  
The minimum application log level for the rule to check. The rule is NON\_COMPLIANT if configuration.loggingConfig.applicationLogLevel is configured with a value not specified in this parameter. Valid values include: 'TRACE', 'DEBUG', 'INFO', 'WARN', 'ERROR', and 'FATAL'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1061c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).