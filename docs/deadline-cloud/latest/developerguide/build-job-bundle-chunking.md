

# Task chunking for job templates
<a name="build-job-bundle-chunking"></a>

Render and simulation jobs often spend more time loading the application and scene file than processing each frame. When a job runs one frame per task, that load time repeats for every frame. *Task chunking* groups multiple tasks into a single unit of work called a *chunk*, so the application loads once for each chunk instead of once for each frame. Chunking helps most when the load time is long relative to the time to process each frame, such as a scene that loads for minutes and then renders each frame in seconds.

If you're migrating from Deadline 10, task chunking replaces the frames per task setting, also called chunk size, in the Deadline 10 submitters.

Task chunking is an extension to Open Job Description (OpenJD) named `TASK_CHUNKING`. In a job template that uses the extension, you define a task parameter with type `CHUNK[INT]`. When the job runs, Deadline Cloud dispatches a range of values to each task instead of a single value, and the `{{Task.Param.Frame}}` variable in your script expands to a range expression such as `1-10`. Your script passes that range to the application. For the full specification, see [RFC 0001: Task Chunking](https://github.com/OpenJobDescription/openjd-specifications/blob/mainline/rfcs/0001-task-chunking.md) on the GitHub website.

To use task chunking, you make two decisions:
+ **Range constraint** – Choose `CONTIGUOUS` when your application accepts start and end frame arguments. Every chunk is then a consecutive range such as `1-10`. Choose `NONCONTIGUOUS` when your application accepts arbitrary frame lists. Chunks can then cover sparse frame sets such as `1-3,5,7-20:2`, which is useful when rendering pick-up frames.
+ **Chunk size** – The `defaultTaskCount` field sets a fixed number of frames for each chunk. If chunks are too small, load time dominates and the job runs inefficiently. If chunks are too large, the job can't balance work across a larger fleet. To avoid tuning the value by hand, set the optional `targetRuntimeSeconds` field. Deadline Cloud then adjusts chunk sizes toward that target runtime based on the observed runtimes of completed chunks.

Chunk size also caps parallelism. A step produces one task for each chunk, which is approximately the frame count divided by the chunk size, and each task runs on one worker. The following table shows how the chunk size limits the number of workers that can process a 100-frame job in parallel.


| Frames in job | Chunk size | Tasks (maximum parallel workers) | 
| --- | --- | --- | 
| 100 | 1 | 100 | 
| 100 | 10 | 10 | 
| 100 | 50 | 2 | 

If the chunk size is larger than the frame count divided by the number of available workers, some workers stay idle. When you set `targetRuntimeSeconds`, Deadline Cloud balances this trade-off for you by adjusting chunk sizes toward the target runtime.

Chunked jobs differ from one-frame-per-task jobs in two ways. In the Deadline Cloud monitor, the step's task list shows one task for each chunk, identified by its frame range. When you download the output for a single task in a chunked job, Deadline Cloud downloads the output for the entire chunk. For example, if Deadline Cloud processed frames 1-10 together as a chunk, downloading the output for frame 3 downloads all of frames 1-10. Downloading chunked output requires `deadline-cloud` version 0.53.3 or later.

For more information about task chunking, see the following topics:
+ [Add task chunking to a job template](build-job-bundle-chunking-add.md) – Convert an existing job template to use chunking.
+ [CHUNK[INT] task parameter reference](build-job-bundle-chunking-reference.md) – Look up every field of the `CHUNK[INT]` parameter.
+ [Group frames into chunks with task chunking on Deadline Cloud](examples-jb-task-chunking.md) – Run ready-made chunking samples.