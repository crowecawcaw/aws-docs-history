

# Enable screen recording for your Connect Customer instance
<a name="enable-sr"></a>

This topic provides steps to enable screen recording for your Connect Customer instance, download and install the Connect Customer Client Application, and perform key configuration steps. 

**Topics**
+ [Step 1: Enable screen recording for your instance](#install-sr-step1)
+ [Step 2: Download and install the Connect Customer Client Application](#install-sr-step2)
+ [Step 3: Configure the Set recording and analytics behavior block](#configure-recording-block)
+ [Configuration tips](#tips-sr)
+ [Next steps](#next-steps-sr)

## Step 1: Enable screen recording for your instance
<a name="install-sr-step1"></a>

**Important**  
If your Connect Customer instance was created before October, 2018, and you don't have service-linked roles set up, follow the steps in [Use service-linked roles](https://docs.aws.amazon.com/connect/latest/adminguide/connect-slr.html#migrate-slr) to migrate to the Connect Customer service-linked role.

The steps in this section explain how to update your instance settings to enable screen recording, and how to encrypt recording artifacts.

1. Open the Connect Customer console at [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/).

1. Choose your instance alias.

1. In the navigation pane, choose **Data storage**, scroll down to **Screen recordings** and choose **Edit**, as shown in the following image.  
![The Screen recordings section of the Data storage page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/console-screenrecordings.png)

1. Choose **Enable screen recording**, and then choose **Create a new S3 bucket (recommended)** or **Select an existing S3 bucket**.

1. If you chose **Create a new Amazon S3 bucket (recommended)**, enter a name in the **Name** box. If you chose to use an existing bucket, select it from the **Name** list.

1. (Optional) To encrypt the recording artifacts in your Amazon S3 bucket, select **Enable encryption**, then choose a KMS key.
**Note**  
When you enable encryption, Connect Customer uses the KMS key to encrypt any intermediate recording data while the service processes it.

1. When finished, choose **Save**.

For more information about instance settings, see [Update settings for your Connect Customer instance](update-instance-settings.md). 

## Step 2: Download and install the Connect Customer Client Application
<a name="install-sr-step2"></a>

Follow the instructions in [Connect Customer Client Application](amazon-connect-client-app.md) to download and install the Connect Customer Client Application for your operating system.

## Step 3: Configure the Set recording and analytics behavior block
<a name="configure-recording-block"></a>
+ Add a [Set recording and analytics behavior](set-recording-behavior.md) block immediately after the point of entry to the flow. Add the block to every flow that you want to enable for screen recording.
+ The following image shows the properties page of the [Set recording and analytics behavior](set-recording-behavior.md) block. In the **Screen Recording** section, choose **On**.  
![The Set recording behavior block, the Screen recording section.](http://docs.aws.amazon.com/connect/latest/adminguide/images/screenrecordingblock.png)

## Configuration tips
<a name="tips-sr"></a>
+ To enable supervisors to search for contacts that have screen recordings, add a [Set contact attributes](set-contact-attributes.md) block before **Set recording and analytics behavior**. Add a custom attribute called something like **screen recording = true**. Supervisors can [search on this custom attribute](search-custom-attributes.md) to find those that have screen recordings.
+ You might want to add a [Distribute by percentage](distribute-by-percentage.md) block before **Set recording and analytics behavior**. This enables you to use screen recording for some but not all contacts.
+ You might want to use the [SuspendContactRecording](https://docs.aws.amazon.com/connect/latest/APIReference/API_SuspendContactRecording.html) and [ResumeContactRecording](https://docs.aws.amazon.com/connect/latest/APIReference/API_ResumeContactRecording.html) APIs to prevent sensitive information from being captured in the screen recording.

## Next steps
<a name="next-steps-sr"></a>

To hide sensitive content such as payment entry pages or unapproved applications from agent screen recordings based on URL patterns, add rule-based redaction to your contact flows. See [Rule-based redaction for screen recordings](rule-based-redaction-screen-recording.md).