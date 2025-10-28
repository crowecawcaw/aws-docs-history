# Converting color space: Procedure A

Follow this procedure to convert to one of these color spaces:

- 601
- 709
- SDR2020
- HLG
  For information about the source color spaces that you can convert to one
  of these color spaces, see [Support for conversion and
  passthrough](color-space-conversions.md "color-space-conversions.md").

For information about the results of conversion, see [The results of different types of conversions](color-space-conversion-results.md "color-space-conversion-results.md").

###### Note

This section assumes that you are familiar with creating or editing an
event.

###### To set up each output

Follow this procedure in each output.

1. On the **Event** page, in the **Output
   groups** section, choose the output group, and choose the output
   that contains the video.
2. Open the **Advanced** section. More fields
   appear.
3. Scroll down to the **Preprocessors** section and
   turn on **Color Corrector**. More fields appear.
4. Complete fields in the **Video** section as
   described in the following table

| Field                                              | Description                                                                                                 |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Video Codec**                                    | Choose any codec.                                                                                           |
| **Advanced**, then **Insert Color Metadata**       | Leave this field checked. You should never remove the color metadata if you are converting the color space. |
| **Video Range**                                    | Choose the correct option. For details, choose the icon above the field.                                    |
| **Preprocessors**, then **Color Space Conversion** | Choose the correct conversion: **Force 601** **Force 709** **Force SDR2020** **Force HLG 2020**             |
