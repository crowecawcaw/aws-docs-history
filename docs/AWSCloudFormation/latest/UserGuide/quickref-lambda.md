# AWS Lambda template

The following template uses an AWS Lambda (Lambda) function and custom resource to append a new security group to a
 list of existing security groups. This function is useful when you want to build a list of security groups
 dynamically, so that your list includes both new and existing security groups. For example, you can pass a list of
 existing security groups as a parameter value, append the new value to the list, and then associate all your values
 with an EC2 instance. For more information about the Lambda function resource type, see [AWS::Lambda::Function](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-function.html").

In the example, when CloudFormation creates the `AllSecurityGroups` custom resource, CloudFormation invokes the
 `AppendItemToListFunction` Lambda function. CloudFormation passes the list of existing security groups and a new
 security group (`NewSecurityGroup`) to the function, which appends the new security group to the list and
 then returns the modified list. CloudFormation uses the modified list to associate all security groups with the
 `MyEC2Instance` resource.


## JSON



```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Parameters": {
        "ExistingSecurityGroups": {
            "Type": "List<AWS::EC2::SecurityGroup::Id>"
        },
        "ExistingVPC": {
            "Type": "AWS::EC2::VPC::Id",
            "Description": "The VPC ID that includes the security groups in the ExistingSecurityGroups parameter."
        },
        "InstanceType": {
            "Type": "String",
            "Default": "t2.micro",
            "AllowedValues": [
                "t2.micro",
                "t3.micro"
            ]
        }
    },

    "Resources": {
        "SecurityGroup": {
            "Type": "AWS::EC2::SecurityGroup",
            "Properties": {
                "GroupDescription": "Allow HTTP traffic to the host",
                "VpcId": {
                    "Ref": "ExistingVPC"
                },
                "SecurityGroupIngress": [
                    {
                        "IpProtocol": "tcp",
                        "FromPort": 80,
                        "ToPort": 80,
                        "CidrIp": "0.0.0.0/0"
                    }
                ],
                "SecurityGroupEgress": [
                    {
                        "IpProtocol": "tcp",
                        "FromPort": 80,
                        "ToPort": 80,
                        "CidrIp": "0.0.0.0/0"
                    }
                ]
            }
        },
        "AllSecurityGroups": {
            "Type": "Custom::Split",
            "Properties": {
                "ServiceToken": {
                    "Fn::GetAtt": [
                        "AppendItemToListFunction",
                        "Arn"
                    ]
                },
                "List": {
                    "Ref": "ExistingSecurityGroups"
                },
                "AppendedItem": {
                    "Ref": "SecurityGroup"
                }
            }
        },
        "AppendItemToListFunction": {
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
                    "ZipFile": {
                        "Fn::Join": [
                            "",
                            [
                                "var response = require('cfn-response');",
                                "exports.handler = function(event, context) {",
                                "   var responseData = {Value: event.ResourceProperties.List};",
                                "   responseData.Value.push(event.ResourceProperties.AppendedItem);",
                                "   response.send(event, context, response.SUCCESS, responseData);",
                                "};"
                            ]
                        ]
                    }
                },
                "Runtime": "nodejs20.x"
            }
        },
        "MyEC2Instance": {
            "Type": "AWS::EC2::Instance",
            "Properties": {
                "ImageId": "{{resolve:ssm:/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2}}",
                "SecurityGroupIds": {
                    "Fn::GetAtt": [
                        "AllSecurityGroups",
                        "Value"
                    ]
                },
                "InstanceType": {
                    "Ref": "InstanceType"
                }
            }
        },
        "LambdaExecutionRole": {
            "Type": "AWS::IAM::Role",
            "Properties": {
                "AssumeRolePolicyDocument": {
                    "Version": "2012-10-17", 		 	 	 
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "Service": [
                                    "lambda.amazonaws.com"
                                ]
                            },
                            "Action": [
                                "sts:AssumeRole"
                            ]
                        }
                    ]
                },
                "Path": "/",
                "Policies": [
                    {
                        "PolicyName": "root",
                        "PolicyDocument": {
                            "Version": "2012-10-17", 		 	 	 
                            "Statement": [
                                {
                                    "Effect": "Allow",
                                    "Action": [
                                        "logs:*"
                                    ],
                                    "Resource": "arn:aws:logs:*:*:*"
                                }
                            ]
                        }
                    }
                ]
            }
        }
    },
    "Outputs": {
        "AllSecurityGroups": {
            "Description": "Security Groups that are associated with the EC2 instance",
            "Value": {
                "Fn::Join": [
                    ", ",
                    {
                        "Fn::GetAtt": [
                            "AllSecurityGroups",
                            "Value"
                        ]
                    }
                ]
            }
        }
    }
}
```

## YAML



```
AWSTemplateFormatVersion: '2010-09-09'
Parameters:
  ExistingSecurityGroups:
    Type: List<AWS::EC2::SecurityGroup::Id>
  ExistingVPC:
    Type: AWS::EC2::VPC::Id
    Description: The VPC ID that includes the security groups in the ExistingSecurityGroups parameter.
  InstanceType:
    Type: String
    Default: t2.micro
    AllowedValues:
      - t2.micro
      - t3.micro
Resources:
  SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Allow HTTP traffic to the host
      VpcId: !Ref ExistingVPC
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          CidrIp: 0.0.0.0/0
      SecurityGroupEgress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          CidrIp: 0.0.0.0/0
  AllSecurityGroups:
    Type: Custom::Split
    Properties:
      ServiceToken: !GetAtt AppendItemToListFunction.Arn
      List: !Ref ExistingSecurityGroups
      AppendedItem: !Ref SecurityGroup
  AppendItemToListFunction:
    Type: AWS::Lambda::Function
    Properties:
      Handler: index.handler
      Role: !GetAtt LambdaExecutionRole.Arn
      Code:
        ZipFile: !Join
          - ''
          - - var response = require('cfn-response');
            - exports.handler = function(event, context) {
            - '   var responseData = {Value: event.ResourceProperties.List};'
            - '   responseData.Value.push(event.ResourceProperties.AppendedItem);'
            - '   response.send(event, context, response.SUCCESS, responseData);'
            - '};'
      Runtime: nodejs20.x
  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      ImageId: '{{resolve:ssm:/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2}}'
      SecurityGroupIds: !GetAtt AllSecurityGroups.Value
      InstanceType: !Ref InstanceType
  LambdaExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17' 		 	 	 
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - lambda.amazonaws.com
            Action:
              - sts:AssumeRole
      Path: /
      Policies:
        - PolicyName: root
          PolicyDocument:
            Version: '2012-10-17' 		 	 	 
            Statement:
              - Effect: Allow
                Action:
                  - logs:*
                Resource: arn:aws:logs:*:*:*
Outputs:
  AllSecurityGroups:
    Description: Security Groups that are associated with the EC2 instance
    Value: !Join
      - ', '
      - !GetAtt AllSecurityGroups.Value
```
