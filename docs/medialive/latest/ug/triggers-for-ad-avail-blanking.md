# Triggers for ad avail

blanking

For ad avail blanking, the ad avail mode that you set controls which SCTE 35
events result in the blanking of the content in the MediaLive outputs.

## Triggers in splice insert

mode

This section describes which message type and segmentation type combination is
blanked by ad avail blanking when the Ad Avail mode is Splice Insert mode.

| Message type ID                                 | Segmentation type                  | Does splice insert mode treat this message as an ad<br>avail? |
| ----------------------------------------------- | ---------------------------------- | ------------------------------------------------------------- |
| splice insert                                   | No segmentation descriptor present | No                                                            |
| Provider advertisement (0x30/0x31)              | Yes, it treats it as an ad avail   |
| Distributor advertisement (0x32/0x33)           | Yes, it treats it as an ad avail   |
| Provider placement opportunity (0x34/0x35 )     | Yes, it treats it as an ad avail   |
| Distributor placement opportunity (0x36/0x37 )  | Yes, it treats it as an ad avail   |
| Break (0x22/0x23)                               | Yes, it treats it as an ad avail   |
| Other: Programs, Chapters, Network, Unscheduled | No                                 |
| time signal                                     | No segmentation descriptor present | Not applicable to time signal messages                        |
| Provider advertisement (0x30/0x31)              | Yes, it treats it as an ad avail   |
| Distributor advertisement (0x32/0x33)           | Yes, it treats it as an ad avail   |
| Provider placement opportunity (0x34/0x35 )     | Yes, it treats it as an ad avail   |
| Distributor placement opportunity (0x36/0x37 )  | Yes, it treats it as an ad avail   |
| Break (0x22/0x23)                               | Yes, it treats it as an ad avail   |
| Other: Programs, Chapters, Network, Unscheduled | No                                 |

## Triggers in timesignal APOS

mode

This section describes which message type/segmentation type combination is
blanked by ad avail blanking when the Ad Avail mode is Timesignal with APOS
mode.

| Message type ID                                 | Segmentation type                  | Does timesignal APOS mode treat this message as an ad<br>avail? |
| ----------------------------------------------- | ---------------------------------- | --------------------------------------------------------------- |
| splice insert                                   | No segmentation descriptor present | No                                                              |
| Provider advertisement                          | No                                 |
| Distributor advertisement                       | No                                 |
| Placement opportunity                           | No                                 |
| Break                                           | No                                 |
| Other: Programs, Chapters, Network, Unscheduled | No                                 |
| time signal                                     | No segmentation descriptor present | Not applicable to time signal messages                          |
| Provider advertisement                          | No                                 |
| Distributor advertisement                       | No                                 |
| Placement opportunity                           | Yes, it treats it as an ad avail   |
| Break                                           | Yes, it treats it as an ad avail   |
| Other: Programs, Chapters, Network, Unscheduled | No                                 |
