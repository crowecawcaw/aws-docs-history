

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Event samples
<a name="eventbridge-events"></a>

The following are sample MGN events in EventBridge:

**Topics**
+ [MGN source server launch result](#eventbridge-event-1)
+ [MGN source server lifecycle state change](#eventbridge-event-2)
+ [MGN source server data replication stalled change](#eventbridge-event-3)

## MGN source server launch result
<a name="eventbridge-event-1"></a>

Emitted when a test or cutover instance launch was completed (successfully or with failure).

Possible states (referring to the **state** field within the **details** field):



1. TEST\_LAUNCH\_SUCCEEDED

1. TEST\_LAUNCH\_FAILED

1. CUTOVER\_LAUNCH\_SUCCEEDED

1. CUTOVER\_LAUNCH\_FAILED

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
<a name="eventbridge-event-2"></a>

Emitted when a source server reaches the READY\_FOR\_TEST lifecycle state for the first time.

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

## MGN source server data replication stalled change
<a name="eventbridge-event-3"></a>

Emitted when the data replication state becomes stalled, and when data replication state is no longer stalled (not stalled). 

Possible states (referring to the **state** field within the **details** field):



1. STALLED

1. NOT\_STALLED

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