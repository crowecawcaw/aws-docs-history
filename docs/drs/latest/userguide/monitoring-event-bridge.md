# Alarm events and EventBridge

## Sample events for Elastic Disaster Recovery

The following are sample events for Elastic Disaster Recovery:

### Source server data replication

status

These events are triggered when source servers' data replication state changes from
Stalled (replication not functioning properly) and not stalled (replication is functioning
as expected).

**STALLED**

```
{
	"version": "0",
	"id": "9da9af57-9253-4406-87cb-7cc400e43465",
	"detail-type": "DRS Source Server Data Replication Stalled Change",
	"source": "aws.drs",
	"account": "111122223333",
	"time": "2016-08-22T20:12:19Z",
	"region": "us-west-2",
	"resources": [
		"arn:aws:drs:us-west-2:111122223333:source-server/s-12345678901234567"
	],
	"detail": {
		"state": "STALLED"
	}
}

```

**NOT_STALLED**

```
{
	"version": "0",
	"id": "9da9af57-9253-4406-87cb-7cc400e43465",
	"detail-type": "DRS Source Server Data Replication Stalled Change",
	"source": "aws.drs",
	"account": "111122223333",
	"time": "2016-08-22T20:12:19Z",
	"region": "us-west-2",
	"resources": [
		"arn:aws:drs:us-west-2:111122223333:source-server/s-12345678901234567"
	],
	"detail": {
		"state": "NOT_STALLED"
	}
}

```

### Source server launch

result

These events are triggered when a drill or recovery instance is launched for a source
server and indicate whether the launch succeeded or failed.

**RECOVERY_LAUNCH_SUCCEEDED**

```

{
    "version": "0",
    "id": "9da9af57-9253-4406-87cb-7cc400e43465",
    "detail-type": "DRS Source Server Launch Result",
    "source": "aws.drs",
    "account": "111122223333",
    "time": "2016-08-22T20:12:19Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:drs:us-west-2:111122223333:source-server/s-12345678901234567"
    ],
    "detail": {
        "state": "RECOVERY_LAUNCH_SUCCEEDED",
        "job-id": "drsjob-04ca7d0d3fb6afa3e",
        "is-drill": "FALSE"
    }
}

```

**RECOVERY_LAUNCH_FAILED**

```

{
    "version": "0",
    "id": "9da9af57-9253-4406-87cb-7cc400e43465",
    "detail-type": "DRS Source Server Launch Result",
    "source": "aws.drs",
    "account": "111122223333",
    "time": "2016-08-22T20:12:19Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:drs:us-west-2:111122223333:source-server/s-12345678901234567"
    ],
    "detail": {
        "state": "RECOVERY_LAUNCH_FAILED",
        "job-id": "drsjob-04ca7d0d3fb6afa3e",
        "is-drill": "FALSE"
    }
}

```

### Recovery instance failback

State Change

These events are triggered as part of the failback process and indicate if failback is
in progress, completed or failed.

**FAILBACK_IN_PROGRESS**

```

{
    "version": "0",
    "id": "9da9af57-9253-4406-87cb-7cc400e43465",
    "detail-type": "DRS Recovery Instance Failback State Change",
    "source": "aws.drs",
    "account": "111122223333",
    "time": "2016-08-22T20:12:19Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:drs:us-west-2:111122223333:recovery-instance/ri-12345678901234567"
    ],
    "detail": {
    "state": "FAILBACK_IN_PROGRESS"
    }
}

```

**FAILBACK_COMPLETED**

```

{
    "version": "0",
    "id": "9da9af57-9253-4406-87cb-7cc400e43465",
    "detail-type": "DRS Recovery Instance Failback State Change",
    "source": "aws.drs",
    "account": "111122223333",
    "time": "2016-08-22T20:12:19Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:drs:us-west-2:111122223333:recovery-instance/ri-12345678901234567"
    ],
    "detail": {
        "state": "FAILBACK_COMPLETED"
    }
}

```

**FAILBACK_ERROR**

```

{
    "version": "0",
    "id": "9da9af57-9253-4406-87cb-7cc400e43465",
    "detail-type": "DRS Recovery Instance Failback State Change",
    "source": "aws.drs",
    "account": "111122223333",
    "time": "2016-08-22T20:12:19Z",
    "region": "us-west-2",
    "resources": [
        "arn:aws:drs:us-west-2:111122223333:recovery-instance/ri-12345678901234567"
    ],
    "detail": {
    "state": "FAILBACK_ERROR"
    }
}

```

### PIT Snapshot Taken

This event is triggered whenever a point in time snapshot is taken and includes its
identifiers.

**PIT Snapshot Taken**

```

{
    "account": "111122223333",
    "detail": {
        "DrsSnapshotID": "112233",
        "EbsSnapshotIDs": "445566,778899"
    },
    "detail-type": "DRS PIT Snapshot Taken",
    "id": "9da9af57-9253-4406-87cb-7cc400e43465",
    "region": "us-west-2",
    "resources": [
        "arn:aws:drs:us-west-2:111122223333:source-server/s-12345678901234567"
    ],
    "source": "aws.drs",
    "time": "2016-08-22T20:12:19Z",
    "version": "0"
}

```

## Registering event rules

You create EventBridge rules that capture events coming from your Elastic Disaster Recovery resources.

###### Note

When you use the AWS Management Console to create an event rule, the console automatically adds the IAM
permissions necessary to grant EventBridge Event permissions to call your desired target type. If
you are creating an event rule using the AWS CLI, you must grant permissions explicitly. For
more information, see [Event Patterns](../../../eventbridge/latest/userguide/eb-event-patterns.md "../../../eventbridge/latest/userguide/eb-event-patterns.md") in the*Amazon EventBridge User Guide*.

###### To create Amazon EventBridge rules

1.  Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2.  Using the following values, create an EventBridge rule that captures events coming from Elastic Disaster Recovery
    resources:

        * For **Rule type**, choose **Rule with an event
         pattern**.
        * For **Event source**, choose **Other**.
        * For **Event pattern**, choose **Custom patterns (JSON
         editor)**, and paste one of the following event pattern examples into the
         text area:





        	+ To catch all Elastic Disaster Recovery events:



        	```
        	{
        		"source": [
        			"aws.drs"
        		]
        	}

        	```
        	+ To catch all Recovery instance failback state changes:



        	```
        	{
        		"detail-type": [
        			"DRS Recovery Instance Failback State Change"
        		],
        		"source": [
        			"aws.drs"
        		]
        	}
        	```
        	+ To catch all events relating to a given Source server:



        	```
        	{
        		"source": [
        			"aws.drs"
        		],
        		"resources": [
        			"arn:aws:drs:us-west-2:111122223333:source-server/s-12345678901234567"
        		]
        	}
        	```
        * For **Target types**, choose**AWS service**, and
         for
         **Select a target**
         choose your desired target.

    For details about creating rules, see
    [Creating Amazon EventBridge rules that react
    to events](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md")
    in the**Amazon EventBridge User Guide**.
