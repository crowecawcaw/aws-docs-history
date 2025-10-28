# Launch instances with On-Demand Capacity Reservations (ODCR)

With [On-Demand Capacity Reservations (ODCR)](../../../AWSEC2/latest/UserGuide/ec2-capacity-reservations.md "../../../AWSEC2/latest/UserGuide/ec2-capacity-reservations.md"),
you can reserve capacity for your cluster Amazon EC2 instances in a specific Availability Zone. This way, you can create and manage Capacity Reservations
independently from the billing accounts that [Savings Plans](https://aws.amazon.com/savingsplans/ "https://aws.amazon.com/savingsplans/") or [regional Reserved Instances](../../../AWSEC2/latest/UserGuide/reserved-instances-scope.md "../../../AWSEC2/latest/UserGuide/reserved-instances-scope.md") offer.

You can configure `open` or `targeted` ODCR. _Open_ ODCR cover any
instances that match the ODCR attributes. These attributes are instance type, platform, and Availability Zone. You must explicitly define _Targeted_ ODCR in the cluster configuration. To determine whether an ODCR is `open` or `targeted`, run the AWS CLI
Amazon EC2 [`describe-capacity-reservation`](../../../cli/latest/reference/ec2/describe-capacity-reservations.md "../../../cli/latest/reference/ec2/describe-capacity-reservations.md") command.

You can also create an ODCR in a cluster placement group that's called a [cluster placement group on-demand capacity reservation (CPG ODCR)](../../../AWSEC2/latest/UserGuide/cr-cpg.md "../../../AWSEC2/latest/UserGuide/cr-cpg.md").

Multiple ODCRs can be grouped in a resource group. This can be defined in the cluster configuration file.
For more information about resource groups, see [What are resource groups?](../../../ARG/latest/userguide/resource-groups.md "../../../ARG/latest/userguide/resource-groups.md")
in the _Resource Groups and Tags User Guide_.

## Using ODCR with AWS ParallelCluster

AWS ParallelCluster supports open ODCR. When using an open ODCR, you don’t need to specify anything in AWS ParallelCluster. Instances are
automatically selected for the cluster. You can specify an existing placement group or have AWS ParallelCluster create a new one for you.

### ODCR in the cluster configuration

Starting with AWS ParallelCluster version 3.3.0, you can define ODCRs in the cluster configuration file, with no need to specify
Amazon EC2 run-instances overrides.

You start by creating [capacity
reservations](../../../AWSEC2/latest/UserGuide/capacity-reservations-using.md "../../../AWSEC2/latest/UserGuide/capacity-reservations-using.md") and [resource groups](../../../AWSEC2/latest/UserGuide/create-cr-group.md "../../../AWSEC2/latest/UserGuide/create-cr-group.md") using the methods described in the
linked documentation for each. You must use the AWS CLI methods to create capacity reservation groups. If you use the AWS Management Console, you can only create
Tag based or Stack based resource groups. Tag based and Stack based resource groups aren't supported by AWS ParallelCluster or the AWS CLI when
launching instances with capacity reservations.

After the capacity reservations and resource groups are created, specify them in [SlurmQueues](Scheduling-v3.md#Scheduling-v3-SlurmQueues "Scheduling-v3.md#Scheduling-v3-SlurmQueues") /
[CapacityReservationTarget](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-CapacityReservationTarget "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-CapacityReservationTarget") or [SlurmQueues](Scheduling-v3.md#Scheduling-v3-SlurmQueues "Scheduling-v3.md#Scheduling-v3-SlurmQueues") /
[ComputeResources](Scheduling-v3.md#Scheduling-v3-SlurmQueues-ComputeResources "Scheduling-v3.md#Scheduling-v3-SlurmQueues-ComputeResources") / [CapacityReservationTarget](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-CapacityReservationTarget "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-CapacityReservationTarget")
as shown in the following example cluster configuration. Replace `values` highlighted in red with your valid values.

```
Image:
  Os: `os`
HeadNode:
  InstanceType: `head_node_instance`
  Networking:
    SubnetId: `public_subnet_id`
  Ssh:
    KeyName: `key_name`
Scheduling:
  Scheduler: `scheduler`
  SlurmQueues:
    - Name: queue1
      Networking:
        SubnetIds:
          - `private_subnet_id`
      ComputeResources:
        - Name: cr1
          Instances:
            - InstanceType: `instance`
          MaxCount: `max_queue_size`
          MinCount: `max_queue_size`
          Efa:
            Enabled: true
          CapacityReservationTarget:
            CapacityReservationResourceGroupArn: `capacity_reservation_arn`
```

###### Warning

- Starting with AWS ParallelCluster version 3.3.0, we don't recommend this method. This section remains as a reference for implementations using prior
  versions.
- This method is not compatible with Multiple instance type allocation with Slurm.
  Support for `targeted` ODCRs is added in AWS ParallelCluster 3.1.1. In this release, a mechanism was introduced that overrides EC2
  `RunInstances` parameters and passes information about the reservation to use for each configured compute resource in
  AWS ParallelCluster. This mechanism is compatible with `targeted` ODCR. However, when you use `targeted` ODCR, you must
  specify the `run-instances` override configuration. _Targeted_ ODCRs must be explicitly defined in the
  AWS CLI Amazon EC2 [`run-instances`](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") command. To determine whether an ODCR is `open` or `targeted` run
  the AWS CLI Amazon EC2 command [`describe-capacity-reservation`](../../../cli/latest/reference/ec2/describe-capacity-reservations.md "../../../cli/latest/reference/ec2/describe-capacity-reservations.md").

Multiple ODCRs can be grouped in a resource group. This can be used in the run-instances override to target multiple ODCRs at the same time.

If you’re using a `targeted` ODCR, you can specify a placement group. However, you also need to specify a
`run-instances` override configuration.

Suppose that AWS created a `targeted` ODCR for you or you have a specific set of Reserved Instances. Then, you can't specify a
placement group. The rules that are configured by AWS might conflict with the placement group setting. So, if a placement group is required for
your application, use a [CPG ODCR](../../../AWSEC2/latest/UserGuide/cr-cpg.md "../../../AWSEC2/latest/UserGuide/cr-cpg.md"). In either case, you must
also specify the `run-instances` override configuration.

If you’re using a CPG ODCR, you must specify the `run-instances` override configuration and you must specify the same placement
group in the cluster configuration.

### Using Reserved Instances with AWS ParallelCluster

Reserved instances [are different](../../../AWSEC2/latest/UserGuide/ec2-capacity-reservations.md#capacity-reservations-differences "../../../AWSEC2/latest/UserGuide/ec2-capacity-reservations.md#capacity-reservations-differences") than Capacity Reservations (ODCR). There are [2 types](../../../AWSEC2/latest/UserGuide/reserved-instances-scope.md "../../../AWSEC2/latest/UserGuide/reserved-instances-scope.md") of reserved instances. A _Regional_ Reserved
Instance doesn't reserve capacity. A _zonal_ Reserved Instance reserves capacity in the specified Availability Zone.

If you have Regional Reserved Instances, there's no capacity reservation and you can get Insufficient Capacity Errors. If you have zonal
Reserved Instances, you have capacity reservation, but there are no `run-instances` API parameters that you can use to specify
them.

Reserved instances are supported by any AWS ParallelCluster version. You don't have to specify anything in AWS ParallelCluster and the
instances are automatically selected.

When using zonal Reserved Instances, you can avoid potential Insufficient Capacity Errors by omitting the placement group specification in the cluster configuration.

###### Warning

- Starting with AWS ParallelCluster version 3.3.0, we don't recommend this method. This section remains as a reference for implementations using prior
  versions.
- This method is not compatible with Multiple instance type allocation with Slurm.
  You can override Amazon EC2 `RunInstances` parameters for each compute resource that's configured in a cluster queue. To do so, create the
  `/opt/slurm/etc/pcluster/run_instances_overrides.json` file on the head node of the cluster with the following code snippet
  content:

- `${queue_name}` is the name of the queue that you want to apply overrides to.
- `${compute_resource_name}` is the compute resource that you want to apply overrides to.
- `${overrides}` is an arbitrary JSON object that contains a list of `RunInstances` overrides to use for the
  specific combination of queue and instance type. The overrides syntax needs to follow the same specifications that are documented in a [run_instances](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.run_instances "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.run_instances") boto3
  call.

```
{
    "${queue_name}": {
        "${compute_resource_name}": {
            ${overrides}
        },
        ...
    },
    ...
}
```

For example, the following JSON configures the ODCR group `group_arn` to be used for `p4d.24xlarge` instances that are
configured in `my-queue` and `my-compute-resource`.

```
{
    `"my-queue"`: {
        `"my-compute-resource"`: {
            "CapacityReservationSpecification": {
                "CapacityReservationTarget": {
                    "CapacityReservationResourceGroupArn": `"group_arn"`
                }
            }
        }
    }
}
```

After this JSON file is generated, the AWS ParallelCluster daemons that are responsible for cluster scaling automatically use the override
configuration for instance launches. To confirm that the specified parameters are being used for instance provisioning, look at the following log
files:

- `/var/log/parallelcluster/clustermgtd` (for static capacity)
- `/var/log/parallelcluster/slurm_resume.log` (for dynamic capacity)
  If the parameters are correct, you'll find a log entry that contains the following:

```
Found RunInstances parameters override. Launching instances with: <parameters_list>
```

###### Warning

- Starting with AWS ParallelCluster version 3.3.0, we don't recommend this method. This section remains as a reference for implementations using prior
  versions.
- This method is not compatible with [Multiple instance type allocation with Slurm](slurm-multiple-instance-allocation-v3.md "slurm-multiple-instance-allocation-v3.md").

1. **Create a resource group, to group capacity.**

```
`$` `aws resource-groups create-group --name `EC2CRGroup` \
   --configuration '{"Type":"AWS::EC2::CapacityReservationPool"}' '{"Type":"AWS::ResourceGroups::Generic", "Parameters": [{"Name": "allowed-resource-types", "Values": ["AWS::EC2::CapacityReservation"]}]}'`
```

###### Note

A resource group doesn't support resources that are shared by other accounts.

If the target ODCR is shared by another account, you don't need to create a resource group. Use `CapacityReservationId` instead
of a resource group in step 3.

```
#!/bin/bash
set -e

# Override run_instance attributes
cat > /opt/slurm/etc/pcluster/run_instances_overrides.json << EOF
{
    "my-queue": {
        "my-compute-resource": {
            "CapacityReservationSpecification": {
                "CapacityReservationTarget": {
                    "CapacityReservationId": "cr-abcdef01234567890"
                }
            }
        }
    }
}
EOF
```

Add capacity reservations to the resource group. Every time that you create a new ODCR, add it to the Group Reservation. Replace
`ACCOUNT_ID` with your account ID,
`PLACEHOLDER_CAPACITY_RESERVATION` with your capacity reservation ID, and
`REGION_ID` with your AWS Region ID (for example, us-east-1).

```
`$` `aws resource-groups group-resources --region `REGION_ID` --group `EC2CRGroup` \
   --resource-arns arn:aws:ec2:`REGION_ID`:`ACCOUNT_ID`:capacity-reservation/`PLACEHOLDER_CAPACITY_RESERVATION``
```

Create a policy document on your local computer. Replace `ACCOUNT_ID` with your account ID and
`REGION_ID` with your AWS Region ID (for example, us-east-1).

```
cat > policy.json << EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "RunInstancesInCapacityReservation",
            "Effect": "Allow",
            "Action": "ec2:RunInstances",
            "Resource": [
                "arn:aws:ec2:`REGION_ID`:`ACCOUNT_ID`:capacity-reservation/*",
                "arn:aws:resource-groups:`REGION_ID`:`ACCOUNT_ID`:group/*"
            ]
        }
    ]
}
EOF
```

2. **Create the IAM policy on your AWS account using the json file that you created.**

```
`$` `aws iam create-policy --policy-name `RunInstancesCapacityReservation` --policy-document file://policy.json`
```

3. **Create the following post install script locally on the instance and name it
   `postinstall.sh`.**

Replace `ACCOUNT_ID` with your AWS account ID, and `REGION_ID` with
your AWS Region ID (for example, us-east-1).

```
#!/bin/bash
set -e

# Override run_instance attributes
cat > /opt/slurm/etc/pcluster/run_instances_overrides.json << EOF
{
    "my-queue": {
        "my-compute-resource": {
            "CapacityReservationSpecification": {
                "CapacityReservationTarget": {
                    "CapacityReservationResourceGroupArn": "arn:aws:resource-groups:`REGION_ID`:`ACCOUNT_ID`:group/`EC2CRGroup`"
                }
            }
        }
    }
}
EOF
```

Upload the file to an Amazon S3 bucket. Replace `amzn-s3-demo-bucket` with your specific S3 bucket name.

```
`$` `aws s3 mb s3://`amzn-s3-demo-bucket`
aws s3 cp postinstall.sh s3://`amzn-s3-demo-bucket`/postinstall.sh`
```

4. **Create the local cluster configuration, replacing the placeholders with your own values.**

```
Region: `REGION_ID`
Image:
  Os: alinux2
HeadNode:
  InstanceType: c5.2xlarge
  Ssh:
    KeyName: `YOUR_SSH_KEY`
  Iam:
    S3Access:
      - BucketName: `amzn-s3-demo-bucket`
    AdditionalIamPolicies:
      - Policy: arn:aws:iam::`ACCOUNT_ID`:policy/RunInstancesCapacityReservation
  ## This post-install script is executed after the node is configured.
  ## It is used to install scripts at boot time and specific configurations
  ## In the script below we are overriding the calls to RunInstance to force
  ## the provisioning of our my-queue partition to go through
  ## the On-Demand Capacity Reservation
  CustomActions:
    OnNodeConfigured:
      Script: s3://`amzn-s3-demo-bucket`/postinstall.sh
  Networking:
    SubnetId: `YOUR_PUBLIC_SUBNET_IN_TARGET_AZ`

Scheduling:
  Scheduler: slurm
  SlurmQueues:
    - Name: my-queue
      ComputeResources:
        - MinCount: 0
          MaxCount: 100
          InstanceType: p4d.24xlarge
          Name: `my-compute-resource`
          Efa:
            Enabled: true
      Networking:
        ## PlacementGroup:
        ##   Enabled: true ## Keep PG disabled if using targeted ODCR
        SubnetIds:
          - `YOUR_PRIVATE_SUBNET_IN_TARGET_AZ`
```

5. **Create the cluster.**

Use the following command to create the cluster. Replace `cluster-config.yaml` with your configuration
file name, `cluster-dl` with your cluster name, and `REGION_ID` with your Region
ID (for example, us-east-1).

```
`$` `pcluster create-cluster --cluster-configuration `cluster-config.yaml` --cluster-name `cluster-dl` --region `REGION_ID``
```

After the cluster is created, the post-install script runs in the head node. The script creates the
`run_instances_overrides.json` file and overrides the calls to `RunInstances` to force the provisioning of the partition
to go through the On-Demand Capacity Reservation.

The AWS ParallelCluster daemons that are responsible for cluster scaling automatically use this configuration for new instances that are
launched. To confirm that the specified parameters are being used to provision instances, you can look at the following log files:

    * `/var/log/parallelcluster/clustermgtd` (for static capacity - [MinCount](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-MinCount "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-MinCount") `> 0`)
    * `/var/log/parallelcluster/slurm_resume.log` (for dynamic capacity)

If the parameters are correct, you'll find a log entry contains the following.

```
Found RunInstances parameters override. Launching instances with: <parameters_list>
```

**Updating `RunInstances` overrides**

You can update the generated JSON configuration at any time without stopping the compute fleet. After the changes are applied, all new
instances launch with the updated configuration. If you need to apply the updated configuration to running nodes, recycle the nodes by forcing an
instance termination and wait for AWS ParallelCluster to replace those nodes. You can do this by terminating the instance from the Amazon EC2 console or
AWS CLI, or by setting the Slurm nodes in a `DOWN` or `DRAIN` state.

Use the following command to set the Slurm node to `DOWN` or `DRAIN`.

```
`$` `scontrol update nodename=`my-queue-dy-my-compute-resource-1` state=down reason=`your_reason`
scontrol update nodename=`my-queue-dy-my-compute-resource-1` state=drain reason=`your_reason``
```
