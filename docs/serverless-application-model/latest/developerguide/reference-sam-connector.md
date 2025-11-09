# AWS SAM connector reference

This section contains reference information for the AWS Serverless Application Model (AWS SAM) connector resource
type. For an introduction to connectors, see [Managing resource permissions with AWS SAM
connectors](managing-permissions-connectors.md "managing-permissions-connectors.md").

## Supported source and destination resource

types for connectors

The `AWS::Serverless::Connector` resource type supports a select number of connections between source
and destination resources. When configuring connectors in your AWS SAM template, use the following table to reference
supported connections and the properties that need to be defined for each source and destination resource type.
For more information about configuring connectors in your template, see
[AWS::Serverless::Connector](sam-resource-connector.md "sam-resource-connector.md").

For both source and destination resources, when defined within the same template, use the `Id`
property. Optionally, a `Qualifier` can be added to narrow the scope of your defined resource. When
the resource is not within the same template, use a combination of supported properties.

To request new connections, [submit a new issue](https://github.com/aws/serverless-application-model/issues/new?assignees=&labels=area%2Fconnectors,stage%2Fneeds-triage&template=other.md&title=%28New%20Connector%20Profile%29 "https://github.com/aws/serverless-application-model/issues/new?assignees=&labels=area%2Fconnectors,stage%2Fneeds-triage&template=other.md&title=%28New%20Connector%20Profile%29") at the _serverless-application-model AWS GitHub
repository_.

| Source type                        | Destination type                   | Permissions     | Source properties                                | Destination properties                   |
| ---------------------------------- | ---------------------------------- | --------------- | ------------------------------------------------ | ---------------------------------------- |
| `AWS::ApiGateway::RestApi`         | `AWS::Lambda::Function`            | `Write`         | `Id` or `Qualifier`, `ResourceId`, and<br>`Type` | `Id` or `Arn` and `Type`                 |
| `AWS::ApiGateway::RestApi`         | `AWS::Serverless::Function`        | `Write`         | `Id` or `Qualifier`, `ResourceId`, and<br>`Type` | `Id` or `Arn` and `Type`                 |
| `AWS::ApiGatewayV2::Api`           | `AWS::Lambda::Function`            | `Write`         | `Id` or `Qualifier`, `ResourceId`, and<br>`Type` | `Id` or `Arn` and `Type`                 |
| `AWS::ApiGatewayV2::Api`           | `AWS::Serverless::Function`        | `Write`         | `Id` or `Qualifier`, `ResourceId`, and<br>`Type` | `Id` or `Arn` and `Type`                 |
| `AWS::AppSync::DataSource`         | `AWS::DynamoDB::Table`             | `Read`          | `Id` or `RoleName` and `Type`                    | `Id` or `Arn` and `Type`                 |
| `AWS::AppSync::DataSource`         | `AWS::DynamoDB::Table`             | `Write`         | `Id` or `RoleName` and `Type`                    | `Id` or `Arn` and `Type`                 |
| `AWS::AppSync::DataSource`         | `AWS::Events::EventBus`            | `Write`         | `Id` or `RoleName` and `Type`                    | `Id` or `Arn` and `Type`                 |
| `AWS::AppSync::DataSource`         | `AWS::Lambda::Function`            | `Write`         | `Id` or `RoleName` and `Type`                    | `Id` or `Arn` and `Type`                 |
| `AWS::AppSync::DataSource`         | `AWS::Serverless::Function`        | `Write`         | `Id` or `RoleName` and `Type`                    | `Id` or `Arn` and `Type`                 |
| `AWS::AppSync::DataSource`         | `AWS::Serverless::SimpleTable`     | `Read`          | `Id` or `RoleName` and `Type`                    | `Id` or `Arn` and `Type`                 |
| `AWS::AppSync::DataSource`         | `AWS::Serverless::SimpleTable`     | `Write`         | `Id` or `RoleName` and `Type`                    | `Id` or `Arn` and `Type`                 |
| `AWS::AppSync::GraphQLApi`         | `AWS::Lambda::Function`            | `Write`         | `Id` or `ResourceId` and `Type`                  | `Id` or `Arn` and `Type`                 |
| `AWS::AppSync::GraphQLApi`         | `AWS::Serverless::Function`        | `Write`         | `Id` or `ResourceId` and `Type`                  | `Id` or `Arn` and `Type`                 |
| `AWS::DynamoDB::Table`             | `AWS::Lambda::Function`            | `Read`          | `Id` or `Arn` and `Type`                         | `Id` or `RoleName` and<br>`Type`         |
| `AWS::DynamoDB::Table`             | `AWS::Serverless::Function`        | `Read`          | `Id` or `Arn` and `Type`                         | `Id` or `RoleName` and<br>`Type`         |
| `AWS::Events::Rule`                | `AWS::Events::EventBus`            | `Write`         | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Events::Rule`                | `AWS::Lambda::Function`            | `Write`         | `Id` or `Arn` and `Type`                         | `Id` or `Arn` and `Type`                 |
| `AWS::Events::Rule`                | `AWS::Serverless::Function`        | `Write`         | `Id` or `Arn` and `Type`                         | `Id` or `Arn` and `Type`                 |
| `AWS::Events::Rule`                | `AWS::Serverless::StateMachine`    | `Write`         | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Events::Rule`                | `AWS::SNS::Topic`                  | `Write`         | `Id` or `Arn` and `Type`                         | `Id` or `Arn` and `Type`                 |
| `AWS::Events::Rule`                | `AWS::SQS::Queue`                  | `Write`         | `Id` or `Arn` and `Type`                         | `Id` or `Arn`, `QueueUrl`, and<br>`Type` |
| `AWS::Events::Rule`                | `AWS::StepFunctions::StateMachine` | `Write`         | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Lambda::Function`            | `AWS::DynamoDB::Table`             | `Read`, `Write` | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Lambda::Function`            | `AWS::Events::EventBus`            | `Write`         | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Lambda::Function`            | `AWS::Lambda::Function`            | `Write`         | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Lambda::Function`            | `AWS::Location::PlaceIndex`        | `Read`          | `Id` or `RoleName` and `Type`                    | `Id` or `Arn` and `Type`                 |
| `AWS::Lambda::Function`            | `AWS::S3::Bucket`                  | `Read`, `Write` | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Lambda::Function`            | `AWS::Serverless::Function`        | `Write`         | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Lambda::Function`            | `AWS::Serverless::SimpleTable`     | `Read`, `Write` | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Lambda::Function`            | `AWS::Serverless::StateMachine`    | `Read`, `Write` | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn`, `Name`, and<br>`Type`     |
| `AWS::Lambda::Function`            | `AWS::SNS::Topic`                  | `Write`         | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Lambda::Function`            | `AWS::SQS::Queue`                  | `Read`, `Write` | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Lambda::Function`            | `AWS::StepFunctions::StateMachine` | `Read`, `Write` | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn`, `Name`, and<br>`Type`     |
| `AWS::S3::Bucket`                  | `AWS::Lambda::Function`            | `Write`         | `Id` or `Arn` and `Type`                         | `Id` or `Arn` and `Type`                 |
| `AWS::S3::Bucket`                  | `AWS::Serverless::Function`        | `Write`         | `Id` or `Arn` and `Type`                         | `Id` or `Arn` and `Type`                 |
| `AWS::Serverless::Api`             | `AWS::Lambda::Function`            | `Write`         | `Id` or `Qualifier`, `ResourceId`, and<br>`Type` | `Id` or `Arn` and `Type`                 |
| `AWS::Serverless::Api`             | `AWS::Serverless::Function`        | `Write`         | `Id` or `Qualifier`, `ResourceId`, and<br>`Type` | `Id` or `Arn` and `Type`                 |
| `AWS::Serverless::Function`        | `AWS::DynamoDB::Table`             | `Read`, `Write` | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Serverless::Function`        | `AWS::Events::EventBus`            | `Write`         | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Serverless::Function`        | `AWS::Lambda::Function`            | `Write`         | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Serverless::Function`        | `AWS::S3::Bucket`                  | `Read`, `Write` | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Serverless::Function`        | `AWS::Serverless::Function`        | `Write`         | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Serverless::Function`        | `AWS::Serverless::SimpleTable`     | `Read`, `Write` | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Serverless::Function`        | `AWS::Serverless::StateMachine`    | `Read`, `Write` | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn`, `Name`, and<br>`Type`     |
| `AWS::Serverless::Function`        | `AWS::SNS::Topic`                  | `Write`         | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Serverless::Function`        | `AWS::SQS::Queue`                  | `Read`, `Write` | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Serverless::Function`        | `AWS::StepFunctions::StateMachine` | `Read`, `Write` | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn`, `Name`, and<br>`Type`     |
| `AWS::Serverless::HttpApi`         | `AWS::Lambda::Function`            | `Write`         | `Id` or `Qualifier`, `ResourceId`, and<br>`Type` | `Id` or `Arn` and `Type`                 |
| `AWS::Serverless::HttpApi`         | `AWS::Serverless::Function`        | `Write`         | `Id` or `Qualifier`, `ResourceId`, and<br>`Type` | `Id` or `Arn` and `Type`                 |
| `AWS::Serverless::SimpleTable`     | `AWS::Lambda::Function`            | `Read`          | `Id` or `Arn` and `Type`                         | `Id` or `RoleName` and<br>`Type`         |
| `AWS::Serverless::SimpleTable`     | `AWS::Serverless::Function`        | `Read`          | `Id` or `Arn` and `Type`                         | `Id` or `RoleName` and<br>`Type`         |
| `AWS::Serverless::StateMachine`    | `AWS::DynamoDB::Table`             | `Read`, `Write` | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Serverless::StateMachine`    | `AWS::Events::EventBus`            | `Write`         | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Serverless::StateMachine`    | `AWS::Lambda::Function`            | `Write`         | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Serverless::StateMachine`    | `AWS::S3::Bucket`                  | `Read`, `Write` | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Serverless::StateMachine`    | `AWS::Serverless::Function`        | `Write`         | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Serverless::StateMachine`    | `AWS::Serverless::SimpleTable`     | `Read`, `Write` | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Serverless::StateMachine`    | `AWS::Serverless::StateMachine`    | `Read`, `Write` | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn`, `Name`, and<br>`Type`     |
| `AWS::Serverless::StateMachine`    | `AWS::SNS::Topic`                  | `Write`         | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Serverless::StateMachine`    | `AWS::SQS::Queue`                  | `Write`         | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::Serverless::StateMachine`    | `AWS::StepFunctions::StateMachine` | `Read`, `Write` | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn`, `Name`, and<br>`Type`     |
| `AWS::SNS::Topic`                  | `AWS::Lambda::Function`            | `Write`         | `Id` or `Arn` and `Type`                         | `Id` or `Arn` and `Type`                 |
| `AWS::SNS::Topic`                  | `AWS::Serverless::Function`        | `Write`         | `Id` or `Arn` and `Type`                         | `Id` or `Arn` and `Type`                 |
| `AWS::SNS::Topic`                  | `AWS::SQS::Queue`                  | `Write`         | `Id` or `Arn` and `Type`                         | `Id` or `Arn`, `QueueUrl`, and<br>`Type` |
| `AWS::SQS::Queue`                  | `AWS::Lambda::Function`            | `Read`, `Write` | `Id` or `Arn` and `Type`                         | `Id` or `RoleName` and<br>`Type`         |
| `AWS::SQS::Queue`                  | `AWS::Serverless::Function`        | `Read`, `Write` | `Id` or `Arn` and `Type`                         | `Id` or `RoleName` and<br>`Type`         |
| `AWS::StepFunctions::StateMachine` | `AWS::DynamoDB::Table`             | `Read`, `Write` | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::StepFunctions::StateMachine` | `AWS::Events::EventBus`            | `Write`         | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::StepFunctions::StateMachine` | `AWS::Lambda::Function`            | `Write`         | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::StepFunctions::StateMachine` | `AWS::S3::Bucket`                  | `Read`, `Write` | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::StepFunctions::StateMachine` | `AWS::Serverless::Function`        | `Write`         | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::StepFunctions::StateMachine` | `AWS::Serverless::SimpleTable`     | `Read`, `Write` | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::StepFunctions::StateMachine` | `AWS::Serverless::StateMachine`    | `Read`, `Write` | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn`, `Name`, and<br>`Type`     |
| `AWS::StepFunctions::StateMachine` | `AWS::SNS::Topic`                  | `Write`         | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::StepFunctions::StateMachine` | `AWS::SQS::Queue`                  | `Write`         | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn` and `Type`                 |
| `AWS::StepFunctions::StateMachine` | `AWS::StepFunctions::StateMachine` | `Read`, `Write` | `Id` or `RoleName` and<br>`Type`                 | `Id` or `Arn`, `Name`, and<br>`Type`     |

## IAM policies created by connectors

This section documents the AWS Identity and Access Management (IAM) policies that are created by AWS SAM when using connectors.

`AWS::DynamoDB::Table` to `AWS::Lambda::Function`

**Policy type**

[Customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") attached to the
`AWS::Lambda::Function` role.

**Access categories**

`Read`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:DescribeStream",
        "dynamodb:GetRecords",
        "dynamodb:GetShardIterator",
        "dynamodb:ListStreams"
      ],
      "Resource": [
        "%{Source.Arn}/stream/*"
      ]
    }
  ]
}
```

`AWS::Events::Rule` to `AWS::SNS::Topic`

**Policy type**

[`AWS::SNS::TopicPolicy`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-sns-topicpolicy.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-sns-topicpolicy.md")
attached to the `AWS::SNS::Topic`.

**Access categories**

`Write`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "events.amazonaws.com"
      },
      "Resource": "%{Destination.Arn}",
      "Action": "sns:Publish",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "%{Source.Arn}"
        }
      }
    }
  ]
}
```

`AWS::Events::Rule` to `AWS::Events::EventBus`

**Policy type**

[Customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") attached to the
`AWS::Events::Rule` role.

**Access categories**

`Write`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "events:PutEvents"
      ],
      "Resource": [
        "%{Destination.Arn}"
      ]
    }
  ]
}
```

`AWS::Events::Rule` to `AWS::StepFunctions::StateMachine`

**Policy type**

[Customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") attached to the `AWS::Events::Rule` role.

**Access categories**

`Write`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "states:StartExecution"
      ],
      "Resource": [
        "%{Destination.Arn}"
      ]
    }
  ]
}
```

`AWS::Events::Rule` to `AWS::Lambda::Function`

**Policy type**

`AWS::Lambda::Permission` attached to the `AWS::Lambda::Function`.

**Access categories**

`Write`

```
{
  "Action": "lambda:InvokeFunction",
  "Principal": "events.amazonaws.com",
  "SourceArn": "%{Source.Arn}"
}
```

`AWS::Events::Rule` to `AWS::SQS::Queue`

**Policy type**

`AWS::SQS::QueuePolicy` attached to the `AWS::SQS::Queue`.

**Access categories**

`Write`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "events.amazonaws.com"
      },
      "Resource": "%{Destination.Arn}",
      "Action": "sqs:SendMessage",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "%{Source.Arn}"
        }
      }
    }
  ]
}
```

`AWS::Lambda::Function` to `AWS::Lambda::Function`

**Policy type**

[Customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") attached to the `AWS::Lambda::Function` role.

**Access categories**

`Write`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "lambda:InvokeAsync",
        "lambda:InvokeFunction"
      ],
      "Resource": [
        "%{Destination.Arn}"
      ]
    }
  ]
}
```

`AWS::Lambda::Function` to `AWS::S3::Bucket`

**Policy type**

[Customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") attached to the `AWS::Lambda::Function` role.

**Access categories**

`Read`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:GetObjectAcl",
        "s3:GetObjectLegalHold",
        "s3:GetObjectRetention",
        "s3:GetObjectTorrent",
        "s3:GetObjectVersion",
        "s3:GetObjectVersionAcl",
        "s3:GetObjectVersionForReplication",
        "s3:GetObjectVersionTorrent",
        "s3:ListBucket",
        "s3:ListBucketMultipartUploads",
        "s3:ListBucketVersions",
        "s3:ListMultipartUploadParts"
      ],
      "Resource": [
        "%{Destination.Arn}",
        "%{Destination.Arn}/*"
      ]
    }
  ]
}
```

`Write`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:AbortMultipartUpload",
        "s3:DeleteObject",
        "s3:DeleteObjectVersion",
        "s3:PutObject",
        "s3:PutObjectLegalHold",
        "s3:PutObjectRetention",
        "s3:RestoreObject"
      ],
      "Resource": [
        "%{Destination.Arn}",
        "%{Destination.Arn}/*"
      ]
    }
  ]
}
```

`AWS::Lambda::Function` to `AWS::DynamoDB::Table`

**Policy type**

[Customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") attached to the `AWS::Lambda::Function` role.

**Access categories**

`Read`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:GetItem",
        "dynamodb:Query",
        "dynamodb:Scan",
        "dynamodb:BatchGetItem",
        "dynamodb:ConditionCheckItem",
        "dynamodb:PartiQLSelect"
      ],
      "Resource": [
        "%{Destination.Arn}",
        "%{Destination.Arn}/index/*"
      ]
    }
  ]
}
```

`Write`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:PutItem",
        "dynamodb:UpdateItem",
        "dynamodb:DeleteItem",
        "dynamodb:BatchWriteItem",
        "dynamodb:PartiQLDelete",
        "dynamodb:PartiQLInsert",
        "dynamodb:PartiQLUpdate"
      ],
      "Resource": [
        "%{Destination.Arn}",
        "%{Destination.Arn}/index/*"
      ]
    }
  ]
}
```

`AWS::Lambda::Function` to `AWS::SQS::Queue`

**Policy type**

[Customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") attached to the `AWS::Lambda::Function` role.

**Access categories**

`Read`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "sqs:ReceiveMessage",
        "sqs:GetQueueAttributes"
      ],
      "Resource": [
        "%{Destination.Arn}"
      ]
    }
  ]
}
```

`Write`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "sqs:DeleteMessage",
        "sqs:SendMessage",
        "sqs:ChangeMessageVisibility",
        "sqs:PurgeQueue"
      ],
      "Resource": [
        "%{Destination.Arn}"
      ]
    }
  ]
}
```

`AWS::Lambda::Function` to `AWS::SNS::Topic`

**Policy type**

[Customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") attached to the `AWS::Lambda::Function` role.

**Access categories**

`Write`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "sns:Publish"
      ],
      "Resource": [
        "%{Destination.Arn}"
      ]
    }
  ]
}
```

`AWS::Lambda::Function` to `AWS::StepFunctions::StateMachine`

**Policy type**

[Customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") attached to the `AWS::Lambda::Function` role.

**Access categories**

`Write`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "states:StartExecution",
        "states:StartSyncExecution"
      ],
      "Resource": [
        "%{Destination.Arn}"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "states:StopExecution"
      ],
      "Resource": [
        "arn:${AWS::Partition}:states:${AWS::Region}:${AWS::AccountId}:execution:%{Destination.Name}:*"
      ]
    }
  ]
}
```

`Read`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "states:DescribeStateMachine",
        "states:ListExecutions"
      ],
      "Resource": [
        "%{Destination.Arn}"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "states:DescribeExecution",
        "states:DescribeStateMachineForExecution",
        "states:GetExecutionHistory"
      ],
      "Resource": [
        "arn:${AWS::Partition}:states:${AWS::Region}:${AWS::AccountId}:execution:%{Destination.Name}:*"
      ]
    }
  ]
}
```

`AWS::Lambda::Function` to `AWS::Events::EventBus`

**Policy type**

[Customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") attached to the `AWS::Lambda::Function` role.

**Access categories**

`Write`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "events:PutEvents"
      ],
      "Resource": [
        "%{Destination.Arn}"
      ]
    }
  ]
}
```

`AWS::Lambda::Function` to `AWS::Location::PlaceIndex`

**Policy type**

[Customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") attached to the `AWS::Lambda::Function` role.

**Access categories**

`Read`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "geo:DescribePlaceIndex",
        "geo:GetPlace",
        "geo:SearchPlaceIndexForPosition",
        "geo:SearchPlaceIndexForSuggestions",
        "geo:SearchPlaceIndexForText"
      ],
      "Resource": [
        "%{Destination.Arn}"
      ]
    }
  ]
}
```

`AWS::ApiGatewayV2::Api` to `AWS::Lambda::Function`

**Policy type**

`AWS::Lambda::Permission` attached to the `AWS::Lambda::Function`.

**Access categories**

`Write`

```
{
  "Action": "lambda:InvokeFunction",
  "Principal": "apigateway.amazonaws.com",
  "SourceArn": "arn:${AWS::Partition}:execute-api:${AWS::Region}:${AWS::AccountId}:%{Source.ResourceId}/%{Source.Qualifier}"
}
```

`AWS::ApiGateway::RestApi` to `AWS::Lambda::Function`

**Policy type**

`AWS::Lambda::Permission` attached to the `AWS::Lambda::Function`.

**Access categories**

`Write`

```
{
  "Action": "lambda:InvokeFunction",
  "Principal": "apigateway.amazonaws.com",
  "SourceArn": "arn:${AWS::Partition}:execute-api:${AWS::Region}:${AWS::AccountId}:%{Source.ResourceId}/%{Source.Qualifier}"
}
```

`AWS::SNS::Topic` to `AWS::SQS::Queue`

**Policy type**

`AWS::SQS::QueuePolicy` attached to the `AWS::SQS::Queue`.

**Access categories**

`Write`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "sns.amazonaws.com"
      },
      "Resource": "%{Destination.Arn}",
      "Action": "sqs:SendMessage",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "%{Source.Arn}"
        }
      }
    }
  ]
}
```

`AWS::SNS::Topic` to `AWS::Lambda::Function`

**Policy type**

`AWS::Lambda::Permission` attached to the `AWS::Lambda::Function`.

**Access categories**

`Write`

```
{
  "Action": "lambda:InvokeFunction",
  "Principal": "sns.amazonaws.com",
  "SourceArn": "%{Source.Arn}"
}
```

`AWS::SQS::Queue` to `AWS::Lambda::Function`

**Policy type**

[Customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") attached to the `AWS::Lambda::Function` role.

**Access categories**

`Write`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "sqs:DeleteMessage"
      ],
      "Resource": [
        "%{Source.Arn}"
      ]
    }
  ]
}
```

`Read`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "sqs:ReceiveMessage",
        "sqs:GetQueueAttributes"
      ],
      "Resource": [
        "%{Source.Arn}"
      ]
    }
  ]
}
```

`AWS::S3::Bucket` to `AWS::Lambda::Function`

**Policy type**

`AWS::Lambda::Permission` attached to the `AWS::Lambda::Function`.

**Access categories**

`Write`

```
{
  "Action": "lambda:InvokeFunction",
  "Principal": "s3.amazonaws.com",
  "SourceArn": "%{Source.Arn}",
  "SourceAccount": "${AWS::AccountId}"
}
```

`AWS::StepFunctions::StateMachine` to `AWS::Lambda::Function`

**Policy type**

[Customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") attached to the `AWS::StepFunctions::StateMachine` role.

**Access categories**

`Write`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "lambda:InvokeAsync",
        "lambda:InvokeFunction"
      ],
      "Resource": [
        "%{Destination.Arn}"
      ]
    }
  ]
}
```

`AWS::StepFunctions::StateMachine` to `AWS::SNS::Topic`

**Policy type**

[Customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") attached to the `AWS::StepFunctions::StateMachine` role.

**Access categories**

`Write`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "sns:Publish"
      ],
      "Resource": [
        "%{Destination.Arn}"
      ]
    }
  ]
}
```

`AWS::StepFunctions::StateMachine` to `AWS::SQS::Queue`

**Policy type**

[Customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") attached to the `AWS::StepFunctions::StateMachine` role.

**Access categories**

`Write`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "sqs:SendMessage"
      ],
      "Resource": [
        "%{Destination.Arn}"
      ]
    }
  ]
}
```

`AWS::StepFunctions::StateMachine` to `AWS::S3::Bucket`

**Policy type**

[Customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") attached to the `AWS::StepFunctions::StateMachine` role.

**Access categories**

`Read`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:GetObjectAcl",
        "s3:GetObjectLegalHold",
        "s3:GetObjectRetention",
        "s3:GetObjectTorrent",
        "s3:GetObjectVersion",
        "s3:GetObjectVersionAcl",
        "s3:GetObjectVersionForReplication",
        "s3:GetObjectVersionTorrent",
        "s3:ListBucket",
        "s3:ListBucketMultipartUploads",
        "s3:ListBucketVersions",
        "s3:ListMultipartUploadParts"
      ],
      "Resource": [
        "%{Destination.Arn}",
        "%{Destination.Arn}/*"
      ]
    }
  ]
}
```

`Write`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:AbortMultipartUpload",
        "s3:DeleteObject",
        "s3:DeleteObjectVersion",
        "s3:PutObject",
        "s3:PutObjectLegalHold",
        "s3:PutObjectRetention",
        "s3:RestoreObject"
      ],
      "Resource": [
        "%{Destination.Arn}",
        "%{Destination.Arn}/*"
      ]
    }
  ]
}
```

`AWS::StepFunctions::StateMachine` to `AWS::DynamoDB::Table`

**Policy type**

[Customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") attached to the `AWS::StepFunctions::StateMachine` role.

**Access categories**

`Read`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:GetItem",
        "dynamodb:Query",
        "dynamodb:Scan",
        "dynamodb:BatchGetItem",
        "dynamodb:ConditionCheckItem",
        "dynamodb:PartiQLSelect"
      ],
      "Resource": [
        "%{Destination.Arn}",
        "%{Destination.Arn}/index/*"
      ]
    }
  ]
}
```

`Write`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:PutItem",
        "dynamodb:UpdateItem",
        "dynamodb:DeleteItem",
        "dynamodb:BatchWriteItem",
        "dynamodb:PartiQLDelete",
        "dynamodb:PartiQLInsert",
        "dynamodb:PartiQLUpdate"
      ],
      "Resource": [
        "%{Destination.Arn}",
        "%{Destination.Arn}/index/*"
      ]
    }
  ]
}
```

`AWS::StepFunctions::StateMachine` to `AWS::StepFunctions::StateMachine`

**Policy type**

[Customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") attached to the `AWS::StepFunctions::StateMachine` role.

**Access categories**

`Read`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "states:DescribeExecution"
      ],
      "Resource": [
        "arn:${AWS::Partition}:states:${AWS::Region}:${AWS::AccountId}:execution:%{Destination.Name}:*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "events:DescribeRule"
      ],
      "Resource": [
        "arn:${AWS::Partition}:events:${AWS::Region}:${AWS::AccountId}:rule/StepFunctionsGetEventsForStepFunctionsExecutionRule"
      ]
    }
  ]
}
```

`Write`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "states:StartExecution"
      ],
      "Resource": [
        "%{Destination.Arn}"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "states:StopExecution"
      ],
      "Resource": [
        "arn:${AWS::Partition}:states:${AWS::Region}:${AWS::AccountId}:execution:%{Destination.Name}:*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "events:PutTargets",
        "events:PutRule"
      ],
      "Resource": [
        "arn:${AWS::Partition}:events:${AWS::Region}:${AWS::AccountId}:rule/StepFunctionsGetEventsForStepFunctionsExecutionRule"
      ]
    }
  ]
}
```

`AWS::StepFunctions::StateMachine` to `AWS::Events::EventBus`

**Policy type**

[Customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") attached to the `AWS::StepFunctions::StateMachine` role.

**Access categories**

`Write`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "events:PutEvents"
      ],
      "Resource": [
        "%{Destination.Arn}"
      ]
    }
  ]
}

```

`AWS::AppSync::DataSource` to `AWS::DynamoDB::Table`

**Policy type**

[Customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") attached to the `AWS::AppSync::DataSource` role.

**Access categories**

`Read`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:GetItem",
        "dynamodb:Query",
        "dynamodb:Scan",
        "dynamodb:BatchGetItem",
        "dynamodb:ConditionCheckItem",
        "dynamodb:PartiQLSelect"
      ],
      "Resource": [
        "%{Destination.Arn}",
        "%{Destination.Arn}/index/*"
      ]
    }
  ]
}
```

`Write`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:PutItem",
        "dynamodb:UpdateItem",
        "dynamodb:DeleteItem",
        "dynamodb:BatchWriteItem",
        "dynamodb:PartiQLDelete",
        "dynamodb:PartiQLInsert",
        "dynamodb:PartiQLUpdate"
      ],
      "Resource": [
        "%{Destination.Arn}",
        "%{Destination.Arn}/index/*"
      ]
    }
  ]
}
```

`AWS::AppSync::DataSource` to `AWS::Lambda::Function`

**Policy type**

[Customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") attached to the `AWS::AppSync::DataSource` role.

**Access categories**

`Write`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "lambda:InvokeAsync",
        "lambda:InvokeFunction"
      ],
      "Resource": [
        "%{Destination.Arn}",
        "%{Destination.Arn}:*"
      ]
    }
  ]
}
```

`AWS::AppSync::DataSource` to `AWS::Events::EventBus`

**Policy type**

[Customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") attached to the `AWS::AppSync::DataSource` role.

**Access categories**

`Write`

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "events:PutEvents"
      ],
      "Resource": [
        "%{Destination.Arn}"
      ]
    }
  ]
}
```

`AWS::AppSync::GraphQLApi` to `AWS::Lambda::Function`

**Policy type**

`AWS::Lambda::Permission` attached to the `AWS::Lambda::Function`.

**Access categories**

`Write`

```
{
  "Action": "lambda:InvokeFunction",
  "Principal": "appsync.amazonaws.com",
  "SourceArn": "arn:${AWS::Partition}:appsync:${AWS::Region}:${AWS::AccountId}:apis/%{Source.ResourceId}"
}
```
