# Setting up the event to use the

ancillary data

After you have enabled SMPTE 2038, you should specify how you want
Elemental Live to use the timecode, captions, AFD signals, and SCTE 104
messages that it detects.

###### Note

The information in this section assumes that you are familiar
with the general steps for creating an event.

- For timecode, set the **Timecode Source** (in
  **Video Selector**) using one of the
  following options:
  - If the SMPTE 2038 contains a timecode and you want to
    use it – Set the source to **Embedded**.
    Elemental Live will extract the timecode from the SMPTE
    2038, and never from the native TS.
  - Choose another value in order to use a different
    timecode source, such as system clock. These other timecode
    sources are never found in the SMPTE 2038.

- For captions, in **Input** >
  **Caption Selector**, set up the captions in
  the usual way.
  - If you don't want to use the captions from the SMPTE
    2038 – Don't create any caption selectors that specify the
    captions of that type.
  - If you want to use the captions from the SMPTE 2038 –
    Create a caption selector that specifies that type of
    captions—**Embedded**,
    **Teletext**, or
    **ARIB**. Elemental Live will extract
    those captions from the SMPTE 2038. It won't look for those
    captions in the native TS.

  Perform the setup of the captions in the output in the
  usual way. For more information about working with
  captions, see [Working with captions](captions.md "captions.md").

- For AFD signals, you can choose to use the AFD signals to
  modify the video:
  - If you don't want to use the signals – Set
    **Respond to AFD** and **Insert
    AFD signaling** to
    **None**.
  - If the SMPTE 2038 contains AFD signals and you want to
    use them – In **Output** > **Video
    Stream** > **Advanced** set
    the **Respond to AFD** field and the
    **Insert AFD signaling** field in the
    usual way. For information about the fields, click the
    question mark icon for the field.
  - If the SMPTE 2038 doesn't contain AFD signals,
    Elemental Live ignores the values in the two fields.

- For SCTE 104 messages, Elemental Live automatically converts
  the messages to SCTE 35 messages.
  - If you don't want to include the SCTE 35 messages in the
    output – There is nothing you need to do because omitting
    the messages is the default behavior.
  - If you want to work with the messages – See [SCTE-35 and SCTE-104 message
    processing in Elemental Live](scte-message-processing.md "scte-message-processing.md").
