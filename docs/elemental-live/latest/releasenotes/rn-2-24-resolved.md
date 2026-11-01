

# Resolved issues in version 2.24 and 3.24
<a name="rn-2-24-resolved"></a>

The **Version** column shows the point release that the issue applies to.

## Resolved issues in Elemental Live 2.24
<a name="rn-2-24-resolved-live"></a>

The following table lists the resolved issues in Elemental Live 2.24.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 2.24.1 | SOCK-38673 | Outputs, SMPTE 2110 | In situations where Live was converting interlaced inputs to progressive SMPTE 2110 outputs it was found that our SMPTE 2110 output would fall out of compliance and not be consumable by some devices. This has been fixed. | 
| 2.24.0 | SOCK-38657 | Outputs, to MediaStore | There was a problem in delivering encodes to AWS Elemental MediaStore when the encode used chunked transfer encoding (CTE). The output could not be written to the MediaStore container. The specific cause for these failures has been resolved. | 
| 2.24.0 | SOCK-38648 | Outputs, SMPTE 2110 | SMPTE 2110 outputs to devices with extremely small buffers could not always be handled by the downstream system. This issue has been fixed. | 
| 2.24.0 | SOCK-38610 | Outputs, SMPTE 2110 | There was a problem with using NMOS in Elemental Live versions 2.19.3 to 2.23.3 and in version 2.23.5. NMOS events would not post to NMOS registration server, which meant that flow connection wasn't possible from the server side. This issue has been resolved and the NMOS registration server can now find and post SDP files. | 
| 2.24.0 | SOCK-38601 | Outputs, SMPTE 2110 | Some downstream systems had problems decoding Elemental Live JPEG XS outputs. This problem occurred even though the Elemental Live implementation was compliant with the standard. These issues have been resolved and tested with a wide variety of interoperability tests. | 
| 2.24.0 | SOCK-38596 | Captions | There was a problem with events that included EBU-TT-D captions in the output. The log files were spammed with region and style messages. This issue has been fixed. | 
| 2.24.0 | SOCK-38579 | Outputs, Reliable TS | Previously, with a Reliable TS output that uses the SRT protocol, the attempt to connect to the remote SRT endpoint could time out. To resolve this problem, the default connection timeout when using primary-only connections has been increased. | 
| 2.24.0 | SOCK-38529 | Ad avails, with ESAM | ESAM SCTE 35 stopped outputting in events longer than 53 hours. This issue has been resolved. | 
| 2.24.0 | SOCK-38476 | Outputs, SMPTE 2110 | We have made density improvements on appliances that have events that are ingesting SMPTE 2110 NMOS 1080p. | 
| 2.24.0 | SOCK-38475 | Inputs, RTMP | A race condition was encountered for workflows where two events ingested from the same RTMP stream. When one event was restarted after the RTMP stream was lost, the ingest process could subsequently crash. This issue has been resolved. | 
| 2.24.0 | SOCK-38365 | Alerts and messages | Starting in version 2.23.2, Elemental Live failed to raise an alarm when the SRT connection was lost on an SRT output. The alarm has been restored. | 
| 2.24.0 | SOCK-38283 | Outputs, SMPTE 2110 | A change has been made to SMPTE 2110-22 outputs. There is now information in the output payload in the first RTP packet for each video frame or field. The information is the Video Support Box and the Color Specification Box. This change brings the implementation into line with the JPEG XS VSF standard. | 
| 2.24.0 | SOCK-38242 | Outputs, SMPTE 2110 | There was an issue where SMPTE 2110-20 (uncompressed) video output. Frequently, the video was out of phase and did not keep the virtual receive buffer at the correct level. This issue has been resolved, so that the SMPTE 2110-20 output is completely compliant. | 
| 2.24.0 | SOCK-38154 | Outputs, SMPTE 2110 | A change has been made to SMPTE 2110-22 outputs. The default value for the video profile parameter has been changed from Main to High. This change brings the implementation into line with the JPEG XS VSF TR 08 standard. | 
| 2.24.0 | SOCK-38152 | Outputs, SMPTE 2110 | A change has been made to SMPTE 2110-22 outputs. The number of RTP payload bytes is now a multiple of 8. This change brings the implementation into line with the JPEG XS VSF TR 08 standard. | 
| 2.24.0 | SOCK-36891 | Outputs, SMPTE 2110 | A change has been made to SMPTE 2110-22 outputs to make it compliant with the standard when the output is Interlace Mode with Top Field First. | 
| 2.24.1 | SOCK-35771 | Audio gain, preview | The Preview page for a running event includes an indicator that shows the current audio gain. There was a problem that caused the indicator to not refresh properly. This problem has been resolved. The indicator continually updates to show the current audio gain as the event is running. | 
| 2.24.1 | SOCK-38705 | Captions, SMPTE 2110 outputs | There was a problem with captions in an event that included input switching and that included SMPTE 2110 outputs. Sometimes an unreliable network caused captions be garbled in the SMPTE 2110 output. This problem has been resolved. | 
| 2.24.1 | SOCK-38725 | Outputs, DASH | There was an issue where Live could get stuck when trying to stop an event that included a DASH output group with one audio output. The problem has been fixed, so that the event stops successfully. | 
| 2.24.1 | SOCK-38284 | Outputs, Reliable TS | Previously, there was a problem with Reliable TS that used Zixi. The value in the Zixi Latency field (in the output) was ignored when the user saved the event. This problem has been resolved. | 
| 2.24.1 | SOCK-38790 | Virtual input switching | Starting with the 2.24.0 release of Live, there was a problem with the virtual input switching feature. The UTC point time in the ESAM Signal Processing Event was incorrect. This has been fixed. | 
| 2.24.2 | SOCK-38918 | Crash | Very rarely, when restarting one Live Event, all the events on the appliance crashed. This issue has been fixed. | 
| 2.24.2 | SOCK-38871 | Web interface | There was a problem on the web interface for an event, in the section for a Reliable TS output group with an output with the Delivery Protocol set to Secure Reliable Transport. The SRT Connection mode was not visible. This issue has been fixed. | 
| 2.24.2 | SOCK-38859 | PTP | Previously, the PTP alert activation threshold was set to a hard-coded value. Now, it is configurable via the environment variable PTP\_ALERT\_PTP\_OFFSET\_THRESHOLD. The field specifies the maximum number of nanoseconds that the PTP clock can be offset from the Grandmaster clock. If the offset is more, an alert occurs. | 
| 2.24.2 | SOCK-38809 | Time format conversion | There was a problem on appliances that were set up with the FORCE\_LTC\_TO\_UTC environment variable set to True. The conversion was inaccurate. This issue has been fixed. | 
| 2.24.3 | SOCK-38928 | Audio input | There was a problem with blank lines in the logs when the event includes Dolby Digital Plus audio. This problem has been fixed. | 
| 2.24.3 | SOCK-38895 | API | The following additional security headers have been added by default to the web server HTTP and HTTPS requests.+ X-Frame-Options: deny<br />+ X-XSS-Protection: 1; mode=block<br />+ X-Content-Type-Options: nosniff<br />+ Strict-Transport-Security: max-age=47304000; includeSubDomains (added only to HTTPS)<br />+ Cache-Control: no-cache | 
| 2.24.3 | SOCK-38822 | Memory leak | Previously, the L842 appliance ran out of memory within one week. The memory leak that caused this problem has been fixed. | 
| 2.24.3 | SOCK-38778 | Captions input | Occasionally, ARIB captions in SDI inputs caused the event to stop. This issue has been fixed. | 
| 2.24.3 | SOCK-38529 | SCTE 35 | ESAM SCTE 35 stopped outputting in events longer than 53 hours. This issue was reported as a known issue in version 2.24.2. This issue has been fixed. | 
| 2.24.5 | SOCK-39063 | Caption outputs | There was an issue with corrupted output captions. This issue occurred in an event that passes through SMPTE 2038 to a SMPTE 2110 output. This issue has been fixed. | 
| 2.24.5 | SOCK-38565 | Caption outputs | There was an issue with missing output captions in an event that converted DVB-Sub or SCTE 27 source captions to WebVTT or Burnin captions. This issue has been fixed. | 
| 2.24.5 | SOCK-39194 | HLS manifests | Sometimes Live stopped emitting child manifests in an HLS output group. This issue has been resolved. | 
| 2.24.5 | SOCK-39195 | Input switching | Sometimes a scheduled input switch didn't occur. This issue has been fixed. | 
| 2.24.5 | SOCK-38914 | Input switching | There was an issue that caused Live to crash during an input switch in an event with a low framerate encode. This issue has been fixed. | 
| 2.24.5 | SOCK-38917 | Output, crash | There was an issue whereby Live didn't respond well when the downstream system for an output wasn't responsive. This situation no longer causes Live to crash. | 
| 2.24.5 | SOCK-38931 | Output, Zixi | There was an issue with an event with a Zixi output, if the event started but the Zixi endpoint was not accepting connections. After the Zixi endpoint did start to accept connections, Live could become unresponsive. This issue has been fixed. Live no longer becomes unresponsive and will start to deliver to the endpoint. | 
| 2.24.5 | SOCK-39193 | PDT | Very rarely, production of the PDT in an HLS output became sporadic. This issue has been fixed. | 
| 2.24.5 | SOCK-39192 | Unpause | Occasionally unpausing the event occasionally caused segment drift. This issue has been fixed. | 
| 2.24.4 | SOCK-38970 | Inputs, AJA cards | Previously, there was a problem with how Elemental Live handled problems reading an AJA card. Elemental Live created a log entry, then immediately tried again to read from the card (instead of waiting for an interval). This could result in filling up the storage disk. This issue has been resolved with three improvements: The attempt to read now has a retry interval (10 milliseconds). In addition, only one entry is written to the log for each attempted input start attempt. And finally, the message in the log provides more detail. | 
| 2.24.4 | SOCK-38969 | Inputs, SMPTE 2022-6 | Previously, there was a problem with how Elemental Live extracted ancillary data from a SMPTE 2022-6 input. If the video was SD (standard definition), the ancillary data wasn't extracted properly. This issue has been fixed. | 
| 2.24.4 | SOCK-38937 | Outputs, Zixi latency | Previously, there was a problem with handling of the Latency field in a Zixi output in a Reliable TS output group. If you changed the value in the field, Elemental Live overwrote it back to the default. This issue has been resolved. | 

## Resolved issues in Statmux 2.24
<a name="rn-2-24-resolved-statmux"></a>

The release notes for this version don't list resolved issues for Statmux.

## Resolved issues in Conductor Live 3.24
<a name="rn-2-24-resolved-cl3"></a>

The following table lists the resolved issues in Conductor Live 3.24.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 3.24.0 | SC-4165 | Web interface | The Conductor Live web interface did not display the correct output playback controls for some output group types: Archive, HLS, RTMP, and Reliable TS. This issue has been resolved. | 
| 3.24.1 | SC-4385, SC-4386 | Channel starts in a cluster | We have made improvements to the robustness of channel starts. The incidence of failed channel starts should now be much lower, especially in node failover situations. | 
| 3.24.2 | SC-4333 | Inputs, SRT | Previously, there was a problem with the information displayed on the Conductor Live web interface for a running channel. The information for an SRT input didn't include information such as the video resolution. This issue has been fixed. | 
| 3.24.4 | SC-4406 | Web interface | Previously, the preview image and media info failed to display when the user edited channel parameters for file inputs. This issue has been resolved. | 
| 3.24.4 | SC-4394 | Web interface | Previously, the preview button was missing from the web interface when the was edited channel parameters for a SMPTE 2022-6 input. The button has been added and now returns a preview image and media info for the URI. Note this only works for a single input on a channel at the moment. | 