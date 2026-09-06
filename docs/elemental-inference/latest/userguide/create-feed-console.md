

# Creating using the console
<a name="create-feed-console"></a>

This section describes how to use the Elemental Inference console to create an Elemental Inference feed.

**Create the feed**

1. Open the [Elemental Inference console](https://console.aws.amazon.com/elemental-inference/).

1. In the left navigation bar, choose **Feeds**. On the **Feeds** page, choose **Create**. 

1. Complete the fields:
   + Enter a friendly name for the feed. You might want to specify a name that helps you to identify the source media that you plan to use with this feed. For example, **feed-soccer**.
   + In **AI features** section, enable the features you want to use. Each feature becomes an output in the feed. See the sections after this procedure for information about specific configuration for a feature.
   + In the **Access role** section, specify the IAM role that Elemental Inference assumes on your behalf to access the resources a feed needs. An access role is required when a smart crop output uses graphic composition, so that Elemental Inference can read your template images from Amazon S3.
   + Optionally, associate tags with the feed.

1. Choose **Create feed**. The **Feeds** page appears showing a list with one line for each feed. After a few moments, the status of the feed you just created will be **Available**.

   **Available** means that the feed isn't currently associated with a source media.

**Associate the resource**

1. In **Feed association**, choose **Add association**. Enter a friendly name for the source media (resource) that you intend for this feed. You might want to specify a name that helps you to identify the feed that this source media belongs to. For example, **source-soccer**.

1. In the **Feed association** section, choose **Save** to confirm the association. The **Feed** information on the page is updated: 
   + In **Feed association**, the **Integration** field appears, showing the data endpoint for the feed.
   + In **General details**, the status of the feed changes to **Active**, which means that a resource is associated with the feed.
   + In **Outputs**, the status of each output changes to **Enabled**.

     If you want to disable an output or change any other information for the output, select the **Edit** button (a pencil) on the right. 

   For information about feed and output status, see [Lifecycle of an AWS Elemental Inference workflow](monitor-inference-feed-lifecycle.md).

1. Make a note of the data endpoint (in the **Integration** field). You will need this value in order to deliver the source media to Elemental Inference.