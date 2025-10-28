# Customize a provisioning timeout

period for cluster resize in Amazon EMR

You can define a timeout period for provisioning Spot Instances for each fleet in
your cluster. If Amazon EMR can't provision the Spot capacity, it cancels the resize
request and stops its attempts to provision additional Spot capacity. When you
create a cluster, you can configure the timeout. For a running cluster, you can add
or update a timeout.

When the timeout period expires, Amazon EMR automatically sends events to an Amazon CloudWatch Events
stream. With CloudWatch, you can create rules that match events according to a specified
pattern, and then route the events to targets to take action. For example, you might
configure a rule to send an email notification. For more information on how to
create rules, see [Creating rules for Amazon EMR events with
CloudWatch](emr-events-cloudwatch-console.md "emr-events-cloudwatch-console.md"). For more information about
different event details, see [Instance fleet state-change
events](emr-manage-cloudwatch-events.md#emr-cloudwatch-instance-fleet-events "emr-manage-cloudwatch-events.md#emr-cloudwatch-instance-fleet-events").

## Examples of provisioning

timeouts for cluster resize

**Specify a provisioning timeout for resize with the
AWS CLI**

The following example uses the `create-cluster` command to add a
provisioning timeout for resize.

```
aws emr create-cluster \
--release-label emr-5.35.0 \
--service-role EMR_DefaultRole \
--ec2-attributes '{"InstanceProfile":"EMR_EC2_DefaultRole","SubnetIds":["subnet-XXXXX"]}' \
--instance-fleets '[{"InstanceFleetType":"MASTER","TargetOnDemandCapacity":1,"TargetSpotCapacity":0,"InstanceTypeConfigs":[{"WeightedCapacity":1,"EbsConfiguration":{"EbsBlockDeviceConfigs":[{"VolumeSpecification":{"SizeInGB":32,"VolumeType":"gp2"},"VolumesPerInstance":2}]},"BidPriceAsPercentageOfOnDemandPrice":100,"InstanceType":"m5.xlarge"}],"Name":"Master - 1"},{"InstanceFleetType":"CORE","TargetOnDemandCapacity":1,"TargetSpotCapacity":1,"LaunchSpecifications":{"SpotSpecification":{"TimeoutDurationMinutes":120,"TimeoutAction":"SWITCH_TO_ON_DEMAND"},"OnDemandSpecification":{"AllocationStrategy":"lowest-price"}},"ResizeSpecifications":{"SpotResizeSpecification":{"TimeoutDurationMinutes":20},"OnDemandResizeSpecification":{"TimeoutDurationMinutes":25}},"InstanceTypeConfigs":[{"WeightedCapacity":1,"EbsConfiguration":{"EbsBlockDeviceConfigs":[{"VolumeSpecification":{"SizeInGB":32,"VolumeType":"gp2"},"VolumesPerInstance":2}]},"BidPriceAsPercentageOfOnDemandPrice":1,"InstanceType":"m5.xlarge"}],"Name":"Core - 2"}]'
```

The following example uses the `modify-instance-fleet` command to
add a provisioning timeout for resize.

```
aws emr modify-instance-fleet \
--cluster-id j-XXXXXXXXXXXXX \
--instance-fleet '{"InstanceFleetId":"if-XXXXXXXXXXXX","ResizeSpecifications":{"SpotResizeSpecification":{"TimeoutDurationMinutes":30},"OnDemandResizeSpecification":{"TimeoutDurationMinutes":60}}}' \
--region us-east-1
```

The following example uses the `add-instance-fleet-command` to add
a provisioning timeout for resize.

```
aws emr add-instance-fleet \
--cluster-id j-XXXXXXXXXXXXX \
--instance-fleet '{"InstanceFleetType":"TASK","TargetOnDemandCapacity":1,"TargetSpotCapacity":0,"InstanceTypeConfigs":[{"WeightedCapacity":1,"EbsConfiguration":{"EbsBlockDeviceConfigs":[{"VolumeSpecification":{"SizeInGB":32,"VolumeType":"gp2"},"VolumesPerInstance":2}]},"BidPriceAsPercentageOfOnDemandPrice":100,"InstanceType":"m5.xlarge"}],"Name":"TaskFleet","ResizeSpecifications":{"SpotResizeSpecification":{"TimeoutDurationMinutes":30},"OnDemandResizeSpecification":{"TimeoutDurationMinutes":35}}}' \
--region us-east-1
```

**Specify a provisioning timeout for resize and launch
with the AWS CLI**

The following example uses the `create-cluster` command to add a
provisioning timeout for resize and launch.

```
aws emr create-cluster \
--release-label emr-5.35.0 \
--service-role EMR_DefaultRole \
--ec2-attributes '{"InstanceProfile":"EMR_EC2_DefaultRole","SubnetIds":["subnet-XXXXX"]}' \
--instance-fleets '[{"InstanceFleetType":"MASTER","TargetOnDemandCapacity":1,"TargetSpotCapacity":0,"LaunchSpecifications":{"OnDemandSpecification":{"AllocationStrategy":"lowest-price"}},"InstanceTypeConfigs":[{"WeightedCapacity":1,"EbsConfiguration":{"EbsBlockDeviceConfigs":[{"VolumeSpecification":{"SizeInGB":32,"VolumeType":"gp2"},"VolumesPerInstance":2}]},"BidPriceAsPercentageOfOnDemandPrice":100,"InstanceType":"m5.xlarge"}],"Name":"Master - 1"},{"InstanceFleetType":"CORE","TargetOnDemandCapacity":1,"TargetSpotCapacity":1,"LaunchSpecifications":{"SpotSpecification":{"TimeoutDurationMinutes":120,"TimeoutAction":"SWITCH_TO_ON_DEMAND"},"OnDemandSpecification":{"AllocationStrategy":"lowest-price"}},"ResizeSpecifications":{"SpotResizeSpecification":{"TimeoutDurationMinutes":20},"OnDemandResizeSpecification":{"TimeoutDurationMinutes":25}},"InstanceTypeConfigs":[{"WeightedCapacity":1,"EbsConfiguration":{"EbsBlockDeviceConfigs":[{"VolumeSpecification":{"SizeInGB":32,"VolumeType":"gp2"},"VolumesPerInstance":2}]},"BidPriceAsPercentageOfOnDemandPrice":1,"InstanceType":"m5.xlarge"}],"Name":"Core - 2"}]'
```

## Considerations for

resize provisioning timeouts

When you configure cluster provisioning timeouts for your instance fleets,
consider the following behaviors.

- You can configure provisioning timeouts for both Spot and On-Demand
  Instances. The minimum provisioning timeout is 5 minutes. The maximum
  provisioning timeout is 7 days.
- You can only configure provisioning timeouts for an EMR cluster that
  uses instance fleets. You must configure each core and task fleet
  separately.
- When you create a cluster, you can configure provisioning timeouts.
  You can add a timeout or update an existing timeout for a running
  cluster.
- If you submit multiple resize operations, then Amazon EMR tracks
  provisioning timeouts for every resize operation. For example, set the
  provisioning timeout on a cluster to `60`
  minutes. Then, submit a resize operation `R1`
  at time `T1`. Submit a second resize operation
  `R2` at time `T2`.
  The provisioning timeout for R1 expires at `T1 + 60
minutes`. The provisioning timeout for R2 expires at
  `T2 + 60 minutes`.
- If you submit a new scale-up resize operation before the timeout
  expires, Amazon EMR continues its attempt to provision capacity for your
  EMR cluster.
