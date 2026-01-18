# Walkthrough: Create a delay

mechanism with a Lambda-backed custom resource

This walkthrough shows you how to configure and launch a Lambda-backed custom resource using
a sample CloudFormation template. This template creates a delay mechanism that pauses stack
deployments for a specified time. This can be useful when you need to introduce deliberate
delays during resource provisioning, such as when waiting for resources to stabilize before
dependent resources are created.

###### Note

While Lambda-backed custom resources were previously recommended for retrieving AMI IDs, we
now recommend using AWS Systems Manager parameters. This approach makes your templates more reusable and
easier to maintain. For more information, see [Get a plaintext value from Systems Manager Parameter
Store](dynamic-references-ssm.md "dynamic-references-ssm.md").

###### Topics

- [Overview](#walkthrough-lambda-backed-custom-resources-overview "#walkthrough-lambda-backed-custom-resources-overview")
- [Sample
  template](#walkthrough-lambda-backed-custom-resources-sample-template "#walkthrough-lambda-backed-custom-resources-sample-template")
- [Sample template walkthrough](#walkthrough-lambda-backed-custom-resources-sample-template-walkthrough "#walkthrough-lambda-backed-custom-resources-sample-template-walkthrough")
- [Prerequisites](#walkthrough-lambda-backed-custom-resources-prerequisites "#walkthrough-lambda-backed-custom-resources-prerequisites")
- [Launching the stack](#walkthrough-lambda-backed-custom-resources-createfunction-createstack "#walkthrough-lambda-backed-custom-resources-createfunction-createstack")
- [Cleaning
  up resources](#walkthrough-lambda-backed-custom-resources-createfunction-cleanup "#walkthrough-lambda-backed-custom-resources-createfunction-cleanup")
- [Related information](#w2aac11c45b9c24b9c23 "#w2aac11c45b9c24b9c23")

## Overview

The sample stack template used in this walkthrough creates a Lambda-backed custom resource.
This custom resource introduces a configurable delay (60 seconds by default) during stack
creation. The delay occurs during stack updates only when the custom resource's properties are
modified.

The template provisions the following resources:

- a custom resource,
- a Lambda function, and
- an IAM role that enables Lambda to write logs to CloudWatch.

It also defines two outputs:

- The actual time the function waited.
- A unique identifier generated during each execution of the Lambda function.

###### Note

CloudFormation is a free service but Lambda charges based on the number of requests for your
functions and the time your code executes. For more information about Lambda pricing, see
[AWS Lambda pricing](https://aws.amazon.com/lambda/pricing/ "https://aws.amazon.com/lambda/pricing/").

## Sample

template

You can see the Lambda-backed custom resource sample template with the delay mechanism
below:

### JSON

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "LambdaExecutionRole": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "AssumeRolePolicyDocument": {
          "Statement": [{
            "Effect": "Allow",
            "Principal": { "Service": ["lambda.amazonaws.com"] },
            "Action": ["sts:AssumeRole"]
          }]
        },
        "Path": "/",
        "Policies": [{
          "PolicyName": "AllowLogs",
          "PolicyDocument": {
            "Statement": [{
              "Effect": "Allow",
              "Action": ["logs:*"],
              "Resource": "*"
            }]
          }
        }]
      }
    },
    "CFNWaiter": {
      "Type": "AWS::Lambda::Function",
      "Properties": {
        "Handler": "index.handler",
        "Runtime": "python3.9",
        "Timeout": 900,
        "Role": { "Fn::GetAtt": ["LambdaExecutionRole", "Arn"] },
        "Code": {
          "ZipFile": { "Fn::Join": ["\n", [
            "from time import sleep",
            "import json",
            "import cfnresponse",
            "import uuid",
            "",
            "def handler(event, context):",
            "  wait_seconds = 0",
            "  id = str(uuid.uuid1())",
            "  if event[\"RequestType\"] in [\"Create\", \"Update\"]:",
            "    wait_seconds = int(event[\"ResourceProperties\"].get(\"ServiceTimeout\", 0))",
            "    sleep(wait_seconds)",
            "  response = {",
            "    \"TimeWaited\": wait_seconds,",
            "    \"Id\": id ",
            "  }",
            "  cfnresponse.send(event, context, cfnresponse.SUCCESS, response, \"Waiter-\"+id)"
          ]]}
        }
      }
    },
    "CFNWaiterCustomResource": {
      "Type": "AWS::CloudFormation::CustomResource",
      "Properties": {
        "ServiceToken": { "Fn::GetAtt": ["CFNWaiter", "Arn"] },
        "ServiceTimeout": 60
      }
    }
  },
  "Outputs": {
    "TimeWaited": {
      "Value": { "Fn::GetAtt": ["CFNWaiterCustomResource", "TimeWaited"] },
      "Export": { "Name": "TimeWaited" }
    },
    "WaiterId": {
      "Value": { "Fn::GetAtt": ["CFNWaiterCustomResource", "Id"] },
      "Export": { "Name": "WaiterId" }
    }
  }
}
```

### YAML

```
AWSTemplateFormatVersion: "2010-09-09"
Resources:
  LambdaExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Statement:
          - Effect: "Allow"
            Principal:
              Service:
                - "lambda.amazonaws.com"
            Action:
              - "sts:AssumeRole"
      Path: "/"
      Policies:
        - PolicyName: "AllowLogs"
          PolicyDocument:
            Statement:
              - Effect: "Allow"
                Action:
                  - "logs:*"
                Resource: "*"
  CFNWaiter:
    Type: AWS::Lambda::Function
    Properties:
      Handler: index.handler
      Runtime: python3.9
      Timeout: 900
      Role: !GetAtt LambdaExecutionRole.Arn
      Code:
        ZipFile:
          !Sub |
          from time import sleep
          import json
          import cfnresponse
          import uuid
​
          def handler(event, context):
            wait_seconds = 0
            id = str(uuid.uuid1())
            if event["RequestType"] in ["Create", "Update"]:
              wait_seconds = int(event["ResourceProperties"].get("ServiceTimeout", 0))
              sleep(wait_seconds)
            response = {
              "TimeWaited": wait_seconds,
              "Id": id
            }
            cfnresponse.send(event, context, cfnresponse.SUCCESS, response, "Waiter-"+id)
  CFNWaiterCustomResource:
    Type: AWS::CloudFormation::CustomResource
    Properties:
      ServiceToken: !GetAtt CFNWaiter.Arn
      ServiceTimeout: 60
Outputs:
  TimeWaited:
    Value: !GetAtt CFNWaiterCustomResource.TimeWaited
    Export:
      Name: TimeWaited
  WaiterId:
    Value: !GetAtt CFNWaiterCustomResource.Id
    Export:
      Name: WaiterId
```

## Sample template walkthrough

The following snippets explain relevant parts of the sample template to help you
understand how the Lambda function is associated with a custom resource and understand the
output.

[AWS::Lambda::Function](../TemplateReference/aws-resource-lambda-function.md "../TemplateReference/aws-resource-lambda-function.md") resource `CFNWaiter`

The `AWS::Lambda::Function` resource specifies the function's source
code, handler name, runtime environment, and execution role Amazon Resource Name
(ARN).

The `Handler` property is set to `index.handler` since it uses
a Python source code. For more information on accepted handler identifiers when using
inline function source codes, see [AWS::Lambda::Function Code](aws-properties-lambda-function-code.md#cfn-lambda-function-code-zipfile "aws-properties-lambda-function-code.md#cfn-lambda-function-code-zipfile").

The `Runtime` is specified as `python3.9` since the source
file is a Python code.

The `Timeout` is set to 900 seconds.

The `Role` property uses the `Fn::GetAtt` function to get the
ARN of the `LambdaExecutionRole` execution role that's declared in the
`AWS::IAM::Role` resource in the template.

The `Code` property defines the function code inline using a Python
function. The Python function in the sample template does the following:

- Create a unique ID using the UUID
- Check if the request is a create or update request
- Sleep for the duration specified for `ServiceTimeout` during
  `Create` or `Update` requests
- Return the wait time and unique ID

### JSON

```
...
    "CFNWaiter": {
      "Type": "AWS::Lambda::Function",
      "Properties": {
        "Handler": "index.handler",
        "Runtime": "python3.9",
        "Timeout": 900,
        "Role": { "Fn::GetAtt": ["LambdaExecutionRole", "Arn"] },
        "Code": {
          "ZipFile": { "Fn::Join": ["\n", [
            "from time import sleep",
            "import json",
            "import cfnresponse",
            "import uuid",
            "",
            "def handler(event, context):",
            "  wait_seconds = 0",
            "  id = str(uuid.uuid1())",
            "  if event[\"RequestType\"] in [\"Create\", \"Update\"]:",
            "    wait_seconds = int(event[\"ResourceProperties\"].get(\"ServiceTimeout\", 0))",
            "    sleep(wait_seconds)",
            "  response = {",
            "    \"TimeWaited\": wait_seconds,",
            "    \"Id\": id ",
            "  }",
            "  cfnresponse.send(event, context, cfnresponse.SUCCESS, response, \"Waiter-\"+id)"
          ]]}
        }
      }
    },
...
```

### YAML

```
...
  CFNWaiter:
    Type: AWS::Lambda::Function
    Properties:
      Handler: index.handler
      Runtime: python3.9
      Timeout: 900
      Role: !GetAtt LambdaExecutionRole.Arn
      Code:
        ZipFile:
          !Sub |
          from time import sleep
          import json
          import cfnresponse
          import uuid
​
          def handler(event, context):
            wait_seconds = 0
            id = str(uuid.uuid1())
            if event["RequestType"] in ["Create", "Update"]:
              wait_seconds = int(event["ResourceProperties"].get("ServiceTimeout", 0))
              sleep(wait_seconds)
            response = {
              "TimeWaited": wait_seconds,
              "Id": id
            }
            cfnresponse.send(event, context, cfnresponse.SUCCESS, response, "Waiter-"+id)
...
```

[AWS::IAM::Role](../TemplateReference/aws-resource-iam-role.md "../TemplateReference/aws-resource-iam-role.md") resource `LambdaExecutionRole`

The `AWS::IAM:Role` resource creates an execution role for the Lambda
function, which includes an assume role policy which allows Lambda to use it. It also
contains a policy allowing CloudWatch Logs access.

### JSON

```
...
    "LambdaExecutionRole": {
      "Type": "AWS::IAM::Role",
      "Properties": {
        "AssumeRolePolicyDocument": {
          "Statement": [{
            "Effect": "Allow",
            "Principal": { "Service": ["lambda.amazonaws.com"] },
            "Action": ["sts:AssumeRole"]
          }]
        },
        "Path": "/",
        "Policies": [{
          "PolicyName": "AllowLogs",
          "PolicyDocument": {
            "Statement": [{
              "Effect": "Allow",
              "Action": ["logs:*"],
              "Resource": "*"
            }]
          }
        }]
      }
    },
...
```

### YAML

```
...
  LambdaExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Statement:
          - Effect: "Allow"
            Principal:
              Service:
                - "lambda.amazonaws.com"
            Action:
              - "sts:AssumeRole"
      Path: "/"
      Policies:
        - PolicyName: "AllowLogs"
          PolicyDocument:
            Statement:
              - Effect: "Allow"
                Action:
                  - "logs:*"
                Resource: "*"
...
```

[AWS::CloudFormation::CustomResource](aws-resource-cloudformation-customresource.md "aws-resource-cloudformation-customresource.md") resource
`CFNWaiterCustomResource`

The custom resource links to the Lambda function with its ARN using `!GetAtt
 CFNWaiter.Arn`. It will implement a 60 second wait time for create and update
operations, as set in `ServiceTimeout`. The resource will only be invoked for an
update operation if the properties are modified.

### JSON

```
...
    "CFNWaiterCustomResource": {
      "Type": "AWS::CloudFormation::CustomResource",
      "Properties": {
        "ServiceToken": { "Fn::GetAtt": ["CFNWaiter", "Arn"] },
        "ServiceTimeout": 60
      }
    }
  },
...
```

### YAML

```
...
  CFNWaiterCustomResource:
    Type: AWS::CloudFormation::CustomResource
    Properties:
      ServiceToken: !GetAtt CFNWaiter.Arn
      ServiceTimeout: 60
...
```

`Outputs`

The `Outputs` of this template are the `TimeWaited` and the
`WaiterId`. The `TimeWaited` value uses a
`Fn::GetAtt` function to provide the amount of time the waiter resource
actually waited. The `WaiterId` uses a `Fn::GetAtt` function to
provide the unique ID that was generated and associated with the execution.

### JSON

```
...
  "Outputs": {
    "TimeWaited": {
      "Value": { "Fn::GetAtt": ["CFNWaiterCustomResource", "TimeWaited"] },
      "Export": { "Name": "TimeWaited" }
    },
    "WaiterId": {
      "Value": { "Fn::GetAtt": ["CFNWaiterCustomResource", "Id"] },
      "Export": { "Name": "WaiterId" }
    }
  }
}
...
```

### YAML

```
...
Outputs:
  TimeWaited:
    Value: !GetAtt CFNWaiterCustomResource.TimeWaited
    Export:
      Name: TimeWaited
  WaiterId:
    Value: !GetAtt CFNWaiterCustomResource.Id
    Export:
      Name: WaiterId
...
```

## Prerequisites

You must have IAM permissions to use all the corresponding services, such as Lambda and
CloudFormation.

## Launching the stack

###### To create the stack

1. Find the template of your preference (YAML or JSON) from the [Sample
   template](#walkthrough-lambda-backed-custom-resources-sample-template "#walkthrough-lambda-backed-custom-resources-sample-template") section and
   save it to your machine with the name
   `samplelambdabackedcustomresource.template`.
2. Open the CloudFormation console at [https://console.aws.amazon.com/cloudformation/](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
3. From the **Stacks** page, choose **Create stack** at
   top right, and then choose **With new resources (standard)**.
4. For **Prerequisite - Prepare template**, choose **Choose an
   existing template**.
5. For **Specify template**, choose **Upload a template
   file**, and then choose **Choose file**.
6. Select the `samplelambdabackedcustomresource.template` template file you
   saved earlier.
7. Choose **Next**.
8. For **Stack name**, type
   `SampleCustomResourceStack` and choose
   **Next**.
9. For this walkthrough, you don't need to add tags or specify advanced settings, so
   choose **Next**.
10. Ensure that the stack name looks correct, and then choose
    **Create**.

It might take several minutes for CloudFormation to create your stack. To monitor progress,
view the stack events. For more information, see [View stack information from the
CloudFormation console](cfn-console-view-stack-data-resources.md "cfn-console-view-stack-data-resources.md").

If stack creation succeeds, all resources in the stack, such as the Lambda function and
custom resource, were created. You have successfully used a Lambda function and custom
resource.

If the Lambda function returns an error, view the function's logs in the CloudWatch Logs [console](https://console.aws.amazon.com/cloudwatch/home#logs: "https://console.aws.amazon.com/cloudwatch/home#logs:"). The name of the log stream is
the physical ID of the custom resource, which you can find by viewing the stack's resources.
For more information, see [View log data](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#ViewingLogData "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#ViewingLogData") in the _Amazon CloudWatch User Guide_.

## Cleaning

up resources

Delete the stack to clean up all the stack resources that you created so that you aren't
charged for unnecessary resources.

###### To delete the stack

1. From the CloudFormation console, choose the **SampleCustomResourceStack**
   stack.
2. Choose **Actions** and then **Delete Stack**.
3. In the confirmation message, choose **Yes, Delete**.

All the resources that you created are deleted.

Now that you understand how to create and use Lambda-backed custom resource, you can use
the sample template and code from this walkthrough to build and experiment with other stacks
and functions.

## Related information

- [CloudFormation Custom Resource Reference](crpg-ref.md "crpg-ref.md")
- [AWS::CloudFormation::CustomResource](aws-resource-cloudformation-customresource.md "aws-resource-cloudformation-customresource.md")
