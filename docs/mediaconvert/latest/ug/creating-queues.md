# Creating a queue

AWS Elemental MediaConvert provides a default on-demand queue. A default queue is available in all
AWS Regions. Other queues appear only in the AWS Region where they are created. To add
additional resources to your account, you can create your own on-demand queues.

To learn how queues affect the way that MediaConvert allocates the processing of
resources, see [Processing multiple jobs in parallel](working-with-on-demand-queues.md#queue-resources "working-with-on-demand-queues.md#queue-resources") . The
following tabs show different options for creating an on-demand queue.

Console
To create an on-demand queue by using the MediaConvert
console:

1. Open the [Queues](https://console.aws.amazon.com/mediaconvert/home#/queues/list "https://console.aws.amazon.com/mediaconvert/home#/queues/list")
   page in the MediaConvert console.
2. Choose **Create queue**.
3. Enter a **Name**. Then optionally enter a
   **Description** and any
   **Tags**.
4. Optionally enter a value for **Concurrent jobs**.
5. Choose **Create queue**.

AWS CLI
The following `create-queue` example creates a new on-demand queue with 100
concurrent jobs.

```
aws mediaconvert create-queue \
	--region `region-name-1` \
	--name `Queue1` \
	--description `"Example queue description."` \
	--concurrentJobs `"100"` \
	--tags `"KeyName1=string1,KeyName2=string2"`
```

For more information about how to create an on-demand queue by using
the AWS CLI, see the [AWS CLI Command Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/create-queue.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/create-queue.html").
