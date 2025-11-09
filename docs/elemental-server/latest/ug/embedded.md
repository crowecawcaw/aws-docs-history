This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Embedded (CEA/EIA-608, CEA/EIA-708), SCTE-20, and Embedded+SCTE-20,

and SCTE-20+Embedded

If your input captions are in any of the following formats, AWS Elemental Server handles them as
"embedded."

- CEA-608
- EIA-608
- CEA-708
- EIA-708
  If your input captions have both embedded captions and SCTE-20 captions and you want both
  types in your outputs, set up separate input captions selectors for the SCTE-20 and the embedded
  captions tracks. Set up the SCTE-20 captions selectors the same way you set up the embedded
  selectors.

###### Note

If you are extracting embedded captions from the input and using embedded captions in the
output, and if the input includes VBI data and you want to include all that data in the output,
then do not follow this procedure. Instead, see [Extracting VBI Data Included in Embedded Input
Captions](embedded-captions-in-vbi-data.md "embedded-captions-in-vbi-data.md").

## Number of Captions Selectors for Embedded

and SCTE-20 Captions

- If all of your output captions are also an embedded format, create only one captions
  selector, even if you want to include multiple tracks in the output. With this setup,
  AWS Elemental Server automatically extracts all tracks and includes them in the output.
- If all of your outputs are in a format that is not embedded, create one captions
  selector for each track that you want to include in the output.
- If some of your outputs have captions in an embedded format and some of your outputs
  have captions in a different format, create one captions selector for the outputs with
  embedded captions. Also create individual selectors for the outputs with other captions that
  aren't embedded, one for each track that you want in your outputs.

## Captions Selector Fields for Embedded,

SCTE-20, Embedded+SCTE-20, and SCTE-20+Embedded Captions

- **Source**: Specify a value for the source format as follows:
  - Choose `embedded` if the source captions are embedded (EIA-608 or CEA-708)
    or embedded+SCTE-20, or SCTE-20+embedded.
  - Choose `SCTE-20` if the source captions are SCTE-20 alone.

- **CC channel number**: This field specifies the track to extract.
  Complete as follows:
  - If you are doing embedded-to-embedded captions (that is, you create only one captions
    selector for the input-embedded captions), AWS Elemental Server ignores this field, so keep the
    default value for **CC channel number**.
  - If you are converting embedded captions to another format (that is, you create several
    captions selectors, one for each track), specify the captions channel number from the input
    that holds the track that you want. To do that, select the channel number from the dropdown
    list. For example, select **1** to choose CC1.

###### Note

AWS Elemental Server doesn't automatically detect which language is in each track (channel).
You can specify that when you set up the output captions so that AWS Elemental Server passes the
language code metadata for the captions channel into the output for downstream use.

- **Force 608 to 708 Upconvert**: The embedded source captions may be
  EIA-608 captions or CEA-708 captions or both EIA-608 and CEA-708. You can specify how you
  want these captions to be handled when the AWS Elemental encoder is ingesting content. The
  following table describes the behavior for various scenarios.

| EIA-608 in Source | CEA-708 in Source | Upconvert Field | Result                                                                                                                                                                                                                                                         |
| ----------------- | ----------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Yes               | No                | Checked         | CEA-708 data is created based on the EIA-608 data and EIA-608 data is added as<br>608-compatibility bits in the CEA-708 data.                                                                                                                                  |
| Yes               | No                | Unchecked       | Original EIA-608 is preserved.                                                                                                                                                                                                                                 |
| No                | Yes               | Checked         | Original CEA-708 is preserved.                                                                                                                                                                                                                                 |
| No                | Yes               | Unchecked       | Original CEA-708 is preserved.                                                                                                                                                                                                                                 |
| Yes               | Yes               | Checked         | **Not recommended.**<br>CEA-708 data is discarded. New CEA-708 data is created based on the EIA-608 data<br>and EIA-608 data is added as 608-compatibility bits in the CEA-708 data.<br>The new CEA-708 data does not include any CEA-708 formatting features. |
| Yes               | Yes               | Unchecked       | Original EIA-608 is preserved and original CEA-708 is preserved.                                                                                                                                                                                               |

- Use **SCTE-20 if Embedded Unavailable**: This field appears
  only if you set the Source to “Embedded.” If the source captions combine embedded (EIA-608 or
  CEA-708) and SCTE-20, you may want to check this field: the encoder gives preference to the
  608/708 embedded captions but switches to use the SCTE-20 captions when necessary. If you
  leave this field unchecked, the encoder never uses the SCTE-20 captions.
