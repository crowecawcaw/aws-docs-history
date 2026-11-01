

# Working with endpoints
<a name="working-with-endpoints"></a>

When you manage media workflows, the details of your content sources and destinations can scatter across spreadsheets, consoles, and separate tools. AWS Elemental MediaConnect provides an endpoint registry that brings together the endpoints that represent your sources and destinations, giving you a centralized place to manage them. You can see which endpoints are available and connect them as you build and adjust your workflows.

## Key points
<a name="endpoints-key-points"></a>

### Endpoint concepts and terminology
<a name="endpoints-concepts-terminology"></a>

Before working with endpoints, familiarize yourself with these key concepts and terms.

**Endpoints and the registry**  
+ **Source endpoint**

  Represents the sending side of a connection.
+ **Destination endpoint**

  Represents the receiving side of a connection.
+ **Endpoint registry**

  The place in MediaConnect that holds all endpoints available to you. Each endpoint is a reusable reference to the side of a connection it represents.

**Endpoint types**  
+ **Standard endpoint**

  An endpoint you register to represent a device or software outside the service, such as a camera, encoder, decoder, or monitor. A standard endpoint defines the configuration that MediaConnect uses to reach that device or software, such as protocol, address, port, and network settings.
+ **Managed endpoint**

  An endpoint that represents a resource that MediaConnect manages, such as a router input or output.

**Connections**  
+ **Connection**

  A link you create between a source endpoint and a destination endpoint.
+ **Connection state**

  The current status of the connection between two endpoints, such as connected or disconnected.

**Cross-account sharing**  
+ **Resource share**

  An AWS Resource Access Manager (AWS RAM) resource that you use to share endpoints with AWS accounts, organizations, or organizational units.
+ **Sharing account**

  The AWS account that owns an endpoint and shares it. The sharing account keeps control of the endpoint.
+ **Consuming account**

  An AWS account that accepts a resource share. After the consuming account accepts the resource share, the shared endpoints are available in its endpoint registry.

## How endpoints work
<a name="how-endpoints-work"></a>

### Endpoint setup
<a name="how-endpoints-work-setup"></a>

Building on these concepts, the following steps show how you set up and connect endpoints at a high level:

1. **Register endpoints** - Register a source endpoint for each sender of your content and a destination endpoint for each receiver. For resources that support endpoints, MediaConnect may register managed endpoints for you automatically.

1. **Connect endpoints** - Connect a source endpoint to a destination endpoint. Content then flows between the devices or resources that the endpoints represent.

You can do these steps in the MediaConnect console, or programmatically using the MediaConnect API.

### Endpoint sharing
<a name="how-endpoints-work-sharing"></a>

The following steps show how you share endpoints with other AWS accounts by using AWS Resource Access Manager (AWS RAM):

1. **Create a resource share** - In the sharing account, add the endpoints that you want to share to a resource share, and choose the accounts, organizations, or organizational units to share them with.

1. **Accept the resource share** - In the consuming account, accept the resource share. The shared endpoints then appear in the consuming account's endpoint registry.

1. **Connect the shared endpoints** - In the consuming account, connect a shared endpoint the same way that you connect any other endpoint.

To stop sharing an endpoint, the sharing account removes it from the resource share. To stop sharing every endpoint in a resource share, the sharing account deletes the resource share.

## Endpoint capabilities and management
<a name="endpoints-capabilities"></a>

After you set up endpoints, you manage them as your workflows change. You can:
+ View, update, and deregister the endpoints that you register.
+ Connect and disconnect endpoints.
+ Track the connection state of your endpoints, and view the network topology of an endpoint's connections.
+ Share endpoints with other accounts.

## Endpoint considerations and limitations
<a name="endpoints-considerations"></a>

As you plan how you will use endpoints, keep these points in mind.


| Consideration | Description | 
| --- | --- | 
| Connection topology | Each connection joins one source endpoint to one destination endpoint. | 
| Supported protocols | Standard endpoints support SRT caller, SRT listener, RTP, and RIST. | 
| Endpoint encryption secret | An endpoint encryption secret must use a customer managed, enabled, symmetric AWS KMS key in the same account and Region. You cannot use the AWS managed key `aws/secretsmanager`. | 
| Networking | A public endpoint supports up to 10 CIDR allow rules. A VPC endpoint uses between 1 and 5 security groups and exactly one subnet in one Availability Zone. | 
| Metrics | Only managed endpoints that represent router inputs and outputs publish Amazon CloudWatch metrics. Standard endpoints do not publish metrics. | 

## Next steps
<a name="endpoints-next-steps"></a>

You can learn how to set up and use endpoints in the following pages of this guide:
+ [Managing endpoints in MediaConnect](managing-endpoints.md)
  + [Registering an endpoint in MediaConnect](registering-endpoint.md)
  + [Viewing endpoints in MediaConnect](viewing-endpoints.md)
  + [Updating an endpoint in MediaConnect](updating-endpoint.md)
  + [Deregistering an endpoint in MediaConnect](deregistering-endpoint.md)
  + [MediaConnect endpoint states](endpoint-states.md)
+ [Connecting and disconnecting endpoints in MediaConnect](connecting-endpoints.md)
  + [Using the Connection manager in MediaConnect](using-connection-manager.md)
+ [Encrypting endpoints in MediaConnect](encrypting-endpoints.md)
+ [Sharing endpoints across accounts in MediaConnect](sharing-endpoints.md)
  + [Creating a resource share in MediaConnect](creating-endpoint-resource-share.md)
  + [Accepting a resource share in MediaConnect](accepting-endpoint-resource-share.md)
  + [Viewing shared endpoints in MediaConnect](viewing-shared-endpoints.md)
  + [Stopping endpoint sharing in MediaConnect](stopping-endpoint-sharing.md)