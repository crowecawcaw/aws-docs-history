

# Triggers for ad avail blanking
<a name="triggers-for-ad-avail-blanking"></a>

For ad avail blanking, the ad avail mode that you set controls which SCTE 35 events result in the blanking of the content in the MediaLive outputs.

## Triggers in splice insert mode
<a name="triggers-splice-insert-mode"></a>

This section describes which message type and segmentation type combination is blanked by ad avail blanking when the Ad Avail mode is Splice Insert mode. 



- **splice insert**
  - **Segmentation type:** No segmentation descriptor present / **Does splice insert mode treat this message as an ad avail?:** No
  - **Segmentation type:** Provider advertisement (0x30/0x31) / **Does splice insert mode treat this message as an ad avail?:** Yes, it treats it as an ad avail
  - **Segmentation type:** Distributor advertisement (0x32/0x33) / **Does splice insert mode treat this message as an ad avail?:** Yes, it treats it as an ad avail
  - **Segmentation type:** Provider placement opportunity (0x34/0x35 ) / **Does splice insert mode treat this message as an ad avail?:** Yes, it treats it as an ad avail
  - **Segmentation type:** Distributor placement opportunity (0x36/0x37 ) / **Does splice insert mode treat this message as an ad avail?:** Yes, it treats it as an ad avail
  - **Segmentation type:** Break (0x22/0x23) / **Does splice insert mode treat this message as an ad avail?:** Yes, it treats it as an ad avail
  - **Segmentation type:** Other: Programs, Chapters, Network, Unscheduled / **Does splice insert mode treat this message as an ad avail?:** No

- **time signal**
  - **Segmentation type:** No segmentation descriptor present / **Does splice insert mode treat this message as an ad avail?:** Not applicable to time signal messages
  - **Segmentation type:** Provider advertisement (0x30/0x31) / **Does splice insert mode treat this message as an ad avail?:** Yes, it treats it as an ad avail
  - **Segmentation type:** Distributor advertisement (0x32/0x33) / **Does splice insert mode treat this message as an ad avail?:** Yes, it treats it as an ad avail
  - **Segmentation type:** Provider placement opportunity (0x34/0x35 ) / **Does splice insert mode treat this message as an ad avail?:** Yes, it treats it as an ad avail
  - **Segmentation type:** Distributor placement opportunity (0x36/0x37 ) / **Does splice insert mode treat this message as an ad avail?:** Yes, it treats it as an ad avail
  - **Segmentation type:** Break (0x22/0x23) / **Does splice insert mode treat this message as an ad avail?:** Yes, it treats it as an ad avail
  - **Segmentation type:** Other: Programs, Chapters, Network, Unscheduled / **Does splice insert mode treat this message as an ad avail?:** No



## Triggers in timesignal APOS mode
<a name="triggers-timesignal-mode"></a>

This section describes which message type/segmentation type combination is blanked by ad avail blanking when the Ad Avail mode is Timesignal with APOS mode. 



- **splice insert**
  - **Segmentation type:** No segmentation descriptor present / **Does timesignal APOS mode treat this message as an ad avail?:** No
  - **Segmentation type:** Provider advertisement / **Does timesignal APOS mode treat this message as an ad avail?:** No
  - **Segmentation type:** Distributor advertisement / **Does timesignal APOS mode treat this message as an ad avail?:** No
  - **Segmentation type:** Placement opportunity / **Does timesignal APOS mode treat this message as an ad avail?:** No
  - **Segmentation type:** Break / **Does timesignal APOS mode treat this message as an ad avail?:** No
  - **Segmentation type:** Other: Programs, Chapters, Network, Unscheduled / **Does timesignal APOS mode treat this message as an ad avail?:** No

- **time signal**
  - **Segmentation type:** No segmentation descriptor present / **Does timesignal APOS mode treat this message as an ad avail?:** Not applicable to time signal messages
  - **Segmentation type:** Provider advertisement / **Does timesignal APOS mode treat this message as an ad avail?:** No
  - **Segmentation type:** Distributor advertisement / **Does timesignal APOS mode treat this message as an ad avail?:** No
  - **Segmentation type:** Placement opportunity / **Does timesignal APOS mode treat this message as an ad avail?:** Yes, it treats it as an ad avail
  - **Segmentation type:** Break / **Does timesignal APOS mode treat this message as an ad avail?:** Yes, it treats it as an ad avail
  - **Segmentation type:** Other: Programs, Chapters, Network, Unscheduled / **Does timesignal APOS mode treat this message as an ad avail?:** No

