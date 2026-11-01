

# Resolved issues in version 2.25 and 3.25
<a name="rn-2-25-resolved"></a>

The **Version** column shows the point release that the issue applies to.

## Resolved issues in Elemental Live 2.25
<a name="rn-2-25-resolved-live"></a>

The following table lists the resolved issues in Elemental Live 2.25.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 2.25.9 | GLV-829 | Captions | Fixed an issue whereby captions weren't included in the output in an event with hot backup inputs. | 
| 2.25.9 | GLV-3723 | Captions, output | There was an issue with the rollover number for CEA-708 embedded captions carried in an ancillary stream in an output. Previously, when the caption distribution packet sequence number rolled over it is incorrectly the rollover number as a duplicate caption packet and is discarded. This issue has been fixed. | 
| 2.25.9 | GLV-3961 | Environment variable | Change to the environment variable HLS\_VOD\_MODE\_DURATION\_BEFORE\_ALERT\_IN\_MSEC. This environment variable was previously limited to the maximum size of an int32. This restriction caused an alert to trigger earlier than expected. This environment variable has been revised to support longer durations. | 
| 2.25.9 | GLV-3388 | Inputs, SMPTE 2110 | There was an issue when a Live event is configured to use a SMPTE 2110 input with SMPTE 2022-7 and embedded timecodes. If one of the ancillary streams (either primary or secondary) that carries the timecode ancillary packets drops, the event might fail to resync timecodes. This issue has been fixed. | 
| 2.25.9 | GLV-2540 | Web interface | There was an issue with the MPTS Perform tab. It was possibly to press a combination of keys and buttons that makes a different tab appear. | 
| 2.25.8 | SOCK-38878 | Audio output | Fixed an issue where the initial audio gain was not being set correctly on event start. | 
| 2.25.8 | GLV-2800 | Inputs, SMPTE 2110 | When running a Live event with a SMPTE 2110 input with an ancillary stream containing timecodes, in some instances the timecodes were being incorrectly parsed. This has been fixed. | 
| 2.25.8 | GLV-2614 | Inputs, SMPTE 2110 | When an Elemental Live event with SMPTE 2110 input had JPEG XS video, Live was incorrectly rejecting a valid JPEG XS license. This has been fixed. | 
| 2.25.8 | GLV-2510 | SCTE 35 | We have added an environment variable, REPEAT\_AVAIL\_IN\_NEST, that toggles to determine whether or not previously reported avails are repeated when a nested avail occurs. | 
| 2.25.7 | GLV-1751 | Nielsen watermarking | Fixed an issue whereby Nielsen watermarking didn't work with AC3 inputs. | 
| 2.25.7 | GLV-1464 | SMPTE 2038 passthrough | Previously, there was an issue with passing through SMPTE 2038 data when the input was a network input. Even if the SMPTE 2038 passthrough checkbox was checked (on a TS output), the output didn't actually include SMPTE 2038. This issue has now been fixed. | 
| 2.25.7 | SOCK-38666 | Web interface | Previously, the banner to display the web interface included a message to enter a URL. This message now includes the IP address of the appliance. | 
| 2.25.6 | GLV-1624 | Output locking | There was an issue where an event could get stuck while trying to resync in an event set up for output locking. This issue has been fixed. | 
| 2.25.6 | GLV-1708 | Outputs, HLS manifest | There was an issue with the contents of the manifest in HLS outputs. If you were implementing, redundant manifests, the CHANNELS attribute was missing from the manifest. This issue has been fixed. | 
| 2.25.6 | GLV-673 | SCTE 35 | There was an issue with handling SCTE 35 PIDs in an input that contains a TS. If the SCTE 35 PID wasn't present when the event started but appeared in the input later, Elemental Live would ignore it. | 
| 2.25.6 | GLV-1785 | Video outputs | There was an issue with video artifacts appearing when the scene transitioned from the field to a white bright logo. This issue has been fixed. | 
| 2.25.5 | GLV-1345 | REST API | Previously, the api/live\_events/:id/bulk\_metadata REST endpoint didn't perform the bulk metadata correctly. This issue has been fixed. | 
| 2.25.5 | GLV-1222 | Inputs, SDI | There was an issue with the processing of ancillary data streams from an SDI source. All the data wasn't being successfully processed. This issue has been fixed. | 
| 2.25.5 | GLV-1125 | Outputs, UDP | There was an issue with handling Teletext captions from an SDI source. This issue has been fixed. | 
| 2.25.5 | GLV-1111 | Unsolicited ESAM | There was an issue with accessing unsolicited\_esam endpoints using the REST API. You must enable API authentication to use these endpoints. To enable authentication, see "Enable user authentication" in the AWS Elemental Live Configuration Guide. For more information, see the section "Authentication and REST" in the Elemental Live API and User Guide. | 
| 2.25.5 | GLV-851 | Video, HEVC source | Previously, an HEVC video source didn't produce an output in the correct aspect ratio. The problem occurred in a video source with the SAR set to anything other than 1:1 and the PAR was absent. The issue has been fixed, and the output now has a suitable aspect ratio. | 
| 2.25.5 | GLV-796 | Captions | Very rarely, 608 captions in the source were dropped in the output. This issue has been fixed. | 
| 2.25.5 | GLV-791 | Audio only outputs | There was a problem with the handling of an audio-only HLS output. Elemental Live sometimes inserted a zero-duration audio-only segment into the manifest. This could cause problems for the downstream systems. Elemental Live no longer inserts zero-duration segments for audio-only outputs. | 
| 2.25.5 | GLV-707 | Outputs, SMPTE 2110 | There is an error in the Elemental Live User Guide, in the General Procedure to set up a SMPTE 2110 output. Step 1 says "Open the section and choose Low Framerate Input." It should say: "Open the section and choose Low Latency Mode." The Elemental Live User Guide will eventually be fixed. | 
| 2.25.5 | GLV-259 | Audio, AAC format | Elemental Live recently adopted new content for the DVB AAC descriptor in the PMT of a TS output. The new descriptor is compliant with EN 300 468 V1.16.1 standard for SI data from DVB. We have now made a further change to provide better support for a wider range of TS analyzers. | 
| 2.25.5 | GLV-160 | Input switching | There is a change to the way that Elemental Live handles input switches. If the active input ends but there is an input switch scheduled within the next 2 seconds, Live won't switch to the failover input. Instead, Live will insert fill frames until the scheduled input switch is due. | 
| 2.25.4 | GLV-403 | Audio, input | An improvement was made that will improve resiliency when different incoming audio tracks aren't formatted consistently. | 
| 2.25.4 | GLV-168 | Captions, output | There was an issue whereby the styling (such as a font color) that applies to TTML captions sometimes appeared in other content in the output. This issue has been fixed. | 
| 2.25.4 | GLV-132 | Crash | Fixed an issue where starting and stopping RTMP caused Elemental Live to crash. | 
| 2.25.4 | GLV-154 | Log files | There was an issue that was causing the log files to have many repetitions of a log message. In this case, the message occurred when the Content-Length header was not set in an HTTP response. The message now repeats a maximum of three time. | 
| 2.25.4 | GLV-137 | MPTS (Statmux) | An improvement has been made to the MPTS demuxer to address customer concerns. The MPTS demuxer previously generated audio stream buffers for all incoming streams received from incoming MPTS. When handling MPTS inputs featuring many programs, this caused unnecessary performance strain. There have been issues in the PMT that should only impact unused streams. In response, we've updated the MPTS demuxer:+ If PID-specific audio selectors are included, the demuxer skips buffer creation for unused audio streams. This handling results in improved system performance and resilience to bad input PMTs.<br />+ If no such selectors are included, the demuxer won't apply any filter to incoming audio streams. Instead, the legacy handling applies. | 
| 2.25.4 | GLV-264 | MPTS (Statmux) | Elemental Live now supports the ability to specify the TSID in the NIT for Statmux MPTS output. Elemental Live also now supports the ability for the user to specify the Original Network ID in the NIT for Statmux MPTS output, and to include that ID in the output. | 
| 2.25.4 | GLV-482 | Output locking | Fixed an issue that could very occasionally result in segmentation drifts in the outputs. | 
| 2.25.4 | SOCK-38874 | SCTE 35 | There was an issue whereby captions might appear in the output when ad avail blanking was applied. This issue has been fixed. | 
| 2.25.3 | GLV-258 | Audio outputs | Elemental Live recently added support in the PMT for the "MPEG-4 AAC descriptor" type of AAC descriptor (in line with tables 2-71 and 2-72 of ISO/IEC 13818-1 2015). As it happens, the addition of this new descriptor revealed a feature of Safari and QuickTime behavior, which is that they don't support PMTs that span more than one TS packet. In order not to break existing workflows, Elemental 2.25.3 resolves this problem by applying special logic to the "MPEG-4 AAC descriptor":+ Live will add the "MPEG-4 AAC descriptor", if doing so wouldn't cause a split in the PMT.<br />+ If the addition would cause a split, Live won't add "MPEG-4 AAC descriptor" but it will add other types of AAC descriptors (the descriptors that Elemental Live has traditionally supported). This conditional behavior applies only to AAC audio descriptors, not to audio descriptors for other audio formats. Also note that the special logic doesn't apply to TS or archive outputs, because Safari and QuickTime are typically not involved in those types of workflows. | 
| 2.25.3 | GLV-237 | Deployment, node recruitment | There was an issue with node recruitment in a Conductor cluster. For information about the issue and the fix, see the revised information about changes to cluster management in [Change to cluster management 3.25.3](rn-2-25-essential.md#rn-2-25-essential-cluster-management). | 
| 2.25.3 | GLV-196 | Logging and messages | Updated Elemental Log Collector (ELC) to add support for customers using RHEL and fixed some minor bugs. | 
| 2.25.3 | GLV-540 | Multiplex and Statmux outputs | Performance and jitter with multiplex and statmux workflows have been improved. | 
| 2.25.3 | GLV-265 | Multiplex and Statmux outputs | Previously, the transport\_stream\_id for statmux/multiplex output MPTS wasn't set in the SDT info. Now, the TSID will be included in the output SDT info and will be updated as needed. | 
| 2.25.3 | GLV-263 | Multiplex and Statmux outputs | Previously, the TDT time info for statmux/multiplex MPTS output was not being initialized to the current time, making TDT dates/times wrong. Now, the TDT time info will be accurate in the output MPTS. | 
| 2.25.3 | GLV-458 | Output locking | Fixed a scenario where resyncs could trigger segmentation drift. | 
| 2.25.3 | GLV-384 | RTMP inputs | Previously, RTMP pull inputs were not responding quickly enough to input switches away from the RTMP input to a different input. The slow response caused fill frames to get generated even if the next input was prepared and ready to activate. That issue has been resolved, and fill is no longer generated. | 
| 2.25.3 | GLV-81 | SDI inputs | Fixed issue with Elemental Live not detecting embedded timecode of SD/625i SDI inputs. | 
| 2.25.2 | GLV-178 | Audio input | There was an issue if an event includes an audio track selector, but there is no incoming audio on that track when the event starts. Previously, Elemental Live failed to detect the audio if it appears later. This issue has been fixed. | 
| 2.25.2 | SOCK-21662 | Audio output | Previously, the AAC descriptor was missing from the PMT in TS outputs. The descriptor is now present. | 
| 2.25.2 | GLV-67 | Captions | There was an issue when Teletext captions were converted to Web VTT. The issue resulted in colored text having a black background. This issue has been fixed. | 
| 2.25.2 | GLV-59 | Input cropping | There was an issue with input cropping. Elemental Live sometimes failed to crop the video on all video renditions in an ABR stack. This issue has been fixed. | 
| 2.25.2 | GLV-56 | Output locking | A memory usage problem was fixed when two encoders were output locked. | 
| 2.25.2 | SOCK-39174 | SCTE 35 | There was an issue with converting SCTE 104 messages to SCTE 35. Elemental Live didn't always handle the Auto Return correctly during the conversion. As a result, the ad avail in the event output didn't always return correctly. This issue has been fixed. | 
| 2.25.2 | SOCK-39075 | Static image | Previously, Elemental Live ignored the position for the static image in the output. This position is set by the Left and Top fields in the Image Inserter in the Global Processor section of the event. This issue is now fixed and Elemental Live positions the image correctly. | 
| 2.25.2 | GLV-40 | Video color space | There was an issue with the color space when the input was HDR with a chroma subsampling of 4:2:2, and the output was 4:2:0. The issue exhibited as a small amount of red bleeding at the edges of lines. This issue has been fixed. | 
| 2.25.2 | SOCK-39331 | Web interface | There was a problem with the web interface in Elemental Live 2.25.1. The web interface couldn't display event details. This problem has been fixed. | 
| 2.25.1 | SOCK-39291 | Outputs, epoch locking | There was a problem where an event with epoch locking enabled could produce an invalid HLS manifest. The two outputs weren't correctly epoch locked, and one of the segments had an incorrect duration. This problem has been resolved. | 
| 2.25.1 | SOCK-38580 | SCTE 35 | Previously, when a SCTE 104 message included multiple nested SCTE 35 messages, Live parsed and ingested only the first message. This issue has been fixed. Live now ingests all the nested SCTE 35 messages. | 
| 2.25.1 | SOCK-39250 | Time | The timezone component of Elemental Live has been updated to the newest version using the IANA Timezone database version 2023c. | 
| 2.25.0 | SOCK-38903 | Alerts and messages | Previously there was no alert when a SMPTE 2110 redundant input pair was missing a source. There is now an alert: 5318 Redundant input pair is not receiving data from source: <identification of the source>. | 
| 2.25.0 | SOCK-38892 | Alerts and messages | Previously there was no alert when a 2022-6 input was missing a source. There is now an alert: 5318 Redundant input pair is not receiving data from source: <identification of the source>. | 
| 2.25.0 | SOCK-39076 | Output, Zixi | There was an issue that could cause instability in delivering a Zixi output. The output would continually fail and restart. The root cause that prevented a successful connection has been resolved. | 
| 2.25.0 | SOCK-38860 | Outputs, Zixi or SRT | There was a latency issue in a Reliable TS output that uses Zixi or SRT. The latency is made up of the value in the Zixi Latency or SRT Latency field and an internal buffer (hard-coded to 1000ms) that is used to smooth out the stream. The combined values could result in too much overall latency. The buffer latency is now in a field that you can set. This Buffer Msec field appears on the web interface in the Output section, above the Zixi Latency or SRT Latency field. | 
| 2.25.0 | SOCK-39053 | Video | There was sometimes an issue with corrupted color when ingesting SDI source video. This issue has been resolved. | 

## Resolved issues in Statmux 2.25
<a name="rn-2-25-resolved-statmux"></a>

The following table lists the resolved issues in Statmux 2.25.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 2.25.8 | GLV-2243 | Audio only passthrough | Fixed an issue where certain configurations of Statmux could lead to MPTS Overflow alerts. | 
| 2.25.4 | GLV-264 | NIT | Elemental Live now supports the ability to specify the TSID in the NIT for Statmux MPTS output. Elemental Live also now supports the ability for the user to specify the Original Network ID in the NIT for Statmux MPTS output, and to include that ID in the output. | 
| 2.25.4 | GLV-137 | Demuxer | An improvement has been made to the MPTS demuxer to address customer concerns. The MPTS demuxer previously generated audio stream buffers for all incoming streams received from incoming MPTS. When handling MPTS inputs featuring many programs, this caused unnecessary performance strain. There have been issues in the PMT that should only impact unused streams. In response, we've updated the MPTS demuxer:+ If PID-specific audio selectors are included, the demuxer skips buffer creation for unused audio streams. This handling results in improved system performance and resilience to bad input PMTs.<br />+ If no such selectors are included, the demuxer won't apply any filter to incoming audio streams. Instead, the legacy handling applies. | 
| 2.25.3 | GLV-237 | Deployment, node recruitment | There was an issue with node recruitment in a Conductor cluster. For information about the issue and the fix, see the revised information about changes to cluster management in [Change to cluster management 3.25.3](rn-2-25-essential.md#rn-2-25-essential-cluster-management). | 

## Resolved issues in Conductor Live 3.25
<a name="rn-2-25-resolved-cl3"></a>

The following table lists the resolved issues in Conductor Live 3.25.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 3.25.9 | GLV-3093 | Conductor Creating Multiple Jobs in Encoder For The Same Channel ID | Previously, there was an issue whereby issuing multiple Channel Start API commands on Conductor Live could produce multiple events on the Live appliance. The problem was that with so many events starting at once, Conductor Live would assume some start requests had failed, so Conductor Live would submit a new request. But in fact, both the original request and the new request would succeed, resulting in duplicate events. This issue has been fixed. | 
| 3.25.3 | GLV-237 | Deployment, node recruitment | There was an issue with node recruitment in a Conductor cluster. For information about the issue and the fix, see the revised information about changes to cluster management in [Change to cluster management 3.25.3](rn-2-25-essential.md#rn-2-25-essential-cluster-management). | 
| 3.25.5 | GLV-1104 | Logging | There was a problem that caused the PSQL log to fill up with repetitive messages. It also sometimes failed to synchronize the databases correctly during an HA failover. Both of these problems have been fixed. | 
| 3.25.7 | GLV-1859 | User authentication | There was a problem when https and auth were configured. The first login attempt with correct password fails every time. Then the wrong password worked on next attempt. This issue has been fixed. | 
| 3.25.8 | SC-4339 | Web interface | Fixed an issue where CL3 was not showing the correct Job Duration once it exceeded one month. | 