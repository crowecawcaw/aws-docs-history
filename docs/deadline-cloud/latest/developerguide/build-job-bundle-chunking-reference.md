

# CHUNK[INT] task parameter reference
<a name="build-job-bundle-chunking-reference"></a>

The `CHUNK[INT]` task parameter type defines an integer task parameter that Deadline Cloud processes as chunks instead of as individual values. A chunked task parameter has the following structure:

```
taskParameterDefinitions:
  - name: {{identifier}}
    type: CHUNK[INT]
    range: {{integer range expression}}
    chunks:
      defaultTaskCount: {{integer}}
      rangeConstraint: CONTIGUOUS | NONCONTIGUOUS
      targetRuntimeSeconds: {{integer}}
```

The following table describes each field.


| Field | Required | Description | 
| --- | --- | --- | 
| range | Yes | The full set of integer values to process, as a list of integers or an integer range expression such as "1-100" or "1,3,7-20:2". Accepts a job parameter reference such as "{{Param.Frames}}". | 
| chunks.defaultTaskCount | Yes | The number of values to combine into a single chunk. The maximum value is 150. Accepts a job parameter reference such as "{{Param.ChunkSize}}". | 
| chunks.rangeConstraint | Yes | The shape of each chunk. With CONTIGUOUS, every chunk is a consecutive range such as 1-10. With NONCONTIGUOUS, a chunk can be an arbitrary set such as 1,3,7-10. | 
| chunks.targetRuntimeSeconds | No | The target runtime for each chunk, in seconds. When set, Deadline Cloud adjusts chunk sizes toward the target based on the observed runtimes of completed chunks. When not set, every chunk uses defaultTaskCount values. | 

The `CHUNK[INT]` type has the following constraints:
+ The job template must list `TASK_CHUNKING` in its `extensions`. Without the extension, job creation fails with the error `The CHUNK[INT] task parameter requires the TASK_CHUNKING extension.`
+ A step's parameter space can contain at most one `CHUNK[INT]` parameter. When a chunk runs, all other task parameters take on a single value while the chunked parameter takes a set of values.

In a step's script, the `{{Task.Param.{{name}}}}` variable for a chunked parameter expands to an integer range expression string. With `rangeConstraint: CONTIGUOUS`, the expression is always in `{{start}}-{{end}}` format, such as `1-1` or `11-20`. With `rangeConstraint: NONCONTIGUOUS`, the expression can be any integer range expression, such as `1-3,5,7-20:2`.

For more information, see the following resources:
+ [RFC 0001: Task Chunking](https://github.com/OpenJobDescription/openjd-specifications/blob/mainline/rfcs/0001-task-chunking.md) on the GitHub website – The full specification of the extension.
+ [Add task chunking to a job template](build-job-bundle-chunking-add.md) – Convert a job template to use chunking.