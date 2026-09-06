

# Passing through VBI data
<a name="captions-in-vbi-data"></a>

Elemental Live supports passthrough of VBI data. You can pass through this data if the following statements are true:
+ The input includes VBI data.
+ You want to include all that data in the output. This data might include embedded captions.

**To pass through VBI data**

1. Create an output for the asset that is to include VBI data.

1. In the **Outputs** section, choose the **Settings** link for the output that contains the video asset.

1. Go to the **Stream** section. Display the **Video** fields. Click **Advanced**. More fields appear.

1. Check the **VBI Passthrough** field.

**Important**  
Do not create a **Captions** object in this output.

All the VBI data (including embedded captions) from the input will be included in the output.