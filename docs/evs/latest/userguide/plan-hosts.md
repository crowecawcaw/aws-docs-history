

# Choose versions, hosts, and size

The hosts in an Amazon Elastic VMware Service environment are Amazon Elastic Compute Cloud (Amazon EC2) bare metal instances that run ESX. Make the host decisions in the following order, because each choice limits the next one. The VMware Cloud Foundation (VCF) version decides which instance types you can use, and the instance type affects how many hosts you need. The number of hosts then decides the capacity and the quotas that you request.

1.  [Choose VCF and ESX versions](plan-versions.md). Choose the VCF version and deployment mode, and check which ESX builds are available.

1.  [Choose instance types](plan-instance-types.md). Choose local NVMe hosts, or diskless hosts for VCF 9.x, and then an instance size.

1.  [Size your environment](plan-sizing.md). Decide how many hosts you need, and which quotas to raise before you start.

1.  [Reserve capacity for hosts](plan-capacity.md). Reserve EC2 capacity for your hosts, including a spare host.

**Topics**
+ [Choose VCF and ESX versions](plan-versions.md)
+ [Choose instance types](plan-instance-types.md)
+ [Size your environment](plan-sizing.md)
+ [Reserve capacity for hosts](plan-capacity.md)