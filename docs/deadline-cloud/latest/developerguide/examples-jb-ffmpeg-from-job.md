# Encode a movie from another Deadline Cloud job's output with FFmpeg

The
[ffmpeg\_movie\_from\_job\_output](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/ffmpeg_movie_from_job_output "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/ffmpeg_movie_from_job_output")
job bundle on the GitHub website downloads the rendered output of another completed job in
the same queue and encodes the image sequence into an MP4 video using
FFmpeg. Use it as a post-processing utility, for example, to
automatically assemble frames into a movie after a Blender or Maya
render job completes.

For encoding a local image sequence (no source-job download), see
[Encode video with FFmpeg on Deadline Cloud](examples-jb-ffmpeg-encode.md "examples-jb-ffmpeg-encode.md").

A pre-submission hook (`inject_s3_settings.py`) runs at
submission time on your workstation and looks up the queue's job
attachment Amazon Simple Storage Service (Amazon S3) bucket configuration. The hook writes the
settings to a JSON file that gets uploaded as a job attachment, so the
worker can download files from Amazon S3 without needing Deadline Cloud API
permissions on the queue role. On the worker, the job uses the
`deadline.job_attachments` Python API to download the source
job's output, then runs FFmpeg to encode the frames into an H.264 MP4
with BT.709 color space metadata.

Bundle hooks are off by default. Enable them once before
submitting:

```
deadline config set settings.allow_bundle_hooks true
```

The job requires FFmpeg from the `conda-forge` conda
channel. The source job and this job must be in the same queue,
because they share the same job attachments Amazon S3 bucket.

Submit with the source job's ID:

```
deadline bundle submit ffmpeg_movie_from_job_output/ \
  -p SourceJobId=`job-id` \
  -p FrameRate=30 \
  -p OutputFilename=my_render.mp4
```

To restrict the download to a single step's output, also pass
`SourceStepId`.
