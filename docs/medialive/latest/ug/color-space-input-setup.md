# Set up inputs to correct metadata

In the previous step, you identified how to correct color space metadata in each MediaLive input.
This section describes how to set up each input for the required correction.

###### Note

This section assumes that you are familiar with creating or editing a channel, as
described in [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md").

###### To set up each input attached to the channel

1. On the **Create Channel** page, in the **Input
   attachments** section, for **Video selector**, choose
   **Video selector**.
2. Set the appropriate values for **Color space** and **Color
   space usage**. See the table after this procedure.
3. This step applies only if you chose **HDR10** and the attached
   input is for a MediaLive device such as AWS Elemental Link, and you plan to convert the content to
   another color space. You must specify the values for the Max CLL and Max FALL for the
   content. You should have obtained this information from the content provider.

In the **Max CLL** field and the **Max FALL**
field, enter the values.
In the following table, each row shows a valid combination of the two fields and the
result of that combination.

| \*_Color space_<br>• field                                                                                   | \*_Color space usage_<br>• field | Result                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------ | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **FOLLOW**                                                                                                   | This field is ignored.           | Passthrough. MediaLive doesn't change the color space metadata.                                                                                                                                  |
| **REC_601\*<br>• or<br>**REC_709*<br>• or<br>\*\*HDR10*<br>• or<br>**HLG\*<br>• or<br>**Dolby Vision 8.1\*\* | **Force**                        | Cleanup. MediaLive marks all the content as using the specified color space.                                                                                                                     |
| **REC_601\*<br>• or<br>**REC_709*<br>• or<br>\*\*HDR10*<br>• or<br>**HLG\*<br>• or<br>**Dolby Vision 8.1\*\* | **Fallback**                     | Cleanup. MediaLive marks the content as using the specified color space only for<br>portions of the content that are unmarked or marked as unknown or marked with an<br>unsupported color space. |
