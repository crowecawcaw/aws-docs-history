

# Resolved issues in version 2.23 and 3.23
<a name="rn-2-23-resolved"></a>

The **Version** column shows the point release that the issue applies to.

## Resolved issues in Elemental Live 2.23
<a name="rn-2-23-resolved-live"></a>

The following table lists the resolved issues in Elemental Live 2.23.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 2.23.0 | SOCK-37998 | Alerts and messages | Previously, the warning about mismatched events in dual socket performance mode was included in the log file, even when the mode was not enabled. This issue has been fixed. | 
| 2.23.1 | SOCK-37868 | Alerts and messages | Alerts have been added to help detect when the Live time is not synchronized with the NTP server. | 
| 2.23.2 | SOCK-37868 | Alerts and messages | There is now an alert when the time on the Live node isn't synched with the NTP server. | 
| 2.23.5 | SOCK-38587 | Alerts and messages | Previously, an issue with the frame drop alert in certain events caused a large number of error log lines to be recorded in the live\_runner.output log file. This has been resolved. | 
| 2.23.3 | SOCK-38313 | Alerts, logs, messages | Fixed an issue where the Download Log Files button was not working. | 
| 2.23.3 | SOCK-38241 | Alerts, logs, messages | Previously, there was a problem with the system clock alert not disappearing after 15 minutes of occurrence. This issue has been fixed. | 
| 2.23.0 | SOCK-37882 | Audio | Previously, there were problems with audio and video synch issues in SMPTE 2110 outputs. Elemental Live 2110 outputs now implement AES67, which resolves the problems. | 
| 2.23.1 | SOCK-38099 | Audio | Fixed a problem where bad audio sometimes occurred in the output after an input switch. | 
| 2.23.1 | SOCK-38061 | Audio | There was a problem whereby Live was incorrectly inserting a discontinuity indicator for audio. This indicator caused issues for the playback system. The problem has been fixed so that the indicator is no longer inserted. | 
| 2.23.0 | SOCK-37880 | Captions | Resolved an issue where a DVB-Sub caption spread over several PES packets can cause our decoder to mistakenly insert a premature "clear screen" caption operation. | 
| 2.23.0 | SOCK-37137 | Captions | There was an issue with 608 input captions that used channels 3 and 4 in addition to channels 1 and 2. Previously, when the captions were converted to WebVTT, lines might be truncated. This problem has been fixed. | 
| 2.23.1 | SOCK-37756 | Configuration | The SSLH listening agent has been removed from Live. As a result of this change, RTMPS input is now supported only on port 1935. | 
| 2.23.1 | SOCK-38012 | Configuration, PTP and chronyd | Previously, there was a problem with the timing daemons. If you enabled PTP and then reinstalled or upgraded Live, chronyd was re-enabled. Now, the chronyd daemon is not re-enabled. | 
| 2.23.5 | SOCK-37327 | DRM | Previously, events that used DRM could cause an enormous increase in memory usage. This problem has been fixed. | 
| 2.23.5 | SOCK-38440 | Event crash | Resolved an issue that led to a seg fault. | 
| 2.23.3 | SOCK-37977 | Event failure | Previously, there was an issue with running an event that include GPU encode information, on a Live node that was CPU-only. This problem has been fixed. | 
| 2.23.3 | SOCK-38110 | Firewall | There was a problem where Elemental Live could stop receiving multicast traffic when the firewall is enabled. This problem has been fixed. | 
| 2.23.4 | SOCK-38272 | Input switching | There was an issue with creating a Live event via the REST API. If the event has multiple inputs and the inputs do not have labels/names it was not possible to switch between inputs, either via the web interface or via the REST API. This has been fixed. | 
| 2.23.5 | SOCK-38530 | Inputs | Previously, if there was a problem ingesting a source, ingest of other similar sources might stop. This problem has been fixed. We also added a message when a timeout occurred in stopping a thread. | 
| 2.23.5 | SOCK-37516 | Inputs | Fixed a scenario when if there are inputs with differing base frame rates (i.e. 25 vs 30) then one of them may fail. | 
| 2.23.3 | SOCK-37346 | Inputs, removing | Fixed issue when removing inputs timed to occur in the future. When the operator removed the inputs, Live might crash during an input switch. | 
| 2.23.0 | SOCK-37782 | Inputs, RTMP | Fixed a memory leak on RTMP inputs. | 
| 2.23.2 | SOCK-38053 | Inputs, RTMP | Previously, for RTMP Pull inputs, Live would remove query parameters from the URL. This could cause issues if, for example, the query presented user credentials to the RTMP server. Now, query parameters are preserved. But note that Live doesn't read the query and will not act on the instructions in the query. | 
| 2.23.2 | SOCK-37831 | Inputs, RTMP | Previously, events with RTMP inputs could crash (stop) abruptly. We have fixed the memory handling issue that caused this crash. | 
| 2.23.0 | SOCK-37891 | Inputs, RTSP | For RTSP inputs, fixed the Interface field on the web interface to correctly set the network interface. | 
| 2.23.1 | SOCK-38088 | Inputs, SDI | Fixed a problem where Live stopped ingesting SDI input if the user stopped and restarted the event. | 
| 2.23.5 | SOCK-38550 | Inputs, SDI | Previously, there was a problem when an SDI input port didn't have a cable attached. The ingest.log could fill up with junk messages, leading to disk fill up. This issue has been fixed. | 
| 2.23.0 | SOCK-37886 | Inputs, SDI and SMPTE 2110 | Fixed a problem where debug buffers were consuming extra memory for SDI and SMPTE 2110 inputs. | 
| 2.23.0 | SOCK-37742 | Inputs, SMPTE 2110 | SMPTE 2110 NMOS inputs were updated so that when an event is restarted, it will re-register the input with a registration server. | 
| 2.23.0 | SOCK-37739 | Inputs, SMPTE 2110 | Added an error message if the input name is blank when setting up NMOS static receivers. | 
| 2.23.0 | SOCK-37736 | Inputs, SMPTE 2110 | Previously, there was a problem with static receivers (for SMPTE 2110 inputs with NMOS). The steps for creating two events with different receiver IDs was complicated. This problem has been fixed. Now, if you want two events to have the same receiver IDs, give event B the same input name as event A. Do this any way you want: by duplicating A, by creating B from scratch, by creating B from scratch and then modifying. If you want the events to have different receiver IDs, give both events different input names. | 
| 2.23.4 | SOCK-38388 | Live crash | We have fixed an error that occurs in a specific scenario. The error causes a crash with the error message "EME has a media error ..." The crash no longer occurs in the identified scenario. | 
| 2.23.4 | SOCK-38214 | Live crash | Fixed a situation where appliance was crashing due to "scaler position rectangle is outside output frame" error. | 
| 2.23.3 | SOCK-37776 | Mellanox card | In rare cases, events outputting through 25 GbE interfaces could have black frames. This problem has been fixed. | 
| 2.23.4 | SOCK-38229 | Output handling | There was an issue with the events that had both remote and non-remote output groups. A problem with the handling of the low video buffer delay interrupted the output to the muxer. This problem has been fixed. | 
| 2.23.3 | SOCK-38179 | Output locking | There was a problem where output locking between two Live appliances stopped synchronizing the outputs after certain SCTE 35 availability events, in particular a chapter start. This problem has been fixed. | 
| 2.23.0 | SOCK-37853 | Outputs, ancillary data | Previously, there was a bug that caused line numbers of ancillary data to be incorrect if they were greater than 256. There was also a bug that caused the line placement of the data to not be consistent with frames, in interlaced output. Both of these issues have been fixed. | 
| 2.23.0 | SOCK-37881 | Outputs, DASH | Fixed an issue for DASH MPD when output audio is Dolby Digital Plus with Atmos. Now, the required fields in the MPD (EC3\_ExtensionType and EC3\_ExtensionComplexityIndex) are correctly inserted. | 
| 2.23.3 | SOCK-37611 | Outputs, dropped frames | Live has optimized Mellanox workflows and improved 2022-7 buffer ability to recover from streams that don't comply with the specification. These changes have significantly improved density for 2022-6 to 2110 workflows. | 
| 2.23.3 | SOCK-38075 | Outputs, Reliable TS with SRT | Previously, there could be a problem with SRT Reliable TS outputs when the SRT server is geographically distant from the AWS Region when the AWS MediaConnect flow exists. This problem has been resolved. | 
| 2.23.0 | SOCK-37662 | Outputs, RTMP | Fixed a problem that sometimes caused an event to crash when it included an RTMP output. | 
| 2.23.0 | SOCK-37872 | Outputs, RTP | Previously, with RTP outputs, the SMPTE 2110-40 ancillary data messages within the RTP packet were not inserted in raster order. This problem has been fixed. | 
| 2.23.2 | SOCK-37674 | Outputs, RTP | Previously, the "Number of TS packets per IP packet" configuration did not accurately apply to RTP outputs. The configuration was only implemented for UDP/TS outputs, even though both output types existed in the same output group. Now, this configuration has been implemented for RTP outputs. | 
| 2.23.5 | SOCK-38559 | Outputs, SMPTE 2110 | When running an Elemental Live event with SMPTE 2110 output and a SMPTE 2110-40 ancillary stream, Live was not correctly ordering the ancillary packets within a single SMPTE 2110-40 RTP packet if the packets had the same line number. This behavior is not compliant per the specification. This has been fixed. | 
| 2.23.5 | SOCK-38524 | Outputs, SMPTE 2110 | When running an event that is configured to use the input clock as the output timing source with SMPTE 2110 output, the output streams may slowly drift behind real time. This problem has been fixed. We also recommend against using the input clock as the output timing source for SMPTE 2110 outputs. Instead, use the system clock. | 
| 2.23.5 | SOCK-38415 | Outputs, SMPTE 2110 | There was a problem running an event with SMPTE 2110 output that had audio streams using 125 microsecond packets. When this event ran for more than 48 hours, the audio stream drifted behind the video. | 
| 2.23.5 | SOCK-38332 | Outputs, SMPTE 2110 | Previously, if you changed the PTP when a SMPTE 2110 output is running, the event could crash. You shouldn't change the PTP while an event is running. | 
| 2.23.0 | SOCK-37884 | Outputs, SRT | This release fixes a problem (previously reported as a known issue) where, in an SRT output with a primary and a secondary destination, the output slows when one of the destinations goes offline. | 
| 2.23.4 | SOCK-38319 | Platform | There was a known issue where we fail to install latest Broadcom TG3 driver on RedHat and CentOS systems. This has been fixed. | 
| 2.23.2 | SOCK-37791 | REST API | Previously, a REST API call to time\_signal would not return the number of frames. The number of frames has now been added to the response. | 
| 2.23.2 | SOCK-37772 | REST API | Previously, a REST API call to adjust\_audio\_gain didn't return information about either the success or failure of the call. Now, the call returns the new value or an appropriate failure message. | 
| 2.23.1 | SOCK-37979 | SMPTE 2110 and NMOS | Previously, after a Live software upgrade, it wasn't possible to restart events that included NMOS. This problem has been fixed; it is possible to restart the events. | 
| 2.23.2 | SOCK-38103 | Time clock configuration | Previously, the installer would not disable and stop chronyd, if ptp4l was enabled. This could lead to conflicts. Now, if the installer detects that ptp4l is enabled, the installer will disable and stop chronyd. | 
| 2.23.0 | SOCK-37828 | Video | Fixed a scenario where non-valid framerate could cause the event to fail. | 
| 2.23.4 | SOCK-38425 | Video codecs: FFMPEG | Elemental Live no longer installs the FFmpeg tool used for some earlier generation codecs. The codecs are still supported, but Live uses a different tool. If you still want to use FFmpeg, search the knowledge articles in the [AWS Elemental Support Center](https://console.aws.amazon.com/elemental-appliances-software/home?region=us-east-1#/supportcenter) for Advisory: AWS Elemental Live 2.23.4 no longer enables FFmpeg by default. | 
| 2.23.2 | SOCK-37160 | Video, color space | There was an issue with Live's ability to recognize the color space in a SMPTE 2110 input. The issue caused corrupted colors. This issue has been fixed. | 
| 2.23.4 | SOCK-38412 | Virtual input switching | There was a problem with virtual input switching in an event with that has many inputs with SCTE-35 messages. This high volume of messages could cause a loss of metadata in the output. | 
| 2.23.4 | SOCK-38227 | Virtual input switching | There was an issue with the virtual input switching feature that occasionally caused the event to crash. This issue has been fixed. | 
| 2.23.4 | SOCK-38373 | XML content | The XML for a Live event now includes the channel name. This data helps match up a channel in the Live XML to the corresponding channel in the Conductor Live XML. | 

## Resolved issues in Statmux 2.23
<a name="rn-2-23-resolved-statmux"></a>

The following table lists the resolved issues in Statmux 2.23.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 2.23.1 | SC-4334 | Virtual sources | Previously, the virtual source field in an MPTS (Statmux) output was ignored. This issue has been fixed. | 

## Resolved issues in Conductor Live 3.23
<a name="rn-2-23-resolved-cl3"></a>

The following table lists the resolved issues in Conductor Live 3.23.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 2.23.0 | SC-4321 | Crash | Previously, there was a problem starting an MPTS after upgrading to version 2.22.4. This problem has been fixed. | 
| 3.23.1 | SC-4266 | High availability and failover | Previously, there was a data loss problem when network connectivity failed in a high availability Conductor Live cluster. During the failure, the secondary Conductor node took control, then the primary regained control. Changes made while the secondary Conductor was in control were lost. This problem has been fixed; data loss no longer occurs. | 
| 3.23.5 | SC-4366 | SDI routers | Previously, there was an issue selecting Interleave 4K/2SI as a valid SDI router output in Conductor. This has been resolved. | 
| 3.23.4 | SC-4353 | SNMP | Previously, there was an issue with the enumeration of Conductor Live channels and Live events using SNMP. The enumeration might begin at the incorrect channel or event ID, and might return partial results. This problem has been fixed. An additional issue that prevented the use of the snmptable command has also been resolved. | 
| 3.23.4 | SOCK-38373 | XML content | The XML for a Live event now includes the channel name. This data helps match up a channel in the Live XML to the corresponding channel in the Conductor Live XML. | 