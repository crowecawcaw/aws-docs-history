# Combinations of input and output codec

The possible input and output codec combinations (in which at least one codec is a Dolby
codec) are as follows. All these combinations support including metadata in the output.

| Input codec                                 | Output codec                                                                                       |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Dolby Digital or Dolby Digital Plus         | Dolby Digital or Dolby Digital Plus                                                                |
| Dolby Digital                               | Dolby Digital Passthrough (so Dolby Digital audio is passed through; it is not<br>transcoded)      |
| Dolby Digital Plus                          | Dolby Digital Passthrough (so Dolby Digital Plus audio is passed through; it is not<br>transcoded) |
| Mix of Dolby Digital Plus and another codec | Dolby Digital Plus (with the Automatic Passthrough field checked)                                  |
| Dolby E                                     | Dolby Digital                                                                                      |
| Dolby E                                     | Dolby Digital Plus                                                                                 |
| Dolby E                                     | Dolby E (passthrough )                                                                             |
| A non-Dolby codec                           | Dolby Digital or Dolby Digital Plus                                                                |

The sample rate when encoding with a Dolby codec is always 48000.
