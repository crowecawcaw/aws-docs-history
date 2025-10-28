# Color space standards that MediaLive

supports

Each color space standard follows a specific standard for the color space, and specific
standards for the three sets of color data.

To read this table, find a color space in the first column, then read across to identify
the standards for the color space and the three sets of color data.

| MediaLive term for the color space | Complies with this color space standard | Complies with this brightness function (gamma) standard | Complies with this standard for display metadata                                                            |
| ---------------------------------- | --------------------------------------- | ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Rec. 601                           | Rec. 601                                | BT.1886                                                 | Not applicable. This color space doesn't include display metadata.                                          |
| Rec. 709                           | Rec. 709                                | BT.1886                                                 | Not applicable. This color space doesn't include display metadata.                                          |
| HDR10                              | Rec. 2020                               | SMPTE ST 2084 (PQ)                                      | SMPTE ST 2086                                                                                               |
| HLG or HLG 2020                    | Rec. 2020                               | HLG rec. 2020 (ARIB_STD-B67/HLG)                        | Not applicable. This color space doesn't include display metadata.                                          |
| Dolby Vision 8.1                   | Rec. 2020                               | SMPTE ST 2084 (PQ)                                      | Proprietary Dolby Vision 8.1 metadata (RPU), on a per-frame basis, and SMPTE ST 2086 on a per-stream basis. |
