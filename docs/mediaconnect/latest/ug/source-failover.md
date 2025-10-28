# Source failover on a MediaConnect flow

Source failover is a setup that involves two redundant sources for a transport stream
flow. This redundancy helps to minimize disruption to your video stream. To use source
failover, you specify two sources for the flow, then choose
one of two options for the failover mode: _Merge_ or _Failover_.

- Merge mode combines the sources into a single stream, allowing a graceful
  recovery from any single-source loss. If you set the failover mode to _Merge_, you can set the recovery window, which is
  the size of the buffer (delay) that you want MediaConnect to maintain. A larger
  recovery window means a longer delay in transmitting the stream, but more room
  for error correction. A smaller recovery window means a shorter delay, but less
  room for error correction. Sources used this way need to be _binary identical_, which means that they need to
  have originated from the same encoder. MediaConnect must also receive content from the
  two sources at the same time. Additionally, if the sources use RTP protocol,
  they must have RTP headers with aligned sequence numbers and they must also
  comply with the SMPTE ST 2022-7 standard.

###### Note

SMPTE ST 2022-7 is a standard developed by the Society of Motion Picture
and Television Engineers (SMPTE) group. The ST 2022-7 standard defines a
method that replaces missing packets with packets in an identical, redundant
stream. This type of failover requires a small latency buffer in your
workflow to allow time for MediaConnect to recover packets from the two
streams.

- Failover mode allows switching between a primary and a backup stream. This
  switching facilitates an easy transition to a more reliable stream. If you set
  the failover mode to _Failover_, you can
  specify a source as the primary source. The second source serves as the backup.
  If you don’t specify a primary source, MediaConnect treats both sources with
  equal priority, and switches to the available source as needed.
  MediaConnect uses the two modes of failover in the following ways:

- In the _Merge_ mode, MediaConnect uses content from
  both sources. The flow randomly selects one of the sources to start with. If
  that source is missing a packet, the flow pulls the missing packet from the
  other source. For example, if the flow is using source A and packet 123 is
  missing, MediaConnect pulls in packet 123 from source B and continues using source A.
  In this mode, the two sources are binary identical/ST 2022-7 compliant.
- In the _Failover_ mode, if you don't specify
  a primary source, MediaConnect randomly uses one of the sources to provide content for
  the flow. If MediaConnect does not receive data from the source for 500 milliseconds,
  the flow switches to the other source, and can continue switching back and forth
  between sources as needed. If you do specify a primary source, MediaConnect uses that
  source to provide content for the flow. The flow switches to the other source if
  the primary source does not send data for 500 milliseconds, and switches back to
  the primary source as soon as data returns.

###### Note

MediaConnect doesn't support source failover on CDI flows or on entitlement
flows. For more information about creating redundancy with CDI flows, visit: [Creating a CDI flow](flows-create-cdi.md "flows-create-cdi.md"). Additionally, you
cannot add a second source to an existing flow for failover if you are using the
Zixi pull protocol.

## Failover support for source protocols in MediaConnect

The following table describes which source protocols support failover.

| Protocol                             | Does this protocol support source failover? | How many sources can be added?               | Supported failover modes         |
| ------------------------------------ | ------------------------------------------- | -------------------------------------------- | -------------------------------- |
| RIST                                 | Yes                                         | 2                                            | Merge or failover                |
| RTP                                  | Yes                                         | 2                                            | Merge or failover                |
| RTP-FEC                              | Yes                                         | 2                                            | Merge or failover                |
| SRT listener                         | Yes                                         | 2                                            | Failover only                    |
| SRT caller                           | Yes                                         | 2                                            | Failover only                    |
| Zixi pull                            | No                                          | None - Zixi pull cannot be used as a source. | Source failover is not supported |
| Zixi push                            | Yes                                         | 2                                            | Merge or failover                |
| Zixi push for AWS Elemental Link UHD | Yes                                         | 2                                            | Failover only                    |
| CDI                                  | No                                          | 1                                            | Source failover is not supported |
| ST 2110 JPEG XS                      | No                                          | 1                                            | Source failover is not supported |
| Entitlement flows                    | No                                          | 1                                            | Source failover is not supported |
