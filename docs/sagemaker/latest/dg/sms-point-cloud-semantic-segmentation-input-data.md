# Output

data for a 3D point cloud semantic segmentation job

When you create a 3D point cloud semantic segmentation labeling job, tasks are sent to
workers. When these workers complete their tasks, their annotations are written to the
Amazon S3 bucket you specified when you created the labeling job. The output data format
determines what you see in your Amazon S3 bucket when your labeling job status ([LabelingJobStatus](../APIReference/API_DescribeLabelingJob.md#API_DescribeLabelingJob_ResponseSyntax "../APIReference/API_DescribeLabelingJob.md#API_DescribeLabelingJob_ResponseSyntax")) is `Completed`.

If you are a new user of Ground Truth, see [Labeling job output data](sms-data-output.md "sms-data-output.md") to learn more about the Ground Truth output data format. To
learn about the 3D point cloud object detection output data format, see [3D point cloud semantic segmentation output](sms-data-output.md#sms-output-point-cloud-segmentation "sms-data-output.md#sms-output-point-cloud-segmentation").
