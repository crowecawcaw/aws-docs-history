AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Network data collection attempts

When a new server is discovered, the collector attempts each configured credential for
each IP address. After the collector finds a valid credential, it only uses that
credential. After two consecutive failures, the collector attempts to collect networking
data for a server after 30 minutes, 2 hours, 8 hours, and then 24 hours. After 6 failed
attempts, the collector continues to try all configured credentials once every day. To
resolve the issue, either edit the current credentials or add additional ones by
choosing **Edit collector**, or make changes to the target server
being monitored.
