# AWS IoT Jobs Troubleshooting

This is the troubleshooting section for AWS IoT Jobs.

## How do I locate an AWS IoT Jobs

endpoint?

**How do I locate the AWS IoT Jobs control plane
endpoint?**

AWS IoT Jobs supports controls plane API operations using the HTTPS protocol.
Verify you have connected to the correct control plane endpoint using the HTTPS
protocol.

For a list of AWS region-specific endpoints, see [AWS IoT Core - control plane endpoints](../../../general/latest/gr/iot-core.md#iot-core-control-plane-endpoints "../../../general/latest/gr/iot-core.md#iot-core-control-plane-endpoints").

For a list of FIPS compliant **AWS IoT Jobs control
plane** endpoints, see [FIPS Endpoints
by Service](https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service "https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service")

###### Note

AWS IoT Jobs and AWS IoT Core share the same AWS Region-specific
endpoints.

**How do I locate the AWS IoT Jobs data plane
endpoint?**

AWS IoT Jobs supports data plane API operations using the HTTPS and MQTT
protocols. Verify you have connected to the correct data plane endpoint using the
HTTPS or MQTT protocol.

- HTTPS protocol
  - Use the following [**describe-endpoint**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-endpoint.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-endpoint.html") CLI command shown below or
    the [`DescribeEndpoint`](../apireference/API_DescribeEndpoint.md "../apireference/API_DescribeEndpoint.md") REST API. For
    the endpoint type, use `iot:Jobs`.

  ```
  aws iot describe-endpoint --endpoint-type `iot:Jobs`
  ```

- MQTT protocol
  - Use the following [**describe-endpoint**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-endpoint.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-endpoint.html") CLI command shown below or
    the [`DescribeEndpoint`](../apireference/API_DescribeEndpoint.md "../apireference/API_DescribeEndpoint.md") REST API. For
    the endpoint type, use `iot:Data-ATS`.

  ```
  aws iot describe-endpoint --endpoint-type `iot:Data-ATS`
  ```

For a list of FIPS compliant **AWS IoT Jobs data
plane** endpoints, see [FIPS Endpoints
by Service](https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service "https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service")

## How do I monitor AWS IoT Jobs activity and

provide metrics?

Monitoring AWS IoT Jobs activity using Amazon CloudWatch provides real-time visibility into
ongoing AWS IoT Jobs operations and helps control costs with CloudWatch alarms via AWS IoT Rules.
You must configure logging before you can monitor AWS IoT Jobs activity and setup CloudWatch
alarms. For more information on setting up logging, see [Configure AWS IoT logging](configure-logging.md "configure-logging.md").

For more information on Amazon CloudWatch and how to setup permission via an IAM user role to
use CloudWatch resources, see [Identity and access management for Amazon CloudWatch](../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md "../../../AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.md").

**How do I set up AWS IoT Jobs metrics and monitoring using
Amazon CloudWatch?**

To set up AWS IoT logging, follow the steps outlined in [Configure AWS IoT logging](configure-logging.md "configure-logging.md"). AWS IoT logging set up can be done in the
AWS Management Console, AWS CLI, or API. AWS IoT logging set up for specific thing groups must be
done in the AWS CLI or API only.

The [AWS IoT Jobs metrics](metrics_dimensions.md#jobs-metrics "metrics_dimensions.md#jobs-metrics") section contains the AWS IoT Jobs metrics used for
monitoring AWS IoT Jobs activity. It explains how to view the metrics in the
AWS Management Console and AWS CLI.

Additionally, you can set up CloudWatch alarms to alert you of specific metrics you
want to closely monitor. For guidance on alarm setup, see [Using Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md").

## Device fleets and single device

troubleshooting

**A job execution maintains a status of `QUEUED`
indefinitely**

When a job execution with a status state of `QUEUED` does not proceed
to the next logical status state such as `IN_PROGRESS`,
`FAILED`, or `TIMED_OUT`, one of the following scenarios may
be the cause:

- Review your device activity in the CloudWatch logs located in the [CloudWatch console](../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatchLogs.md"). For more information, refer to [Monitor AWS IoT using CloudWatch Logs](cloud-watch-logs.md "cloud-watch-logs.md").
- The IAM role associated with the job and subsequent job execution may not
  have the correct permissions listed in one of the policy statements of the IAM
  policy attached to that IAM role. Use the [`describe-job`](../apireference/API_DescribeJob.md "../apireference/API_DescribeJob.md") API to identify the IAM role linked to
  that job and subsequent job execution and review the IAM policy for correct
  permissions. Once the policy permission statements have been updated, you should
  be able to perform the [`AssumeRole`](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") API command on the resource.

**A job execution was not created for my thing or thing
group**

When a job updates its status state to `IN_PROGRESS`, it will begin
the job document rollout to all devices in your target group. This status state
update will create a job execution for each target device. If a job execution was
not created for one of the target devices, refer to the following guidance:

- Is the `thing`
  _directly_ targeted by the job, the job has a status state of
  `IN_PROGRESS`, and the job is concurrent? If all three conditions
  are met, then the job is still sending out job executions to all devices in your
  target group and that specific `thing` has not received its job
  execution yet.

      + Review the devices in your target group for the job and the job status
       state in the AWS Management Console or use the [`describe-job`](../apireference/API_DescribeJob.md "../apireference/API_DescribeJob.md") API command.
      + Use the [`describe-job`](../apireference/API_DescribeJob.md "../apireference/API_DescribeJob.md") API command to review if the job has
       the `IsConcurrent` property set to true or false. For more
       information, see [Job limits](job-limits.md "job-limits.md").

- The `thing` is _not directly_ targeted by the
  job.
  - If the `Thing` was added to a `ThingGroup` and the
    job targeted the `ThingGroup`, then verify the `Thing`
    is part of the `ThingGroup`.
  - If the job is a snapshot job with a status state of
    `IN_PROGRESS` and is concurrent, then the job is still sending
    out job executions to all devices in your target group and that specific
    `Thing` has not received its job execution yet.
  - If the job is a continuous job with a status state of
    `IN_PROGRESS` and is concurrent, then the job is still sending
    out job executions to all devices in your target group and that specific
    `Thing` has not received its job execution yet. For continuous
    jobs only, you can also remove the `Thing` from the
    `ThingGroup` and then add the `Thing` back to the
    `ThingGroup`.
  - If the job is a snapshot job with a status state of
    `IN_PROGRESS` and is not concurrent, then it's likely the
    `Thing` or `ThingGroup` membership relationship is
    not acknowledged by AWS IoT Jobs. It is recommended to add several seconds of
    waiting time after your `AddThingToThingGroup` call before you
    create your `Job`. Alternatively, you can switch the target
    selection to `Continuous`, thus making the service backfill the
    delayed `Thing` and `ThingGroup` membership attachment
    event.

**New job fails due to `LimitedExceededException`
error**

If your job creation fails with an error response of
`LimitedExceededException`, then call the `list-jobs` API
and review all jobs with `isConcurrent=true` to determine if you are at
your job concurrency limit. See [Job
limits](job-limits.md "job-limits.md") for additional information on concurrent jobs. To view your job
concurrency limits and to request a limit increase, see [AWS IoT Device Management jobs limits and quotas](../../../general/latest/gr/iot_device_management.md#job-limits "../../../general/latest/gr/iot_device_management.md#job-limits").

**Job document size limit**

The job document size is limited by the MQTT payload size. If you need a job
document larger than 32 kB (kilobytes), 32,000 B (bytes), then create and store the
job document in Amazon S3 and add an Amazon S3 object URL in the `documentSource`
field for the `CreateJob` API or using the AWS CLI. For the AWS Management Console,
add an Amazon S3 object URL in the Amazon S3 URL text box when creating a job.

- AWS Management Console create job documentation: [Create and manage jobs by using the AWS Management Console](manage-job-console.md "manage-job-console.md")
- AWS CLI create job documentation: [Create and manage jobs using the AWS CLI](manage-job-cli.md "manage-job-cli.md")
- `CreateJob` API documentation: [CreateJob](../apireference/API_CreateJob.md "../apireference/API_CreateJob.md")

**Device Side MQTT message requests throttle
limits**

If you receive an error code 400 `ThrottlingException`, the device
side MQTT message failed due to reaching the limit of simultaneous device side
requests. See [AWS IoT Device Management jobs limits and quotas](../../../general/latest/gr/iot_device_management.md#job-limits "../../../general/latest/gr/iot_device_management.md#job-limits") for more information on throttle limits
and if it is adjustable.

**Connection timeout error**

An error code 400 `RequestExpired` indicates a connection failure due
to high latency or low client side timeout values.

- See [Testing connectivity with your device data
  endpoint](iot-quick-start-test-connection.md "iot-quick-start-test-connection.md") for information on testing connection between the client side
  and server side.

**Invalid API command**

Confirm the correct API command is entered to avoid an error message stating the
API command is invalid. See the [AWS IoT API Reference](../apireference/Welcome.md "../apireference/Welcome.md") for a comprehensive list of all
AWS IoT API commands.

**Service side connection error**

An error code 503 `ServiceUnavailable` indicates the error originated
from the server side.

- See [AWS Health Dashboard (all
  AWS services)](https://health.aws.amazon.com/health/status "https://health.aws.amazon.com/health/status") for the current status of all AWS services.
- See [AWS Health Dashboard (personal AWS account)](https://aws.amazon.com/premiumsupport/technology/aws-health-dashboard/ "https://aws.amazon.com/premiumsupport/technology/aws-health-dashboard/") for the current status of your
  personal AWS account.
