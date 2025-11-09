This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Encoding – Rate Control Modes

For **Rate Control Mode**, you will generally get the best video quality
per bit by using the Quality Variable Bitrate (**QVBR**) rate control mode. For
more information, see [Using QVBR Rate Control Mode](using-qvbr.md "using-qvbr.md").

## Description

Rate control modes define how the encoding engine uses the buffer model and how bits flow
into the engine.

- The **Rate Control Mode** field has the following options.
  - **Constant Bitrate** (CBR) mode: Uses the buffer model
    described above where Max Bitrate equals the defined (Average) Bitrate. In this mode, the
    system adds fill bits to the stream to ensure a constant bitrate video encoding.
  - **Variable Bitrate (VBR)** mode: Uses the buffer model
    described above where Max Bitrate is greater than or equal to the (Average) Bitrate. In
    this mode, the system adds no fill bits for VBR video encoding.
  - **Average Bitrate (ABR)** mode: Does not use the buffer
    model but allows the bitrate to vary as needed while maintaining an overall average
    bitrate for the entire video encoding.
  - **Constant Quantizer (CQ)** mode: Disables rate control
    completely. The system encodes frames using a constant **Quantization
    Parameter** (**QP**), which you can set using the
    **Start QP** setting.
  - **Statmux**: See [Encoding – Statmux Rate Control](vq-statmux.md "vq-statmux.md").

- **Start / Min / Max QP**: This field specifies the level of
  compression to start at when performing rate control and the minimum and maximum levels of
  compression.

## Recommendations

- **CBR** mode provides the lowest quality at a given
  bitrate but has the benefit of providing minimal bitrate variation. It is supported by the
  widest variety of playback devices.
- **VBR** mode provides better quality than CBR but has more
  bitrate variation (though is still limited). VBR is supported by many modern devices but is
  not as widely supported as CBR, particularly with older playback devices.
- **ABR** mode provides the best quality but should only be
  used if bitrate variation is not critical.
- **CQ Mode** is a legacy control mode which does not
  typically provide any notable benefits for video quality tuning. Use of CQ mode is not
  recommended.
- **QP Mode** has an encoder which adjusts QP values
  optimally: leave all fields blank. Use of QP is not recommended.

## Location of Fields

| Location of Field on Web Interface             | Location of Tag in XML                                                                                                                                                                    |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Streams – Video > Advanced > Rate Control Mode | stream_assembly/video_description/`codec`/rate_control_mode<br>where `codec` is one of the following:<br>• `h264_settings`<br>• `vc1_settings`<br>• `mpeg2_settings`<br>• `h265_settings` |
| Streams – Video > Advanced > Start QP          | stream_assembly/video_description/`codec`/qp<br>where `codec` is one of the following:<br>• `h264_settings`<br>• `vc1_settings`<br>• `mpeg2_settings`                                     |
| Streams – Video > Advanced > Min QP            | stream_assembly/video_description/`codec`/min_qp<br>where `codec` is one of the following:<br>• `h264_settings`<br>• `vc1_settings`<br>• `mpeg2_settings`                                 |
| Streams – Video > Advanced > Max QP            | stream_assembly/video_description/`codec`/max_qp<br>where `codec` is one of the following:<br>• `h265_settings`<br>• `vc1_settings`<br>• `mpeg2_settings`                                 |
