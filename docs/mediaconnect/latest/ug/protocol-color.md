# Color support for CDI protocols

MediaConnect CDI flows support multiple configurations of color space, bit depth, and chroma
sampling for each protocol. The following table describes the configurations supported
by each CDI protocol.

###### Note

MediaLive does not currently support RGB color space for CDI inputs. If you will be
outputting a CDI flow from MediaConnect to MediaLive, ensure that you use YCbCr color
space.

| CDI color support | Protocol                                                         | Supported color configurations |
| ----------------- | ---------------------------------------------------------------- | ------------------------------ |
| CDI               | • YCbCr 10-bit 4:2:2<br>• RGB 10-bit 4:4:4<br>• RGB 12-bit 4:4:4 |
| ST 2110 JPEG XS   | • YCbCr 10-bit 4:2:2<br>• RGB 10-bit 4:4:4<br>• RGB 12-bit 4:4:4 |
