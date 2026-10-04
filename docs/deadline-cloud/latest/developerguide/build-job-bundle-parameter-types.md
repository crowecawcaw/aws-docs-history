

# Job parameter types
<a name="build-job-bundle-parameter-types"></a>

Each entry in a job template's `parameterDefinitions` list declares one job parameter. Every parameter has a `name` and a `type`, and can have a `description`, a `default`, and a `userInterface` block with a `label`, a `groupLabel`, and a `control`. The type determines which values the parameter accepts, which constraint fields it supports, and which control the submission dialog shows for it by default. A template refers to the value as `{{Param.{{Name}}}}`. The types are as follows.

Some types are part of the base Open Job Description specification. The rest are added by the `EXPR` extension, and a template that uses them must list `EXPR` in its `extensions`. For the field-by-field definition of each type, see the [Open Job Description job parameter definitions](https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas#2-jobparameterdefinition) on the GitHub website.

`INT`  
An integer, as a number or a numeric string. Constraints: `allowedValues`, `minValue`, `maxValue`. Control: `SPIN_BOX`, or `DROPDOWN_LIST` when `allowedValues` is set.

`FLOAT`  
A number, as a number or a numeric string. Constraints: `allowedValues`, `minValue`, `maxValue`. Control: `SPIN_BOX`, or `DROPDOWN_LIST` when `allowedValues` is set. The `decimals` field sets the number of editable decimal places.

`STRING`  
A string. Constraints: `allowedValues`, `minLength`, `maxLength`. Control: `LINE_EDIT`, or `DROPDOWN_LIST` when `allowedValues` is set. Also accepts `MULTILINE_EDIT`, and `CHECK_BOX` when `allowedValues` holds a true/false pair such as `["true", "false"]`.

`PATH`  
A file or directory path. Path mapping rules are applied to the value on the worker. Constraints: `allowedValues`, `minLength`, `maxLength`, `objectType`, `dataFlow`. Control: `CHOOSE_INPUT_FILE`, `CHOOSE_OUTPUT_FILE`, or `CHOOSE_DIRECTORY`, depending on `objectType` and `dataFlow`.

`BOOL` (requires `EXPR`)  
`true` or `false`; the numbers `1` or `0`; or the strings `true`, `yes`, `on`, `1`, `false`, `no`, `off`, `0` in any letter case. No constraints. Control: `CHECK_BOX`.

`RANGE_EXPR` (requires `EXPR`)  
An integer range expression such as `"1-100"`, `"1-100:10"`, or `"1,3,5-9"`. Constraints: `minLength`, `maxLength`. Control: `LINE_EDIT`.

`LIST[STRING]` (requires `EXPR`)  
A list of strings. Constraints: `minLength` and `maxLength` for the list; `item.allowedValues`, `item.minLength`, and `item.maxLength` for each item. Control: `LINE_EDIT_LIST`.

`LIST[PATH]` (requires `EXPR`)  
A list of paths. Path mapping rules are applied to each value. Constraints: the list and item constraints of `LIST[STRING]`, plus `objectType` and `dataFlow`. Control: `CHOOSE_INPUT_FILE_LIST`, `CHOOSE_OUTPUT_FILE_LIST`, or `CHOOSE_DIRECTORY_LIST`, depending on `objectType` and `dataFlow`.

`LIST[INT]`, `LIST[FLOAT]` (requires `EXPR`)  
A list of numbers. Constraints: `minLength` and `maxLength` for the list; `item.allowedValues`, `item.minValue`, and `item.maxValue` for each item. Control: `SPIN_BOX_LIST`.

`LIST[BOOL]` (requires `EXPR`)  
A list of boolean values, each accepting the same values as `BOOL`. Constraints: `minLength`, `maxLength`. Control: `CHECK_BOX_LIST`.

`LIST[LIST[INT]]` (requires `EXPR`)  
A list of integer lists, for structured input such as an adjacency list. Constraints: nested `item` constraints. Control: `HIDDEN`; there is no visual control for this type.

Every type also accepts `HIDDEN` as its control, which keeps the parameter out of the submission dialog. Set `HIDDEN` for values that a pipeline supplies programmatically.

The `PATH` and `LIST[PATH]` types carry two extra fields. `objectType` is `FILE` or `DIRECTORY`, and `dataFlow` is `IN`, `OUT`, `INOUT`, or `NONE`. Job attachments read these fields to decide which paths to upload as inputs and which to watch for outputs. A `PATH` parameter also supports `fileFilters` and `fileFilterDefault` for the file dialog. For more information, see [Job template elements for job bundles](build-job-bundle-template.md).

The following definitions show a checkbox, a frame range, a list of camera names, and a list of input files. The template lists `EXPR` because the last four types require it.

```
specificationVersion: 'jobtemplate-2023-09'
extensions:
  - EXPR
parameterDefinitions:
  - name: Samples
    type: INT
    default: 64
    minValue: 1
    maxValue: 4096
  - name: UseGpu
    type: BOOL
    default: false
    userInterface:
      label: Render on GPU
  - name: Frames
    type: RANGE_EXPR
    default: "1-100"
    userInterface:
      label: Frame Range
  - name: Cameras
    type: LIST[STRING]
    default: ["main", "closeup"]
    minLength: 1
    userInterface:
      label: Cameras to Render
  - name: Textures
    type: LIST[PATH]
    objectType: FILE
    dataFlow: IN
    default: []
```

In a template with the `EXPR` extension, each parameter has a matching expression type: `int`, `float`, `string`, `path`, `bool`, `range_expr`, or `list[{{T}}]`. A `RANGE_EXPR` or list parameter can be the `range` of a task parameter directly, so that each frame or item becomes a task. For `PATH` and `LIST[PATH]`, `RawParam.{{Name}}` is the value as submitted, as a string, before path mapping.

```
steps:
  - name: Render
    parameterSpace:
      taskParameterDefinitions:
        - name: Camera
          type: STRING
          range: "{{Param.Cameras}}"
        - name: Frame
          type: INT
          range: "{{Param.Frames}}"
    script:
      actions:
        onRun:
          command: render
          args:
            - "--camera"
            - "{{Task.Param.Camera}}"
            - "--frame"
            - "{{Task.Param.Frame}}"
            - "--samples"
            - "{{Param.Samples}}"
            - "{{ '--gpu' if Param.UseGpu else null }}"
            - "{{ ['--textures', Param.Textures.join(',')] if len(Param.Textures) > 0 else null }}"
```

The last two arguments are expressions. A `null` result adds no argument, and a list result adds each item as a separate argument. For more information, see [Expressions in job templates](build-job-bundle-expressions.md).

To submit a job bundle that uses the `EXPR` parameter types, the Deadline Cloud CLI and the submission dialog in `deadline bundle gui-submit` and the Deadline Cloud monitor must be a version that supports the extension. Older clients reject templates with these types.