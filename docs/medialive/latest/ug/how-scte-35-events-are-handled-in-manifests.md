

# How SCTE 35 events are handled in manifests and sparse tracks
<a name="how-scte-35-events-are-handled-in-manifests"></a>

When you enable manifest decoration or sparse track in an HLS or Microsoft Smooth output group, MediaLive inserts up to three types of information. The triggers for inserting this information depend on the mode. 

## Types of information
<a name="manifest-types-of-info"></a>


| Type of instruction | When inserted | 
| --- | --- | 
| Base64 | Information about all SCTE 35 messages in the output is incorporated into the manifest; the entire SCTE 35 message is added in base64 format. | 
| Cue-out, cue-in | SCTE 35 messages that are ad avails result in the insertion of cue-out, cue-in instructions. | 
| Blackout | Only applies to the SCTE 35 Enhanced ad marker style (for HLS output; see [Enabling decoration – HLS](procedure-to-enable-decoration-hls.md)).<br />SCTE 35 messages that are *not *ad avails result in the insertion of blackout start/end instructions, assuming that blackout is enabled. If blackout is not enabled, these instructions are not inserted. | 

## Splice insert mode
<a name="splice-insert-mode"></a>

This table describes MediaLive handling when splice insert mode is enabled. The table shows how MediaLive will react when it encounters a specific message type and segmentation type in the source.

To read this table, find a message type in the first column and a segmentation type in the second column. Then read across in the other three columns. A *Yes* indicates that MediaLive will insert this type of information in the manifest when it encounters this message type and segmentation type.


<table>
<thead>
  <tr><th>Message type ID</th><th>Segmentation type</th><th>Inserts base64 information</th><th>Inserts cue-out, cue-in information</th><th>Inserts blackout information</th></tr>
</thead>
<tbody>
  <tr><td rowspan="6">splice insert</td><td>No segmentation descriptor present</td><td>Yes</td><td></td><td> </td></tr>
  <tr><td>Provider advertisement</td><td>Yes</td><td>Yes</td><td> </td></tr>
  <tr><td>Distributor advertisement</td><td>Yes</td><td>Yes</td><td> </td></tr>
  <tr><td>Placement opportunity</td><td>Yes</td><td>Yes</td><td> </td></tr>
  <tr><td>Break</td><td>Yes</td><td>Yes</td><td></td></tr>
  <tr><td>Other: Programs, Chapters, Network, Unscheduled</td><td>Yes</td><td> Yes</td><td>Yes</td></tr>
  <tr><td rowspan="6">time signal</td><td>No segmentation descriptor present</td><td colspan="3">Not applicable to time signal messages </td></tr>
  <tr><td>Provider advertisement</td><td>Yes</td><td>Yes</td><td></td></tr>
  <tr><td>Distributor advertisement</td><td>Yes</td><td>Yes</td><td> </td></tr>
  <tr><td>Placement opportunity</td><td>Yes</td><td>Yes</td><td> </td></tr>
  <tr><td>Break</td><td>Yes</td><td>Yes</td><td></td></tr>
  <tr><td>Other: Programs, Chapters, Network, Unscheduled</td><td>Yes</td><td> No</td><td>Yes</td></tr>
</tbody>
</table>


## Timesignal APOS mode
<a name="timesignal-apos-mode"></a>

This table describes MediaLive handling when timesignal APOS mode is enabled. The table shows how MediaLive will react when it encounters a specific message type and segmentation type in the source.

To read this table, find a message type in the first column and a segmentation type in the second column. Then read across in the other three columns. A *Yes* indicates that MediaLive will insert this type of information in the manifest when it encounters this message type and segmentation type.



- **splice insert**
  - **Segmentation type:** No segmentation descriptor present / **Inserts base64 information:** Yes / **Inserts cue-out, cue-in information:**   / **Inserts blackout information:**  
  - **Segmentation type:** Provider advertisement / **Inserts base64 information:** Yes / **Inserts cue-out, cue-in information:**   / **Inserts blackout information:**  
  - **Segmentation type:** Distributor advertisement / **Inserts base64 information:** Yes / **Inserts cue-out, cue-in information:**   / **Inserts blackout information:**  
  - **Segmentation type:** Placement opportunity / **Inserts base64 information:** Yes / **Inserts cue-out, cue-in information:**   / **Inserts blackout information:**  
  - **Segmentation type:** Break / **Inserts base64 information:** Yes / **Inserts cue-out, cue-in information:**  / **Inserts blackout information:** 
  - **Segmentation type:** Other: Programs, Chapters, Network, Unscheduled / **Inserts base64 information:** Yes / **Inserts cue-out, cue-in information:**   / **Inserts blackout information:**  

- **time signal**
  - **Segmentation type:** Provider advertisement / **Inserts base64 information:** Yes / **Inserts cue-out, cue-in information:**   / **Inserts blackout information:**  
  - **Segmentation type:** Distributor advertisement / **Inserts base64 information:** Yes / **Inserts cue-out, cue-in information:**   / **Inserts blackout information:**  
  - **Segmentation type:** Placement opportunity / **Inserts base64 information:** Yes / **Inserts cue-out, cue-in information:** Yes / **Inserts blackout information:**  
  - **Segmentation type:** Break / **Inserts base64 information:** Yes / **Inserts cue-out, cue-in information:** Yes / **Inserts blackout information:** 
  - **Segmentation type:** Other: Programs, Chapters, Network, Unscheduled / **Inserts base64 information:** Yes / **Inserts cue-out, cue-in information:**   / **Inserts blackout information:** Yes

