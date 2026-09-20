

# Getting ready: Set the ad avail mode
<a name="getting-ready-set-the-ad-avail-mode"></a>

You must set the mode for SCTE 35 handling. The blanking, blackout, and manifest decoration features of MediaLive work different depending on the mode.

**To set the ad avail mode**

1. In the channel that you are creating, in the navigation pane, choose **General settings**. Choose **Avail configuration**.

1. Complete the fields as follows:


<table>
<thead>
  <tr><th>Field</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><b>Avail settings</b></td><td>If your organization has a POIS server that handles decisions about SCTE 35 messages, then choose <b>ESAM</b> and read <a href="scte35-pois-conditioning.md">POIS signal conditioning</a> now.Otherwise, choose <b>SCTE 35 splice insert</b> or <b>SCTE 35 time signal apos</b>. The mode to choose depends on the message types that you expect to be present in the source, and on how you want to handle those messages. See the table later on this page.</td></tr>
  <tr><td><b>Ad avail offset</b></td><td>Set a value, if desired. For details about a field on the MediaLive console, choose the <b>Info</b> link next to the field.</td></tr>
  <tr><td><b>web_delivery_allowed_flag</b> </td><td rowspan="2">Typically, leave as <b>Follow</b>. For information about these fields, see <a href="ad-avail-blanking-restriction-flags.md">Ad avail blanking restriction flags</a>.</td></tr>
  <tr><td><b>no_regional_blackout_flag</b></td></tr>
  <tr><td><b>SCTE 35 segmentation scope</b></td><td>This field affects segment breaks in the video output encodes, in output groups that contain transport streams. In other words, in HLS, MediaPackage, Multiplex, and UDP output groups. This field doesn't affect output groups that don't contain transport streams.The field controls how segmentation in these TS output groups is affected by SCTE 35 messages. <br />The field is particularly important if some of these TS output groups have SCTE 35 passthrough enabled (they are <i>SCTE 35-enabled output groups</i>), and some don't have it enabled. <br />Choose the desired appropriate value: <ul><li> <b>ALL_OUTPUT_GROUPS</b>: MediaLive inserts the SCTE 35-triggered segment break in all output groups. In non-SCTE 35-enabled output groups, this behavior might result in unnecessary segment breaks or in inconsistent segment break lengths. </li><li> <b>SCTE35_ENABLED_OUTPUT_GROUPS</b>: MediaLive inserts the SCTE 35-triggered segment break only in <i>SCTE 35-enabled output groups</i>. This is the recommended value, because it reduces unnecessary segment breaks in output groups that aren't SCTE 35 enabled. </li></ul></td></tr>
</tbody>
</table>


This table identifies how the two different ad avail modes work. It identifies the combinations of message type and segmentation type that each mode considers as an *ad avail*. Note that in both modes, MediaLive looks at both splice insert messages and time signal messages.

To read this table, find a message type in the first column and a segmentation type in the second column. The third and fourth columns specify whether MediaLive treats this message combination as an ad avail when the mode is splice insert mode and when the mode is timesignal APOS mode.



- **splice insert**
  - **Segmentation type and IDs:** No segmentation descriptor present / **Does splice insert mode treat this message as an ad avail:** No / **Does timesignal APOS mode treat this message as an ad avail:** No
  - **Segmentation type and IDs:** Provider advertisement (0x30/0x31) / **Does splice insert mode treat this message as an ad avail:** Yes, it treats it as an ad avail / **Does timesignal APOS mode treat this message as an ad avail:** No
  - **Segmentation type and IDs:** Distributor advertisement (0x32/0x33) / **Does splice insert mode treat this message as an ad avail:** Yes, it treats it as an ad avail / **Does timesignal APOS mode treat this message as an ad avail:** No
  - **Segmentation type and IDs:** Provider placement opportunity (0x34/0x35 ) / **Does splice insert mode treat this message as an ad avail:** Yes, it treats it as an ad avail / **Does timesignal APOS mode treat this message as an ad avail:** No
  - **Segmentation type and IDs:** Distributor placement opportunity (0x36/0x37 ) / **Does splice insert mode treat this message as an ad avail:** Yes, it treats it as an ad avail / **Does timesignal APOS mode treat this message as an ad avail:** No
  - **Segmentation type and IDs:** Break (0x22/0x23) / **Does splice insert mode treat this message as an ad avail:** Yes, it treats it as an ad avail / **Does timesignal APOS mode treat this message as an ad avail:** No
  - **Segmentation type and IDs:** Other: Programs, Chapters, Network, Unscheduled / **Does splice insert mode treat this message as an ad avail:** Yes, it treats it as an ad avail / **Does timesignal APOS mode treat this message as an ad avail:** No

- **time signal**
  - **Segmentation type and IDs:** No segmentation descriptor present / **Does splice insert mode treat this message as an ad avail:** Not applicable to time signal messages / **Does timesignal APOS mode treat this message as an ad avail:** Not applicable to time signal messages
  - **Segmentation type and IDs:** Provider advertisement (0x30/0x31) / **Does splice insert mode treat this message as an ad avail:** Yes, it treats it as an ad avail / **Does timesignal APOS mode treat this message as an ad avail:** No
  - **Segmentation type and IDs:** Distributor advertisement (0x32/0x33) / **Does splice insert mode treat this message as an ad avail:** Yes, it treats it as an ad avail / **Does timesignal APOS mode treat this message as an ad avail:** No
  - **Segmentation type and IDs:** Provider placement opportunity (0x34/0x35 ) / **Does splice insert mode treat this message as an ad avail:** Yes, it treats it as an ad avail / **Does timesignal APOS mode treat this message as an ad avail:** Yes, it treats it as an ad avail
  - **Segmentation type and IDs:** Distributor placement opportunity (0x36/0x37 ) / **Does splice insert mode treat this message as an ad avail:** Yes, it treats it as an ad avail / **Does timesignal APOS mode treat this message as an ad avail:** Yes, it treats it as an ad avail
  - **Segmentation type and IDs:** Break (0x22/0x23) / **Does splice insert mode treat this message as an ad avail:** Yes, it treats it as an ad avail / **Does timesignal APOS mode treat this message as an ad avail:** Yes, it treats it as an ad avail
  - **Segmentation type and IDs:** Other: Programs, Chapters, Network, Unscheduled / **Does splice insert mode treat this message as an ad avail:** No / **Does timesignal APOS mode treat this message as an ad avail:** No

