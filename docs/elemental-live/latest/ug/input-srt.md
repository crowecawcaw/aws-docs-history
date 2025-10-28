# Ingesting SRT content

AWS Elemental Live supports ingest of a transport stream (TS) that is
sent from an upstream system that is set up as an SRT listener. In this
scenario, the upstream system waits for Elemental Live (the SRT caller) to
initiate the SRT connection handshake that precedes the transmission of
the source content. The transport stream source can be encrypted with
AES.

**Roles**

With an SRT input, Elemental Live has two roles and the upstream system has two
roles:

- For the SRT connection handshake: Elemental Live is the SRT caller (the
  party that initiates the handshake). The upstream system is the SRT
  listener.

- For the transmission: Elemental Live is always the receiver of the
  content. The upstream system is always the sender of the content.

###### Topics

- [Get ready](input-srt-prereqs.md "input-srt-prereqs.md")
- [Setting up an SRT input](input-srt-setup.md "input-srt-setup.md")
