# Amazon Kinesis Video Streams Edge Agent FAQ

The following are some common questions for the Amazon Kinesis Video Streams Edge Agent service.

## What operating systems does Amazon Kinesis Video Streams Edge Agent

support?

Amazon Kinesis Video Streams Edge Agent currently supports the following operating systems:

**Ubuntu**

- 22.x
  - AMD64

- 18.x
  - ARM

**AL2**

- amzn2
  - AMD64 amazonlinux:2.0.20210219.0-amd64 (Snowball)

## Does the Amazon Kinesis Video Streams Edge Agent support H.265

media?

Amazon Kinesis Video Streams Edge Agent only supports H.264 elementary streams.

## Does the Amazon Kinesis Video Streams Edge Agent work in AL2?

Yes.

## How can I run multiple streams within

the AWS IoT thing or device?

Send another [StartEdgeConfigurationUpdate](API_StartEdgeConfigurationUpdate.md "API_StartEdgeConfigurationUpdate.md") to the same
`HubDeviceArn`, but different
Amazon Kinesis Video Streams/AWS Secrets Manager ARNs.

## How can I edit a

`StartEdgeConfigurationUpdate` after it has been sent?

Send an updated [StartEdgeConfigurationUpdate](API_StartEdgeConfigurationUpdate.md "API_StartEdgeConfigurationUpdate.md")to the same
`HubDeviceArn` with the same Amazon Kinesis Video Streams ARN. When the application
receives the message from Amazon Kinesis Video Streams, it overrides the previous configuration for
that stream. Changes will take place then.

## Do you have any examples of common

`ScheduleConfigs`?

The Amazon Kinesis Video Streams Edge Agent uses the system time of the device that it's running
on.

| Description                             | ScheduleExpression           | DurationInSeconds |
| --------------------------------------- | ---------------------------- | ----------------- |
| 24/7 recording, hourly uploading        | `(null ScheduleConfig)`      |
| 9:00:00 AM<br>• 4:59:59 PM every day    | `0 0 9-16<br>• ? *`          | 3599              |
| 9:00:00 AM<br>• 4:59:59 PM weekdays     | `0 0 9-16 ?<br>• 2-6 *`      | 3599              |
| `0 0 9-16 ?<br>• 2,3,4,5,6 *`           | 3599                         |
| `0 0 9-16 ?<br>• MON-FRI *`             | 3599                         |
| `0 0 9-16 ?<br>• MON,TUE,WED,THU,FRI *` | 3599                         |
| 9:00:00 AM<br>• 4:59:59 PM weekends     | `0 0 9-16 ?<br>• SAT,SUN *`  | 3599              |
| 10:00:00 PM<br>• 11:59:59 PM weekdays   | `0 0 22,23 ?<br>• MON-FRI *` | 3599              |
| 9:00:00 AM<br>• 10:00:00 AM every day   | `0 0 9<br>• ? *`             | 3600              |
| 4:00:00 PM<br>• 5:59:59 PM every day    | `0 0 16-17<br>• ? *`         | 3599              |

For more examples, see the [Quartz documentation](https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html "https://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html").

## Is there a maximum stream limit?

The Amazon Kinesis Video Streams Edge Agent currently has a hard limit of 16 streams per device. Use the
[DeleteEdgeConfiguration](API_DeleteEdgeConfiguration.md "API_DeleteEdgeConfiguration.md") API to delete streams from a
device. Updating a configuration for the same stream using the [StartEdgeConfigurationUpdate](API_StartEdgeConfigurationUpdate.md "API_StartEdgeConfigurationUpdate.md") does not increase the device’s
stream count.

## How do I restart a job that has errored

out?

If an error is encountered, the Amazon Kinesis Video Streams Edge Agent will attempt to restart the job.
However, with some errors (such as configuration errors), you must manually restart
the job.

To determine which jobs need to be restarted manually, see the **FatalError** metric in [Monitor the Amazon Kinesis Video Streams Edge Agent with
CloudWatch](monitoring-edge-cloudwatch.md "monitoring-edge-cloudwatch.md").

Resend the [StartEdgeConfigurationUpdate](API_StartEdgeConfigurationUpdate.md "API_StartEdgeConfigurationUpdate.md") to restart the job
for the stream.

## How do I monitor the health of my

Amazon Kinesis Video Streams Edge Agent?

For more information, see [Monitor the Amazon Kinesis Video Streams Edge Agent with
CloudWatch](monitoring-edge-cloudwatch.md "monitoring-edge-cloudwatch.md").
