# Perform DynamoDB CRUD operations with Step Functions

You can integrate Step Functions with DynamoDB to perform CRUD operations on a DynamoDB table. This page lists the supported
DynamoDB APIs and provides an example `Task` state to retrieve an item from DynamoDB.

To learn about integrating with AWS services in Step Functions, see [Integrating services](integrate-services.md "integrate-services.md") and [Passing parameters to a service API in Step Functions](connect-parameters.md "connect-parameters.md").

###### Key features of optimized DynamoDB integration

- There is no specific optimization for the [Request Response](connect-to-resource.md#connect-default "connect-to-resource.md#connect-default") integration pattern.
- [Wait for a Callback with Task Token](connect-to-resource.md#connect-wait-token "connect-to-resource.md#connect-wait-token")
  integration pattern is not supported.
- Only [`GetItem`](../../../amazondynamodb/latest/APIReference/API_GetItem.md "../../../amazondynamodb/latest/APIReference/API_GetItem.md"), [`PutItem`](../../../amazondynamodb/latest/APIReference/API_PutItem.md "../../../amazondynamodb/latest/APIReference/API_PutItem.md"), [`UpdateItem`](../../../amazondynamodb/latest/APIReference/API_UpdateItem.md "../../../amazondynamodb/latest/APIReference/API_UpdateItem.md"), and [`DeleteItem`](../../../amazondynamodb/latest/APIReference/API_DeleteItem.md "../../../amazondynamodb/latest/APIReference/API_DeleteItem.md") API actions are available
  through optimized integration. Other API actions, such as [`CreateTable`](../../../amazondynamodb/latest/APIReference/API_CreateTable.md "../../../amazondynamodb/latest/APIReference/API_CreateTable.md") are available using the
  DynamoDB AWS SDK integration.
  The following is an example `Task` state that retrieves a message from DynamoDB.

```
"Read next Message from DynamoDB": {
    "Type": "Task",
    "Resource": "arn:aws:states:::dynamodb:getItem",
    "Arguments": {
        "TableName": "`DYNAMO_DB_TABLE_NAME`",
        "Key": {
            "MessageId": {"S": "{% $List[0] %}"}
        }
    }
```

To see this state in a working example, see the [Transfer data records with Lambda, DynamoDB,
and Amazon SQS](sample-project-transfer-data-sqs.md "sample-project-transfer-data-sqs.md") starter template.

###### Exception prefix differences

When standard DynamoDB connections experience an error, the exception prefix will be `DynamoDb` (mixed case).

For optimized integrations, the exception prefix will be `DynamoDB` (uppercase `DB`).

###### Quota for input or result data

When sending or receiving data between services, the maximum input or result for a task is 256 KiB of data as a UTF-8 encoded string. See [Quotas related to state
machine executions](service-quotas.md#service-limits-state-machine-executions "service-quotas.md#service-limits-state-machine-executions").

## Optimized DynamoDB APIs

- [`GetItem`](../../../amazondynamodb/latest/APIReference/API_GetItem.md "../../../amazondynamodb/latest/APIReference/API_GetItem.md")
- [`PutItem`](../../../amazondynamodb/latest/APIReference/API_PutItem.md "../../../amazondynamodb/latest/APIReference/API_PutItem.md")
- [`DeleteItem`](../../../amazondynamodb/latest/APIReference/API_DeleteItem.md "../../../amazondynamodb/latest/APIReference/API_DeleteItem.md")
- [`UpdateItem`](../../../amazondynamodb/latest/APIReference/API_UpdateItem.md "../../../amazondynamodb/latest/APIReference/API_UpdateItem.md")

###### Parameters in Step Functions are expressed in PascalCase

Even if the native service API is in camelCase, for example the API action `startSyncExecution`, you specify parameters in PascalCase, such as: `StateMachineArn`.

## IAM policies for calling DynamoDB

The following example templates show how AWS Step Functions generates IAM policies based on the resources in your state machine definition. For more information, see [How Step Functions generates IAM policies for integrated
services](service-integration-iam-templates.md "service-integration-iam-templates.md") and [Discover service integration patterns in Step Functions](connect-to-resource.md "connect-to-resource.md").

_Static resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "dynamodb:GetItem",
 "dynamodb:PutItem",
 "dynamodb:UpdateItem",
 "dynamodb:DeleteItem"
 ],
 "Resource": [
 "arn:aws:dynamodb:`us-east-1`:`123456789012`:table/myTableName"
 ]
 }
 ]
}`

```

_Dynamic resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "dynamodb:GetItem",
 "dynamodb:PutItem",
 "dynamodb:UpdateItem",
 "dynamodb:DeleteItem"
 ],
 "Resource": "*"
 }
 ]
}`

```

For more information about the IAM policies for all DynamoDB API actions, see
[IAM policies with DynamoDB](../../../amazondynamodb/latest/developerguide/using-identity-based-policies.md "../../../amazondynamodb/latest/developerguide/using-identity-based-policies.md") in the
_Amazon DynamoDB Developer Guide_. Additionally, for information about the IAM policies for PartiQL for DynamoDB, see
[IAM policies with PartiQL for DynamoDB](../../../amazondynamodb/latest/developerguide/ql-iam.md "../../../amazondynamodb/latest/developerguide/ql-iam.md") in the
_Amazon DynamoDB Developer Guide_.
