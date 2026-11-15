

# Creating a Smart Cropping job
<a name="playground-create-job"></a>

To submit a Smart Cropping job, use the following procedure. To start an All features preview instead, see [Starting a preview](playground-preview-start.md).

1. Open the Elemental Inference console at [https://console.aws.amazon.com/elemental-inference/](https://console.aws.amazon.com/elemental-inference/).

1. In the navigation pane, choose **Playground**, and then choose **Create job**.

1. Under **Features**, choose **Smart Cropping**.

1. Under **Input settings**, for **Input S3 URI**, enter the Amazon S3 URI of an MP4 file, or choose **Browse** and use **Choose a file** to select one. **Browse** lists only buckets in the console's current AWS Region. To use a bucket in another Region, enter its URI. To process only part of the video, optionally enter **Start time** and **End time** in HH:MM:SS format.

1. Under **Output settings**, for **Destination**, enter the Amazon S3 folder URI where the output is written, or choose **Browse** and use **Choose a location**.

1. Under **Service role**, if the service role doesn't exist yet, choose **Create service role**. If it exists but doesn't cover the buckets you selected, choose **Update role permissions**.

1. Choose **Create job**. The job appears in the **Playground Jobs** table.