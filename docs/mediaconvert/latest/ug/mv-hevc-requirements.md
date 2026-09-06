

# MV-HEVC output requirements and limitations
<a name="mv-hevc-requirements"></a>

MediaConvert restricts MV-HEVC jobs in these ways:
+ **Pro tier add-on feature.** MV-HEVC is available as a Pro tier add-on. For information about feature tiers, see [AWS Elemental MediaConvert pricing](https://aws.amazon.com/mediaconvert/pricing/).
+ **H.265 (HEVC) codec only.** All video outputs in a job with multi-view inputs must use the H.265 (HEVC) codec. Other codecs are not supported. If you specify a different codec, your job will fail with an error.
+ **MP4 or MOV containers only.** You can package MV-HEVC outputs in MP4 or MOV containers only.
+ **File group output group only.** You can put MV-HEVC outputs in a File group output group only.
+ **All inputs must have multiViewSettings, or none.** You cannot mix multi-view and non-multi-view inputs in the same job. Either all inputs must include `multiViewSettings`, or none of them can. If you specify `multiViewSettings` on some inputs but not all, your job will fail validation.
+ **Exactly one enhancement layer per input.** Each input supports exactly one enhancement layer in `multiViewSettings`. The `multiViewSettings` array must contain exactly one item.
+ **Matching input resolutions.** Both the primary input file (left eye) and the enhancement layer file (right eye) must have the same resolution.
+ **Matching frame rates.** The enhancement layer file must have the same frame rate as the primary input file.
+ **Matching frame counts.** The enhancement layer file must have the same number of frames as the primary input file.
+ **Enhancement layer must contain video.** Each enhancement layer file specified in `multiViewSettings` must contain a video stream.
+ **MP4 or MOV input files required.** Both the primary input file and the enhancement layer file must be in MP4 or MOV containers. Other input container formats are not supported for multi-view jobs.
+ **Matching input containers.** The enhancement layer file must use the same container format as the primary input file. For example, if the primary input is MP4, the enhancement layer must also be MP4.
+ **MV-HEVC outputs only.** When `multiViewSettings` is present on your inputs, all video outputs in the job must be MV-HEVC. You cannot mix MV-HEVC and non-multi-view video outputs in the same job.
+ **Smart Crop not supported.** You cannot use Smart Crop (adaptive cropping) scaling behavior with multi-view inputs. If you set Scaling behavior to Smart Cropping and also specify `multiViewSettings`, your job will fail validation.
+ **AVC Passthrough not supported.** You cannot use AVC Passthrough codec settings with multi-view inputs.

**Note**  
MediaConvert automatically forces HVC1 sample entry type for MV-HEVC outputs. You do not need to set this manually.