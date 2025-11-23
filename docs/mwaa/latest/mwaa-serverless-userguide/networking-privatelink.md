# Access Amazon MWAA Serverless using an interface endpoint (AWS PrivateLink)

You can use AWS PrivateLink to create a private connection between your VPC and Amazon MWAA Serverless. You can access Amazon MWAA Serverless as if it were in your VPC, without the
use of an internet gateway, NAT device, VPN connection, or Direct Connect connection. Instances in your VPC don't need public IP addresses to access Amazon MWAA Serverless.

You establish this private connection by creating an _interface endpoint_, powered by AWS PrivateLink. We create an endpoint network interface in each subnet that you enable for the interface endpoint. These are requester-managed network interfaces that serve as the entry point for traffic destined for Amazon MWAA Serverless.

For more information, refer to [Access AWS services through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the _AWS PrivateLink Guide_.

## Considerations for Amazon MWAA Serverless

Before you set up an interface endpoint for Amazon MWAA Serverless, review [Considerations](../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints") in the _AWS PrivateLink Guide_.

Amazon MWAA Serverless supports making calls to all of its API actions through the interface endpoint.

VPC endpoint policies are supported for Amazon MWAA Serverless. By default, full access to Amazon MWAA Serverless is allowed through the interface endpoint. Alternatively, you can associate a security group with the endpoint network interfaces to control traffic to Amazon MWAA Serverless through the interface endpoint.

## Create an interface endpoint for Amazon MWAA Serverless

You can create an interface endpoint for Amazon MWAA Serverless using either the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, refer to [Create an interface endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the _AWS PrivateLink Guide_.

Create an interface endpoint for Amazon MWAA Serverless using the following service name:

```
com.amazonaws.`region`.airflow-serverless
```

If you enable private DNS for the interface endpoint, you can make API requests to Amazon MWAA Serverless using its default Regional DNS name. For example, `airflow-serverless.us-east-1.api.com`.

## Create an endpoint policy for your interface endpoint

An endpoint policy is an IAM resource that you can attach to an interface endpoint. The default endpoint policy allows full access to Amazon MWAA Serverless through the interface endpoint. To control the access allowed to Amazon MWAA Serverless from your VPC, attach a custom endpoint policy to the interface endpoint.

An endpoint policy specifies the following information:

- The principals that can perform actions (AWS accounts, IAM users, and IAM roles).
- The actions that can be performed.
- The resources on which the actions can be performed.

For more information, refer to [Control access to services using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _AWS PrivateLink Guide_.

###### Example: VPC endpoint policy for Amazon MWAA Serverless actions

The following is an example of a custom endpoint policy. When you attach this policy to your interface endpoint, it grants access to the listed Amazon MWAA Serverless actions for all principals on all resources.

```
{
  "Statement": [
    {
      "Principal": "*",
      "Effect": "Allow",
      "Action": [
        "`airflow-serverless`:`GetWorkflow`",
        "`airflow-serverless`:`ListWorkflows`"
      ],
      "Resource":"*"
    }
  ]
}
```
