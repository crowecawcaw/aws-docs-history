# Creating MXF outputs

MXF is an output container format that carries video content for editing, archiving, and
exchange. The MXF format is governed by a set of specifications, some of which define
_MXF profiles_, also called shims. These MXF profiles
lay out constraints on encoding settings including video codec, resolution, and
bitrate.

To make sure that your outputs comply with these specifications, you can use the
MediaConvert automatic profile selection. When you do that, MediaConvert automatically
encodes the correct profile, based on the values you choose for your codec, resolution, and
bitrate. For more information, see [Working with default MXF profiles](default-automatic-selection-of-mxf-profiles.md "default-automatic-selection-of-mxf-profiles.md").

You can also explicitly choose your MXF profile. When you do so in the MediaConvert
console, MediaConvert automatically populates the dropdown list for **Video
codec** with only valid codecs. When you aren't using automatic profile
selection, refer to the relevant specifications for constraints on your resolution and
bitrate.

###### Note

When you manually specify your MXF profile, you must set up your output in a way that
is compatible with that specification. You can submit jobs with incompatible MXF
profiles and encoding settings, but those jobs will fail.

###### Topics

- [List of codecs supported within each MXF profile](codecs-supported-with-each-mxf-profile.md "codecs-supported-with-each-mxf-profile.md")
- [Job settings to create an MXF output](setting-up-an-mxf-job.md "setting-up-an-mxf-job.md")
- [Working with default MXF profiles](default-automatic-selection-of-mxf-profiles.md "default-automatic-selection-of-mxf-profiles.md")
- [MXF output requirements](mxf-job-limitations.md "mxf-job-limitations.md")
- [XDCAM RDD9 output requirements](xdcam-rdd9.md "xdcam-rdd9.md")
- [Audio settings requirements for different MXF profiles](output-audio-requirements-for-each-mxf-profile.md "output-audio-requirements-for-each-mxf-profile.md")
