# Error codes

MediaConvert returns error codes when transcoding jobs run into problems. You can use
Amazon EventBridge to track the error codes that the service returns.

MediaConvert charges your account only when a job reaches the `COMPLETED` status.
You don't pay for jobs that end in an `ERROR` status.

The following provides detailed information about error codes and messages that MediaConvert
returns, their possible causes, and solutions. To find information about an error, you
can quickly find the error code using the following links. Details for each error are
available after the table.

**Error codes**

[1010](#1010 "#1010") | [1020](#1020 "#1020") | [1021](#1021 "#1021") | [1022](#1022 "#1022") | [1030](#1030 "#1030") | [1040](#1040 "#1040") | [1041](#1041 "#1041") | [1042](#1042 "#1042") | [1043](#1043 "#1043") | [1056](#1056 "#1056") | [1060](#1060 "#1060") | [1075](#1075 "#1075") | [1076](#1076 "#1076") | [1080](#1080 "#1080") | [1091](#1091 "#1091") | [1092](#1092 "#1092") | [1093](#1093 "#1093") | [1401](#1401 "#1401") | [1404](#1404 "#1404") | [1432](#1432 "#1432") | [1433](#1433 "#1433") | [1434](#1434 "#1434") | [1515](#1515 "#1515") | [1517](#1517 "#1517") | [1522](#1522 "#1522") | [1550](#1550 "#1550") | [1601](#1601 "#1601") | [1602](#1602 "#1602") | [1603](#1603 "#1603") | [1700](#1700 "#1700") | [1999](#1999 "#1999") | [3400](#3400 "#3400") | [3401](#3401 "#3401") | [3403](#3403 "#3403") | [3404](#3404 "#3404") | [3408](#3408 "#3408") | [3450](#3450 "#3450") | [3451](#3451 "#3451") | [3452](#3452 "#3452") | [3453](#3453 "#3453") | [3454](#3454 "#3454") | [3455](#3455 "#3455") | [3456](#3456 "#3456") | [3457](#3457 "#3457") | [3458](#3458 "#3458") | [3999](#3999 "#3999")

The following is a list of error codes, troubleshooting steps, and related error
messages:

**1010 | File access error**

MediaConvert can't open one or more of your input files.

What this means: MediaConvert tried to access your input file but couldn't open it. This typically happens when the file is inaccessible, corrupted, or in an unsupported format. This could be because of IAM permission issues, an unsupported file type, or an incorrect Amazon S3 path.

To resolve this issue:

- Verify that the file path is correct.
- Verify that your IAM role has proper permissions to access the file.
- Verify that your input file is in a supported format.
- Try downloading the file to verify it's not corrupted.
- Try playing the file in a media player to verify its integrity.

For more information about supported input formats and codecs, see [Supported input formats](reference-codecs-containers-input.md "reference-codecs-containers-input.md").

Example error messages:

**`Unable to open input file
 [*s3://amzn-s3-demo-bucket/VIDEO.MP4*]: Failed
 probe/open: [No parser found for container]]`**

**`Unable to open input file
 [*https://amzn-s3-demo-bucket.s3.region-code.amazonaws.com/MANIFEST.M3U8*]:
 [Failed probe/open: [The manifest file at this URL isn't formed
 correctly: [*https://amzn-s3-demo-bucket.s3.region-code.amazonaws.com/MANIFEST.M3U8*].
 It contains more than one #EXT-X-VERSION tag. Fix the manifest and
 resubmit your job.]]`**

**`Unable to open input file
 [*https://amzn-s3-demo-bucket.s3.region-code.amazonaws.com/MANIFEST.M3U8*]:
 [Failed probe/open: [The version of the manifest file at this URL is
 more recent than we support:
 [*https://amzn-s3-demo-bucket.s3.region-code.amazonaws.com/MANIFEST.M3U8*]. We
 support versions up to [4].]]`**

**`Unable to open input file
 [*https://amzn-s3-demo-bucket.s3.region-code.amazonaws.com/MANIFEST.M3U8*]:
 [Failed probe/open: [The child manifest at this URL isn't formed
 correctly: [*https://amzn-s3-demo-bucket.s3.region-code.amazonaws.com/VARIANT.M3U8*].
 It specifies a larger segment duration in #EXTINF than in
 #EXT-X-TARGETDURATION. The problem is on this line: [#EXTINF:13,]. Fix
 the manifest and resubmit your job.]]`**

**`Failed to initialize pipeline [Caption file
 [*s3://amzn-s3-demo-bucket/CAPTIONS.VTT*] does
 not appear to be the correct type.]. (IS)`**

**`Failed to download
 *s3://amzn-s3-demo-bucket/IMAGE.PNG*`**

**1020 | Missing video error**

MediaConvert can't find any video in your input stream.

What this means: MediaConvert was able to open your file but couldn't locate any video content within it. The file might be audio-only or have a video track that's formatted incorrectly.

To resolve this issue:

- Verify that your file actually contains video content.
- Verify that the video codec is supported by MediaConvert.
- Try re-encoding the file with a standard video codec.

For more information about supported video codecs and containers, see [Supported input formats](reference-codecs-containers-input.md "reference-codecs-containers-input.md").

Example error messages:

**`Your input file
 [*s3://amzn-s3-demo-bucket/VIDEO.MP4*] doesn't
 have video that the transcoder can consume. Check your input video codec
 against this list of supported input video codec and container
 combinations: https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers-input.html#reference-codecs-containers-input-video.`**

**`Video sync did not read enough good frames to process successfully`**

**`No video found in program [1]`**

**`No video found for stream index [1] with PID
 [256].`**

**`Invalid program id specified for job. 0 is not a valid program
 id.`**

**1021 | Missing audio error**

MediaConvert can't find any audio in your input stream.

What this means: MediaConvert was able to open your file but couldn't locate any audio content within it. The file might be video-only or have an audio track that's formatted incorrectly.

To resolve this issue:

- Verify that your file actually contains audio content.
- Verify that you've selected the correct audio track in your job settings.
- Verify that the audio codec is supported by MediaConvert.

For more information about supported audio codecs and containers, see [Supported input formats](reference-codecs-containers-input.md "reference-codecs-containers-input.md").

Example error messages:

**`No audio frames decoded on [selector-(*Audio Selector
 1)*-track-1-drc]`**

**`Demuxer and decoder cancelled on [selector-(*Audio
 Selector 1*)-track-1-drc] before any frames were
 decoded`**

**1022 | Timecode error**

MediaConvert could not find or read timecode in your input.

What this means: MediaConvert was looking for a specific type of timecode in your input file but couldn't find it. This happens when you've configured your job to use a timecode source that doesn't exist in your file.

To resolve this issue:

- Modify your Embedded timecode override setting to None.
- Use a different timecode source that exists in your input.
- Modify your timecode source to "Start at 0" if your file doesn't have embedded timecodes.

For more information about timecode configuration options, see [Setting up timecodes](setting-up-timecode.md "setting-up-timecode.md").

Example error messages:

**`You set Embedded timecode override (embeddedTimecodeOverride)
 to Use MDPM (USE_MDPM), but no MDPM timecode was found in your input.
 Leave Embedded timecode override blank, or set to None (NONE), and
 resubmit your job.`**

**1030 | Unsupported codec error**

MediaConvert doesn't support the codec or container of the input file.

What this means: Your input file uses a video or audio codec that MediaConvert cannot process. Not all media formats are supported, even if they play in standard media players.

To resolve this issue:

- Review the list of supported input codecs and containers.
- If possible, obtain your content in a different format.

For more information about supported input formats and codecs, see [Supported input formats](reference-codecs-containers-input.md "reference-codecs-containers-input.md").

Example error messages:

**`Audio codec [*adpcm\_ms*] for track [1] is
 not a supported input audio codec`**

**`Unsupported video input: [*High 4:4:4 Predictive
 profile* is unsupported]`**

**`Video codec [*unknown*] is not a supported
 input video codec`**

**`Video codec [*svq1*] is not a supported
 input video codec`**

**1040 | Job settings compatibility error**

One or more of the job's encoding settings aren't supported in the
combination specified. Or, the encoding settings aren't compatible with the
input.

What this means: Your job settings contain incompatible options or require information that's missing from your input file. For example, you might be trying to use settings that only work with certain input types.

To resolve this issue:

- Review the specific error message for details about which settings are problematic.
- Specify required settings like resolution or framerate instead of using "Follow source".
- Verify that your output settings are compatible with your chosen codec.
- Verify that your input and output paths are different.

For more information about configuring job settings correctly, see [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md").

Example error messages:

**`You did not specify resolution for Video description
 [*1*] and there is no input resolution to follow.
 To resolve: Specify a width and height, and resumbit your
 job.`**

**`You did not specify framerate for Video description
 [*1*] and there is no input framerate to follow.
 To resolve: Specify framerate, and resumbit your job.`**

**`Invalid audio track specified for audio_selector
 [*1*]. Audio track [*1*] not
 found in input container.`**

**`video_description [*1*] is not a valid
 AVC-Intra operating point. Invalid frame rate
 [*30/1*]. Supported frame rates for AVC Intra class
 100, 1920x1080, PROGRESSIVE are [*25/1, 60000/1001, 30000/1001,
 24000/1001, 50/1*]`**

**`Invalid resolution [*640 x 1159*], only even
 values are supported. video_description
 [*1*].`**

**`video_description [*1*] is not a valid
 AVC-Intra operating point. Invalid frame rate
 [*30/1*]. Supported frame rates for AVC Intra class
 100, 1920x1080, PROGRESSIVE are [*25/1, 60000/1001, 30000/1001,
 24000/1001, 50/1*]`**

**`Frame rate is set to follow, but there is no frame rate
 information in the input stream info`**

**`Duplicate input and output path
 [*s3://amzn-s3-demo-bucket/VIDEO.MP4*] found in
 job.`**

**`Error initializing encoder for video target
 [*1*] [initialization failed: Invalid level
 specified for the selected framerate or resolution.]`**

**1041 | Acceleration compatibility error**

Your job settings aren't compatible with accelerated transcoding.

What this means: You've enabled accelerated transcoding, but some of your job settings aren't supported with this feature. Accelerated transcoding has specific requirements and limitations.

To resolve this issue:

- Review the specific error message for details about incompatible settings.
- Modify your job settings as suggested in the error message.
- Review the complete list of accelerated transcoding requirements.
- Consider disabling accelerated transcoding if you need the incompatible features.

For more information about accelerated transcoding requirements and limitations, see [Accelerated transcoding job settings requirements](job-requirements.md "job-requirements.md").

Example error messages:

**`Your job settings aren't compatible with accelerated
 transcoding. Adjust your job settings as follows: [Disable interpolated
 frame rate conversion in the following output: [*1*].
 Disable inverse telecine by choosing Deinterlace as the deinterlacer
 mode in the following output:
 [*2*].]`**

**1042 | Acceleration requirement error**

This job doesn't require enough processing power to benefit from
accelerated transcoding.

What this means: Your job is too small or simple to see meaningful benefits from accelerated transcoding. The overhead of setting up acceleration might actually make the job take longer.

To resolve this issue:

- Disable accelerated transcoding for this job.
- Consider using accelerated transcoding for more complex jobs that
  would take 10 or more minutes to run.
- Consider batching smaller jobs together if appropriate.

Example error messages:

**`This job doesn't require enough processing power to benefit
 from accelerated transcoding. Disable accelerated transcoding, and
 resubmit your job.`**

**1043 | Acceleration input error**

MediaConvert can't use accelerated transcoding with your input files.

What this means: Your input files aren't compatible with accelerated transcoding. This feature only works with certain input formats.

To resolve this issue:

- Disable accelerated transcoding for this job.
- Review the compatible input requirements.

Example error messages:

**`Your input files aren't compatible with accelerated
 transcoding. Disable accelerated transcoding and resubmit your
 job.`**

**1056 | File open error**

The service can't open an input or output file.

What this means: MediaConvert attempted to access your file but encountered an error. This could be because of permission issues, file corruption, or unsupported file formats.

To resolve this issue:

- Verify your IAM permissions for both input and output locations.
- Verify that your file isn't corrupted by downloading it.
- Verify that you're using a [supported file format](reference-codecs-containers-input.md "reference-codecs-containers-input.md").
- Use the Browse button in the console to verify the correct S3 path.

Example error messages:

**`Demuxer: [The transcoder can't read this media segment:
 [*https://amzn-s3-demo-bucket.s3.region-code.amazonaws.com/SEGMENT\_00001.TS*]. The
 segment is listed in this HLS child manifest:
 [*https://amzn-s3-demo-bucket.s3.region-code.amazonaws.com/MANIFEST.M3U8*]. Check
 the segment to make sure that it's formed correctly and not
 corrupt.]`**

**`MGILoaderMOV
 [*s3://amzn-s3-demo-bucket/VIDEO.MOV*] file
 contains unsupported pixel format.`**

**`MGILoaderMOV unable to open
 [*s3://amzn-s3-demo-bucket/VIDEO.MOV*] file :
 [-1094995529]`**

**1060 | Timecode clipping error**

The start and end timecodes specified for an input clip don't exist in the
associated input stream.

What this means: You've set up input clipping with timecodes that don't match what's available in your input file. This often happens when your file's embedded timecodes don't start at 00:00:00:00.

To resolve this issue:

- Set both the input Timecode source and the Timecode configuration Source under Job settings to Start at 0.
- Modify your clip start and end times to match the actual timecodes in your file.
- Use the embedded timecodes in your file as a reference when setting clip points.
- Use a media analysis tool to check the actual duration and
  timecode range of your input.

For more information about how MediaConvert handles timecodes and input timelines, see [Input
timelines](specifying-inputs.md#input-timelines "specifying-inputs.md#input-timelines").

Example error messages:

**`The clipping start timecode [*00:12:55;00*] was not found in input number [*1*]`**

**`Decoder closed. No pictures decoded.`**

**`Demuxer unable to seek to clipping start timecode [*00:16:37:00*]`**

**`The clipping region [*00:00:00:00*] to [*00:00:07:12*] was not found in input number [*1*]`**

**1075 | Demux structure error**

MediaConvert couldn't recover from a problematic file when demuxing.

What this means: Your input file has structural issues that prevent MediaConvert from properly reading it. The file might be corrupted, incomplete, or created with non-standard settings.

To resolve this issue:

- Verify that you've provided a supported input format.
- Verify that your file was completely uploaded to Amazon S3.
- Try re-encoding or remuxing your source file before submitting the
  job.
- If the issue persists, contact Support.

For more information about supported input formats and requirements, see [Supported input formats](reference-codecs-containers-input.md "reference-codecs-containers-input.md").

Example error messages:

**`Unable to open input file [*s3://amzn-s3-demo-bucket/file.mp4*]: [Failed probe/open:
 [no moov box found in file]]`**

**`Error initializing demux info for file [*s3://amzn-s3-demo-bucket/audio.mp4*] (Incompatible audio
 stream)`**

**`Demuxer: [elst box outside of track]`**

**`Error initializing demux info for file
 [s3://amzn-s3-demo-bucket/captions.vtt] (Incompatible container
 headers)`**

**`Demuxer: [invalid AVC header]`**

**1076 | File truncation error**

MediaConvert couldn't read from one of the input files. The file
might have an unexpected end of file.

What this means: MediaConvert started reading your input file but encountered an abrupt end, suggesting the file is truncated or incomplete.

To resolve this issue:

- Verify that your file was completely uploaded to Amazon S3.
- Verify if the file plays correctly in a media player.
- Try re-encoding or re-exporting the file from its source.
- Verify that your input file is valid and that it's truncated
  properly.

For more information about troubleshooting file upload issues, see [Troubleshooting Amazon S3 upload issues](../../../AmazonS3/latest/userguide/troubleshooting-upload-issues.md "../../../AmazonS3/latest/userguide/troubleshooting-upload-issues.md").

Example error messages:

**`Demuxer: [ReadPacketData File read failed - end of file hit at
 length [*93524619*]. Is file
 truncated?]`**

**`Audio input pipeline error: [Demuxer: [ReadPacketData File read
 failed - end of file hit at length [*123251788*]. Is file truncated?]]`**

**1080 | MXF configuration error**

There is a problem in the way that the MXF output settings are
configured in your job.

What this means: Your MXF output settings contain invalid or incompatible options. MXF is a professional format with strict requirements for valid files.

To resolve this issue:

- Review your MXF output settings for invalid combinations.
- Verify that your video and audio settings comply with MXF specifications.
- Consider using an MXF profile preset as a starting point.

For more information about MXF output requirements and specifications, see [Creating MXF outputs](mxf.md "mxf.md").

Example error messages:

**`MXF_muxer [1]: BadFilePath (status 0x7)`**

**1091 | Output encryption error**

There was an error encrypting one or more of the job outputs.

What this means: MediaConvert couldn't apply the DRM or encryption you specified. This typically happens because of permission issues or problems with your encryption configuration.

To resolve this issue:

- Verify that the IAM role you chose has permission to invoke SPEKE.
- Verify that your SPEKE API endpoint is correctly configured and accessible.
- Review the specific error message for details about the encryption failure.
- See guidance on proper role configuration.

For more information about setting up DRM encryption, see [Content encryption and DRM in AWS Elemental MediaConvert](implementing-digital-rights-management-drm.md "implementing-digital-rights-management-drm.md").

Example error messages:

**`SPEKE keyserver request failed:*-Unable to
 parse response xml Response code [200]HTTP/1.1 200 OK
 Date:*...`**

**`SPEKE keyserver request failed:*-Response
 code [403]HTTP/1.1 403 Forbidden Date:*...`**

**`SPEKE keyserver request failed:*-Response
 code [500]HTTP/1.1 500 Internal Server Error
 Date*...`**

**`SPEKE keyserver request failed:*-OpenSSL
 SSL\_connect: Connection reset by peer in connection to
 abcdefg123.execute-api.us-west-2.amazonaws.com:443*`**

**`[GenerateKey] Failed to find key [*0*] for [*https://abcdefg123.execute-api.ap-south-1.amazonaws.com/UAT/encryptionKeys*]`**

**1092 | Audio decode error**

MediaConvert can't decode one or more of your input audio streams.

What this means: While your audio format is technically supported, there's
something unusual or corrupted in your specific audio stream that prevents
MediaConvert from processing it.

To resolve this issue:

- Verify if the audio plays correctly in a media player.
- Try extracting and re-encoding just the audio portion of your file.
- Verify that your audio stream uses standard settings for its
  codec.
- MediaConvert supports the codec and container, but there is a problem
  with the audio source that prevents the transcoder from reading
  it.

Example error messages:

**`Decoder: [Dolby decoder error: The transcoder couldn't decode the
 audio frame header in the first 100 frames of your input. Your audio
 source is either corrupt or in a format that the transcoder doesn't
 support. For a list of supported audio inputs, see the documentation.
 For MediaConvert, see
 https://docs.aws.amazon.com/mediaconvert/latest/ug/reference-codecs-containers-input.html.]`**

**1093 | Audio description error**

MediaConvert encountered an error with audio description settings.

What this means: You've configured audio description (AD) settings incorrectly. When using AD features, you need to specify both the AD audio channel and a valid AD data channel.

To resolve this issue:

- Specify the correct channel in your input that contains your AD data stream.
- If your input doesn't have AD data, remove both AD audio channel and AD data channel settings.
- Review the documentation for proper configuration.

For more information about configuring audio descriptions correctly, see [Audio descriptions](audio-descriptions.md "audio-descriptions.md").

Example error messages:

**`You specified an audio description (AD) data channel that does not
 contain an AD data stream. This is required when you specify an AD audio
 channel. To resolve: Specify the channel in your input that contains
 your AD data stream, or remove both AD audio channel and AD data channel
 from your output remix settings. Then resubmit your job.`**

**1401 | S3 access denied error**

Amazon S3 denied access to a file or bucket.

What this means: MediaConvert doesn't have permission to read from your input location or write to your output location. This is typically because of incorrect IAM permissions or bucket policies.

To resolve this issue:

- Verify the bucket policies on your input and output Amazon S3 buckets.
- Verify that the IAM role you specified in your job has the necessary permissions.
- Make sure the IAM user creating the job has appropriate permissions.
- See [Set Up IAM Permissions](iam-role.md "iam-role.md") for guidance.

For more information about Amazon S3 access permissions and bucket policies, see [Using bucket policies and user policies](../../../AmazonS3/latest/userguide/using-iam-policies.md "../../../AmazonS3/latest/userguide/using-iam-policies.md") in the _Amazon S3 User Guide_.

Example error messages:

**`Unable to open input file [*s3://amzn-s3-demo-bucket/file.webm*]: [Failed
 probe/open: [Can't read input stream: [Failed to read data: Access
 denied to [*s3://amzn-s3-demo-bucket/file.webm]*]]]`**

**`Demuxer: [Failed to read data: Error caching file]`**

**`Unable to write to output file [*s3://amzn-s3-demo-bucket/file\_00001.ts*]: [Failed to
 write data: Access Denied]`**

**`Audio input pipeline error: [Demuxer: [Failed to read data: Error
 caching file]]`**

**`The role you provided is not authorized to perform kms:Decrypt on your destination S3 bucket. Check that your role has the correct permissions and that that you've specified the correct S3 bucket.`**

**1404 | File not found error**

MediaConvert could not find a file or Amazon S3 bucket.

What this means: The Amazon S3 file or bucket you specified in your job doesn't exist or MediaConvert can't access it. This could be because of a typo in the path, a missing file, or permission issues.

To resolve this issue:

- Verify that the Amazon S3 bucket and file paths are correct.
- Verify that the files actually exist in the specified location.
- Verify that your IAM role has permission to access the bucket.
- Try using the console's Browse button to select your files.

For more information about Amazon S3 buckets and access control, see [Working with Amazon S3 buckets](../../../AmazonS3/latest/userguide/UsingBucket.md "../../../AmazonS3/latest/userguide/UsingBucket.md") and [Using bucket policies and user policies](../../../AmazonS3/latest/userguide/using-iam-policies.md "../../../AmazonS3/latest/userguide/using-iam-policies.md") in the Amazon S3 documentation.

Example error messages:

**`Unable to open input file [*s3://amzn-s3-demo-bucket/file.mp4*]: [Failed probe/open:
 [Can't read input stream: [Failed to read data: HeadObject
 failed]]]`**

**1432 | IAM role permission error**

The role specified in your MediaConvert job settings doesn't have
the necessary permissions or has another problem.

What this means: The IAM role you provided exists but doesn't have the permissions MediaConvert needs to access your resources.

To resolve this issue:

- Verify that your IAM role has the correct policy attachments.
- Verify that the role has permission to access your Amazon S3 buckets.
- Make sure the role has MediaConvert listed as a trusted entity.
- See [Set Up IAM Permissions](iam-role.md "iam-role.md") for guidance.

For more information about setting up IAM roles with proper permissions
for MediaConvert, see [Set Up IAM
Permissions](iam-role.md "iam-role.md").

Example error messages:

**`Unable to open input file [*s3://amzn-s3-demo-bucket/file.mp4*]: [Failed probe/open:
 [Can't read input stream: [Failed to read data: Invalid role provided in
 RESOURCE_ROLE_ARN]]]`**

**1433 | IAM role missing error**

The role specified in your MediaConvert job settings doesn't
exist.

What this means: You've provided an IAM role ARN that MediaConvert can't find. The role might have been deleted or you might have a typo in the ARN.

To resolve this issue:

- Verify that the IAM role exists in your AWS account.
- Verify that there aren't any typos in the role ARN.
- Create a new role if necessary using the guidance in [Set Up IAM Permissions](iam-role.md "iam-role.md").
- Verify that the job has the right IAM role specified.

For more information about creating and configuring IAM roles for MediaConvert,
see [Set Up IAM Permissions](iam-role.md "iam-role.md").

Example error messages:

**`Unable to assume role. Check that the role exists and that MediaConvert is a trusted entity.`**

**1434 | IAM trust policy error**

The role specified in your MediaConvert job settings doesn't have
the necessary permissions.

What this means: MediaConvert can't assume the IAM role you provided. This typically happens when the role's trust policy doesn't include MediaConvert as a trusted service.

To resolve this issue:

- Verify that your IAM role has a trust relationship with MediaConvert.
- Verify that the trust policy is correctly formatted.
- See [Set Up IAM Permissions](iam-role.md "iam-role.md") for
  guidance on configuring the trust relationship.
- Verify that the job has the right IAM role specified and that the
  role has MediaConvert as a trusted entity.

For more information about setting up trust relationships for IAM roles,
see [Set Up IAM Permissions](iam-role.md "iam-role.md").

Example error messages:

**`Unable to open input file *s3://amzn-s3-demo-bucket/file.mp4*]: [Failed probe/open:
 [Can't read input stream: [Failed to read data: AssumeRole
 failed]]]`**

**1515 | IAM role format error**

The role specified in your MediaConvert job settings doesn't have
the necessary permissions or is malformed.

What this means: There's a problem with the IAM role ARN you provided. It might be incorrectly formatted or missing required permissions.

To resolve this issue:

- Verify that the role ARN is correctly formatted.
- Verify that the role has the necessary permissions.
- Make sure the role has MediaConvert listed as a trusted entity.
- See [Set Up IAM Permissions](iam-role.md "iam-role.md") for
  guidance.
- Verify that the job has the right IAM role specified and that the
  role has the correct permissions.

For more information about IAM role ARN format and permissions, see
[Set Up IAM Permissions](iam-role.md "iam-role.md").

Example error messages:

**`Invalid role ARN format. Please check the role ARN and try again.`**

**1517 | S3 Write Error**

MediaConvert encountered an error when writing to Amazon S3.

What this means: A call to Amazon S3 failed during the writing/uploading
process of output files.

To resolve this issue:

- Verify that the IAM role you specified has s3:PutObject permissions for the destination bucket.
- Verify bucket policies that might be restricting write operations to the destination bucket.
- Ensure the destination bucket exists and is in the correct AWS Region.
- Verify network connectivity to Amazon S3 endpoints.

For more information about Amazon S3 permissions and access control, see [Access control in Amazon S3](../../../AmazonS3/latest/userguide/access-control-overview.md "../../../AmazonS3/latest/userguide/access-control-overview.md").

**1522 | Processing timeout error**

There is an unexpected timeout with this job.

What this means: Your job took longer than the maximum allowed processing time and was terminated. This is an internal system limitation rather than an issue with your content or settings.

To resolve this issue:

- Contact Support for assistance.
- Consider breaking very large jobs into smaller segments.

Example error messages:

**`An internal error has occurred and your job timed out. Contact Support.`**

**1550 | Acceleration system error**

There is an unexpected internal error with accelerated transcoding.

To resolve this issue:

- Try running the job again without accelerated transcoding.
- If the issue persists, contact Support.

For more information about accelerated transcoding, see [Accelerated transcoding](accelerated-transcoding.md "accelerated-transcoding.md").

Example error messages:

**`Acceleration fault`**

**1601 | Nielsen Watermark Error**

MediaConvert encountered an error with Nielsen Watermarking.

What this means: There was an error during the Nielsen audio watermarking process. Nielsen watermarking embeds inaudible identification codes into audio content for audience measurement purposes.

To resolve this issue:

- Verify that your Nielsen watermarking settings are correctly configured.
- Verify that you have valid Nielsen credentials and parameters.
- Ensure the audio input is compatible with Nielsen watermarking requirements.
- Contact Nielsen support if the problem persists.

For more information about Nielsen watermarking in MediaConvert, see [Working with Nielsen watermarking](nielsen-watermarking.md "nielsen-watermarking.md").

**1602 | NexGuard Watermark Error**

MediaConvert encountered an error with NexGuard Watermarking.

What this means: There was an error during the NexGuard watermarking process. NexGuard watermarking embeds forensic tracking information into video content for content protection and piracy tracking.

To resolve this issue:

- Verify that your NexGuard watermarking settings are correctly configured.
- Verify that your video input meets NexGuard's requirements.
- Ensure you have a valid NexGuard license.
- Contact NexGuard support if the problem persists.

**1603 | Kantar Watermark Error**

MediaConvert encountered an error with Kantar Watermarking.

What this means: There was an error during the Kantar audio watermarking process. Kantar watermarking embeds inaudible identification codes into audio content for audience measurement purposes.

To resolve this issue:

- Verify that your Kantar watermarking settings are correctly configured.
- Verify that your audio input meets Kantar's requirements for sample rate, bit depth, and channel count.
- Ensure you have a valid Kantar license.
- Contact Kantar support if the problem persists.

For more information about Kantar watermarking in MediaConvert, see [Using Kantar for audio watermarking](kantar-watermarking.md "kantar-watermarking.md").

**1700 | Dolby Preprocessor Error**

MediaConvert encountered an error with the Dolby Vision preprocessor.

What this means: There was an error during the Dolby Vision preprocessing stage. Dolby Vision processing requires specific metadata and configuration to properly handle HDR content.

To resolve this issue:

- Verify that your input file contains valid Dolby Vision metadata.
- Verify that your Dolby Vision settings are correctly configured.
- Ensure your input file meets the requirements for Dolby Vision processing.
- If the problem persists, contact Support.

For more information about Dolby Vision processing in MediaConvert, see [Creating Dolby Vision outputs with AWS Elemental MediaConvert](dolby-vision.md "dolby-vision.md").

Example error messages:

**`Your input [%i] contains invalid Dolby Vision metadata on frame
 X. To resolve: Check your input for valid Dolby Vision metadata. Then
 resubmit your job.`**

**1999 | Unexpected system error**

There is an unexpected error.

What this means: MediaConvert encountered an internal error. This is a general
error code for unexpected issues.

To resolve this issue:

- Review the specific error message for any actionable information.
- For audio/video sync issues, try setting Audio duration to Match video duration.
- If the error persists, contact Support.

Example error messages:

**`Your input has a low framerate and audio that continues past the
 end of the video. MediaConvert could not synchronize audio and
 video, and could not create an output. To resolve: Set Audio
 duration to Match video duration in the output audio container
 settings, or manually trim your input so that audio and video
 durations exactly match. Then resubmit your job.`**

**`Post Transcode work failed. See previous log messages for the
 reason for failure.`**

**`Unknown error`**

**`Job failed with unexpected error: std::bad_alloc`**

**`Video sync did not find a valid series of timestamps in the
 input`**

**`Could not commit single file`**

**`Video pipeline failed to start`**

**`*empty error
 message*`**

**`Encoder runtime error on gpu [0] pipeline [Error processing GOP
 data in reorder FIFO].`**

**3400 | HLS manifest error**

Your HLS input doesn't conform to the requirements for MediaConvert
supported HLS inputs.

What this means: There's a problem with your HLS manifest file or its referenced segments. Common issues include malformed manifests, unsupported features, or URL length limitations.

To resolve this issue:

- Review the specific error message for details about the HLS issue.
- Verify that your manifest file follows the HLS specification.
- Ensure your manifest file size is under 16 MB.
- Review HLS input requirements.

For more information about HTTP input requirements and HLS manifest
specifications, see [HLS input requirements](using-hls-inputs.md "using-hls-inputs.md").

Example error messages:

**`3400: MediaConvert can't open the following HLS input*https://amzn-s3-demo-bucket.s3.region-code.amazonaws.com/...excessively\_long\_example\_URL\_truncated\_for\_docs.../index.m3u8*.
 The input URL exceeded a character count limit of 900 characters.
 Reduce the character count to 900 characters or less, and resubmit
 your job. To find the input URL character count, combine the input
 you entered with the individually referenced files within the HLS
 manifest. For example, if your input is
 https://www.example.com/manifest.m3u8?key1=value1&key2=value2,
 and lists a segment with the path file/path/segment_ts_720_0001.ts,
 the input URL will be
 https://www.example.com/file/path/segment_ts_720_0001.ts?key1=value1&key2=value2
 which is 80 characters long.`**

**`3400: MediaConvert can't open the following HLS input: *https://amzn-s3-demo-bucket.s3.region-code.amazonaws.com/HLS/manifest.m3u8*. This
 manifest is malformed: *https://amzn-s3-demo-bucket.s3.region-code.amazonaws.com/HLS/sub-manifest.m3u8*. Fix
 the manifest and then resubmit your job.`**

**`3400: MediaConvert can't open the following HLS input: *https://amzn-s3-demo-bucket.s3.region-code.amazonaws.com/HLS/manifest.m3u8*. The file
 size of this manifest is larger than MediaConvert supports:
 *https://amzn-s3-demo-bucket.s3.region-code.amazonaws.com/HLS/sub-manifest.m3u8*.
 MediaConvert supports manifest file sizes up to 16 MB.`**

**`3400: MediaConvert can't open the following input: *https://amzn-s3-demo-bucket.s3.region-code.amazonaws.com/HLS/manifest.m3u8*.
 Reason:...`**

**3401 | HTTP authentication error**

You specified an HTTP(S) URL for an input file that requires
authentication.

What this means: Your HTTP input is password-protected or requires authentication, but MediaConvert doesn't support passing credentials to HTTP servers.

To resolve this issue:

- Remove authentication requirements from your HTTP server for this file.
- Download the file and upload it to Amazon S3 instead.

For more information about HTTP input requirements and limitations, see [HTTP input requirements](http-input-requirements.md "http-input-requirements.md").

Example error messages:

**`3401: Access to '*https://amzn-s3-demo-bucket.s3.region-code.amazonaws.com/index.m3u8REMOVED=true*' requires
 authorization.`**

**3403 | HTTP forbidden error**

You specified an HTTP URL for an input file, but the HTTP server
refuses the request.

What this means: The HTTP server hosting your input file is actively refusing the connection. This could be because of access restrictions or server configuration issues.

To resolve this issue:

- Verify that the URL is correct.
- Contact the team managing the HTTP server about access permissions.
- Consider downloading the file and uploading it to Amazon S3 instead.

For more information about HTTP input requirements and limitations, see [HTTP input requirements](http-input-requirements.md "http-input-requirements.md").

Example error messages:

**`3403: Access to '*https://amzn-s3-demo-bucket.s3.region-code.amazonaws.com/index.m3u8REMOVED=true*' is
 forbidden.`**

**3404 | HTTP not found error**

You specified an HTTP URL for an input file, but the HTTP server
doesn't have the file.

What this means: The HTTP server can't find the file at the location you specified. The file might have been moved, renamed, or deleted.

To resolve this issue:

- Verify that there aren't any typos in the URL.
- Verify that the file exists at the specified location.
- Verify if the file has been moved or renamed.

For more information about HTTP input requirements and troubleshooting, see [HTTP input requirements](http-input-requirements.md "http-input-requirements.md").

Example error messages:

**`3404: '*https://amzn-s3-demo-bucket.s3.region-code.amazonaws.com/index.m3u8REMOVED=true*' not
 found.`**

**3408 | HTTP upload error**

You specified an HTTP URL for an input file, but the upload failed
for a reason that is unrelated to errors 3401, 3403, and 3404.

What this means: There was an unexpected issue when MediaConvert tried to access your HTTP input. This could be because of network problems, server configuration issues, or other HTTP-related errors.

To resolve this issue:

- Try accessing the URL directly to verify it works.
- Contact the team managing the HTTP server.
- Consider downloading the file and uploading it to Amazon S3 instead.
- If the issue persists, contact Support.

For more information about HTTP input requirements and troubleshooting, see [HTTP input requirements](http-input-requirements.md "http-input-requirements.md").

Example error messages:

**`3408: Error uploading file from HTTP source: Connection timed out.`**

**3450 | HTTP server error**

You specified an HTTP URL for an input file, but the HTTP server
returned an error or failed.

What this means: The HTTP server encountered an internal error when MediaConvert tried to access your file. This is an issue with the server hosting your content rather than with MediaConvert.

To resolve this issue:

- Contact the team responsible for the HTTP server.
- Try accessing the file directly to see if you get the same error.
- Consider downloading the file and uploading it to Amazon S3 instead.

For more information about HTTP input requirements and troubleshooting, see [HTTP input requirements](http-input-requirements.md "http-input-requirements.md").

Example error messages:

**`3450: Error encountered when accessing: '*s3://amzn-s3-demo-bucket/file.mp4*'.`**

**3451 | HTTP connection error**

You specified an HTTP URL for an input file, but MediaConvert
couldn't connect to the HTTP server.

What this means: MediaConvert couldn't establish a connection to the HTTP server. The server might be down, unreachable, or the URL might be incorrect.

To resolve this issue:

- Verify that the URL is correct.
- Verify if the server is online and accessible.
- Try accessing the URL directly from a browser.
- Consider downloading the file and uploading it to Amazon S3 instead.

For more information about HTTP input requirements and network connectivity, see [HTTP input requirements](http-input-requirements.md "http-input-requirements.md").

Example error messages:

**`3451: Server could not be reached when accessing: '*s3://amzn-s3-demo-bucket/file.mp4*'.`**

**3457 | Input policy restriction error**

You specified an input location that your policy disallows.

What this means: Your AWS account has an input policy that restricts which input locations MediaConvert can use, and your specified input location violates this policy.

To resolve this issue:

- Use an input location that complies with your organization's policies.
- Contact your AWS administrator if you need an exception to the policy.
- Transfer your content to an approved input location.
- Specify an allowed input location and resubmit your job.

For more information about input policies and restrictions, see [How to allow or disallow input location types using an
Input policy](disallow-inputs.md#input-policies "disallow-inputs.md#input-policies").

Example error messages:

**`3457: You specified an input location that your policy disallows:
 '*s3://amzn-s3-demo-bucket/file.mp4*. Specify an allowed
 input location and resubmit your job.`**

**3452 | Malformed URL with spaces error**

The URL you specified for your HTTP input is malformed.

What this means: The HTTP URL you provided doesn't follow proper URL formatting standards and cannot be processed by MediaConvert.

To resolve this issue:

- Verify that your URL is properly formatted with the correct protocol (http:// or https://).
- Ensure the URL doesn't contain spaces or other unsupported characters.
- Test the URL in a web browser to verify it's accessible.

For more information about HTTP input requirements, see [HTTP input requirements](http-input-requirements.md "http-input-requirements.md").

Example error messages:

**`3452: URL '*http://example.com/invalid url with spaces*' is malformed.`**

**3453 | HTTP redirect error**

MediaConvert can't follow redirects when accessing your HTTP input.

What this means: Your HTTP input URL redirects to another location, but MediaConvert doesn't support following HTTP redirects for security and reliability reasons.

To resolve this issue:

- Use the final destination URL directly instead of a redirecting URL.
- Contact the server administrator to get the direct URL to your content.
- Consider downloading the file and uploading it to Amazon S3 instead.

For more information about HTTP input requirements, see [HTTP input requirements](http-input-requirements.md "http-input-requirements.md").

Example error messages:

**`3453: MediaConvert can't follow redirects when accessing your input: *http://example.com/redirect-url*. For information about HTTP(S) input requirements, see https://docs.aws.amazon.com/mediaconvert/latest/ug/upload-input-files.html#http-input-requirements.`**

**3454 | DNS resolution error**

Name resolution failed when accessing your HTTP input.

What this means: MediaConvert cannot resolve the domain name in your HTTP URL to an IP address. The domain might not exist, be temporarily unavailable, or have DNS configuration issues.

To resolve this issue:

- Verify that the domain name in your URL is correct and exists.
- Check if the domain is accessible from other locations.
- Wait and retry if this is a temporary DNS issue.
- Consider using an IP address instead of a domain name if possible.

For more information about HTTP input requirements, see [HTTP input requirements](http-input-requirements.md "http-input-requirements.md").

Example error messages:

**`3454: Name resolution failed when accessing: '*http://nonexistent-domain.example.com/video.mp4*'.`**

**3455 | SSL/TLS error**

SSL failures encountered when accessing your HTTPS input.

What this means: MediaConvert encountered SSL/TLS certificate or connection issues when trying to access your HTTPS input. This could be due to expired certificates, certificate chain issues, or unsupported SSL configurations.

To resolve this issue:

- Verify that the SSL certificate for your HTTPS server is valid and not expired.
- Check that the certificate chain is properly configured.
- Ensure the server supports modern SSL/TLS protocols.

For more information about HTTPS input requirements, see [HTTP input requirements](http-input-requirements.md "http-input-requirements.md").

Example error messages:

**`3455: SSL failures encountered when accessing: '*https://example.com/video.mp4*'.`**

**3456 | Invalid HTTP server address**

The HTTP server address for your input URL is invalid.

What this means: The server address portion of your HTTP URL contains invalid characters or formatting that prevents MediaConvert from connecting to it.

To resolve this issue:

- Verify that the server address in your URL is correctly formatted.
- Check for any invalid characters in the hostname or IP address.
- Ensure the port number (if specified) is valid.

For more information about HTTP input requirements, see [HTTP input requirements](http-input-requirements.md "http-input-requirements.md").

Example error messages:

**`3456: HTTP server address '*invalid-server-address*' for URL '*http://invalid-server-address/video.mp4*' is invalid.`**

**3458 | Ranged-GET not supported**

The URL you provided doesn't support ranged-GET requests.

What this means: MediaConvert requires HTTP servers to support partial content
requests (HTTP Range requests), but your server doesn't support this
feature.

To resolve this issue:

- Configure your HTTP server to support ranged-GET requests.
- Download the file and upload it to Amazon S3 instead.
- Use a different HTTP server that supports ranged-GET
  requests.

For more information about HTTP input requirements, see [HTTP input requirements](http-input-requirements.md "http-input-requirements.md").

Example error messages:

**`3458: The URL you provided doesn't support ranged-GET requests: '*http://example.com/video.mp4*'.`**

**3999 | HTTP unexpected error**

There was an unexpected error related to retrieving your input
file from an HTTP server.

What this means: MediaConvert encountered an unexpected issue when trying to access your HTTP input. This is a general error code for HTTP-related problems that don't fit other specific error categories.

To resolve this issue:

- Try downloading the file manually to verify it's accessible.
- If you can download it, upload it to Amazon S3 and use that as your input.
- If you can't download it, contact the team managing the HTTP server.
- If you can download it but still get this error with Amazon S3, contact Support.

For more information about HTTP input requirements and troubleshooting, see [HTTP input requirements](http-input-requirements.md "http-input-requirements.md").

Example error messages:

**`3999: Unexpected error when accessing HTTP input: Internal server error.`**
