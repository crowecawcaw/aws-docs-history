# Configuring interface VPC endpoints (AWS PrivateLink) for AWS Glue

(AWS PrivateLink)

You can establish a private connection between your VPC and AWS Glue by creating an
_interface VPC endpoint_. Interface endpoints are powered by [AWS PrivateLink](https://aws.amazon.com/privatelink "https://aws.amazon.com/privatelink"), a technology that enables you
to privately access AWS Glue APIs without an internet gateway, NAT device, VPN
connection, or AWS Direct Connect connection. Instances in your VPC don't need public IP
addresses to communicate with AWS Glue APIs. Traffic between your VPC and AWS Glue
does not leave the Amazon network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your
subnets.

For more information, see [Interface VPC
endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User
Guide_.

## Considerations for

AWS Glue VPC endpoints

Before you set up an interface VPC endpoint for AWS Glue, ensure that
you review [Interface endpoint properties and limitations](../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations") in the _Amazon VPC User Guide_.

AWS Glue supports making calls to all of its API actions from your
VPC.

## Creating an interface VPC endpoint for

AWS Glue

You can create a VPC endpoint for the AWS Glue service using either
the Amazon VPC console or the AWS Command Line Interface (AWS CLI). For more information, see [Creating an
interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

Create a VPC endpoint for AWS Glue using the following service name:

- com.amazonaws.`region`.glue

If you enable private DNS for the endpoint, you can make API requests to
AWS Glue using its default DNS name for the Region,
for example, `glue.us-east-1.amazonaws.com`.

For more information, see [Accessing a service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the
_Amazon VPC User Guide_.

## Creating a VPC endpoint policy for

AWS Glue

You can attach an endpoint policy to your VPC endpoint that controls access to
AWS Glue. The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

###### Example: VPC endpoint policy for AWS Glue to allow job creation

and update

The following is an example of an endpoint policy for AWS Glue.
When attached to an endpoint, this policy grants access to the listed
AWS Glue actions for all principals on all resources.

```
{
  "Statement": [
    {
      "Sid": "RestrictPassRole",
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "arn:aws:iam::123456789012:role/GlueServiceRole*",
      "Condition": {
        "StringEquals": {
          "iam:PassedToService": "glue.amazonaws.com"
        }
      }
    }
  ]
}
```

###### Example: VPC endpoint policy to allow read-only Data Catalog access

The following is an example of an endpoint policy for AWS Glue.
When attached to an endpoint, this policy grants access to the listed
AWS Glue actions for all principals on all resources.

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "glue:GetDatabase",
        "glue:GetDatabases",
        "glue:GetTable",
        "glue:GetTables",
        "glue:GetTableVersion",
        "glue:GetTableVersions",
        "glue:GetPartition",
        "glue:GetPartitions",
        "glue:BatchGetPartition",
        "glue:SearchTables"
      ],
      "Resource": "*"
    }
  ]
}
```
