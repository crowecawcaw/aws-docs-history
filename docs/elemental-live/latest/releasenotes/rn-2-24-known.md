

# Newly identified issues in version 2.24 and 3.24
<a name="rn-2-24-known"></a>

The **Version** column shows the point release that the issue applies to.

## Newly identified issues in Elemental Live 2.24
<a name="rn-2-24-known-live"></a>

The following table lists the newly identified issues in Elemental Live 2.24.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 2.24.0 | SOCK-38143 | Output, JPEG XS | There is an issue with output encoded with JPEG XS. The encode doesn't include a timecode. This issue doesn't affect passthrough of JPEG XS. | 
| 2.24.2 | SOCK-38529 | Ad avails, with ESAM | ESAM SCTE 35 stopped outputting in events longer than 53 hours. This issue was mistakenly marked as resolved in version 2.24.0. | 
| 2.24.2 | SOCK-36270 | Performance on L8xx appliances | There is an issue with the competing demands of different workflows on the same L88x appliance. You might sometimes want to use the appliance for workflows that require optimization for source ingestion, at other times for workflows that require optimization for outputs. We continue to look into this issue. | 

## Newly identified issues in Conductor Live 3.24
<a name="rn-2-24-known-cl3"></a>

The following table lists the newly identified issues in Conductor Live 3.24.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 3.24 | SOCK-38143 | Output, JPEG XS | There is an issue with output encoded with JPEG XS. The encode doesn't include a timecode. This issue doesn't affect passthrough of JPEG XS. | 