# Information

for creating a 3D point cloud object tracking adjustment or verification labeling
job

You can create an adjustment and verification labeling job using the Ground Truth console or
`CreateLabelingJob` API. To learn more about adjustment and verification
labeling jobs, and to learn how create one, see [Label verification and adjustment](sms-verification-data.md "sms-verification-data.md").

When you create an adjustment labeling job, your input data to the labeling job can
include labels, and yaw, pitch, and roll measurements from a previous labeling job or
external source. In the adjustment job, pitch, and roll will be visualized in the worker
UI, but cannot be modified. Yaw is adjustable.

Ground Truth uses Tait-Bryan angles with the following intrinsic rotations to visualize yaw,
pitch and roll in the worker UI. First, rotation is applied to the vehicle according to
the z-axis (yaw). Next, the rotated vehicle is rotated according to the intrinsic
y'-axis (pitch). Finally, the vehicle is rotated according to the intrinsic x''-axis
(roll).
