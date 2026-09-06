

# Replication performance errors
<a name="replication-performance-errors"></a>

This topic covers replication errors related to performance, convergence, and lag in AWS Elastic Disaster Recovery.

**Topics**
+ [Error: Replication not converging](#common-not-converging)
+ [Replication lag increasing](#Replication-Lag-Issues)
+ [Error: Unknown data replication error](#common-unknown-data-replication-error)
+ [Error: Failed to configure replication software](#common-configure-replication-software)
+ [Error: Failed to download replication software](#common-download-replication-software)
+ [Error: Failed to establish communication with recovery instance](#common-communication-recovery-instance)
+ [Error: Failed to pair replication agent with replication server](#common-pair-replication-agent-server)

## Error: Replication not converging
<a name="common-not-converging"></a>

**Error:** `NOT_CONVERGING` status

**Cause:** The rate of data changes on the source server exceeds the available replication bandwidth. Elastic Disaster Recovery cannot catch up with the ongoing writes.

**Resolution:**

------
#### [ Console ]
+ Check **Replication lag** and **ETA** in the Elastic Disaster Recovery console.
+ Check the **Disk settings** tab. Consider upgrading the staging disk type for higher throughput (for example, gp2 to gp3).

------
#### [ CLI ]

Run the following command to check replication lag and ETA:

```
aws drs describe-source-servers \
    --filters sourceServerIDs={{SOURCE_SERVER_ID}}
```

Run the following command to check disk type, IOPS, and throughput configuration:

```
aws drs get-replication-configuration \
    --source-server-id {{SOURCE_SERVER_ID}}
```

------

Additionally:
+ Calculate required bandwidth. For more information, see [bandwidth requirements](comm-bandwidth-planning.md#Calculating-Bandwidth).
+ Run a bandwidth test. For more information, see [network bandwidth test](Replication-Related-FAQ.md#perform-connectivity-bandwidth-test).

**Note**  
Changing the staging disk type might affect replication costs. Review Amazon EBS pricing before making changes.

## Replication lag increasing
<a name="Replication-Lag-Issues"></a>

**Symptom:** Replication lag grows over time or spikes unexpectedly.

**Causes:**
+ Source server is down or the agent is not running.
+ TCP port 1500 is blocked outbound from the source server to the replication server.
+ Source server MAC address changed. This requires agent reinstallation.
+ Source server recently rebooted or Elastic Disaster Recovery services restarted. Disks are re-read, and lag grows temporarily until the process completes.
+ Source server experienced a spike in write operations. Lag grows until Elastic Disaster Recovery flushes the backlog.
+ Insufficient bandwidth for the combined write throughput of all source servers.

**Resolution:**
+ Verify the agent is running and the source server is connected.
+ Verify TCP port 1500 connectivity from the source server to the replication server.
+ If the lag is temporary (post-reboot or write spike), wait for replication to converge.
+ If lag persists, check bandwidth. For more information, see [bandwidth requirements](comm-bandwidth-planning.md#Calculating-Bandwidth).
+ Consider upgrading the staging disk type for higher throughput.

## Error: Unknown data replication error
<a name="common-unknown-data-replication-error"></a>

**Error:** `unknown_error`

**Cause:** An unclassified replication error. Multiple root causes are possible.

**Resolution:**
+ Check connectivity between the source server and the replication server.
+ Check AWS CloudTrail for API throttling errors.
+ Monitor replication server performance (CPU, memory, disk I/O) in Amazon CloudWatch.
+ Verify network bandwidth is adequate. For more information, see [bandwidth requirements](comm-bandwidth-planning.md#Calculating-Bandwidth).
+ Check agent logs. For more information, see [Agent logs and diagnostics](agent-diagnostics.md#agent-log-locations).
+ If the error persists, contact AWS Support with the agent logs and source server ID.

## Error: Failed to configure replication software
<a name="common-configure-replication-software"></a>

**Error:** `FAILED_TO_CONFIGURE_REPLICATION_SOFTWARE`

**Cause:** An internal error occurred during replication software configuration. This is typically transient.

**Resolution:** Retry the operation. If the error persists, contact AWS Support.

## Error: Failed to download replication software
<a name="common-download-replication-software"></a>

**Error:** `FAILED_TO_DOWNLOAD_REPLICATION_SOFTWARE_TO_FAILBACK_CLIENT`

**Cause:** The Failback Client cannot download replication software from Amazon S3. This indicates connectivity issues to the Amazon S3 endpoint, or a proxy or network security appliance is filtering traffic.

**Resolution:**
+ Verify connectivity to the Amazon S3 endpoint. For more information, see [TCP port 443 troubleshooting](verifying-network-connectivity.md).
+ Check for a proxy or network security appliance intercepting or blocking the download.
+ Retry the operation.

## Error: Failed to establish communication with recovery instance
<a name="common-communication-recovery-instance"></a>

**Error:** `FAILED_TO_ESTABLISH_RECOVERY_INSTANCE_COMMUNICATION`

**Cause:** The Failback Client cannot communicate with the recovery instance.

**Resolution:**
+ If you use a public network (no VPN or ), ensure the recovery instance has a public IP address. By default, Elastic Disaster Recovery launch templates disable public IP assignment.
+ If you use a private network, verify routing between the Failback Client and the recovery instance.
+ Check that the security group on the recovery instance allows inbound traffic on the required ports.

## Error: Failed to pair replication agent with replication server
<a name="common-pair-replication-agent-server"></a>

**Error:** Failed to pair replication agent with replication server

**Cause:** The replication agent, replication server, and Elastic Disaster Recovery endpoint cannot establish a three-way communication channel.

**Resolution:**
+ Verify connectivity between the agent, the replication server, and the Elastic Disaster Recovery endpoint.
+ If the error persists, contact AWS Support.