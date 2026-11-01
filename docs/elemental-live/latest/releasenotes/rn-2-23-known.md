

# Newly identified issues in version 2.23 and 3.23
<a name="rn-2-23-known"></a>

The **Version** column shows the point release that the issue applies to.

## Newly identified issues in Elemental Live 2.23
<a name="rn-2-23-known-live"></a>

The following table lists the newly identified issues in Elemental Live 2.23.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 2.23.3 | SOCK-38330 | Captions, Teletext source | There is a known issue with converting Teletext source captions. If you select both Polish (and specify the language code) and English, there can be problems with the conversion of special characters. | 
| 2.23.3 | SOCK-38272 | Input switching | If an event is created using the REST API, input switching doesn't work. | 
| 2.23.5 | SOCK-38476 | Inputs, SMPTE 2110 | There is currently a limitation on the number of SMPTE 2110/NMOS 1080p sources that Live can encode. The maximum number of sources is 5 events, each with one SMPTE 2110/NMOS source. | 
| 2.23.3 | SOCK-38319 | Operating system driver | There is known issue where the installer fails to update to the latest Broadcom TG3 driver on RedHat systems. | 
| 2.23.4 | SOCK-36891 | Output – JPEG XS | SMPTE ST 2110-22 (JPEG XS) output issue is not compliant when Interlace Mode is Top Field First, instead of Progressive. | 
| 2.23.4 | SOCK-38143 | Output – Timecode in JPEG XS | There is an issue with output encoded with JPEG XS. The encode doesn't include a timecode. | 
| 2.23.4 | SOCK-36839 | Outputs to MediaStore get stuck | A few customers have reported that some events outputting to MediaStore are getting stuck in post-processing when trying to stop. If this happens, the workaround is to manually search for eme\_live processes that are stuck, and then stop them. | 
| 2.23.3 | SOCK-36891 | Outputs, JPEG XS | There is an issue with JPEG XS interlaced outputs with some vendors. The problems can result in distorted or poor video quality. | 
| 2.23.3 | SOCK-38325 | Outputs, ProRes file outputs | There is an issue with ProRes file outputs with more than 12 audio streams, when the destination is a CIFS network storage. The outputs have discontinuities, which results in high IOPS (input/output operations per second). | 
| 2.23.3 | SOCK-38240 | Outputs, SMPTE 2110 with JPEG XS | Sometimes there is an issue with these outputs. The destination can't receive the output from Elemental Live. The problem might reside in a problem in the SDP. | 
| 2.23.5 | SOCK-38365 | Outputs, SRT | There is no alarm when the SRT connection is lost on an SRT output. | 
| 2.23.3 | SOCK-38329 | SCTE-35 | SCTE-35 preroll for splice insert is translated incorrectly. As a result, ads are shown at the wrong time. | 
| 2.23.3 | SOCK-36839 | Stopping events | Occasionally, when cancelling several events at the same time, some of the events do not stop. The workaround is to restart the service, or to use the CLI to stop the process for each stuck event. | 
| 2.23.3 | SOCK-38143 | Timecode | Occasionally, the timecode is not present in outputs that are encoded with JPEG XS. | 

## Newly identified issues in Conductor Live 3.23
<a name="rn-2-23-known-cl3"></a>

The following table lists the newly identified issues in Conductor Live 3.23.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 3.23.5 | SC-4165 | Start and pause | The Conductor web interface doesn't display output controls for pausing, starting a Live event (channel). | 