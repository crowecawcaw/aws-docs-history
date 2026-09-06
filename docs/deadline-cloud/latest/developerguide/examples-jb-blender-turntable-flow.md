

# Publish renders to Autodesk Flow Production Tracking from Deadline Cloud
<a name="examples-jb-blender-turntable-flow"></a>

The [blender\_turntable\_to\_flow](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/blender_turntable_to_flow) job bundle on the GitHub website demonstrates how to integrate Deadline Cloud with Autodesk Flow Production Tracking (formerly ShotGrid). The bundle renders frames, encodes a review-ready movie, extracts a thumbnail, and publishes the result to Flow as a new Version on an Asset's review Task. The render step uses a Blender turntable as a placeholder — replace it with any renderer to adapt this pattern for your pipeline. For more information about Flow Production Tracking, see [Flow Production Tracking overview](https://www.autodesk.com/products/flow-production-tracking/overview) on the Autodesk website.

The bundle demonstrates two core patterns for render-and-publish pipelines on Deadline Cloud:
+ Post-render work modeled as discrete job steps (movie encode, thumbnail generation, publish) that are independently observable, retryable, and schedulable.
+ Chained, dependent, non-render tasks that run after a render and fan out in parallel.

The step graph:

```
RenderTurntable  (one task per frame)
   ├─ GenerateMovie      (ffmpeg frames → H.264 mp4)
   ├─ GenerateThumbnail  (mid frame → jpg)
   └─ PublishToFlow      (depends on movie + thumbnail)
```

The job needs Blender, FFmpeg, and Python. Configure a conda queue environment with `blender ffmpeg python>=3.10 pip` on channels `deadline-cloud conda-forge`. Flow credentials are stored in AWS Secrets Manager (Secrets Manager) and read at runtime by the queue role.

A submission hook (`hooks.yaml`) reads Flow parameters from environment variables (`FLOW_PROJECT_ID`, `FLOW_ASSET_NAME`, `FLOW_SECRET_ARN`) so artists don't manually enter project metadata. Enable bundle hooks before first use:

```
deadline config set settings.allow_bundle_hooks true
```

Submit the job:

```
deadline bundle gui-submit blender_turntable_to_flow
```