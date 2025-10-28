# Step A: Prepare the MOV

asset

1. Create a file – Use a third-party process to create
   a MOV file encoded with Apple QuickTime Run Length Encoding.
   Other codecs in the MOV container are not supported. Take care
   with the following settings:
   - Aspect ratio: The motion overlay can have any aspect
     ratio. It does not have to match the aspect ratio of the
     video output.
   - Frame rate: The frame rate of the motion overlay
     asset must match the frame rate of the underlying video.
   - Size: The motion overlay can be any size, in pixels,
     up to the size of the underlying video. The motion
     overlay must be prepared in the desired size; there is
     no way to resize it when setting it up in the
     event.
   - Position: The motion overlay cannot be positioned so
     that part of the motion overlay runs beyond the right
     edge or bottom edge of the underlying video.
     - If you set up a motion overlay so that it is
       too big or it overruns and Elemental Live can
       identify this error at event creation time, then
       an error message will appear.
     - If Elemental Live cannot identify the error in
       advance, an error message will appear while the
       event is running. The event will not stop but the
       insertion request will fail.

2. Place the file – Place the MOV file in a location
   accessible to the Elemental Live: on a local directory, on a
   remote filesystem accessible via mount point, or in an Amazon S3
   bucket.

You can specify the location in one of the following
ways:

    * Local to the Elemental Live appliance. For example,
     `/data/assets/motion overlay.mov`
    * A remote server via a mount point. For example,
     `/data/mnt/assets/motion
     overlay.mov`
    * An Amazon S3 bucket, using SSL. For example,
     `Amazon S3ssl://company.test/DOC-EXAMPLE-BUCKET/motion
     overlay.mov`
    * An Amazon S3 bucket, without SSL. For example,
     `S3://company.test/DOC-EXAMPLE-BUCKET/motion
     overlay.mov`
