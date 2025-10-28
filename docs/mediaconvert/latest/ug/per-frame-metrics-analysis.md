# Metric analysis techniques

This section provides techniques for analyzing your per-frame metrics and applying best practices to optimize your encoding workflow.

When analyzing frame metrics, keep the following indicators in mind:

- _Consistency_ – Sudden changes in metrics might indicate scene
  transitions or encoding problems.
- _Minimum values_ – Frames with significantly lower quality scores
  might need attention.
- _Correlation with content_ – For a given bitrate, complex visual
  scenes typically have lower scores.
- _Trends over time_ – Changes in metrics over time might indicate
  issues with your encoding configuration.
  For comprehensive analysis, we recommend that you generate and compare multiple metrics
  together. You might find frames with low PSNR scores that maintain acceptable VMAF scores and
  still deliver a good viewer experience. Additionally, perform a detailed visual review in a
  controlled environment.

To get the most from your per-frame metric reports, we recommend the following
strategies:

- Combine several metrics for a more complete quality picture.
- Test metrics across different encoding parameters.
- Pair metric data with visual checks in controlled viewing conditions.
- Account for your content's unique attributes when reading the numbers.
- Set quality benchmarks for your specific workflow requirements.
- Start with small content samples to establish baseline expectations.
- Record your findings to help with future encoding decisions.
- If 95% of your content has a good score, viewers will generally have a good
  experience.
  The following is a list of tips when for interpretting results for different per-frame
  metric types:

**PSNR**

Excellent: 40dB or greater (high bitrate, visually lossless)

Good: 30-40dB (typical streaming quality)

Poor: 30dB or less (visible artifacts)

Tip: High motion and detailed content generally need higher values for a good
viewing experience.

**PSNR HVS**

Good: 35dB or greater

Acceptable: 30-35dB

Poor: 30dB or less

PSNR HVS scores are generally 2-3dB lower than regular PSNR scores.

**SSIM**

Excellent: 0.95 or greater

Great: 0.90-0.95

Good: 0.80-0.90

Poor: 0.80 or less

Tip: SSIM is more reliable for static or slow content and less reliable for high
motion content.

**MS SSIM**

Similar scale to SSIM but more accurate

Excellent: 0.98 or greater

Good: 0.90-0.98

Poor: 0.90 or less

Tip: MS SSIM is better at catching motion issues than SSIM.

**VMAF**

Excellent: 90 or greater (premium streaming)

Good: 70-90 (typical streaming)

Fair: 50-70

Poor: 50 or less

Most reliable for natural content

Less reliable for animation/gaming

Tip: VMAF scores typically drop 10-15 points when moving from 1080p to 4K at same
bitrate

**QVBR**

Excellent: 9 or greater

Good: 7 to 8

Fair: 5 to 7

Poor: 5 or less
