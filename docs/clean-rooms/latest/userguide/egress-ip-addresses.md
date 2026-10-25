

# AWS Clean Rooms egress IP address ranges
<a name="egress-ip-addresses"></a>

When AWS Clean Rooms reads data from an external data source, Databricks or Snowflake, the request originates from a fixed set of AWS Clean Rooms egress IP addresses. These IP address ranges are the same for all external data sources that AWS Clean Rooms supports.

If your external data source restricts inbound access with an IP allowlist, add the AWS Clean Rooms egress IP address range for your Region to that allowlist so that AWS Clean Rooms can reach your data while other traffic remains blocked.

The following table lists the egress IP address range that AWS Clean Rooms uses in each AWS Region.


| AWS Region | Region name | IP address range (CIDR) | 
| --- | --- | --- | 
| us-east-1 | US East (N. Virginia) | 66.36.0.0/24 | 
| us-east-2 | US East (Ohio) | 66.36.1.0/24 | 
| us-west-2 | US West (Oregon) | 66.36.2.0/24 | 
| eu-west-1 | Europe (Ireland) | 66.36.3.0/24 | 
| eu-central-1 | Europe (Frankfurt) | 66.36.4.0/24 | 
| eu-north-1 | Europe (Stockholm) | 66.36.5.0/24 | 
| ap-northeast-1 | Asia Pacific (Tokyo) | 66.36.6.0/24 | 
| ap-northeast-2 | Asia Pacific (Seoul) | 66.36.7.0/24 | 
| eu-west-2 | Europe (London) | 66.36.8.0/24 | 
| ap-southeast-1 | Asia Pacific (Singapore) | 66.36.9.0/24 | 
| ap-southeast-2 | Asia Pacific (Sydney) | 66.36.10.0/24 | 