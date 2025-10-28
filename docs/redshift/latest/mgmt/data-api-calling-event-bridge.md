Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Scheduling Amazon Redshift Data API operations with

Amazon EventBridge

You can create rules that match selected events and route them to targets to take
action. You can also use rules to take action on a predetermined schedule. For more
information, see the [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md").

To schedule Data API operations with EventBridge, the associated IAM role must trust
the principal for CloudWatch Events (events.amazonaws.com). This role should have the equivalent of
the managed policy `AmazonEventBridgeFullAccess` attached. It should also
have `AmazonRedshiftDataFullAccess` policy permissions that are managed by
the Data API. You can create an IAM role with these permissions on the IAM
console. When creating a role on the IAM console, choose the AWS service trusted
entity for CloudWatch Events. Specify the IAM role in the `RoleArn` JSON value in the
EventBridge target. For more information about creating an IAM role, see [Creating a Role for an AWS Service (Console)](../../../IAM/latest/UserGuide/id_roles_create_for-service.md#roles-creatingrole-service-console "../../../IAM/latest/UserGuide/id_roles_create_for-service.md#roles-creatingrole-service-console") in the
_IAM User Guide_.

The `name` of the rule that you create in Amazon EventBridge must match the
`StatementName` in the `RedshiftDataParameters`.

The following examples show variations of creating EventBridge rules with a single or
multiple SQL statements and with an Amazon Redshift cluster or an Amazon Redshift Serverless workgroup as the data
warehouse.

The following example uses the AWS CLI to create an EventBridge rule that is used to
run a SQL statement against an Amazon Redshift cluster.

```
aws events put-rule
--name test-redshift-cluster-data
--schedule-expression "rate(1 minute)"
```

Then an EventBridge target is created to run on the schedule specified in the rule.

```
aws events put-targets
--cli-input-json file://data.json
```

The input data.json file is as follows. The `Sql` JSON key
indicates there is a single SQL statement. The `Arn` JSON value
contains a cluster identifier.
The
`RoleArn` JSON value contains the IAM role used to run the SQL
as described previously.

```
{
    "Rule": "test-redshift-cluster-data",
    "EventBusName": "default",
    "Targets": [
        {
            "Id": "2",
            "Arn": "arn:aws:redshift:us-east-1:123456789012:cluster:mycluster",
            "RoleArn": "arn:aws:iam::123456789012:role/Administrator",
            "RedshiftDataParameters": {
                "Database": "dev",
                "DbUser": "root",
                "Sql": "select 1;",
                "StatementName": "test-redshift-cluster-data",
                "WithEvent": true
            }
        }
    ]
}
```

The following example uses the AWS CLI to create an EventBridge rule that is used to
run a SQL statement against an Amazon Redshift Serverless workgroup.

```
aws events put-rule
--name  test-redshift-serverless-workgroup-data
--schedule-expression "rate(1 minute)"
```

Then an EventBridge target is created to run on the schedule specified in the rule.

```
aws events put-targets
--cli-input-json file://data.json
```

The input data.json file is as follows. The `Sql` JSON key
indicates there is a single SQL statement. The `Arn` JSON value
contains a workgroup name.
The
`RoleArn` JSON value contains the IAM role used to run the SQL
as described previously.

```
{
    "Rule": "test-redshift-serverless-workgroup-data",
    "EventBusName": "default",
    "Targets": [
        {
            "Id": "2",
            "Arn": "arn:aws:redshift-serverless:us-east-1:123456789012:workgroup/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "RoleArn": "arn:aws:iam::123456789012:role/Administrator",
            "RedshiftDataParameters": {
                "Database": "dev",
                "Sql": "select 1;",
                "StatementName": "test-redshift-serverless-workgroup-data",
                "WithEvent": true
            }
        }
    ]
}
```

The following example uses the AWS CLI to create an EventBridge rule that is used to
run multiple SQL statements against an Amazon Redshift cluster.

```
aws events put-rule
--name  test-redshift-cluster-data
--schedule-expression "rate(1 minute)"
```

Then an EventBridge target is created to run on the schedule specified in the rule.

```
aws events put-targets
--cli-input-json file://data.json
```

The input data.json file is as follows. The `Sqls` JSON key
indicates there are multiple SQL statements. The `Arn` JSON value
contains a cluster identifier.
The
`RoleArn` JSON value contains the IAM role used to run the SQL
as described previously.

```
{
    "Rule": "test-redshift-cluster-data",
    "EventBusName": "default",
    "Targets": [
        {
            "Id": "2",
            "Arn": "arn:aws:redshift:us-east-1:123456789012:cluster:mycluster",
            "RoleArn": "arn:aws:iam::123456789012:role/Administrator",
            "RedshiftDataParameters": {
                "Database": "dev",
                "Sqls": ["select 1;", "select 2;", "select 3;"],
                "StatementName": "test-redshift-cluster-data",
                "WithEvent": true
            }
        }
    ]
}
```

The following example uses the AWS CLI to create an EventBridge rule that is used to
run multiple SQL statements against an Amazon Redshift Serverless workgroup.

```
aws events put-rule
--name  test-redshift-serverless-workgroup-data
--schedule-expression "rate(1 minute)"
```

Then an EventBridge target is created to run on the schedule specified in the rule.

```
aws events put-targets
--cli-input-json file://data.json
```

The input data.json file is as follows. The `Sqls` JSON key
indicates there are multiple SQL statements. The `Arn` JSON value
contains a workgroup name.
The
`RoleArn` JSON value contains the IAM role used to run the SQL
as described previously.

```
{
    "Rule": "test-redshift-serverless-workgroup-data",
    "EventBusName": "default",
    "Targets": [
        {
            "Id": "2",
            "Arn": "arn:aws:redshift-serverless:us-east-1:123456789012:workgroup/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "RoleArn": "arn:aws:iam::123456789012:role/Administrator",
            "RedshiftDataParameters": {
                "Database": "dev",
                "Sqls": ["select 1;", "select 2;", "select 3;"],
                "StatementName": "test-redshift-serverless-workgroup-data",
                "WithEvent": true
            }
        }
    ]
}
```
