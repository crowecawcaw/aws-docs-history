AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# AWS HealthOmics and interface VPC endpoints

(AWS PrivateLink)

You can establish a private connection between your VPC and AWS HealthOmics by creating an _interface VPC
endpoint_. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology that you can use to privately access HealthOmics API operations without an
internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC don't require
public IP addresses to communicate with HealthOmics API operations. Traffic between your VPC and HealthOmics doesn't go
outside the Amazon network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets.

For more information, see [Interface VPC
endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User
Guide_.

VPC endpoint policies are supported for HealthOmics for all Regions except Israel (Tel Aviv). By default, full
access to HealthOmics is allowed through the endpoint.

## Considerations for HealthOmics VPC

endpoints

Before you set up an interface VPC endpoint for HealthOmics, make sure that you review [Interface
endpoint properties and limitations](../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations") in the _Amazon VPC User Guide_.

HealthOmics supports making calls to all HealthOmics Storage API actions from your VPC.

VPC endpoint policies aren't supported for HealthOmics by default, but you can create a VPC endpoint for
full HealthOmics access for the HealthOmics Storage operations. For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the
_Amazon VPC User Guide_.

## Creating an interface VPC endpoint for

HealthOmics

You can create a VPC endpoint for the HealthOmics service by using the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For
more information, see [Creating an
interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

Create a VPC endpoint for HealthOmics by using the following service names:

- com.amazonaws.`region`.storage-omics
- com.amazonaws.`region`.control-storage-omics
- com.amazonaws.`region`.analytics-omics
- com.amazonaws.`region`.workflows-omics
- com.amazonaws.`region`.tags-omics

The US East (N. Virginia) and US West (Oregon) regions support AWS PrivateLink FIPS endpoints. For these
regions, you can also use the following service names:

- com.amazonaws.`region`.storage-omics-fips
- com.amazonaws.`region`.control-storage-omics-fips
- com.amazonaws.`region`.analytics-omics-fips
- com.amazonaws.`region`.workflows-omics-fips
- com.amazonaws.`region`.tags-omics-fips

If you turn on private DNS for the endpoint, you can make API requests to HealthOmics by using its default DNS
name for the Region, for example, `omics.us-east-1.amazonaws.com`.

For more information, see [Accessing a service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the
_Amazon VPC User Guide_.

## Creating a VPC endpoint policy for

HealthOmics

You can attach an endpoint policy to your VPC endpoint that controls access to
HealthOmics. The policy specifies the following information:

- The principal that can perform actions
- The actions that can be performed
- The resources on which actions can be performed

For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

###### Example: VPC endpoint policy for HealthOmics actions.

The following is an example of an endpoint policy for HealthOmics. When attached to
an endpoint, this policy grants access to HealthOmics actions for all principals on
all resources.

API

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

AWS CLI

```
aws ec2 modify-vpc-endpoint \
    --vpc-endpoint-id `vpce-id` \
    --region us-west-2 \
    --policy-document \
    "{\"Statement\":[{\"Principal\":\"*\",\"Effect\":\"Allow\",\"Action\":[\"omics:List*\"],\"Resource\":\"*\"}]}"
```

## Special considerations for accessing read sets using Amazon S3 URIs

To access read sets through Amazon S3 URIs when you're using a private connection, set up the PrivateLink
interface endpoints on the sequence store. After you set them up, the endpoints have the following
formats:

```
   com.amazonaws.`region`.storage-omics
   com.amazonaws.`region`.control-storage-omics
```

To use Gateway endpoints, follow the guide [Gateway endpoints for
Amazon S3](../../../vpc/latest/privatelink/vpc-endpoints-s3.md "../../../vpc/latest/privatelink/vpc-endpoints-s3.md") to configure your gateway endpoints. HealthOmics owns the Amazon S3 bucket, so you don't have to create or
adjust the bucket policy. Gateway endpoints rely on the policy attached to the user or role that accesses the
data, but you can also configure endpoints with more restrictive policies. These policies can include restrictions
on access based on the Amazon S3 Access Point ARN and Amazon S3 actions.
