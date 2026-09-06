

# Updating queues
<a name="updating-queue-status"></a>

You can update an existing queue to change its **Name**, **Concurrent jobs**, or **Status**.

Use **Description** to help keep details about your queues.

Use **Concurrent jobs** to specify the maximum number of jobs your queue can process concurrently.

Use **Status** to manage whether a queue is **Active** or **Paused**. New queues default to an **Active** status and are available to process jobs immediately. You can optionally **Pause** a queue to stop processing any additional jobs. When you pause jobs, MediaConvert finishes processing jobs that are already running. If you submit a job to a paused queue, its status will remain in `SUBMITTED` until you change the queue's status back to **Active** or cancel the job. 

The following tabs show how to change the status of an on-demand queue.

------
#### [ Console  ]

To update an on-demand queue by using the MediaConvert console:

1. Open the [Queues](https://console.aws.amazon.com/mediaconvert/home#/queues/list) page in the MediaConvert console.

1. In the **On-demand queues** section, select the queue.

1. Choose **Edit queue**.

1. Change the **Description**, **Concurrent jobs**, or **Status** of your queue.

1. Choose **Save queue**.

------
#### [ AWS CLI  ]

The following `update-queue` example pauses an active on-demand queue.

```
aws mediaconvert update-queue \
	--name {{Queue1}} \
	--status {{PAUSED}}
```

The following `update-queue` example activates a paused on-demand queue.

```
aws mediaconvert update-queue \
	--name {{Queue1}} \
	--status {{ACTIVE}}
```

The following `update-queue` example changes the number of Concurrent jobs for an on-demand queue.

```
aws mediaconvert update-queue \
	--name {{Queue1}} \
	--concurrentJobs {{250}}
```

For more information about how to change the status of an on-demand queue by using the AWS CLI, see the [AWS CLI Command Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/update-queue.html).

------