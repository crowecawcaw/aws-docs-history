# Connecting your network for AWS DataSync

transfers

If [you need an AWS DataSync agent](do-i-need-datasync-agent.md "do-i-need-datasync-agent.md"), you must
establish several network connections for a data transfer. The
following diagram shows the three network connections in a DataSync transfer from a storage
system (which could be on premises, in another cloud, or at the edge) to an AWS storage
service.

![AWS DataSync network architecture showing three essential connections for data transfer workflow.](images/datasync-network-connection-diagram-overview.png)

## 1. Network connection between your

storage system and agent

Your DataSync agent connects to your on-premises storage or storage in other clouds.
For more information, see [Network requirements for on-premises, self-managed, and other cloud storage](datasync-network.md#on-premises-network-requirements "datasync-network.md#on-premises-network-requirements").

## 2. Network connection between your

agent and DataSync service

There are a few aspects to connecting your agent to the DataSync service. First, you must establish
network connectivity between your storage location and AWS. Second, your agent needs a service endpoint to
communicate with DataSync.

###### Contents

- [Connecting your storage network to
  AWS](networking-datasync.md#connecting-options-to-amazon "networking-datasync.md#connecting-options-to-amazon")
- [Choosing a service endpoint](networking-datasync.md#service-endpoint-options "networking-datasync.md#service-endpoint-options")

### Connecting your storage network to

AWS

When using DataSync, consider the following options for connecting your storage
network to AWS:

- **Direct Connect** - With [Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md"), you can create a dedicated connection between
  your storage network and AWS. From a DataSync perspective, this lets
  you:

      + Transfer data over a private path to your virtual private cloud
       (VPC), which avoids routing over the public internet.
      + Get a more predictable connection than using a virtual private
       network (VPN) to connect your storage network to AWS (particularly
       if your agent is an Amazon EC2 instance).
      + Use any type of DataSync service endpoint, including [public](choose-service-endpoint.md#choose-service-endpoint-public "choose-service-endpoint.md#choose-service-endpoint-public"), [Federal Information
       Processing Standard (FIPS)](choose-service-endpoint.md#choose-service-endpoint-fips "choose-service-endpoint.md#choose-service-endpoint-fips"), or [VPC](choose-service-endpoint.md#datasync-in-vpc "choose-service-endpoint.md#datasync-in-vpc") endpoints.

  For more information, see [DataSync architecture and routing examples with
  Direct Connect](direct-connect-architecture.md "direct-connect-architecture.md").

- **VPN** - You can connect your storage
  network to AWS by using a VPN (such as [AWS Site-to-Site VPN](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md")).
- **Public internet** - You can connect your
  storage network directly to DataSync over the internet by using a [public](choose-service-endpoint.md#choose-service-endpoint-public "choose-service-endpoint.md#choose-service-endpoint-public") or [FIPS](choose-service-endpoint.md#choose-service-endpoint-fips "choose-service-endpoint.md#choose-service-endpoint-fips") service
  endpoint.

### Choosing a service endpoint

Your agent uses a service endpoint to communicate with DataSync. For more
information, see [Choosing a service endpoint for your AWS DataSync
agent](choose-service-endpoint.md "choose-service-endpoint.md").

## 3. Network connection between

DataSync service and AWS storage service

To connect DataSync to an AWS storage service, you just have to make sure that the
DataSync service can access your S3 bucket or file system. For more information, see [Network requirements for
AWS storage services](datasync-network.md#storage-service-network-requirements "datasync-network.md#storage-service-network-requirements").

## Networking when you don't need a

DataSync agent

For transfers that [don't require a DataSync
agent](do-i-need-datasync-agent.md#when-agent-not-required "do-i-need-datasync-agent.md#when-agent-not-required"), you just have to make sure that the DataSync service can access the AWS
storage systems you’re transferring between. For more information, see [Network requirements for
AWS storage services](datasync-network.md#storage-service-network-requirements "datasync-network.md#storage-service-network-requirements").

## How and where DataSync traffic flows through the

network

DataSync has _data plane_ and _control plane_
traffic. Knowing how each of these flows through the network is important if you want to
separate your DataSync traffic.

- **Data plane traffic** – Includes the file
  or object data moving between your storage locations. In most cases, data plane
  traffic routes through [network
  interfaces](required-network-interfaces.md "required-network-interfaces.md") that DataSync automatically generates and manages when you
  create a task. Where these network interfaces get created depends on the type of
  AWS storage service you’re transferring to or from and the service endpoint
  that your DataSync agent uses.
- **Control plane traffic** – Includes
  management activities for your DataSync resources. This traffic routes through the
  service endpoint that your agent uses.

## Network security for DataSync

For information about how your storage data (including metadata) is secured during a
transfer, see [AWS DataSync encryption in transit](encryption-in-transit.md "encryption-in-transit.md").
