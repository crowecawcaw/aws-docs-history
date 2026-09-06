

# Disabling smart crop
<a name="smart-crop-disable-console"></a>

**To disable smart crop in all outputs**

To disable smart crop and remove all Elemental Inference features from a channel, edit the channel in MediaLive and choose **Remove feed** in the Elemental Inference settings section. You can also remove the cropping output from the feed in the Elemental Inference console. For more information, see [ Work with existing Elemental Inference feeds](https://docs.aws.amazon.com/elemental-inference/latest/userguide/elemental-inference-modify-delete) in the *AWS Elemental Inference user guide*.

**To disable smart crop in individual outputs**

1. On the **Create channel** or **Edit channel page**, in the **Output groups** section, select the output that contains the video. 

1. Display the **Stream settings** section, and choose the **Video** section. 
   + Adjust the values in the **Width** and **Height** fields.
   + Open **Scaling settings**, then set **Scaling behavior** to a value other than **SMART\_CROP**.