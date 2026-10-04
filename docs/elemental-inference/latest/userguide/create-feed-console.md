

# Creating using the console
<a name="create-feed-console"></a>

This section describes how to use the Elemental Inference console to create an Elemental Inference feed.

**Integration with AWS Elemental MediaLive**  
We recommend that you use Elemental Inference integrated with MediaLive. This combined workflow delivers live video processing alongside Elemental Inference. For more information, see the [AWS Elemental MediaLive User Guide](https://docs.aws.amazon.com/medialive/latest/ug/).

**Create the feed**

1. Open the [Elemental Inference console](https://console.aws.amazon.com/elemental-inference/).

1. In the navigation pane, choose **Feeds**. On the **Feeds** page, choose **Create feed**.

1. On the **Create feed** page, complete the following sections:
   + **Feed settings** – Enter a name for the feed. You might want to choose a name that helps you identify the source media that you plan to use with this feed. For example, **feed-soccer**.
   + **AI features** – Select at least one feature to enable. Each feature that you select becomes an output in the feed. The available features are **Smart Cropping**, **Event Clipping**, **Smart Subtitling**, and **Contextual Metadata**. For the configuration details of each feature, see the sections that follow this procedure.
   + **Access role** – Choose how Elemental Inference obtains the IAM role that it assumes on your behalf to access the resources a feed needs. You can use an existing role, create a new role from a template, or use a custom role ARN. An access role is required when a smart cropping output uses template groups, so that Elemental Inference can read your template images from Amazon S3.
   + (Optional) **Resource policy** – Add a resource policy to grant another AWS account or service read access to the feed's metadata. For more information, see [Managing feed policies](feed-policies.md).
   + (Optional) **Tags** – Add tags to the feed.

1. Choose **Create feed**. The **Feeds** page appears, showing a list with one line for each feed. After a few moments, the status of the feed that you created becomes **Available**, which means that the feed isn't currently associated with a source media.

**Associate the resource**

1. On the feed details page, in **Feed association**, choose **Add association**. Enter a name for the source media (resource) that you intend for this feed. You might want to choose a name that helps you identify the feed that this source media belongs to. For example, **source-soccer**.

1. Choose **Save** to confirm the association. When a resource is associated, the **Feed** information on the page updates:
   + The status of the feed changes to **Active**, which means that a resource is associated with the feed.
   + The **Integration** field shows the data endpoint for the feed.
   + The status of each output changes to **Enabled**.

   For information about feed and output status, see [Lifecycle of an AWS Elemental Inference workflow](monitor-inference-feed-lifecycle.md).

1. Make a note of the data endpoint (in the **Integration** field). You need this value to deliver the source media to Elemental Inference.