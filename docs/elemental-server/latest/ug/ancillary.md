This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Ancillary (QuickTime Captions Track or Captions in MXF VANC

Data)

If your input captions are in either of the following formats, the service handles them as
"ancillary" data:

- QuickTime captions track (format QTCC)
- MXF VANC data
  AWS Elemental Server does not create output captions in these formats, but you can convert them to
  a [supported output
  format](choose-a-supported-output-captions-format.md "choose-a-supported-output-captions-format.md")..

###### Note

If your content includes 608 XDS data, see [Setting Up Input Captions With 608 XDS
Data](setting-up-for-608-xds-data.md "setting-up-for-608-xds-data.md")

**For ancillary captions**

- Create one captions selector per track to use in your outputs.
- In each captions selector, for **Source**, choose
  **Ancillary**.
- In each captions selector, for **CC channel**, choose the channel number
  for the track that is associated with the selector.

For example, the input captions have English in CC channel 1 and Spanish in CC channel 2.
To use these captions, create Captions selector 1, and then choose 1 in the **CC
channel** dropdown list. Next, create Captions selector 2, and then choose 2 in the
**CC channel** dropdown list.
