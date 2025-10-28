NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Event samples

The following are sample MGN events in EventBridge:

###### Topics

- [MGN source server launch result](#eventbridge-event-1 "#eventbridge-event-1")
- [MGN source server lifecycle state change](#eventbridge-event-2 "#eventbridge-event-2")
- [MGN source server data replication stalled
  change](#eventbridge-event-3 "#eventbridge-event-3")

## MGN source server launch result

Emitted when a test or cutover instance launch was completed (successfully or with
failure).

Possible states (referring to the **state** field within
the **details** field):

1. TEST_LAUNCH_SUCCEEDED
2. TEST_LAUNCH_FAILED
3. CUTOVER_LAUNCH_SUCCEEDED
4. CUTOVER_LAUNCH_FAILED

Sample event:

```

{
  "version": "0",
  "id": "9da9af57-9253-4406-87cb-7cc400e43465",
  "detail-type": "MGN Source Server Launch Result",
  "source": "aws.mgn",
  "account": "111122223333",
  "time": "2016-08-22T20:12:19Z",
  "region": "us-west-2",
  "resources": [
    "arn:aws:mgn:us-west-2:111122223333:source-server/s-12345678901234567"
  ],
  "detail": {
    "state": "*TEST_LAUNCH_SUCCEEDED*",     "job-id": "*mgnjob-04ca7d0d3fb6afa3e*"
  }
}

```

## MGN source server lifecycle state change

Emitted when a source server reaches the READY_FOR_TEST lifecycle state for the first time.

Sample event:

```

{
  "version": "0",
  "id": "9da9af57-9253-4406-87cb-7cc400e43465",
  "detail-type": "MGN Source Server Lifecycle State Change",
  "source": "aws.mgn",
  "account": "111122223333",
  "time": "2016-08-22T20:12:19Z",
  "region": "us-west-2",
  "resources": [
    "arn:aws:mgn:us-west-2:111122223333:source-server/s-12345678901234567"
  ],
  "detail": {
     "state": "*READY_FOR_TEST*"
  }
}

```

## MGN source server data replication stalled

change

Emitted when the data replication state becomes stalled, and when data replication state is no longer stalled (not stalled).

Possible states (referring to the **state** field within
the **details** field):

1. STALLED
2. NOT_STALLED

Sample event:

```

{
  "version": "0",
  "id": "9da9af57-9253-4406-87cb-7cc400e43465",
  "detail-type": "MGN Source Server Data Replication Stalled Change",
  "source": "aws.mgn",
  "account": "111122223333",
  "time": "2016-08-22T20:12:19Z",
  "region": "us-west-2",
  "resources": [
    "arn:aws:mgn:us-west-2:111122223333:source-server/s-12345678901234567"
  ],
  "detail": {
     "state": "*STALLED*"
  }
}

```
