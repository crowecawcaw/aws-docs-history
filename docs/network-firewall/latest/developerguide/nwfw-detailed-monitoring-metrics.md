# Flow and alert log metrics in the firewall monitoring dashboard

The firewall monitoring dashboard provides multiple options for viewing key metrics about your firewall.

Availability of graphs and other visualizations in the dashboard depend on your logging configuration.
If you have not reviewed the [prerequisites](nwfw-detailed-monitoring.md#nwfw-detailed-monitoring-prerequisites "nwfw-detailed-monitoring.md#nwfw-detailed-monitoring-prerequisites"), do that now.

The following table describes the available visualizations and metrics for each log type:

| Log type   | Metric visualization                | Description                                                                                 |
| ---------- | ----------------------------------- | ------------------------------------------------------------------------------------------- |
| Flow logs  | Firewall traffic summary            | Total number of connections and unique destinations observed.                               |
| Flow logs  | Top long-lived TCP flows            | TCP connections that were active for more than 350 seconds.                                 |
| Flow logs  | Top TCP flows (SYN without SYN-ACK) | TCP connections showing potential connectivity issues or scanning activity.                 |
| Flow logs  | Top talkers                         | Most active source and destination IP addresses, ports, and domains observed in traffic.    |
| Flow logs  | Top Source IP by Packets            | Source IP addresses observed to send the highest number of packets.                         |
| Flow logs  | Top Source IP by Bytes              | Source IP addresses observed to send the most data, measured in bytes.                      |
| Flow logs  | Top Destination IP by Packets       | Destination IP addresses observed to receive the highest number of packets.                 |
| Flow logs  | Top Destination IP by Bytes         | Destination IP addresses observed to receive the most data, measured in bytes.              |
| Alert logs | Top PrivateLink Endpoint Candidates | Most frequent suspected PrivateLink endpoints observed in traffic.                          |
| Alert logs | Firewall traffic summary            | Total number of rejected connections and dropped connections.                               |
| Alert logs | Top rejected traffic                | Most frequently rejected domains, IP addresses, and ports.                                  |
| Alert logs | Top dropped traffic                 | Most frequently dropped domains, IP addresses, and ports.                                   |
| Alert logs | Top alerted host headers            | Most frequent HTTP host headers observed in traffic.                                        |
| Alert logs | Top dropped/rejected host headers   | Most frequent HTTP host headers observed in dropped and rejected traffic.                   |
| Alert logs | Top HTTP URI paths                  | Most frequently accessed HTTP URI paths.                                                    |
| Alert logs | Top HTTP User-Agents                | Most common HTTP User-Agent strings observed.                                               |
| Alert logs | Top alerted TLS SNI                 | Most frequent Server Name Indication values observed in TLS traffic.                        |
| Alert logs | Top dropped/rejected TLS SNI        | Most frequently dropped and rejected Server Name Indication values observed in TLS traffic. |
