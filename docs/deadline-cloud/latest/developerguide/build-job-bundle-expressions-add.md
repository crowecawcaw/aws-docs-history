

# Add expressions to a job template
<a name="build-job-bundle-expressions-add"></a>

The following procedure adds expressions to a job template that renders a Blender animation. It derives the output file pattern from the scene file name, quotes paths for bash, and requests a GPU worker and switches the render device when you select a checkbox. For background on expressions and when to use them, see [Expressions in job templates](build-job-bundle-expressions.md).

Before you begin, you need the following:
+ A job bundle with a job template. For more information, see [Job template elements for job bundles](build-job-bundle-template.md).
+ The `openjd` command-line tool, to check a template before you submit it. Install it with `pip install openjd-cli`. For more information, see the [openjd-cli repository](https://github.com/OpenJobDescription/openjd-cli) on the GitHub website.

**To add expressions to a job template**

1. Add the `EXPR` extension to the top of your `template.yaml` file. To use expressions in `hostRequirements`, also add `FEATURE_BUNDLE_1`, which allows format strings in host requirement fields:

   ```
   specificationVersion: 'jobtemplate-2023-09'
   extensions:
     - EXPR
     - FEATURE_BUNDLE_1
   ```

   If you skip this step, any `{{ }}` that contains more than a parameter reference fails validation, because the base specification accepts only references such as `{{Param.Frames}}`.

1. Write an expression where the template needs a computed value. For example, build the output pattern from the scene file name with a path expression. Use `repr_sh` to quote values that a bash script receives:

   ```
   blender --background {{repr_sh(Param.BlenderSceneFile)}} \
           --render-output {{repr_sh(Param.OutputDir / Param.BlenderSceneFile.stem + '_####')}}
   ```

   For a `PATH` parameter, `.stem` is the file name without its extension, and `/` joins path components. For all of the available operations, see [Expression quick reference](build-job-bundle-expressions-reference.md).

1. To reuse a computed value in several places, bind it to a name in a `let` block on the step's `script`. Names you define start with a lowercase letter, which keeps them distinct from the `Param` and `Task` variables:

   ```
   script:
     let:
       - output_pattern = Param.OutputDir / (Param.BlenderSceneFile.stem + '_####')
     actions:
       onRun:
         command: bash
         args: ["{{Task.File.Run}}"]
   ```

   The name is then available as `{{output_pattern}}` in the step's actions and embedded files.

1. To add an argument only when a parameter is set, write a conditional that evaluates to `null` in the other case. In an `args` list, a `null` item is dropped:

   ```
   args:
     - "--frame"
     - "{{Task.Param.Frame}}"
     - "{{ '--gpu' if Param.UseGpu else null }}"
   ```

   A host requirement can use the same parameter. The capability `name` is also an expression, so one requirement can ask for a GPU when the checkbox is selected and for a CPU otherwise:

   ```
   hostRequirements:
     amounts:
       - name: "{{ 'amount.worker.gpu' if Param.UseGpu else 'amount.worker.vcpu' }}"
         min: 1
   ```

   Deadline Cloud resolves the name when it creates the job and checks that the result is a valid capability name.

1. Check the template before you submit it. The `openjd check` command parses every expression and type-checks it against the declared parameter types:

   ```
   openjd check template.yaml
   ```

   To see the expanded commands for a specific set of parameter values, run one task locally:

   ```
   openjd run template.yaml --step RenderBlender \
       -p BlenderSceneFile={{/path/to/scene.blend}} \
       -p UseGpu=true \
       --tasks '[{"Frame": 1}]'
   ```

1. Submit the job bundle with the Deadline Cloud CLI:

   ```
   deadline bundle submit {{my-job-bundle}}
   ```

   If an expression references a parameter that doesn't exist or applies an operation to the wrong type, the submission fails with a message that shows the expression and points to the error.

The following complete job template puts the pieces together. It renders a Blender animation, names the output after the scene file, and requests a GPU worker and renders on the GPU only when the `UseGpu` checkbox is selected:

```
specificationVersion: 'jobtemplate-2023-09'
extensions:
  - EXPR
  - FEATURE_BUNDLE_1
name: Blender Render with Expressions
parameterDefinitions:
  - name: BlenderSceneFile
    type: PATH
    objectType: FILE
    dataFlow: IN
  - name: Frames
    type: RANGE_EXPR
    default: "1-100"
  - name: OutputDir
    type: PATH
    objectType: DIRECTORY
    dataFlow: OUT
    default: "./output"
  - name: UseGpu
    type: BOOL
    default: false
  - name: Samples
    type: INT
    default: 64
    minValue: 1
steps:
  - name: RenderBlender
    parameterSpace:
      taskParameterDefinitions:
        - name: Frame
          type: INT
          range: "{{Param.Frames}}"
    hostRequirements:
      amounts:
        - name: "{{ 'amount.worker.gpu' if Param.UseGpu else 'amount.worker.vcpu' }}"
          min: 1
    script:
      let:
        - output_pattern = Param.OutputDir / (Param.BlenderSceneFile.stem + '_####')
        - device = 'GPU' if Param.UseGpu else 'CPU'
      actions:
        onRun:
          command: bash
          args: ["{{Task.File.Run}}"]
      embeddedFiles:
        - name: Run
          type: TEXT
          data: |
            set -xeuo pipefail

            mkdir -p {{repr_sh(Param.OutputDir)}}

            blender --background {{repr_sh(Param.BlenderSceneFile)}} \
                    --render-output {{repr_sh(output_pattern)}} \
                    --render-format PNG \
                    --use-extension 1 \
                    --render-frame {{Task.Param.Frame}} \
                    --python-expr {{repr_sh('import bpy; bpy.context.scene.cycles.samples = ' + string(Param.Samples) + '; bpy.context.scene.cycles.device = ' + repr_py(device))}}
```

In this example, submitting with `BlenderSceneFile=/shots/shot010.blend` and `UseGpu=true` requires a worker with at least one GPU and expands the render command. It writes `/shots/output/shot010_####` and sets the Cycles device to `GPU`. With `UseGpu=false`, the requirement becomes at least one vCPU, which any worker satisfies, and the same template renders on the CPU.

For more information, see the following topics:
+ [Job parameter types](build-job-bundle-parameter-types.md) – Define boolean, list, and frame range parameters.
+ [How to submit a job to Deadline Cloud](submit-jobs-how.md) – Submit the job bundle to your queue.
+ The [blender-ffmpeg-expr sample template](https://github.com/OpenJobDescription/openjd-specifications/blob/mainline/samples/v2023-09/job_templates/blender-ffmpeg-expr.yaml) on the GitHub website renders and encodes an animation with path expressions.