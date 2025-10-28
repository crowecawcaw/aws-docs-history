# Using pseudo parameters

when registering maintenance window tasks

When you register a task in Maintenance Windows, a tool in AWS Systems Manager, you specify the parameters
that are unique to each of the four task types. (In CLI commands, these are provided
using the `--task-invocation-parameters` option.)

You can also reference certain values using _pseudo
parameter_ syntax, such as `{{RESOURCE_ID}}`,
`{{TARGET_TYPE}}`, and `{{WINDOW_TARGET_ID}}`. When the
maintenance window task runs, it passes the correct values instead of the pseudo
parameter placeholders. The full list of pseudo parameters you can use is provided later
in this topic in [Supported pseudo parameters](#pseudo-parameters "#pseudo-parameters").

###### Important

For the target type `RESOURCE_GROUP`, depending on the ID format needed
for the task, you can choose between using `{{TARGET_ID}}` and
`{{RESOURCE_ID}}` to reference the resource when your task runs.
`{{TARGET_ID}}` returns the full ARN of the resource.
`{{RESOURCE_ID}}` returns only a shorter name or ID of the resource,
as shown in these examples.

- `{{TARGET_ID}}` format:
  `arn:aws:ec2:us-east-1:123456789012:instance/i-02573cafcfEXAMPLE`
- `{{RESOURCE_ID}}` format: `i-02573cafcfEXAMPLE`
  For target type `INSTANCE`, both the
  `{{TARGET_ID}}` and `{{RESOURCE_ID}}` parameters yield the
  instance ID only. For more information, see [Supported pseudo parameters](#pseudo-parameters "#pseudo-parameters").

`{{TARGET_ID}}` and `{{RESOURCE_ID}}` can be used to pass
IDs of AWS resources only to Automation, Lambda, and Step Functions tasks. These two pseudo
parameters can't be used with Run Command tasks.

## Pseudo parameter examples

Suppose that your payload for an AWS Lambda task needs to reference an instance by
its ID.

Whether you’re using an `INSTANCE` or a `RESOURCE_GROUP`
maintenance window target, this can be achieved by using the
`{{RESOURCE_ID}}` pseudo parameter. For example:

```
"TaskArn": "arn:aws:lambda:us-east-2:111122223333:function:SSMTestFunction",
    "TaskType": "LAMBDA",
    "TaskInvocationParameters": {
        "Lambda": {
            "ClientContext": "ew0KICAi--truncated--0KIEXAMPLE",
            "Payload": "{ \"instanceId\": \"{{RESOURCE_ID}}\" }",
            "Qualifier": "$LATEST"
        }
    }
```

If your Lambda task is intended to run against another supported target type in
addition to Amazon Elastic Compute Cloud (Amazon EC2) instances, such as an Amazon DynamoDB table, the same syntax
can be used, and `{{RESOURCE_ID}}` yields the name of the table only.
However, if you require the full ARN of the table, use `{{TARGET_ID}}`,
as shown in the following example.

```
"TaskArn": "arn:aws:lambda:us-east-2:111122223333:function:SSMTestFunction",
    "TaskType": "LAMBDA",
    "TaskInvocationParameters": {
        "Lambda": {
            "ClientContext": "ew0KICAi--truncated--0KIEXAMPLE",
            "Payload": "{ \"tableArn\": \"{{TARGET_ID}}\" }",
            "Qualifier": "$LATEST"
        }
    }
```

The same syntax works for targeting instances or other resource types. When
multiple resource types have been added to a resource group, the task runs against
each of the appropriate resources.

###### Important

Not all resource types that might be included in a resource group yield a
value for the `{{RESOURCE_ID}}` parameter. For a list of supported
resource types, see [Supported pseudo parameters](#pseudo-parameters "#pseudo-parameters").

As another example, to run an Automation task that stops your EC2 instances, you
specify the `AWS-StopEC2Instance` Systems Manager document (SSM document) as the
`TaskArn` value and use the `{{RESOURCE_ID}}` pseudo
parameter:

```
"TaskArn": "AWS-StopEC2Instance",
    "TaskType": "AUTOMATION"
    "TaskInvocationParameters": {
        "Automation": {
            "DocumentVersion": "1",
            "Parameters": {
                "instanceId": [
                    "{{RESOURCE_ID}}"
                ]
            }
        }
    }
```

To run an Automation task that copies a snapshot of an Amazon Elastic Block Store (Amazon EBS) volume,
you specify the `AWS-CopySnapshot` SSM document as the
`TaskArn` value and use the `{{RESOURCE_ID}}` pseudo
parameter.

```
"TaskArn": "AWS-CopySnapshot",
    "TaskType": "AUTOMATION"
    "TaskInvocationParameters": {
        "Automation": {
            "DocumentVersion": "1",
            "Parameters": {
                "SourceRegion": "us-east-2",
                "targetType":"RESOURCE_GROUP",
                "SnapshotId": [
                    "{{RESOURCE_ID}}"
                ]
            }
        }
    }
```

## Supported pseudo parameters

The following list describes the pseudo parameters that you can specify using the
`{{`PSEUDO_PARAMETER`}}` syntax in the
`--task-invocation-parameters` option.

- **`WINDOW_ID`**: The ID of the
  target maintenance window.
- **`WINDOW_TASK_ID`**: The ID of
  the window task that is running.
- **`WINDOW_TARGET_ID`**: The ID of
  the window target that includes the target (target ID).
- **`WINDOW_EXECUTION_ID`**: The ID
  of the current window execution.
- **`TASK_EXECUTION_ID`**: The ID of
  the current task execution.
- **`INVOCATION_ID`**: The ID of the
  current invocation.
- **`TARGET_TYPE`**: The type of
  target. Supported types include `RESOURCE_GROUP` and
  `INSTANCE`.
- **`TARGET_ID`**:

If the target type you specify is `INSTANCE`, the
`TARGET_ID` pseudo parameter is replaced by the ID of the
instance. For example, `i-078a280217EXAMPLE`.

If the target type you specify is `RESOURCE_GROUP`, the value
referenced for the task execution is the full ARN of the resource. For
example:
`arn:aws:ec2:us-east-1:123456789012:instance/`i-078a280217EXAMPLE``.
 The following table provides sample `TARGET_ID` values for
particular resource types in a resource group.

###### Note

`TARGET_ID` isn't supported for Run Command tasks.

| Resource type               | Example TARGET_ID                                                                        |
| --------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AWS::CloudWatch::Alarm`    | `arn:aws:cloudwatch:us-east-1:123456789012:alarm:MyCloudWatchAlarm`i-078a280217EXAMPLE`` |
| `AWS::DynamoDB::Table`      | `arn:aws:dynamodb:us-east-1:123456789012:table/MyTable`                                  |
| `AWS::EC2::Instance`        | `arn:aws:ec2:us-east-1:123456789012:instance/`i-078a280217EXAMPLE``                      |
| `AWS::EC2::Image`           | `arn:aws:ec2:us-east-1:123456789012:image/ami-02250b3732EXAMPLE`                         |
| `AWS::EC2::SecurityGroup`   | `arn:aws:ec2:us-east-1:123456789012:security-group/sg-cEXAMPLE`                          |
| `AWS::EC2::Snapshot`        | `arn:aws:ec2:us-east-1:123456789012:snapshot/snap-03866bf003EXAMPLE`                     |
| `AWS::EC2::Volume`          | `arn:aws:ec2:us-east-1:123456789012:volume/vol-0912e04d78EXAMPLE`                        |
| `AWS::ECS::Service`         | `arn:aws:ecs:us-east-1:123456789012:service/my-ecs-service`                              |
| `AWS::RDS::DBCluster`       | `arn:aws:rds:us-east-2:123456789012:cluster:My-Cluster`                                  |
| `AWS::RDS::DBInstance`      | `arn:aws:rds:us-east-1:123456789012:db:My-SQL-Instance`                                  |
| `AWS::S3::Bucket`           | `arn:aws:s3:::amzn-s3-demo-bucket`                                                       |
| `AWS::SSM::ManagedInstance` | `arn:aws:ssm:us-east-1:123456789012:managed-instance/mi-0feadcf2d9EXAMPLE`               | <br>• **`RESOURCE_ID`**: The short ID of a resource type contained in a resource group. The following table provides sample `RESOURCE_ID` values for particular resource types in a resource group. ###### Note `RESOURCE_ID` isn't supported for Run Command tasks.                                                                                                                              |
| Resource type               | Example RESOURCE_ID                                                                      |
| ---                         | ---                                                                                      |
| `AWS::CloudWatch::Alarm`    | `MyCloudWatchAlarm`                                                                      |
| `AWS::DynamoDB::Table`      | `MyTable`                                                                                |
| `AWS::EC2::Instance`        | `i-078a280217EXAMPLE`                                                                    |
| `AWS::EC2::Image`           | `ami-02250b3732EXAMPLE`                                                                  |
| `AWS::EC2::SecurityGroup`   | `sg-cEXAMPLE`                                                                            |
| `AWS::EC2::Snapshot`        | `snap-03866bf003EXAMPLE`                                                                 |
| `AWS::EC2::Volume`          | `vol-0912e04d78EXAMPLE`                                                                  |
| `AWS::ECS::Service`         | `my-ecs-service`                                                                         |
| `AWS::RDS::DBCluster`       | `My-Cluster`                                                                             |
| `AWS::RDS::DBInstance`      | `My-SQL-Instance`                                                                        |
| `AWS::S3::Bucket`           | `amzn-s3-demo-bucket`                                                                    |
| `AWS::SSM::ManagedInstance` | `mi-0feadcf2d9EXAMPLE`                                                                   | ###### Note If the AWS resource group you specify includes resource types that don't yield a `RESOURCE_ID` value, and aren't listed in the preceding table, then the `RESOURCE_ID` parameter isn't populated. An execution invocation will still occur for that resource. In these cases, use the `TARGET_ID` pseudo parameter instead, which will be replaced with the full ARN of the resource. |
