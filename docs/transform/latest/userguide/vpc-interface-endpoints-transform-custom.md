

# AWS Transform custom and interface endpoints (AWS PrivateLink)
<a name="vpc-interface-endpoints-transform-custom"></a>

You can establish a private connection between your VPC and AWS Transform custom by creating an *interface VPC endpoint*. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink), a technology that enables you to privately access AWS Transform custom services without an internet gateway, NAT device, VPN connection, or Direct Connect connection. Traffic between your VPC and AWS Transform custom does not leave the Amazon network. 

Each interface endpoint is represented by one or more [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in your subnets. 

For more information, see [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html) in the *Amazon VPC User Guide*. 

**Note**  
You must enable AWS PrivateLink integration for Amazon S3 since AWS Transform custom makes S3 API calls. For detailed instructions, see the [AWS PrivateLink for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html) documentation. If you encounter S3 access issues while using AWS Transform custom, refer to our [troubleshooting guide](custom-troubleshooting.md#custom-s3-access-issues).
If you are not using AWS PrivateLink Private DNS feature (see [Private DNS](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html#interface-endpoint-private-dns)), you must:  
Configure routing to VPC interface endpoints (see the [Routing to VPC interface endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-vpc-interface-endpoint.html) documentation)
Set the `ATX_CUSTOM_ENDPOINT` environment variable to specify your custom domain, for example:  

    ```
    ATX_CUSTOM_ENDPOINT=https://transform-custom.<region>.api.aws atx
    ```

## Considerations for AWS Transform custom VPC endpoints
<a name="vpc-interface-endpoints-transform-custom-considerations"></a>

Before you set up an interface VPC endpoint for AWS Transform custom, ensure that you review [Interface endpoint properties and limitations](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#vpce-interface-limitations) in the *Amazon VPC User Guide*. 

AWS Transform custom supports making calls to all of its API actions through the interface endpoint.

## Prerequisites
<a name="vpc-interface-endpoints-transform-custom-prereq"></a>

Before you begin any of the procedures below, ensure that you have the following:
+ An AWS account with appropriate permissions to create and configure resources.
+ A VPC already created in your AWS account.
+ Familiarity with AWS services, especially Amazon VPC and AWS Transform custom.

## Creating an interface VPC endpoint for AWS Transform custom
<a name="vpc-interface-endpoints-transform-custom-create"></a>

You can create a VPC endpoint for the AWS Transform custom service using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint) in the *Amazon VPC User Guide*.

Create the following VPC endpoints for AWS Transform custom using this service name: 
+ com.amazonaws.{{region}}.transform-custom

Replace {{region}} with AWS Region where you desire to use AWS Transform custom CLI, for example, *com.amazonaws.us-east-1.transform-custom*.

For more information, see [Accessing a service through an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#access-service-though-endpoint) in the *Amazon VPC User Guide*.

## Creating a VPC endpoint policy for AWS Transform custom
<a name="vpc-interface-endpoints-transform-custom-policy"></a>

You can attach an endpoint policy to your VPC endpoint that controls access to AWS Transform custom. The policy specifies the following information:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*. 

**Example: VPC endpoint policy for AWS Transform custom actions**  
The following is an example of an endpoint policy for AWS Transform custom. When attached to an endpoint, this policy grants access to the listed AWS Transform custom actions for all principals on all resources.

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "transform-custom:*"
         ],
         "Resource":"*"
      }
   ]
}
```

## Using an on-premises computer to connect to a AWS Transform custom endpoint
<a name="vpc-interface-endpoints-transform-custom-on-prem"></a>

This section describes the process of using an on-premises computer to connect to AWS Transform custom through a AWS PrivateLink endpoint in your AWS VPC.

1. [Create a VPN connection between your on-premises device and your VPC.](https://docs.aws.amazon.com/vpn/latest/clientvpn-user/client-vpn-user-what-is.html)

1. [Create an interface VPC endpoint for AWS Transform custom.](#vpc-interface-endpoints-transform-custom-create)

1. [Set up an inbound Amazon Route 53 endpoint.](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-vpc-interface-endpoint.html) This will enable you to use the DNS name of your AWS Transform custom endpoint from your on-premises device.