

# Creating MV-HEVC spatial video outputs with AWS Elemental MediaConvert
<a name="mv-hevc-spatial-video"></a>

MV-HEVC (Multi-View HEVC) is an output codec format that encodes two video views—left eye and right eye—into a single bitstream, enabling spatial and 3D video playback.

To create an MV-HEVC output, you provide two input video files: one for the left eye (base layer) and one for the right eye (enhancement layer). MediaConvert encodes both views into a single MV-HEVC bitstream and packages the result in an MP4 or MOV container.

You configure MV-HEVC by adding `multiViewSettings` to your job inputs. The primary `fileInput` on each input serves as the left eye (base layer), and the file specified in `multiViewSettings` serves as the right eye (enhancement layer). MediaConvert then produces an H.265 output that contains both views.

**Note**  
MV-HEVC is a Pro tier add-on feature. For information about feature tiers, see [AWS Elemental MediaConvert pricing](https://aws.amazon.com/mediaconvert/pricing/).

**Topics**
+ [Supported containers for MV-HEVC](mv-hevc-supported-containers.md)
+ [Job settings to create an MV-HEVC output](setting-up-mv-hevc-job.md)
+ [MV-HEVC output requirements and limitations](mv-hevc-requirements.md)
+ [Supported encoding settings for MV-HEVC](mv-hevc-supported-encoding.md)