

# Resolved issues in version 2.21 and 3.21
<a name="rn-2-21-resolved"></a>

The **Version** column shows the point release that the issue applies to.

## Resolved issues in Elemental Live 2.21
<a name="rn-2-21-resolved-live"></a>

The following table lists the resolved issues in Elemental Live 2.21.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 2.21.3 | SOCK-37094 | API | Sometimes, the response time of mute/unmute API call goes up abnormally if the API call is requested repeatedly. This problem has been fixed. | 
| 2.21.3 | SOCK-36040 | Authentication | There was an issue where in certain circumstances PAM authentication would not allow a user to log in. This has been resolved. | 
| 2.21.1 | SOCK-34897 | Captions | When running an event with teletext input and WebVTT output with "Pass Style Information" enabled, there were occasional extraneous characters present in the output. This is now fixed. | 
| 2.21.3 | SOCK-36196 | Captions | Fixed an issue of RTMP onCuePoint SCTE-35 ad break message having unexpectedly long preroll value. | 
| 2.21.4 | SOCK-37109 | Captions | There was a problem with alignment in WebVTT output captions. This problem applies when the input source has Teletext or embedded (608/708) captions, and the event has been configured to produce WebVTT captions with pass style information enabled. The problem occurs when the captions are configured to automatically detect the VTT position. Captions that appear centered in the original input, while marked as align:center in the WebVTT output, do not appear centered when viewed. This problem has been fixed. | 
| 2.21.3 | SOCK-37122, SOCK-37106 | Captions | There was a problem starting in Live 2.20.1 that caused output captions to be out of sync with the video. This problem could occur when the source captions was Teletext. This issue has been fixed. | 
| 2.21.5 | SOCK-37499 | Drivers | Previously, SSH connectivity could be lost when upgrading the TG3 NIC driver if the SSH connection and driver were both on the eth0 interface. This problem no longer occurs during an upgrade. | 
| 2.21.5 | SOCK-37527 | Drivers | Previously, there was a problem with the TG3 or BNXT\_EN NIC firmware installation. If the firmware was out of date but the respective driver was up to date, the firmware would not be installed. Now, the firmware will always be upgraded, regardless of the driver update status. | 
| 2.21.1 | SOCK-34727 | Event log | The XML REST API Elemental Live event status was not reporting values for <buffer\_avg>, <buffer\_max>, and <fill\_msec>. This is now fixed. | 
| 2.21.4 | SOCK-37222 | Firmware | The NIC driver firmware has been upgraded to resolve issues on appliances that include the 1G Cu SFP link speed interface. These issues occurs on specific appliances in the L800 series. | 
| 2.21.3 | SOCK-37063 | Input | Sometimes Live wasn't always able to find Sync Bytes in Network Inputs. This prevented Live from using some sources. This problem has been fixed. | 
| 2.21.5 | SOCK-37175 | Input switching | Previously, there was a problem with switching inputs where the current input and the new input didn't have the same number of audio selectors. In this case, the event would stop. Now, the switch will occur. Although note that the number of audio encodes in the output might not be as expected. For optimal user experience, all inputs must have the same number of audio selectors, with the same languages. | 
| 2.21.4 | SOCK-37299 | Input switching | When customers schedule an input switch ahead of the switch time, Live starts preparing the input. In a scenario where the audio sample format in the source changes between the probe and the switch time, the updated audio information is not passed to audio sync. This resulted in corrupted audio on the output. The issue has been fixed. | 
| 2.21.3 | SOCK-37099 | Input, SRT | There is a problem when a Live event is configured with either two events that use SRT as the input type or with two events that use AWS Elemental MediaConnect as the input type. Sometimes, when the even switches from one input to the other, Live crashes. This problem has been fixed. | 
| 2.21.3 | SOCK-36109 | Input, TS | There is sometimes a problem with the way that Live encodes a TS source. If the bitrate of the elementary stream is very low, "packet interleave error" messages might appear in the logs. An improvement has been implemented to resolve this problem. If you are still seeing this message, contact AWS Elemental Support for help. | 
| 2.21.1 | SOCK-36684 | Inputs | Elemental Live could fail to probe again after an input became degraded. This is now fixed. | 
| 2.21.1 | SOCK-36840 | Inputs | The Elemental Live encoder sometimes failed during resolution changes. This is now fixed. | 
| 2.21.2 | SOCK-36957 | Inputs | Changing the resolution on MPEG2, H264, and H265 inputs could cause Elemental Live to fail. This is now fixed. | 
| 2.21.2 | SOCK-36974 | Inputs | The Elemental Live encoder sometimes failed when a counter rolled over after 414 days. This is now fixed. | 
| 2.21.0 | SOCK-36635 | Inputs - Audio | Elemental Live events that used a SMPTE ST 2022-6 stream with AC-3 audio as an input could crash during ingest if the first AC-3 audio frame parsed had an invalid AC-3 header. This is now fixed. The invalid AC-3 header is now discarded so that the audio stream continues to be probed until a valid audio frame is processed. | 
| 2.21.1 | SOCK-36674 | Inputs - Failover | Differences between CPU and GPU HEVC NAL could cause problems with failover. An environment variable now forces CPU only systems to use 64 x 46 HEVC tree blocks so that NAL packet PPS and SPS values between CPU and GPU encodes match. | 
| 2.21.1 | SOCK-36701 | Inputs - Frame rates | Frame rates that were not valid could cause Elemental Live to terminate. This is now fixed. | 
| 2.21.0 | SOCK-36593 | Inputs - Overlays and captions | In some situations, motion graphics overlays and non-passthrough image captions (burn-in, SMPTE-TT, and CFF-TT) appeared backwards or upside-down for HD inputs. This is now fixed. | 
| 2.21.0 | SOCK-36034 | Inputs - SDI | Ingest had the potential to fail if the SDI device was not recognized. This is now fixed. | 
| 2.21.1 | SOCK-36737 | Inputs - SMPTE | When an event is configured to use a SMPTE ST 2110 or SMPTE ST 2022-6 input with SMPTE ST 2022-7 redundancy, the network input could drop packets consistently. This could lead to the per-event ingest log filling up the /opt disk partition. This is now fixed. | 
| 2.21.1 | SOCK-36766 | Inputs - SMPTE ST 2110; Audio | Issues with packet timestamps could cause audio to drop for SMPTE ST 2110 inputs. This is now fixed, and SMPTE ST 2110 inputs now require the precision time protocol (PTP) of the source to be synchronized. | 
| 2.21.1 | SOCK-36540 | Inputs; Captions | Elemental Live events with SCTE-27 caption PIDs that did not match between inputs could cause validation errors that halted events in a preprocessing state. This is now fixed. | 
| 2.21.0 | SOCK-25526 | Inputs; CL3 | The ZeroMQ library is updated to version 4.3.3 to address potential crashes in the web layer. | 
| 2.21.1 | SOCK-36769 | Inputs; Downgrade | Downgrading to version 2.18.1 or later of Elemental Live while simultaneously attempting to restore a database could cause the downgrade to fail. This is now fixed. | 
| 2.21.5 | SOCK-35472 | Logs | Previously, both Elemental Live and Conductor Live mishandled situations where a port was misconfigured. The mishandling resulted in a dump of messages in the logs, filling up the logs. This problem has been resolved, the logs are no longer flooded with messages. | 
| 2.21.2 | SOCK-36915 | Logs; Statmux; CL3 | Data that was retained for 90 days could fill up the logs, causing partitions to run out of space. This data is now retained for 30 days to avoid the issue. | 
| 2.21.3 | SOCK-36947 | Motion graphics overlay | Fixed problem where creating new motion graphics overlays could make Elemental Live crash. | 
| 2.21.1 | SOCK-36665 | Network - Log | In some situations, Elemental Live logged numerous duplicate messages in a short time frame, filling up the /var/log/ partition. This is now fixed. | 
| 2.21.0 | SOCK-35851 | NMOS | Previously, NMOS did not work properly in authenticated environments. This is now fixed. | 
| 2.21.3 | SOCK-37013 | Output | There was a problem with the output produced when the event includes a SMPTE 2110 source. The audio and video were not synchronized. This problem has been fixed. | 
| 2.21.3 | SOCK-34214 | Output locking | In complex output locking workflows, rare instances of caption packet corruption might cause a frame to have a DTS value that is less than the previous frame. The cause of the packet corruption has been fixed. | 
| 2.21.3 | SOCK-36121 | Output, DASH | A problem could cause intermittent or complete failure in playback of a DASH output sent to Akamai and then to a Shaka player. | 
| 2.21.3 | SOCK-36994 | Output, DASH | The Dolby MediaValidator failed the validation on DASH streams because the manifest was missing information about DVH1 or DVHE. Live now adds the appropriate information, depending on the HVC1 setting in the output. | 
| 2.21.3 | SOCK-37121 | Output, DASH | Under certain circumstances for DASH output containing audio, a signaling was missing from the DASH manifest. This is now fixed. | 
| 2.21.3 | SOCK-36113 | Output, HLS | There was a problem with the HLS manifest. Sometimes, invalid data was being appended to the EXT-X-MAP:URI line in the manifest. This problem has been fixed. | 
| 2.21.3 | SOCK-36316 | Output, HLS | When you have configured an HLS output group to pause when you start the event, Live might insert a discontinuity marker too early in the HL output. | 
| 2.21.3 | SOCK-36963 | Output, M2TS | There was a problem with missing data when upgrading from 2.19.5 The settings for an M2TS output were deleted. This problem has been resolved; starting with 2.21.3, the settings are no longer deleted. | 
| 2.21.2 | SOCK-34214 | Outputs | Rare instances of caption packet corruption could cause non-monotonic DTS values. This is now fixed. | 
| 2.21.2 | SOCK-35976 | Outputs | After the WebDAV server disconnected and was restored, DASH output could still fail to recover the stream. This is now fixed. | 
| 2.21.2 | SOCK-36044 | Outputs | Publishing to an endpoint in chunked transfer mode could cause playback to fail when using DASH for ultra low latency streaming. This is now fixed. | 
| 2.21.1 | SOCK-36101 | Outputs | An SNMP trap cannot be sent out if the event name contains a double byte character. To work around this, Elemental Live now replaces invalid ASCII-8BIT characters with ? for SNMP traps that use event names. | 
| 2.21.1 | SOCK-36823 | Outputs | Previously, one failed endpoint statistics call resulted in a Zixi send error. It now takes three sequential failed endpoint statistics calls to trigger a Zixi send error and cause the link to reset and reconnect. | 
| 2.21.2 | SOCK-36875 | Outputs | When DVB subs were missing PTS values, Elemental Live DVB subs could become out of sync. This is now fixed. | 
| 2.21.2 | SOCK-36931, SOCK-36693 | Outputs | There was an issue that caused streaming to local Amazon S3 storage to fail with a 403 error. This is now fixed. | 
| 2.21.4 | SOCK-37330 | Outputs | There is a problem with Live events that have a 4K source, and that have more than one output that is full HD (1920x1080) or lower resolution, and with the deinterlacer explicitly enabled. In some instances, one or more of the outputs may be incorrectly windowboxed (that is, there are black bars on all four sides of the image). This problem has been fixed. | 
| 2.21.1 | SOCK-36822 | Outputs - HLS | Missing presentation timestamp (PTS) values could result in delayed captions. This is now fixed. | 
| 2.21.1 | SOCK-36266 | Outputs - HLS; Output locking | Previously, the \#EXT-X-DISCONTINUITY HLS tag was placed a segment late for output locking workflows when marking audio configuration discontinuities on remote encoders. This is now fixed. It now is consistently placed correctly across all output-locked encoders. | 
| 2.21.0 | SOCK-36595 | Outputs - MS Smooth | HTTP sometimes timed out after 30 seconds when publishing Microsoft Smooth (MSS) output to IIS servers/endpoints. This is now fixed. | 
| 2.21.1 | SOCK-36377 | Outputs - SMPTE ST 2022 | RTP streams can use FEC packets for error correction. According to SMPTE ST 2022-1-2007, FEC packets must have the same source port as data packets. Elemental Live was not doing this. Elemental Live now sets the FEC packet source port to be the same as the data packet source port. | 
| 2.21.0 | SOCK-36580 | Outputs - SMPTE ST 2110 | Downgrading to a previous version of Elemental Live with events that had SMPTE ST 2110 outputs sometimes failed to retain video settings. This is now fixed. | 
| 2.21.5 | SOCK-36866 | Outputs, DASH | A problem has been fixed in events with an AWS Elemental MediaStore container as the destination in a DASH output. Previously, the manifest file was not updated after a network outage. The problem has now been fixed. | 
| 2.21.0 | SOCK-36385 | Outputs; CL3 | Elemental Live events in Elemental CL3 clusters sometimes failed over to a backup, but came back with events running that could not be stopped by CL3. This caused duplicate events to be published to customer endpoints. This is now fixed. | 
| 2.21.2 | SOCK-36934 | Outputs; CL3 | The monitoring output feed for Elemental Live to Statmux communication erroneously included telemetry data. This is now fixed. | 
| 2.21.1 | SOCK-36832 | Outputs; Statmux; CL3 | The variable bitrate (VBR) check box was removed from the output transport stream settings page erroneously. This is now fixed, and the check box is once again present and functional. | 
| 2.21.6 | SOCK-36929 | SCTE-35 | For a SCTE 104 avail (from an SDI input), there was a problem in computing the splice time that is embedded in a MS Smooth sparse track. For downstream software that obtains the avail start time from the MS Smooth sparse track, the result was that the video froze for about 2 seconds at the start time of the avail. This problem has been resolved. The start time of the avail that is embedded in a MS Smooth sparse track is now correct, and the video no longer freezes. | 
| 2.21.5 | SOCK-36668 | Starting and stopping | There was a fix to intermittent issues with activating the appliance after a software restart, in appliances with a more advanced network configuration. | 
| 2.21.0 | SOCK-35578, SOCK-35097 | Time codes | The new environment variable FORCE\_LTC\_TO\_UTC allows the forcing of LTC time codes to UTC. | 
| 2.21.0 | SOCK-34876 | Time zones | Web callback timestamps were inconsistent for assertions and de-assertions. This is now fixed by adjusting them to local time. | 
| 2.21.3 | SOCK-37133 | Video | When creating a Live event that has a 4K input and an ABR stack output, some of the lower resolution renditions may incorrectly be window-boxed (i.e., black bars on all four sides of the image). This has been fixed. | 

## Resolved issues in Statmux 2.21
<a name="rn-2-21-resolved-statmux"></a>

The following table lists the resolved issues in Statmux 2.21.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 2.21.2 | SOCK-36915 | Logs; Statmux; CL3 | Data that was retained for 90 days could fill up the logs, causing partitions to run out of space. This data is now retained for 30 days to avoid the issue. | 
| 2.21.5 | SC-4271 | Modifying a running MPTS | Previously, modifying a running MPTS in a 1:1 statmux redundancy group didn't reconfigure the secondary MPTS. Now, both MPTS configurations are updated. | 
| 2.21.0 | SOCK-36469 | Statmux | Stopping a Multi Program Transport Stream (MPTS) could cause Statmux to become unresponsive as it continued attempting to run. This is now fixed. | 
| 2.21.0 | SC-4208 | Statmux; CL3 | The maximum video buffer delay for MPTS MPEG2 programs was not set correctly. This caused higher than the 1.8-megabit maximum allowed for SD MP2 video. This is now fixed. | 
| 2.21.0 | SC-4234 | Statmux; CL3 | The following 1:1 redundancy group validations were added in Statmux: Prevent transfers: Prevent transfer from active to backup unless there are three active nodes. This can happen during automatic failover when there are two active nodes and one backup. Prevent transfer from active to backup if there is already a backup node. Prevent transfer from backup to active if there are already two active nodes Prevent additions: Prevent the addition of backup nodes unless there are already two active nodes. Prevent the addition of an active node if there are any MPTS jobs or MPTS enabled channels attached. Prevent removals: Prevent the removal of active nodes from the redundancy group when there are MPTS jobs or MPTS enabled channels attached, or when there is a backup node in the pool. | 
| 2.21.1 | SC-4241 | Statmux; CL3 | Previously, the network could become overloaded by multicast traffic. This is now fixed. Network communication between Elemental Live and Statmux is now improved. You can also now edit multicast addresses and modify address allocation to avoid overload by multicast traffic. | 

## Resolved issues in Conductor Live 3.21
<a name="rn-2-21-resolved-cl3"></a>

The following table lists the resolved issues in Conductor Live 3.21.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 3.21.3 | SC-4279 | Alerts | Many alerts (specifically those with alert codes greater than 5000) did not show in the Statmux web interface or AWS Elemental Conductor Live web interface or the APIs. This has been resolved and these alerts will now appear. | 
| 3.21.2 | SC-4240 | CL3 | Channels that are part of a 1:1 redundancy pair are also paired together in the web interface. When viewing and searching, these channels always appear together. When you delete one, you also delete its pair. This was clear on the CL3 Channels index page and CL3 Channel Bulk action page, but was not clear on the MPTS index page. This is now fixed. | 
| 3.21.2 | SC-4235 | CL3 - MPTS | The Output Listening check box can now be found on the main configuration tab. | 
| 3.21.0 | SC-4245 | CL3 web interface | There was a defect in the web interface that caused profile duplication of SMPTE ST 2022-6 input to fail. This is now fixed. | 
| 3.21.0 | SC-4244 | Inputs - CL3 | Previously, it was not possible to enter parameters for all SMPTE ST 2110 and SMPTE ST 2022-6 input fields. This is now fixed. | 
| 3.21.0 | SOCK-25526 | Inputs; CL3 | The ZeroMQ library is updated to version 4.3.3 to address potential crashes in the web layer. | 
| 3.21.2 | SOCK-36915 | Logs; Statmux; CL3 | Data that was retained for 90 days could fill up the logs, causing partitions to run out of space. This data is now retained for 30 days to avoid the issue. | 
| 3.21.2 | SOCK-36934 | Outputs; CL3 | The monitoring output feed for Elemental Live to Statmux communication erroneously included telemetry data. This is now fixed. | 
| 3.21.0 | SOCK-36385 | Outputs; CL3 | Elemental Live events in Elemental CL3 clusters sometimes failed over to a backup, but came back with events running that could not be stopped by CL3. This caused duplicate events to be published to customer endpoints. This is now fixed. | 
| 3.21.1 | SC-4241 | Statmux; CL3 | Previously, the network could become overloaded by multicast traffic. This is now fixed. Network communication between Elemental Live and Statmux is now improved. You can also now edit multicast addresses and modify address allocation to avoid overload by multicast traffic. | 
| 3.21.0 | SC-4234 | Statmux; CL3 | The following 1:1 redundancy group validations were added in Statmux: Prevent transfers:+ Prevent transfer from active to backup unless there are three active nodes. This can happen during automatic failover when there are two active nodes and one backup.<br />+ Prevent transfer from active to backup if there is already a backup node.<br />+ Prevent transfer from backup to active if there are already two active nodes Prevent additions:<br />+ Prevent the addition of backup nodes unless there are already two active nodes.<br />+ Prevent the addition of an active node if there are any MPTS jobs or MPTS enabled channels attached. Prevent removals:<br />+ Prevent the removal of active nodes from the redundancy group when there are MPTS jobs or MPTS enabled channels attached, or when there is a backup node in the pool. | 
| 3.21.0 | SC-4208 | Statmux; CL3 | The maximum video buffer delay for MPTS MPEG2 programs was not set correctly. This caused higher than the 1.8-megabit maximum allowed for SD MP2 video. This is now fixed. | 
| 3.21.5 | SC-4290 | Web interface | Previously, when you pasted a URL on a screen where channel filters are set, the paste action would clear the filters. Pasting no longer clears the filters. | 