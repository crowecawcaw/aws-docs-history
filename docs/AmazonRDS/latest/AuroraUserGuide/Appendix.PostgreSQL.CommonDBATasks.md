# Dead connection

handling in PostgreSQL

Dead connections occur when a database session remains active on the server despite the
client application having abandoned or terminated abnormally. This situation typically arises
when client processes crash or terminate unexpectedly without properly closing their database
connections or canceling ongoing requests.

PostgreSQL efficiently identifies and cleans up dead connections when server processes are
idle or attempt to send data to clients. However, detection is challenging for sessions that are
idle, waiting for client input, or actively running queries. To handle these scenarios,
PostgreSQL provides `tcp_keepalives_*`, `tcp_user_timeout`, and
`client_connection_check_interval` parameters.

###### Topics

- [Understanding TCP keepalive](#Appendix.PostgreSQL.CommonDBATasks.DeadConnectionHandling.Understanding "#Appendix.PostgreSQL.CommonDBATasks.DeadConnectionHandling.Understanding")
- [Key TCP
  keepalive parameters in Aurora PostgreSQL](#Appendix.PostgreSQL.CommonDBATasks.DeadConnectionHandling.Parameters "#Appendix.PostgreSQL.CommonDBATasks.DeadConnectionHandling.Parameters")
- [Use cases
  for TCP keepalive settings](#Appendix.PostgreSQL.CommonDBATasks.DeadConnectionHandling.UseCases "#Appendix.PostgreSQL.CommonDBATasks.DeadConnectionHandling.UseCases")
- [Best
  practices](#Appendix.PostgreSQL.CommonDBATasks.DeadConnectionHandling.BestPractices "#Appendix.PostgreSQL.CommonDBATasks.DeadConnectionHandling.BestPractices")

## Understanding TCP keepalive

TCP Keepalive is a protocol-level mechanism that helps maintain and verify connection
integrity. Each TCP connection maintains kernel-level settings that govern keepalive behavior.
When the keepalive timer expires, the system does the following:

- Sends a probe packet with no data and the ACK flag set.
- Expects a response from the remote endpoint according to TCP/IP specifications.
- Manages connection state based on the response or lack thereof.

## Key TCP

keepalive parameters in Aurora PostgreSQL

| Parameter                          | Description                                                                                                                                                  | Default values |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tcp_keepalives_idle`              | Specifies number of seconds of inactivity before sending keepalive message.                                                                                  | 300            |
| `tcp_keepalives_interval`          | Specifies number of seconds between retransmissions of unacknowledged keepalive messages.                                                                    | 30             |
| `tcp_keepalives_count`             | Maximum lost keepalive messages before declaring connection dead                                                                                             | 2              |
| `tcp_user_timeout`                 | Specifies how long (in Milliseconds) unacknowledged data can remain before forcibly closing the connection.                                                  | 0              |
| `client_connection_check_interval` | Sets the interval (in Milliseconds) for checking client connection status during long-running queries. This ensures quicker detection of closed connections. | 0              | ## Use cases for TCP keepalive settings ### Keeping idle sessions alive To prevent idle connections from being terminated by firewalls or routers due to inactivity: <br>• Configure `tcp_keepalives_idle` to send keepalive packets at regular intervals. ### Detecting dead connections To detect dead connections promptly: <br>• Adjust `tcp_keepalives_idle`, `tcp_keepalives_interval`, and `tcp_keepalives_count`. For example, with Aurora PostgreSQL defaults, it takes about a minute (2 probes × 30 seconds) to detect a dead connection. Lowering these values can speed up detection. <br>• Use `tcp_user_timeout` to specify the maximum wait time for an acknowledgment. TCP keepalive settings help the kernel detect dead connections, but PostgreSQL may not act until the socket is used. If a session is running a long query, dead connections might only be detected after query completion. In PostgreSQL 14 and higher versions, `client_connection_check_interval` can expedite dead connection detection by periodically polling the socket during query execution. ## Best practices <br>• **Set reasonable keepalive intervals:** Tune `tcp_user_timeout`, `tcp_keepalives_idle`, `tcp_keepalives_count` and `tcp_keepalives_interval` to balance detection speed and resource use. <br>• **Optimize for your environment:** Align settings with network behavior, firewall policies, and session needs. <br>• **Leverage PostgreSQL features:** Use `client_connection_check_interval` in PostgreSQL 14 and higher versions for efficient connection checks. |
