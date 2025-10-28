# Setting up Neptune-to-Neptune replication

Your primary production DB cluster resides in a VPC in a given source region.
There are three main things that you need to replicate or emulate in a different,
recovery region for the purposes of disaster recovery:

- The data stored in the cluster.
- The configuration of the primary cluster. This would include whether it uses
  IAM authentication, whether it is encrypted, its DB cluster parameters, its instance
  parameters, instance sizes, and so forth).
- The networking topology it uses, including the target VPC, its security
  groups, and so forth.
  You can use Neptune management APIs such as the following to gather that information:

- [DescribeDBClusters](api-clusters.md#DescribeDBClusters "api-clusters.md#DescribeDBClusters")
- [DescribeDBInstances](api-instances.md#DescribeDBInstances "api-instances.md#DescribeDBInstances")
- [DescribeDBClusterParameters](api-parameters.md#DescribeDBClusterParameters "api-parameters.md#DescribeDBClusterParameters")
- [DescribeDBParameters](api-parameters.md#DescribeDBParameters "api-parameters.md#DescribeDBParameters")
- [`DescribeVpcs`](../../../AWSEC2/latest/APIReference/API_DescribeVpcs.md "../../../AWSEC2/latest/APIReference/API_DescribeVpcs.md")
  With the information you gather, you can use the following procedure to set up a
  backup cluster in a different region, to which your production cluster can fail over
  in the event of a failure.

## Enable Neptune streams

You can use the [ModifyDBClusterParameterGroup](api-parameters.md#ModifyDBClusterParameterGroup "api-parameters.md#ModifyDBClusterParameterGroup") to set the `neptune_streams`
parameter to 1. Then, reboot all the instances in the DB cluster so that change takes
effect.

It's a good idea to perform at least one add or update operation on the source
DB cluster after Neptune streams has been enabled. This populates the change stream
with data points that can be referenced later when re-syncing the production cluster
with the backup cluster.

## Create a new VPC in the region where you want to set up your backup cluster

Before creating a new Neptune DB cluster in a different region from your primary
cluster, you need to establish a new VPC in the target region to host the cluster.
Connectivity between the primary and backup clusters is established through VPC peering,
which uses traffic across private subnets in different VPCs. However, to establish
VPC peering between two VPCs, they must not have overlapping CIDR blocks or IP address
spaces. This that you can't just use the default VPC in both regions, because the CIDR
block for a default VPC is always the same (`172.31.0.0/16`).

You can use an existing VPC in the target region as long as it meets the following
conditions:

- It does not have a CIDR block that overlaps with the CIDR block of the
  VPC where your primary cluster is located.
- It is not already peered with another VPC that has the same CIDR block
  as the VPC where your primary cluster is located.

If there is no suitable VPC available in the target region, create one using the
Amazon EC2 [`CreateVpc`](../../../AWSEC2/latest/APIReference/API_CreateVpc.md "../../../AWSEC2/latest/APIReference/API_CreateVpc.md") API.

## Create a snapshot of your primary cluster and restore it to the target backup region

Now you create a new Neptune cluster in an appropriate VPC in the target backup
region that is a copy of your production cluster:

###### Make a copy of your production cluster in the backup region

1. In your target backup region, re-create the parameters and parameter groups
   used by your production DB cluster. You can do this using [CreateDBClusterParameterGroup](api-parameters.md#CreateDBClusterParameterGroup "api-parameters.md#CreateDBClusterParameterGroup"), [CreateDBParameterGroup](api-parameters.md#CreateDBParameterGroup "api-parameters.md#CreateDBParameterGroup"), [ModifyDBClusterParameterGroup](api-parameters.md#ModifyDBClusterParameterGroup "api-parameters.md#ModifyDBClusterParameterGroup") and [ModifyDBParameterGroup](api-parameters.md#ModifyDBParameterGroup "api-parameters.md#ModifyDBParameterGroup").

Note that the [CopyDBClusterParameterGroup](api-parameters.md#CopyDBClusterParameterGroup "api-parameters.md#CopyDBClusterParameterGroup") and
[CopyDBParameterGroup](api-parameters.md#CopyDBParameterGroup "api-parameters.md#CopyDBParameterGroup") APIs do
not currently support cross-region copying. 2. Use [CreateDBClusterSnapshot](api-snapshots.md#CreateDBClusterSnapshot "api-snapshots.md#CreateDBClusterSnapshot") to
create a snapshot of your production cluster in the VPC in your production region. 3. Use [CopyDBClusterSnapshot](api-snapshots.md#CopyDBClusterSnapshot "api-snapshots.md#CopyDBClusterSnapshot") to
copy the snapshot to the VPC in your target backup region. 4. Use [RestoreDBClusterFromSnapshot](api-snapshots.md#RestoreDBClusterFromSnapshot "api-snapshots.md#RestoreDBClusterFromSnapshot") to
create a new DB cluster in the VPC in your target backup region using the copied snapshot.
Use the configuration settings and parameters that you copied from your primary production
cluster. 5. The new Neptune cluster now exists but doesn't contain any instances. Use [CreateDBInstance](api-instances.md#CreateDBInstance "api-instances.md#CreateDBInstance") to create a new
primary/writer instance that has the same instance type and size as your production
cluster's writer instance. There's no need to create additional read-replicas at this point
unless your backup instance will be used to service read I/O in the target region prior
to a failover.

## Establish VPC peering between your primary cluster's VPC and your new backup cluster's VPC

By setting up VPC peering, you enable your primary cluster's VPC to communicate
with your backup cluster's VPC as if they are a single private network. To do this,
take the following steps:

1. From your production cluster's VPC, call the [`CreateVpcPeeringConnection`](../../../AWSEC2/latest/APIReference/CreateVpcPeeringConnection.md "../../../AWSEC2/latest/APIReference/CreateVpcPeeringConnection.md")
   API to establish the peering connection.
2. From your target backup cluster's VPC, call the [`AcceptVpcPeeringConnection`](../../../AWSEC2/latest/APIReference/AcceptVpcPeeringConnection.md "../../../AWSEC2/latest/APIReference/AcceptVpcPeeringConnection.md")
   API to accept the peering connection.
3. From your production cluster's VPC, use the [`CreateRoute`](../../../AWSEC2/latest/APIReference/CreateRoute.md "../../../AWSEC2/latest/APIReference/CreateRoute.md") API to add a route
   to the VPC's route table that redirects all traffic to the target VPC's CIDR block
   so that it uses the VPC peering prefix list.
4. Similarly, from your target backup cluster's VPC, use the [`CreateRoute`](../../../AWSEC2/latest/APIReference/CreateRoute.md "../../../AWSEC2/latest/APIReference/CreateRoute.md") API to add a route
   to the VPC's route table that routes traffic to the primary cluster's VPC.

## Set up the Neptune streams replication infrastructure

Now that both clusters are deployed and network communication between both regions
has been established, use the [Neptune-to-Neptune AWS CloudFormation template](streams-consumer-setup.md "streams-consumer-setup.md")
to deploy the Neptune streams consumer Lambda function with the additional infrastructure
that supports data replication. Do this in your primary production cluster's VPC.

The parameters that you will need to provide for this AWS CloudFormation stack are:

- **`NeptuneStreamEndpoint`**   –  
  The stream endpoint for the primary cluster, in URL format. For example:
  `https://`(cluster name)`:8182/pg/stream`.
- **`QueryEngine`**   –  
  This must be either `gremlin`, `sparql`, or `openCypher`.
- **`RouteTableIds`**   –  
  Lets you add routes for both a DynamoDB VPC Endpoint and a monitoring VPC Endpoint.

Two additional parameters, namely `CreateMonitoringEndpoint` and
`CreateDynamoDBEndpoint`, must also be set to true if they do not
already exists on the primary cluster's VPC. If they do already exist, make sure
they are set to false or the AWS CloudFormation creation will fail.

- **`SecurityGroupIds`**   –  
  Specifies the security group used by the Lambda consumer to communicate with the
  primary cluster's Neptune stream endpoint.

In the target backup cluster, attach a security group that allows traffic
originating from this security group.

- **`SubnetIds`**   –  
  A list of subnet ID in the primary cluster's VPC that can be used by the Lambda
  consumer to communicate with the primary cluster.
- **`TargetNeptuneClusterEndpoint`**   –  
  The cluster endpoint (hostname only) of the target backup cluster.
- **`TargetAWSRegion`**   –  
  The target backup cluster's AWS region, such as `us-east-1`).
  You must provide this parameter only when the AWS region of the target backup
  cluster is different from the region of the Neptune source cluster, as in
  the case of cross-region replication. If the source and target regions
  are the same, this parameter is optional.

Note that if the `TargetAWSRegion` value is not a [valid AWS region that Neptune supports](limits.md#limits-regions "limits.md#limits-regions"),
the process fails.

- **`VPC`**   –  
  The ID of the primary cluster's VPC.

All other parameters can be left with their default values.

Once the AWS CloudFormation template has been deployed, Neptune will begin replicating
any changes from the primary cluster to the backup cluster. You can monitor this
replication in the CloudWatch logs generated by the Lambda consumer function.
