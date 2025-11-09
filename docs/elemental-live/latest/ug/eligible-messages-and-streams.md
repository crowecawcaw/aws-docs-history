# Eligible messages and

streams

Elemental Live can extract SCTE-35 messages and SCTE-104 messages
from input sources.

The following table specifies the sources (and their corresponding
input types) that Elemental Live supports for each message type.

|                                                           |                                 |                              |
| --------------------------------------------------------- | ------------------------------- | ---------------------------- |
| Message type                                              | Source type                     | Elemental Live Input type    |
| SCTE-35                                                   | HLS                             | HLS network input            |
| MPTS over RTP or UDP                                      | Network input                   |
| Transport stream                                          | Secure Reliable Transport (SRT) |
| Transport stream over RTP or UDP                          | Network input                   |
| Transport stream over RTP with SMPTE 2022-7<br>redundancy | SMPTE 2022-7 network input      |
| SCTE-104                                                  | SDI                             | An SDI or Quadrant interface |
| SDI                                                       | Interleave 4K (HD-2SI)          |
| SMPTE 2110-04 over RTP or UDP                             | SMPTE 2110                      |

###### Note

SCTE-104 messages are converted to SCTE-35 messages early in the
processing, so this guide uses “SCTE-35 messages” to refer to both
SCTE-35 messages and SCTE-104 messages.
