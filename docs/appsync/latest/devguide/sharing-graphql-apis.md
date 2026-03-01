# Sharing AWS AppSync GraphQL APIs

AWS AppSync integrates with AWS Resource Access Manager (AWS RAM) to enable resource sharing. AWS RAM is a service that
enables you to share invoke actions (query, mutation, and subscription operations and connect
requests to your real-time WebSocket endpoint) on AWS AppSync GraphQL APIs with other AWS accounts
or through AWS Organizations. With AWS RAM, you share resources that you own by creating a resource share.
A resource share specifies the resources to share, and the consumers with whom to share them.
Consumers can include the following.

- Specific AWS accounts inside or outside of its organization in AWS Organizations
- An organizational unit inside of its organization in AWS Organizations
- An entire organization in AWS Organizations
  For more information about AWS RAM, see the [AWS Resource Access Manager User Guide](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md").

###### Topics

- [Prerequisites for sharing AWS AppSync GraphQL APIs](#prerequisites-sharing-apis "#prerequisites-sharing-apis")
- [Share AWS AppSync GraphQL APIs](#share_graphal_apis "#share_graphal_apis")
- [Stop sharing AWS AppSync GraphQL APIs](#stop-sharing-apis "#stop-sharing-apis")
- [Cross-account events](#cross-account-events "#cross-account-events")

## Prerequisites for sharing AWS AppSync GraphQL APIs

Sharing AWS AppSync GraphQL APIs has the following prerequisites.

- To share an AWS AppSync GraphQL API, you must own it in your AWS account. This means that
  the AWS AppSync GraphQL API must be allocated or provisioned in your account.
- To share an AWS AppSync GraphQL API with your organization or an organizational unit in
  AWS Organizations, you must enable sharing with AWS Organizations. For more information, see [Enable resource sharing within AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the _AWS Resource Access Manager User
  Guide_.

## Share AWS AppSync GraphQL APIs

To share an AWS AppSync GraphQL API, start by creating a resource share using AWS Resource Access Manager. A
resource share specifies the resources to share, the consumers with whom they are shared, and
what actions principals can perform. When you share an AWS AppSync GraphQL API that you own, with
other AWS accounts, you enable those accounts to call that AWS AppSync API in your AWS account.

If you are part of an organization in AWS Organizations, and sharing within your organization is
enabled, consumers in your organization are automatically granted access to the shared
resource. Otherwise, consumers receive an invitation to join the resource share and are
granted access to the shared resource after accepting the invitation.

**Sharing considerations**

- You can share only AWS AppSync GraphQL APIs, not other API types such as Event APIs.
- You can share only AWS AppSync GraphQL APIs that have `AWS_IAM` as one of the
  authorization modes configured on the API.

If `AWS_IAM` is removed from the list of authorization modes for a shared AppSync
GraphQL API, while the resource share may still exist, it will be rendered ineffective.

- You can share both public and private AWS AppSync GraphQL APIs.
- Private AWS AppSync GraphQL APIs can always be accessed via VPC endpoints in VPCs in the
  origin AWS account, and all authorization modes are supported, not just
  `AWS_IAM`.
- For shared AWS AppSync GraphQL APIs, permissions are managed for the API resource only and
  do not support fine grained permissions for field and type, and field resources. When you
  share an API, you are sharing the API ARN and the ARNs for all of its types and
  fields.

### Create a resource share that you own using the AWS RAM console

To share an AWS AppSync GraphQL API, use the procedure described in [Creating
a resource share](../../../ram/latest/userguide/working-with-sharing-create.md "../../../ram/latest/userguide/working-with-sharing-create.md") in the _AWS Resource Access Manager User Guide_, using the
RAM permission name
`AWSRAMPermissionAppSyncGraphQLApiInvokeAccess`.

### Create and use a customer managed permission to share a private AWS AppSync GraphQL API using the AWS RAM console

To share a private AWS AppSync GraphQL API, create a customer managed permission using the procedure described in [Creating and using customer managed permissions](../../../ram/latest/userguide/create-customer-managed-permissions.md "../../../ram/latest/userguide/create-customer-managed-permissions.md") in the _AWS Resource Access Manager User
Guide_.

As an example, an owner for Account A wants to grant principals in Account B permission to access a private AWS AppSync GraphQL API (PrivateApiA) for calls made via VPCE-B (a VPC Endpoint owned by Account B). In this case, the owner for Account A needs to create an AWS RAM customer managed permission as follows.

```
{
    "Effect": "Allow",
    "Action": ["appsync:GraphQL"],
    "Condition": {
        "StringEqualsIgnoreCase": {
            "aws:SourceVpce": [
                "VPCE-B"
            ]
        }
    }
}
```

Assume that this new customer managed AWS RAM permission is named `private-api-A-access-via-vpce-b`.

To enable cross-account access to `PrivateApiA` via `VPCE-B`, the customer can create an AWS RAM resource share with the following parameters and the customer-managed permission in the previous example.

- **Resource Type:** `appsync:Apis`
- **Resource:** `arn:aws:appsync:us-west-2:A:apis/PrivateApiA`
- **Permission:** `private-api-A-access-via-vpce-b` (Customer-managed permission)
- **Principal:** `Account: B`

### Create a resource share that you own using the AWS CLI

To share an AWS AppSync GraphQL API using the AWS CLI, use the `create-resource-share` command with `arn:aws:ram::aws:permission/AWSRAMPermissionAppSyncApiInvokeAccess` as the value for the `--permission-arns` switch.

For a complete list of available commands for AWS RAM, see the [AWS RAM CLI reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/index.html").

## Stop sharing AWS AppSync GraphQL APIs

To stop sharing AWS AppSync GraphQL APIs that you own, you must either delete the resource share or update the principals that you shared the resource with. Refer to the documentation in the following sections for the action you want to perform.

**To stop sharing a resource that you own using the AWS RAM console**

See [Update a resource share](../../../ram/latest/userguide/working-with-sharing-update.md "../../../ram/latest/userguide/working-with-sharing-update.md") in the _AWS Resource Access Manager User
Guide_.

**To stop sharing a resource that you own using the AWS CLI**

Use the [disassociate-resource-share](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/disassociate-resource-share.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/disassociate-resource-share.html") command.

**To delete a resource share you own using the AWS RAM console**

See [Deleting a resource share](../../../ram/latest/userguide/working-with-sharing-delete.md "../../../ram/latest/userguide/working-with-sharing-delete.md") in the _AWS Resource Access Manager User
Guide_.

**To delete a resource share you own using the AWS CLI**

Use the [delete-resource-share](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/delete-resource-share.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/delete-resource-share.html") command.

For a complete list of available commands for AWS RAM, see the [AWS RAM CLI reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/index.html").

## Cross-account events

You can opt-in to logging AWS CloudTrail Data Events for monitoring and auditing cross-account
AWS AppSync GraphQL API DataPlane activity. For more information, see [Logging data
events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md") in the _AWS CloudTrail User Guide_.
