# Using EventBridge with AWS HealthOmics

HealthOmics sends events to Amazon EventBridge when resources change status. Resources include import jobs, export jobs, resource
shares, workflows, tasks, and runs. For each type of resource, there is a list of status changes that generate an
event.

An event bus is a router that receives events and delivers them to destinations. Your account includes a default
event bus that automatically receives events from AWS services. You can create additional custom event buses.

You create EventBridge rules to specify the actions to take when the event bus receives events. For example, you can
create a rule that notifies you about status changes for a resource.

Common scenarios for using events include:

- To monitor when a user shares a resource with you or revokes the share.
- To monitor whether a run fails or completes successfully.
  For more information about using EventBridge, see [What is Amazon EventBridge?](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md")

###### Topics

- [Set up EventBridge for HealthOmics](#eventbridge-setup-events "#eventbridge-setup-events")
- [EventBridge events in HealthOmics](#eventbridge-healthomics-events "#eventbridge-healthomics-events")
- [Event message structure](#eventbridge-message-structure "#eventbridge-message-structure")
- [Event message examples](#eventbridge-cli-examples "#eventbridge-cli-examples")

## Set up EventBridge for HealthOmics

Before you can monitor for EventBridge events, create an EventBridge bus and create rules for the events of interest.

### Configure an EventBridge bus

You can use the default event bus for your AWS account or configure a custom event bus. To configure a
custom event bus, follow these steps:

1. Open the EventBridge console: [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the left navigation, choose **Event buses**.
3. Choose **Create event bus**.
4. In the **Create event bus** form, enter a name for the bus.
5. Choose **Create** to create the bus.

### Create an EventBridge rule

The following procedure shows how to create a simple rule. For more information about rules, see [Rules in EventBridge](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md").

1. Open the EventBridge console: [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the left navigation, choose **Rules**.
3. Choose **Create rule**. The console opens the **Create rule**
   form.
4. In **Define rule detail**, provide a name for the rule.
   - For **Name**, enter a name for the bus.
   - For **Event bus**, select the bus for this rule.
   - Choose **Next**.

5. In **Build event pattern**, under **Event source** select
   **AWS events or EventBridge partner events**.
6. Scroll down to **Event pattern**.
   1. For **Event source**, select **AWS services**.
   2. For **AWS service**, enter
      **omics** in the text filter and select **AWS HealthOmics** as the service.
   3. For **Event type** select the event of interest (or **All events**).
   4. Choose **Next**.

7. In **Select target(s)**, select a target for the event. For example, choose
   **AWS service**, the chose **CloudWatch log group**, and configure a log group.

For many target types, EventBridge
needs permission to send events to the target. The console creates these permissions for you. 8. (Optional) In **Configure tags**, associate tags with the rule. 9. In **Review and update**, review the configuration and choose **Create rule**.

## EventBridge events in HealthOmics

The following table lists the events that HealthOmics sends to EventBridge, and the list of possible status values for the
event.

| Event name                            | Possible status values                                                              |
| ------------------------------------- | ----------------------------------------------------------------------------------- |
| Annotation Import Job Status Change   | Submitted, in progress, cancelled, completed, failed, or completed with<br>failures |
| Annotation Store Share Status Change  | Pending, activating, active, deleting, deleted, failed                              |
| Annotation Store Status Change        | Creating, created, updating, updated, deleting, deleted, or creation<br>failed      |
| Read Set Activation Job Status Change | Submitted, in progress, completed, failed, or completed with<br>failures            |
| Read Set Export Job Status Change     | Submitted, in progress, completed, failed, or completed with<br>failures            |
| Read Set Import Job Status Change     | Submitted, in progress, completed, failed, or completed with<br>failures            |
| Read Set Status Change                | Processing upload, upload failed, active, archived, activating, or<br>deleted       |
| Reference Import Job Status Change    | Submitted, in progress, completed, failed, or completed with<br>failures            |
| Reference Status Change               | Active or deleted                                                                   |
| Reference Store Status Change         | Created, updated, active, or deleted                                                |
| Run Status Change                     | Pending, starting, running, stopping, completed, deleted, failed, or<br>cancelled   |
| Sequence Store Status Change          | Created, updated, active, or deleted                                                |
| Task Status Change                    | Pending, starting, running, stopping, completed, deleted, failed, or<br>cancelled   |
| Variant Import Job Status Change      | Submitted, in progress, cancelled, completed, failed, or completed with<br>failures |
| Variant Store Share Status Change     | Pending, activating, active, deleting, deleted, failed                              |
| Variant Store Status Change           | Creating, created, updating, updated, deleting, deleted, or creation<br>failed      |
| Workflow Share Status Change          | Pending, activating, active, deleting, deleted, failed                              |
| Workflow Status Change                | Creation success, creation failure, deletion success, or deletion failure           |

## Event message structure

HealthOmics provides best effort delivery to send state change event messages to EventBridge. The event is an object with
JSON structure that also contains metadata details. You can use the metadata as input to either recreate the event
or to learn more information. Events include the following fields:

- `version` — Currently 0 (zero) for all events.
- `id` — A Version 4 UUID generated for every event.
- `detail-type` — The type of event that's being sent.
- `account` — The 12-digit AWS account ID of the bucket
  owner.
- `source` — Identifies the service that generated the event.
- `time` — The time the event occurred.
- `region` — Identifies the AWS Region of the bucket.
- `resources` — A JSON array that contains the Amazon Resource
  Name (ARN) of the bucket.
- `detail` — A JSON object that contains information about the
  event.

Run events include the following fields:

- `uuid` — The universally unique identifier for the run.
- `workflowId` — Workflow identifier of the workflow associated with this run.
- `workflowName` — Name of the workflow associated with this run..
- `runId` — Run identifier.
- `runName` — Run name.
- `runOutputUri` — The URI for where the run will write its output data.

## Event message examples

The following example is an event for a change in run status, showing the additional fields.

```
{
    "version":"0",
    "id":"c0e540f4-df38-b986-86c1-3e3730f971fe",
    "detail-type":"Run Status Change",
    "source":"aws.omics",
    "account":"123456789012",
    "time":"2022-10-20T22:07:35Z",
    "region":"us-west-2",
    "resources":[
        "arn:aws:omics:us-west-2:123456789012:run/2101313"
    ],
    "detail":{
        "omicsVersion":"1.0.0",
        "arn":"arn:aws:omics:us-west-2:123456789012:run/2101313",
        "status":"COMPLETED",
        "uuid":"153893cd-097a-40ec-aec7-838a97cd2b21",
        "runId": "1234567",
        "runName": "run name",
        "runOutputUri": "s3://amzn-s3-demo-bucket/run-output/2101313",
        "workflowId": "1234567",
        "workflowName": "workflow name"
    }
}
```

The following example is an event for a change in task status.

```
{
    "version": "0",
    "id": "718d6817-c868-26d3-8ef0-0dc9b2ac73f4",
    "detail-type": "Task Status Change",
    "source": "aws.omics",
    "account": "123456789012",
    "time": "2024-10-30T09:05:44Z",
    "region": "us-west-2",
    "resources": ["arn:aws:omics:us-west-2:123456789012:task/8888888"],
    "detail": {
        "omicsVersion": "1.0.0",
        "arn": "arn:aws:omics:us-west-2:123456789012:task/8888888",
        "status": "COMPLETED",
        "runArn": "arn:aws:omics:us-west-2:123456789012:run/2101313",
        "runUuid": "153893cd-097a-40ec-aec7-838a97cd2b21",
        "runId": "1234567",
        "runName": "run name",
        "workflowId": "1234567",
        "workflowName": "workflow name"
    }
}
```

The following is an example of an event for a read set status change.

```
{
  "version": "0",
  "id": "64ca0eda-9751-dc55-c41a-1bd50b4fc9b7",
  "detail-type": "Read Set Status Change",
  "source": "aws.omics",
  "account": "123456789012",
  "time": "2023-04-04T17:53:06Z",
  "region": "us-west-2",
  "resources": ["arn:aws:omics:us-west-2:123456789012:sequenceStore/1234567890/readSet/3456789012"],
  "detail": {
     "omicsVersion": "1.0.0",
     "arn": "arn:aws:omics:us-west-2:123456789012:sequenceStore/1234567890/readSet/3456789012",
     "sequenceStoreId" : "1234567890",
     "id": "3456789012",
     "status": "PROCESSING_UPLOAD"
  }
}
```

A similar event gets created for a variant store import job.

```
{
    "version": "0",
    "id": "6a7e8feb-b491-4cf7-a9f1-bf3703467718",
    "detail-type": "Variant Store Status Change",
    "source": "aws.omics",
    "account": "123456789012",
    "time": "2015-12-22T18:43:48Z",
    "region": "us-east-1",
    "resources": ["arn:aws:omics:us-east-1:123456789012:myvariantstore2"],
    "detail": {
       "omicsVersion": "1.0.0",
       "arn": "arn:aws:omics:us-east-1:123456789012:myvariantstore2",
       "status": "CREATED",
       "storeId": "6710c5f02610",
       "storeName": "myvariantstore2"
    }
}
```

The following is an event for a change in import job status.

```
{
    "version": "0",
    "id": "6a7e8feb-b491-4cf7-a9f1-bf3703467718",
    "detail-type": "Variant Import Job Status Change",
    "source": "aws.omics",
    "account": "123456789012",
    "time": "2015-12-22T18:43:48Z",
    "region": "us-east-1",
    "resources": ["arn:aws:omics:us-east-1:123456789012:my_variant_store/b64ea9a3-459f-4b68-92c3-3ddb83209fe9"],
    "detail": {
       "omicsVersion": "1.0.0",
       "arn": "arn:aws:omics:us-east-1:123456789012:my_variant_store/b64ea9a3-459f-4b68-92c3-3ddb83209fe9",
       "status": "COMPLETED",
       "jobId": "b64ea9a3-459f-4b68-92c3-3ddb83209fe9",
       "storeId": "a74869f91e20",
       "storeName": "my_variant_store"
    }
}
```
