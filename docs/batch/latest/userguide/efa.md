# Elastic Fabric Adapter

An Elastic Fabric Adapter (EFA) is a network device to accelerate High Performance Computing (HPC) applications.
AWS Batch supports applications that use EFA if the following conditions are met.

- For a list of instance types that support EFAs, see [Supported instance types](../../../AWSEC2/latest/UserGuide/efa.md#efa-instance-types "../../../AWSEC2/latest/UserGuide/efa.md#efa-instance-types") in the _Amazon EC2 User Guide_.

###### Tip

To see a list of instance types that support EFAs in an AWS Region, run the
following command. Then, cross reference the list that's returned with the list of
available instance types in the AWS Batch console.

```
`$` `aws ec2 describe-instance-types --region `us-east-1` --filters Name=network-info.efa-supported,Values=true --query "InstanceTypes[*].[InstanceType]" --output text | sort`
```

- For a list of operating systems that support EFA, see [Supported
  operating systems](../../../AWSEC2/latest/UserGuide/efa.md#efa-os "../../../AWSEC2/latest/UserGuide/efa.md#efa-os").
- The AMI has the EFA driver loaded.
- The security group for the EFA must allows all inbound and outbound traffic to and from the security group
  itself.
- All instances that use an EFA must be in the same cluster placement group.
- The job definition must include a `devices` member with `hostPath`
  set to `/dev/infiniband/uverbs0` to allow the EFA device to be passed through to
  the container. If `containerPath` is specified, it must also be set to
  `/dev/infiniband/uverbs0`. If `permissions` is set it must be set to
  `READ` | `WRITE` | `MKNOD`.

The location of the [LinuxParameters](../APIReference/API_LinuxParameters.md "../APIReference/API_LinuxParameters.md") members
are different for multi-node parallel jobs and single-node container jobs. The following
examples show the differences, but are missing required values.

###### Example for multi-node parallel job

```
{
  "jobDefinitionName": "EFA-MNP-JobDef",
  "type": "multinode",
  "nodeProperties": {
    ...
    "nodeRangeProperties": [
      {
        ...
        "container": {
          ...
          "linuxParameters": {
            "devices": [
              {
                "hostPath": "/dev/infiniband/uverbs0",
                "containerPath": "/dev/infiniband/uverbs0",
                "permissions": [
                    "READ", "WRITE", "MKNOD"
                ]
              },
            ],
          },
        },
      },
    ],
  },
}
```

###### Example for single-node container job

```
{
  "jobDefinitionName": "EFA-Container-JobDef",
  "type": "container",
  ...
  "containerProperties": {
    ...
    "linuxParameters": {
      "devices": [
        {
          "hostPath": "/dev/infiniband/uverbs0",
        },
      ],
    },
  },
}
```

For more information about EFA, see [Elastic Fabric Adapter](../../../AWSEC2/latest/UserGuide/efa.md "../../../AWSEC2/latest/UserGuide/efa.md") in
_Amazon EC2 User Guide_.
