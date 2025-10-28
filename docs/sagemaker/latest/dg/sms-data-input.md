# Input data

The input data are the data objects that you send to your workforce to be labeled.
There are two ways to send data objects to Ground Truth for labeling:

- Send a list of data objects that require labeling using an input manifest
  file.
- Send individual data objects in real time to a perpetually running, streaming
  labeling job.
  If you have a dataset that needs to be labeled one time, and you do not require an
  ongoing labeling job, create a standard labeling job using an input manifest file.

If you want to regularly send new data objects to your labeling job after it has
started, create a streaming labeling job. When you create a streaming labeling job, you
can optionally use an input manifest file to specify a group of data that you want
labeled immediately when the job starts. You can continuously send new data objects to a
streaming labeling job as long as it is active.

###### Note

Streaming labeling jobs are only supported through the SageMaker API. You cannot create
a streaming labeling job using the SageMaker AI console.

The following task types have special input data requirements and options:

- For [3D point cloud](sms-point-cloud.md "sms-point-cloud.md") labeling job input data requirements, see
  [3D Point Cloud Input Data](sms-point-cloud-input-data.md "sms-point-cloud-input-data.md").
- For [video frame](sms-video-task-types.md "sms-video-task-types.md") labeling job input data requirements, see [Video Frame Input Data](sms-video-frame-input-data-overview.md "sms-video-frame-input-data-overview.md").

###### Topics

- [Input manifest files](sms-input-data-input-manifest.md "sms-input-data-input-manifest.md")
- [Automate data setup for labeling jobs](sms-console-create-manifest-file.md "sms-console-create-manifest-file.md")
- [Supported data formats](sms-supported-data-formats.md "sms-supported-data-formats.md")
- [Ground Truth streaming labeling jobs](sms-streaming-labeling-job.md "sms-streaming-labeling-job.md")
- [Input Data Quotas](input-data-limits.md "input-data-limits.md")
- [Select Data for Labeling](sms-data-filtering.md "sms-data-filtering.md")
