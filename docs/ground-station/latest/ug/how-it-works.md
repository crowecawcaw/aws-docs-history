# Use AWS Ground Station Dataflow endpoint groups

_Dataflow endpoints_ define the location where you want the data to be
synchronously streamed to or from during contacts. Dataflow endpoints are always created as part
of a _dataflow endpoint group_. By including multiple dataflow
endpoints in a group, you are asserting that the specified endpoints can all be used together
during a single contact. For example, if a contact needs to send data to three separate dataflow
endpoints, you must have three endpoints in a single dataflow endpoint group that match the
dataflow endpoint configs in your mission profile.

## Dataflow endpoint group versions

AWS Ground Station supports two versions of dataflow endpoint groups:

- **DataflowEndpointGroup** - The original implementation that supports uplink and downlink using a [dataflow endpoint](../APIReference/API_DataflowEndpoint.md "../APIReference/API_DataflowEndpoint.md"), and downlink-only for an [AWS Ground Station Agent endpoint](../APIReference/API_AwsGroundStationAgentEndpoint.md "../APIReference/API_AwsGroundStationAgentEndpoint.md")
- **DataflowEndpointGroupV2** - Updated version that supports both uplink and downlink dataflows for AWS Ground Station Agent endpoints with improved clarity and functionality

| Dataflow endpoint group comparison | Feature                                         | DataflowEndpointGroup                                                      | DataflowEndpointGroupV2 |
| ---------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------- | ----------------------- |
| Supported endpoint types           | DataflowEndpoint, AwsGroundStationAgentEndpoint | DownlinkAwsGroundStationAgentEndpoint, UplinkAwsGroundStationAgentEndpoint |
| Endpoints supporting uplink        | DataflowEndpoint                                | UplinkAwsGroundStationAgentEndpoint                                        |
| Endpoints supporting downlink      | DataflowEndpoint, AwsGroundStationAgentEndpoint | DownlinkAwsGroundStationAgentEndpoint                                      |

DataflowEndpointGroupV2 was created to support uplink dataflows and to make the language surrounding dataflow endpoint groups clearer. We recommend using [UplinkAwsGroundStationAgentEndpoint](../APIReference/API_UplinkAwsGroundStationAgentEndpoint.md "../APIReference/API_UplinkAwsGroundStationAgentEndpoint.md") and [DownlinkAwsGroundStationAgentEndpoint](../APIReference/API_DownlinkAwsGroundStationAgentEndpoint.md "../APIReference/API_DownlinkAwsGroundStationAgentEndpoint.md") endpoints with a [DataflowEndpointGroupV2](../APIReference/API_CreateDataflowEndpointGroupV2.md "../APIReference/API_CreateDataflowEndpointGroupV2.md") for all new use cases. DataflowEndpointGroup remains supported for backward compatibility, but DataflowEndpointGroupV2 provides enhanced functionality and clearer configuration options.

###### Tip

The dataflow endpoints are identified by a name of your choosing when executing contacts. These
names do not need to be unique across the account. This allows multiple contacts across
different satellites and antenna to be executed at the same time using the same mission profile.
This can be useful if you have a constellation of satellites that have the same operating
characteristics. You can scale the number of dataflow endpoint groups up to fit the maximum
number of simultaneous contacts your constellation of satellite requires.

When one or more resources in a dataflow endpoint group is in use for a contact, the entire
group is reserved for the duration of that contact. You may execute multiple contacts
concurrently, but those contacts must be executed on different dataflow endpoint groups.

###### Important

Dataflow endpoint groups must be in a `HEALTHY` state to schedule contacts using them.
For information on how to troubleshoot dataflow endpoint groups that are not in a `HEALTHY`
state, see [Troubleshoot DataflowEndpointGroups not in a HEALTHY
state](troubleshooting-dfeg.md "troubleshooting-dfeg.md") .

See the following documentation for more information about how to perform operations on dataflow endpoint groups using CloudFormation, the AWS Command Line Interface, or the AWS Ground Station API.

- [AWS::GroundStation::DataflowEndpointGroup CloudFormation resource type](../../../AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.md")
- [Dataflow Endpoint Group AWS CLI reference](../../../cli/latest/reference/groundstation/create-dataflow-endpoint-group.md "../../../cli/latest/reference/groundstation/create-dataflow-endpoint-group.md")
- [Dataflow Endpoint Group API reference](../APIReference/API_CreateDataflowEndpointGroup.md "../APIReference/API_CreateDataflowEndpointGroup.md")

## Dataflow endpoints

The members of a dataflow endpoint group are dataflow endpoints. The supported endpoint types depend on which dataflow endpoint group version you use.

### DataflowEndpointGroup endpoints

DataflowEndpointGroup supports uplink and downlink using a [dataflow endpoint](../APIReference/API_DataflowEndpoint.md "../APIReference/API_DataflowEndpoint.md"), and downlink-only for an [AWS Ground Station Agent endpoint](../APIReference/API_AwsGroundStationAgentEndpoint.md "../APIReference/API_AwsGroundStationAgentEndpoint.md"). For both types of endpoints, you will create the supporting constructs (e.g. IP
addresses) prior to creating the dataflow endpoint group.
Please see [Work with dataflows](dataflows.md "dataflows.md") for recommendations on which
dataflow endpoint type to use and how to set up the supporting constructs.

The following sections describe both supported endpoint types.

###### Important

All dataflow endpoints within a single dataflow endpoint group must be of the same type. You cannot mix
[AWS Ground Station Agent endpoints](../APIReference/API_AwsGroundStationAgentEndpoint.md "../APIReference/API_AwsGroundStationAgentEndpoint.md") with
[Dataflow endpoints](../APIReference/API_DataflowEndpoint.md "../APIReference/API_DataflowEndpoint.md")
in the same group. If your use case requires both types of endpoints, you must create separate dataflow endpoint
groups for each type.

For DataflowEndpointGroupV2, you can mix [UplinkAwsGroundStationAgentEndpoint](../APIReference/API_UplinkAwsGroundStationAgentEndpoint.md "../APIReference/API_UplinkAwsGroundStationAgentEndpoint.md") and [DownlinkAwsGroundStationAgentEndpoint](../APIReference/API_DownlinkAwsGroundStationAgentEndpoint.md "../APIReference/API_DownlinkAwsGroundStationAgentEndpoint.md")
in the same group.

#### AWS Ground Station Agent endpoint

The AWS Ground Station Agent Endpoint utilizes the AWS Ground Station Agent as a software component
to terminate connections. To construct an AWS Ground Station Agent Endpoint, you will only
populate the `AwsGroundStationAgentEndpoint` field of the EndpointDetails. For more
information about the AWS Ground Station Agent, see the full
[AWS Ground Station Agent User Guide](../gs-agent-ug.md "../gs-agent-ug.md").

The `AwsGroundStationAgentEndpoint` consists of the following:

- `Name` - The dataflow endpoint name. For the contact to use this dataflow endpoint, this name must match the name used in your dataflow endpoint config.
- `EgressAddress` - The IP and port address used to egress data from the Agent.
- `IngressAddress` - The IP and port address used to ingress data to the Agent.

#### Dataflow endpoint

The Dataflow Endpoint utilizes a networking application as a software component to terminate
connections. Use Dataflow Endpoint when you want to uplink Digital Signal Data, downlink
less-than 50MHz of Digital Signal Data, or downlink Demodulated/Decoded Signal Data. To
construct a Dataflow Endpoint, you will populate the `Endpoint` and
`Security Details` fields of the EndpointDetails.

The `Endpoint` consists of the following:

- `Name` - The dataflow endpoint name. For the contact to use this dataflow endpoint, this name must match the name used in your dataflow endpoint config.
- `Address` - The IP and port address used.

The `SecurityDetails` consists of the following:

- `roleArn` - The Amazon Resource Name (ARN) of a role that AWS Ground Station will assume to create Elastic Network Interfaces (ENIs) in your VPC.
  These ENIs serve as the ingress and egress points of data streamed during a contact.
- `securityGroupIds` - The security groups to attach to the elastic network interfaces.
- `subnetIds` - A list of subnets where AWS Ground Station may place elastic network interfaces to send streams to your instances.
  If multiple subnets are specified, they must be routable to one another.
  If the subnets are in different Availability Zones (AZs), you may incur cross-AZ data transfer charges.

The IAM role passed into `roleArn` must have a trust policy that allows the `groundstation.amazonaws.com` service principal to assume the role.
See the [Example Trust Policy](#dataflow-endpoint-trust-policy-example "#dataflow-endpoint-trust-policy-example") section below for an example. During endpoint creation the endpoint resource id does not exist,
so the trust policy must use an asterisk (`*`) in place of `your-endpoint-id`. This can be updated after creation to use the endpoint resource id in order to scope the trust policy to that specific dataflow endpoint group.

The IAM role must have an IAM policy that allows AWS Ground Station to set up the ENIs. See the [Example Role Policy](#dataflow-endpoint-role-policy-example "#dataflow-endpoint-role-policy-example") section below for an example.

For more information on how to update a role's trust policy, see
[Managing IAM roles](../../../IAM/latest/UserGuide/id_roles_manage.md "../../../IAM/latest/UserGuide/id_roles_manage.md") in the IAM User Guide.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "groundstation.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`999999999999`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:groundstation:`us-east-1`:`999999999999`:dataflow-endpoint-group/`your-endpoint-id`"
 }
 }
 }
 ]
}`

```

For more information on how to update or attach a role policy, see
[Managing IAM policies](../../../IAM/latest/UserGuide/access_policies_manage.md "../../../IAM/latest/UserGuide/access_policies_manage.md") in the IAM User Guide.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface",
 "ec2:DeleteNetworkInterface",
 "ec2:CreateNetworkInterfacePermission",
 "ec2:DeleteNetworkInterfacePermission",
 "ec2:DescribeSubnets",
 "ec2:DescribeVpcs",
 "ec2:DescribeSecurityGroups"
 ],
 "Resource": "*"
 }
 ]
}`

```

### DataflowEndpointGroupV2 endpoints

DataflowEndpointGroupV2 introduces specialized endpoint types that provide clearer configuration and enhanced functionality:

- **[UplinkAwsGroundStationAgentEndpoint](../APIReference/API_UplinkAwsGroundStationAgentEndpoint.md "../APIReference/API_UplinkAwsGroundStationAgentEndpoint.md")** - Optimized for uplink dataflows
- **[DownlinkAwsGroundStationAgentEndpoint](../APIReference/API_DownlinkAwsGroundStationAgentEndpoint.md "../APIReference/API_DownlinkAwsGroundStationAgentEndpoint.md")** - Optimized for downlink dataflows

These specialized endpoints replace the generic [AwsGroundStationAgentEndpoint](../APIReference/API_AwsGroundStationAgentEndpoint.md "../APIReference/API_AwsGroundStationAgentEndpoint.md") with direction-specific configurations that make it easier to set up and manage your dataflows.

#### Uplink AWS Ground Station Agent endpoint

The [UplinkAwsGroundStationAgentEndpoint](../APIReference/API_UplinkAwsGroundStationAgentEndpoint.md "../APIReference/API_UplinkAwsGroundStationAgentEndpoint.md") is specifically designed for uplink dataflows and provides clearer configuration options. Use this endpoint type when you need to provide data to AWS Ground Station to be uplinked to your satellite.

The `UplinkAwsGroundStationAgentEndpoint` consists of the following:

- `Name` - The dataflow endpoint name. For the contact to use this dataflow endpoint, this name must match the name used in your dataflow endpoint config.
- `IngressAddressAndPort` - Single IP and port address for data input to the agent
- `AgentIpAndPortAddress` - Port range for agent communication

#### Downlink AWS Ground Station Agent endpoint

The [DownlinkAwsGroundStationAgentEndpoint](../APIReference/API_DownlinkAwsGroundStationAgentEndpoint.md "../APIReference/API_DownlinkAwsGroundStationAgentEndpoint.md") is optimized for downlink dataflows, including narrowband downlink, wideband demodulation/decode, and uplink echo scenarios.

The `DownlinkAwsGroundStationAgentEndpoint` consists of the following:

- `Name` - The dataflow endpoint name. For the contact to use this dataflow endpoint, this name must match the name used in your dataflow endpoint config.
- `EgressAddressAndPort` - Single IP and port address for data output from the agent
- `AgentIpAndPortAddress` - Port range for agent communication

## Creating dataflow endpoint groups

You can create dataflow endpoint groups using either version:

### CreateDataflowEndpointGroup

Use [CreateDataflowEndpointGroup](../APIReference/API_CreateDataflowEndpointGroup.md "../APIReference/API_CreateDataflowEndpointGroup.md") for backward compatibility or when you need to use the generic [AwsGroundStationAgentEndpoint](../APIReference/API_AwsGroundStationAgentEndpoint.md "../APIReference/API_AwsGroundStationAgentEndpoint.md") or [DataflowEndpoint](../APIReference/API_DataflowEndpoint.md "../APIReference/API_DataflowEndpoint.md") types.

### CreateDataflowEndpointGroupV2

Use [CreateDataflowEndpointGroupV2](../APIReference/API_CreateDataflowEndpointGroupV2.md "../APIReference/API_CreateDataflowEndpointGroupV2.md") for new implementations to take advantage of specialized endpoint types that support both uplink and downlink dataflows. This API only supports [UplinkAwsGroundStationAgentEndpoint](../APIReference/API_UplinkAwsGroundStationAgentEndpoint.md "../APIReference/API_UplinkAwsGroundStationAgentEndpoint.md") and [DownlinkAwsGroundStationAgentEndpoint](../APIReference/API_DownlinkAwsGroundStationAgentEndpoint.md "../APIReference/API_DownlinkAwsGroundStationAgentEndpoint.md").

## Migration considerations

If you're currently using DataflowEndpointGroup, you can continue using your existing configuration without changes. AWS Ground Station maintains full backward compatibility.

If you'd like to migrate to use the new DataflowEndpointGroupV2, and are currently using a [DataflowEndpoint](../APIReference/API_DataflowEndpoint.md "../APIReference/API_DataflowEndpoint.md") with a Dataflow Endpoint Application to receive your data, you'll need to migrate to use the AWS Ground Station Agent instead. If you're already using an AWS Ground Station Agent for downlink, you can use the same agent instance for uplink as well - no additional agent instances are required.

To migrate to DataflowEndpointGroupV2:

1. If migrating from DataflowEndpoint, set up the AWS Ground Station Agent following the [AWS Ground Station Agent User Guide](../gs-agent-ug.md "../gs-agent-ug.md")
2. Identify your dataflow direction and create the appropriate endpoint type ([UplinkAwsGroundStationAgentEndpoint](../APIReference/API_UplinkAwsGroundStationAgentEndpoint.md "../APIReference/API_UplinkAwsGroundStationAgentEndpoint.md") or [DownlinkAwsGroundStationAgentEndpoint](../APIReference/API_DownlinkAwsGroundStationAgentEndpoint.md "../APIReference/API_DownlinkAwsGroundStationAgentEndpoint.md"))
3. Create the [DataflowEndpointGroupV2](../APIReference/API_CreateDataflowEndpointGroupV2.md "../APIReference/API_CreateDataflowEndpointGroupV2.md") referencing those endpoints
4. Create a new [dataflow endpoint config](../APIReference/API_CreateConfig.md "../APIReference/API_CreateConfig.md") that references the new DataflowEndpointGroupV2 by name
5. Create a new mission profile that references the dataflow endpoint config as a dataflow edge
6. Use the new mission profile to schedule contacts
7. Test your configuration before deploying to production

For more information about the complete workflow, see [Understand AWS Ground Station Core components](how-it-works.md "how-it-works.md") and [Create configs](getting-started.md "getting-started.md").
