

# PID remapping

The PID remapping processor changes the Packet IDs (PIDs) of the streams in the transport stream that a router output sends.

## How PID remapping works
<a name="how-pid-remapping-works"></a>

PID remapping runs on a router output. After MediaConnect routes content from a router input to the router output, the PID remapping processor transforms the transport stream before MediaConnect sends it to the output's destination. The following steps show how this works at a high level:

1. **Read the input structure** - MediaConnect reads the tables in the incoming transport stream that describe the program and its streams.

1. **Apply your rules** - For each stream in the program, MediaConnect applies the rules that you defined (see [Rules](pid-remapping-writing-rules.md)).

1. **Rebuild the transport stream** - MediaConnect regenerates the tables that describe the transport stream, applies additional settings at the transport stream level (see [Transport stream settings](pid-remapping-transport-stream-settings.md)), and preserves the timing information that receivers need.

1. **Send the output** - MediaConnect sends the transformed transport stream to the output's destination.

After a route change, MediaConnect applies your rules again to the new input.

## PID remapping considerations and limitations
<a name="pid-remapping-considerations"></a>


| Consideration | Description | 
| --- | --- | 
| Transport stream type | Single-program transport streams (SPTS). MediaConnect sends a multiple-program transport stream (MPTS) without remapping. | 
| Changes to the transport stream structure | When PID remapping changes the structure of the transport stream, the change might briefly interrupt downstream receivers while they adjust. | 
| PIDs outside the program | MediaConnect replaces the packets on PIDs that aren't part of the program with null packets. | 
| PID values | 32 to 8,190. | 
| Rules | Up to 32 rules. | 
| SMPTE ST 2022-7 | Two router outputs with the same PID remapping settings don't produce identical streams, so a receiver can't merge them. | 

**Topics**
+ [How PID remapping works](#how-pid-remapping-works)
+ [PID remapping considerations and limitations](#pid-remapping-considerations)
+ [PID remapping concepts](pid-remapping-terminology.md)
+ [Configuring PID remapping](configuring-pid-remapping.md)
+ [Transport stream settings](pid-remapping-transport-stream-settings.md)
+ [Rules](pid-remapping-writing-rules.md)
+ [PID remapping examples](pid-remapping-examples.md)
+ [Monitoring PID remapping](monitoring-pid-remapping.md)