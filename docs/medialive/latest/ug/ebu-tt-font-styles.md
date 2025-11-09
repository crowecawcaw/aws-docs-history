# Font styles for EBU-TT-D

This section applies if you are [setting up EBU-TT-D captions](output-sidecar-and-smptett-mss.md "output-sidecar-and-smptett-mss.md") from source captions that are embedded or Teletext
captions. You can optionally specify some of the font style information.

An EBU-TT-D caption encode consists of an XML file that the downstream system reads
and processes. This XML file includes a section for font style information. You can
specify some of this information.

1.  In the output that has the EBU-TT-D captions, display the section for the
    captions.
2.  Complete these fields. For details about a field on the MediaLive console, choose the **Info** link next to the field.

        * **Style control**
        * **Fill line gap**
        * **Font family**

    This setup results in one of the following options:

The XML file for the captions includes the following style information:

| Style information                                                | Value in XML file for Include option                                  | Value in XML file for Exclude option    |
| ---------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------- |
| Font style information (position, alignment, italics, and so on) | Set to match the source captions.                                     | Left blank.                             |
| Font color and background color                                  | Set to match the source captions.                                     | Set to white font and black background. |
| Font size                                                        | Set to 100%.                                                          | Set to 100%.                            |
| Font family                                                      | Set to the value that you specified in **Font<br>family**.            | Set to **monospaced**.                  |
| Line gap                                                         | Set up to match the value that you specified in **Fill line<br>gap**. | Set up to leave the gap unfilled.       |
