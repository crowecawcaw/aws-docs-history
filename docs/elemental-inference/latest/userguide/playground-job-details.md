

# Viewing job results

Every job appears in the **Playground Jobs** table. The **Feature** column shows whether a job is **Smart Cropping** or **All features**. A job's status is one of the following:
+ **Queued** – The job is waiting in the playground queue.
+ **Processing** – MediaConvert is running a Smart Cropping job, or preparing a preview's clip.
+ **In progress** – A preview is running.
+ **Complete** – A Smart Cropping job wrote its output, or a preview finished and its results are saved.
+ **Not finished** – A preview ended without saved results, for example because you stopped it, it failed, or you closed its tab. Open it and choose **Run again**.
+ **Canceled** – The job was canceled, or a preview was stopped before MediaConvert finished preparing its clip. That can happen after **Analyzing clip** has started.
+ **Error** – The MediaConvert job failed. Open the job to see why.

To open a job, choose its job ID. A saved preview opens with its results, without running again. If MediaConvert had to prepare a preview's clip again, for example because you stopped the preview early and ran it again, the table shows one row with the newest attempt's status. To see the earlier attempts, choose the information icon next to the status. Each one opens its own **Job details** page.

For a Smart Cropping job:
+ When the job is complete, the **Original video** and the **Smart crop output** play side by side.
+ The following actions are available:
  + **Duplicate job** opens the **Create job** page with this job's settings filled in. Nothing is submitted until you choose **Create job**.
  + **View in MediaConvert** opens the job in the MediaConvert console.
+ If your browser can't play the video because its format or codec isn't supported, the job still succeeded. View the output in MediaConvert, or download it from Amazon S3.