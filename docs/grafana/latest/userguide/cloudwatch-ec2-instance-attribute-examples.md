# Using

ec2_instance_attribute examples

## JSON filters

The `ec2_instance_attribute` query takes `filters`
in JSON format. You can specify pre-defined filters of
`ec2:DescribeInstances`. Note that the actual filtering takes
place in AWS, not in Grafana.

The following code example shows the filters syntax.

```
{ filter_name1: [ filter_value1 ], filter_name2: [ filter_value2 ] }
```

The following example shows the `ec2_instance_attribute()`
query.

```
ec2_instance_attribute(us - east - 1, InstanceId, { 'tag:Environment': ['production'] });
```

## Selecting

attributes

Only one attribute per instance can be returned. Any flat attribute can
be selected (that is, if the attribute has a single value and isn’t an
object or array). The following flat attributes are available.

- `AmiLaunchIndex`
- `Architecture`
- `ClientToken`
- `EbsOptimized`
- `EnaSupport`
- `Hypervisor`
- `IamInstanceProfile`
- `ImageId`
- `InstanceId`
- `InstanceLifecycle`
- `InstanceType`
- `KernelId`
- `KeyName`
- `LaunchTime`
- `Platform`
- `PrivateDnsName`
- `PrivateIpAddress`
- `PublicDnsName`
- `PublicIpAddress`
- `RamdiskId`
- `RootDeviceName`
- `RootDeviceType`
- `SourceDestCheck`
- `SpotInstanceRequestId`
- `SriovNetSupport`
- `SubnetId`
- `VirtualizationType`
- `VpcId`

Tags can be selected by prefixing the tag name with `Tags`.

The following example shows the `ec2_instance_attribute()`
query.

```

ec2_instance_attribute(us - east - 1, Tags.Name, { 'tag:Team': ['sysops'] });

```
