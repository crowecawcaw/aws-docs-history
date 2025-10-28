# Access AWS FIS using an interface VPC endpoint (AWS PrivateLink)

You can establish a private connection between your VPC and AWS Fault Injection Service by creating an
_interface VPC endpoint_. VPC endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology that enables you
to privately access AWS FIS APIs without an internet gateway, NAT device, VPN connection, or
AWS Direct Connect connection. Instances in your VPC don't need public IP addresses to
communicate with AWS FIS APIs.

Each interface endpoint is represented by one or more [elastic network interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in
your subnets.

For more information, see [Access AWS services through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the
_AWS PrivateLink Guide_.

## Considerations for AWS FIS VPC endpoints

Before you set up an interface VPC endpoint for AWS FIS, review [Access an AWS service using
an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the _AWS PrivateLink Guide_.

AWS FIS supports making calls to all of its API actions from your VPC.

## Create an interface VPC endpoint for AWS FIS

You can create a VPC endpoint for the AWS FIS service using either the Amazon VPC console or
the AWS Command Line Interface (AWS CLI). For more information, see [Create a
VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the _AWS PrivateLink Guide_.

Create a VPC endpoint for AWS FIS using the following service name: `com.amazonaws.`region`.fis`.

If you enable private DNS for the endpoint, you can make API requests to AWS FIS using
its default DNS name for the Region, for example,
`fis.us-east-1.amazonaws.com`.

## Create a VPC endpoint policy for AWS FIS

You can attach an endpoint policy to your VPC endpoint that controls access to AWS FIS.
The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Control access to VPC endpoints using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _AWS PrivateLink Guide_.

###### Example: VPC endpoint policy for specific AWS FIS actions

The following VPC endpoint policy grants access to the listed AWS FIS actions
on all resources to all principals.

```
{
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "fis:ListExperimentTemplates",
            "fis:StartExperiment",
            "fis:StopExperiment",
            "fis:GetExperiment"
         ],
         "Resource":"*",
         "Principal":"*"
      }
   ]
}
```

###### Example: VPC endpoint policy that denies access from a specific AWS account

The following VPC endpoint policy denies the specified AWS account access to
all actions and resources, but grants all other AWS accounts access to all actions
and resources.

```
{
   "Statement":[
      {
         "Effect": "Allow",
         "Action": "*",
         "Resource": "*",
         "Principal": "*"
      },
      {
         "Effect":"Deny",
         "Action": "*",
         "Resource": "*",
         "Principal": {
           "AWS": [ "123456789012" ]
         }
      }
   ]
}
```
