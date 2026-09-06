

# Create an SRT input
<a name="input-caller-srt-setup"></a>

After you have obtained the necessary information from the upstream system, you can create the SRT input.

**To set up an SRT input**

1. Make sure that you have the information that you [obtained from the upstream system](input-caller-srt-prereqs.md).

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/).

1. In the navigation pane, choose **Inputs**. On the **Inputs** page, choose **Create input**. Then choose **SRT caller**.

1. In the **Input class** section, choose the class for this input:
   + STANDARD\_INPUT
   + SINGLE\_INPUT

1. In the **Source A** and **Source B** sections, enter the information that you obtained.

1. Complete the **Decryption** fields, if applicable:
   + **Enabled**: Check the box. More fields appear. 
   + Select the appropriate algorithm. 
   + If the list of ARNs is populated, select the ARN of the passphrase that you [created earlier](input-caller-srt-prereqs.md). If the list is empty, type the ARN into the entry field.

1. In the **Tags **section, create tags if you want to associate tags with this input. For more information, see [Tagging resources](tagging.md).

1. Choose **Create**. MediaLive creates the input and adds it to the list of inputs. The input specifies either one or two sources. The sources don't appear in the list, but if you choose the **Name** link, the details page shows them. 