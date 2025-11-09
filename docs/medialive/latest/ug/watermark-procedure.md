# Setting up Nielsen watermarks in a MediaLive

channel

###### Note

The information in this section assumes that you are familiar with the
general steps for creating a channel, as described in [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md"). It also assumes that you have already
set up the audio encodes (outputs) that will contain the watermarks.

###### To create Nielsen watermarks

1. On the **Create channel** page of the
   MediaLive console, choose the output group in the left navigation bar. Then
   choose the output. In the **Stream settings**
   pane, choose the desired **Audio** tab.

In the **Codec settings** section,
expand the **Additional encoding settings**
section. Expand the **Additional settings** drop-down
menu, and find the **Audio Watermark Settings**
field. 2. Choose **Audio watermark**, then choose
**Nielsen Distribution Type**. 3. Choose the option that applies:

    * **Program content**: Typically, this option applies
     if your organization is a network broadcaster.
    * **Final distribution**: Typically, this option
     applies if your organization is a broadcast affiliate or a cable network
     provider.

4. If you want to include CBET watermarks: In the **CBET
   Settings** field, choose **Nielsen CBET**.
   More fields appear.

If you want to include NAES watermarks: In the **NAES II and
NW Settings** field, choose **NAES II and NW**.
More fields appear.

You can include both sets of watermarks in the same output
audio. 5. Complete the fields as shown in the table.

| Area                        | Field                                                                                                                                                                                                                                                                                                                    | Description                               |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------- |
| **CBET Settings**           | **CBET Source ID (CSID)**                                                                                                                                                                                                                                                                                                | The value that you obtained from Nielsen. |
| **CBET Check Digits**       | The value that you obtained from Nielsen.                                                                                                                                                                                                                                                                                |
| **CBET Stepaside**          | **ENABLED**: Nielsen watermarks that are<br>already in the source are left intact. MediaLive will insert new watermarks<br>only in portions of the audio where there are no existing watermarks.<br>**DISABLED**: Existing Nielsen watermarks are<br>removed. MediaLive will insert new watermarks throughout the audio. |
| **NAES II and NW Settings** | **Source ID (SID)**                                                                                                                                                                                                                                                                                                      | The value that you obtained from Nielsen. |
| **Check Digits**            | The value that you obtained from Nielsen.                                                                                                                                                                                                                                                                                |
| **Timezone**                | Choose a time zone to apply to the watermarks. Or leave as UTC,<br>which is the default.                                                                                                                                                                                                                                 |
