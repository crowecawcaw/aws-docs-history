# Jobs notifications

The AWS IoT Jobs service publishes MQTT messages to reserved topics when jobs
are pending or when the first job execution in the list changes. Devices can track
pending jobs by subscribing to these topics.

## Job notification types

Job notifications are published to MQTT topics as JSON payloads. There are two
kinds of notifications:

**ListNotification**

A `ListNotification` contains a list of no more than 15 pending job
executions. They are sorted by status (`IN_PROGRESS` job executions
before `QUEUED` job executions) and then by the times when they were
queued.

A `ListNotification` is published whenever one of the following
criteria is met.

- A new job execution is queued or changes to a non-terminal status
  (`IN_PROGRESS` or `QUEUED`).
- An old job execution changes to a terminal status (`FAILED`,
  `SUCCEEDED`, `CANCELED`, `TIMED_OUT`,
  `REJECTED`, or `REMOVED`).

For more information about the limits with and without the scheduling configuration,
see [Job executions limits](job-limits.md#job-execution-limits "job-limits.md#job-execution-limits").

**NextNotification**

- A `NextNotification` contains summary information about the job
  execution that's next in the queue.

A `NextNotification` is published whenever the first job
execution in the list changes.

    + A new job execution is added to the list as `QUEUED`,
     and it's the first one in the list.
    + The status of an existing job execution that wasn't the first one
     in the list changes from `QUEUED` to
     `IN_PROGRESS`, and becomes the first one in the list.
     (This happens when there are no other `IN_PROGRESS` job
     executions in the list or when the job execution whose status
     changes from `QUEUED` to `IN_PROGRESS` was
     queued earlier than any other `IN_PROGRESS` job execution
     in the list.)
    + The status of the job execution that is first in the list changes
     to a terminal status and is removed from the list.

For more information about publishing and subscribing to MQTT topics, see
[Device communication protocols](protocols.md "protocols.md").

###### Note

Notifications are not available when you use HTTP Signature Version 4 or
HTTP TLS to communicate with jobs.

## Job pending

The AWS IoT Jobs service publishes a message on an MQTT topic when a
job is added to or removed from the list of pending job executions
for a thing or the first job execution in the list changes:

- `$aws/things/`thingName`/jobs/notify`
- `$aws/things/`thingName`/jobs/notify-next`

The messages contain the following example payloads:

`$aws/things/`thingName`/jobs/notify`:

```
{
  "timestamp" : 10011,
  "jobs" : {
    "IN_PROGRESS" : [ {
      "jobId" : "other-job",
      "queuedAt" : 10003,
      "lastUpdatedAt" : 10009,
      "executionNumber" : 1,
      "versionNumber" : 1
    } ],
    "QUEUED" : [ {
      "jobId" : "this-job",
      "queuedAt" : 10011,
      "lastUpdatedAt" : 10011,
      "executionNumber" : 1,
      "versionNumber" : 0
    } ]
  }
}
```

If the job execution called `this-job` originated from a job with the
optional scheduling configuration selected and the job document rollout scheduled to
take place during a maintenance window, it'll only appear during a recurring
maintenance window. Outside of a maintenance window, the job called
`this-job` will be excluded from the list of pending job executions
as shown in the following example.

```
{
  "timestamp" : 10011,
  "jobs" : {
    "IN_PROGRESS" : [ {
      "jobId" : "other-job",
      "queuedAt" : 10003,
      "lastUpdatedAt" : 10009,
      "executionNumber" : 1,
      "versionNumber" : 1
    } ],
    "QUEUED" : []
  }
}
```

`$aws/things/`thingName`/jobs/notify-next`:

```
{
  "timestamp" : 10011,
  "execution" : {
    "jobId" : "other-job",
    "status" : "IN_PROGRESS",
    "queuedAt" : 10009,
    "lastUpdatedAt" : 10009,
    "versionNumber" : 1,
    "executionNumber" : 1,
    "jobDocument" : {"c":"d"}
  }
}
```

If the job execution called `other-job` originated from a job with the
optional scheduling configuration selected and the job document rollout scheduled to
take place during a maintenance window, it'll only appear during a recurring
maintenance window. Outside of a maintenance window, the job called
`other-job` won't be listed as the next job execution as shown in the
following example.

```
{} //No other pending jobs
```

```
{
  "timestamp" : 10011,
  "execution" : {
      "jobId" : "this-job",
      "queuedAt" : 10011,
      "lastUpdatedAt" : 10011,
      "executionNumber" : 1,
      "versionNumber" : 0,
      "jobDocument" : {"a":"b"}
  }
} // "this-job" is pending next to "other-job"
```

Possible job execution status values are `QUEUED`,
`IN_PROGRESS`, `FAILED`,
`SUCCEEDED`, `CANCELED`,
`TIMED_OUT`, `REJECTED`, and
`REMOVED`.

The following series of examples show the published notifications to each
topic as job executions are created and changed from one state to another.

First, one job, called `job1`, is created. This
notification is published to the `jobs/notify`
topic:

```
{
  "timestamp": 1517016948,
  "jobs": {
    "QUEUED": [
      {
        "jobId": "job1",
        "queuedAt": 1517016947,
        "lastUpdatedAt": 1517016947,
        "executionNumber": 1,
        "versionNumber": 1
      }
    ]
  }
}
```

This notification is published to the
`jobs/notify-next` topic:

```
{
  "timestamp": 1517016948,
  "execution": {
    "jobId": "job1",
    "status": "QUEUED",
    "queuedAt": 1517016947,
    "lastUpdatedAt": 1517016947,
    "versionNumber": 1,
    "executionNumber": 1,
    "jobDocument": {
      "operation": "test"
    }
  }
}
```

When another job is created (`job2`), this notification
is published to the `jobs/notify` topic:

```
{
  "timestamp": 1517017192,
  "jobs": {
    "QUEUED": [
      {
        "jobId": "job1",
        "queuedAt": 1517016947,
        "lastUpdatedAt": 1517016947,
        "executionNumber": 1,
        "versionNumber": 1
      },
      {
        "jobId": "job2",
        "queuedAt": 1517017191,
        "lastUpdatedAt": 1517017191,
        "executionNumber": 1,
        "versionNumber": 1
      }
    ]
  }
}
```

A notification is not published to the
`jobs/notify-next` topic because the next job in the
queue (`job1`) has not changed. When `job1`
starts to execute, its status changes to `IN_PROGRESS`.
No notifications are published because the list of jobs and the next
job in the queue have not changed.

When a third job (`job3`) is added, this notification
is published to the `jobs/notify` topic:

```
{
  "timestamp": 1517017906,
  "jobs": {
    "IN_PROGRESS": [
      {
        "jobId": "job1",
        "queuedAt": 1517016947,
        "lastUpdatedAt": 1517017472,
        "startedAt": 1517017472,
        "executionNumber": 1,
        "versionNumber": 2
      }
    ],
    "QUEUED": [
      {
        "jobId": "job2",
        "queuedAt": 1517017191,
        "lastUpdatedAt": 1517017191,
        "executionNumber": 1,
        "versionNumber": 1
      },
      {
        "jobId": "job3",
        "queuedAt": 1517017905,
        "lastUpdatedAt": 1517017905,
        "executionNumber": 1,
        "versionNumber": 1
      }
    ]
  }
}
```

A notification is not published to the
`jobs/notify-next` topic because the next job in the
queue is still `job1`.

When `job1` is complete, its status changes to
`SUCCEEDED`, and this notification is published to
the `jobs/notify` topic:

```
{
  "timestamp": 1517186269,
  "jobs": {
    "QUEUED": [
      {
        "jobId": "job2",
        "queuedAt": 1517017191,
        "lastUpdatedAt": 1517017191,
        "executionNumber": 1,
        "versionNumber": 1
      },
      {
        "jobId": "job3",
        "queuedAt": 1517017905,
        "lastUpdatedAt": 1517017905,
        "executionNumber": 1,
        "versionNumber": 1
      }
    ]
  }
}
```

At this point, `job1` has been removed from the queue,
and the next job to be executed is `job2`. This
notification is published to the `jobs/notify-next`
topic:

```
{
  "timestamp": 1517186269,
  "execution": {
    "jobId": "job2",
    "status": "QUEUED",
    "queuedAt": 1517017191,
    "lastUpdatedAt": 1517017191,
    "versionNumber": 1,
    "executionNumber": 1,
    "jobDocument": {
      "operation": "test"
    }
  }
}
```

If `job3` must begin executing before `job2`
(which is not recommended), the status of `job3` can be
changed to `IN_PROGRESS`. If this happens,
`job2` is no longer next in the queue, and this
notification is published to the `jobs/notify-next`
topic:

```
{
  "timestamp": 1517186779,
  "execution": {
    "jobId": "job3",
    "status": "IN_PROGRESS",
    "queuedAt": 1517017905,
    "startedAt": 1517186779,
    "lastUpdatedAt": 1517186779,
    "versionNumber": 2,
    "executionNumber": 1,
    "jobDocument": {
      "operation": "test"
    }
  }
}
```

No notification is published to the `jobs/notify` topic
because no job has been added or removed.

If the device rejects `job2` and updates its status to
`REJECTED`, this notification is published to the
`jobs/notify` topic:

```
{
  "timestamp": 1517189392,
  "jobs": {
    "IN_PROGRESS": [
      {
        "jobId": "job3",
        "queuedAt": 1517017905,
        "lastUpdatedAt": 1517186779,
        "startedAt": 1517186779,
        "executionNumber": 1,
        "versionNumber": 2
      }
    ]
  }
}
```

If `job3` (which is still in progress) is force
deleted, this notification is published to the
`jobs/notify` topic:

```
{
  "timestamp": 1517189551,
  "jobs": {}
}
```

At this point, the queue is empty. This notification is published
to the `jobs/notify-next` topic:

```
{
  "timestamp": 1517189551
}
```
