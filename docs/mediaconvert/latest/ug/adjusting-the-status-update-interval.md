# Adjust the status update

interval

By default, AWS Elemental MediaConvert sends `STATUS_UPDATE` events to
Amazon EventBridge approximately once per minute. These status updates provide information
about how your job is progressing. You can adjust the status update interval by
specifying a different update frequency in your job.

###### To specify the STATUS_UPDATE frequency

1. On the **Create job** page, in the **Job** pane on the left, in the **Job settings** section, choose
   **AWS integration**.
2. In the **AWS integration** section on the right,
   for **Status update interval (sec)**, choose
   **interval, in seconds, between updates**.
   If you use the API or an SDK, you can find this setting in the JSON file of your job. The setting name is [statusUpdateInterval](../apireference/jobs.md#jobs-prop-createjobrequest-statusupdateinterval "../apireference/jobs.md#jobs-prop-createjobrequest-statusupdateinterval").
