

# DurableConfig
<a name="sam-property-function-durableconfig"></a>

Configures durable execution settings for AWS Lambda functions. Durable functions can run for up to one year and automatically checkpoint progress, enabling long-running workflows and fault-tolerant applications. For more information about durable functions, see [Lambda durable functions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html) in the *AWS Lambda Developer Guide*.

## Syntax
<a name="sam-property-function-durableconfig-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-function-durableconfig-syntax.yaml"></a>

```
  [ExecutionTimeout](#sam-function-durableconfig-executiontimeout): {{Integer}}
  [RetentionPeriodInDays](#sam-function-durableconfig-retentionperiodindays): {{Integer}}
```

## Properties
<a name="sam-property-function-durableconfig-properties"></a>

 `ExecutionTimeout`   <a name="sam-function-durableconfig-executiontimeout"></a>
The amount of time (in seconds) that Lambda allows a durable function to run before stopping it. The maximum is one 366-day year or 31,622,400 seconds.  
*Type*: Integer  
*Required*: Yes  
*Minimum*: 1  
*Maximum*: 31622400  
*CloudFormation compatibility*: This property is passed directly to the `[ExecutionTimeout](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-durableconfig.html#cfn-lambda-function-durableconfig-executiontimeout)` property of the `AWS::Lambda::Function` `DurableConfig` data type.

 `RetentionPeriodInDays`   <a name="sam-function-durableconfig-retentionperiodindays"></a>
The number of days after a durable execution is closed that Lambda retains its history, from one to 90 days. The default is 14 days.  
*Type*: Integer  
*Required*: No  
*Default*: 14  
*Minimum*: 1  
*Maximum*: 90  
*CloudFormation compatibility*: This property is passed directly to the `[RetentionPeriodInDays](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-durableconfig.html#cfn-lambda-function-durableconfig-retentionperiodindays)` property of the `AWS::Lambda::Function` `DurableConfig` data type.

## Examples
<a name="sam-property-function-durableconfig--examples"></a>

### DurableConfig
<a name="sam-property-function-durableconfig--examples--durableconfig"></a>

Durable configuration example for a function with a 1-hour execution timeout and 7-day retention period.

#### YAML
<a name="sam-property-function-durableconfig--examples--durableconfig--yaml"></a>

```
DurableConfig:
  ExecutionTimeout: 3600
  RetentionPeriodInDays: 7
```