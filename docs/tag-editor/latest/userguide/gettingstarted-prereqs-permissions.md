# Set up permissions

To make full use of Tag Editor, you might need additional permissions to tag
resources or to see a resource's tag keys and values. These permissions are in the
following categories:

- Permissions for individual services so that you can tag resources from
  those services and include them in resource groups.
- Permissions that are required to use the Tag Editor console.
  If you're an administrator, you can provide permissions for your users by creating
  policies through the AWS Identity and Access Management (IAM) service. You first create IAM roles, users,
  or groups, and then apply the policies with the permissions that they need. For
  information about creating and attaching IAM policies, see [Working with
  policies](../../../IAM/latest/UserGuide/ManagingPolicies.md "../../../IAM/latest/UserGuide/ManagingPolicies.md").

## Permissions for individual

services

###### Important

This section describes permissions that are required if you want to tag
resources **from other AWS service consoles and APIs**.

To add tags to a resource, you need the permissions required for the service
to which the resource belongs. For example, to tag Amazon EC2 instances, you must
have permissions to the tagging operations in that service's API, such as the
[Amazon EC2
CreateTags](../../../AWSEC2/latest/APIReference/API_CreateTags.md "../../../AWSEC2/latest/APIReference/API_CreateTags.md") operation.

## Permissions required to use the

Tag Editor console

To use the Tag Editor console to list and tag resources, the following permissions must be added to a user's policy
statement in IAM. You can add either AWS managed policies that are
maintained and kept up to date by AWS, or you can create and maintain your own
custom policy.

### Using AWS managed

policies for Tag Editor permissions

Tag Editor supports the following AWS managed policies that you can use to
provide a predefined set of permissions to your users. You can attach these
managed policies to any role, user, or group just as you would any other
policy that you create.

**[ResourceGroupsandTagEditorReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ResourceGroupsandTagEditorReadOnlyAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ResourceGroupsandTagEditorReadOnlyAccess")**

This policy grants the attached IAM role or user permission
to call the read-only operations for both AWS Resource Groups and Tag Editor.
To read a resource's tags, you must also have permissions for
that resource through a separate policy. Learn more in the following
**Important** note.

**[ResourceGroupsandTagEditorFullAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ResourceGroupsandTagEditorFullAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ResourceGroupsandTagEditorFullAccess")**

This policy grants the attached IAM role or user permission
to call any Resource Groups operation and the read and write tag
operations in Tag Editor. To read or write a resource's tags, you
must also have permissions for that resource through a separate
policy. Learn more in the following **Important** note.

###### Important

The two previous policies grant permission to call the Tag Editor
operations and use the Tag Editor console. However, you must also have
permissions not only to invoke the operation, but also appropriate
permissions to the specific resource whose tags you're trying to access.
To grant that access to the tags, you must also attach one of the
following policies:

- The AWS managed policy [ReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ReadOnlyAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/ReadOnlyAccess") grants
  permissions to the read-only operations for every service's
  resources. AWS automatically keeps this policy up to date with
  new AWS services as they become available.
- Many services provide service-specific read-only AWS managed
  policies that you can use to limit access to only the resources
  provided by that service. For example, Amazon EC2 provides [AmazonEC2ReadOnlyAccess](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess").
- You can create your own policy that grants access to only the
  specific read-only operations for the few services and resources
  you want your users to access. This policy uses either an
  allowlist strategy or a denylist strategy.

An allowlist strategy takes advantage of the fact that access
is denied by default until you **_explicitly allow_** it
in a policy. So, you can use a policy like the following
example.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [ "tag:*" ],
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`444455556666`:*",
 "arn:aws:s3:::`amzn-s3-demo-bucket2`"
 ]
 }
 ]
}`

```

Alternatively, you could use a denylist strategy that allows
access to all resources except those that you explicitly block.
This requires a separate policy that applies to the relevant
users that allows access. The following example policy then
denies access to the specific resources listed by the Amazon
Resource Name (ARN).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [ "tag:*" ],
 "Resource": [
 "arn:aws:ec2:`us-east-1`:`123456789012`:instance:*",
 "arn:aws:s3:::`amzn-s3-demo-bucket3`"
 ]
 }
 ]
}`

```

### Adding Tag Editor permissions

manually

- `tag:*` (This permission allows all Tag Editor actions. If
  you instead want to restrict actions that are available to a user,
  you can replace the asterisk with a [specific
  action](../../../IAM/latest/UserGuide/list_awsresourcegroups.md "../../../IAM/latest/UserGuide/list_awsresourcegroups.md"), or with a comma-separated list of
  actions.)
- `tag:GetResources`
- `tag:TagResources`
- `tag:UntagResources`
- `tag:getTagKeys`
- `tag:getTagValues`
- `resource-explorer:*`
- `resource-groups:SearchResources`
- `resource-groups:ListResourceTypes`

###### Note

The `resource-groups:SearchResources` permission allows Tag Editor to list resources when
you filter your search using tag keys or values.

The `resource-explorer:ListResources` permission allows Tag Editor to list resources
when you search resources without defining search tags.

## Granting permissions

for using Tag Editor

To add a policy for using AWS Resource Groups and Tag Editor to a role, do the
following.

1. Open the [IAM console
   to the **Roles** page](https://console.aws.amazon.com/iamv2/home#/roles "https://console.aws.amazon.com/iamv2/home#/roles").
2. Find the role to which you want to grant Tag Editor permissions. Choose
   the role's name to open the role's **Summary**
   page.
3. On the **Permissions** tab, choose **Add
   permissions**.
4. Choose **Attach existing policies directly**.
5. Choose **Create policy**.
6. On the **JSON** tab, paste the following policy
   statement.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "tag:GetResources",
 "tag:TagResources",
 "tag:UntagResources",
 "tag:getTagKeys",
 "tag:getTagValues",
 "resource-explorer:*",
 "resource-groups:SearchResources",
 "resource-groups:ListResourceTypes"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Note

This example policy statement grants permissions to perform only
Tag Editor actions. 7. Choose **Next: Tags** and then choose **Next:
Review**. 8. Enter a name and description for the new policy. For example,
`AWSTaggingAccess`. 9. Choose **Create policy**.

Now that the policy is saved in IAM, you can attach it to other principals,
such as roles, groups, or users. For more information about how to add a policy
to a principal, see [Adding
and removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _IAM User
Guide_.

## Authorization and access control based on

tags

AWS services support the following:

- **Action-based policies** – For
  example, you can create a policy that allows users to perform
  `GetTagKeys` or `GetTagValues` operations, but
  no others.
- **Resource-level permissions in
  policies** – Many services support using [ARNs](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") to
  specify individual resources in the policy.
- **Authorization based on tags** –
  Many services support using resource tags in the condition of a policy.
  For example, you can create a policy that allows users full access to a
  group that has the same tag as the users. For more information, see
  [What is ABAC for AWS?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _AWS Identity and Access Management User
  Guide_.
- **Temporary credentials** – Users
  can assume a role with a policy that allows Tag Editor operations.

Tag Editor doesn't use any service-linked roles.

For more information about how Tag Editor integrates with AWS Identity and Access Management (IAM), see
the following topics in the _AWS Identity and Access Management User Guide_:

- [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md#management_svcs "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md#management_svcs")
- [Actions, resources, and condition keys for Tag Editor](../../../service-authorization/latest/reference/list_awstageditor.md "../../../service-authorization/latest/reference/list_awstageditor.md")
- [Controlling access to
  AWS resources using policies](../../../IAM/latest/UserGuide/access_controlling.md "../../../IAM/latest/UserGuide/access_controlling.md")
