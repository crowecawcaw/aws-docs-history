# Add task chunking to a job template

The following procedure converts a job template that renders one frame per task into
one that renders chunks of frames. For background on chunking and how to choose a chunk
size, see [Task chunking for job templates](build-job-bundle-chunking.md "build-job-bundle-chunking.md").

Before you begin, you need the following:

- A job bundle with a job template that defines a frame task parameter. For more
  information, see [Job template elements for job bundles](build-job-bundle-template.md "build-job-bundle-template.md").
- A queue associated with a fleet that supports chunking. Service-managed fleets
  always run a compatible worker agent. Customer-managed fleets require worker agent
  version 0.28.21 or later on the workers.

###### To add task chunking to a job template

1. Add the `TASK_CHUNKING` extension to the top of your
   `template.yaml` file:

```
specificationVersion: 'jobtemplate-2023-09'
extensions:
  - TASK_CHUNKING
```

If you skip this step, job creation fails with the error `The CHUNK[INT] task
 parameter requires the TASK_CHUNKING extension.` 2. In the step's `parameterSpace`, change the frame task parameter type
from `INT` to `CHUNK[INT]` and add the `chunks`
property:

```
taskParameterDefinitions:
  - name: Frame
    type: CHUNK[INT]
    range: "{{Param.Frames}}"
    chunks:
      defaultTaskCount: 10
      rangeConstraint: CONTIGUOUS
```

For all of the available fields, see [CHUNK[INT] task parameter reference](build-job-bundle-chunking-reference.md "build-job-bundle-chunking-reference.md"). 3. Update the step's script to accept a frame range instead of a single frame. With
`rangeConstraint: CONTIGUOUS`, the `{{Task.Param.Frame}}`
variable always expands to a range in `start-end` format, so the script can
split it with the `cut` command:

```
START_FRAME="$(echo '{{Task.Param.Frame}}' | cut -d- -f1)"
END_FRAME="$(echo '{{Task.Param.Frame}}' | cut -d- -f2)"
```

With `rangeConstraint: NONCONTIGUOUS`, the variable expands to an
arbitrary range expression such as `1-3,5,7-20:2`. Transform the expression
into the syntax that your application accepts. For a working transformation, see the
[task chunking samples](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/task_chunking "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/task_chunking") on GitHub. 4. Submit the job bundle with the Deadline Cloud CLI:

```
deadline bundle submit `my-job-bundle`
```

5. To verify that chunking is in effect, open the job in the Deadline Cloud monitor and view the
   step's task list. Each task represents one chunk and shows a frame range such as
   `1-10` instead of a single frame number.
   The following complete job template renders a Blender animation in chunks of 10
   frames:

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

In this example, Deadline Cloud divides the 100 frames into chunks such as `1-10`
and `11-20`, and each task renders its chunk with a single Blender
invocation.

For more information, see the following topics:

- [Group frames into chunks with task chunking on Deadline Cloud](examples-jb-task-chunking.md "examples-jb-task-chunking.md") – Ready-to-submit chunking
  samples, including a non-contiguous variant.
- [How to submit a job to Deadline Cloud](submit-jobs-how.md "submit-jobs-how.md") –
  Submit the job bundle to your queue.
