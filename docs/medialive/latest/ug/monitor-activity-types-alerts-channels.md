

# List of alerts for channels
<a name="monitor-activity-types-alerts-channels"></a>

The following table lists the alerts that MediaLive might generate for a channel. You can view these alerts in these ways:
+ You can view the alerts for each channel on the MediaLive console. For more information, see [Alerts tab – Viewing alerts](monitoring-console-general.md#view-alerts).
+ You use your preferred AWS SDK or API to monitor alerts about channel activity. For more information, see [Monitoring alerts using the AWS SDKs or API](monitoring-api.md).
+ MediaLive turns alerts into CloudWatch events with the detailType set to `MediaLive Channel Alert`. For an example of the JSON for these events, see [JSON for a state change event](monitoring-cloudwatch-json-state-change.md).


| Alert ID | Alert wording | Description | 
| --- | --- | --- | 
| 5002  | Input Image Missing  | The channel was configured with a URL to an input image (for example, an avail blanking image). The channel can't access the file.  | 
| 5007  | Initial Probe is Taking Longer Than Expected  | The MediaLive pipeline is not yet generating output because it is waiting for an input that it can successfully decode.  | 
| 5008  | Input Resource is Inaccessible  | The channel configuration references a resource that MediaLive can't access. The specific resource is identified in the alert.  | 
| 5010  | Input Removed the Active Program  | The transport stream program that was in use is no longer present in the input.  | 
| 5012  | SCTE-35 Input Data Could Not Be Processed  | MediaLive can't process the SCTE-35 data that is being received. It's possible that the SCTE-35 PTS is not synchronized with the video PTS.  | 
| 5051  | Watermark License Failure  | MediaLive couldn't acquire a valid A/B watermarking license from the configured license source. This can happen if the AWS Secrets Manager secret name is invalid, the secret can't be accessed, or the license file can't be opened. MediaLive continues to encode the output group without watermarks. | 
| 5052  | Watermark Library Initialization Failure  | The A/B watermarking library couldn't be initialized. Possible causes include a rejected license (expired or malformed license, or an operator ID or watermark ID length that doesn't match the license). MediaLive omits watermarking for the affected output group and continues to encode the channel.  | 
| 5101  | Audio Not Detected  | The channel can't decode audio in the source. Either the active input is unavailable, or the active input doesn't contain audio, or the audio is encrypted.  | 
| 5102  | Audio PID Missing  | The audio selector for the current input specifies a PID (as the source of the audio), but that PID doesn't exist in the input.  | 
| 5104  | Audio Requires Dolby E Decode  | The input requires Dolby E decode, but a Dolby E decode audio track selector was not specified. MediaLive might replace the audio with silence.  | 
| 5201  | Video Not Detected  | The channel can't decode the video in the source. Either the active input is unavailable, or the active input doesn't contain video, or the video is encrypted.  | 
| 5202  | Black Video Detected  | Black video was detected. MediaLive might have performed an automatic input failover.  | 
| 5301  | HTTP Get Failed  | The HTTP Get failed, so retrieval of the asset failed. Perhaps there was a network issue, or the HTTP server had a problem, or the server requires user credentials.  | 
| 5302  | Stopped Receiving UDP Input  | A UDP input (which includes RTP, MediaConnect, and Link inputs) did not receive any packets for at least one second.  | 
| 5304  | RTP Header Corruption  | The channel is configured to receive an RTP input, but the packets received don't conform to RTP.  | 
| 5305  | RTMP Stream Not Found  | The channel is configured to receive an RTMP input, but the specified RTMP stream is not being received.  | 
| 5307  | RTMP Has No Audio/Video  | The channel is configured to receive an RTMP input, but the specified RTMP stream is no longer present.  | 
| 5308  | RTMP Server Disconnected  | The channel is configured to receive an RTMP input, but the specified RTMP stream has disconnected.  | 
| 5309  | RTMP Input Connect Failed  | The channel is configured to receive an RTMP input but there was a failure to connect to the RTMP URL.  | 
| 5313  | HLS Segments Could Not Be Decrypted  | An HLS input could not be decrypted. Check that the key provided for decryption is correct.  | 
| 5314  | Input Double-Publishing Detected  | Multiple source IP addresses are sending packets to the same MediaLive input. This situation typically causes decode errors.  | 
| 5315  | Data PID Missing  | A transport stream data PID was specified in the channel configuration, but it isn’t available in the input.  | 
| 5316  | Input PTS Behind PCR  | A transport stream input contains video and/or audio frames that are arriving too late to decode based on comparison of their PTS (presentation timestamp) to the transport stream PCRs (program clock references). MediaLive might not be able to decode the video or audio.  | 
| 5601  | Input Failed Over  | An input has failed and the channel is configured for automatic input failover. MediaLive has switched to the other input.  | 
| 6001  | ESAM HTTP Post Failed  | A HTTP Post to the configured ESAM server failed. ESAM is part of the SCTE 35 configuration for the channel.  | 
| 6002  | Failed to Open UDP Socket For Write  | The channel failed to open a UDP output connection.  | 
| 6003  | Failed to Write to UDP Socket  | The channel failed to write a UDP output packet.  | 
| 6005  | Failed to Create Output File or Socket  | The channel failed to create an output file.  | 
| 6006  | Failed to Write to Output  | The channel failed to write data to an output.  | 
| 6007  | Failed to Close or Finalize The Output  | The channel failed to write data to an output  | 
| 6008  | Failed to Delete Output File  | The Channel failed to delete an output file.  | 
| 6010  | Failed HTTP Post Output Request  | An HTTP Post to an output failed.  | 
| 6015  | Failed to Get HTTP Output Token  | The channel couldn't write to an output because it was unauthorized. For example, an HTTP access returned 401 (Unauthorized) or 403 (Forbidden).  | 
| 6018 | Failed RTMP Connection | The channel is configured to send RTMP output, but was not able to connect to its endpoint | 
| 6028  | Failed to Validate Certificate Chain When Publishing  | An HTTP write failed because the remote server's SSL certificate or SSH fingerprint was deemed not OK.  | 
| 6030  | The Configured TS Muxer Bitrate is Too Low  | A transport stream output was configured and the bitrate specified is not sufficient to carry the video, audio, and data that need to be carried within it. The channel includes a transport stream output. The bitrate specified in the output is too low for the combined video, audio, and data.  | 
| 6031  | Timecode Synchronization Threshold Exceeded  | The channel was configured with a TimecodeConfiguration SyncThreshold, and the output timecode was resynchronized with the input timecode.  | 
| 6033  | Pipeline is Paused  | The MediaLive pipeline has been paused.  | 
| 6035  | Unable to perform requested color space conversion  | The channel was unable to perform the configured color space conversion.  | 
| 6036  | Output Group is Paused  | An output group has been paused due to input loss. This only occurs if the output group is not configured to emit content on input loss.  | 
| 6038  | Nielsen Audio Watermarks could not be initialized  | Nielsen audio watermarks could not be initialized.  | 
| 6043  | Failed To Upload Thumbnail  | Video thumbnails couldn't be uploaded. MediaLive might need access to Amazon S3.  | 
| 6044 | Unable to place splice point at IDR boundary | The channel can't insert an SCTE-35 splice point into the output at the correct time. The output frame rate must be a multiple of the slowest frame rate. Change your configuration so that all frame rates are multiples of each other. | 
| 6045 | The MQCS score is low for this pipeline | At least one of the outputs in the pipeline has a media quality confidence score (MQCS) that is below the acceptable level. | 
| 6047 | Unable to retrieve secret from AWS Secrets Manager | Your channel couldn't retrieve a secret from AWS Secrets Manager. Verify that the secret ARN in the channel configuration is correct. Confirm that the secret exists in the same AWS Region as the channel and that the channel's IAM role has secretsmanager:GetSecretValue permission for the secret. | 
| 6501  | Large Upload Cache Backlog  | The channel maintains a cache of files pending upload that it clears after successful delivery to the output. The cache has more files pending upload to the configured destination than expected, which might indicate a temporary network slowdown between MediaLive and the destination. Or it might indicate that the destination server is slower than expected.  | 
| 6704  | Embedded Timecodes Too Far Apart for Pipeline Locking  | Pipelines in the pipeline locking pool have embedded input timecodes that are too far apart for pipeline locking synchronization. This typically occurs when pipelines are receiving content from different input sources or when input sources are not properly synchronized.  | 
| 6707  | Output Configuration Mismatch Detected  | Pipelines in the pipeline locking pool have incompatible output configurations and pipeline locking has been disabled. This typically occurs when channels have different output group counts, segment lengths, muxer configurations, or video encoding parameters. Ensure all channels in the pipeline locking pool have identical output configurations.  | 
| 6751  | Unable to Establish Video Alignment on Input Content  | MediaLive is unable to synchronize video content across pipelines in the pipeline locking pool using [video aligned locking](pipeline-locking-verify-input.md#pipeline-locking-video-alignment-inputs). This typically occurs when input content differs between pipelines. Ensure that all pipelines in the pool are receiving identical source content.  | 