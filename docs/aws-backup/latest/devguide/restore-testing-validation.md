# Restore testing validation

You have the option of creating an event-driven validation that runs when a restore
testing job completes.

First, create a validation workflow with any target supported by Amazon EventBridge, such as
AWS Lambda. Second, add an EventBridge rule that listens for the restore job reaching the status
`COMPLETED`. Third, create a restore testing plan (or let an existing one run
as scheduled). Finally, after the restore test has finished, monitor the logs of the
validation workflow to ensure it ran as expected (once validation has run, a validation
status will display in the [AWS Backup
console](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup")).

1. ###### Set up validation workflow

You can set up a validation workflow using Lambda or any other target supported by
EventBridge. For example, if you are validating a restore test containing an Amazon EC2 instance,
you may include code that pings a healthcheck endpoint.

You can use the details in the event to determine which resource(s) to
validate.

You can use [Lambda layers](../../../lambda/latest/dg/chapter-layers.md "../../../lambda/latest/dg/chapter-layers.md") to use the
latest SDK (because `PutRestoreValidationResult` is not available
through the Lambda SDK).

Here is a sample:

```
import { Backup } from "@aws-sdk/client-backup";

export const handler = async (event) => {
  console.log("Handling event: ", event);

  const restoreTestingPlanArn = event.detail.restoreTestingPlanArn;
  const resourceType = event.detail.resourceType;
  const createdResourceArn = event.detail.createdResourceArn;

  // TODO: Validate the resource

  const backup = new Backup();
  const response = await backup.putRestoreValidationResult({
    RestoreJobId: event.detail.restoreJobId,
    ValidationStatus: "SUCCESSFUL", // TODO
    ValidationStatusMessage: "" // TODO
  });

  console.log("PutRestoreValidationResult: ", response);
  console.log("Finished");
};
```

2. ###### Add an EventBridge rule

[Create an
EventBridge rule](../../../eventbridge/latest/userguide/eb-get-started.md#eb-gs-create-rule "../../../eventbridge/latest/userguide/eb-get-started.md#eb-gs-create-rule") that listens for the restore job [`COMPLETED` event](eventbridge.md#monitoring-events-in-eventbridge "eventbridge.md#monitoring-events-in-eventbridge").

Optionally, you can filter events by resource type or restore testing plan ARN. Set
the target of this rule to invoke the validation workflow you defined in Step 1. Here is
an example:

```
{
  "source":[
    "aws.backup"
  ],
  "detail-type":[
    "Restore Job State Change"
  ],
  "detail":{
    "resourceType":[
      "..."
    ],
    "restoreTestingPlanArn":[
      "..."
    ],
    "status":[
      "COMPLETED"
    ]
  }
}
```

3. ###### Let the restore testing plan run and complete

The restore testing plan will run according to the schedule you have
configured.

See [Create a
restore testing plan](restore-testing.md#restore-testing-create "restore-testing.md#restore-testing-create") if you do not yet have one or [Update a
restore testing plan](restore-testing.md#restore-testing-update "restore-testing.md#restore-testing-update") if you wish to change the settings. 4. ###### Monitor the results

Once a restore testing plan has run as scheduled, you can check the logs of your
validation workflow to ensure it ran correctly.

You can call the API `PutRestoreValidationResult` to post the results,
which will then be viewable in the [AWS Backup
console](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup") and through AWS Backup API calls that describe and list restore jobs, such
as `DescribeRestoreJob` or `ListRestoreJob`.

Once a validation status is set, it cannot be changed.
