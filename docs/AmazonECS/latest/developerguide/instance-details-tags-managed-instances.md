# Tags for

Amazon ECS Managed Instances

Amazon ECS Managed Instances support a combination of custom tags and tags added by AWS that can be used for cost optimization. For more information about using tags for billing, see [Use tags for billing](ecs-using-tags.md#tag-resources-for-billing "ecs-using-tags.md#tag-resources-for-billing").

## Tags added by AWS

AWS adds the following tags to each Amazon ECS Managed Instance created by the capacity
provider:

- Amazon ECS automatically adds the reserved tags `AmazonECSCreated` and
  `AmazonECSManaged` to Amazon ECS Managed Instances.
- Amazon ECS adds the following system tags to each instance:
  - A tag with a _Key_ as
    `aws:ecs:clusterName` and a _Value_
    set to the name of the cluster.
  - A tag with a _Key_ as
    `aws:ecs:capacityProviderName` and a
    _Value_ set to the name of the capacity
    provider.
  - A tag with a _Key_ as
    `aws:ecs:containerInstanceId` and a
    _Value_ as the container instance ID for the
    Amazon ECS Managed Instance.

- Amazon EC2 adds the system tag `aws:ec2:managed-launch` with the
  value `ecs-managed-instances`. In addition, Amazon EC2 adds system
  tags denoting the launch template that was used to create the managed instance, and the Amazon EC2 fleet that the managed instance is part of.

## Custom tags

You can add additional custom tags to Amazon ECS Managed Instances by adding tags to the capacity
provider and enabling tag propagation using the `propagateTags`
property.

The following example capacity provider definition shows how tags can be specified and
propagated from the capacity provider when creating the capacity provider using the
`CAPACITY_PROVIDER` value for `propagateTags`.

```
{
    "name": "my-cluster-managed-instances-cp",
    "cluster": "my-cluster",
     "tags": [
                {
                "key":"tag_key",
                "value":"tag_value"
                }
            ],
    "managedInstancesProvider": {
        "infrastructureRoleArn": "arn:aws:iam::123456789012:role/ecsInfrastructureRole",
        "propagateTags": "CAPACITY_PROVIDER",
        "instanceLaunchTemplate": {
            "ec2InstanceProfileArn": "arn:aws:iam::123456789012:instance-profile/ecsInstanceProfile",
            "networkConfiguration": {
                "subnets": [
                    "subnet-abcdef01234567",
                    "subnet-bcdefa98765432"
                ],
                "securityGroups": [
                    "sg-0123456789abcdef"
                ]
            }
        }
    }
}
```

###### Note

When you add new tags to a capacity provider, the newly added tags will not be
propagated to existing instances but will be propagated to any newly created
instances.

For more information about Amazon ECS Managed Instances capacity providers, see [Amazon ECS Managed Instances capacity providers](managed-instances-capacity-providers-concept.md "managed-instances-capacity-providers-concept.md").
