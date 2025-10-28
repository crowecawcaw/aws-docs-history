# Required roles and permissions

AWS Control Tower uses IAM roles to help manage access to resources.

For general information about roles, see [User groups, roles, and permission sets](user-groups-roles-permissions.md "user-groups-roles-permissions.md").

###### About permissions

- For information about IAM groups and their permissions in AWS Control Tower, see [IAM Identity Center groups for AWS Control Tower](sso-groups.md "sso-groups.md").
- For information about permissions required to provision accounts, see [Permissions required for accounts](permissions.md "permissions.md").
- For information about console permissions required for AWS Control Tower, see [Permissions required to use the AWS Control Tower console](additional-console-required-permissions.md "additional-console-required-permissions.md").

###### About roles

- For information about how to create a role, including permissions designed for programmatic access, see [Create roles and assign permissions](assign-permissions.md "assign-permissions.md"), and [Programmatic roles and trust relationships for the AWS Control Tower audit account](roles-how.md#stacksets-and-roles "roles-how.md#stacksets-and-roles").
- For information about other roles that AWS Control Tower uses to manage your accounts, see [Using identity-based policies (IAM policies) for AWS Control Tower](access-control-managing-permissions.md "access-control-managing-permissions.md"), and the [Managed policies for AWS Control Tower](managed-policies-table.md "managed-policies-table.md").
- For information about AWS Control Tower and AWS Config roles, see [AWS Control Tower ConfigRecorderRole](aws-controltower-configrecorderrole.md "aws-controltower-configrecorderrole.md").
- For information about roles that AWS Control Tower uses to aggregate AWS Config information for your accounts, see [How AWS Control Tower aggregates AWS Config rules in unmanaged OUs and accounts](roles-how.md#config-role-for-organizations "roles-how.md#config-role-for-organizations").
- For information about how to protect your resources as you are assigning roles and permissions, see [Optional conditions for your role trust relationships](conditions-for-role-trust.md "conditions-for-role-trust.md"), [Optionally configure AWS KMS keys](configure-kms-keys.md "configure-kms-keys.md"), and [Prevent cross-service impersonation](prevent-confused-deputy.md "prevent-confused-deputy.md").
- For specific information about automated account provisioning in AWS Control Tower with IAM roles, see [Automated Account Provisioning with IAM Roles](roles-how.md#automated-provisioning "roles-how.md#automated-provisioning").
- To view the policy that protects the AWS Config SNS topic, see [The AWS Config SNS topic policy](receive-notifications.md#config-sns-policy "receive-notifications.md#config-sns-policy").
