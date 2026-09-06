

# Troubleshooting VPC networking
<a name="vpc-troubleshooting-guide"></a>

**Topics**
+ [Network monitoring and troubleshooting](#vpc-network-monitoring-troubleshooting)
+ [Configuration troubleshooting](#vpc-configuration-troubleshooting)

## Network monitoring and troubleshooting
<a name="vpc-network-monitoring-troubleshooting"></a>

### CloudTrail logging
<a name="vpc-cloudtrail"></a>

All Configuration API operations and workflow runs using VPC networking are logged in CloudTrail. Use CloudTrail to audit configuration changes and track which runs use VPC networking.

### Troubleshooting with ENI flow logs
<a name="vpc-flow-logs-troubleshooting"></a>

When your workflow runs access external resources over the internet, you can use VPC Flow Logs to verify connectivity and diagnose issues. HealthOmics provisions elastic network interfaces (ENIs) in your VPC subnets to route traffic from your workflow tasks. By examining flow logs on these ENIs, you can trace network traffic to and from external destinations.

**Cost management for VPC Flow Logs**  
VPC Flow Logs can incur significant costs, especially at the VPC level. To minimize costs:  
**Delete flow logs after troubleshooting.** Once you've resolved connectivity issues, delete the flow log to stop incurring charges.
**Use Amazon S3 instead of CloudWatch Logs for long-term storage.** Amazon S3 storage is significantly cheaper than CloudWatch Logs. Configure flow logs to publish to Amazon S3 if you need to retain logs for compliance or security analysis.
**Set CloudWatch Logs retention policies.** If using CloudWatch Logs, configure automatic log expiration (for example, 7 days) to prevent indefinite storage costs.
**Use ENI-level flow logs for troubleshooting.** For one-time debugging, create flow logs on the specific customer ENI rather than the entire VPC.

#### Setting up flow logs for troubleshooting
<a name="vpc-flow-logs-setup"></a>

**Option 1: VPC-level flow logs (for ongoing monitoring)**

Enable flow logs on your VPC to automatically capture traffic from all HealthOmics workflow runs. This is best when you have many workflow runs and want comprehensive visibility without tracking individual ENIs.

1. **Enable VPC Flow Logs.** In the Amazon VPC console:

   1. Choose **Your VPCs** and select the VPC used in your HealthOmics configuration

   1. Choose the **Flow logs** tab

   1. Choose **Create flow log**

   1. Configure the flow log to capture **All** traffic (both accepted and rejected)

   1. Select CloudWatch Logs as the destination for easier querying

1. **Start a workflow run.** Start a workflow run with VPC networking enabled. Note the run ID and start time for filtering flow logs later.

Query flow logs using CloudWatch Logs Insights by time window, destination IP, or traffic patterns. You don't need to identify specific ENI IDs.

**Option 2: ENI-level flow logs (for targeted troubleshooting)**

Enable flow logs on specific ENIs when you have only a few HealthOmics ENIs in your account. This is the most cost-effective approach and makes it easy to isolate traffic for specific workflow runs.

1. **Find the customer ENI.** In the Amazon EC2 console:

   1. Choose **Network Interfaces**

   1. Filter by tag `Service: HealthOmics` to show only ENIs created by HealthOmics

   1. Optionally, further filter by the subnet ID from your HealthOmics configuration

   1. Note the ENI ID and private IP address

1. **Enable flow logs on the ENI.**

   1. Select the ENI and choose the **Flow logs** tab

   1. Choose **Create flow log**

   1. Configure the flow log to capture **All** traffic

   1. Select CloudWatch Logs as the destination

**Note**  
Flow logs only capture traffic from the time they are enabled. For VPC-level flow logs, enable them before running workflows. For ENI-level flow logs, once enabled on an ENI, the same flow log will capture traffic for all future workflow runs that use that ENI.

#### Understanding VPC Flow Log format
<a name="vpc-flow-logs-analyzing"></a>

VPC Flow Logs use a space-separated format with the following fields:

```
version account_id interface_id srcaddr dstaddr srcport dstport protocol packets bytes start end action log_status
```

**Field descriptions:**
+ **version** — Flow log format version (typically 2)
+ **account\_id** — Your AWS account ID
+ **interface\_id** — The ENI ID (for example, eni-0e57c5476efeac402)
+ **srcaddr** — Source IP address
+ **dstaddr** — Destination IP address
+ **srcport** — Source port number
+ **dstport** — Destination port number
+ **protocol** — IANA protocol number (6=TCP, 17=UDP, 1=ICMP)
+ **packets** — Number of packets in the flow
+ **bytes** — Number of bytes in the flow
+ **start** — Flow start time (Unix timestamp)
+ **end** — Flow end time (Unix timestamp)
+ **action** — ACCEPT or REJECT
+ **log\_status** — OK, NODATA, or SKIPDATA

**Example flow log entries:**

```
2 074296239033 eni-0e57c5476efeac402 10.0.130.58 13.226.238.96 40565 443 6 13 1502 1774338927 1774338929 ACCEPT OK
2 074296239033 eni-0e57c5476efeac402 13.226.238.96 10.0.130.58 443 40565 6 8 1024 1774338928 1774338930 ACCEPT OK
```

These entries show successful bidirectional HTTPS communication. Key IPs: **10.0.130.58** is the customer ENI created by HealthOmics in your account, and **13.226.238.96** is the external public domain your workflow is accessing. The first entry is outbound traffic, and the second is the return traffic. Both show ACCEPT, indicating the traffic was allowed by security groups.

#### Querying flow logs in CloudWatch Logs Insights
<a name="vpc-flow-logs-querying"></a>

When flow logs are published to CloudWatch Logs, use CloudWatch Logs Insights to query and analyze the data.

**Find rejected traffic (start here)**

```
fields @timestamp, interfaceId, srcAddr, dstAddr, srcPort, dstPort, protocol, action
| filter action = "REJECT"
| sort @timestamp desc
```

If this returns results, you may have a connectivity issue. The rejected entries show which traffic is being blocked by security groups or network ACLs.

**Find traffic to a specific external IP**

First, resolve the domain to an IP address using `nslookup` or `dig`:

```
$ nslookup ftp.ncbi.nlm.nih.gov
Server:  127.53.53.53
Address: 127.53.53.53#53

Non-authoritative answer:
ftp.ncbi.nlm.nih.gov    canonical name = ftp.wip.ncbi.nlm.nih.gov.
Name:    ftp.wip.ncbi.nlm.nih.gov
Address: 130.14.250.10
Name:    ftp.wip.ncbi.nlm.nih.gov
Address: 130.14.250.11
```

The "Server" and "Address" at the top are your DNS resolver. The addresses under "Non-authoritative answer" (130.14.250.10 and 130.14.250.11) are the actual IPs for the domain.

Query flow logs using a prefix to match any IP in that range:

```
fields @timestamp, interfaceId, srcAddr, dstAddr, srcPort, dstPort, protocol, action
| filter dstAddr like "130.14.250"
| sort @timestamp desc
```

This matches any IP starting with 130.14.250, capturing traffic to all IPs in that subnet.

**Find HTTPS traffic to external destinations**

```
fields @timestamp, interfaceId, srcAddr, dstAddr, srcPort, dstPort, protocol, action
| filter dstPort = 443 and protocol = 6
| filter not (dstAddr like /^10\./ or dstAddr like /^172\./ or dstAddr like /^192\.168\./)
| sort @timestamp desc
```

The second filter excludes private IP ranges, showing only traffic to external (public) destinations.

**Note**  
Protocol numbers: 6=TCP, 17=UDP, 1=ICMP. For load-balanced services (for example, CloudFront), DNS may return different IPs, so filter by destination port instead of IP address.

#### Common flow log patterns and issues
<a name="vpc-flow-logs-common-issues"></a>

**Outbound traffic rejected**  

```
Outbound: 2 074296239033 eni-0e57c5476efeac402 10.0.130.58 13.226.238.96 40565 443 6 1 60 1774338927 1774338929 REJECT OK
```
**Cause:** Security group doesn't allow outbound traffic to the destination port or IP range.  
**Solution:** Add an outbound rule to your security group:  
+ For HTTPS: Allow TCP port 443 to 0.0.0.0/0
+ For HTTP: Allow TCP port 80 to 0.0.0.0/0
+ For broader access: Allow all TCP/UDP to 0.0.0.0/0

**Return traffic rejected**  

```
Outbound: 2 074296239033 eni-0e57c5476efeac402 10.0.130.58 8.8.8.8 54321 53 17 1 64 1774338927 1774338929 ACCEPT OK
Return:   2 074296239033 eni-0e57c5476efeac402 8.8.8.8 10.0.130.58 53 54321 17 1 64 1774338928 1774338930 REJECT OK
```
**Cause:** Network ACL is blocking return traffic. Unlike security groups (stateful), network ACLs are stateless and require explicit rules for both directions.  
**Solution:** In the VPC console, check your subnet's network ACL and verify inbound rules allow traffic on ephemeral ports (1024-65535) from external sources. Add rule if needed: Allow TCP/UDP ports 1024-65535 from 0.0.0.0/0

**Missing return traffic**  

```
Outbound: 2 074296239033 eni-0e57c5476efeac402 10.0.130.58 8.8.8.8 54321 53 17 1 64 1774338927 1774338929 ACCEPT OK
```
**Cause:** NAT Gateway/Internet Gateway not configured properly, or ENI doesn't have connectivity to internet.  
**Solution:**  
+ Verify route table has route to NAT Gateway (0.0.0.0/0 → nat-xxxxx)
+ Verify NAT Gateway is in AVAILABLE state with an Elastic IP
+ Check NAT Gateway is in a public subnet with route to Internet Gateway

**No flow log entries for expected traffic**  
**Cause:** Traffic not reaching the ENI, or flow logs not configured correctly.  
**Solution:**  
+ Verify flow logs are enabled and configured to capture all traffic
+ Check workflow logs in CloudWatch Logs to confirm the workflow is attempting to access the external resource
+ Verify route table has route to NAT Gateway (0.0.0.0/0 → nat-xxxxx)
+ Verify NAT Gateway is in AVAILABLE state with an Elastic IP

#### Best practices for flow log troubleshooting
<a name="vpc-flow-logs-best-practices"></a>

1. **Enable flow logs before starting troubleshooting.** Flow logs only capture traffic from the time they are enabled. Enable them on all subnets in your HealthOmics configuration before running workflows.

1. **Use CloudWatch Logs Insights for analysis.** CloudWatch Logs Insights provides powerful querying capabilities for flow logs. Save commonly used queries for quick access.

1. **Filter by time window.** Narrow your flow log queries to the specific time window when your workflow run was active to reduce noise and improve query performance.

1. **Look for both directions of traffic.** Always verify that both outbound and return traffic show ACCEPT. A connection requires bidirectional communication.

1. **Document your findings.** When troubleshooting connectivity issues, document the customer ENI ID, IP addresses, ports, and flow log entries. This information is valuable for support cases and future troubleshooting.

1. **Test with a simple workflow first.** Before running complex workflows, test connectivity with a simple workflow that attempts to access the external resource and logs the result. This helps isolate network issues from workflow logic issues.

## Configuration troubleshooting
<a name="vpc-configuration-troubleshooting"></a>

### Configuration stuck in CREATING status
<a name="vpc-ts-creating-status"></a>

**Cause:** Network resource provisioning can take several minutes.

**Solution:** Wait up to 10 minutes. If the status doesn't change to ACTIVE, check the following:
+ Your subnets and security groups exist and are in the same VPC.
+ You have the required IAM permissions.
+ The service-linked role was created successfully.

### Run fails to start with VPC networking
<a name="vpc-ts-run-fails"></a>

**Cause:** The configuration might not be ACTIVE, or there might be network connectivity issues.

**Solution:**
+ Verify that the configuration status is ACTIVE by using `GetConfiguration`.
+ Check that security group rules allow the required outbound traffic.
+ Ensure that subnets are in Availability Zones where HealthOmics operates.

### Cannot delete configuration
<a name="vpc-ts-delete-config"></a>

**Cause:** The configuration is in use by active workflow runs.

**Solution:** Wait for all runs using the configuration to complete, then retry the deletion.

### Cannot delete service-linked role
<a name="vpc-ts-delete-slr"></a>

**Cause:** Active VPC configurations exist in your account.

**Solution:** Delete all VPC configurations first, then delete the service-linked role.

### Workflow cannot connect to external resource
<a name="vpc-ts-connectivity"></a>

**Cause:** Security group or route table misconfiguration.

**Solution:**

1. Enable VPC Flow Logs to identify rejected packets

1. Check security group outbound rules allow traffic to the destination

1. Verify route table has a route to NAT Gateway (0.0.0.0/0 → nat-xxxxxx)

1. For cross-Region AWS service access, ensure the destination Region is reachable

1. Test connectivity from an Amazon EC2 instance in the same subnet

### Network performance issues
<a name="vpc-ts-performance"></a>

**Symptom:** Slow data transfer or workflow timeouts.

**Cause:** Network throughput limitations or NAT Gateway saturation.

**Solution:**
+ Network throughput begins at 10 Gbps per ENI and scales up to 100 Gbps over a 60-minute period with sustained traffic
+ For workflows with immediate high-throughput requirements, please contact AWS Support
+ Monitor NAT Gateway metrics in CloudWatch to identify saturation
+ Consider deploying additional NAT Gateways in multiple Availability Zones for higher throughput

### Workflow cannot reach the internet
<a name="vpc-ts-no-internet"></a>

**Cause:** The private subnets might not have a route to a NAT gateway, or security group rules might be blocking outbound traffic.

**Solution:**
+ Verify that the route table for your private subnets includes a route to a NAT gateway (0.0.0.0/0 → nat-xxxxxxxxx).
+ Check that security group rules allow outbound traffic on the required ports.
+ Verify that the NAT gateway is in a public subnet with a route to an internet gateway.

### Workflow run fails with connectivity errors
<a name="vpc-ts-connectivity-errors"></a>

**Cause:** Network traffic might be blocked or misconfigured.

**Solution:**

1. Verify that the configuration is still in ACTIVE status by using `GetConfiguration`.

1. Create a VPC flow log on the ENIs in your VPC to inspect traffic. For more information, see [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) in the *Amazon VPC User Guide*.

1. Check the flow log for REJECT entries. If you see rejected packets, update your security group rules to allow the required outbound traffic.

1. If the flow log does not reveal a root cause, contact AWS Support.