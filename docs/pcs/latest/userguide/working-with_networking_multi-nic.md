# Multiple network interfaces in

AWS PCS

Some EC2 instances have multiple network cards. This allows them to provide higher network
performance, including bandwidth capabilities above 100 Gbps and improved packet handling.
For more information about instances with multiple network cards, see [Elastic
network interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md#network-cards "../../../AWSEC2/latest/UserGuide/using-eni.md#network-cards") in the _Amazon Elastic Compute Cloud User Guide_.

Configure additional network cards for instances in an AWS PCS compute node group by
adding network interfaces to its EC2 launch template. Below is an example launch template
that enables two network cards, such as can be found on an `hpc7a.96xlarge`
instance. Note the following details:

- The subnet for each network interface must be the same as you choose when
  configuring the AWS PCS compute node group that will use the launch
  template.
- The primary network device, where routine network communication such as SSH and
  HTTPS traffic will occur, is established by setting a `DeviceIndex` of
  `0`. Other network interfaces have a `DeviceIndex` of
  `1`. There can only be one primary network interface—all other
  interfaces are secondary.
- All network interfaces must have a unique `NetworkCardIndex`. A
  recommended practice is to number them sequentially as they are defined in the
  launch template.
- Security groups for each network interface are set using `Groups`. In
  this example, an inbound SSH security group
  (`sg-`SshSecurityGroupId``) is added to
the primary network interface, as well as the security group enabling within-cluster
communications (`sg-`ClusterSecurityGroupId``).
  Finally, a security group allowing outbound connections to the internet
  (`sg-`InternetOutboundSecurityGroupId``)
  is added to both primary and secondary interfaces.

```
{
    "NetworkInterfaces": [
        {
            "DeviceIndex": 0,
            "NetworkCardIndex": 0,
            "SubnetId": "subnet-`SubnetId`",
            "Groups": [
               "sg-`SshSecurityGroupId`",
               "sg-`ClusterSecurityGroupId`",
               "sg-`InternetOutboundSecurityGroupId`"
            ]
        },
        {
            "DeviceIndex": 1,
            "NetworkCardIndex": 1,
            "SubnetId": "subnet-`SubnetId`",
            "Groups": ["sg-`InternetOutboundSecurityGroupId`"]
        }
    ]
}
```
