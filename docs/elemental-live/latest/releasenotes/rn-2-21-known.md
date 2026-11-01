

# Newly identified issues in version 2.21 and 3.21
<a name="rn-2-21-known"></a>

The **Version** column shows the point release that the issue applies to.

## Newly identified issues in Elemental Live 2.21
<a name="rn-2-21-known-live"></a>

The following table lists the newly identified issues in Elemental Live 2.21.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 2.21.3 | SOCK-37299 | Input prepare | When customers schedule an input switch ahead of the switch time, Live starts preparing the input. In a scenario where the audio sample format in the source changes between the probe and the switch time, the updated audio information is not passed to audio sync. This will result in corrupted audio on the output. | 
| 2.21.2 | SOCK-37013 | Inputs – SMPTE ST 2110 | There is sometimes a sync drift of up to .1 seconds between audio and video for Elemental Live SMPTE ST 2110 inputs. | 
| 2.21.0 | SOCK-36737 | Inputs - SMPTE | When an event was configured to use a SMPTE ST 2110 or SMPTE ST 2022-6 input with SMPTE ST 2022-7 redundancy, the network input could drop packets consistently. This led to the per-event ingest log filling up the /opt disk partition. This issue is fixed in version 2.21.1. | 
| 2.21.0 | SOCK-36691 | Outputs - SCTE-35 | The combination of output locking resyncs and SCTE-35 conditioning could lead to segment drift. | 
| 2.21.3 | SOCK-37300 | SMPTE 2110 | When running multiple SMPTE 2110\+2022-7 or 2022-6\+2022-7 HD events, there is a possibility that all events will intermittently drop video frames at the same time. As more events are added, the occurrences of packet drops increases. The problem is being actively investigated. | 

## Newly identified issues in Statmux 2.21
<a name="rn-2-21-known-statmux"></a>

The following table lists the newly identified issues in Statmux 2.21.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 2.21.3 | SOCK-37243 | Alerts | The alerts for "MPTS channel output bitrate is 0" and "Program <N> switched active encoder to pipeline 0" will fire when a Statmux channel is started. These alerts will clear shortly after the channel has started. This is due to startup delays in the channel to statmux communications and do not represent an issue unless the alerts stay on indefinitely. | 
| 2.21.3 | SOCK-37242 | Alerts | The alert that appears for MPTS output protection does not get cleared after the underlying problem has been resolved. | 
| 2.21.3 | SC-4279 | Alerts | Many alerts (specifically those with alert codes greater than 5000) did not show in the Statmux web interface or AWS Elemental Conductor Live web interface or the APIs. This has been resolved and these alerts will now appear. | 
| 2.21.0 | SOCK-36700 | Statmux - Log | A critical log message "Failed to send update MultiplexProgram message to MME" erroneously displays. This message is coming from Statmux, but there is no impact to Statmux customers. | 