

# Troubleshooting AWS Managed Microsoft AD high CPU utilization
<a name="ms_ad_troubleshooting_high_cpu"></a>

The following can help you troubleshoot high CPU issues on AWS Managed Microsoft AD domain controllers.

## Finding the root cause
<a name="ms_ad_high_cpu_root_cause"></a>

The first step in troubleshooting high CPU utilization is to analyze CloudWatch metrics to identify patterns that may explain the increased resource consumption.

### Step 1: Review Directory Service CloudWatch metrics
<a name="ms_ad_high_cpu_step1"></a>

Monitor your AWS Managed Microsoft AD performance using CloudWatch metrics to identify traffic patterns that correlate with high CPU usage. For detailed information on viewing and interpreting Directory Service metrics, see [Using CloudWatch to monitor the performance of your AWS Managed Microsoft AD domain controllers](ms_ad_monitor_dc_performance.md).

Look for shifting patterns in the following key metrics that might explain the CPU increase:
+ **DNS queries per second** – Sudden spikes may indicate DNS resolution issues or misconfigured applications.
+ **Kerberos/NTLM authentications** – Higher authentication rates from user logons or service accounts.
+ **LDAP queries per second** – Increased LDAP traffic from applications or services.

Compare current metrics with historical baselines to identify when the high CPU utilization began and correlate it with specific traffic increases. If no correlation is found in the metrics then the root cause is not an overwhelming increase in traffic. Instead the root cause is likely an inefficient LDAP query, skip to [Step 3: Capture detailed traffic analysis with Traffic Mirroring](#ms_ad_high_cpu_step3).

### Step 2: Identify source machines using VPC Flow Logs
<a name="ms_ad_high_cpu_step2"></a>

VPC Flow Logs provide an effective method to identify the source IP addresses of machines generating traffic to your domain controllers. For more information, see [Logging IP traffic using VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html). Use the destination port numbers to differentiate between services:
+ **Port 53** – DNS queries
+ **Port 88** – Kerberos authentication
+ **Port 123** – NTP clock synchronization
+ **Port 135, 49152-65535** – RPC
+ **Ports 389, 636, 3268, 3269** – LDAP queries (389 or 3268 for standard LDAP, 636 or 3269 for LDAPS)
+ **Port 445** – SMB file sharing (Group Policies)
+ **Port 464** – Kerberos password change
+ **Port 9389** – Active Directory Web Service

To enable and analyze VPC Flow Logs:
+ Enable VPC Flow Logs for the subnets containing your domain controller ENIs.
+ Filter logs by destination ports to identify traffic patterns.
+ Organize by most packets and/or most bytes over the period of time.
+ Analyze source IP addresses to determine which machines are generating the most traffic.

### Step 3: Capture detailed traffic analysis with Traffic Mirroring
<a name="ms_ad_high_cpu_step3"></a>

VPC Flow Logs provide limited information about the actual content of requests. For more detailed analysis, consider Traffic Mirroring to capture full packet data. For more information, see [Get started using Traffic Mirroring to monitor network traffic](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-getting-started.html). This is particularly useful when you need to analyze:
+ LDAP filter complexity and efficiency
+ Specific DNS query patterns
+ Authentication request details

Traffic Mirroring allows you to capture complete network packets sent to your domain controller instances, enabling deep analysis of the traffic causing high CPU utilization.

### Step 4: Investigate source applications and optimize traffic
<a name="ms_ad_high_cpu_step4"></a>

Once you've identified the source machines and traffic patterns, investigate the applications generating the traffic:
+ **Review application configurations** – Check if applications are making inefficient queries or excessive requests. Avoid hard coding the application to a single domain controller.
+ **Analyze LDAP queries** – Inefficient LDAP queries are the most common cause of high domain controller CPU. Look for complex filters that could benefit from attribute indexing.
+ **Examine DNS caching** – Verify that DNS client caching is enabled to reduce repetitive queries.
+ **Check authentication patterns** – Identify if service accounts are authenticating too frequently.

## Resolution strategies
<a name="ms_ad_high_cpu_resolution"></a>

Based on your investigation, implement appropriate optimization strategies:

### Optimize applications
<a name="ms_ad_high_cpu_optimize_apps"></a>
+ **Optimize LDAP queries** – Rewrite complex LDAP queries. Avoid setting the search base to the root of the domain and instead configure it to an OU where the objects you are searching for reside. Avoid using a search scope that performs subtree searches. Instead use a base or single level scope. Include the object class in your filter. For example, `(objectClass=user)` or `(objectClass=computer)`. Avoid using wildcards in the filter unless the attribute is indexed. Add an index if a wildcard scan is required. For more information, see [Extend your AWS Managed Microsoft AD schema](ms_ad_schema_extensions.md). Don't index everything as the indexing process also increases CPU utilization.

  ```
  # Sample LDIF code to index the email attribute
  dn: CN=mail,CN=Schema,CN=Configuration,DC=yourdomain,DC=com
  changetype: modify
  replace: searchFlags
  searchFlags: 1
  ```
+ **Enable DNS client caching** – Configure clients to cache DNS responses locally to reduce server load.
+ **Implement connection pooling** – Configure applications to reuse LDAP connections rather than creating new ones for each query.

### Scale your directory infrastructure
<a name="ms_ad_high_cpu_scale"></a>

If traffic optimization doesn't resolve the high CPU utilization:
+ **Add more domain controllers** – Scale out by deploying additional domain controllers to distribute the load. For more information, see [Deploying additional domain controllers for your AWS Managed Microsoft AD](ms_ad_deploy_additional_dcs.md).
+ **Upgrade to Enterprise Edition** – If using Standard Edition, upgrade to Enterprise Edition for increased CPU capacity and performance. For more information, see [Upgrading your AWS Managed Microsoft AD](ms_ad_upgrade_edition.md). If already using Enterprise Edition, Contact [AWS Support](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html) for increased capacity.

For pricing information about AWS Managed Microsoft AD editions, see [Directory Service Pricing](https://aws.amazon.com/directoryservice/pricing/#Comparison_Table).