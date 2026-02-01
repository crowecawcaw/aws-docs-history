• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Step 2: Verify or

add instance permissions for Session Manager

By default, AWS Systems Manager doesn't have permission to perform actions on your
instances. You can provide instance permissions at the account level using an
AWS Identity and Access Management (IAM) role, or at the instance level using an instance profile. If your
use case allows, we recommend granting access at the account level using the Default
Host Management Configuration. If you've already set up the Default Host Management
Configuration for your account using the
`AmazonSSMManagedEC2InstanceDefaultPolicy` policy, you can proceed to
the next step. For more information about the Default Host Management Configuration,
see [Managing EC2
instances automatically with Default Host Management Configuration](fleet-manager-default-host-management-configuration.md "fleet-manager-default-host-management-configuration.md").

Alternatively, you can use instance profiles to provide the required permissions
to your instances. An instance profile passes an IAM role to an Amazon EC2 instance.
You can attach an IAM instance profile to an Amazon EC2 instance as you launch it or to
a previously launched instance. For more information, see [Using instance
profiles](../../../IAM/latest/UserGuide/roles-usingrole-instanceprofile.md "../../../IAM/latest/UserGuide/roles-usingrole-instanceprofile.md").

For on-premises servers or virtual machines (VMs), permissions are provided by the
IAM service role associated with the hybrid activation used to register your
on-premises servers and VMs with Systems Manager. On-premises servers and VMs do not use
instance profiles.

If you already use other Systems Manager tools, such as Run Command or Parameter Store, an instance
profile with the required basic permissions for Session Manager might already be attached
to your Amazon EC2 instances. If an instance profile that contains the AWS managed
policy `AmazonSSMManagedInstanceCore` is already attached to your
instances, the required permissions for Session Manager are already provided. This is also
true if the IAM service role used in your hybrid activation contains the
`AmazonSSMManagedInstanceCore` managed policy.

However, in some cases, you might need to modify the permissions attached to your
instance profile. For example, you want to provide a narrower set of instance
permissions, you have created a custom policy for your instance profile, or you want
to use Amazon Simple Storage Service (Amazon S3) encryption or AWS Key Management Service (AWS KMS) encryption options for
securing session data. For these cases, do one of the following to allow Session Manager
actions to be performed on your instances:

- **Embed permissions for Session Manager actions in a custom IAM
  role**

To add permissions for Session Manager actions to an existing IAM role that
doesn't rely on the AWS-provided default policy
`AmazonSSMManagedInstanceCore`, follow the steps in [Add
Session Manager permissions to an existing IAM role](getting-started-add-permissions-to-existing-profile.md "getting-started-add-permissions-to-existing-profile.md").

- **Create a custom IAM role with Session Manager permissions
  only**

To create an IAM role that contains permissions only for Session Manager
actions, follow the steps in [Create a custom
IAM role for Session Manager](getting-started-create-iam-instance-profile.md "getting-started-create-iam-instance-profile.md").

- **Create and use a new IAM role with permissions for
  all Systems Manager actions**

To create an IAM role for Systems Manager managed instances that uses a default
policy supplied by AWS to grant all Systems Manager permissions, follow the steps in
[Configure instance permissions required for Systems Manager](setup-instance-permissions.md "setup-instance-permissions.md").

###### Topics

- [Add
  Session Manager permissions to an existing IAM role](getting-started-add-permissions-to-existing-profile.md "getting-started-add-permissions-to-existing-profile.md")
- [Create a custom
  IAM role for Session Manager](getting-started-create-iam-instance-profile.md "getting-started-create-iam-instance-profile.md")
