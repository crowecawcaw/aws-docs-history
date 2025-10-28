# Configuring a job with Accelerated transcoding

You set up Accelerated transcoding for your AWS Elemental MediaConvert jobs in the same way that you set
up unaccelerated jobs, except that you enable acceleration.

###### Note

We recommend that you use a dedicated transcoding queue for your Accelerated transcoding jobs. This
will provide isolation between the resources that you use for your accelerated jobs
and your other jobs.

###### To set up your transcoding job with Accelerated transcoding (console)

1. Set up your transcoding job as usual. For more information, see [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md").

Make sure that your job input files and output settings conform to the
limitations and requirements listed in [Accelerated transcoding job settings requirements](job-requirements.md "job-requirements.md"). 2. Change your timecode settings from the default value
**Embedded** to **Start at zero**.

    1. On the **Create job** page, in the **Job** pane on the left, under **Job settings**, choose
     **Settings**.
    2. In the **Timecode configuration** pane, for
     **Source**, choose **Start at
     0**.
    3. On the **Create job** page, in the **Job** pane on the left, under **Inputs**, choose the
     input.
    4. In the **Video selector**  pane, for
     **Timecode source**, choose **Start at
     0**.

3. If you don't already have a dedicated queue for Accelerated transcoding jobs, create
   one. For more information, see [Creating a queue](creating-queues.md "creating-queues.md").
4. On the **Create job** page, in the **Job** pane on the left, in the **Job Settings** section, choose
   **Settings**.
5. For **Acceleration**, choose **Enabled** or
   **Preferred**.

With both **Enabled** and **Preferred**, if
your input files and transcoding settings are compatible with accelerated
transcoding, MediaConvert runs the job with Accelerated transcoding.

If your input files or transcoding settings aren't compatible with accelerated
transcoding, MediaConvert handles the job differently, depending on the value
that you set for **Acceleration**:

    * **Enabled** – The service fails the
     incompatible job.
    * **Preferred** – The service runs the job
     without Accelerated transcoding.


    Setting **Acceleration** to
     **Preferred** incurs Professional tier pricing only
     when MediaConvert runs the job with Accelerated transcoding.

For more information about what files and settings are compatible with
Accelerated transcoding, see [Accelerated transcoding job settings requirements](job-requirements.md "job-requirements.md").
If you use the API or an SDK, you can find this setting in the JSON file of your job. The setting name is AccelerationMode, under [AccelerationSettings](../apireference/jobs.md#jobs-prop-createjobrequest-accelerationsetting "../apireference/jobs.md#jobs-prop-createjobrequest-accelerationsetting").
