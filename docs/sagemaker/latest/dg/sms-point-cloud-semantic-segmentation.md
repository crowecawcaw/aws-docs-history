# Understand the 3D point cloud

semantic segmentation task type

Semantic segmentation involves classifying individual points of a 3D point cloud into
pre-specified categories. Use this task type when you want workers to create a point-level
semantic segmentation mask for 3D point clouds. For example, if you specify the classes
`car`, `pedestrian`, and `bike`, workers select one
class at a time, and color all of the points that this class applies to the same color in
the point cloud.

For this task type, the data object that workers label is a single point cloud frame.
Ground Truth generates a 3D point cloud visualization using point cloud data you provide. You can
also provide camera data to give workers more visual information about scenes in the frame,
and to help workers paint objects. When a worker paints an object in either the 2D image or
the 3D point cloud, the paint shows up in the other view.

You can also adjust or verify annotations created in a 3D point cloud object detection
labeling job using the 3D point cloud semantic segmentation adjustment or labeling task
type. To learn more about adjustment and verification labeling jobs, and to learn how create
one, see [Label verification and adjustment](sms-verification-data.md "sms-verification-data.md").

If you are a new user of the Ground Truth 3D point cloud labeling modality, we recommend you
review [3D point cloud labeling jobs
overview](sms-point-cloud-general-information.md "sms-point-cloud-general-information.md"). This labeling modality is
different from other Ground Truth task types, and this topic provides an overview of important
details you should be aware of when creating a 3D point cloud labeling job.

The following topics explain how to create a 3D point cloud semantic segmentation job, show
what the worker task interface looks like (what workers see when they work on this task),
and provide an overview of the output data you get when workers complete their tasks.

###### Topics

- [Create a 3D
  point cloud semantic segmentation labeling job](sms-point-cloud-semantic-segmentation-create-labeling-job.md "sms-point-cloud-semantic-segmentation-create-labeling-job.md")
- [View the worker task
  interface for a 3D point cloud semantic segmentation job](sms-point-cloud-semantic-segmentation-worker-ui.md "sms-point-cloud-semantic-segmentation-worker-ui.md")
- [Output
  data for a 3D point cloud semantic segmentation job](sms-point-cloud-semantic-segmentation-input-data.md "sms-point-cloud-semantic-segmentation-input-data.md")
