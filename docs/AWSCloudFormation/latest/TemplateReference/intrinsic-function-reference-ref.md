This is the new _AWS CloudFormation Template Reference Guide_.
Please update your bookmarks and links. For help getting started with CloudFormation, see the
[AWS CloudFormation User Guide](../UserGuide/Welcome.md "../UserGuide/Welcome.md").

# `Ref`

The intrinsic function `Ref` returns the value of a specified parameter,
resource, or another intrinsic function. This function is commonly used to create references
between resources within a CloudFormation template.

## Declaration

### JSON

```
{ "Ref" : "`logicalName`" }
```

```
{ "Ref" : "`IntrinsicFunction`" }
```

### YAML

Syntax for the full function name:

```
Ref: `logicalName`
```

```
Ref:
   `IntrinsicFunction`
```

Syntax for the short form:

```
!Ref `logicalName`
```

```
!Ref
   `IntrinsicFunction`
```

## Parameters

logicalName

The logical name of the resource or parameter you want to
reference.

IntrinsicFunction

The intrinsic function that resolves to a valid string. It should contain
references to parameters or identifiers, and should not contain resource
logical identifiers.

## Return value

The return value of `Ref` depends on the type of entity being
referenced:

- When you specify a parameter's logical name, it returns the value of the
  parameter. For more information, see [CloudFormation template
  Parameters syntax](../UserGuide/parameters-section-structure.md "../UserGuide/parameters-section-structure.md").
- When you specify a resource's logical name, it returns a value that you use to
  identify that resource. Usually, that's the name of the resource. However, for
  some resources, an identifier is returned that has another significant meaning
  in the context of the resource. For example, the `AWS::EC2::EIP`
  resource returns the IP address, and the `AWS::EC2::Instance` returns
  the instance ID. For more information about `Ref` return values for a
  resource, see the documentation for that resource in the [Resource and property reference](aws-template-resource-type-ref.md "aws-template-resource-type-ref.md").
- When you specify an intrinsic function, it returns the output of that
  function.

## Examples

### Create references between

resources

The following resource declaration for an Elastic IP address needs the instance ID
of an EC2 instance. It uses the `Ref` function to specify the instance ID
of the `MyEC2Instance` resource declared elsewhere in the
template.

#### JSON

```
{
  "AWSTemplateFormatVersion":"2010-09-09",
  "Resources":{

      `...`

    "MyEIP":{
      "Type":"AWS::EC2::EIP",
      "Properties":{
        "InstanceId":{
          "Ref":"MyEC2Instance"
        }
      }
    }
  }
}
```

#### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Resources:

  `...`

  MyEIP:
    Type: AWS::EC2::EIP
    Properties:
      InstanceId: !Ref MyEC2Instance
```

### Return a resource

identifier as stack output

The following examples show how to use the `Ref` function to return the
name of an Amazon S3 bucket with the logical name `MyBucket` as stack output.

#### JSON

```
{
  "AWSTemplateFormatVersion":"2010-09-09",
  "Resources":{
    "MyBucket":{
      "Type":"AWS::S3::Bucket",
      "Properties":{
        "BucketName":{
          "Fn::Sub": "${AWS::StackName}-mybucket"
        }
      }
    }
  },
  "Outputs":{
    "BucketNameOutput":{
      "Description":"The name of the S3 bucket",
      "Value":{
        "Ref":"MyBucket"
      }
    }
  }
}
```

#### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  MyBucket:
    Type: AWS::S3::Bucket
    Properties:
      BucketName: !Sub ${AWS::StackName}-mybucket

Outputs:
  BucketNameOutput:
    Description: The name of the S3 bucket
    Value: !Ref MyBucket
```

### Use

`Fn::Join` intrinsic function inside `Ref`
function

###### Note

When you use the `AWS::LanguageExtensions` transform, you can use
`Ref` in combination with other intrinsic functions. For
supported functions, see [Supported functions](#ref-supported-functions "#ref-supported-functions").

The following examples show how to set identifiers of resources using the
`Fn::Sub` intrinsic function, conditions, and the input for the
`Stage` parameter. The `Ref` and the
`Fn::GetAtt` functions then reference the appropriate values, based
on the stage. `Fn::Sub` is first used with `Fn::GetAtt` to
obtain the ARN of the appropriate Amazon SQS queue to set the dimensions of the Amazon CloudWatch
alarm. Next, [Fn::Join](intrinsic-function-reference-join.md "intrinsic-function-reference-join.md") is used with `Ref` to
create the name of the SNS topic for the `AlarmActions` property.

#### JSON

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Transform": "AWS::LanguageExtensions",
    "Parameters": {
        "Stage": {
            "Type": "String",
            "Default": "Dev",
            "AllowedValues": [
                "Dev",
                "Prod"
            ]
        }
    },
    "Conditions": {
        "isProd": {
            "Fn::Equals": [
                {"Ref": "Stage"},
                "Prod"
            ]
        },
        "isDev": {
            "Fn::Equals": [
                {"Ref": "Stage"},
                "Dev"
            ]
        }
    },
    "Resources": {
        "DevQueue": {
            "Type": "AWS::SQS::Queue",
            "Condition": "isDev",
            "Properties": {
                "QueueName": {"Fn::Sub": "My${Stage}Queue"}
            }
        },
        "ProdQueue": {
            "Type": "AWS::SQS::Queue",
            "Condition": "isProd",
            "Properties": {
                "QueueName": {"Fn::Sub": "My${Stage}Queue"}
            }
        },
        "DevTopic": {
            "Condition": "isDev",
            "Type": "AWS::SNS::Topic"
        },
        "ProdTopic": {
            "Condition": "isProd",
            "Type": "AWS::SNS::Topic"
        },
        "MyAlarm": {
            "Type": "AWS::CloudWatch::Alarm",
            "Properties": {
                "AlarmDescription": "Alarm if queue depth grows beyond 10 messages",
                "Namespace": "AWS/SQS",
                "MetricName": "ApproximateNumberOfMessagesVisible",
                "Dimensions":[
                    {
                        "Name": {"Fn::Sub": "${Stage}Queue"},
                        "Value": {"Fn::GetAtt": [{"Fn::Sub": "${Stage}Queue"}, "QueueName"]}
                    }
                ],
                "Statistic": "Sum",
                "Period": 300,
                "EvaluationPeriods": 1,
                "Threshold": 10,
                "ComparisonOperator": "GreaterThanThreshold",
                "AlarmActions": [
                    {
                        "Ref": {"Fn::Join": ["", [{"Ref": "Stage"}, "Topic"]]}
                    }
                ]
            }
        }
    }
}
```

#### YAML

```
AWSTemplateFormatVersion: 2010-09-09
Transform: AWS::LanguageExtensions
Parameters:
  Stage:
    Type: String
    Default: Dev
    AllowedValues:
      - Dev
      - Prod
Conditions:
  isProd: !Equals
    - !Ref Stage
    - Prod
  isDev: !Equals
    - !Ref Stage
    - Dev
Resources:
  DevQueue:
    Type: AWS::SQS::Queue
    Condition: isDev
    Properties:
      QueueName: !Sub My${Stage}Queue
  ProdQueu:
    Type: AWS::SQS::Queue
    Condition: isProd
    Properties:
      QueueName: !Sub My${Stage}Queue
  DevTopic:
    Condition: isDev
    Type: AWS::SNS::Topic
  ProdTopic:
    Condition: isProd
    Type: AWS::SNS::Topic
  MyAlarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      AlarmDescription: Alarm if queue depth grows beyond 10 messages
      Namespace: AWS/SQS
      MetricName: ApproximateNumberOfMessagesVisible
      Dimensions:
        - Name: !Sub '${Stage}Queue'
          Value: !GetAtt
            - !Sub '${Stage}Queue'
            - QueueName
      Statistic: Sum
      Period: 300
      EvaluationPeriods: 1
      Threshold: 10
      ComparisonOperator: GreaterThanThreshold
      AlarmActions:
        - !Ref
          'Fn::Join':
            - ''
            - - !Ref Stage
              - Topic
```

## Supported functions

When you use the [AWS::LanguageExtensions transform](transform-aws-languageextensions.md "transform-aws-languageextensions.md"), you can use the
following functions within the `Ref` function.

- [Fn::Base64](intrinsic-function-reference-base64.md "intrinsic-function-reference-base64.md")
- [Fn::FindInMap](intrinsic-function-reference-findinmap.md "intrinsic-function-reference-findinmap.md")
- [Fn::If](intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-if "intrinsic-function-reference-conditions.md#intrinsic-function-reference-conditions-if")
- [Fn::ImportValue](intrinsic-function-reference-importvalue.md "intrinsic-function-reference-importvalue.md")
- [Fn::Join](intrinsic-function-reference-join.md "intrinsic-function-reference-join.md")
- [Fn::Sub](intrinsic-function-reference-sub.md "intrinsic-function-reference-sub.md")
- [Fn::ToJsonString](intrinsic-function-reference-ToJsonString.md "intrinsic-function-reference-ToJsonString.md")
- `Ref`
