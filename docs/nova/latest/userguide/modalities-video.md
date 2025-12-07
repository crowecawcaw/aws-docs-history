# Video understanding

The Amazon Nova models allow you to include a single video in the payload, which can be
provided either in base64 format or through an Amazon S3 URI. When using the base64 method, the
overall payload size must remain within 25 MB. However, you can specify an Amazon S3 URI for video
understanding. This approach enables you to leverage the model for longer videos (up to 1 GB
in size) without being constrained by the overall payload size limitation. Amazon Nova models
can analyze the passed video and answer questions, classify a video, and summarize
information in the video based on provided instructions.

| Media File Type | File Formats supported                        | **Input Method**                                                                                                        |
| --------------- | --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Video           | MP4, MOV, MKV, WebM, FLV, MPEG, MPG, WMV, 3GP | Base64<br>_Recommended for payload size less than<br>25 MB_                                                             |
|                 |                                               | Amazon S3 URI<br>_Recommended for payloads greater than 25 MB up to<br>2 GB. Individual files must be 1 GB or smaller._ |

There are no differences in the video input token count, regardless of whether the video
is passed as base64 (as long as it fits within the size constraints) or via an Amazon S3
location.

Note that for 3GP file format, the "format" field passed in the API request should be of
the format "three_gp".

When using Amazon S3, ensure that you are set the "Content-Type" metadata to the correct MIME
type for the video.

## Video size information

Amazon Nova video understanding capabilities support Multi-Aspect Ratio. All videos are
resized with distortion (up or down, based on the input) to **672\*672 square** dimensions before feeding it to the model. The model
utilizes a dynamic sampling strategy based on the length of the video. For Amazon Nova Lite and Amazon Nova Pro, with videos less
than or equal to 16 minutes in duration, a 1 frame per second (FPS) sampling rate is
employed. However, for videos exceeding 16 minutes in length, the sampling rate
decreases in order to maintain a consistent 960 frames sampled, with the frame sampling
rate varying accordingly. This approach is designed to provide more accurate scene-level
video understanding for shorter videos compared to longer video content. We recommend
that you keep the video length less than 1 hour for low motion, and less than 16 minutes
for anything with higher motion. For Amazon Nova Premier, the 1 FPS sampling rate is applied up to a limit of 3,200 frames.

There should be no difference when analyzing a 4k version of a video and a Full HD
version. Similarly, because the sampling rate is at most 1 FPS, a 60 FPS video should
perform as well as a 30 FPS video. Because of the 1 GB limit in video size, using higher
than required resolution and FPS is not beneficial and will limit the video length that
fits in that size limit. You might want to pre-process videos longer than 1 GB.

## Video tokens

The length of the video is main factor impacting the number of tokens generated. To
calculate the approximate cost, you should multiply the estimated number of video tokens
by the per-token price of the specific model being utilized.

The following table provides some approximations of frame sampling and token utilization per video
length for Amazon Nova Pro, Lite, and Micro:

| video_duration        | 10 sec | 30 sec | 16 min  | 20 min  | 30 min  | 45 min  | 1 hr    | 1.5 hr  |
| --------------------- | ------ | ------ | ------- | ------- | ------- | ------- | ------- | ------- |
| frames_to_sample      | 10     | 30     | 960     | 960     | 960     | 960     | 960     | 960     |
| sample_rate_fps       | 1      | 1      | 1       | 0.755   | 0.5     | 0.35556 | 0.14    | 0.096   |
| Estimated token count | 2,880  | 8,640  | 276,480 | 276,480 | 276,480 | 276,480 | 276,480 | 276,480 |

The following table provides some approximations of frame sampling and token utilization per video
length for Amazon Nova Premier:

| video_duration        | 10 sec | 30 sec | 16 min  | 20 min  | 30 min  | 45 min  | 1 hr | 1.5 hr |
| --------------------- | ------ | ------ | ------- | ------- | ------- | ------- | ---- | ------ |
| frames_to_sample      | 10     | 30     | 960     | 1200    | 1800    | 2700    |      |        |
| sample_rate_fps       | 1      | 1      | 1       | 1       | 1       | 1       |      |        |
| Estimated token count | 2,880  | 8,640  | 276,480 | 345,600 | 518,400 | 777,600 |      |        |

The following table provides some approximations of frame sampling and token utilization per video length for
Amazon Nova Lite 1.5

| video_duration        | 10 sec | 30 sec | 16 min  | 20 min  | 30 min  | 45 min  | 1 hr | 1.5 hr |
| --------------------- | ------ | ------ | ------- | ------- | ------- | ------- | ---- | ------ |
| frames_to_sample      | 10     | 30     | 960     | 1200    | 1800    | 2700    |      |        |
| sample_rate_fps       | 1      | 1      | 1       | 1       | 1       | 1       |      |        |
| Estimated token count | 2,880  | 8,640  | 276,480 | 345,600 | 518,400 | 777,600 |      |        |
