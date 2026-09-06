

# Getting ready: Set the ad avail mode
<a name="getting-ready-set-the-ad-avail-mode"></a>

You must set the mode for SCTE 35 handling. The blanking, blackout, and manifest decoration features of MediaLive work different depending on the mode.

**To set the ad avail mode**

1. In the channel that you are creating, in the navigation pane, choose **General settings**. Choose **Avail configuration**.

1. Complete the fields as follows:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/medialive/latest/ug/getting-ready-set-the-ad-avail-mode.html)

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

