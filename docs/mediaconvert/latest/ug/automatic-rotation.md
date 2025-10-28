# Configuring automatically detected rotation

If your video has embedded rotation metadata, AWS Elemental MediaConvert can detect it and
automatically rotate your video content so that it's oriented correctly in your
outputs.

###### Note

AWS Elemental MediaConvert doesn't pass through rotation metadata. Regardless of how you
set **Rotate**, job outputs don't have rotation metadata.

###### To enable automatic rotation

1. Check that your input container is .mov or .mp4 and that your input has
   rotation metadata.
2. On the **Create job** page, in the **Job** pane on the left, in the **Inputs** section, choose the input that
   has rotation metadata.
3. In the **Video selector** section on the left, for
   **Rotate**, choose **Automatic**.

###### Note

AWS Elemental MediaConvert doesn't rotate images and motion images that you overlay. If
you use the image inserter feature or the motion image inserter
feature with the rotate feature, rotate your overlay before you upload it. Specify
the position of your overlays as you want them to appear on the video after
rotation.
