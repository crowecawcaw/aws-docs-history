

# lambda-function-log-format-json
<a name="lambda-function-log-format-json"></a>

Checks if AWS Lambda functions have the log format set to JSON for more control and better readability. The rule is NON\_COMPLIANT if configuration.loggingConfig.logFormat is not 'JSON'. 



**Identifier:** LAMBDA\_FUNCTION\_LOG\_FORMAT\_JSON

**Resource Types:** AWS::Lambda::Function

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), AWS GovCloud (US-East), AWS GovCloud (US-West), China (Ningxia) Region

**Parameters:**

None  

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1065c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).