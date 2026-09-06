

# Access AWS Serverless Application Repository using an interface endpoint (AWS PrivateLink)
<a name="vpc-interface-endpoints"></a>

You can use AWS PrivateLink to create a private connection between your VPC and AWS Serverless Application Repository. You can access AWS Serverless Application Repository as if it were in your VPC, without the use of an internet gateway, NAT device, VPN connection, or Direct Connect connection. Instances in your VPC don't need public IP addresses to access AWS Serverless Application Repository.

You establish this private connection by creating an *interface endpoint*, powered by AWS PrivateLink. We create an endpoint network interface in each subnet that you enable for the interface endpoint. These are requester-managed network interfaces that serve as the entry point for traffic destined for AWS Serverless Application Repository.

For more information, see [Access AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html) in the *AWS PrivateLink Guide*.

## Considerations for AWS Serverless Application Repository
<a name="vpc-endpoint-considerations"></a>

Before you set up an interface endpoint for AWS Serverless Application Repository, review [Considerations](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#considerations-interface-endpoints) in the *AWS PrivateLink Guide*.

AWS Serverless Application Repository supports making calls to all of its API actions through the interface endpoint.

## Create an interface endpoint for AWS Serverless Application Repository
<a name="vpc-endpoint-create"></a>

You can create an interface endpoint for AWS Serverless Application Repository using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws) in the *AWS PrivateLink Guide*.

Create an interface endpoint for AWS Serverless Application Repository using the following service name:

```
com.amazonaws.{{region}}.serverlessrepo
```

If you enable private DNS for the interface endpoint, you can make API requests to AWS Serverless Application Repository using its default Regional DNS name. For example, `serverlessrepo.us-east-1.amazonaws.com`.

## Create an endpoint policy for your interface endpoint
<a name="vpc-endpoint-policy"></a>

An endpoint policy is an IAM resource that you can attach to an interface endpoint. The default endpoint policy allows full access to AWS Serverless Application Repository through the interface endpoint. To control the access allowed to AWS Serverless Application Repository from your VPC, attach a custom endpoint policy to the interface endpoint.

An endpoint policy specifies the following information:
+ The principals that can perform actions (AWS accounts, IAM users, and IAM roles).
+ The actions that can be performed.
+ The resources on which the actions can be performed.

For more information, see [Control access to services using endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *AWS PrivateLink Guide*.

**Example: VPC endpoint policy for AWS Serverless Application Repository actions**  
The following is an example of a custom endpoint policy. When you attach this policy to your interface endpoint, it grants access to the listed AWS Serverless Application Repository action for all principals on all resources. The following example allows all users the permission to create applications through the VPC endpoint.

```
{
   "Statement": [
      {
         "Principal": "*",
         "Effect": "Allow",
         "Action": [
            "{{serverlessrepo}}:{{CreateApplication}}"
         ],
         "Resource":"*"
      }
   ]
}
```