

# ProvisionedThroughputObject
<a name="sam-property-simpletable-provisionedthroughputobject"></a>

The object describing the properties of a provisioned throughput.

## Syntax
<a name="sam-property-simpletable-provisionedthroughputobject-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="w2aac13c22c53c19b5b5"></a>

```
  [ReadCapacityUnits](#sam-simpletable-provisionedthroughputobject-readcapacityunits): {{Integer}}
  [WriteCapacityUnits](#sam-simpletable-provisionedthroughputobject-writecapacityunits): {{Integer}}
```

## Properties
<a name="sam-property-simpletable-provisionedthroughputobject-properties"></a>

 `ReadCapacityUnits`   <a name="sam-simpletable-provisionedthroughputobject-readcapacityunits"></a>
The maximum number of strongly consistent reads consumed per second before DynamoDB returns a `ThrottlingException`.  
*Type*: Integer  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[ReadCapacityUnits](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-provisionedthroughput.html#aws-properties-dynamodb-table-provisionedthroughput-properties)` property of the `AWS::DynamoDB::Table` `ProvisionedThroughput` data type.

 `WriteCapacityUnits`   <a name="sam-simpletable-provisionedthroughputobject-writecapacityunits"></a>
The maximum number of writes consumed per second before DynamoDB returns a `ThrottlingException`.  
*Type*: Integer  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[WriteCapacityUnits](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-provisionedthroughput.html#aws-properties-dynamodb-table-provisionedthroughput-properties)` property of the `AWS::DynamoDB::Table` `ProvisionedThroughput` data type.

## Examples
<a name="sam-property-simpletable-provisionedthroughputobject--examples"></a>

### ProvisionedThroughput
<a name="sam-property-simpletable-provisionedthroughputobject--examples--provisionedthroughput"></a>

Provisioned throughput example.

#### YAML
<a name="sam-property-simpletable-provisionedthroughputobject--examples--provisionedthroughput--yaml"></a>

```
Properties:
   ProvisionedThroughput:
     ReadCapacityUnits: {{5}}
     WriteCapacityUnits: {{5}}
```