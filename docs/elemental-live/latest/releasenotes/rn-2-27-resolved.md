

# Resolved issues in version 2.27 and 3.27
<a name="rn-2-27-resolved"></a>

The **Version** column shows the point release that the issue applies to.

## Resolved issues in Elemental Live 2.27
<a name="rn-2-27-resolved-live"></a>

The following table lists the resolved issues in Elemental Live 2.27.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 2.27.5 | GLV-7202 | Captions, SCTE-35 | Previously, SCTE-35 messages with a non-zero pts\_adjustment field were not being output when processed through the ESAM pipeline. This issue has been fixed. | 
| 2.27.5 | GLV-7194 | Event processing | Previously, editing an event with an audio selector group could cause the preview to break. This issue has been fixed. | 
| 2.27.5 | GLV-6577 | Outputs, encoding | Previously, the field\_based\_flag value was not being set correctly for AVC interlaced encodes. This has been corrected for improved spec compliance. | 
| 2.27.5 | GLV-6798 | Platform, database | Previously, the sessions database table could encounter limitations with very high usage over time. The primary key has been migrated to support larger values. | 
| 2.27.5 | GLV-7083 | Platform, imports | Previously, importing event XML files from older software versions could fail. An automatic upgrade process has been added to handle older XML formats during import. | 
| 2.27.5 | V2159100448 | Platform | Previously, repeated privileged operations on systems running RHEL 9.6 could cause a gradual increase in kernel slab memory usage over time. This issue has been fixed. | 
| 2.27.5 | P391933808 | Outputs, CMAF | Previously, CMAF outputs with Dolby content could fail validation unnecessarily. Validation has been updated to allow CMAF outputs past Dolby validation where appropriate. | 
| 2.27.5 | P375412968 | Outputs, CMAF | Previously, MP4/CMAF outputs with EC-3 or AC-3 audio could have an incorrect track count in the sample description. This issue has been fixed. | 
| 2.27.5 | P381199744 | Captions, SCTE-35 | Previously, when ESAM returned late for immediate splice insert or time signal events, the start time was not adjusted. Changes have been made to move the start time forward in this situation. | 
| 2.27.5 | V2041197194 | Event processing | Previously, stopping an event could result in a gradual increase in memory usage over time. This issue has been fixed. | 
| 2.27.5 | V1994113448 | Event processing | Previously, unexpired SCTE-35 network end/start messages could be processed incorrectly. This issue has been fixed. | 
| 2.27.5 | EMM-4248 | Event processing | In certain situations, H.264 auPPS and auSPS field parsing could cause event processing errors. This issue has been fixed. | 
| 2.27.5 | 828de255b9c | Inputs, SMPTE 2110 | Previously, SMPTE 2110 setup could fail when hyperthreading was disabled. This has been fixed to handle the configuration more gracefully. | 
| 2.27.4 | GLV-7161 | Platform, Downgrades | Previously, license files could be lost during software downgrades. Changes have been made to preserve license files from existing installations when performing downgrades. | 
| 2.27.4 | GLV-2849 | Inputs, RTMP | Previously, an event could crash when an RTMP pull input was disconnected, such as during a stop or input switch. This issue has been fixed. | 
| 2.27.4 | GLV-7090 | Outputs, SRT | SRT output could block indefinitely in some instances. Send timeout and buffer size configuration has been added for reliable transport stream SRT senders to prevent blocking. | 
| 2.27.4 | GLV-7116 | Outputs, CMAF Ingest | The CMAF Ingest destinations have been updated for better path handling. | 
| 2.27.4 | GLV-6993 | Event processing | Previously, input pipeline preparation could fail to reset properly when cancelled for perpetually decoded inputs. This issue has been fixed. | 
| 2.27.4 | GLV-7132 | Platform, NMOS | Previously, there was an issue with null sender IDs in NMOS implementation. This issue has been resolved. | 
| 2.27.4 | GLV-5513 | Event processing | A timeout has been added to prevent indefinite blocking during event processing operations. | 
| 2.27.4 | GLV-7074 | Event processing | Frame sync black fill behavior has been improved to differentiate between active and ended input states. | 
| 2.27.4 | GLV-7081 | SCTE-35 | Previously, SCTE-35 NotIndicated signals could cause HLS segment doubling. This issue has been fixed. | 
| 2.27.4 | GLV-3400 | SCTE-35 | Excessive "Does not contain an avail" messages could be generated in certain workflows. Message frequency has been limited to reduce log noise. | 
| 2.27.4 | GLV-7109 | Captions, CMAF Ingest | Previously, embedded captions could interfere with MediaPackage v2/CMAF frame capture functionality. This issue has been resolved. | 
| 2.27.4 | EMM-4062 | Outputs, CMAF Ingest | CMAF Ingest segment numbers could be incorrect after event stop/start operations. This issue has been fixed. | 
| 2.27.4 | LIVESEC-12 | API | Stricter validations on /devices/{device\_id}/preview endpoint now restrict image locations to the /public/images/preview directory and filenames to alphanumeric characters. | 
| 2.27.4 | GLV-7083 | NMOS | Previously, importing an XML with a 2110 receiver group input without a corresponding shadow input required manual correction. The import process now automatically adds the shadow input. | 
| 2.27.4 | GLV-7185 | Platform | The latest Red Hat security patches have been applied. We continue to apply Red Hat security patches to keep the appliance secure, in accordance with the shared responsibility model. | 
| 2.27.3 | GLV-6571 | API | The playlist API endpoint (used to create a playlist of inputs to ingest) can sometimes result in a 500 error code. This issue has been fixed. | 
| 2.27.3 | GLV-6342 | Data delivery | Previously, large file transfers to Amazon S3 could fail because the transfer timed out. The timeout has been increased. | 
| 2.27.3 | GLV-6662 | Data delivery | Previously, data transfers over slower connections could fail. This issue has been fixed. | 
| 2.27.3 | GLV-6947 | Deleting events | Previously, archived events sometimes didn't get deleted on the expected date. This issue has been fixed. | 
| 2.27.3 | GLV-6363 | Input preview | Sometimes input preview didn't appear when it was enabled. This issue has been fixed. | 
| 2.27.3 | GLV-6944 | Inputs, SMPTE 2110 with NMOS | There was an issue with patching of a SMPTE 2110 input that uses NMOS. If user authentication was enabled, the patch didn't occur. This issue has been fixed. | 
| 2.27.3 | GLV-6714 | Outputs, RTMP | There was an issue when creating an RTMP output group by duplicating an event or using a Conductor Live profile. Some settings didn't get copied over. This issue has been fixed. | 
| 2.27.3 | GLV-5843 | Performance | The resource allocation logic on Elemental Live, Elemental Statmux, and Conductor Live has been raised to prevent event crashes. | 
| 2.27.3 | GLV-6383 | Platform, downgrades | Previously, a downgrade to Elemental Live 2.27.0 might fail. This issue has been fixed. | 
| 2.27.3 | GLV-6350 | Platform, upgrades | There was an issue with events not automatically restarting after upgrading the software. This issue has been fixed. | 
| 2.27.2 | GLV-2972 | Authentication | A recent change inadvertently introduced the rule that if authentication was enabled, only users with the Admin role could download the XML from the web interface or using the API. This issue has been fixed so that any authenticated user can perform these actions. | 
| 2.27.2 | GLV-5785 | Captions, EBU-TT and TTML | Previously, Live might omit or skip some non-ASCII characters when encoding captions into TTML/EBU-TT format. This problem has been fixed. | 
| 2.27.2 | GLV-5843 | Event crash | Previously, a node might crash when a lot of events were running. Changes have been made to prevent the crash in this situation. | 
| 2.27.2 | GLV-4829 | Event crash | Previously, MXF archive output used in conjunction with WAV audio output could cause crashes. This problem has been fixed. | 
| 2.27.2 | GLV-5881 | Inputs, Dolby | Previously, there was an issue with handling Dolby audio input. The issue forced the user to restart the event. The issue has been fixed. In addition, a change has been made to reduce the number of log messages when problems like this one occur. | 
| 2.27.2 | GLV-6069 | Inputs, SMPTE 2110 | ST 2110-30 output timing handling has been adjusted to be more resilient when faced with input timing disruptions. | 
| 2.27.2 | GLV-5889 | Platform, downgrade | Previously, there was an issue that prevented a downgrade from 2.27.1 to 2.26.5. This issue has been fixed. | 
| 2.27.2 | GLV-5432 | XML import | An issue has been corrected that prevented the import of a Live event XML file that included a SMPTE 2110 input. | 
| 2.27.1 | GLV-525 | Alerts, logs, and messages | Loudness log files will now be retained for 30 days (by default) before being deleted from the appliance. The retention period is configurable in the Settings > General tab, and cleanup can be disabled by setting to 0 days. | 
| 2.27.1 | GLV-2606 | Backup files | TGF files will now be retained for 30 days (by default) before being deleted from the appliance. The retention period is configurable in the Settings > General tab, and cleanup can be disabled by setting to 0 days. | 
| 2.27.1 | GLV-5696 | Captions, EBU-TT-D | In Live 2.27.0, the calculation of tts:lineHeight in EBU-TT-D captions outputs was incorrect. This error caused the text to appear noticeably larger. This issue has been fixed. | 
| 2.27.1 | GLV-5241 | HLS manifests | Fixed an issue where pausing and unpausing an output group could result in partial HLS parent manifests being written. | 
| 2.27.1 | GLV-5816 | Inputs, SDI | In Live 2.27.0, the configuration of ancillary data (SCTE 35 messages) in an SDI input was reset when the channel was started. This caused any channel that was already running to stop ingesting ancillary data. This issue has been fixed. | 
| 2.27.1 | GLV-5545 | Inputs, SMPTE 2110 | Fixed an issue where new NMOS events weren't being imported properly. | 
| 2.27.1 | GLV-5677 | Inputs, SMPTE 2110 | Previously, the system status API didn't apply to 2110 inputs configured with NMOS receiver groups, or with SDI input groups. This meant that it wasn't possible to verify the status of these inputs. This issue has been fixed. | 
| 2.27.1 | GLV-5764 | Inputs, SMPTE 2110 with NMOS | There was an issue when importing the XML for an event, when the event included configuration for a 2110 NMOS input. Elemental Live didn't handle the audio selectors correctly. This issue has been fixed. | 
| 2.27.1 | GLV-3024 | Motion graphic overlays | Previously, Elemental Live might lose AV Sync if motion graphics overlays were enabled and many input switches happened. Additionally, there was a memory leak with MOV motion graphics. Both of these issues have been fixed. | 
| 2.27.1 | GLV-5382 | Motion graphic overlays | Fixed an issue where motion graphics insertion would stop on looping inputs after the first input switch. | 
| 2.27.1 | GLV-5609 | Outputs, CMAF ingest | Previously, Elemental Live was incorrectly validating against output name modifiers across different CMAF Ingest output groups. Now, Live enforces modifier name uniqueness only within each output group. | 
| 2.27.1 | GLV-5383 | Outputs, SRT | Increased the send delay for SRT outputs to 4 seconds. Now, after a successful connection, Elemental Live attempts to send data for 4 seconds before timing out. | 
| 2.27.1 | GLV-5610 | Outputs, SRT | The passphrase length for SRT outputs has been increased from 72 characters to 80 characters. | 
| 2.27.1 | GLV-5257 | Video | Fixed an issue where Elemental Live was not always inserting RAI markers per specification. | 
| 2.27.1 | GLV-5763 | Web interface | In Elemental Live 2.27.0, you couldn't save changes to settings in the Settings > General page. This issue has been fixed. | 
| 2.27.0 | GLV-4662 | Alerts and logging | Improved logging of SCTE 35 handling, to include a unique ID. This ID makes it easier to trace processing of customer SCTE 35 messages through the transcoding pipeline. | 
| 2.27.0 | GLV-5070 | Alerts and logging | There is improved logging during the assignment of output PIDs to used input streams. | 
| 2.27.0 | GLV-4669 | Alerts and logs | Logs for NMOS and motion graphics could grow indefinitely. There is now a limit to the number and size of these logs. | 
| 2.27.0 | GLV-4749 | Alerts and logs | Fixed an issue where the logs in /opt/elemental\_se/web/log on Conductor Live were not correctly rotated. | 
| 2.27.0 | GLV-5097 | Alerts and logs | Unnecessary messages have been removed from the logs. | 
| 2.27.0 | GLV-5262 | Alerts and logs | SVQ is defined by the encoder favoring speed over quality. Diagnostic logging has been improved when SVQ occurs. | 
| 2.27.0 | GLV-5367 | Alerts and logs | Fixed an issue where missing IDs on deferred caption stores could cause spamming in logs. | 
| 2.27.0 | GLV-4847 | Audio | Fixed an issue where normalized mono audio can begin to slowly decay towards silence. | 
| 2.27.0 | GLV-3763 | Audio-only outputs | There was an issue with HLS audio-only outputs whereby the media segments were faster than real time. This issue has been fixed. | 
| 2.27.0 | GLV-2571 | Captions, EBU-TT-D | Previously, the data included in EBU-TT-D captions outputs had unreferenced (and unnecessary) style and region elements. This data has been removed. | 
| 2.27.0 | GLV-2572 | Captions, EBU-TT-D | Previously, the data included in EBU-TT-D captions outputs had the style elements in both the body and paragraph sections. Now, the tts:fontSize and tts:lineHeight appear only in the paragraph <p> sections. | 
| 2.27.0 | GLV-5404 | Epoch locking | Very rarely, epoch locked events could crash. The underlying issue has been fixed. | 
| 2.27.0 | GLV-5172 | Inputs, RTP | There was an issue when a Live event with an RTP FEC input is erroneously sent streams from two different sources at the same time. The log might get filled with misleading messages about a change in the FEC protection parameters. This issue has been fixed. | 
| 2.27.0 | GLV-3705 | Motion graphics | Fixed an issue where motion graphics might render with an incorrect hue. | 
| 2.27.0 | GLV-5039 | NMOS | When upgrading from Live 2.26.1 to Live 2.26.4 or later, NMOS could stop working. This issue has been fixed. | 
| 2.27.0 | GLV-4280 | NMOS 2110 | Live events with NMOS-controlled 2110 outputs sometimes would not appear in the NMOS network. This issue has been fixed. | 
| 2.27.0 | GLV-4454 | NMOS 2110 | Fixed an issue whereby changing the secondary interface on a 2110 Receiver Group would not update the NMOS receiver. | 
| 2.27.0 | GLV-4656 | Output listening | There was an issue with Live's handling of output when output listening is enabled. The output bandwidth was unexpectedly high. This issue has been fixed. | 
| 2.27.0 | GLV-4856 | Outputs, CMAF Ingest | Fixed an issue in CMAF Ingest outputs where video and audio segments didn't align when video had non-integer framerate. | 
| 2.27.0 | GLV-5301 | Outputs, SRT | There was an issue where SRT output connection failures resulted in the encoder favoring speed over quality. This SVQ resulted in alarms. The issue has been resolved. | 
| 2.27.0 | GLV-5312 | Outputs, Zixi | Fixed an issue where secondary Zixi outputs failed to initialize correctly. | 
| 2.27.0 | GLV-5334 | Platform | The operating system has been upgraded from RHEL 9.2 to RHEL 9.4. | 
| 2.27.0 | GLV-5175 | PTS | There was an issue where the PTS adjustment was set to 0. Elemental Live still performed the adjustment on some messages. This issue has been fixed. | 
| 2.27.0 | GLV-4729 | SCTE 35 | Fixed a case where long Network Start blackouts didn't work properly. | 
| 2.27.0 | GLV-4850 | SCTE 35 | Previously, some SCTE 104 messages in a 2110 input might not get successfully converted. This issue has been fixed. | 
| 2.27.0 | GLV-5116 | SCTE 35 | There was an issue when an event includes SMPTE 2110 input and the SMPTE 2110 ancillary stream carries a SCTE 104 message in which the duration\_extension\_frames field is non-zero. The duration calculated for the number of frames was incorrect. This issue has been fixed. | 
| 2.27.0 | GLV-5370 | SCTE 35 | Fixed an issue where resynching could cause empty SCTE 35 segments in CMAF Ingest outputs. | 
| 2.27.0 | GLV-5226 | SDI | Fixed an issue with the SDI router. | 

## Resolved issues in Statmux 2.27
<a name="rn-2-27-resolved-statmux"></a>

The following table lists the resolved issues in Statmux 2.27.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 2.27.3 | GLV-5843 | Performance | The resource allocation logic on Elemental Live, Elemental Statmux, and Conductor Live has been raised to prevent event crashes. | 
| 2.27.1 | GLV-5763 | Web interface | In Elemental Statmux 2.27.0, you couldn't save changes to settings in the Settings > General page. This issue has been fixed. | 
| 2.27.0 | GLV-5070 | Alerts and logging | There is improved logging during the assignment of output PIDs to used input streams. | 
| 2.27.0 | GLV-5333 | Virtual IPs | Fixed an issue where Statmux crashed when using virtual source IPs. | 

## Resolved issues in Conductor Live 3.27
<a name="rn-2-27-resolved-cl3"></a>

The following table lists the resolved issues in Conductor Live 3.27.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 3.27.3 | GLV-5754 | Deleting profiles | Previously, it was not possible to delete Conductor Live profiles that used SMPTE 2110 inputs. This issue has been fixed. | 
| 3.27.3 | GLV-6619 | Inputs, SMPTE 2110 with NMOS | There was a problem with updating Conductor Live profiles on SMPTE 2110 inputs that use NMOS. The problem resulted in an error in the web interface. This issue has been fixed. | 
| 3.27.3 | GLV-6714 | Outputs, RTMP | There was an issue when creating an RTMP output group by duplicating an event or using a Conductor Live profile. Some settings didn't get copied over. This issue has been fixed. | 
| 3.27.3 | GLV-5843 | Performance | The resource allocation logic on Elemental Live, Elemental Statmux, and Conductor Live has been raised to prevent event crashes. | 
| 3.27.1 | GLV-4997 | Alerts, logs, and messages | Fixed an issue where some alerts were not clearing properly after channels were stopped or restarted. | 
| 3.27.0 | GLV-3720 | Schedule | Fixed an issue where the user couldn't enable schedules in Conductor Live. | 
| 3.27.0 | GLV-5385 | Upgrading | Sometimes a channel would not restart after an upgrade of the Conductor node. This issue has been fixed. | 