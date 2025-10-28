# Understand the 3D point cloud object

tracking task type

Use this task type when you want workers to add and fit 3D cuboids around objects to track
their movement across 3D point cloud frames. For example, you can use this task type to ask
workers to track the movement of vehicles across multiple point cloud frames.

For this task type, the data object that workers label is a sequence of point cloud
frames. A _sequence_ is defined as a temporal series of point cloud
frames. Ground Truth renders a series of 3D point cloud visualizations using a sequence you provide
and workers can switch between these 3D point cloud frames in the worker task interface.

Ground Truth provides workers with tools to annotate objects with 9 degrees of
freedom (x,y,z,rx,ry,rz,l,w,h) in three dimensions in both 3D
scene and projected side views (top, side, and back). When a worker draws a cuboid around an
object, that cuboid is given a unique ID, for example `Car:1` for one car in the
sequence and `Car:2` for another. Workers use that ID to label the same object in
multiple frames.

You can also provide camera data to give workers more visual information about scenes in
the frame, and to help workers draw 3D cuboids around objects. When a worker adds a 3D
cuboid to identify an object in either the 2D image or the 3D point cloud, and the cuboid
shows up in the other view.

You can adjust annotations created in a 3D point cloud object detection labeling job using
the 3D point cloud object tracking adjustment task type.

If you are a new user of the Ground Truth 3D point cloud labeling modality, we recommend you
review [3D point cloud labeling jobs
overview](sms-point-cloud-general-information.md "sms-point-cloud-general-information.md"). This labeling modality is
different from other Ground Truth task types, and this page provides an overview of important
details you should be aware of when creating a 3D point cloud labeling job.

The following topics explain how to create a 3D point cloud object tracking job, show what
the worker task interface looks like (what workers see when they work on this task), and
provide an overview of the output data you get when workers complete their tasks. The final
topic provides useful information for creating object tracking adjustment or verification
labeling jobs.

###### Topics

- [Create a 3D point
  cloud object tracking labeling job](sms-point-cloud-object-tracking-create-labeling-job.md "sms-point-cloud-object-tracking-create-labeling-job.md")
- [View the worker task
  interface for a 3D point cloud object tracking task](sms-point-cloud-object-tracking-worker-ui.md "sms-point-cloud-object-tracking-worker-ui.md")
- [Output data for a 3D point
  cloud object tracking labeling job](sms-point-cloud-object-tracking-output-data.md "sms-point-cloud-object-tracking-output-data.md")
- [Information
  for creating a 3D point cloud object tracking adjustment or verification labeling
  job](sms-point-cloud-object-tracking-adjustment-verification.md "sms-point-cloud-object-tracking-adjustment-verification.md")
