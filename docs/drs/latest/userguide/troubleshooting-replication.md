

# Troubleshooting replication errors
<a name="troubleshooting-replication"></a>

Use this section to troubleshoot issues with data replication between your source servers and the AWS Elastic Disaster Recovery staging area.


| If you see... | See | 
| --- | --- | 
| Connection timeouts, port 443/1500 blocked, or need to verify network paths | [Verifying network connectivity](verifying-network-connectivity.md) | 
| "Agent not seen", "Disconnected", "Failed to authenticate", or "Failed to connect" errors | [Agent communication errors](replication-connectivity-errors.md) | 
| "Failed to launch replication server", "Failed to create staging disks", or firewall rule errors | [Replication infrastructure errors](replication-server-errors.md) | 
| "Not converging", replication lag growing, or unknown replication errors | [Replication performance errors](replication-performance-errors.md) | 
| Need to calculate bandwidth requirements or measure source server write speed | [Bandwidth requirements](comm-bandwidth-planning.md) | 

**Topics**
+ [Verifying network connectivity](verifying-network-connectivity.md)
+ [Replication errors: agent communication](replication-connectivity-errors.md)
+ [Replication infrastructure errors](replication-server-errors.md)
+ [Replication performance errors](replication-performance-errors.md)
+ [Replication bandwidth requirements](comm-bandwidth-planning.md)