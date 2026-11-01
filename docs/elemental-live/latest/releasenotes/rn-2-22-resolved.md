

# Resolved issues in version 2.22 and 3.22
<a name="rn-2-22-resolved"></a>

The **Version** column shows the point release that the issue applies to.

## Resolved issues in Elemental Live 2.22
<a name="rn-2-22-resolved-live"></a>

The following table lists the resolved issues in Elemental Live 2.22.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 2.22.0 | SOCK-37117 | Alerts | A new alert has been added when the output UDP buffer underflows. An underflow often indicates that the buffer\_msec value is too small. | 
| 2.22.0 | SOCK-37186 | Alerts | An alert is now set for any statmux channel when complexity data from the encoder is arriving too late to be used. The alert is cleared 3 seconds after the complexity data begins arriving on time. The alert code is 7007, and an example of the alert message is: Setting alert [7007] [Program[program-A][0]] [7007-Program[program-A][0]] [Program progra-A late arriving complexity data from encoder on pipeline 0. | 
| 2.22.4 | SOCK-37242 | Alerts and messages | The alert 6004 Output Protection Engaged now automatically clears after 30 seconds. Additionally, the text of the alert has been updated to read: Output loss detected on output (Primary: udp://xxx.xxx.xxx.xxx?interface=ethX). Starting transmission to ensure output continuity. | 
| 2.22.4 | SOCK-37302 | Alerts and messages | Fixed a problem with UDP underflow alerts that weren't clearing properly. | 
| 2.22.1 | SOCK-37470 | Alerts and messages | Alert 5010 "Program input missing" is now automatically cleared after an input switch. | 
| 2.22.0 | SOCK-37138 | Audio | A problem has been fixed with distortion in the audio for SMPTE ST 2110-31 (Dolby Digital and Dolby Digital Plus audio streams). | 
| 2.22.4 | SOCK-37357 | Audio | Fixed scenario that would stop event audio from resuming, when audio channel count changed in an active event when using audio selector groups. | 
| 2.22.3 | SOCK-37592 | Audio, mute | Previously, if you used the API to call the mute\_audio twice or more, you had to call the unmute\_audio twice to cancel the mute. This problem has been fixed. | 
| 2.22.0 | SOCK-37109 | Captions | There was a problem with alignment in WebVTT output captions. This problem applies when the input source has Teletext or embedded (608/708) captions, and the event has been configured to produce WebVTT captions with pass style information enabled. The problem occurs when the captions are configured to automatically detect the VTT position. Captions that appear centered in the original input, while marked as align:center in the WebVTT output, do not appear centered when viewed. This problem has been fixed. | 
| 2.22.1 | SOCK-37482 | Captions, ancillary | Fixed a timing problem that could occur when in ancillary captions in a Quicktime output container. | 
| 2.22.1 | SOCK-37487 | Captions, EBU-TT-D and WebVTT | Fixed a timestamp problem in EBU-TT-D output captions or WebVTT output captions. | 
| 2.22.1 | SOCK-37464 | Captions, WebVTT | Previously, the timestamp on WebVTT output captions might be out of order, which could cause problems for the downstream system. This problem has been fixed. | 
| 2.22.3 | SOCK-37618 | Color space | Previously, there was a problem with handling color space in an SDI input. This problem has been resolved. | 
| 2.22.5 | SOCK-37885 | Deployment | Previous versions of AWS Elemental Live include an expired root certificate that might cause problems with one of the libraries that Elemental Live uses. The certificate has been removed. | 
| 2.22.1 | SOCK-37499 | Drivers | Previously, SSH connectivity could be lost when upgrading the TG3 NIC driver if the SSH connection and driver were both on the eth0 interface. This problem no longer occurs during an upgrade. | 
| 2.22.1 | SOCK-37527 | Drivers | Previously, there was a problem with the TG3 or BNXT\_EN NIC firmware installation. If the firmware was out of date but the respective driver was up to date, the firmware would not be installed. Now, the firmware will always be upgraded, regardless of the driver update status. | 
| 2.22.3 | SOCK-36317 | Input switching | Fixed scenarios where Live could become unresponsive when doing an input switch to an input whose frame rate is double that of the output, and there is both an interlaced and progressive output. | 
| 2.22.1 | SOCK-37175 | Input switching | Previously, there was a problem with switching inputs where the current input and the new input didn't have the same number of audio selectors. In this case, the input switch would not occur. Now, the switch will occur. Although note that the number of audio encodes in the output might not be as expected. For optimal user experience, all inputs must have the same number of audio selectors, with the same languages. | 
| 2.22.0 | SOCK-37299 | Input switching | When customers schedule an input switch ahead of the switch time, Live starts preparing the input. In a scenario where the audio sample format in the source changes between the probe and the switch time, the updated audio information is not passed to audio sync. This resulted in corrupted audio on the output. The issue has been fixed. | 
| 2.22.1 | SOCK-37488 | Input switching | Previously there was a problem when performing an input switch from an input with embedded captions extracted from SMPTE 2038 ancillary data to an input with embedded captions extracted from the native TS. Live didn't extract the captions from the new input. This problem has been resolved. It. | 
| 2.22.3 | SOCK-37652 | Input switching | Previously, there was a race condition that could cause Elemental Live to crash when the user set up motion graphics and input switching in the same event. | 
| 2.22.3 | SOCK-35661 | Inputs, HDMI | Previously, when Elemental Live stopped ingesting an HDMI source, there was logic that caused a 10 second delay when Live started ingesting the source again. HDMI sources no longer have this extra 10 second delay at re-startup. | 
| 2.22.3 | SOCK-37764 | Inputs, SDI | A problem has been fixed with Elemental Live being slow to start ingest SDI inputs. | 
| 2.22.3 | SOCK-37613 | Inputs, SMPTE 2110 | An improvement has been made for SMPTE 2110 inputs, so that Elemental Live can now read both SDP files that include source filters and files that don't include source filters. | 
| 2.22.4 | SOCK-37799 | Installing | Fixed issues where installer would fail when it had no internet access. | 
| 2.22.1 | SOCK-35472 | Logs | Previously, both Elemental Live and Conductor Live mishandled situations where a port was misconfigured. The mishandling resulted in a dump of messages in the logs, filling up the logs. This problem has been fixed. The logs are no longer flooded with messages. | 
| 2.22.0 | SOCK-37225 | Logs | There was an issue where the plat-api logs would fill up the log partition. This has been fixed by limiting the verbosity of the logs and decreasing the rotation duration. | 
| 2.22.1 | SOCK-37471 | Output locking | Previously, there was a problem in outputs that had SCTE-35 message and that had output locking enabled. The problem could lead to segment drift. This problem has been fixed. | 
| 2.22.1 | SOCK-37473 | Output locking | Previously, it sometimes happened that synchronizing of outputs that were set up with output locking might fail. This problem has been fixed. | 
| 2.22.1 | SOCK-37481 | Output locking | Previously, there was a problem with segment length and synching of audio and video in outputs with output locking enabled. This problem has been fixed. | 
| 2.22.4 | SOCK-37659 | Output quality | Previously, there was a problem that manifested in several ways in the output: low VQ (video quality), slow frame rate, dropped audio frames. This problem has been fixed. | 
| 2.22.0 | SOCK-37330 | Outputs | There is a problem with Live events that have a 4K source, and that have more than one output that is full HD (1920x1080) or lower resolution, and with the deinterlacer explicitly enabled. In some instances, one or more of the outputs may be incorrectly windowboxed (that is, there are black bars on all four sides of the image). This problem has been fixed. | 
| 2.22.3 | SOCK-37599 | Outputs to MediaStore | Previously, outputs to AWS Elemental MediaStore caused memory usages to increase by 20% over 12 hours. This problem has been fixed. | 
| 2.22.3 | SOCK-37646 | Outputs, Archive | Previously, there was a problem in Archive outputs sent to Amazon S3. With a very large or a small ("0") rollover interval, Elemental Live was failing to upload the content to Amazon S3, which resulted in a timeout error. The issue has been fixed. If no interval is provided, timeout duration for uploads will fall back to default to 10 minutes. Otherwise, a suitable timeout will be calculated based on the rollover interval provided by the customer. | 
| 2.22.1 | SOCK-36866 | Outputs, DASH | A problem has been fixed in events with an AWS Elemental MediaStore container as the destination in a DASH output. Previously, the manifest file was not updated after a network outage. The problem has now been fixed. | 
| 2.22.4 | SOCK-37239 | Outputs, DASH | Previously, there was a problem with storage of the SPS/PPS data in a DASH output stream. This problem could result in the downstream player being unable to play the content. This problem has been fixed. | 
| 2.22.1 | SOCK-37467 | Outputs, HLS | The EXTINF durations in FMP4 HLS I-Frame Only Playlists are now correct. Previously, if output locking created a short segment, that was not reflected in the EXTINF duration which has now been fixed. | 
| 2.22.1 | SOCK-37476 | Outputs, HLS | Previously, there was a problem with setting segment size for video outputs in an HLS output group that also contained a frame capture encode. The problem had a detrimental effect on SCTE-35 messages in the transport stream. This problem will no longer occur. | 
| 2.22.1 | SOCK-37489, SOCK-37490 | Outputs, Microsoft Smooth | Previously, a Microsoft Smooth output might have a corrupt or missing header. This problem has been fixed. | 
| 2.22.3 | SOCK-37671 | Outputs, Reliable TS | When Elemental Live tries to make a connection with Reliable TS, an alert now appears ("ReliableTs Connection Alert"). The alert now disappears when the connection has been made. | 
| 2.22.3 | SOCK-37724 | Outputs, Reliable TS | Previously, in the Reliable TS output group on the web interface, the Latency setting was omitted from the SRT and Zixi options. This has been fixed. | 
| 2.22.1 | SOCK-37469 | Outputs, RTMP | Previously, there was a problem with RTMP output that failed to deliver but that didn't receive an error message. These connections could linger indefinitely. Now, Live will reset the connection. | 
| 2.22.3 | SOCK-37537 | Outputs, SMPTE 2110 | For SMPTE 2110 Output, an improvement has been made in this release to indefinitely retry sending whenever the send response failure code indicates the send queue is temporarily full. There is a 100 microsecond delay between each retry. | 
| 2.22.4 | SOCK-37851 | Outputs, SMPTE 2110 | Previously, a crash could occur when streaming a SMPTE 2110 output with JPEG-XS video. The crash was related to lack of memory. This problem with handling the memory has been fixed. | 
| 2.22.0 | SOCK-37017 | Outputs, UDP | The maximum video buffer delay milliseconds on an MPTS now have a lower bound of 250 milliseconds which reduces latency at the expense of video quality. Each MPTS now has an encoder\_buffer\_msec setting that controls the UDP output buffering on all channels in the MPTS. Lower values reduce latency but may also cause instability during input switching or on heavily loaded nodes. | 
| 2.22.1 | SOCK-37485 | Outputs, UDP | Previously, a DNS failure on UDP output might cause permanent loss of output. This problem has been fixed. | 
| 2.22.3 | SOCK-37628 | Outputs, UDP | Previously, UDP output underflow would occur on the Live events when using a Statmux with MPEG-2 channels. These output underflows should no longer occur. | 
| 2.22.3 | SOCK-37630 | Performance | Elemental Live now ensures CPUs will not throttle frequency by using lower power states, to ensure maximal performance. | 
| 2.22.2 | SOCK-36929 | SCTE-35 | For a SCTE 104 avail (from an SDI input), there was a problem in computing the splice time that is embedded in a MS Smooth sparse track. For downstream software that obtains the avail start time from the MS Smooth sparse track, the result was that the video froze for about 2 seconds at the start time of the avail. This problem has been resolved. The start time of the avail that is embedded in a MS Smooth sparse track is now correct, and the video no longer freezes. | 
| 2.22.4 | SOCK-36740 | Security | The sudo package installed on Live and Conductor nodes has been upgraded to 1.8.23-10\_9.1 to patch security vulnerability CVE-2021-3156. This upgrade applies to both CentOS and RHEL. | 
| 2.22.3 | SOCK-37656 | SMPTE 2110 | Previously, Elemental Live entered a null value in some 2110 transport parameters that are not required. Null values are not allowed. This problem has been fixed. Also, nmos-live automatically updates to newer versions. | 
| 2.22.1 | SOCK-36668 | Starting and stopping | There was a fix to intermittent problems with activating the appliance after a software restart, in appliances with a more advanced network configuration. | 
| 2.22.5 | SC-4321 | Statmux | There was an issue in the 2.22.4 version of AWS Elemental Live that caused Statmux MPTS to fail. This issue has been fixed. If you use AWS Elemental Statmux, you should skip 2.22.4 when you upgrade, and install this new version instead. | 

## Resolved issues in Statmux 2.22
<a name="rn-2-22-resolved-statmux"></a>

The following table lists the resolved issues in Statmux 2.22.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 2.22.0 | SOCK-37286 | Alerts | Statmux will now set an alert if the outputting of interleaved TS data falls below real time. | 
| 2.22.2 | SOCK-37243 | Alerts and logs | Previously, when a channel started in a Statmux MPTS, there were many alerts. These unnecessary alerts no longer appear. | 
| 2.22.4 | SC-4262 | Bandwidth | The new default behavior on a Statmux MPTS is to suppress null packets for communications between the Live channel and Statmux. This change reduces the bandwidth load. | 
| 2.22.2 | SOCK-37636 | Install | Starting with Elemental Live 2.22.2, Statmux core files will be stored in the directory /data/server/cores/. | 
| 2.22.1 | SC-4271 | Modifying a running MPTS | Previously, modifying a running MPTS in a 1:1 statmux redundancy group didn't reconfigure the secondary MPTS. Now, both MPTS configurations are updated. | 
| 2.22.3 | SOCK-37628 | Outputs, UDP | Previously, UDP output underflow would occur on the Live events when using a Statmux with MPEG-2 channels. These output underflows should no longer occur. | 
| 2.22.0 | SOCK-37017 | Video buffer | The maximum video buffer delay milliseconds on an MPTS now have a lower bound of 250 milliseconds which reduces latency at the expense of video quality. Each MPTS now has an encoder\_buffer\_msec setting that controls the UDP output buffering on all channels in the MPTS. Lower values reduce latency but may also cause instability during input switching or on heavily loaded nodes. | 
| 2.22.2 | SOCK-37505 | Video quality | An optimization has been made that automatically improves the video quality in a Statmux MPTS. | 

## Resolved issues in Conductor Live 3.22
<a name="rn-2-22-resolved-cl3"></a>

The following table lists the resolved issues in Conductor Live 3.22.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 3.22.2 | SC-4227 | Alerts and logs | Previously, the logstash service would eventually fill up the disk with log messages in /var/log/messages. This has been resolved by configuring logstash to only log messages for warnings and higher severity messages. | 
| 3.22.4 | SC-4254 | Alerts and messages | Conductor alerts that have never been set will no longer appear in the list of inactive alerts. Only alerts that have first been set and then cleared will show in the list of inactive alerts. | 
| 3.22.4 | SC-4312 | Alerts and messages | Conductor Live alerts now display a Time Cleared field that shows when the alert was last cleared. If the alert has never been cleared, this field is empty. | 
| 3.22.3 | SC-4315 | Failover | Previously, there was an issue where the channels on an Elemental Live node would not fail over correctly. This problem has been fixed. | 
| 3.22.2 | SOCK-37648 | License | There is no detailed error message if the Statmux license (which is required to use Statmux features of Conductor Live) is not installed on the Conductor Live appliance. Instead, when the channel starts, the MPTS row on the web interface turns red and the Status change to Error. If you get this error, open the Settings>Licenses page on the web interface to determine if the error has occurred because the license is missing. In a future release, we plan to add a specific error message for this problem. | 
| 3.22.4 | SC-4307 | Memory handling | There was a problem with memory handling that could manifest in several ways: folders on the node might run out of space, which could affect failover, or database replication, backup, and syncing. This problem has been fixed. | 
| 3.22.2 | SC-4277 | Statmux | Previously, an MPTS could time out when starting. This issue has been fixed. | 
| 3.22.2 | SC-4271 | Statmux | Previously, there was an issue with modifying a Statmux MPTS that was running in a redundant configuration. The second node didn't always get updated. This issue has been fixed: both nodes get updated. | 
| 3.22.2 | SC-4250 | Statmux | There was a problem with modifying the min and max bitrate fields in a Statmux MPTS. This is the scenario that applied: When you add a channel as an MPTS member, you can set custom values for the bitrate fields for that channel. You do this from the MPTS Control page in Conductor Live. Previously, if you then changed the channel so that the channel uses a different profile, the custom bitrate values reverted to the default for that profile. Now, if you switch the profile, the custom values are kept if they are within the acceptable range for that profile. The bitrate values only revert to the default if the custom rates are outside the acceptable range. | 
| 3.22.1 | SC-4290 | Web interface | Previously, when you pasted a URL on a screen where channel filters are set, the paste action would clear the filters. Pasting no longer clears the filters. | 
| 3.22.3 | SC-4296 | Web interface and REST API | Fixed scenarios where Conductor Live was not able to process Live/Statmux node/channel updates in a timely manner, resulting in decrease in responsiveness of commands and status in the Conductor Live web interface. | 