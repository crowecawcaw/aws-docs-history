

# Create a MediaConnect Router input
<a name="setup-input-mediaconnect-router"></a>

Unlike MediaConnect Inputs, with MediaConnect Router Inputs there is no MediaConnect setup step required to create an input. Instead, you can creating the input in MediaLive makes it available in the MediaConnect router I/O interface as an available destination.

Create your input before you create the channel that ingests the input. 

**Topics**
+ [Create the MediaConnect input](#emx-router-create)

## Create the MediaConnect input
<a name="emx-router-create"></a>

**To create an input**

1. Make sure that you have the information from [step 1](setup-emx-flows.md). 

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/).

1. In the navigation pane, choose **Inputs**. On the **Inputs** page, choose **Create input**.

1. Complete the **Input details** section:
   + **Input** name – enter a name.
   + **Input type** – choose **MediaConnect Router**. 

1. Complete the **MediaConnect Router Input settings** section:
   + **Channel and input class** – choose the class for this input:
     + STANDARD\_INPUT
     + SINGLE\_INPUT 
   + **Pipeline 0 Availability Zone** – Specify the availability zone you want your channel to create pipeline 0 in. 

     If you're creating a STANDARD\_INPUT, then for **Pipeline 1 Availability Zone **, specify the availability zone you want your channel to create pipeline 1 in. 
   + **Do you want to enable custom encryption?** – Specify an AES-256 key in hexadecimal format that's 64 characters:
     + **Secret Arn** – You can select an existing secret arn you're also going to specify in MediaConnect Router. They must match for the workflow to work.

1. In the **Tags **section, create tags if you want to associate tags with this input. For more information, see [Tagging resources](tagging.md).

1. Choose **Create**.

   MediaLive creates the input and automatically displays the availability zones that input. MediaLive The router output ARN should be empty as this input is not associated. 