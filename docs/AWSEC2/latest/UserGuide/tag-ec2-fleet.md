# Tag a new or existing EC2 Fleet request and the instances and

volumes it launches

To help categorize and manage your EC2 Fleet requests and the instances and volumes that it
launches, you can tag them with custom metadata. You can assign a tag to an EC2 Fleet request
when you create it, or afterward. Similarly, you can assign a tag to the instances and
volumes when they're launched by the fleet, or afterward.

When you tag a fleet request, the instances and volumes that are launched by the fleet
are not automatically tagged. You need to explicitly tag the instances and volumes
launched by the fleet. You can choose to assign tags to only the fleet request, or to
only the instances launched by the fleet, or to only the volumes attached to the
instances launched by the fleet, or to all of them.

###### Note

For `instant` fleet types, you can tag volumes that are attached to
On-Demand Instances and Spot Instances. For `request` or `maintain` fleet types, you
can only tag volumes that are attached to On-Demand Instances.

For more information about how tags work, see [Tag your Amazon EC2 resources](Using_Tags.md "Using_Tags.md").

**Prerequisite**

Grant the user the permission to tag resources. For more information, see [Example: Tag resources](ExamplePolicies_EC2.md#iam-example-taggingresources "ExamplePolicies_EC2.md#iam-example-taggingresources").

###### To grant a user the permission to tag resources

Create a IAM policy that includes the following:

- The `ec2:CreateTags` action. This grants the user permission to
  create tags.
- The `ec2:CreateFleet` action. This grants the user permission to
  create an EC2 Fleet request.
- For `Resource`, we recommend that you specify `"*"`.
  This allows users to tag all resource types.
  To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

###### To tag a new EC2 Fleet request

To tag an EC2 Fleet request when you create it, specify the key-value pair in the [JSON file](create-ec2-fleet.md#ec2-fleet-cli-skeleton "create-ec2-fleet.md#ec2-fleet-cli-skeleton") used to create the fleet. The
value for `ResourceType` must be `fleet`. If you specify
another value, the fleet request fails.

###### To tag instances and volumes launched by an EC2 Fleet

To tag instances and volumes when they are launched by the fleet, specify the tags
in the [launch template](create-launch-template.md "create-launch-template.md") that is
referenced in the EC2 Fleet request.

###### Note

You can't tag volumes attached to Spot Instances that are launched by a
`request` or `maintain` fleet type.

###### To tag an existing EC2 Fleet request, instance, and volume

Use the [create-tags](../../../cli/latest/reference/ec2/create-tags.md "../../../cli/latest/reference/ec2/create-tags.md") command
to tag existing resources.

```
aws ec2 create-tags \
    --resources `fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE` `i-1234567890abcdef0` `vol-1234567890EXAMPLE` \
    --tags Key=`purpose`,Value=`test`
```
