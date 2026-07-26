# Group frames into chunks with task chunking on Deadline Cloud

The
[task\_chunking](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/task_chunking "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/task_chunking")
samples demonstrate the
[Task
Chunking](https://github.com/OpenJobDescription/openjd-specifications/blob/mainline/rfcs/0001-task-chunking.md "https://github.com/OpenJobDescription/openjd-specifications/blob/mainline/rfcs/0001-task-chunking.md") extension for Open Job Description. Render jobs often
spend significant time loading applications and scene files before
rendering each frame. Chunking amortizes this overhead by processing
multiple frames per chunk, which reduces total job runtime.

The samples include four examples:

basic\_contiguous\_chunks

A minimal example using `rangeConstraint: CONTIGUOUS`.
Each chunk expands to a range like `"1-10"` or
`"11-20"`.

basic\_non\_contiguous\_chunks

A minimal example using `rangeConstraint: NONCONTIGUOUS`.
Chunks can be arbitrary frame sets like
`"1-3,5,7-20:2"`.

blender\_render\_with\_contiguous\_chunks

A real-world example converted from the
[Render Blender scenes on Deadline Cloud](examples-jb-blender-render.md "examples-jb-blender-render.md") bundle to render with
contiguous chunks.

blender\_render\_with\_non\_contiguous\_chunks

A Blender variant with non-contiguous chunks.

Choose a range constraint based on the application:

- `CONTIGUOUS`: Use when the application supports
  start and end frame arguments.
- `NONCONTIGUOUS`: Use when the application supports
  arbitrary frame lists.
  Submit any of the samples with the Deadline Cloud CLI:

```
deadline bundle submit `sample-directory`
```

To learn how task chunking works and how to add it to your own job
templates, see [Task chunking for job templates](build-job-bundle-chunking.md "build-job-bundle-chunking.md").
