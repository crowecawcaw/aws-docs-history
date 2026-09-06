

# AWS HealthImaging and interface VPC endpoints (AWS PrivateLink)
<a name="vpc-interface-endpoints"></a>

You can establish a private connection between your VPC and AWS HealthImaging by creating an *interface VPC endpoint*. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink), a technology that you can use to privately access HealthImaging APIs without an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. Instances in your VPC don't need public IP addresses to communicate with HealthImaging APIs. Traffic between your VPC and HealthImaging does not leave the Amazon network. 

Each interface endpoint is represented by one or more [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in your subnets. 

For more information, see [Interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html) in the *Amazon VPC User Guide*. 

**Topics**
+ [Considerations for HealthImaging VPC endpoints](#vpc-endpoint-considerations)
+ [Creating an interface VPC endpoint for HealthImaging](#vpc-endpoint-create)
+ [Creating a VPC endpoint policy for HealthImaging](#vpc-endpoint-policy)

## Considerations for HealthImaging VPC endpoints
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface VPC endpoint for HealthImaging, make sure that you review [Interface endpoint properties and limitations](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#vpce-interface-limitations) in the *Amazon VPC User Guide*. 

HealthImaging supports making calls to all AWS HealthImaging actions from your VPC. 

## Creating an interface VPC endpoint for HealthImaging
<a name="vpc-endpoint-create"></a>

You can create a VPC endpoint for the HealthImaging service using the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#create-interface-endpoint) in the *Amazon VPC User Guide*.

Create VPC endpoints for HealthImaging using the following service names: 
+ com.amazonaws.{{region}}.medical-imaging
+ com.amazonaws.{{region}}.runtime-medical-imaging
+ com.amazonaws.{{region}}.dicom-medical-imaging

**Note**  
Private DNS must be enabled to use PrivateLink.

You can make API requests to HealthImaging using its default DNS name for the Region, for example, `medical-imaging.us-east-1.amazonaws.com`.

For more information, see [Accessing a service through an interface endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html#access-service-though-endpoint) in the *Amazon VPC User Guide*.

## Creating a VPC endpoint policy for HealthImaging
<a name="vpc-endpoint-policy"></a>

You can attach an endpoint policy to your VPC endpoint that controls access to HealthImaging. The policy specifies the following information:
+ The principal that can perform actions
+ The actions that can be performed
+ The resources on which actions can be performed

For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *Amazon VPC User Guide*. 

**Example: VPC endpoint policy for HealthImaging actions**  
The following is an example of an endpoint policy for HealthImaging. When attached to an endpoint, this policy grants access to HealthImaging actions for all principals on all resources.

------
#### [ API ]

```
{
   "Statement":[
      {
         "Principal":"*",
         "Effect":"Allow",
         "Action":[
            "medical-imaging:*"
         ],
         "Resource":"*"
      }
   ]
}
```

------
#### [ CLI ]

```
aws ec2 modify-vpc-endpoint \
    --vpc-endpoint-id {{vpce-id}}   
    --region us-west-2 \
    --private-dns-enabled \
    --policy-document \
    "{\"Statement\":[{\"Principal\":\"*\",\"Effect\":\"Allow\",\"Action\":[\"medical-imaging:*\"],\"Resource\":\"*\"}]}"
```

------