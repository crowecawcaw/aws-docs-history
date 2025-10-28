# Create or update an EC2 launch

template

EFA network interfaces are set up in the EC2 launch template for an AWS PCS compute node
group. If there are multiple network cards, multiple EFAs can be configured. The EFA security
group and the optional placement group are included in the launch template as well.

Here is an example launch template for instances with two network cards, such as **hpc7a.96xlarge**. The instances will be launched in
`subnet-`SubnetID1`` in cluster placement group
 `pg-`PlacementGroupId1``.

Security groups must be added specifically to each EFA interface. Every EFA needs the
security group that enables EFA traffic
(`sg-`EfaSecGroupId``). Other security groups, especially
 ones that handle regular traffic like SSH or HTTPS, only need to be attached to the primary
 network interface (designated by a `DeviceIndex`of`0`). Launch templates
 where network interfaces are defined do not support setting security groups using the
 `SecurityGroupIds`parameter—you must set a value for`Groups` in
each network interface that you configure.

```
{
    "Placement": {
        "GroupId": "pg-`PlacementGroupId1`"
    },
    "NetworkInterfaces": [
        {
            "DeviceIndex": 0,
            "InterfaceType": "efa",
            "NetworkCardIndex": 0,
            "SubnetId": "subnet-`SubnetId1`",
            "Groups": [
                "sg-`SecurityGroupId1`",
                "sg-`EfaSecGroupId`"
            ]
        },
        {
            "DeviceIndex": 1,
            "InterfaceType": "efa",
            "NetworkCardIndex": 1,
            "SubnetId": "subnet-`SubnetId1`"
            "Groups": ["sg-`EfaSecGroupId`"]
        }
    ]
}
```
