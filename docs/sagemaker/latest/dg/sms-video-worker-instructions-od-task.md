# Your Task

When you work on a video frame object detection task, you need to select a
category from the **Label category** menu on the right side of
your worker portal to start annotating. After you've chosen a category, draw
annotations around objects that this category applies to. To learn more about
the tools you see in your worker UI, refer to the [Tool Guide](sms-video-worker-instructions-tool-guide.md "sms-video-worker-instructions-tool-guide.md").

After you've added a label, you may see a downward pointing arrow next to the
label in the **Labels** menu. Select this arrow and then select
one option for each label attribute you see to provide more information about
that label.

![Gif showing how a worker can use the bounding box tool for their object detection tasks.](/images/sagemaker/latest/dg/images/sms/video/kitti-od-general-labeling-job.gif)
You may see frame attributes under the **Labels** menu. These
attributes will appear on each frame in your task. Use these attribute prompts
to enter additional information about each frame.

![Example frame attribute prompt.](images/sms/frame-attributes.png)
To edit an annotation, select the label of the annotation that you want to
edit in the **Labels** menu or select the annotation in the
frame. When you edit or delete an annotation, the action will only modify the
annotation in a single frame.

If you are working on a task that includes a bounding box tool, use the
predict next icon to predict the location of all bounding boxes that you have
drawn in a frame in the next frame. If you select a single box and then select
the predict next icon, only that box will be predicted in the next frame. If you
have not added any boxes to the current frame, you will receive an error. You
must add at least one box to the frame before using this feature.

###### Note

The predict next feature will not overwrite manually created annotations. It will only
add annotations. If you use predict next and as a result have more than one
bounding box around a single object, delete all but one box. Each object
should only be identified with a single box.

After you've used the predict next icon, review the location of each box in
the next frame and make adjustments to the box location and size if necessary.

The following graphic demonstrates how to use the predict next tool:

![Gif showing how a worker can adjust the predicted boxes in the next frame.](/images/sagemaker/latest/dg/images/sms/video/kitti-video-od.gif)
For all other tools, you can use the **Copy to next** and
**Copy to all** tools to copy your annotations to the next
or all frames respectively.
