

# PID remapping concepts
<a name="pid-remapping-terminology"></a>

Before you configure PID remapping, familiarize yourself with these terms.

**Transport stream structure**  
+ **Packet ID (PID)**

  A number that identifies the packets of one stream in a transport stream.
+ **Elementary stream**

  A single video, audio, or metadata stream in a transport stream.
+ **Program**

  A set of elementary streams that play together, such as a video stream and its audio streams.
+ **Program Map Table (PMT)**

  The table that lists the elementary streams in a program, with their PIDs, stream types, and languages.
+ **Program Association Table (PAT)**

  The table that lists the programs in the transport stream, and the PID of each program's PMT.
+ **Service Description Table (SDT)**

  The table that describes the services in the transport stream, such as the service and provider names.
+ **Program Clock Reference (PCR)**

  Timing information that receivers use to keep playback in sync. The PCR is either on a dedicated PCR PID, which carries only the PCR, or shared with an elementary stream.

**PID remapping rules**  
+ **Rule**

  A match expression and an action. MediaConnect checks the rules in order, and applies the first rule that matches each stream.
+ **Match expression**

  An expression that selects streams, for example by stream type, PID, position, or language. You can combine match expressions with logical operators.
+ **Action**

  The operation that MediaConnect applies to the streams that a match expression selects, for example keeping a stream on its PID or dropping it.
+ **Default action**

  The action that MediaConnect applies to a stream when no rules match.