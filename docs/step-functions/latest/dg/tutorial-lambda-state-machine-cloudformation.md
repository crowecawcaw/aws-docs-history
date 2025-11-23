# Using CloudFormation to create a workflow in Step Functions

In this tutorial, you will create a AWS Lambda function using AWS CloudFormation. You'll use
the CloudFormation console and a YAML template to create a _stack_ (IAM
roles, the Lambda function, and the state machine). Then, you'll use the Step Functions console to
start the state machine execution.

For more information, see [Working with
CloudFormation Templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md") and the `AWS::StepFunctions::StateMachine` resource in the
_AWS CloudFormation User Guide_.

## Step 1: Set up your CloudFormation template

Before you use the [example
templates](#lambda-state-machine-cfn-step-2 "#lambda-state-machine-cfn-step-2"), you should understand how to declare the different parts of an CloudFormation
template.

### To create an IAM

role for Lambda

Define the trust policy associated with the IAM role for the Lambda function. The
following examples define a trust policy using either YAML or JSON.

YAML

```
LambdaExecutionRole:
    Type: "AWS::IAM::Role"
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: Allow
            Principal:
              Service: lambda.amazonaws.com
            Action: "sts:AssumeRole"
```

JSON

```
          "LambdaExecutionRole": {
              "Type": "AWS::IAM::Role",
              "Properties": {
                  "AssumeRolePolicyDocument": {
                      "Version": "2012-10-17",
                      "Statement": [
                          {
                              "Effect": "Allow",
                              "Principal": {
                                  "Service": "lambda.amazonaws.com"
                              },
                              "Action": "sts:AssumeRole"
                          }
                      ]
                  }
              }
```

### To create a Lambda

function

Define the following properties for a Lambda function that will print the message
`Hello World`.

###### Important

Ensure that your Lambda function is under the same AWS account and AWS Region as your state machine.

YAML

```
MyLambdaFunction:
    Type: "AWS::Lambda::Function"
    Properties:
      Handler: "index.handler"
      Role: !GetAtt [ LambdaExecutionRole, Arn ]
      Code:
        ZipFile: |
          exports.handler = (event, context, callback) => {
              callback(null, "Hello World!");
          };
      Runtime: "nodejs12.x"
      Timeout: "25"
```

JSON

```
        "MyLambdaFunction": {
              "Type": "AWS::Lambda::Function",
              "Properties": {
                  "Handler": "index.handler",
                  "Role": {
                      "Fn::GetAtt": [
                          "LambdaExecutionRole",
                          "Arn"
                      ]
                  },
                  "Code": {
                      "ZipFile": "exports.handler = (event, context, callback) => {\n    callback(null, \"Hello World!\");\n};\n"
                  },
                  "Runtime": "nodejs12.x",
                  "Timeout": "25"
              }
          },
```

### To create an IAM role for the

state machine execution

Define the trust policy associated with the IAM role for the state machine
execution.

YAML

```
StatesExecutionRole:
    Type: "AWS::IAM::Role"
    Properties:
      AssumeRolePolicyDocument:
        Version: "2012-10-17"
        Statement:
          - Effect: "Allow"
            Principal:
              Service:
                - !Sub states.${AWS::Region}.amazonaws.com
            Action: "sts:AssumeRole"
      Path: "/"
      Policies:
        - PolicyName: StatesExecutionPolicy
          PolicyDocument:
            Version: "2012-10-17"
            Statement:
              - Effect: Allow
                Action:
                  - "lambda:InvokeFunction"
                Resource: "*"
```

JSON

```
        "StatesExecutionRole": {
              "Type": "AWS::IAM::Role",
              "Properties": {
                  "AssumeRolePolicyDocument": {
                      "Version": "2012-10-17",
                      "Statement": [
                          {
                              "Effect": "Allow",
                              "Principal": {
                                  "Service": [
                                      {
                                          "Fn::Sub": "states.${AWS::Region}.amazonaws.com"
                                      }
                                  ]
                              },
                              "Action": "sts:AssumeRole"
                          }
                      ]
                  },
                  "Path": "/",
                  "Policies": [
                      {
                          "PolicyName": "StatesExecutionPolicy",
                          "PolicyDocument": {
                              "Version": "2012-10-17",
                              "Statement": [
                                  {
                                      "Effect": "Allow",
                                      "Action": [
                                          "lambda:InvokeFunction"
                                      ],
                                      "Resource": "*"
                                  }
                              ]
                          }
                      }
                  ]
              }
          },
```

### To create a Lambda state machine

Define the Lambda state machine.

YAML

```
MyStateMachine:
    Type: "AWS::StepFunctions::StateMachine"
    Properties:
      DefinitionString:
        !Sub
          - |-
            {
              "Comment": "A Hello World example using an AWS Lambda function",
              "StartAt": "HelloWorld",
              "States": {
                "HelloWorld": {
                  "Type": "Task",
                  "Resource": "${lambdaArn}",
                  "End": true
                }
              }
            }
          - {lambdaArn: !GetAtt [ MyLambdaFunction, Arn ]}
      RoleArn: !GetAtt [ StatesExecutionRole, Arn ]
```

JSON

```
        "MyStateMachine": {
              "Type": "AWS::StepFunctions::StateMachine",
              "Properties": {
                  "DefinitionString": {
                      "Fn::Sub": [
                          "{\n  \"Comment\": \"A Hello World example using an AWS Lambda function\",\n  \"StartAt\": \"HelloWorld\",\n  \"States\": {\n    \"HelloWorld\": {\n      \"Type\": \"Task\",\n      \"Resource\": \"${lambdaArn}\",\n      \"End\": true\n    }\n  }\n}",
                          {
                              "lambdaArn": {
                                  "Fn::GetAtt": [
                                      "MyLambdaFunction",
                                      "Arn"
                                  ]
                              }
                          }
                      ]
                  },
                  "RoleArn": {
                      "Fn::GetAtt": [
                          "StatesExecutionRole",
                          "Arn"
                      ]
                  }
              }
          }
```

## Step 2: Use the CloudFormation template to create a

Lambda State Machine

Once you understand the components of the CloudFormation template, you can put them together
and use the template to create an CloudFormation stack.

### To create the Lambda state

machine

1. Copy the following example data to a file named `MyStateMachine.yaml`
   for the YAML example, or `MyStateMachine.json` for JSON.

YAML

```
AWSTemplateFormatVersion: "2010-09-09"
  Description: "An example template with an IAM role for a Lambda state machine."
  Resources:
    LambdaExecutionRole:
      Type: "AWS::IAM::Role"
      Properties:
        AssumeRolePolicyDocument:
          Version: "2012-10-17"
          Statement:
            - Effect: Allow
              Principal:
                Service: lambda.amazonaws.com
              Action: "sts:AssumeRole"

    MyLambdaFunction:
      Type: "AWS::Lambda::Function"
      Properties:
        Handler: "index.handler"
        Role: !GetAtt [ LambdaExecutionRole, Arn ]
        Code:
          ZipFile: |
            exports.handler = (event, context, callback) => {
                callback(null, "Hello World!");
            };
        Runtime: "nodejs12.x"
        Timeout: "25"

    StatesExecutionRole:
      Type: "AWS::IAM::Role"
      Properties:
        AssumeRolePolicyDocument:
          Version: "2012-10-17"
          Statement:
            - Effect: "Allow"
              Principal:
                Service:
                  - !Sub states.${AWS::Region}.amazonaws.com
              Action: "sts:AssumeRole"
        Path: "/"
        Policies:
          - PolicyName: StatesExecutionPolicy
            PolicyDocument:
              Version: "2012-10-17"
              Statement:
                - Effect: Allow
                  Action:
                    - "lambda:InvokeFunction"
                  Resource: "*"

    MyStateMachine:
      Type: "AWS::StepFunctions::StateMachine"
      Properties:
        DefinitionString:
          !Sub
            - |-
              {
                "Comment": "A Hello World example using an AWS Lambda function",
                "StartAt": "HelloWorld",
                "States": {
                  "HelloWorld": {
                    "Type": "Task",
                    "Resource": "${lambdaArn}",
                    "End": true
                  }
                }
              }
            - {lambdaArn: !GetAtt [ MyLambdaFunction, Arn ]}
        RoleArn: !GetAtt [ StatesExecutionRole, Arn ]
```

JSON

```
{
      "AWSTemplateFormatVersion": "2010-09-09",
      "Description": "An example template with an IAM role for a Lambda state machine.",
      "Resources": {
          "LambdaExecutionRole": {
              "Type": "AWS::IAM::Role",
              "Properties": {
                  "AssumeRolePolicyDocument": {
                      "Version": "2012-10-17",
                      "Statement": [
                          {
                              "Effect": "Allow",
                              "Principal": {
                                  "Service": "lambda.amazonaws.com"
                              },
                              "Action": "sts:AssumeRole"
                          }
                      ]
                  }
              }
          },
          "MyLambdaFunction": {
              "Type": "AWS::Lambda::Function",
              "Properties": {
                  "Handler": "index.handler",
                  "Role": {
                      "Fn::GetAtt": [
                          "LambdaExecutionRole",
                          "Arn"
                      ]
                  },
                  "Code": {
                      "ZipFile": "exports.handler = (event, context, callback) => {\n    callback(null, \"Hello World!\");\n};\n"
                  },
                  "Runtime": "nodejs12.x",
                  "Timeout": "25"
              }
          },
          "StatesExecutionRole": {
              "Type": "AWS::IAM::Role",
              "Properties": {
                  "AssumeRolePolicyDocument": {
                      "Version": "2012-10-17",
                      "Statement": [
                          {
                              "Effect": "Allow",
                              "Principal": {
                                  "Service": [
                                      {
                                          "Fn::Sub": "states.${AWS::Region}.amazonaws.com"
                                      }
                                  ]
                              },
                              "Action": "sts:AssumeRole"
                          }
                      ]
                  },
                  "Path": "/",
                  "Policies": [
                      {
                          "PolicyName": "StatesExecutionPolicy",
                          "PolicyDocument": {
                              "Version": "2012-10-17",
                              "Statement": [
                                  {
                                      "Effect": "Allow",
                                      "Action": [
                                          "lambda:InvokeFunction"
                                      ],
                                      "Resource": "*"
                                  }
                              ]
                          }
                      }
                  ]
              }
          },
          "MyStateMachine": {
              "Type": "AWS::StepFunctions::StateMachine",
              "Properties": {
                  "DefinitionString": {
                      "Fn::Sub": [
                          "{\n  \"Comment\": \"A Hello World example using an AWS Lambda function\",\n  \"StartAt\": \"HelloWorld\",\n  \"States\": {\n    \"HelloWorld\": {\n      \"Type\": \"Task\",\n      \"Resource\": \"${lambdaArn}\",\n      \"End\": true\n    }\n  }\n}",
                          {
                              "lambdaArn": {
                                  "Fn::GetAtt": [
                                      "MyLambdaFunction",
                                      "Arn"
                                  ]
                              }
                          }
                      ]
                  },
                  "RoleArn": {
                      "Fn::GetAtt": [
                          "StatesExecutionRole",
                          "Arn"
                      ]
                  }
              }
          }
      }
  }
```

2. Open the [CloudFormation
   console](https://console.aws.amazon.com/cloudformation/home "https://console.aws.amazon.com/cloudformation/home") and choose **Create Stack**.
3. On the **Select Template** page, choose **Upload a
   template to Amazon S3**. Choose your `MyStateMachine` file, and
   then choose **Next**.
4. On the **Specify Details** page, for **Stack
   name**, enter `MyStateMachine`, and then choose
   **Next**.
5. On the **Options** page, choose **Next**.
6. On the **Review** page, choose **I acknowledge that CloudFormation
   might create IAM resources.** and then choose
   **Create**.

CloudFormation begins to create the `MyStateMachine` stack and displays the
**CREATE_IN_PROGRESS** status. When the process is complete, CloudFormation
displays the **CREATE_COMPLETE** status. 7. (Optional) To display the resources in your stack, select the stack and choose the
**Resources** tab.

## Step 3: Start a State Machine

execution

After you create your Lambda state machine, you can start its execution.

### To start the state machine

execution

1. Open the [Step Functions console](https://console.aws.amazon.com/states/home "https://console.aws.amazon.com/states/home") and
   choose the name of the state machine that you created using CloudFormation.
2. On the **`MyStateMachine-ABCDEFGHIJ1K`**
   page, choose **New execution**.

The **New execution** page is displayed. 3. (Optional) Enter a custom execution name to override the generated default.

###### Non-ASCII names and logging

Step Functions accepts names for state machines, executions, activities, and labels that contain non-ASCII characters. Because such characters will prevent Amazon CloudWatch from logging data, we recommend using only ASCII characters so you can track Step Functions metrics. 4. Choose **Start Execution**.

A new execution of your state machine starts, and a new page showing your running
execution is displayed. 5. (Optional) In the **Execution Details**, review the
**Execution Status** and the **Started** and
**Closed** timestamps. 6. To view the results of your execution, choose **Output**.
