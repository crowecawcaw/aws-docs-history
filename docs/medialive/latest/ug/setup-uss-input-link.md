

# Create an Elemental Link input
<a name="setup-uss-input-link"></a>

After you have obtained information about the AWS Elemental Link hardware device, you can create an Elemental Link input.

**To create a Link input**

1. Make sure that you have the information from [step 1](setup-input-link-obtain-info.md).

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/).

1. Set the AWS Region to match the Region where the AWS Elemental Link device exists.

1. In the navigation pane, choose **Inputs**. On the **Inputs** page, choose **Create input**.

1. Complete the **Input details** section:
   + **Input** name – enter a name.
   + **Input type** – choose **Elemental Link**. 

1. In the **Input devices** section, for **Input class**, choose the class for this input:
   + STANDARD\_INPUT
   + SINGLE\_INPUT

1. In **Input devices**, choose one or two devices to attach to this input as the source. From the dropdown lists, choose the device names you previously obtained. The lists show only the devices that are set up in the current Region.
   + If the input is a standard-class input, complete both fields, to provide two source devices. 
   + If the input is a single-class input, complete the first field and leave the second field empty. 

1. In the **Tags **section, create tags if you want to associate tags with this input. For more information, see [Tagging resources](tagging.md).

1. Choose **Create**.

   The **Details** pane appears for the input, showing details about the input and the MediaLive device that it uses, including the following:
   + **ID** – A unique numerical ID for the input.
   + **ARN** – An input ARN that includes that numerical ID. 
   + **Input device** – The unique ID of the AWS Elemental Link device.
   + **Device thumbnail** – A thumbnail of the content that is currently being pushed by the device, if there is any being pushed. The device generates the thumbnails by capturing a video frame approximately every 5 seconds.