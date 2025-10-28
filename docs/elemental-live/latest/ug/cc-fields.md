# Completing the fields in the CC channel

number

- **CC Channel number**: This field specifies the language to
  extract. Complete as follows:
  - If you are setting up embedded passthrough only (you are creating only one
    captions selector for the input embedded captions), this field is ignored, so keep
    the default.
  - If you are setting up embedded-to-another-format, (you are creating several
    captions selectors, one for each language), enter the number of the CC instance
    (from the input) that holds the desired language. For example, if this captions
    selector is intended to hold the French captions and the French captions are in
    event 2, enter 2 in this field.

- **Force 608 to 708 Upconvert**: The embedded source captions can be
  EIA-608 captions, CEA-708 captions, or both EIA-608 and CEA-708. You can specify how
  you want these captions to be handled when Elemental Live is ingesting content. The
  following table describes the behavior for various scenarios.

| EIA-608 in Source | CEA-708 in Source | Convert Field | Result                                                                                                                                                                                                                                             |
| ----------------- | ----------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Yes               | No                | Checked       | CEA-708 data is created based on the EIA-608 data. EIA-608 data is added as 608-compatibility bits in the CEA-708 data.                                                                                                                            |
| Yes               | No                | Unchecked     | Original EIA-608 is preserved.                                                                                                                                                                                                                     |
| No                | Yes               | Checked       | Original CEA-708 is preserved.                                                                                                                                                                                                                     |
| No                | Yes               | Unchecked     | Original CEA-708 is preserved.                                                                                                                                                                                                                     |
| Yes               | Yes               | Checked       | CEA-708 data is discarded. New CEA-708 data is created based on the EIA-608 data, and EIA-608 data is added as 608-compatibility bits in the CEA-708 data. The new CEA-708 data will not include any CEA-708 formatting features. Not recommended. |
| Yes               | Yes               | Unchecked     | Original EIA-608 is preserved and original CEA-708 is preserved.                                                                                                                                                                                   | <br>• **Use SCTE-20 if Embedded Unavailable**: This field appears only if you set the **Source** to **Embedded**. If the source captions combine embedded (EIA-608 or CEA-708) and SCTE-20, you might want to set this field to **Auto**. Elemental Live will give preference to the 608/708 embedded captions but will switch to use the SCTE-20 captions when necessary. If you set this field to Off, Elemental Live will never use the SCTE-20 captions. |
