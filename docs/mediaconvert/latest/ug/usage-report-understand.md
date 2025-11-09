# Understanding your AWS billing and usage

reports for MediaConvert

AWS Elemental MediaConvert billing and usage reports use codes and abbreviations.

A `UsageType` is a string with a value such as
`PDX-P-AVC-HD-MHQ-60-NTM`, `SYD-DOLBY_VIS-HD-NTM`, or
`DUB-B-AVC-SD-SHQ-30-NTM`. For on-demand jobs, each usage type begins
with a AWS Region prefix, followed by the features used, and ending with a code
indicating _Normalized Transcoding Minutes_ (NTM).

Normalized transcoding minutes are a calculated combination of output minutes and features
used. They are MediaConvert’s standardized unit for measuring service and feature usage.
This means that as you use more features, your transcoding jobs contribute more towards
meeting monthly shared discount thresholds. For more detailed information about NTM and
monthly shared discount thresholds, see [MediaConvert Pricing](https://aws.amazon.com/mediaconvert/pricing/ "https://aws.amazon.com/mediaconvert/pricing/") and the
[MediaConvert
FAQs](https://aws.amazon.com/mediaconvert/faqs/#billing "https://aws.amazon.com/mediaconvert/faqs/#billing").

The below table maps the short billing AWS Region code to the conventional AWS Region
code and name. For example, the usage named `PDX-P-AVC-HD-MHQ-60-NTM`
indicates a job ran in us-west-2 (PDX). It also indicates professional tier billing (P),
AVC video codec encoding (AVC), multi-pass HQ quality tuning level (MHQ), between 60 and
119 frames per second (60), and normalized transcoding minutes (NTM).

For more information, see [Regions and
Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/").

| Billing region code | Region name               | Region code    |
| ------------------- | ------------------------- | -------------- |
| ARN                 | Europe (Stockholm)        | eu-north-1     |
| AUH                 | Middle East (UAE)         | me-central-1   |
| BOM                 | Asia Pacific (Mumbai)     | ap-south-1     |
| CDG                 | Europe (Paris)            | eu-west-3      |
| CMH                 | US East (Ohio)            | us-east-2      |
| CPT                 | Africa (Cape Town)        | af-south-1     |
| DUB                 | Europe (Ireland)          | eu-west-1      |
| DXB                 | Middle East (UAE)         | me-central-1   |
| FRA                 | Europe (Frankfurt)        | eu-central-1   |
| GRU                 | South America (São Paulo) | sa-east-1      |
| IAD                 | US East (N. Virginia)     | us-east-1      |
| ICN                 | Asia Pacific (Seoul)      | ap-northeast-2 |
| KIX                 | Asia Pacific (Osaka)      | ap-northeast-3 |
| LHR                 | Europe (London)           | eu-west-2      |
| MEL                 | Asia Pacific (Melbourne)  | ap-southeast-4 |
| NRT                 | Asia Pacific (Tokyo)      | ap-northeast-1 |
| PDT                 | AWS GovCloud (US-West)    | us-gov-west-1  |
| PDX                 | US West (Oregon)          | us-west-2      |
| SFO                 | US West (N. California)   | us-west-1      |
| SIN                 | Asia Pacific (Singapore)  | ap-southeast-1 |
| SYD                 | Asia Pacific (Sydney)     | ap-southeast-2 |
| YUL                 | Canada (Central)          | ca-central-1   |
| ZHY                 | China (Ningxia)           | cn-northwest-1 |

The following table lists usage types that appear in your billing and usage report and their
abbreviations.

| Usage abbreviation | Usage                                                                     |
| ------------------ | ------------------------------------------------------------------------- |
| 120                | Greater than 60 fps, but less than or equal to 120 frames per second      |
| 30                 | Less than or equal to 30 frames per second                                |
| 4K                 | Greater than 1080p, but less than or equal to 2160p resolution            |
| 60                 | Greater than 30 fps, but less than or equal to 60 frames per second       |
| 8K                 | greater than 2160p, up to and including 4320p resolution                  |
| AUD                | Audio-only                                                                |
| AV1                | AV1 video codec                                                           |
| AVC                | AVC video codec                                                           |
| AVCI               | AVC-Intra video codec                                                     |
| B                  | Basic tier                                                                |
| DOLBY              | Dolby audio                                                               |
| DOLBY_VIS          | Dolby Vision                                                              |
| DTS                | Audio Normalization                                                       |
| FRAMEFORMER        | FrameFormer frame rate conversion algorithm                               |
| GIF                | Animated GIF                                                              |
| HD                 | Greater than or equal to 720p, but less than or equal to 1080p resolution |
| HDR10PLUS          | HDR 10 plus                                                               |
| HEVC               | HEVC video codec                                                          |
| KANTAR             | Kantar watermarking                                                       |
| M                  | Multi-pass quality tuning level                                           |
| MHQ                | Multi-pass HQ quality tuning level                                        |
| MP2                | MPEG-2 video codec                                                        |
| NEXGUARD           | NexGuard watermarking                                                     |
| NIELSEN_SID_TIC    | Nielsen watermarking                                                      |
| NTM                | Normalized transcoding minute                                             |
| P                  | Professional tier                                                         |
| PASS               | Video passthrough                                                         |
| PR                 | Apple ProRes video codec                                                  |
| PROBE              | MediaConvert Probe                                                        |
| RTS                | Reserved transcode slot                                                   |
| S                  | Single-pass quality tuning level                                          |
| SD                 | Less than 720p resolution                                                 |
| SHQ                | Single-pass HQ quality tuning level                                       |
| VC3                | VC-3 video codec                                                          |
| VP8                | VP8 video codec                                                           |
| VP9                | VP9 video codec                                                           |
| XAVC               | XAVC video codec                                                          |
| Y                  | Yearly RTS commitment                                                     |
