# Requirements to create verification and adjustment

labeling jobs

To create a label verification or adjustment job, you must satisfy the following
criteria.

- For non streaming labeling jobs: The input manifest file you use must contain
  the label attribute name (`LabelAttributeName`) of the labels that
  you want adjusted. When you chain a successfully completed labeling job, the
  output manifest file is used as the input manifest file for the new, chained
  job. To learn more about the format of the output manifest file Ground Truth produces
  for each task type, see [Labeling job output data](sms-data-output.md "sms-data-output.md").

For streaming labeling jobs: The Amazon SNS message you sent to the Amazon SNS input
topic of the adjustment or verification labeling job must contain the label
attribute name of the labels you want adjusted or verified. To see an example of
how you can create an adjustment or verification labeling job with streaming
labeling jobs, see this [Jupyter Notebook example](https://github.com/aws/amazon-sagemaker-examples/blob/master/ground_truth_labeling_jobs/ground_truth_streaming_labeling_jobs/ground_truth_create_chained_streaming_labeling_job.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/master/ground_truth_labeling_jobs/ground_truth_streaming_labeling_jobs/ground_truth_create_chained_streaming_labeling_job.ipynb") in GitHub.

- The task type of the verification or adjustment labeling job must be the same
  as the task type of the original job unless you are using the [Image Label Verification](sms-label-verification.md "sms-label-verification.md") task type
  to verify bounding box or semantic segmentation image labels. See the next
  bullet point for more details about the video frame task type
  requirements.
- For video frame annotation verification and adjustment jobs, you must use the
  same annotation task type used to create the annotations from the previous
  labeling job. For example, if you create a video frame object detection job to
  have workers draw bounding boxes around objects, and then you create a video
  object detection adjustment job, you must specify _bounding boxes_ as the annotation task type. To learn more video
  frame annotation task types, see [Task types](sms-video-overview.md#sms-video-frame-tools "sms-video-overview.md#sms-video-frame-tools").
- The task type you select for the adjustment or verification labeling job must
  support an audit workflow. The following Ground Truth [built-in task types](sms-task-types.md "sms-task-types.md")
  support adjustment and verification labeling jobs: bounding box, semantic
  segmentation, 3D point cloud object detection, 3D point cloud object tracking,
  and 3D point cloud semantic segmentation, and all video frame object detection
  and video frame object tracking task types — bounding box, polyline,
  polygon and keypoint.
