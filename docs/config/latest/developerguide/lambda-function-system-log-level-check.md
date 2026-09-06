

# lambda-function-system-log-level-check
<a name="lambda-function-system-log-level-check"></a>

Checks if AWS Lambda functions with JSON structured logs are configured with a specified system log level. The rule is NON\_COMPLIANT if configuration.loggingConfig.systemLogLevel is not a value specified in the required rule parameter. 



**Identifier:** LAMBDA\_FUNCTION\_SYSTEM\_LOG\_LEVEL\_CHECK

**Resource Types:** AWS::Lambda::Function

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Ningxia) Region

**Parameters:**

logLevelType: String  
The minimum system log level for the rule to check. The rule is NON\_COMPLIANT if configuration.loggingConfig.systemLogLevel is configured with a value not specified in this parameter. Valid values include: 'DEBUG', 'INFO', and 'WARN'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1071c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).