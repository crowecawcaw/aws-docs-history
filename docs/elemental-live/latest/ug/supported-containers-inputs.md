# Rules

for extracting captions from
sources

To
use captions in a source, Elemental Live must be able to extract the captions.
The rules are as follows:

- Elemental Live can always extract sidecar captions from the source, so
  long as Elemental Live supports the captions format.

- Elemental Live can always support captions from a streaming source, so
  long as Elemental Live supports the captions format and the input
  type.

- Elemental Live can't necessarily extract captions from a file source.
  Even if Elemental Live supports the captions format, it can extract the
  captions only from specific container types. See the table that
  follows.

| Container<br>in file input   | Elemental Live<br>can<br>extract<br>captions<br>from<br>the container? |
| ---------------------------- | ---------------------------------------------------------------------- |
| Adobe Flash                  |                                                                        |
| Audio Video Interleave (AVI) |                                                                        |
| HLS                          | Yes                                                                    |
| Matroska                     |                                                                        |
| MP4                          | Yes                                                                    |
| MPEG Transport Stream (TS)   | Yes                                                                    |
| MPEG-1 System Stream         |                                                                        |
| MXF                          | Yes                                                                    |
| No container                 | Yes                                                                    |
| QuickTime                    | Yes                                                                    |
| WAV                          | Yes                                                                    |
