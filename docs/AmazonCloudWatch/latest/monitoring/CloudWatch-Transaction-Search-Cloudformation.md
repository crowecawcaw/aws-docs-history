# Using Transaction Search with AWS CloudFormation

You can use AWS CloudFormation to enable and configure X-Ray Transaction Search.

###### Note

To create a AWS CloudFormation stack, see [Creating your first stack](../../../AWSCloudFormation/latest/UserGuide/gettingstarted.md "../../../AWSCloudFormation/latest/UserGuide/gettingstarted.md") .

## Prerequisites

- You must have access to an AWS account with an IAM user or role that has permissions to use Amazon EC2, Amazon S3, AWS CloudFormation, or have administrative user access.
- You must have a Virtual Private Cloud (VPC) that has access to the internet. To keep things simple, you can use the default VPC that comes with your account. The default VPC and default subnets are sufficient for this configuration.
- Make sure Transaction Search is disabled before you enable using AWS CDK or AWS CloudFormation.

## Enabling Transaction Search

To enable Transaction Search using CloudFormation, you need to create the following two resources.

- `AWS::Logs::ResourcePolicy`
- `AWS::XRay::TransactionSearchConfig`

1. **Create AWS::Logs::ResourcePolicy** – Create a resource policy that allows X-Ray to send traces to CloudWatch Logs

**YAML**

```
Resources:
  LogsResourcePolicy:
    Type: AWS::Logs::ResourcePolicy
    Properties:
      PolicyName: TransactionSearchAccess
      PolicyDocument: !Sub >
        {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Sid": "TransactionSearchXRayAccess",
              "Effect": "Allow",
              "Principal": {
                "Service": "xray.amazonaws.com"
              },
              "Action": "logs:PutLogEvents",
              "Resource": [
                "arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:aws/spans:*",
                "arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/application-signals/data:*"
              ],
              "Condition": {
                "ArnLike": {
                  "aws:SourceArn": "arn:${AWS::Partition}:xray:${AWS::Region}:${AWS::AccountId}:*"
                },
                "StringEquals": {
                  "aws:SourceAccount": "${AWS::AccountId}"
                }
              }
            }
          ]
        }
```

**JSON**

```
{
    "Resources": {
        "LogsResourcePolicy": {
            "Type": "AWS::Logs::ResourcePolicy",
            "Properties": {
                "PolicyName": "TransactionSearchAccess",
                "PolicyDocument": {
                    "Fn::Sub": "{\n  \"Version\": \"2012-10-17\",		 	 	 \n  \"Statement\": [\n    {\n      \"Sid\": \"TransactionSearchXRayAccess\",\n      \"Effect\": \"Allow\",\n      \"Principal\": {\n        \"Service\": \"xray.amazonaws.com\"\n      },\n      \"Action\": \"logs:PutLogEvents\",\n      \"Resource\": [\n        \"arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:aws/spans:*\",\n        \"arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/application-signals/data:*\"\n      ],\n      \"Condition\": {\n        \"ArnLike\": {\n          \"aws:SourceArn\": \"arn:${AWS::Partition}:xray:${AWS::Region}:${AWS::AccountId}:*\"\n        },\n        \"StringEquals\": {\n          \"aws:SourceAccount\": \"${AWS::AccountId}\"\n        }\n      }\n    }\n  ]\n}"
                }
            }
        }
    }
}
```

2. **Create and Configure AWS::XRay::TransactionSearchConfig** – Create the `TransactionSearchConfig` resource to enable Transaction Search.

**YAML**

```
Resources:
  XRayTransactionSearchConfig:
    Type: AWS::XRay::TransactionSearchConfig
```

**JSON**

```
{
  "Resources": {
    "XRayTransactionSearchConfig": {
      "Type": "AWS::XRay::TransactionSearchConfig"
    }
  }
}
```

3. (Optional) You can set the `IndexingPercentage` property to control the percentage of spans that will be indexed.

**YAML**

```
Resources:
  XRayTransactionSearchConfig:
    Type: AWS::XRay::TransactionSearchConfig
    Properties:
      IndexingPercentage: 50
```

**JSON**

```
{
  "Resources": {
    "XRayTransactionSearchConfig": {
      "Type": "AWS::XRay::TransactionSearchConfig",
      "Properties": {
        "IndexingPercentage": 20
      }
    }
  }
}
```

The IndexingPercentage value can be set between 0 and 100.

## Template examples

The following example includes both the resource policy and the TransactionSearchConfig.

**YAML**

```
Resources:
  LogsResourcePolicy:
    Type: AWS::Logs::ResourcePolicy
    Properties:
      PolicyName: TransactionSearchAccess
      PolicyDocument: !Sub >
        {
          "Version": "2012-10-17",
          "Statement": [
            {
              "Sid": "TransactionSearchXRayAccess",
              "Effect": "Allow",
              "Principal": {
                "Service": "xray.amazonaws.com"
              },
              "Action": "logs:PutLogEvents",
              "Resource": [
                "arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:aws/spans:*",
                "arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/application-signals/data:*"
              ],
              "Condition": {
                "ArnLike": {
                  "aws:SourceArn": "arn:${AWS::Partition}:xray:${AWS::Region}:${AWS::AccountId}:*"
                },
                "StringEquals": {
                  "aws:SourceAccount": "${AWS::AccountId}"
                }
              }
            }
          ]
        }

  XRayTransactionSearchConfig:
    Type: AWS::XRay::TransactionSearchConfig
    Properties:
      IndexingPercentage: 10
```

**JSON**

```
{
    "Resources": {
        "LogsResourcePolicy": {
            "Type": "AWS::Logs::ResourcePolicy",
            "Properties": {
                "PolicyName": "TransactionSearchAccess",
                "PolicyDocument": {
                    "Fn::Sub": "{\n  \"Version\": \"2012-10-17\",		 	 	 \n  \"Statement\": [\n    {\n      \"Sid\": \"TransactionSearchXRayAccess\",\n      \"Effect\": \"Allow\",\n      \"Principal\": {\n        \"Service\": \"xray.amazonaws.com\"\n      },\n      \"Action\": \"logs:PutLogEvents\",\n      \"Resource\": [\n        \"arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:aws/spans:*\",\n        \"arn:${AWS::Partition}:logs:${AWS::Region}:${AWS::AccountId}:log-group:/aws/application-signals/data:*\"\n      ],\n      \"Condition\": {\n        \"ArnLike\": {\n          \"aws:SourceArn\": \"arn:${AWS::Partition}:xray:${AWS::Region}:${AWS::AccountId}:*\"\n        },\n        \"StringEquals\": {\n          \"aws:SourceAccount\": \"${AWS::AccountId}\"\n        }\n      }\n    }\n  ]\n}"
                }
            }
        },
        "XRayTransactionSearchConfig": {
            "Type": "AWS::XRay::TransactionSearchConfig",
            "Properties": {
                "IndexingPercentage": 20
            }
        }
    }
}
```

Here is an example using AWS CDK in TypeScript.

**CDK**

```
import * as cdk from '@aws-cdk/core';
import * as logs from '@aws-cdk/aws-logs';
import * as xray from '@aws-cdk/aws-xray';

export class XRayTransactionSearchStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create the resource policy
    const transactionSearchAccess = new logs.CfnResourcePolicy(this, 'XRayLogResourcePolicy', {
      policyName: 'TransactionSearchAccess',
      policyDocument: JSON.stringify({
        Version: '2012-10-17',
        Statement: [
          {
            Sid: 'TransactionSearchXRayAccess',
            Effect: 'Allow',
            Principal: {
              Service: 'xray.amazonaws.com',
            },
            Action: 'logs:PutLogEvents',
            Resource: [
              `arn:${this.partition}:logs:${this.region}:${this.account}:log-group:aws/spans:*`,
              `arn:${this.partition}:logs:${this.region}:${this.account}:log-group:/aws/application-signals/data:*`,
            ],
            Condition: {
              ArnLike: {
                'aws:SourceArn': `arn:${this.partition}:xray:${this.region}:${this.account}:*`,
              },
              StringEquals: {
                'aws:SourceAccount': this.account,
              },
            },
          },
        ],
      }),
    });

    // Create the TransactionSearchConfig with dependency
    const transactionSearchConfig = new xray.CfnTransactionSearchConfig(this, 'XRayTransactionSearchConfig', {
      indexingPercentage: 10,
    });

    // Add the dependency to ensure Resource Policy is created first
    transactionSearchConfig.addDependsOn(transactionSearchAccess);
  }
}


```

## Verifying the configuration

After deploying your AWS CloudFormation stack, you can verify the configuration using the AWS CLI.

**aws xray get-trace-segment-destination**

A successful configuration will return the following.

```
{
    "Destination": "CloudWatchLogs",
    "Status": "ACTIVE"
}
```
