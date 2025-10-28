# Working with SRT

Elemental Live supports both inputs and outputs that use the SRT
(secure reliable transport) protocol.

Elemental Live can ingest a transport stream (TS) that is sent from
an SRT caller. In this scenario, the upstream system initiates the
handshake that precedes transmission. AWS Elemental Live is the SRT listener that
accepts or rejects the handshake. The transport stream source can be
encrypted with AES.

To work with SRT inputs, see [Ingesting SRT content](input-srt.md "input-srt.md"). To work with
SRT outputs, see [Delivering TS using the SRT protocol](output-srt.md "output-srt.md").
