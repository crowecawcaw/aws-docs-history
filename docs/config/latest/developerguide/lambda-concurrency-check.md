

# lambda-concurrency-check
<a name="lambda-concurrency-check"></a>

Checks if the Lambda function is configured with a function-level concurrent execution limit. The rule is NON\_COMPLIANT if the Lambda function is not configured with a function-level concurrent execution limit. 



**Identifier:** LAMBDA\_CONCURRENCY\_CHECK

**Resource Types:** AWS::Lambda::Function

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except China (Ningxia) Region

**Parameters:**

ConcurrencyLimitHigh (Optional)Type: String  
Maximum concurrency execution limit

ConcurrencyLimitLow (Optional)Type: String  
Minimum concurrency execution limit

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1057c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).