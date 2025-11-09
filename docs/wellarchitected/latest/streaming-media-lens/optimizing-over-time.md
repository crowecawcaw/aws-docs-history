# Optimizing over time

Content delivery is the largest cost-optimization area for
organizations streaming content to large audiences. You should
_always_ be evaluating the perceptual quality
of content and striving to lower video data rates while
maintaining, or ideally improving quality through encoder
optimization.

| SM_COST3: How do you minimize distribution costs while maintaining visual<br>quality?                                         |
| ----------------------------------------------------------------------------------------------------------------------------- |
| **SM_CBP5 – Use objective and subjective measurement<br>techniques to benchmark and improve video compression<br>efficiency** |

To optimize quality while balancing delivery costs, you should
focus on media processing and compression. The codec you use
will be dependent on your content complexity, encoder
capabilities, and client interoperability. Most codecs provide
many controls that can be tuned. Use a combination of objective
and subjective measurement to understand and improve your
compression efficiency over time. 

Though not always an accurate representation of human visual
perception, objective measurement tools, like Peak
Signal-to-Noise-Ratio (PSNR), Structural Similarity (SSIM), and
Video Multi-Method Assessment Fusion (VMAF) are readily
available tools to help analyze your compression performance.
Given a source, varied encoding job settings, and resulting
outputs, compare these metrics to tune for your unique content.
In general, though there are many options to consider while
tuning video compression settings, high motion content will
require a higher data rate than low motion to retain the same
perceptual quality. 

Subjective measurement techniques will uncover practical issues
with your video compression that might not be identified by
objective scoring. For subjective testing with human eyes and
real network conditions outside of a production environment,
consider user feedback mechanisms that enable willing users to
provide information on their viewing experience. For a simulated
environment, **Amazon Mechanical
Turk** can give you access to humans willing to watch
your content and provide feedback. For a small fee,
_Turkers_ around the world can provide you
with valuable insights on their playback experience, which can
be used to improve your workload.

Use this combination of subjective, objective, and
real-user-metrics to tune encoding settings and ABR protocol
configuration.  It is recommended that you familiarize yourself
with the codec and encoder you use for delivery so that you can
identify optimizations that could save you delivery costs. For
example, context-aware or quality-based encoding, available as a
QVBR setting for **AWS Elemental
MediaLive** and **AWS Elemental MediaConvert**, can analyze the complexity of the
content and optimize processing on your behalf.
