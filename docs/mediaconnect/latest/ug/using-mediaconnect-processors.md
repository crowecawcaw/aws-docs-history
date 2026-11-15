

# Using MediaConnect processors
<a name="using-mediaconnect-processors"></a>

A processor transforms a stream as it passes through a MediaConnect resource. For example, a processor can change the Packet IDs (PIDs) in a transport stream, or remove the streams that a receiver doesn't need. You can add processors when you create or update a resource that supports them.

The following table lists the processor types and the resources that they work with.


| Processor type | Resources | Description | 
| --- | --- | --- | 
| [PID remapping](processors-pid-remapping.md) | Router outputs | Changes the streams and Packet IDs (PIDs) in a transport stream so that it matches what a receiver expects. For example, you can keep the same transport stream structure across route changes. You can also keep only the audio languages that a receiver needs, or map streams to fixed PID ranges. | 

**Topics**
+ [PID remapping](processors-pid-remapping.md)