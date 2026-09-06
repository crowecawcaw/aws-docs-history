

# AWS HealthOmics and interface VPC endpoints (AWS PrivateLink)
<a name="vpc-interface-endpoints"></a>

You can establish a private connection between your VPC and AWS HealthOmics by creating an *interface VPC endpoint*. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink), a technology that you can use to privately access HealthOmics API operations without an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC don't require public IP addresses to communicate with HealthOmics API operations. Traffic between your VPC and HealthOmics doesn't go outside the Amazon network. 

Each interface endpoint is represented by one or more [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in your subnets. 

For more information, see [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html) in the *Amazon VPC User Guide*. 

VPC endpoint policies are supported for HealthOmics for all Regions except Israel (Tel Aviv). By default, full access to HealthOmics is allowed through the endpoint.

## Considerations for HealthOmics VPC endpoints
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface VPC endpoint for HealthOmics, make sure that you review [Interface endpoint properties and limitations](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#vpce-interface-limitations) in the *Amazon VPC User Guide*. 

HealthOmics supports making calls to all HealthOmics Storage API actions from your VPC. 

VPC endpoint policies aren't supported for HealthOmics by default, but you can create a VPC endpoint for full HealthOmics access for the HealthOmics Storage operations. For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*.

## Creating an interface VPC endpoint for HealthOmics
<a name="vpc-endpoint-create"></a>

You can create a VPC endpoint for the HealthOmics service by using the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint) in the *Amazon VPC User Guide*.

Create a VPC endpoint for HealthOmics by using the following service names: 
+ com.amazonaws.{{region}}.storage-omics
+ com.amazonaws.{{region}}.control-storage-omics
+ com.amazonaws.{{region}}.analytics-omics
+ com.amazonaws.{{region}}.workflows-omics
+ com.amazonaws.{{region}}.tags-omics

The US East (N. Virginia), US West (Oregon), and US East (Ohio) regions support AWS PrivateLink FIPS endpoints. For these regions, you can also use the following service names: 
+ com.amazonaws.{{region}}.storage-omics-fips
+ com.amazonaws.{{region}}.control-storage-omics-fips
+ com.amazonaws.{{region}}.analytics-omics-fips
+ com.amazonaws.{{region}}.workflows-omics-fips
+ com.amazonaws.{{region}}.tags-omics-fips

If you turn on private DNS for the endpoint, you can make API requests to HealthOmics by using its default DNS name for the Region, for example, `omics.us-east-1.amazonaws.com`. 

For more information, see [Accessing a service through an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#access-service-though-endpoint) in the *Amazon VPC User Guide*.

## Creating a VPC endpoint policy for HealthOmics
<a name="vpc-endpoint-policy"></a>

You can attach an endpoint policy to your VPC endpoint that controls access to HealthOmics. The policy specifies the following information:
+ The principal that can perform actions
+ The actions that can be performed
+ The resources on which actions can be performed

For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*. 

**Example: VPC endpoint policy for HealthOmics actions.**  
The following is an example of an endpoint policy for HealthOmics. When attached to an endpoint, this policy grants access to HealthOmics actions for all principals on all resources.

------
#### [ API ]

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "omics:List*"
         ],
         "Resource":"*"
      }
   ]
}
```

------
#### [ AWS CLI ]

```
aws ec2 modify-vpc-endpoint \
    --vpc-endpoint-id {{vpce-id}} \
    --region us-west-2 \
    --policy-document \
    "{\"Statement\":[{\"Principal\":\"*\",\"Effect\":\"Allow\",\"Action\":[\"omics:List*\"],\"Resource\":\"*\"}]}"
```

------

## Special considerations for accessing read sets using Amazon S3 URIs
<a name="vpc-access-s3-uris"></a>

To access read sets through Amazon S3 URIs when you're using a private connection, set up the PrivateLink interface endpoints on the sequence store. After you set them up, the endpoints have the following formats:

```
   com.amazonaws.{{region}}.storage-omics 
   com.amazonaws.{{region}}.control-storage-omics
```

To use Gateway endpoints, follow the guide [Gateway endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html) to configure your gateway endpoints. HealthOmics owns the Amazon S3 bucket, so you don't have to create or adjust the bucket policy. Gateway endpoints rely on the policy attached to the user or role that accesses the data, but you can also configure endpoints with more restrictive policies. These policies can include restrictions on access based on the Amazon S3 Access Point ARN and Amazon S3 actions.