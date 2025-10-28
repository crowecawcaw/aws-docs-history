# Sharing a video encode

You can create one video encode and share it among several outputs. Follow the
[earlier procedure](create-video-scratch.md "create-video-scratch.md") to create the
encode once. Then set up the encode for the other outputs using the following
steps.

Note that the procedure for sharing a video encode is nearly identical to the
procedure for sharing an audio encode or captions encode.

1. On the **Create channel** page, find the output group
   that you [created](creating-a-channel-step4.md "creating-a-channel-step4.md").
2. Under that output group, find the output where you want to set up a video
   encode.
3. If the output already contains a video encode, choose that video and then
   choose **Remove video**.
4. Choose **Add video**. A menu appears that includes the
   option **Use an existing video description**, followed by a
   list of the videos that currently exist in the entire channel.
5. Choose the video that you want to use. On the dialog that appears, choose
   **Share the existing settings**.

The fields for this encode appear. Above the first field is an information
message that lists all the outputs that share this encode.

You might want to change the video description to include the term
_shared_, as a reminder to
yourself.

Keep in mind that there is only one instance of this encode in the
channel. Therefore, if you change a field, you will change the field in all
the other outputs that use this encode.

Remember this rule if you change the **Video selector
name** field. If you specify a different selector in the encode
in one output, you change it in all the outputs that share this encode. If
you actually want to specify a different selector, you might need to clone
the encode instead of sharing it.

## To stop sharing an encode

You might need to stop sharing an encode. For example, you might have outputs
A, B, and C that all share the encode H.264-hi-resolution. You want to remove
output C from the shared setup and set up output C with its own (unshared)
encode.

To stop sharing an encode follow these steps.

1. On the **Create channel** page, find the output group
   that has the output that contains the video that you want to remove from
   the shared setup.
2. Select the output group, then select the output that contains the
   video encode. The name of the shared video encode appears, and the names
   of all the outputs that share that encode.
3. Make a note of the video encode, in case you need to refer to it
   again.
4. Select **Remove video**.

You can now create a new video encode for this output, either by [creating from scratch](create-video-scratch.md "create-video-scratch.md"), by sharing a
different encode, or by [cloning](create-video-clone.md "create-video-clone.md") the
encode that you just unshared (cloning isn't the same as sharing).
