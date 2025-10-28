# Enable SMPTE 2038

You must set up the input to ingest the SMPTE 2038 ancillary
data.

###### Note

The information in this section assumes that you are familiar
with the general steps for creating an event.

###### To set up the event to look for ancillary data in SMPTE

2038

Follow these steps for both types of handling—extract and use,
and passthrough.

1.  Speak to the content provider to obtain information about the
    SMPTE 2038 ancillary data in the source:
    - Find out which of the four types of ancillary data are
      in the SMPTE 2038. If the ancillary data includes captions,
      find out which format of captions is present.

    - Find out whether the SMPTE 2038 includes custom data.
      Elemental Live can ingest custom data only if it is set up
      in a DID/SDID pair. It can't ingest data that's set up in a
      DID/DBN pair.

    Obtain the values of the DID and SDID for all the custom
    data pairs.

    Obtain a description of the data in each pair.

2.  On the Elemental Live web interface, display the details for
    the event that you want to set up.
3.  In **Input**, make sure you have set the
    **Input type** field to one of the following.
    These types are all valid for TS inputs:

        * **Network Input**
        * **File Input**
        * **HLS File Input**
        * **HLS Network Input**
        * **SMPTE 2022-7 Network Input**

    The **Prefer SMPTE 2038** field appears in
    the **Advanced** section of the
    **Input** section.

4.  In **Input** > **Advanced**,
    set **Prefer SMPTE 2038**:
    - **Checked** – You should choose this
      option if the source content contains SMPTE 2038 ancillary
      data. If the content provider has included SMPTE-2038, they
      intend for you to use it.
    - **Unchecked** – If you do not want
      Elemental Live to look at the SMPTE 2038, uncheck this
      field. Choose this option if the source content doesn't
      include SMPTE 2038 ancillary data. Elemental Live looks for
      ancillary data in the native TS. Even if a SMPTE 2038 PID
      is present, Elemental Live ignores that PID.
