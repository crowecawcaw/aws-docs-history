# Amazon DCV server sessions

Counters in this set provide information about a single session.
There's one instance of this counter set for each created session, whether a user is connected or not.

If the administrator closes a session, the corresponding instance is removed; if the administrator
re-creates a session with the same name, all the counters restart from zero.

| Counter name         | Description                                                                                                           | Unit    |
| -------------------- | --------------------------------------------------------------------------------------------------------------------- | ------- |
| Session Duration sec | Total number of seconds the session has been open                                                                     | Seconds |
| Total Pixels         | Number of pixels in the display area, which is the sum of the number of pixels across all the displays in the session | Pixels  |
| Display Count        | Number of displays in the session                                                                                     | Count   |

The following counters are the same as the ones in **Amazon DCV Server** counter set, with minor differences in the description:

| Counter name                 | Description                                                                                                         |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Active Connections           | Number of active connections to the session instance                                                                |
| Total Connections            | Incrementing number of connections to the session instance, including active, reconnected and disconnected clients  |
| Idle Disconnections          | Incrementing number of connections to the session instance that were disconnected because of inactivity             |
| Ungraceful Disconnections    | Incrementing number of connections to the session instance that were disconnected because of an error               |
| Receive Rate bits/sec        | Rate in bits per second at which data is received within the session                                                |
| Received Bytes               | Total number of bytes received since session start                                                                  |
| Send Rate bits/sec           | Rate in bits per second at which data is sent within the session                                                    |
| Sent Bytes                   | Total number of bytes sent since session start                                                                      |
| HTTP Download Rate bits/sec  | Bandwidth in bits per second for outgoing HTTP data within the session                                              |
| HTTP Downloaded Bytes        | Total number of bytes sent over HTTP within the session                                                             |
| Round-Trip Time ms           | Average round-trip latency between server and clients within the session, in milliseconds                           |
| Minimum Round-Trip Time ms   | Minimum round-trip latency detected since the session was established, in milliseconds                              |
| Total WebSocket Connections  | Incrementing number of WebSocket connections to the server, including active, reconnected and disconnected clients. |
| Active WebSocket Connections | Number of active WebSocket connections to the server.                                                               |
| Total QUIC Connections       | Incrementing number of QUIC connections to the server, including active, reconnected and disconnected clients.      |
| Active QUIC Connections      | Number of active QUIC connections to the server.                                                                    |
