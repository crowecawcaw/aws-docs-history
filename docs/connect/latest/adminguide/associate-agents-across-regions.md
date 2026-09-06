

# Associate agents to Connect Customer instances across multiple AWS Regions
<a name="associate-agents-across-regions"></a>

To allow your agents to sign-in to both AWS Regions and process contacts from either Region, you must first assign them to a traffic distribution group. 

1. If you have not yet set up a traffic distribution group, do so now. For instructions, see [Create traffic distribution groups for your Connect Customer instance](setup-traffic-distribution-groups.md).

1. After your traffic distribution group is created successfully (`Status` is `ACTIVE`), you can assign agents to it. Always associate users to a traffic distribution group in the source Region.

   Assigning an agent to a traffic distribution group without an `ACTIVE` status results in `ResourceNotFoundException`. Use the [DescribeTrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeTrafficDistributionGroup.html) API to determine whether it has been created successfully (`Status` must be `ACTIVE`). 

1. You can assign an agent to a traffic distribution group by calling the [AssociateTrafficDistributionGroupUser](https://docs.aws.amazon.com/connect/latest/APIReference/API_AssociateTrafficDistributionGroupUser.html) API. 

## Examples
<a name="examples-associate"></a>

The following `associate-traffic-distribution-group-user` example command shows how agents can be associated to and used across multiple AWS Regions.

```
aws connect associate-traffic-distribution-group-user 
  --traffic-distribution-group-id {{UUID}}
  --user-id {{UUID}}
  --instance-id
```

The following [AssociateTrafficDistributionGroupUser](https://docs.aws.amazon.com/connect/latest/APIReference/API_AssociateTrafficDistributionGroupUser.html) example associates an agent with a traffic distribution group.

```
PUT /traffic-distribution-group/{{trafficDistributionGroupId}}/user HTTP/1.1
Content-type: application/json
 
{
   "UserId": "{{string}}"
}
```

The following `disassociate-traffic-distribution-group-user` example command disassociates an agent from a traffic distribution group. 

```
aws connect disassociate-traffic-distribution-group-user 
 --instance-id {{your instance ID}}
 --traffic-distribution-group-id {{UUID}} 
  --user-id {{UUID}}
```

The following [DisassociateTrafficDistributionGroupUser](https://docs.aws.amazon.com/connect/latest/APIReference/API_DisassociateTrafficDistributionGroupUser.html) example disassociates an agent from a traffic distribution group.

```
DELETE /traffic-distribution-group/{{trafficDistributionGroupId}}/user/{{UserId}} HTTP/1.1
```

## Why an AssociateTrafficDistributionGroupUser call fails
<a name="why-association-fails"></a>

An [AssociateTrafficDistributionGroupUser](https://docs.aws.amazon.com/connect/latest/APIReference/API_AssociateTrafficDistributionGroupUser.html) API call fails with an `ResourceNotFoundException` in the following cases:

1. The specified traffic distribution group does not exist.

1. The status of the traffic distribution group is not `ACTIVE`.

1. The `user-id {{UUID}}` is not a user from the source Connect Customer instance.