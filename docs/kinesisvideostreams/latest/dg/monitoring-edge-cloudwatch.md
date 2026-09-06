

# Monitor the Amazon Kinesis Video Streams Edge Agent with CloudWatch
<a name="monitoring-edge-cloudwatch"></a>

You can monitor the Amazon Kinesis Video Streams Edge Agent using Amazon CloudWatch, which collects and processes raw data into readable, near real-time metrics. These statistics are recorded for a period of 15 months. With this historical information, you can gain a better perspective on how your web application or Amazon Kinesis Video Streams Edge Agent service is performing. 

To view the metrics, do the following:

1. Sign in to the AWS Management Console and open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the left navigation, under **Metrics**, select **All Metrics**.

1. Choose the **Browse** tab, then select the **EdgeRuntimeAgent** custom namespace.

Amazon Kinesis Video Streams Edge Agent publishes the following metrics under the namespace `EdgeRuntimeAgent`:



- ** Stream name, `RecordJob` **
  - **State:** Running / **Description:** Publishes continuously when the `RecordJob` is running.<br />Units: None. "1" is published for as long as `RecordJob` is in this state.
  - **State:** FatalError / **Description:** Publishes if a `RecordJob` fatally errors.<br />Units: None. "1" is published once, when this event occurs. See logs for additional information. 
  - **State:** Completed / **Description:** Publishes when a `RecordJob` is completed.<br />Units: None. "1" is published once, when this event occurs.

- ** Stream name, `UploadJob` **
  - **State:** Running / **Description:** Publishes continuously when the `UploadJob` is running.<br />Units: None. "1" is published for as long as `UploadJob` is in this state.
  - **State:** FatalError / **Description:** Publishes if the `UploadJob` fatally errors.<br />Units: None. "1" is published once, when this event occurs.  See logs for additional information. 
  - **State:** Completed / **Description:** Publishes when the `UploadJob` is completed.<br />Units: None. "1" is published once, when this event occurs.

- ** Stream name **
  - **State:** PercentageSpaceUsed
  - **Description:** This is the percentage used out of the total space allocated in Amazon Kinesis Video Streams Edge Agent configurations for recording media. See [LocalSizeConfig](https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_LocalSizeConfig.html) for more information.<br />Units: Percentage (scale 0–1). 

- ** Thing name **
  - **State:** Alive / **Description:** Publishes every minute from the Amazon Kinesis Video Streams Edge Agent, regardless of any configurations running on it.<br />This can be used to understand if the Amazon Kinesis Video Streams Edge Agent is alive and ready to accept configurations.<br />Units: None. "1" is published every minute.
  - **State:** RecordJobs.HealthyJobCount / **Description:** Total count of running and scheduled record jobs on Amazon Kinesis Video Streams Edge Agent.<br />Units: Count.
  - **State:** UploadJobs.HealthyJobCount / **Description:** Total count of running and scheduled upload jobs on Amazon Kinesis Video Streams Edge Agent.<br />Units: Count.
  - **State:** RecordJobs.UnhealthyJobCount / **Description:** Total count of currently errored record jobs.<br />Units: Count.
  - **State:** UploadJobs.UnhealthyJobCount / **Description:** Total count of currently errored upload jobs.<br />Units: Count.
  - **State:** RecordJobs.RunningJobCount / **Description:** Total count of actively running record jobs.<br />Units: Count.
  - **State:** UploadJobs.RunningJobCount / **Description:** Total count of actively running upload jobs.<br />Units: Count.
  - **State:** RecordJobs.EdgeConfigCount / **Description:** Total count of record configurations in process on Amazon Kinesis Video Streams Edge Agent.<br />Units: Count.
  - **State:** UploadJobs.EdgeConfigCount / **Description:** Total count of upload configurations in process on Amazon Kinesis Video Streams Edge Agent.<br />Units: Count.



## CloudWatch metrics guidance for Amazon Kinesis Video Streams Edge Agent
<a name="monitoring-edge-qa"></a>

CloudWatch metrics can be useful for finding answers to the following questions:

**Topics**
+ [Does the Amazon Kinesis Video Streams Edge Agent have enough space to record?](#monitoring-edge-space)
+ [Is the Amazon Kinesis Video Streams Edge Agent alive?](#monitoring-edge-alive)
+ [Are there any unhealthy jobs?](#monitoring-edge-unhealthy)
+ [Do any jobs need external intervention?](#monitoring-edge-intervention)

### Does the Amazon Kinesis Video Streams Edge Agent have enough space to record?
<a name="monitoring-edge-space"></a>

**Relevant metrics:** `PercentageSpaceUsed`

**Action:** No action required.

### Is the Amazon Kinesis Video Streams Edge Agent alive?
<a name="monitoring-edge-alive"></a>

**Relevant metrics:** `Alive`

**Action:** If at any point you stop receiving this metric, it means that the Amazon Kinesis Video Streams Edge Agent encountered **one or more** of the following:
+ An application runtime issue: memory or other resource constraint, bug, and so on
+ The AWS IoT device that the agent is running on shutdown, crashed, or terminated
+ The AWS IoT device doesn't have network connectivity

### Are there any unhealthy jobs?
<a name="monitoring-edge-unhealthy"></a>

**Relevant metrics:**
+ `RecordJobs.UnhealthyJobCount`
+ `UploadJobs.UnhealthyJobCount`

**Action:** Inspect the logs and look for the `FatalError` metric.
+ If the `FatalError` metric **is** present, a fatal error was encountered and you need to manually restart the job. Inspect the logs and fix the issue before using `StartEdgeConfigurationUpdate` to manually restart the job. 
+ If the `FatalError` metric **isn't** present, a transient (non-fatal) error was encountered and Amazon Kinesis Video Streams Edge Agent is retrying the job.

**Note**  
To have the agent reattempt a fatally-errored job, use [StartEdgeConfigurationUpdate](https://docs.aws.amazon.com/kinesisvideostreams/latest/APIReference/API_StartEdgeConfigurationUpdate.html).

### Do any jobs need external intervention?
<a name="monitoring-edge-intervention"></a>

**Relevant metrics:**
+ `PercentageSpaceUsed` – If this exceeds a certain value, the record job is paused and resumes only when space is available (when media goes out of retention). You can send an updated configuration with a higher `MaxLocalMediaSizeInMB` to update the job immediately.
+ `RecordJob.FatalError` / `UploadJob.FatalError` – Investigate the agent's logs and send the configuration again for the job to resume.

**Action:** Make an API call with the configuration to restart jobs that encounter this problem.