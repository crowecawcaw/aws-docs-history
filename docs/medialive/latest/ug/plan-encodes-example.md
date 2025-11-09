# Example of a plan for output encodes

After you have performed this procedure, you should have information that looks like this
example.

| Example   | Output group                                             | Type of encode                                                 | Encode nickname          | Characteristics of the encode |
| --------- | -------------------------------------------------------- | -------------------------------------------------------------- | ------------------------ | ----------------------------- |
| HLS       | Video                                                    | VideoA                                                         | AVC 1920x1080, 5 Mbps    |
| VideoB    | AVC 1280x720, 3 Mbps                                     |
| VideoC    | AVC 320x240, 750 Kbps                                    |
| Audio     | AudioA                                                   | AAC 2.0 in English at 192000 bps                               |
| AudioB    | AAC 2.0 in French at 192000 bps                          |
| Captions  | CaptionsA                                                | WebVTT (object-style) converted from embedded, in English      |
| CaptionsB | WebVTT (object-style) converted from embedded, in French |
| RTMP      | Video                                                    | VideoD                                                         | AVC 1920x1080, 5Mbps     |
| Audio     | AudioC                                                   | Dolby Digital 5.1 in Spanish                                   |
| Captions  | CaptionsC                                                | RTMP CaptionInfo (converted from embedded) in Spanish          |
| Archive   | Video                                                    | VideoE                                                         | AVC, 1920x1080, 8.5 Mbps |
| Audio     | AudioD                                                   | Dolby Digital 2.0 in Spanish                                   |
| AudioE    | Dolby Digital 2.0 in French                              |
| AudioF    | Dolby Digital 2.0 in English                             |
| Captions  | CaptionsD                                                | DVB-Sub (object-style) converted from Teletext, in 6 languages |
