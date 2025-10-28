# Compute environments on Fargate

AWS Batch compute environments on AWS Fargate don't support all of the compute environment parameters that are
available. Some parameters are not supported at all. Others have specific requirements for Fargate.

The following list describes compute environment parameters that aren't valid or otherwise restricted in
Fargate jobs.

`type`

This parameter must be `MANAGED`.

```
"type": "MANAGED"
```

Parameters in the `computeResources` object

`allocationStrategy`
`bidPercentage`
`desiredvCpus`
`imageId`
`instanceTypes`
`ec2Configuration`
`ec2KeyPair`
`instanceRole`
`launchTemplate`
`minvCpus`
`placementGroup`
`spotIamFleetRole`

These aren't applicable for Fargate compute environments and can't be provided.

`subnets`

If the subnets listed in this parameter don't have NAT gateways attached, the `assignPublicIp`
parameter in the job definition must be set to `ENABLED`.

`tags`

This isn't applicable for Fargate compute environments and can't be provided. To specify tags for
Fargate compute environments, use the `tags` parameter that's not in the
`computeResources` object.

`type`

This must be either `FARGATE` or `FARGATE_SPOT`.

```
"type": "FARGATE_SPOT"
```
