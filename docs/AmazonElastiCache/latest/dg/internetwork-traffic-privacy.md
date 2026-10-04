

# Internetwork traffic privacy
<a name="internetwork-traffic-privacy"></a>

Amazon ElastiCache uses the following techniques to secure your cache data and protect it from unauthorized access:
+ **[Amazon VPCs and ElastiCache security](VPCs.md)** explains the type of security group you need for your installation.
+ **[Identity and Access Management for Amazon ElastiCache](IAM.md)** for granting and limiting actions of users, groups, and roles.

For ElastiCache Serverless caches with a public endpoint, connections are secured with IAM authentication and TLS 1.3 instead of Amazon Virtual Private Cloud (Amazon VPC) security groups. All users in the cache's user group must use IAM authentication.

**Topics**
+ [Amazon VPCs and ElastiCache security](VPCs.md)
+ [ElastiCache API and interface VPC endpoints (AWS PrivateLink)](elasticache-privatelink.md)
+ [Subnets and subnet groups](SubnetGroups.md)