# Using Amazon Keyspaces with interface VPC endpoints

Interface VPC endpoints enable private communication between your virtual private cloud
(VPC) running in Amazon VPC and Amazon Keyspaces. Interface VPC endpoints are powered by AWS PrivateLink,
which is an AWS service that enables private communication between VPCs and AWS
services.

AWS PrivateLink enables this by using an elastic network interface with private IP addresses
in your VPC so that network traffic does not leave the Amazon network. Interface VPC
endpoints don't require an internet gateway, NAT device, VPN connection, or AWS Direct Connect
connection. For more information, see [Amazon Virtual Private Cloud](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md") and
[Interface VPC endpoints (AWS PrivateLink)](../../../vpc/latest/privatelink/vpce-interface.md "../../../vpc/latest/privatelink/vpce-interface.md").

###### Topics

- [Using interface VPC endpoints for
  Amazon Keyspaces](#using-interface-vpc-endpoints "#using-interface-vpc-endpoints")
- [Populating system.peers table entries with
  interface VPC endpoint information](#system_peers "#system_peers")
- [Controlling access to interface VPC
  endpoints for Amazon Keyspaces](#interface-vpc-endpoints-policies "#interface-vpc-endpoints-policies")
- [Availability](#availability "#availability")
- [VPC endpoint policies and Amazon Keyspaces point-in-time
  recovery (PITR)](#VPC_PITR_restore "#VPC_PITR_restore")
- [Common errors and warnings](#vpc_troubleshooting "#vpc_troubleshooting")

## Using interface VPC endpoints for

Amazon Keyspaces

You can create an interface VPC endpoint so that traffic between Amazon Keyspaces and your Amazon VPC
resources starts flowing through the interface VPC endpoint. To get started, follow
the steps to [create an
interface endpoint](../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint"). Next, edit the security group associated with the
endpoint that you created in the previous step, and configure an inbound rule for port 9142. For more information, see [Adding, removing, and
updating rules](../../../vpc/latest/userguide/VPC_SecurityGroups.md#AddRemoveRules "../../../vpc/latest/userguide/VPC_SecurityGroups.md#AddRemoveRules").

For a step-by-step tutorial to configure a connection to Amazon Keyspaces through a VPC endpoint,
see [Tutorial: Connect to Amazon Keyspaces using an interface VPC
endpoint](vpc-endpoints-tutorial.md "vpc-endpoints-tutorial.md"). To learn how to configure cross-account
access for Amazon Keyspaces resources separated from applications in different AWS accounts in a VPC, see [Configure cross-account access to Amazon Keyspaces with VPC endpoints](access.md "access.md").

## Populating `system.peers` table entries with

interface VPC endpoint information

Apache Cassandra drivers use the `system.peers` table to query for node
information about the cluster. Cassandra drivers use the node information to load
balance connections and retry operations. Amazon Keyspaces populates nine entries in the
`system.peers` table automatically for clients connecting through the
public endpoint.

To provide clients connecting through interface VPC endpoints with similar
functionality, Amazon Keyspaces populates the `system.peers` table in your account with
an entry for each Availability Zone where a VPC endpoint is available. To look up and
store available interface VPC endpoints in the `system.peers` table, Amazon Keyspaces
requires that you grant the IAM entity used to connect to Amazon Keyspaces access permissions to
query your VPC for the endpoint and network interface information.

###### Important

Populating the `system.peers` table with your available interface VPC
endpoints improves load balancing and increases read/write throughput. It is
recommended for all clients accessing Amazon Keyspaces using interface VPC endpoints and is required for Apache Spark.

To grant the IAM entity used to connect to Amazon Keyspaces permissions to look up the
necessary interface VPC endpoint information, you can update your existing IAM role or
user policy, or create a new IAM policy as shown in the following example.

```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Sid":"ListVPCEndpoints",
         "Effect":"Allow",
         "Action":[
            "ec2:DescribeNetworkInterfaces",
            "ec2:DescribeVpcEndpoints"
         ],
         "Resource":"*"
      }
   ]
}
```

###### Note

The managed policies `AmazonKeyspacesReadOnlyAccess_v2` and
`AmazonKeyspacesFullAccess` include the required permissions to let Amazon Keyspaces
access the Amazon EC2 instance to read information about available interface VPC endpoints.

To confirm that the policy has been set up correctly, query the
`system.peers` table to see networking information. If the
`system.peers` table is empty, it could indicate that the policy hasn't
been configured successfully or that you have exceeded the request rate quota for
`DescribeNetworkInterfaces` and `DescribeVPCEndpoints` API
actions. `DescribeVPCEndpoints` falls into the `Describe*`
category and is considered a _non-mutating action_.
`DescribeNetworkInterfaces` falls into the subset of _unfiltered
and unpaginated non-mutating actions_, and different quotas apply. For
more information, see [Request token bucket
sizes and refill rates](../../../AWSEC2/latest/APIReference/throttling.md#throttling-limits-rate-based "../../../AWSEC2/latest/APIReference/throttling.md#throttling-limits-rate-based") in the Amazon EC2 API Reference.

If you do see an empty table, try again a few minutes later to rule out request rate
quota issues. To verify that you have configured the VPC endpoints correctly, see
[My VPC endpoint connection doesn't work properly](troubleshooting.md#troubleshooting.connection.vpce "troubleshooting.md#troubleshooting.connection.vpce"). If your query returns
results from the table, your policy has been configured correctly.

## Controlling access to interface VPC

endpoints for Amazon Keyspaces

With VPC endpoint policies, you can control access to resources in two ways:

- **IAM policy** – You can control the
  requests, users, or groups that are allowed to access Amazon Keyspaces through a specific
  VPC endpoint. You can do this by using a [condition
  key](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the policy that is attached to an IAM user, group, or
  role.
- **VPC policy** – You can control which VPC
  endpoints have access to your Amazon Keyspaces resources by attaching policies to them. To
  restrict access to a specific keyspace or table to only allow traffic coming
  through a specific VPC endpoint, edit the existing IAM policy that restricts
  resource access and add that VPC endpoint.

The following are example endpoint policies for accessing Amazon Keyspaces resources.

- **IAM policy example: Restrict all access to a specific
  Amazon Keyspaces table unless traffic comes from the specified VPC endpoint**
  – This sample policy can be attached to an IAM user, role, or group. It
  restricts access to a specified Amazon Keyspaces table unless incoming traffic originates
  from a specified VPC endpoint.

```
{
   "Version": "2012-10-17",
   "Statement": [
      {
         "Sid": "UserOrRolePolicyToDenyAccess",
         "Action": "cassandra:*",
         "Effect": "Deny",
         "Resource": [
                        "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/mykeyspace/table/mytable",
                        "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/system*"
           ],
         "Condition": { "StringNotEquals" : { "aws:sourceVpce": "vpce-abc123" } }
      }
   ]
}
```

###### Note

To restrict access to a specific table, you must also include access to
the system tables. System tables are read-only.

- **VPC policy example: Read-only access** –
  This sample policy can be attached to a VPC endpoint. (For more information, see
  [Controlling access to Amazon VPC resources](../../../vpc/latest/userguide/vpc-endpoints-access.md#vpc-endpoint-policies "../../../vpc/latest/userguide/vpc-endpoints-access.md#vpc-endpoint-policies")). It restricts actions to
  read-only access to Amazon Keyspaces resources through the VPC endpoint that it's attached
  to.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "ReadOnly",
      "Principal": "*",
      "Action": [
        "cassandra:Select"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
```

- **VPC policy example: Restrict access to a specific Amazon Keyspaces
  table** – This sample policy can be attached to a VPC
  endpoint. It restricts access to a specific table through the VPC endpoint that
  it's attached to.

```
{
   "Version": "2012-10-17",
   "Statement": [
        {
            "Sid": "RestrictAccessToTable",
            "Principal": "*",
            "Action": "cassandra:*",
            "Effect": "Allow",
            "Resource": [
                        "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/mykeyspace/table/mytable",
                        "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/system*"
           ]
        }
   ]
}
```

###### Note

To restrict access to a specific table, you must also include access to
the system tables. System tables are read-only.

## Availability

Amazon Keyspaces supports using interface VPC endpoints in all of the AWS Regions where
the service is available. For more information, see [Service endpoints for Amazon Keyspaces](programmatic.md "programmatic.md").

## VPC endpoint policies and Amazon Keyspaces point-in-time

recovery (PITR)

If you are using IAM policies with [condition keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") to
restrict incoming traffic, the table restore operation may fail. For example,
if you restrict source traffic to specific VPC endpoints using `aws:SourceVpce` condition keys, the table restore operation fails.
To allow Amazon Keyspaces to perform a restore operation on your principal's behalf,
you must add an `aws:ViaAWSService` condition key to your IAM policy. The `aws:ViaAWSService` condition key allows access when any AWS service
makes a request using the principal's credentials. For more information,
see [IAM JSON policy elements: Condition key](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_. The following policy is an example of this.

```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Sid":"CassandraAccessForVPCE",
         "Effect":"Allow",
         "Action":"cassandra:*",
         "Resource":"*",
         "Condition":{
            "Bool":{
               "aws:ViaAWSService":"false"
            },
            "StringEquals":{
               "aws:SourceVpce":[
                  "vpce-12345678901234567"
               ]
            }
         }
      },
      {
         "Sid":"CassandraAccessForAwsService",
         "Effect":"Allow",
         "Action":"cassandra:*",
         "Resource":"*",
         "Condition":{
            "Bool":{
               "aws:ViaAWSService":"true"
            }
         }
      }
   ]
}
```

## Common errors and warnings

**If you're using Amazon Virtual Private Cloud and you connect to Amazon Keyspaces, you might
see the following warning.**

```
`Control node cassandra.us-east-1.amazonaws.com/1.111.111.111:9142 has an entry for itself in system.peers: this entry will be ignored. This is likely due to a misconfiguration;
please verify your rpc_address configuration in cassandra.yaml on all nodes in your cluster.`
```

This warning occurs because the `system.peers` table contains entries for
all of the Amazon VPC endpoints that Amazon Keyspaces has permissions to view, including the Amazon VPC
endpoint that you're connected through. You can safely ignore this warning.

For other errors, see
[My VPC endpoint connection doesn't work properly](troubleshooting.md#troubleshooting.connection.vpce "troubleshooting.md#troubleshooting.connection.vpce").
