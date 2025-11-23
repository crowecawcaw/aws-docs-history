# Source failover and merge for router inputs in

MediaConnect

MediaConnect supports two types of redundancy configurations for router inputs:
**Failover** and **Merge**.

## Failover mode

In failover mode, a router input can have two sources. The router input will automatically switch
sources based on the source priority configuration. If no priority is defined, the router input will
randomly use one of the sources and will switch to the other source if the active source does not send data
for 500 milliseconds. If one source is defined as the _Primary_ source, the router
input will use the primary source and will switch to the secondary source if the primary source does not
send data for 500 milliseconds. The router input will switch back to the primary source as soon as data returns.

To create a failover router input, you specify the input type as **Failover** and provide a protocol configuration for each source. MediaConnect
treats the first source as the primary, and the second as the backup.

For instructions on how to create or update a router input, see [Creating a router I/O in MediaConnect](creating-router-io.md "creating-router-io.md") and [Updating a router I/O in MediaConnect](editing-router-io.md "editing-router-io.md").

## Merge mode

In merge mode, a router input accepts two identical, simultaneous video streams on the
same IP address but different ports. MediaConnect merges the content of the two streams at
the network packet level, allowing a graceful recovery from any single-source loss. For
example: if the router input is using source A and packet 123 is missing, MediaConnect pulls in
packet 123 from source B and continues using source A.

To create a merge router input, you specify the router input type as **Merge** and provide a protocol configuration for each source. The
two sources must be binary identical, which means that they need to have originated from
the same encoder. Additionally, if the sources use RTP protocol, they must have RTP
headers with aligned sequence numbers and they must also comply with the SMPTE ST 2022-7
standard.

When configuring a merge router input, you can also set a recovery window. This is the
size of the buffer (delay) that you want MediaConnect to maintain. A larger recovery
window means a longer delay in transmitting the stream, but more room for error
correction. A smaller recovery window means a shorter delay, but less room for error
correction.

For instructions on how to create or update a router input, see [Creating a router I/O in MediaConnect](creating-router-io.md "creating-router-io.md") and [Updating a router I/O in MediaConnect](editing-router-io.md "editing-router-io.md").

## Supported protocols

The following table describes which source protocols support failover and merge for
MediaConnect router inputs.

| Protocol     | Does this protocol support source failover? | How many sources can be added? | Supported failover modes |
| ------------ | ------------------------------------------- | ------------------------------ | ------------------------ |
| RIST         | Yes                                         | 2                              | Merge or failover        |
| RTP          | Yes                                         | 2                              | Merge or failover        |
| SRT listener | Yes                                         | 2                              | Failover only            |
| SRT caller   | Yes                                         | 2                              | Failover only            |
