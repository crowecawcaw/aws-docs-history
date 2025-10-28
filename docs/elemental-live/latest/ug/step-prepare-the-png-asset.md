# Step A: Prepare the png

asset

1. Create a file – Use a third-party process to convert
   an animation asset to a series of PNG files.
2. Take care with these aspects of the conversion:
   - File count: When you insert the files into the video,
     you will specify the frame rate for the motion overlay.
     Therefore, make sure that the conversion results in a
     file count that aligns with the intended frame rate.
     (The frame rate of the motion overlay does not
     necessarily have to match the frame rate of the
     underlying video.) For example, if the motion overlay
     will run for 10 seconds at 30 frames/second, make sure
     that the conversion produces 300 files. If the file
     count and frame rate do not align, the quality of the
     animation might suffer.
   - The PNG files must contain RGB and one alpha channel.
     The alpha channel will be used for per-pixel
     blending.
   - File names: Make sure that the file names of the converted files include
     a sequential number. Numbering must start at 0. There can be any number of
     digits in the numerical part of the file name, as long as it is the same for
     each file. For example, 000 to 200 (three digits in both files) but not 00
     to 200 (two digits in one file and three digits in the other file).
   - Aspect ratio: The motion overlay can have any aspect
     ratio. It does not have to match the aspect ratio of the
     video output.
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

3. Place the file – Place the converted file in a
   location accessible to Elemental Live: On a local directory, on
   a remote filesystem accessible via mount point, or in an Amazon S3
   bucket. Choose a location as described in [Fields for a PNG asset](png-set-up-event-fields.md "png-set-up-event-fields.md"), then note the location
   for setting up the motion overlay in the event.

You can specify the location in one of the following ways:

    * Local to the Elemental Live appliance. For example,
     `/data/assets/motion
     overlay_001.png`
    * A remote server via a mount point. For example,
     `/data/mnt/assets/motion
     overlay_001.png`
    * An Amazon S3 bucket, using SSL. For example,
     `Amazon S3ssl://company.test/DOC-EXAMPLE-BUCKET/motion
     overlay_001.png`
    * An Amazon S3 bucket, without SSL. For example,
     `S3://company.test/DOC-EXAMPLE-BUCKET/motion
     overlay_001.png`
