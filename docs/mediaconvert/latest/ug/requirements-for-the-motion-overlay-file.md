

# Requirements to set up motion graphic overlay files
<a name="requirements-for-the-motion-overlay-file"></a>

The following table describes how to set up motion graphic overlay files.


| Motion graphic file requirement | Description | 
| --- | --- | 
| File type | QuickTime (.mov)+  Container: QuickTime <br />+  Codec: QuickTime Animation (RLE) <br />+  Color space: RGBA <br />Sequential PNG (.png)+  Make sure that the names of the .png files end with sequential numbers that specify the order that they are played in. For example, overlay\_000.png, overlay\_001.png, overlay\_002.png, and so on. <br />+  Pad your initial file name with enough zeros to complete the sequence. For example, if the first image is overlay\_0.png, there can be only 10 images in the sequence, with the last image being overlay\_9.png. However, if the first image is overlay\_00.png, there can be 100 images in the sequence. <br />+  Make sure that the number of images in your series matches the frame rate and your intended overlay duration. For example, if you want a 30-second overlay at 30 fps, you should have 900 .png images. <br />+  Requires an alpha channel.  | 
| Frame rate | QuickTime (.mov)+  Use any frame rate. The frame rate that you use doesn't have to match the frame rate of the underlying video. <br />Sequential PNG (.png)+  Use any frame rate. The frame rate that you use doesn't have to match the frame rate of the underlying video.  <br />+  Specify the frame rate when you set up the overlay.  | 
| Aspect ratio | Use any aspect ratio. It doesn't have to match the aspect ratio of the underlying video. | 
| Size in pixels | Use any size. MediaConvert scales the motion graphic with any outputs that have video scaling. | 