# 3D Point Cloud Task types

You can use Ground Truth 3D point cloud labeling modality for a variety of use cases. The
following list briefly describes each 3D point cloud task type. For additional details and
instructions on how to create a labeling job using a specific task type, select the task
type name to see its task type page.

- [3D point cloud object detection](sms-point-cloud-object-detection.md "sms-point-cloud-object-detection.md") – Use this
  task type when you want workers to locate and classify objects in a 3D point cloud
  by adding and fitting 3D cuboids around objects.
- [3D point cloud object tracking](sms-point-cloud-object-tracking.md "sms-point-cloud-object-tracking.md") – Use this
  task type when you want workers to add and fit 3D cuboids around objects to track
  their movement across a sequence of 3D point cloud frames. For example, you can use
  this task type to ask workers to track the movement of vehicles across multiple
  point cloud frames.
- [3D point cloud semantic segmentation](sms-point-cloud-semantic-segmentation.md "sms-point-cloud-semantic-segmentation.md") –
  Use this task type when you want workers to create a point-level semantic
  segmentation mask by painting objects in a 3D point cloud using different colors
  where each color is assigned to one of the classes you specify.
- 3D point cloud adjustment task types –
  Each of the task types above has an associated _adjustment_ task
  type that you can use to audit and adjust annotations generated from a 3D point
  cloud labeling job. Refer to the task type page of the associated type to learn how
  to create an adjustment labeling job for that task.
