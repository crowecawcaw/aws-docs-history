# Step A:

Prepare the overlay asset

1.  Create a file with the following characteristics:
    - File type: A BMP, PNG, or TGA file.
    - Aspect ratio: The overlay can have any aspect ratio. It does not have
      to match the aspect ratio of the underlying video.
    - Size, in pixels: The overlay can be any size up to the same size as
      the underlying video. The overlay cannot be positioned so that part of
      the overlay runs beyond the right edge or bottom edge of the underlying
      video.
      - If you set up an overlay so that it is too big or it overruns an
        edge, if Elemental Live can identify this error at event creation time,
        an error message will appear then.
      - If Elemental Live cannot identify the error in advance, an error
        message will appear while the event is running. The event will not
        stop but the insertion request will fail.

2.  Place the prepared file in a location accessible to the Elemental Live
    node. You can specify the location in one of the following
    ways:

        * Local to the Elemental Live appliance. E.g.
         `/data/assets/overlay.mov`
        * A remote server via a mount point. E.g.
         `/data/mnt/assets/overlay.mov`
        * An S3 bucket, using SSL. E.g.
         `s3ssl://company.test/sample_bucket/overlay.mov`
        * An S3 bucket, without SSL. E.g.
         `s3://company.test/sample_bucket/overlay.mov`

    Use sse=true to enable S3 Server Side Encryption (SSE) and
    rrs=true to enable Reduced Redundancy Storage (RRS). Default values
    for RRS and SSE are false.

Example: `s3://<hostname>/sample_bucket/
 encrypted?rrs=true&sse=true` 3. Make a note of the location.
