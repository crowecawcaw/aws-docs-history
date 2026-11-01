

# Limits
<a name="lgw-limits"></a>

The following limits apply to a local gateway and its route tables.

**Local gateway capacity quotas**  
These limits depend on the workloads that you run on your Outpost. Calculate both counts before you add workloads, because the local gateway returns no error when you exceed them. The following section explains how to calculate each count.


| Limit | Maximum | 
| --- | --- | 
| IP addresses per local gateway | 8,192 | 
| BGP advertisements per local gateway | 300 | 

## Calculate your IP address and BGP advertisement counts
<a name="lgw-calculate-ip-bgp"></a>

**IP addresses**  
How you count your IP addresses depends on the route mode of your local gateway. With customer-owned IP (CoIP) routing, your count is the number of CoIP addresses that you have associated with instances on your Outpost. With direct VPC routing, calculate your count as follows.

Each IP address on your Outpost counts once toward the limit, whatever network interface it is on. To calculate your count, add up the private IPv4 addresses on every network interface on your Outpost, including the primary address and every secondary address. A network interface with one primary address and nine secondary addresses counts as ten. The count includes the addresses on the network interfaces of your Amazon EC2 instances and the address that each Amazon EKS pod receives when your cluster assigns pods their own IP addresses, for example with the Amazon VPC CNI plugin. Reattaching a network interface between instances does not change your count, because the addresses stay the same. Reattaching is a configuration change, so the local gateway does not apply it while you are over the limit.

For example, 100 instances with one network interface and one private IP address each use 100 addresses. If those instances are Amazon EKS worker nodes and each runs 30 pods with their own IP addresses, the count is 100 plus 3,000, which is 3,100. To count the addresses in your Outpost subnets with the AWS CLI, run the following command, listing each Outpost subnet ID.

```
aws ec2 describe-network-interfaces \
  --filters Name=subnet-id,Values={{subnet-0example1}},{{subnet-0example2}} \
  --query 'length(NetworkInterfaces[].PrivateIpAddresses[])'
```

If you exceed the limit, the local gateway freezes the configuration at the last known valid state under the limit and applies no new changes until the configuration is back under the limit.

**BGP advertisements**  
Each prefix that the Outpost advertises to your local network devices counts once toward the limit. With direct VPC routing, the Outpost advertises the subnets on your Outpost that have a route in the subnet route table targeting the local gateway. With customer-owned IP (CoIP) routing, it advertises the address ranges of your customer-owned IP address pool. Subnets without a route that targets the local gateway are not advertised and do not count. For example, 20 subnets with a route that targets the local gateway and one CoIP pool range advertised as a single prefix make 21 advertisements. If you exceed the limit, some advertised prefixes might not be applied.

**Local gateway configuration quotas**  
These limits apply to how you configure a local gateway and its route tables. Unlike the capacity quotas, the local gateway returns an error when you try to exceed one of these limits, so you know immediately when you reach one.


| Limit | Maximum | 
| --- | --- | 
| Local gateway route tables per local gateway | 10 | 
| VIF groups per local gateway | 10 | 
| Routes that target a VIF group per local gateway route table | 100 | 
| VIFs per VIF group | 4 | 
| VPC associations per local gateway route table | 500 | 