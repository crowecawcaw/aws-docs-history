

# Transport stream settings

PID remapping changes the transport stream itself. MediaConnect makes the following changes at the transport stream level:
+ Regenerates the Program Association Table (PAT), Program Map Table (PMT), and Service Description Table (SDT) so that they describe the updated structure of the output streams. The PMT preserves the input stream details, such as language and codec.
+ Sets the transport stream ID, program number, and PMT PID, either to the input values or to values that you set.
+ Places the Program Clock Reference (PCR) in the output, either on a dedicated PCR PID or on a PID shared with an elementary stream.

The following table describes the settings that you can change.


| Setting | Description | Custom value | 
| --- | --- | --- | 
| **Transport stream ID** | The number that identifies the transport stream. | A whole number from 0 to 65,535. | 
| **Program number** | The number that identifies the program. | A whole number from 1 to 65,535. | 
| **Program map table PID** | The PID that carries the PMT. | A PID. | 
| **Program clock reference PID** | The dedicated PCR PID in the output. | A PID. | 

## PCR placement
<a name="pid-remapping-pcr-placement"></a>

Receivers use the PCR to keep playback in sync. MediaConnect keeps the PCR in the output, even when your rules move or remove the stream that carries it. MediaConnect raises an alert if the PCR PID conflicts with another setting or rule.

The following table shows where MediaConnect places the PCR in the output, based on where the PCR is in the input.


| PCR in the input | PCR in the output | 
| --- | --- | 
| On a dedicated PCR PID | The same PID, or the **Program clock reference PID** that you set. | 
| Shared with an elementary stream that you keep | Shared with the same elementary stream, at that stream's output PID. | 
| Shared with an elementary stream that you drop or replace with null packets | MediaConnect removes the stream's content and keeps only the PCR, on the same PID number as the input stream or on the **Program clock reference PID** that you set. | 

If the input has no PCR, the output has no PCR. MediaConnect doesn't support a PCR on the PMT PID.