# Job template elements for job bundles

The job template defines the runtime environment and the processes that run as part of a
 Deadline Cloud job. You can create parameters in a template so that it can be used to create jobs that
 differ only in input values, much like a function in a programming language.

When you submit a job to Deadline Cloud, it runs in any queue environments applied to the queue.
 Queue environments are built using the Open Job Description (OpenJD) external environments
 specification. For details, see the [Environment template](https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas#12-environment-template "https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas#12-environment-template") in the OpenJD GitHub repository.

For an introduction creating a job with an OpenJD job template, see [Introduction to creating a job](https://github.com/OpenJobDescription/openjd-specifications/wiki/Introduction-to-Creating-a-Job "https://github.com/OpenJobDescription/openjd-specifications/wiki/Introduction-to-Creating-a-Job") in the OpenJD GitHub repository. Additional
 information can be found in [How
 jobs are run](https://github.com/OpenJobDescription/openjd-specifications/wiki/How-Jobs-Are-Run "https://github.com/OpenJobDescription/openjd-specifications/wiki/How-Jobs-Are-Run"). There are job template samples in the in the OpenJD GitHub
 repository's `samples` directory.

You can define the job template in either YAML format (`template.yaml`) or JSON
 format (`template.json`). The examples in this section are shown in YAML
 format.

For example, the job template for the `blender_render` sample defines an input
 parameter `BlenderSceneFile` as a file path:


```
- name: BlenderSceneFile
  type: PATH
  objectType: FILE
  dataFlow: IN
  userInterface:
    control: CHOOSE_INPUT_FILE
    label: Blender Scene File
    groupLabel: Render Parameters
    fileFilters:
    - label: Blender Scene Files
      patterns: ["*.blend"]
    - label: All Files
      patterns: ["*"]
  description: >
    Choose the Blender scene file to render. Use the 'Job Attachments' tab
    to add textures and other files that the job needs.
```
The `userInterface` property defines the behavior of automatically generated
 user interfaces for both the command line using the `deadline bundle gui-submit`
 command and within the job submission plugins for applications like Autodesk Maya.

In this example, the UI widget for inputting a value for the `BlenderSceneFile`
 parameter is a file-selection dialog that shows only `.blend` files.


![A user-interface widget for entering the scene file parameter for an OpenJD job template.](/images/deadline-cloud/latest/developerguide/images/blender_submit_scene_file_widget.png)
For more examples of using the `userInteface` element, see the [gui\_control\_showcase](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/gui_control_showcase "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/gui_control_showcase") sample in the [deadline-cloud-samples](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline") repository on GitHub.

The `objectType` and `dataFlow` properties control the behavior of
 job attachments when you submit a job from a job bundle. In this case, `objectType:
 FILE` and `dataFlow:IN` mean that the value of
 `BlenderSceneFile` is an input file for job attachments.

In contrast, the definition of the `OutputDir` parameter has `objectType:
 DIRECTORY` and `dataFlow: OUT`:


```
- name: OutputDir
  type: PATH
  objectType: DIRECTORY
  dataFlow: OUT
  userInterface:
    control: CHOOSE_DIRECTORY
    label: Output Directory
    groupLabel: Render Parameters
  default: "./output"
  description: Choose the render output directory.
```
The value of the `OutputDir` parameter is used by job attachments as the
 directory where the job writes output files.

For more information about the `objectType` and `dataFlow`
 properties, see [JobPathParameterDefinition](https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas#22-jobpathparameterdefinition "https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas#22-jobpathparameterdefinition") in the [Open Job Description
 specification](https://github.com/OpenJobDescription/openjd-specifications "https://github.com/OpenJobDescription/openjd-specifications")

The rest of the `blender_render` job template sample defines the job's workflow
 as a singe step with each frame in the animation rendered as a separate task:


```
steps:
- name: RenderBlender
  parameterSpace:
    taskParameterDefinitions:
    - name: Frame
      type: INT
      range: "{{Param.Frames}}"
  script:
    actions:
      onRun:
        command: bash
        # Note: {{Task.File.Run}} is a variable that expands to the filename on the worker host's
        # disk where the contents of the 'Run' embedded file, below, is written.
        args: ['{{Task.File.Run}}']
    embeddedFiles:
      - name: Run
        type: TEXT
        data: |
          # Configure the task to fail if any individual command fails.
          set -xeuo pipefail

          mkdir -p '{{Param.OutputDir}}'

          blender --background '{{Param.BlenderSceneFile}}' \
                  --render-output '{{Param.OutputDir}}/{{Param.OutputPattern}}' \
                  --render-format {{Param.Format}} \
                  --use-extension 1 \
                  --render-frame {{Task.Param.Frame}}
```
For example, if the value of the `Frames` parameter is `1-10`, it
 defines 10 tasks. Each has task has a different value for the `Frame` parameter. To
 run a task:


1. All of the variable references in the `data` property of the embedded file
 are expanded, for example `--render-frame 1`.
2. The contents of the `data` property is written to a file in the session
 working directory on disk.
3. The task's `onRun` command resolves to `bash `location of
 embedded file`` and then runs.
For more information about embedded files, sessions, and path-mapped locations, see [How
 jobs are run](https://github.com/OpenJobDescription/openjd-specifications/wiki/How-Jobs-Are-Run "https://github.com/OpenJobDescription/openjd-specifications/wiki/How-Jobs-Are-Run") in the [Open
 Job Description specification](https://github.com/OpenJobDescription/openjd-specifications/wiki/How-Jobs-Are-Run "https://github.com/OpenJobDescription/openjd-specifications/wiki/How-Jobs-Are-Run").

There are more examples of job templates in the [deadline-cloud-samples/job\_bundles](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles") repository, as well as the [template samples](https://github.com/OpenJobDescription/openjd-specifications/tree/mainline/samples "https://github.com/OpenJobDescription/openjd-specifications/tree/mainline/samples") provided with the Open Job Descriptions specification.
