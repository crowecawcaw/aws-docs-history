# Task chunking for job templates

Task chunking lets you group multiple tasks into a single unit of work called a chunk.
In a render job, for example, this means Deadline Cloud can dispatch multiple frames together instead
of one frame per command invocation. This reduces the overhead of starting applications for
each task and shortens total job runtime. For details, see [Running multiple frames at a time](https://github.com/OpenJobDescription/openjd-specifications/wiki/Job-Intro-03-Creating-a-Job-Template#42-running-multiple-frames-at-a-time "https://github.com/OpenJobDescription/openjd-specifications/wiki/Job-Intro-03-Creating-a-Job-Template#42-running-multiple-frames-at-a-time") in the OpenJD wiki.

OpenJD supports extensions that add optional features to job templates. Task chunking is
enabled by adding the `TASK_CHUNKING` extension. To use chunking, add the extension
to your job template and use the `CHUNK[INT]` task parameter type. Submit chunked
jobs using the same `deadline bundle submit` command. For example, the following
job template renders frames in chunks of 10:

```
specificationVersion: 'jobtemplate-2023-09'
extensions:
  - TASK_CHUNKING
name: Blender Render with Contiguous Chunking
parameterDefinitions:
  - name: BlenderSceneFile
    type: PATH
    objectType: FILE
    dataFlow: IN
  - name: Frames
    type: STRING
    default: "1-100"
  - name: OutputDir
    type: PATH
    objectType: DIRECTORY
    dataFlow: OUT
    default: "./output"
steps:
  - name: RenderBlender
    parameterSpace:
      taskParameterDefinitions:
        - name: Frame
          type: CHUNK[INT]
          range: "{{Param.Frames}}"
          chunks:
            defaultTaskCount: 10
            rangeConstraint: CONTIGUOUS
    script:
      actions:
        onRun:
          command: bash
          args: ["{{Task.File.Run}}"]
      embeddedFiles:
        - name: Run
          type: TEXT
          data: |
            set -xeuo pipefail

            mkdir -p '{{Param.OutputDir}}'

            # Parse the chunk range (e.g., "1-10") into start and end frames
            START_FRAME="$(echo '{{Task.Param.Frame}}' | cut -d- -f1)"
            END_FRAME="$(echo '{{Task.Param.Frame}}' | cut -d- -f2)"

            blender --background '{{Param.BlenderSceneFile}}' \
                    --render-output '{{Param.OutputDir}}/output_####' \
                    --render-format PNG \
                    --use-extension 1 \
                    -s "$START_FRAME" \
                    -e "$END_FRAME" \
                    --render-anim
```

In this example, Deadline Cloud divides the 100 frames into chunks like `1-10`,
`11-20`, and so on. The `{{Task.Param.Frame}}` variable expands to a
range expression like `1-10`. Because `rangeConstraint` is set to
`CONTIGUOUS`, the range is always in `start-end` format. The script
parses this range and passes the start and end frames to Blender using the `-s`
and `-e` options with `--render-anim`.

The `chunks` property supports the following fields:

- `defaultTaskCount` – (Required) How many tasks to combine into a
  single chunk. The maximum value is 150.
- `rangeConstraint` – (Required) If `CONTIGUOUS`, a chunk
  is always a contiguous range like `1-10`. If `NONCONTIGUOUS`, a
  chunk can be an arbitrary set like `1,3,7-10`.
- `targetRuntimeSeconds` – (Optional) The target runtime in seconds
  for each chunk. Deadline Cloud can dynamically adjust the chunk size to approach this target once
  some chunks have completed.
  For more task chunking examples, including basic and Blender examples with both
  contiguous and non-contiguous chunks, see the [task
  chunking samples](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/task_chunking "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/task_chunking") in the Deadline Cloud samples repository on GitHub.

###### Customer-managed fleet requirements

Task chunking requires a compatible worker agent version. If you use customer-managed
fleets, ensure your worker agents are updated before submitting jobs with chunking.
Service-managed fleets always use a compatible worker agent version.

###### Downloading output for chunked jobs

When you download output for a single task in a chunked job, Deadline Cloud downloads the output
for the entire chunk. For example, if frames 1-10 were processed together, downloading the
output for frame 3 includes all frames 1-10. This feature requires `deadline-cloud`
version 0.53.3 or later.
