

# Converting Nielsen watermarks to ID3
<a name="feature-nielsen-id3"></a>

If one or more inputs in a channel includes Nielsen watermarks in the audio, you have the option of setting up the channel to convert those watermarks to ID3 metadata. These watermarks are part of the measurement and analytics capabilities supported by Nielsen.

This option applies only in the following scenario:
+ One or more inputs in your channel includes Nielsen watermarks in the audio.
+ Your channel has at least one output group that can include the Nielsen ID3 tag:
  + Archive output group
  + CMAF Ingest output group
  + HLS output group. The output must be a standard output (not an audio-only output)For example, an HLS output group.
+ You know that at least some of your playback devices implement the Nielsen SDK. This SDK provides functionality to handle the ID3 tags.

Converting the watermarks to ID3 tags doesn't remove the original watermarks. Outputs where you include the ID3 tags will contain both the watermark and the ID3 tags. Outputs that don't include the ID3 tags will contain only the watermark. 

**Note**  
The Nielsen SDK generates ID3 tag data approximately every 5 minutes. As a result, output segments contain ID3 tags at approximately 5-minute intervals.

You can't remove the watermarks from the audio, but if your playback devices don't implement the Nielsen SDK, the devices simply ignore the watermarks.

**Note**  
 Do not confuse this feature with the ability to [insert ID3 metadata](id3-metadata.md) in outputs.

**To set up watermarks as ID3 tags**

1. On the **Create channel** page, in the **General settings** section, in the **Nielsen Configuration** pane, choose **Enable Nielsen configuration**.

1. Set the fields as follows:
   + **Nielsen PCM to ID3 tagging**: Choose **ENABLED**.
   + **Distributor ID**: Optionally, enter the distributor ID that you obtained from Nielsen. If you enter an ID here, it is added to the ID3 metadata along with the source ID (SID) that is always in the source watermark. 

1. Go to the output group and output where you want to include the ID3 tags.

   (If the output group is **MediaPackage**, you don't have to set up the output. The ID3 tags are always passed through, if the output is a standard output.)



<table>
<thead>
  <tr><th>Output group</th><th>Section</th><th>Instruction</th><th></th><th></th></tr>
</thead>
<tbody>
  <tr><td> <b>Archive</b></td><td><b>Output settings</b></td><td>Choose <b>PID settings</b>. In <b>Nielsen ID3</b>, choose <b>PASSTHROUGH</b>.</td><td></td><td></td></tr>
  <tr><td><b>CMAF Ingest</b></td><td><b>CMAF Ingest settings</b></td><td>In <b>Nielsen ID3 Behavior</b>, choose <b>PASSTHROUGH</b>.</td><td></td><td></td></tr>
  <tr><td><b>HLS</b></td><td><b>Output settings</b></td><td>The contain must be a standard HLS container. Verify the value in the <b>HLS Settings</b> field.Choose <b>PID settings</b>. In <b>Nielsen ID3 behavior</b>, choose <b>PASSTHROUGH</b>.</td><td></td><td></td></tr>
  <tr><td><b>UDP</b></td><td><b>Output settings</b></td><td>Choose <b>Network settings</b>, then choose <b>PID settings</b>. In <b>Nielsen ID3</b>, choose <b>PASSTHROUGH</b>.</td><td></td><td></td></tr>
</tbody>
</table>
