

# Required roles and permissions
<a name="roles-overview"></a>

AWS Control Tower uses IAM roles to help manage access to resources.

For general information about roles, see [User groups, roles, and permission sets](https://docs.aws.amazon.com/controltower/latest/userguide/user-groups-roles-permissions.html).

**About permissions**
+ For information about IAM groups and their permissions in AWS Control Tower, see [IAM Identity Center groups for AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/sso-groups.html).
+ For information about permissions required to provision accounts, see [Permissions required for accounts](https://docs.aws.amazon.com/controltower/latest/userguide/permissions.html).
+ For information about console permissions required for AWS Control Tower, see [Permissions required to use the AWS Control Tower console](https://docs.aws.amazon.com/controltower/latest/userguide/additional-console-required-permissions.html).

**About roles**
+ For information about how to create a role, including permissions designed for programmatic access, see [Create roles and assign permissions](https://docs.aws.amazon.com/controltower/latest/userguide/assign-permissions.html), and [Programmatic roles and trust relationships for the AWS Control Tower audit account](https://docs.aws.amazon.com/controltower/latest/userguide/roles-how.html#stacksets-and-roles).
+ For information about other roles that AWS Control Tower uses to manage your accounts, see [Using identity-based policies (IAM policies) for AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/access-control-managing-permissions.html), and the [Managed policies for AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/managed-policies-table.html).
+ For information about AWS Control Tower and AWS Config roles, see [AWS Control Tower ConfigRecorderRole](https://docs.aws.amazon.com/controltower/latest/userguide/aws-controltower-configrecorderrole.html).
+ For information about roles that AWS Control Tower uses to aggregate AWS Config information for your accounts, see [How AWS Control Tower aggregates AWS Config rules in unmanaged OUs and accounts](https://docs.aws.amazon.com/controltower/latest/userguide/roles-how.html#config-role-for-organizations).
+ For information about how to protect your resources as you are assigning roles and permissions, see [Optional conditions for your role trust relationships](https://docs.aws.amazon.com/controltower/latest/userguide/conditions-for-role-trust.html), [Optionally configure AWS KMS keys](https://docs.aws.amazon.com/controltower/latest/userguide/configure-kms-keys.html), and [Prevent cross-service impersonation](https://docs.aws.amazon.com/controltower/latest/userguide/prevent-confused-deputy.html).
+ For specific information about automated account provisioning in AWS Control Tower with IAM roles, see [Automated Account Provisioning with IAM Roles](https://docs.aws.amazon.com/controltower/latest/userguide/roles-how.html#automated-provisioning).
+ To view the policy that protects the AWS Config SNS topic, see [The AWS Config SNS topic policy](https://docs.aws.amazon.com/controltower/latest/userguide/receive-notifications.html#config-sns-policy).