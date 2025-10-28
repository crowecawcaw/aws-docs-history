# Amazon DCV server

This counter set contains global statistics about the DCV Server service on the host. It also contains an aggregated variant of many counters
that are also available in the other counter sets, providing a way to access the information aggregated over the full lifetime of the server, and with a static path
(you don’t have to retrieve session or connection identifiers in order to read the counters in this counter set).

###### Note

the aggregated instance from one of the other counter sets (e.g. "\DCV Server Connections(\_Total)\Sent Bytes)" returns the sum over all active connections,
while the global counter is accumulated since the server started, and includes connections that have been closed.

| Counter name                 | Description                                                                                                         | Unit         | Notes                                                                  |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------ | ---------------------------------------------------------------------- |
| Active Sessions              | Number of active sessions on the host                                                                               | Count        |                                                                        |
| Total Sessions               | Incrementing number of sessions created on the host, including the session that have been closed                    | Count        |                                                                        |
| Active Connections           | Number of active connections to the server                                                                          | Count        |                                                                        |
| Total Connections            | Incrementing number of connections to the server, including active, reconnected and disconnected clients            | Count        |                                                                        |
| Idle Disconnections          | Incrementing number of connections that were disconnected because of inactivity                                     | Count        |                                                                        |
| Receive Rate bits/sec        | Rate in bits per second at which data is received by the server                                                     | Bits/sec     |                                                                        |
| Received Bytes               | Total number of bytes received since the service was started                                                        | Bytes        |                                                                        |
| Send Rate bits/sec           | Rate in bits per second at which data is sent by the server                                                         | Bits/sec     |                                                                        |
| Sent Bytes                   | Total number of bytes sent since the service was started                                                            | Bytes        |                                                                        |
| HTTP Download Rate bits/sec  | Bandwidth in bits per second for outgoing HTTP traffic                                                              | Bits/sec     | Client-to-server traffic for file storage is counted in Receive Rate   |
| HTTP Downloaded Bytes        | Total number of bytes sent over HTTP since the service was started                                                  | Bytes        | Client-to-server traffic for file storage is counted in Received Bytes |
| Round-Trip Time ms           | Average round-trip latency between server and clients, in milliseconds                                              | Milliseconds | Measured and updated once every 5 seconds                              |
| Minimum Round-Trip Time ms   | Minimum round-trip latency detected since the server started, in milliseconds                                       | Milliseconds | Updated once every 5 seconds                                           |
| Total WebSocket Connections  | Incrementing number of WebSocket connections to the server, including active, reconnected and disconnected clients. | Count        |                                                                        |
| Active WebSocket Connections | Number of active WebSocket connections to the server.                                                               | Count        |                                                                        |
| Total QUIC Connections       | Incrementing number of QUIC connections to the server, including active, reconnected and disconnected clients.      | Count        |                                                                        |
| Active QUIC Connections      | Number of active QUIC connections to the server.                                                                    | Count        |                                                                        |
