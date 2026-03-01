# Controlling Network Traffic

To help control network traffic to your WorkSpaces Applications streaming instances, consider these
options:

- When you launch an Amazon AppStream streaming instance, you launch it into a subnet in your VPC. You can deploy streaming
  instances in a private subnet if they should not be accessible from the internet.
- To provide internet access to your streaming instances in a private subnet, use a NAT gateway. For more information, see [Configure a VPC with Private Subnets and a NAT Gateway](managing-network-internet-NAT-gateway.md "managing-network-internet-NAT-gateway.md").
- Security groups that belong to your VPC let you control the network traffic between WorkSpaces Applications streaming instances and VPC resources such as license servers, file servers, and database servers. Security groups also isolate traffic between your streaming instances and WorkSpaces Applications management services.

Use security groups to restrict access to your streaming instances. For example, you can allow traffic only from the address ranges for your corporate network. For more information, see [Security Groups in Amazon WorkSpaces Applications](managing-network-security-groups.md "managing-network-security-groups.md").

- You can stream from WorkSpaces Applications streaming instances in your VPC without going through the public internet. To do so, use an interface VPC endpoint (interface endpoint). For more information, see [Tutorial: Creating and Streaming from Interface VPC Endpoints](creating-streaming-from-interface-vpc-endpoints.md "creating-streaming-from-interface-vpc-endpoints.md").

You can also call WorkSpaces Applications API operations from your VPC without sending traffic over the public internet by using an interface endpoint. For more information, see [Access WorkSpaces Applications API Operations and CLI Commands Through an Interface VPC Endpoint](access-api-cli-through-interface-vpc-endpoint.md "access-api-cli-through-interface-vpc-endpoint.md").

- Use IAM roles and policies to manage administrator access to WorkSpaces Applications, Application Auto Scaling, and Amazon S3
  buckets. For more information, see the following topics:
  - [Using AWS Managed Policies and Linked Roles to Manage Administrator Access to WorkSpaces Applications Resources](controlling-administrator-access-with-policies-roles.md "controlling-administrator-access-with-policies-roles.md")
  - [Using IAM Policies to Manage Administrator Access to Application Auto Scaling](autoscaling-iam-policy.md "autoscaling-iam-policy.md")
  - [Restricting Administrator Access to the Amazon S3 Bucket for Home Folders and Application Settings Persistence](s3-iam-policy-restricted-access.md "s3-iam-policy-restricted-access.md")

- You can use SAML 2.0 to federate authentication to WorkSpaces Applications. For more information, see [Amazon WorkSpaces Applications Service Quotas](limits.md "limits.md").

###### Note

For smaller WorkSpaces Applications deployments, you can use WorkSpaces Applications user pools. By default, user pools support a maximum of 50 users. For more information about WorkSpaces Applications quotas (also referred to as limits), see [Amazon WorkSpaces Applications Service Quotas](limits.md "limits.md"). For deployments that must support 100 or more WorkSpaces Applications users, we recommend using SAML 2.0.
