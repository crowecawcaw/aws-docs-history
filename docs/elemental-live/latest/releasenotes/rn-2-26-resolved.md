

# Resolved issues in version 2.26 and 3.26
<a name="rn-2-26-resolved"></a>

The **Version** column shows the point release that the issue applies to.

## Resolved issues in Elemental Live 2.26
<a name="rn-2-26-resolved-live"></a>

The following table lists the resolved issues in Elemental Live 2.26.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 2.26.5 | GLV-1647 | Audio inputs, Dolby Digital | There was an issue with events configured to pass through Dolby Digital audio. If the event was also configured to perform automatic input failover if audio silence was detected, then the 5101 (silence exceeded) alert appeared for the secondary input. This alert should not appear in this scenario. This issue has been fixed. | 
| 2.26.5 | GLV-1954 | Caption outputs | There was an issue with source Teletext (OP-47) captions that are wrapped in SMPTE 2031 in SDI inputs. Sometimes extra data was passed through, which resulted in garbage text in the output captions. This issue has been fixed. | 
| 2.26.5 | GLV-131 | Caption outputs | There was an issue with events configured to pass through SCTE-27 or DVBSub captions. If a PID was selected in the caption selector, then only the selected PID would be present in the output, other caption PIDs were removed. This issue has been fixed so that Live ignores the caption selector, and passes through all the captions that are in the source. | 
| 2.26.5 | GLV-4401 | Input switching | Fixed an extremely rare edge case where input switching might fail. | 
| 2.26.5 | GLV-3668 | Input switching | There was an issue on Elemental L88x and L98x appliances. Input switching might cause a memory leak. This issue has been fixed. | 
| 2.26.5 | GLV-4574 | Installing | Sometimes the Elemental installer would run out of disk space. This issue has been fixed. | 
| 2.26.5 | GLV-4477 | Installing | The RHEL 9 installed on the appliances now includes packages that better support policy-based routing rules. | 
| 2.26.5 | GLV-4499 | Logs | The amount of data about ad avails in the Elemental logs has been reduced, making it easier to scan the logs for the pertinent information. | 
| 2.26.5 | GLV-3446 | Logs | There were duplicate SCTE 35 messages and ad avail messages in the logs. The duplicates no longer appear. | 
| 2.26.5 | GLV-2248 | Logs | The SCTE-35 logging for M2TS ingest now shows the identifier for the input where the SCTE-35 message came in. | 
| 2.26.5 | GLV-4133 | Motion graphic overlay | Previously, motion graphic overlays might disappear after an input switch. This issue has been fixed. | 
| 2.26.5 | GLV-3024 | Motion graphic overlay | There was an issue with events configured with motion graphic overlays. If the event included many input switches, the audio and video might become unsynchronized. This issue has been fixed. | 
| 2.26.5 | GLV-4642 | NMOS configuration | Previously, NMOS failed to start when bonded interfaces were present. NMOS now works with bonded interfaces. | 
| 2.26.5 | GLV-4640 | NMOS configuration | NMOS had issues with custom CA certificates. NMOS now works with custom CA certificates. | 
| 2.26.5 | GLV-4599 | NMOS configuration | Previously, NMOS required the name of the Elemental Live appliance to resolve to localhost. This issue has been fixed. | 
| 2.26.5 | GLV-4597 | SCTE 35 | Some SCTE 35 Segmentation Event types were not correctly honoring cancellation indicators in time signals. This issue has been fixed. The types are: Break Start, Provider Advertisement Start, Distributor Advertisement Start, Provider Placement Opportunity Start, Distributor Placement Opportunity Start. | 
| 2.26.5 | GLV-4612 | SMPTE 2110 inputs | Previously, on each input switch away from an NMOS-controlled 2110 source, the event crashed. This issue has been fixed. | 
| 2.26.5 | GLV-3434 | SMPTE 2110 inputs | There was an issue with Live events that use SMPTE 2110 input with static SDP files. The web server that provides the SDP file might respond with a non-200 HTTP status. When Live attempted to fetch the SDP file, the event and any similar events would crash. This has been fixed. | 
| 2.26.5 | GLV-4134 | SMPTE 2110 outputs | There was an issue with events configured with motion graphic overlays and SMPTE 2110 outputs. An input switch would cause discontinuities on the SMPTE 2110 outputs. This issue has been fixed. | 
| 2.26.5 | GLV-4595 | Web interface | On the Devices Settings page, an orange backgrounds appeared on some saved fields. This background no longer appears. | 
| 2.26.4 | GLV-1826 | Alerts | The output listening alert no longer clears after 30 seconds. The alert clears only when the issue gets resolved. | 
| 2.26.4 | GLV-4145 | API | The XML format of the devices API (GET /devices.xml) was changed by mistake in Elemental Live 2.26.3. The unintentional changes have been reverted. Starting with Elemental Live 2.26.3, we have also made an intentional change to the API:+ SMPTE 2110 receiver groups have been added to the XML.<br />+ Empty elements have the nil='true' attribute | 
| 2.26.4 | GLV-4143 | API | Previously, the system\_status.json API returned an error when SDI devices were present on the system. This error no longer gets returned. | 
| 2.26.4 | GLV-2372 | Audio, Dolby Atmos | Dolby Atmos encoding now uses the latest library. | 
| 2.26.4 | GLV-1156 | Captions, TTML | Previously, with TTML output captions, a slow memory leak could occur. This problem has been fixed. | 
| 2.26.4 | GLV-3961 | Environment variable | Change to the environment variable HLS\_VOD\_MODE\_DURATION\_BEFORE\_ALERT\_IN\_MSEC. This environment variable was previously limited to the maximum size of an int32. This restriction caused an alert to trigger earlier than expected. This environment variable has been revised to support longer durations. | 
| 2.26.4 | GLV-4233 | Input switching | Previously, with some file-based input switches, the channel would stop emitting output. The only workaround was to restart. This problem has been fixed. | 
| 2.26.4 | GLV-4035 | Input switching | Fixed a scenario where input switches could sometimes fail. | 
| 2.26.4 | GLV-3562 | Input switching | Previously, an event might crash if the event was configured for virtual input switching or perpetually-prepared inputs, and an input switch occurred. This problem has been fixed. | 
| 2.26.4 | GLV-3959 | Inputs | Fixed a performance regression on 2022-6/2022-7 inputs. | 
| 2.26.4 | GLV-3914 | Motion graphics | Fixed an issue whereby motion graphics insertion sometimes fell behind for demanding inputs (for example 4K at 60fps). | 
| 2.26.4 | GLV-3541 | NMOS | Previously, if user authentication was enabled on a node, NMOS wouldn't work. This problem has been fixed. | 
| 2.26.4 | GLV-241 | Outputs, Zixi | Fixed Zixi stream validation to allow primary and secondary streams to allow same destination IP address and port w/ unique stream ids. You can set up the two streams in one of these ways:+ With the same IP address and port, but different interfaces.<br />+ With different IP addresses, port, and interfaces | 
| 2.26.4 | GLV-3915 | SCTE 35 | Fixed an issue that prevented users from creating events with RTMP ad markers. | 
| 2.26.4 | GLV-3120 | Video quality | We have made improvements of approximately 5% to the video quality of speed 0 HEVC. At the same time, compute speed either remains unchanged or is actually faster. | 
| 2.26.3 | GLV-2610 | Alerts and logging | We have implemented improvements in the Elemental Log Collector script. | 
| 2.26.3 | GLV-2654 | Audio, Dolby Digital | The Elemental Live implementation of the Dolby Digital (AC3) decoder has been modified to match the specification. You should not see any change in behavior. | 
| 2.26.3 | GLV-2695 | Captions, CEA-608 | Previously, there was an issue with garbled content when CEA-608 embedded captions were passed through. The captions were garbled. This issue has been fixed. | 
| 2.26.3 | GLV-3723 | Captions, output | There was an issue with the rollover number for CEA-708 embedded captions carried in an ancillary stream in an output. Previously, when the caption distribution packet sequence number rolled over it is incorrectly the rollover number as a duplicate caption packet and is discarded. This issue has been fixed. | 
| 2.26.3 | GLV-3562 | Input switching | There was an issue with switching inputs in a running event configured for virtual input switching or perpetually-prepared inputs. It was possible for the event to crash. The root cause has been fixed. | 
| 2.26.3 | GLV-2885 | NMOS | Since Live version 2.26.0, there has been an issue with the NMOS service when the node was configured for HTTPS. The NMOS service no longer able to discover and register Live event output elementary streams as NMOS senders on the upstream registry. This issue has been fixed. The registration now succeeds. | 
| 2.26.3 | GLV-2487 | Outputs, HLS | There was an issue with CUE OUT and CUE IN tags in the manifest in HLS outputs that occurred in very specific event configurations. The tag was sometimes not inserted or was inserted with an invalid value. This issue has been fixed. | 
| 2.26.3 | GLV-3713 | Outputs, Reliable TS | Fixed an issue on the web interface where ReliableTS StreamID field had a double entry. | 
| 2.26.3 | GLV-2875 | Scripts | Previously arbitrary commands could be run from the pre-processing and post-processing fields on Elemental Live and AWS Elemental Conductor Live. Now only scripts can be run and those scripts must be located in either /data or /opt/elemental\_se/web/public/script directories. Note that the script PID is logged to live\_runner.output. This makes it easier to stop a command if the script runs for too long. | 
| 2.26.2 | SOCK-38878 | Audio output | Fixed an issue where the initial audio gain was not being set correctly when the event starts. | 
| 2.26.2 | GLV-829 | Captions | Fixed an issue whereby captions weren't included in the output in an event with hot backup inputs. | 
| 2.26.2 | GLV-715 | Captions, input | Previously, in very specific use cases, AWS Elemental Live failed to extract SMPTE 2038 Teletext data from the input because the decoder didn't read the data correctly. This issue has been fixed. | 
| 2.26.2 | GLV-1448 | Captions, output | There was an issue with EBU-TT-D captions. If the caption didn't have a specified alignment with its text region, AWS Elemental Live didn't choose the best default alignment. AWS Elemental Live now right-aligns the captions in the text region. | 
| 2.26.2 | GLV-3388 | Inputs, SMPTE 2110 | There was an issue when a Live event is configured to use a SMPTE 2110 input with SMPTE 2022-7 and embedded timecodes. If one of the ancillary streams (either primary or secondary) that carries the timecode ancillary packets drops, the event might fail to resync timecodes. This issue has been fixed. | 
| 2.26.2 | GLV-2800 | Inputs, SMPTE 2110 | There was an issue with SMPTE 2110 inputs that have an ancillary stream that contains timecodes. Sometime, the timecodes were being parsed incorrectly. This issue has been fixed. | 
| 2.26.2 | GLV-1834 | Outputs, in transport steams | There was an issue whereby SDTs in transport streams were always labeled as stream type of 1, regardless of content. This issue has been fixed. | 
| 2.26.2 | GLV-2114 | Platform | A firmware issue has been fixed. | 
| 2.26.2 | GLV-3314 | REST API | There was an issue with the /api/devices/preview endpoint returning 500 errors. This issue has been fixed. | 
| 2.26.2 | GLV-3452 | SCTE 35 | The encoder now performs segment drift correction on SCTE 35 boundaries. | 
| 2.26.2 | GLV-2553 | SCTE 35 | There was an issue with using ESAM POIS server to process SCTE 35 messages. Sometimes, if frames were dropped, the splice preroll could get set to a negative number. This issue has been fixed. | 
| 2.26.2 | GLV-2414 | SCTE 35 | Previously, SCTE 35 messages weren't detected if the PID wasn't present in an input when the channel starts. This issue has been fixed. | 
| 2.26.1 | GLV-2614 | Inputs, SMPTE 2110 | When an AWS Elemental Live event with SMPTE 2110 input had JPEG XS video, Live was incorrectly rejecting a valid JPEG XS license. This has been fixed. | 
| 2.26.1 | GLV-1122 | Installer | Previously, there was no error message when the user installed a GPU build on a CPU-only node. Now, the installer validates the system hardware matches the installer type. | 
| 2.26.1 | GLV-2389 | Licenses | There was an issue where the MOTD was not always accurately displaying correct license information. This has been fixed. | 
| 2.26.1 | GLV-2773 | Logging | Response times were not being printed in Apache SSL access logs. This issue has been resolved. | 
| 2.26.1 | GLV-1489 | Output locking | There was an issue where output locking resync was off by 1 frame when the input is 50fps and the output is 25fps. This issue has been fixed. | 
| 2.26.1 | GLV-907 | Outputs, HLS | Previously, Live didn't honor the baseurl setting for fMP4 HLS output init files. This issue has been fixed. | 
| 2.26.1 | GLV-2510 | SCTE 35 | We have added an environment variable, REPEAT\_AVAIL\_IN\_NEST, that toggles to determine whether or not previously reported avails are repeated when a nested avail occurs. | 

## Resolved issues in Statmux 2.26
<a name="rn-2-26-resolved-statmux"></a>

The following table lists the resolved issues in Statmux 2.26.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 2.26.2 | GLV-2243 | Passthrough programs | There was an issue on AWS Elemental Statmux, whereby audio-only passthrough programs could fail after 20 to 30 minutes. This problem has been fixed. | 

## Resolved issues in Conductor Live 3.26
<a name="rn-2-26-resolved-cl3"></a>

The following table lists the resolved issues in Conductor Live 3.26.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 3.26.5 | GLV-3093 | Events | Previously, in some situations Conductor might create multiple events on the Live appliance when only one event is appropriate. Conductor no longer creates multiple events. | 
| 3.26.3 | GLV-3720 | Schedules | Previously (since version 3.26.1), it was not possible to enable the schedule feature. This issue has been fixed. | 
| 3.26.3 | GLV-2875 | Scripts | Previously arbitrary commands could be run from the pre-processing and post-processing fields on Elemental Live and AWS Elemental Conductor Live. Now only scripts can be run and those scripts must be located in either /data or /opt/elemental\_se/web/public/script directories. Note that the script PID is logged to live\_runner.output. This makes it easier to stop a command if the script runs for too long. | 
| 3.26.2 | GLV-2540 | Web interface | There was an issue with the MPTS Perform tab. It was possibly to press a combination of keys and buttons that makes a different tab appear. | 
| 3.26.2 | GLV-1104 | Logging | There was an issue with continually duplicated entries the PSQL log when the user enables HA. This issue has been fixed. | 
| 3.26.1 | GLV-1859 | User authentication | There was an issue with how Conductor Live handled user login attempts. The issue has been resolved. | 
| 3.26.1 | GLV-2773 | Logging | Response times were not being printed in Apache SSL access logs. This issue has been resolved. | 