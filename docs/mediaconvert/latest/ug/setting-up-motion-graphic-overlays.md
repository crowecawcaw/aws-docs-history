# Configuring motion image insertion

Motion graphic overlays apply to every output in the job. Therefore, set them up
as a processor in the settings that apply to the entire job.

You can set up still graphic overlays that appear only on individual outputs. For
information, see [Choosing between input and output overlays](choosing-between-input-overlay-and-output-overlay.md "choosing-between-input-overlay-and-output-overlay.md").

###### To set up a motion graphic overlay

1. Open the AWS Elemental MediaConvert console at [https://console.aws.amazon.com/mediaconvert](https://console.aws.amazon.com/mediaconvert "https://console.aws.amazon.com/mediaconvert").
2. Set up your job, as described in [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md").
3. On the **Create job** page, in the **Job** pane on the left, under **Job settings**, choose
   **Settings**.
4. In the **Global processors** section to the right of the
   **Job** pane, enable **Motion
   image inserter**.
5. For **Input**, specify your motion graphic file name. If
   you're using a series of .png files, provide the file name of the first
   image.
6. Specify values for the other fields. For more information about these
   fields, choose the **Info** link on the console next to
   **Motion image inserter**.
