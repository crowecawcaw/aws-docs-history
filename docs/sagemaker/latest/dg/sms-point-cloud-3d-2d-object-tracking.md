# Understand the 3D-2D point cloud

object tracking task type

Use this task type when you want workers to link 3D point cloud annotations with 2D images annotations and
also link 2D image annotations among various cameras.
Currently, Ground Truth supports cuboids for annotation in a 3D point cloud and
bounding boxes for annotation in 2D videos.
For example, you can use this task type to ask workers to link the movement of a vehicle
in 3D point cloud with its 2D video. Using 3D-2D linking, you can easily correlate
point cloud data (like the distance of a cuboid) to video data (bounding box) for up to 8 cameras.

Ground Truth provides workers with tools to annotate cuboids in a 3D point cloud and bounding boxes in up to 8 cameras using the same annotation UI.
Workers can also link various bounding boxes for the same object across different cameras.
For example, a bounding box in camera1 can be linked to a bounding box in camera2.
This lets you to correlate an object across multiple cameras using a unique ID.

###### Note

Currently, SageMaker AI does not support creating a 3D-2D linking job using the console.
To create a 3D-2D linking job using the SageMaker API, see [Create a labeling job (API)](sms-3d-2d-point-cloud-object-tracking-create-labeling-job.md#sms-point-cloud-3d-2d-object-tracking-create-labeling-job-api "sms-3d-2d-point-cloud-object-tracking-create-labeling-job.md#sms-point-cloud-3d-2d-object-tracking-create-labeling-job-api").

The following topics explain how to create a 3D-2D point cloud object tracking labeling
job, show what the worker task interface looks like (what workers see when they work on this
task), and provide an overview of the output data you get when workers complete their
tasks.

###### Topics

- [Create a
  3D-2D point cloud object tracking labeling job](sms-3d-2d-point-cloud-object-tracking-create-labeling-job.md "sms-3d-2d-point-cloud-object-tracking-create-labeling-job.md")
- [View the worker task
  interface for a 3D-2D object tracking labeling job](sms-point-cloud-3d-2d-object-tracking-worker-ui.md "sms-point-cloud-3d-2d-object-tracking-worker-ui.md")
- [Output data for a
  3D-2D object tracking labeling job](sms-point-cloud-3d-2d-object-tracking-output-data.md "sms-point-cloud-3d-2d-object-tracking-output-data.md")
