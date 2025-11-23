# CloudFormation Ingest examples: Defining resources

When using AMS CloudFormation ingest, you customize a CloudFormation template and submit it to AMS in an RFC with the CloudFormation ingest change type (ct-36cn2avfrrj9v).
To create a CloudFormation template that can be reused multiple times, you add the stack configuration parameters to the CloudFormation ingest change type execution
input rather than hard coding them in the CloudFormation template. The biggest benefit is that you can reuse the template.

The AMS CloudFormation ingest change type input schema enables you to choose up to sixty parameters in a CloudFormation template and provide custom values.

This example shows how to define a resource property, which can be used in a variety of
CloudFormation templates, as a parameter in the AMS CloudFormation ingest CT. The examples in this section specifically show SNS topic usage.

###### Topics

- [Example 1: Hard code the CloudFormation SNSTopic resource TopicName property](#cfn-ingest-example-1 "#cfn-ingest-example-1")
- [Example 2: Use an SNSTopic resource to reference a parameter in the AMS change type](#cfn-ingest-example-2 "#cfn-ingest-example-2")
- [Example 3: Create an SNS topic by submitting a JSON execution parameters file with the AMS ingest change type](#cfn-ingest-example-3 "#cfn-ingest-example-3")
- [Example 4: Submit a new change type that references the same CloudFormation template](#cfn-ingest-example-4 "#cfn-ingest-example-4")
- [Example 5: Use the default parameter values in the CloudFormation template](#cfn-ingest-example-5 "#cfn-ingest-example-5")

## Example 1: Hard code the CloudFormation SNSTopic resource `TopicName` property

In this example, you hard code the CloudFormation SNSTopic resource `TopicName` property in the CloudFormation template. Note that the `Parameters`
section is empty.

To have a CloudFormation template that allows you to change the value for the SNSTopic name for a new stack without having to create a new CloudFormation template,
you can use the AMS `Parameters` section of the CloudFormation ingest change type to make that
configuration. By doing this, you use the same CloudFormation template later to create a new stack with a different `SNSTopic` name.

```
{
  "AWSTemplateFormatVersion" : "2010-09-09",
  "Description" : "My SNS Topic",
  "Parameters" : {
  },
  "Resources" : {
    "SNSTopic" : {
      "Type" : "AWS::SNS::Topic",
      "Properties" : {
        "TopicName" : "MyTopicName"
      }
    }
  }
}
```

## Example 2: Use an SNSTopic resource to reference a parameter in the AMS change type

In this example, you use an `SNSTopic` resource `TopicName` property defined in the CloudFormation template to reference a `Parameter` in the
AMS change type.

```
{
  "AWSTemplateFormatVersion" : "2010-09-09",
  "Description" : "My SNS Topic",
  "Parameters" : {
    "TopicName" : {
      "Type" : "String",
      "Description" : "Topic ID",
      "Default" : "MyTopicName"
    }
  },
  "Resources" : {
    "SNSTopic" : {
      "Type" : "AWS::SNS::Topic",
      "Properties" : {
        "TopicName" : { "Ref" : "TopicName"}
      }
    }
  }
}
```

## Example 3: Create an SNS topic by submitting a JSON execution parameters file with the AMS ingest change type

In this example, you submit a JSON execution parameters file with the AMS ingest CT that creates the SNS topic `TopicName`. The SNS topic must be defined in the
CloudFormation template in the modifiable way shown in this example.

```
{
  "Name": "cfn-ingest",
  "Description": "CFNIngest Web Application Stack",
  "CloudFormationTemplateS3Endpoint": "`$S3_PRESIGNED_URL`",
  "VpcId": "`VPC_ID`",
  "Tags": [
    {"Key": "Enviroment Type", "Value": "Dev"}
  ],
  "Parameters": [
    {"Name": "TopicName", "Value": "MyTopic1"}
  ],
  "TimeoutInMinutes": 60
}
```

## Example 4: Submit a new change type that references the same CloudFormation template

This JSON example changes the SNS `TopicName` value without making a change to the CloudFormation template. Instead, you submit a new
Deployment | Ingestion | Stack from CloudFormation Template | Create change type that references the same CFN template.

```
{
  "Name": "cfn-ingest",
  "Description": "CFNIngest Web Application Stack",
  "CloudFormationTemplateS3Endpoint": "`$S3_PRESIGNED_URL`",
  "VpcId": "`VPC_ID`",
  "Tags": [
    {"Key": "Enviroment Type", "Value": "Dev"}
  ],
  "Parameters": [
    {"Name": "TopicName", "Value": "MyTopic2"}
  ],
  "TimeoutInMinutes": 60
}
```

## Example 5: Use the default parameter values in the CloudFormation template

In this example, the SNS `TopicName` = 'MyTopicName' is created because no `TopicName` value was provided in the
`Parameters` execution parameter. If you don't provide `Parameters` definitions, the default parameter values in the CloudFormation template are used.

```
{
  "Name": "cfn-ingest",
  "Description": "CFNIngest Web Application Stack",
  "CloudFormationTemplateS3Endpoint": "`$S3_PRESIGNED_URL`",
  "VpcId": "`VPC_ID`",
  "Tags": [
    {"Key": "Enviroment Type", "Value": "Dev"}
  ],
  "TimeoutInMinutes": 60
}
```
