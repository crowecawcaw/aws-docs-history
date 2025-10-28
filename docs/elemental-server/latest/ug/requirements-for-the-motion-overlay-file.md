This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Requirements for Motion

Overlay Files

###### General requirements for motion graphic files

Set up the files for your motion graphic as follows:

- **File type**: Use `.swf`, `.mov`, or a set of
  sequential `.png` files.
- **Frame rate**: Use any frame rate; it
  doesn't have to match the frame rate of the underlying video. Frame rate is
  embedded in `.mov` and `.swf` files; with a set of `.png` files you specify the
  frame rate when you set up the overlay.
- **Aspect ratio**: Use any aspect ratio; it
  doesn't have to match the aspect ratio of the underlying video.
- **Size in pixels**: Use any size.
  AWS Elemental Server scales the motion graphic with any outputs that have video
  scaling. Create the overlay in the size that looks how you want it when
  overlaid on your input video.
- **Location**: Save your overlay files in one
  of the following places:

      + Local to the AWS Elemental Server system.


      For example:
       `/data/assets/overlay_001.png`
      + A remote server via a mount point.


      For example:
       `/data/mnt/assets/overlay_001.png`
      + **AWS Elemental Server version 2.10 and later** An Amazon S3 bucket, using SSL.


       For example:
       `s3ssl://company.test/sample_bucket/overlay_001.png`
      + **AWS Elemental Server version 2.10 and later** An Amazon S3 bucket, without SSL.


       For example:
       `s3://company.test/sample_bucket/overlay_001.png`

  For Amazon S3, use sse=true to enable S3 Server Side Encryption (SSE) and rrs=true to enable Reduced Redundancy Storage (RRS). Default values for RRS and SSE are false.

###### Additional requirements for sets of sequential .png files

Set up your .png motion image files follows:

- Make sure that the names of the .png files end with sequential numbers
  that specify the order that they are played in. For example,
  `overlay_000.png`,
  `overlay_001.png`,
  `overlay_002.png`, and so on.
- Pad your initial file name with enough zeros to complete the sequence. For
  example, if the first image is `overlay_0.png`, there can be only 10 images in
  the sequence, with the last image being `overlay_9.png`. But if the first
  image is `overlay_00.png`, there can be 100 images in the sequence.
- Make sure that the number of images in your series matches the frame rate
  and your intended overlay duration. For example, if you want a 30-second
  overlay at 30 fps, you should have 900 .png images.
