# Encoding parameters that affect

performance

You can tune the quality, speed, and density of the video encodes in
each event.

## CABAC

For information about this parameter, see [Miscellaneous video tuning
parameters](vq-miscellaneous-tuning.md "vq-miscellaneous-tuning.md").

## Codec of the output

encode

Some codecs make more demands on the CPU than other codes. Here is a
comparison of the processing demands of codecs, from least to most
demanding:

- JPEG XS
- MPEG
- AVC
- HEVC

For more information, see [Controlling video quality](video-quality.md "video-quality.md").

## Density versus quality

(SVQ)

You can modify the density and quality balance of each individual
encode by setting the **Density vs Quality** field. You can
favor quality at the cost of density, or you can favor density at the cost
of quality.

For more information, see [Miscellaneous video tuning
parameters](vq-miscellaneous-tuning.md "vq-miscellaneous-tuning.md").

## Encode order

If you are using a version of AWS Elemental Live before version 2.24.4,
AWS Elemental Live assigns CPU resources to the encodes (streams)
in the order in which they appear in the web interface or in the XML of the
event. You should list your video encodes (streams) from highest resolution
to lowest resolution. In this way, Elemental Live will first assign CPU resources to
the most difficult encodes.

Starting
with version 2.24.4, Elemental Live automatically assigns resources to the most
difficult encodes.

## Frame rate, resolution, bitrate, and color

depth

A key factor in performance is the pixels per second being produced by
all outputs in all events.

The following characteristics of each video encode affect pixels per second:

| Characteristic               | Field in the Video section of the Output section                                        | Comment                                                                                                     |
| ---------------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Resolution                   | **Resolution**                                                                          |                                                                                                             |
| Frame rate                   | **Frame Rate**                                                                          |                                                                                                             |
| Bitrate                      | **Rate Control Mode**                                                                   | See [Setting up QVBR and rate control mode](qvbr-and-rate-control-mode.md "qvbr-and-rate-control-mode.md"). |
| Color depth: 8-bit or 10-bit | Part of the profile of the codec: **Video Stream**, then **Advanced**, then **Profile** |                                                                                                             | ## Group of pictures For more information, see [Group of pictures (GOP) configuration](vq-gop.md "vq-gop.md"). ## Lookahead For more information, see [Miscellaneous video tuning parameters](vq-miscellaneous-tuning.md "vq-miscellaneous-tuning.md"). ## Quantization For more information, see [Quantization controls](vq-quantization.md "vq-quantization.md"). ## Slices This parameter affects CPU usage. The number of slices in each video frame affects the CPU usage. You must balance the desired quality against the processing demands of that quality. We recommend that you set the slices to automatic, to let Elemental Live set the value that works best for the video resolution. For more information, see [Miscellaneous video tuning parameters](vq-miscellaneous-tuning.md "vq-miscellaneous-tuning.md"). |
