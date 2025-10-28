# Use instance profiles

Use an instance profile to pass an IAM role to an EC2 instance. For more information, see
[IAM roles for Amazon EC2](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md") in the
_Amazon EC2 User Guide_.

## Managing instance profiles

(console)

If you use the AWS Management Console to create a role for Amazon EC2, the console automatically creates an
instance profile and gives it the same name as the role. When you then use the Amazon EC2 console
to launch an instance with an IAM role, you can select a role to associate with the instance.
In the console, the list that's displayed is actually a list of instance profile names. The
console does not create an instance profile for a role that is not associated with
Amazon EC2.

You can use the AWS Management Console to delete IAM roles and instance profiles for Amazon EC2 if the
role and the instance profile have the same name. To learn more about deleting instance
profiles, see [Delete roles or instance profiles](id_roles_manage_delete.md "id_roles_manage_delete.md").

###### Note

To update permissions for an instance, replace its instance profile. We do not recommend
removing a role from an instance profile, because there is a delay of up to one hour before
this change takes effect.

## Managing instance profiles (AWS CLI or AWS

API)

If you manage your roles from the AWS CLI or the AWS API, you create roles and instance
profiles as separate actions. Because roles and instance profiles can have different names,
you must know the names of your instance profiles as well as the names of roles they contain.
That way you can choose the correct instance profile when you launch an EC2 instance.

You can attach tags to your IAM resources, including instance profiles, to identify,
organize, and control access to them. You can tag instance profiles only when you use the
AWS CLI or AWS API.

###### Note

An instance profile can contain only one IAM role, although a role can be included in
multiple instance profiles. This limit of one role per instance profile cannot be increased.
You can remove the existing role and then add a different role to an instance profile. You
must then wait for the change to appear across all of AWS because of [eventual consistency](https://en.wikipedia.org/wiki/Eventual_consistency "https://en.wikipedia.org/wiki/Eventual_consistency"). To
force the change, you must [disassociate the instance profile](../../../AWSEC2/latest/APIReference/API_DisassociateIamInstanceProfile.md "../../../AWSEC2/latest/APIReference/API_DisassociateIamInstanceProfile.md") and then [associate the instance
profile](../../../AWSEC2/latest/APIReference/API_AssociateIamInstanceProfile.md "../../../AWSEC2/latest/APIReference/API_AssociateIamInstanceProfile.md"), or you can stop your instance and then restart it.

### Managing instance profiles (AWS CLI)

You can use the following AWS CLI commands to work with instance profiles in an AWS
account.

- Create an instance profile: [`aws iam
create-instance-profile`](../../../cli/latest/reference/iam/create-instance-profile.md "../../../cli/latest/reference/iam/create-instance-profile.md")
- Tag an instance profile: [`aws iam
tag-instance-profile`](../../../cli/latest/reference/iam/tag-instance-profile.md "../../../cli/latest/reference/iam/tag-instance-profile.md")
- List tags for an instance profile: [`aws iam
list-instance-profile-tags`](../../../cli/latest/reference/iam/list-instance-profile-tags.md "../../../cli/latest/reference/iam/list-instance-profile-tags.md")
- Untag an instance profile: [`aws iam
untag-instance-profile`](../../../cli/latest/reference/iam/untag-instance-profile.md "../../../cli/latest/reference/iam/untag-instance-profile.md")
- Add a role to an instance profile: [`aws iam
add-role-to-instance-profile`](../../../cli/latest/reference/iam/add-role-to-instance-profile.md "../../../cli/latest/reference/iam/add-role-to-instance-profile.md")
- List instance profiles: [`aws iam
list-instance-profiles`](../../../cli/latest/reference/iam/list-instance-profiles.md "../../../cli/latest/reference/iam/list-instance-profiles.md"), [`aws iam
list-instance-profiles-for-role`](../../../cli/latest/reference/iam/list-instance-profiles-for-role.md "../../../cli/latest/reference/iam/list-instance-profiles-for-role.md")
- Get information about an instance profile: [`aws iam
get-instance-profile`](../../../cli/latest/reference/iam/get-instance-profile.md "../../../cli/latest/reference/iam/get-instance-profile.md")
- Remove a role from an instance profile: [`aws iam
remove-role-from-instance-profile`](../../../cli/latest/reference/iam/remove-role-from-instance-profile.md "../../../cli/latest/reference/iam/remove-role-from-instance-profile.md")
- Delete an instance profile: [`aws iam
delete-instance-profile`](../../../cli/latest/reference/iam/delete-instance-profile.md "../../../cli/latest/reference/iam/delete-instance-profile.md")

You can also attach a role to an already running EC2 instance by using the following
commands. For more information, see [IAM Roles for Amazon EC2](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#attach-iam-role "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#attach-iam-role").

- Attach an instance profile with a role to a stopped or running
  EC2 instance: [`aws ec2
associate-iam-instance-profile`](../../../cli/latest/reference/ec2/associate-iam-instance-profile.md "../../../cli/latest/reference/ec2/associate-iam-instance-profile.md")
- Get information about an instance profile attached to an EC2
  instance: [`aws ec2
describe-iam-instance-profile-associations`](../../../cli/latest/reference/ec2/describe-iam-instance-profile-associations.md "../../../cli/latest/reference/ec2/describe-iam-instance-profile-associations.md")
- Detach an instance profile with a role from a stopped or
  running EC2 instance: [`aws ec2
disassociate-iam-instance-profile`](../../../cli/latest/reference/ec2/disassociate-iam-instance-profile.md "../../../cli/latest/reference/ec2/disassociate-iam-instance-profile.md")

### Managing instance profiles (AWS

API)

You can call the following AWS API operations to work with instance profiles in an
AWS account.

- Create an instance profile: [`CreateInstanceProfile`](../APIReference/API_CreateInstanceProfile.md "../APIReference/API_CreateInstanceProfile.md")
- Tag an instance profile: [`TagInstanceProfile`](../APIReference/API_TagInstanceProfile.md "../APIReference/API_TagInstanceProfile.md")
- List tags on an instance profile: [`ListInstanceProfileTags`](../APIReference/API_TagInstanceProfile.md "../APIReference/API_TagInstanceProfile.md")
- Untag an instance profile: [`UntagInstanceProfile`](../APIReference/API_TagInstanceProfile.md "../APIReference/API_TagInstanceProfile.md")
- Add a role to an instance profile: [`AddRoleToInstanceProfile`](../APIReference/API_AddRoleToInstanceProfile.md "../APIReference/API_AddRoleToInstanceProfile.md")
- List instance profiles: [`ListInstanceProfiles`](../APIReference/API_ListInstanceProfiles.md "../APIReference/API_ListInstanceProfiles.md"), [`ListInstanceProfilesForRole`](../APIReference/API_ListInstanceProfilesForRole.md "../APIReference/API_ListInstanceProfilesForRole.md")
- Get information about an instance profile: [`GetInstanceProfile`](../APIReference/API_GetInstanceProfile.md "../APIReference/API_GetInstanceProfile.md")
- Remove a role from an instance profile: [`RemoveRoleFromInstanceProfile`](../APIReference/API_RemoveRoleFromInstanceProfile.md "../APIReference/API_RemoveRoleFromInstanceProfile.md")
- Delete an instance profile: [`DeleteInstanceProfile`](../APIReference/API_DeleteInstanceProfile.md "../APIReference/API_DeleteInstanceProfile.md")

You can also attach a role to an already running EC2 instance by calling the following
operations. For more information, see [IAM Roles for Amazon EC2](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#attach-iam-role "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#attach-iam-role").

- Attach an instance profile with a role to a stopped or running
  EC2 instance: [`AssociateIamInstanceProfile`](../../../AWSEC2/latest/APIReference/API_AssociateIamInstanceProfile.md "../../../AWSEC2/latest/APIReference/API_AssociateIamInstanceProfile.md")
- Get information about an instance profile attached to an EC2
  instance: [`DescribeIamInstanceProfileAssociations`](../../../AWSEC2/latest/APIReference/API_DescribeIamInstanceProfileAssociations.md "../../../AWSEC2/latest/APIReference/API_DescribeIamInstanceProfileAssociations.md")
- Detach an instance profile with a role from a stopped or
  running EC2 instance: [`DisassociateIamInstanceProfile`](../../../AWSEC2/latest/APIReference/API_DisassociateIamInstanceProfile.md "../../../AWSEC2/latest/APIReference/API_DisassociateIamInstanceProfile.md")
