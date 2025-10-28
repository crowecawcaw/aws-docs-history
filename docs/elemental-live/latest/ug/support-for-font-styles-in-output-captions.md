# Support for

font styles in output captions

Depending on the scenario, there are three possibilities for the
font style for output captions:

- You can specify the style you want for fonts, including color,
  outline, and background color.
- The font styles in the input are passed through.
- The font styles are controlled by the downstream player.

| Font style options                                                     | Source captions | Output captions                                                                                                                | Options for font style |
| ---------------------------------------------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------- |
| ARIB                                                                   | ARIB            | None. The font styles in the input are automatically passed through in the output.                                             |
| SCTE-27                                                                | SCTE-27         | None. The font styles in the input are automatically passed through in the output.                                             |
| DVB-Sub                                                                | DVB-Sub         | None. The font styles in the input are automatically passed through in the output.                                             |
| Teletext                                                               | Teletext        | None. The font styles in the input are automatically passed through in the output.                                             |
| Teletext                                                               | DVB-Sub         | None. The font styles in the input are automatically passed through in the output.                                             |
| Any supported captions format                                          | Burn-in         | You can specify font styles in the output. If you don’t specify styles, the Elemental Live defaults are used.                  |
| Any supported captions format                                          | DVB-Sub         | You can specify font styles in the output. If you don’t specify styles, the Elemental Live defaults are used.                  |
| An Embedded Combination (Embedded, Embedded+SCTE-20, SCTE-20+Embedded) | CCF-TT or TTML  | The font information in the source can be copied to the output, or you can let the downstream player determine the font style. |
| Teletext or SMPTE-TT or TTML or CCF-TT                                 | CCF-TT or TTML  | The font information in the source can be copied to the output, or you can let the downstream player determine the font style. |
| Any Other                                                              | Any Other       | No control: the font style is always determined by the downstream player.                                                      |
