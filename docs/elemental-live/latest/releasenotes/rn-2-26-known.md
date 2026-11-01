

# Newly identified issues in version 2.26 and 3.26
<a name="rn-2-26-known"></a>

The **Version** column shows the point release that the issue applies to.

## Newly identified issues in Elemental Live 2.26
<a name="rn-2-26-known-live"></a>

The following table lists the newly identified issues in Elemental Live 2.26.


| Version | Key | Topic | Description | 
| --- | --- | --- | --- | 
| 2.26.2 | GLV-3408 | Output captions | There is an issue with the following event configuration: Two (or more) HLS output groups that both include DVB-Sub input captions and Web VTT output captions that using OCR. When the event starts, the event gets stuck in the pre-processing stage. This message appears: All Caption Target OCR Languages must match for a given caption selector. The workaround for this issue is to set up each HLS output group in a separate event. | 