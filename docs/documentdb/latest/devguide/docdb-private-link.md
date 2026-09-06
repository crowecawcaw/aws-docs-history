

# Amazon DocumentDB API and interface VPC endpoints (AWS PrivateLink)
<a name="docdb-private-link"></a>

**Note**  
Amazon DocumentDB elastic clusters do not support AWS PrivateLink VPC endpoints.

You can establish a private connection between your VPC and Amazon DocumentDB API endpoints by creating an interface VPC endpoint. Interface endpoints are powered by AWS PrivateLink.

While Amazon DocumentDB instance-based clusters do not require an interface VPC endpoint connection, AWS PrivateLink enables you to privately access Amazon DocumentDB API operations without an internet gateway, NAT device, VPN connection, or Direct Connect connection. Amazon DocumentDB instances in your VPC don't need public IP addresses to communicate with Amazon DocumentDB API endpoints to launch, modify, or terminate database instances and database clusters. Your Amazon DocumentDB instances also don't need public IP addresses to use any of the available Amazon DocumentDB API operations. Traffic between your VPC and Amazon DocumentDB doesn't leave the Amazon network.

Each interface endpoint is represented by one or more elastic network interfaces in your subnets. For more information, see [Elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in the *Amazon EC2 User Guide.*

For more information about VPC endpoints, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *Amazon Virtual Private Cloud (AWS PrivateLink) User Guide*. For more information about Amazon DocumentDB operations, see the [Amazon DocumentDB API Reference](https://docs.aws.amazon.com/documentdb/latest/APIReference/).

**Topics**
+ [Considerations for VPC endpoints](#endpoint-considerations)
+ [Region availability](#region-availability)
+ [Creating an interface VPC endpoint for Amazon DocumentDB API](#create-interface-endpoint)
+ [Creating a VPC endpoint policy for Amazon DocumentDB API](#create-endpoint-policy)

## Considerations for VPC endpoints
<a name="endpoint-considerations"></a>

Before you set up an interface VPC endpoint for Amazon DocumentDB API endpoints, ensure that you review the [interface endpoint prerequisites](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#prerequisites-interface-endpoints) in the *Amazon Virtual Private Cloud (AWS PrivateLink) User Guide*.

All Amazon DocumentDB API operations relevant to managing Amazon DocumentDB resources are available from your VPC using AWS PrivateLink.

VPC endpoint policies are supported for Amazon DocumentDB API endpoints. By default, full access to Amazon DocumentDB API operations is allowed through the endpoint. For more information, see [Control access to VPC endpoints using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *Amazon Virtual Private Cloud (AWS PrivateLink) User Guide*.

## Region availability
<a name="region-availability"></a>

Amazon DocumentDB API currently supports VPC endpoints in the following AWS Regions:
+ US East (Ohio)
+ US East (N. Virginia)
+ US West (Oregon)
+ Africa (Cape Town)
+ Asia Pacific (Hong Kong)
+ Asia Pacific (Mumbai)
+ Asia Pacific (Hyderabad)
+ Asia Pacific (Osaka)
+ Asia Pacific (Seoul)
+ Asia Pacific (Singapore)
+ Asia Pacific (Sydney)
+ Asia Pacific (Tokyo)
+ Canada (Central)
+ China (Beijing)
+ China (Ningxia)
+ Europe (Frankfurt)
+ Europe (Ireland)
+ Europe (London)
+ Europe (Paris)
+ Europe (Spain)
+ Europe (Milan)
+ Middle East (UAE)
+ South America (São Paulo)
+ AWS GovCloud (US-East)
+ AWS GovCloud (US-West)

## Creating an interface VPC endpoint for Amazon DocumentDB API
<a name="create-interface-endpoint"></a>

You can create a VPC endpoint for the Amazon DocumentDB API using either the Amazon VPC Console or the AWS Command Line Interface (AWS CLI). For more information, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *Amazon Virtual Private Cloud (AWS PrivateLink) User Guide*.

Create a VPC endpoint for the Amazon DocumentDB API using the service name `com.amazonaws.region.rds`.

Excluding AWS Regions in China, if you enable private DNS for the endpoint, you can make API requests to Amazon DocumentDB with the VPC endpoint using its default DNS name for the AWS Regions, for example rds.us-east-1.amazonaws.com. For the China (Beijing) and China (Ningxia) AWS Regions, you can make API requests with the VPC endpoint using rds-api.cn-north-1.amazonaws.com.cn and rds-api.cn-northwest-1.amazonaws.com.cn, respectively.

For more information, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *Amazon Virtual Private Cloud (AWS PrivateLink) User Guide*.

## Creating a VPC endpoint policy for Amazon DocumentDB API
<a name="create-endpoint-policy"></a>

You can attach an endpoint policy to your VPC endpoint that controls access to the Amazon DocumentDB API. The policy specifies the following information:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

For more information, see [Control access to VPC endpoints using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *Amazon Virtual Private Cloud (AWS PrivateLink) User Guide*.

**Example: VPC endpoint policy for Amazon DocumentDB API actions**

The following is an example of an endpoint policy for Amazon DocumentDB API. When attached to an endpoint, this policy grants access to the listed Amazon DocumentDB API actions for all principals on all resources.

```
{
"Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "docdb:CreateDBInstance",
            "docdb:ModifyDBInstance",
            "docdb:CreateDBSnapshot"
         ],
         "Resource":"*"
      }
   ]
}
```

**Example: VPC endpoint policy that denies all access from a specified AWS account**

The following VPC endpoint policy denies AWS account 123456789012 all access to resources using the endpoint. The policy allows all actions from other accounts.

```
{
  "Statement": [
    {
      "Action": "*",
      "Effect": "Allow",
      "Resource": "*",
      "Principal": "*"
    },
    {
      "Action": "*",
      "Effect": "Deny",
      "Resource": "*",
      "Principal": { "AWS": [ "123456789012" ] }
     }
   ]
}
```