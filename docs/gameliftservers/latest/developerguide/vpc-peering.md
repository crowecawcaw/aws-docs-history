# VPC peering for Amazon GameLift Servers

This topic provides guidance on how to set up a VPC peering connection between your
Amazon GameLift Servers-hosted game servers and your other non-Amazon GameLift Servers resources. Use Amazon Virtual Private Cloud (VPC) peering
connections to enable your game servers to communicate directly and privately with your
other AWS resources, such as a web service or a repository. You can establish VPC peering
with any resources that run on AWS and are managed by an AWS account that you have
access to.

###### Note

VPC peering is an advanced feature. To learn about preferred options for enabling your
game servers to communicate directly and privately with your other AWS resources, see
[Communicate with other AWS resources from
your fleets](gamelift-sdk-server-resources.md "gamelift-sdk-server-resources.md").

If you're already familiar with Amazon VPCs and VPC peering, understand that setting up peering
with Amazon GameLift Servers game servers is somewhat different. You don't have access to the VPC that
contains your game servers—it is controlled by the Amazon GameLift Servers service—so you can't
directly request VPC peering for it. Instead, you first pre-authorize the VPC with your
non-Amazon GameLift Servers resources to accept a peering request from the Amazon GameLift Servers service. Then you trigger
Amazon GameLift Servers to request the VPC peering that you just authorized. Amazon GameLift Servers handles the tasks of
creating the peering connection, setting up the route tables, and configuring the
connection.

## To set up VPC peering for an existing

fleet

1. ###### Get AWS account ID(s) and credentials.

You need an ID and sign-in credentials for the following AWS accounts. You
can find AWS account IDs by signing into the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") and viewing your account settings. To get credentials, go
to the IAM console.

    * AWS account that you use to manage your Amazon GameLift Servers game servers.
    * AWS account that you use to manage your non-Amazon GameLift Servers resources.

If you're using the same account for Amazon GameLift Servers and non-Amazon GameLift Servers resources, you need
ID and credentials for that account only. 2. ###### Get identifiers for each VPC.

Get the following information for the two VPCs to be peered:

    * VPC for your Amazon GameLift Servers game servers – This is your Amazon GameLift Servers fleet ID.
     Your game servers are deployed in Amazon GameLift Servers on a fleet of EC2 instances. A
     fleet is automatically placed in its own VPC, which is managed by the
     Amazon GameLift Servers service. You don't have direct access to the VPC, so it is
     identified by the fleet ID.
    * VPC for your non-Amazon GameLift Servers AWS resources – You can establish a
     VPC peering with any resources that run on AWS and are managed by an
     AWS account that you have access to. If you haven't already created a
     VPC for these resources, see [Getting started with
     Amazon VPC](../../../vpc/latest/userguide/getting-started-ipv4.md "../../../vpc/latest/userguide/getting-started-ipv4.md"). Once you have created a VPC, you can find the
     VPC ID by signing into the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") for Amazon VPC and viewing your VPCs.

###### Note

When setting up a peering, both VPCs must exist in the same region. The
VPC for your Amazon GameLift Servers fleet game servers is in the same region as the
fleet. 3. ###### Authorize a VPC peering.

In this step, you are pre-authorizing a future request from Amazon GameLift Servers to peer the
VPC with your game servers with your VPC for non-Amazon GameLift Servers resources. This action
updates the security group for your VPC.

To authorize the VPC peering, call the service API [CreateVpcPeeringAuthorization()](../../../gamelift/latest/apireference/API_CreateVpcPeeringAuthorization.md "../../../gamelift/latest/apireference/API_CreateVpcPeeringAuthorization.md") or use the AWS CLI command
`create-vpc-peering-authorization`. Make this call using the
account that manages your non-Amazon GameLift Servers resources. Identify the following
information:

    * Peer VPC ID – This is for the VPC with your non-Amazon GameLift Servers
     resources.
    * Amazon GameLift Servers AWS account ID – This is the account that you use to
     manage your Amazon GameLift Servers fleet.

Once you've authorized a VPC peering, the authorization remains valid for 24
hours unless revoked. You can manage your VPC peering authorizations using the
following operations:

    * [DescribeVpcPeeringAuthorizations()](../../../gamelift/latest/apireference/API_DescribeVpcPeeringAuthorizations.md "../../../gamelift/latest/apireference/API_DescribeVpcPeeringAuthorizations.md") (AWS CLI
     `describe-vpc-peering-authorizations`).
    * [DeleteVpcPeeringAuthorization()](../../../gamelift/latest/apireference/API_DeleteVpcPeeringAuthorization.md "../../../gamelift/latest/apireference/API_DeleteVpcPeeringAuthorization.md") (AWS CLI
     `delete-vpc-peering-authorization`).

4. ###### Request a peering connection.

With a valid authorization, you can request that Amazon GameLift Servers establish a peering
connection.

To request a VPC peering, call the service API [CreateVpcPeeringConnection()](../../../gamelift/latest/apireference/API_CreateVpcPeeringConnection.md "../../../gamelift/latest/apireference/API_CreateVpcPeeringConnection.md") or use the AWS CLI command
`create-vpc-peering-connection`. Make this call using the account
that manages your Amazon GameLift Servers game servers. Use the following information to identify
the two VPCs that you want to peer:

    * Peer VPC ID and AWS account ID – This is the VPC for your
     non-Amazon GameLift Servers resources and the account that you use to manage them. The VPC
     ID must match the ID on a valid peering authorization.
    * Fleet ID – This identifies the VPC for your Amazon GameLift Servers game
     servers.

5. ###### Track the peering connection status.

Requesting a VPC peering connection is an asynchronous operation. To track the
status of a peering request and handle success or failure cases, use one of the
following options:

    * Continuously poll with `DescribeVpcPeeringConnections()`.
     This operation retrieves the VPC peering connection record, including
     the status of the request. If a peering connection is successfully
     created, the connection record also contains a CIDR block of private IP
     addresses that is assigned to the VPC.
    * Handle fleet events associated with VPC peering connections with
     [DescribeFleetEvents()](../../../gamelift/latest/apireference/API_DescribeFleetEvents.md "../../../gamelift/latest/apireference/API_DescribeFleetEvents.md"), including success and failure
     events.

Once the peering connection is established, you can manage it using the following
operations:

- [DescribeVpcPeeringConnections()](../../../gamelift/latest/apireference/API_DescribeVpcPeeringConnections.md "../../../gamelift/latest/apireference/API_DescribeVpcPeeringConnections.md") (AWS CLI
  `describe-vpc-peering-connections`).
- [DeleteVpcPeeringConnection()](../../../gamelift/latest/apireference/API_DeleteVpcPeeringConnection.md "../../../gamelift/latest/apireference/API_DeleteVpcPeeringConnection.md") (AWS CLI
  `delete-vpc-peering-connection`).

## To set up VPC peering with a new

fleet

You can create a new Amazon GameLift Servers fleet and request a VPC peering connection at the same
time.

1. ###### Get AWS account ID(s) and credentials.

You need an ID and sign-in credentials for the following two AWS accounts.
You can find AWS account IDs by signing into the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") and viewing your account
settings. To get credentials, go to the IAM console.

    * AWS account that you use to manage your Amazon GameLift Servers game servers.
    * AWS account that you use to manage your non-Amazon GameLift Servers resources.

If you're using the same account for Amazon GameLift Servers and non-Amazon GameLift Servers resources, you need
ID and credentials for that account only. 2. ###### Get the VPC ID for your non-Amazon GameLift ServersAWS resources.

If you haven't already created a VPC for these resources, do so now (see
[Getting started with
Amazon VPC](../../../vpc/latest/userguide/getting-started-ipv4.md "../../../vpc/latest/userguide/getting-started-ipv4.md")). Be sure that you create the new VPC in the same region
where you plan to create your new fleet. If your non-Amazon GameLift Servers resources are managed
under a different AWS account or user/user group than the one you use with
Amazon GameLift Servers, you'll need to use these account credentials when requesting
authorization in the next step.

Once you have created a VPC, you can locate the VPC ID in Amazon VPC console
by viewing your VPCs. 3. ###### Authorize a VPC peering with non-Amazon GameLift Servers resources.

When Amazon GameLift Servers creates the new fleet and a corresponding VPC, it also sends a
request to peer with the VPC for your non-Amazon GameLift Servers resources. You need to
pre-authorize that request. This step updates the security group for your
VPC.

Using the account credentials that manage your non-Amazon GameLift Servers resources, call the
service API [CreateVpcPeeringAuthorization()](../../../gamelift/latest/apireference/API_CreateVpcPeeringAuthorization.md "../../../gamelift/latest/apireference/API_CreateVpcPeeringAuthorization.md") or use the AWS CLI command
`create-vpc-peering-authorization`. Identify the following
information:

    * Peer VPC ID – ID of the VPC with your non-Amazon GameLift Servers
     resources.
    * Amazon GameLift Servers AWS account ID – ID of the account that you use to
     manage your Amazon GameLift Servers fleet.

Once you've authorized a VPC peering, the authorization remains valid for 24
hours unless revoked. You can manage your VPC peering authorizations using the
following operations:

    * [DescribeVpcPeeringAuthorizations()](../../../gamelift/latest/apireference/API_DescribeVpcPeeringAuthorizations.md "../../../gamelift/latest/apireference/API_DescribeVpcPeeringAuthorizations.md") (AWS CLI
     `describe-vpc-peering-authorizations`).
    * [DeleteVpcPeeringAuthorization()](../../../gamelift/latest/apireference/API_DeleteVpcPeeringAuthorization.md "../../../gamelift/latest/apireference/API_DeleteVpcPeeringAuthorization.md") (AWS CLI
     `delete-vpc-peering-authorization`).

4. Follow the instructions for [creating a
   new fleet using the AWS CLI](fleets-creating.md "fleets-creating.md"). Include the following additional
   parameters:
   - _peer-vpc-aws-account-id_ – ID
     for the account that you use to manage the VPC with your non-Amazon GameLift Servers
     resources.
   - _peer-vpc-id_ – ID of the VPC
     with your non-Amazon GameLift Servers account.

A successful call to [create-fleet](../../../cli/latest/reference/gamelift/create-fleet.md "../../../cli/latest/reference/gamelift/create-fleet.md") with the VPC peering parameters generates both a new fleet and
a new VPC peering request. The fleet's status is set to **New** and the fleet activation process is initiated. The peering
connection request's status is set to **initiating-request**. You can track the success or failure of the peering
request by calling [describe-vpc-peering-connections](../../../cli/latest/reference/gamelift/describe-vpc-peering-connections.md "../../../cli/latest/reference/gamelift/describe-vpc-peering-connections.md").

When requesting both a new fleet and a VPC peering connection, both actions either
succeed or fail. If a fleet fails during the creation process, the VPC peering
connection will not be established. Likewise, if a VPC peering connection fails for any
reason, the new fleet will fail to move from status **Activating** to **Active**.

###### Note

The new VPC peering connection is not completed until the fleet is ready to become
active. This means that the connection is not available and can't be used during the
game server build installation process.

The following example creates both a new fleet and a peering connection between a
pre-established VPC and the VPC for the new fleet. The pre-established VPC is uniquely
identified by the combination of your non-Amazon GameLift Servers AWS account ID and the VPC ID.

```
$ AWS gamelift create-fleet
    --name "My_Fleet_1"
    --description "The sample test fleet"
    --ec2-instance-type "c5.large"
    --fleet-type "ON_DEMAND"
    --build-id "build-1111aaaa-22bb-33cc-44dd-5555eeee66ff"
    --runtime-configuration "GameSessionActivationTimeoutSeconds=300,
                             MaxConcurrentGameSessionActivations=2,
                             ServerProcesses=[{LaunchPath=C:\game\Bin64.dedicated\MultiplayerSampleProjectLauncher_Server.exe,
                                               Parameters=+sv_port 33435 +start_lobby,
                                               ConcurrentExecutions=10}]"
    --new-game-session-protection-policy "FullProtection"
    --resource-creation-limit-policy "NewGameSessionsPerCreator=3,
                                      PolicyPeriodInMinutes=15"
    --ec2-inbound-permissions "FromPort=33435,ToPort=33435,IpRange=0.0.0.0/0,Protocol=UDP"
                              "FromPort=33235,ToPort=33235,IpRange=0.0.0.0/0,Protocol=UDP"
    --metric-groups  "EMEAfleets"
    --peer-vpc-aws-account-id "111122223333"
    --peer-vpc-id "vpc-a11a11a"
```

_Copyable version:_

```
AWS gamelift create-fleet --name "My_Fleet_1" --description "The sample test fleet" --fleet-type "ON_DEMAND" --metric-groups "EMEAfleets" --build-id "build-1111aaaa-22bb-33cc-44dd-5555eeee66ff" --ec2-instance-type "c5.large" --runtime-configuration "GameSessionActivationTimeoutSeconds=300,MaxConcurrentGameSessionActivations=2,ServerProcesses=[{LaunchPath=C:\game\Bin64.dedicated\MultiplayerSampleProjectLauncher_Server.exe,Parameters=+sv_port 33435 +start_lobby,ConcurrentExecutions=10}]" --new-game-session-protection-policy "FullProtection" --resource-creation-limit-policy "NewGameSessionsPerCreator=3,PolicyPeriodInMinutes=15" --ec2-inbound-permissions "FromPort=33435,ToPort=33435,IpRange=0.0.0.0/0,Protocol=UDP" "FromPort=33235,ToPort=33235,IpRange=0.0.0.0/0,Protocol=UDP" --peer-vpc-aws-account-id "111122223333" --peer-vpc-id "vpc-a11a11a"
```

## Troubleshooting VPC peering issues

If you're having trouble establishing a VPC peering connection for your Amazon GameLift Servers game
servers, consider these common root causes:

- An authorization for the requested connection was not found:
  - Check the status of a VPC authorization for the non-Amazon GameLift Servers VPC. It
    might not exist or it might have expired.
  - Check the regions of the two VPCs you're trying to peer. If they're
    not in the same region, they can't be peered.

- The CIDR blocks (see [Invalid VPC peering connection configurations](../../../vpc/latest/peering/invalid-peering-configurations.md#overlapping-cidr "../../../vpc/latest/peering/invalid-peering-configurations.md#overlapping-cidr")) of your two VPCs are
  overlapping. The IPv4 CIDR blocks that are assigned to peered VPCs cannot
  overlap. The CIDR block of the VPC for your Amazon GameLift Servers fleet is automatically
  assigned and can't be changed, so you'll need to change the CIDR block for of
  the VPC for your non-Amazon GameLift Servers resources. To resolve this issue:
  - Look up this CIDR block for your Amazon GameLift Servers fleet by calling
    `DescribeVpcPeeringConnections()`.
  - Go to the Amazon VPC console, find the VPC for your non-Amazon GameLift Servers
    resources, and change the CIDR block so that they don't overlap.

- The new fleet did not activate (when requesting VPC peering with a new fleet).
  If the new fleet failed to progress to **Active**
  status, there is no VPC to peer with, so the peering connection cannot
  succeed.
