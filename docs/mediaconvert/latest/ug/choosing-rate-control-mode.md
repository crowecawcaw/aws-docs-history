# Comparison of QVBR with other rate control

modes

The rate control mode that you choose depends on the way that you will distribute your
asset. AWS Elemental MediaConvert offers the following choices for bitrate mode:

Quality-Defined Variable Bitrate (QVBR) Mode

Choose this mode for distribution over the internet (OTT) and for video
on-demand (VOD) download. For higher video quality for your file size, always
choose this mode except in the following cases:

- You need your bitrate to be constant, for example, for
  distribution over fixed-bandwidth networks
- You need your total file size to not drop below the size that you
  specify, for example, to comply with contractual or regulatory
  requirements

When you choose QVBR, the encoder determines the right number of bits to
use for each part of the video to maintain the video quality that you
specify. You can keep the QVBR quality level blank to let the encoder
determine the appropriate quality level based on the input video frames. You
can use the same QVBR settings for all your assets; the encoder
automatically adjusts the file size to suit the complexity of the video. For
more information, see [Configuring QVBR](qvbr-guidelines.md "qvbr-guidelines.md").

Constant Bitrate (CBR) Mode

Choose CBR only if you need the asset's bitrate to remain constant over
time. For example, you might need a constant bitrate if you distribute your
assets over limited, fixed bandwidth networks.

When you choose CBR, the encoder caps the file size and quality with the
value that you set for **Bitrate**. The encoder uses the
same number of bits for all parts of the video.

Variable Bitrate Mode (VBR)

Choose VBR if you distribute your asset over a network that allows for a
changing bitrate, like the internet, but you need to specify the total file
size of your asset.

###### Note

With QVBR, if you set up your output for multi-pass encoding, you can
optionally specify a maximum average bitrate that caps the total file
size of your output. Only choose VBR if your file size can't be smaller
than the size you specify.

With VBR, you specify the asset's average bitrate; the encoder allocates
bits so that more bits go to complex parts of the video. The total file size
(excluding container, packaging, and audio data) works out to the average
bitrate that you specify (in bits per second) times the length of the asset
(in seconds).

When you use VBR, you get best results if you adjust your average bitrate
to suit the complexity of each asset.

The following graph illustrates how the varying bitrate modes (QVBR and VBR) save
unnecessary bits and provide better quality compared to CBR. The graph shows QVBR versus
CBR, but the same principle applies to VBR.

In the parts of the graph where the QVBR line is above the CBR line, as in the part
labeled Area 1, the CBR capped bitrate limits video quality below that of other scenes,
so QVBR gives you more consistent quality. In the parts where the QVBR line drops below
the CBR line, as in the part labeled Area 2, a low bitrate is sufficient for the same
video quality, so QVBR saves bits and provides the opportunity for cost savings in
storage and distribution through your content delivery network (CDN).

![This chart shows a comparison of bitrate over time for constant versus variable bitrate rate control modes. The line for CBR is nearly flat, because the bitrate barely changes over time. The line for VBR jumps far above it in places where the video is encoded with enough data to show good quality for complex video. The VBR line drops far below the CBR line in places where little data is needed for good quality.](images/RateCtlModeChart.png)
