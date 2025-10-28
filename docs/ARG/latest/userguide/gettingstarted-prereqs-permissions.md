# Set up permissions

To make full use of Resource Groups and Tag Editor, you might need additional permissions to tag
resources or to see a resource's tag keys and values. These permissions fall into the
following categories:

- Permissions for individual services so that you can tag resources from those
  services and include them in resource groups.
- Permissions that are required to use the Tag Editor console
- Permissions that are required to use the AWS Resource Groups console and API.
  If you are an administrator, you can provide permissions for your users by creating
  policies through the AWS Identity and Access Management (IAM) service. You first create your principals, such as
  IAM roles or users, or associate external identities with your AWS environment using
  a service like AWS IAM Identity Center. Then you apply policies with the permissions that your users
  need. For information about creating and attaching IAM policies, see [Working with
  policies](../../../IAM/latest/UserGuide/ManagingPolicies.md "../../../IAM/latest/UserGuide/ManagingPolicies.md").

## Permissions for individual services

###### Important

This section describes permissions that are required if you want to tag
resources from other service consoles and APIs, and add those resources to
resource groups.

As described in [Resources and their group types](resource-groups.md#resource-groups-intro "resource-groups.md#resource-groups-intro"), each resource group represents a
collection of resources of specified types that share one or more tag keys or
values. To add tags to a resource, you need the permissions required for the service
to which the resource belongs. For example, to tag Amazon EC2 instances, your must have
permissions to the tagging actions in that service's API, such as those listed in
the [Amazon EC2 User Guide](../../../AWSEC2/latest/UserGuide/Using_Tags.md#Using_Tags_CLI "../../../AWSEC2/latest/UserGuide/Using_Tags.md#Using_Tags_CLI").

To make full use of the Resource Groups feature, you need other permissions that allow you
to access a service's console and interact with the resources there. For examples of
such policies for Amazon EC2, see [Example policies for working
in the Amazon EC2 console](../../../AWSEC2/latest/UserGuide/iam-policies-ec2-console.md "../../../AWSEC2/latest/UserGuide/iam-policies-ec2-console.md") in the
_Amazon EC2 User Guide_.

## Required permissions for

Resource Groups and Tag Editor

To use Resource Groups and Tag Editor, the following permissions must be added to a user's
policy statement in IAM. You can add either AWS-managed policies that are
maintained and kept up-to-date by AWS, or you can create and maintain your own
custom policy.

### Using AWS managed

policies for Resource Groups and Tag Editor permissions

AWS Resource Groups and Tag Editor support the following AWS managed policies that you
can use to provide a predefined set of permissions to your users. You can attach
these managed policies to any user, role or group just as you would any other
policy that you create.

**[ResourceGroupsandTagEditorReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ResourceGroupsandTagEditorReadOnlyAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ResourceGroupsandTagEditorReadOnlyAccess")**

This policy grants the attached IAM role or user permission to
call the read-only operations for both Resource Groups and Tag Editor. To read a
resource's tags, you must also have permissions for that resource
through a separate policy (see the following Important note).

**[ResourceGroupsandTagEditorFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ResourceGroupsandTagEditorFullAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ResourceGroupsandTagEditorFullAccess")**

This policy grants the attached IAM role or user permission to
call any Resource Groups operation and the read and write tag operations in
Tag Editor. To read or write a resource's tags, you must also have
permissions for that resource through a separate policy (see the
following Important note).

###### Important

The two previous policies grant permission to call the Resource Groups and Tag Editor
operations and use those consoles. For Resource Groups operations, those policies are
sufficient and grant all the permissions needed to work with any resource in
the Resource Groups console.

However, for tagging operations and the Tag Editor console, permissions are
more granular. You must have permissions not only to invoke the operation,
but also appropriate permissions to the specific resource whose tags you're
trying to access. To grant that access to the tags, you must also attach one
of the following policies:

- The AWS-managed policy [ReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ReadOnlyAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ReadOnlyAccess") grants permissions to the read-only
  operations for every service's resources. AWS automatically keeps
  this policy up to date with new AWS services as they become
  available.
- Many services provide a service-specific read-only AWS-managed
  policies that you can use to limit access to only the resources
  provided by that service. For example, Amazon EC2 provides [AmazonEC2ReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess").
- You could create your own policy that grants access to only the
  very specific read-only operations for the few services and
  resources you want your users to access. This policy use either an
  "allow list" strategy or a deny list strategy.

An allow list strategy takes advantage of the fact that access is
denied by default until you **_explicitly allow_** it in a
policy. So you can use a policy like the following example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [ "resource-groups:*" ],
 "Resource": "arn:aws:resource-groups:*:123456789012:group/*"
 }
 ]
}`

```

Alternatively, you could use a "deny list" strategy that allows
access to all resources except those that you explicitly
block.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [ "resource-groups:*" ],
 "Resource": "arn:aws:resource-groups:*:123456789012:group/*"
 }
 ]
}`

```

### Adding Resource Groups and Tag Editor

permissions manually

- `resource-groups:*` (This permission allows all Resource Groups
  actions. If you instead want to restrict actions that are available to a
  user, you can replace the asterisk with a [specific Resource Groups
  action](../../../IAM/latest/UserGuide/list_awsresourcegroups.md "../../../IAM/latest/UserGuide/list_awsresourcegroups.md"), or to a comma-separated list of actions)
- `cloudformation:DescribeStacks`
- `cloudformation:ListStackResources`
- `tag:GetResources`
- `tag:TagResources`
- `tag:UntagResources`
- `tag:getTagKeys`
- `tag:getTagValues`
- `resource-explorer:*`

###### Note

The `resource-groups:SearchResources` permission allows Tag Editor to list resources when
you filter your search using tag keys or values.

The `resource-explorer:ListResources` permission allows Tag Editor to list resources
when you search resources without defining search tags.

To use Resource Groups and Tag Editor in the console, you also need permission to run the
`resource-groups:ListGroupResources` action. This permission is
necessary for listing available resource types in the current Region. Using
policy conditions with `resource-groups:ListGroupResources` is not
currently supported.
