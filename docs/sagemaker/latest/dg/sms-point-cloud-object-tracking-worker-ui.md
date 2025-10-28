# View the worker task

interface for a 3D point cloud object tracking task

Ground Truth provides workers with a web portal and tools to complete your 3D point cloud
object tracking annotation tasks. When you create the labeling job, you provide the
Amazon Resource Name (ARN) for a pre-built Ground Truth UI in the `HumanTaskUiArn`
parameter. When you create a labeling job using this task type in the console, this UI
is automatically used. You can preview and interact with the worker UI when you create a
labeling job in the console. If you are a new use, it is recommended that you create a
labeling job using the console to ensure your label attributes, point cloud frames, and
if applicable, images, appear as expected.

The following is a GIF of the 3D point cloud object tracking worker task interface and
demonstrates how the worker can navigate the point cloud frames in the sequence. The
annotating tools are a part of the worker task interface. They are not available for the
preview interface.

![Gif showing how the worker can navigate the point cloud frames in the sequence.](images/pointcloud/gifs/object_tracking/nav_frames.gif)
Once workers add a single cuboid, that cuboid is replicated in all frames of the
sequence with the same ID. Once workers adjust the cuboid in another frame, Ground Truth will
interpolate the movement of that object and adjust all cuboids between the manually
adjusted frames. The following GIF demonstrates this interpolation feature. In the
navigation bar on the bottom-left, red-areas indicate manually adjusted frames.

![Gif showing how the location of a cuboid is inferred in in-between frames.](/images/sagemaker/latest/dg/images/pointcloud/gifs/object_tracking/label-interpolation.gif)
If you provide camera data for sensor fusion, images are matched up with scenes in
point cloud frames. These images appear in the worker portal as shown in the following
GIF.

Worker can navigate in the 3D scene using their keyboard and mouse. They can:

- Double click on specific objects in the point cloud to zoom into them.
- Use a mouse-scroller or trackpad to zoom in and out of the point cloud.
- Use both keyboard arrow keys and Q, E, A, and D keys to move Up, Down, Left,
  Right. Use keyboard keys W and S to zoom in and out.
  Once a worker places a cuboids in the 3D scene, a side-view will appear with the three
  projected side views: top, side, and back. These side-views show points in and around
  the placed cuboid and help workers refine cuboid boundaries in that area. Workers can
  zoom in and out of each of those side-views using their mouse.

The following video demonstrates movements around the 3D point cloud and in the
side-view.

![Gif showing movements around the 3D point cloud showing a street scene.](images/pointcloud/gifs/object_tracking/nav_general_UI.gif)
Additional view options and features are available. See the [worker instruction page](sms-point-cloud-worker-instructions-object-tracking.md "sms-point-cloud-worker-instructions-object-tracking.md") for a comprehensive overview of the Worker UI.

## Worker tools

Workers can navigate through the 3D point cloud by zooming in and out, and moving
in all directions around the cloud using the mouse and keyboard shortcuts. If
workers click on a point in the point cloud, the UI will automatically zoom into
that area. Workers can use various tools to draw 3D cuboid around objects. For more
information, see **Assistive Labeling Tools**.

After workers have placed a 3D cuboid in the point cloud, they can adjust these
cuboids to fit tightly around cars using a variety of views: directly in the 3D
cuboid, in a side-view featuring three zoomed-in perspectives of the point cloud
around the box, and if you include images for sensor fusion, directly in the 2D
image.

View options that enable workers to easily hide or view label text, a ground mesh,
and additional point attributes. Workers can also choose between perspective and
orthogonal projections.

###### Assistive Labeling Tools

Ground Truth helps workers annotate 3D point clouds faster and more accurately using
UX, machine learning and computer vision powered assistive labeling tools for 3D
point cloud object tracking tasks. The following assistive labeling tools are
available for this task type:

- **Label autofill** – When a worker
  adds a cuboid to a frame, a cuboid with the same dimensions and orientation
  is automatically added to all frames in the sequence.
- **Label interpolation** – After a
  worker has labeled a single object in two frames, Ground Truth uses those
  annotations to interpolate the movement of that object between those two
  frames. Label interpolation can be turned on and off.
- **Bulk label and attribute management**
  – Workers can add, delete, and rename annotations, label category
  attributes, and frame attributes in bulk.
  - Workers can manually delete annotations for a given object before
    or after a frame. For example, a worker can delete all labels for an
    object after frame 10 if that object is no longer located in the
    scene after that frame.
  - If a worker accidentally bulk deletes all annotations for a
    object, they can add them back. For example, if a worker deletes all
    annotations for an object before frame 100, they can bulk add them
    to those frames.
  - Workers can rename a label in one frame and all 3D cuboids
    assigned that label are updated with the new name across all frames.
  - Workers can use bulk editing to add or edit label category
    attributes and frame attributes in multiple frames.

- **Snapping** – Workers can add a
  cuboid around an object and use a keyboard shortcut or menu option to have
  Ground Truth's autofit tool snap the cuboid tightly around the object's boundaries.
- **Fit to ground** – After a worker
  adds a cuboid to the 3D scene, the worker can automatically snap the cuboid
  to the ground. For example, the worker can use this feature to snap a cuboid
  to the road or sidewalk in the scene.
- **Multi-view labeling** – After a
  worker adds a 3D cuboid to the 3D scene, a side -panel displays front and
  two side perspectives to help the worker adjust the cuboid tightly around
  the object. Workers can annotation the 3D point cloud, the side panel and
  the adjustments appear in the other views in real time.
- **Sensor fusion** – If you provide
  data for sensor fusion, workers can adjust annotations in the 3D scenes and
  in 2D images, and the annotations will be projected into the other view in
  real time.
- **Auto-merge cuboids** – Workers can
  automatically merge two cuboids across all frames if they determine that
  cuboids with different labels actually represent a single object.
- **View options** – Enables workers to
  easily hide or view label text, a ground mesh, and additional point
  attributes like color or intensity. Workers can also choose between
  perspective and orthogonal projections.
