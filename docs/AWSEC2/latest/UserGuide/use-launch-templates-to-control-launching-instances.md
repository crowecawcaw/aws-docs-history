# Use Amazon EC2 launch

templates to control launching Amazon EC2 instances

You can control the configuration of your Amazon EC2 instances by specifying that users can
only launch instances if they use a launch template, and that they can only use a
specific launch template. You can also control who can create, modify, describe, and
delete launch templates and launch template versions.

## Use launch templates to control

launch parameters

A launch template can contain all or some of the parameters to configure an
instance at launch. However, when you launch an instance using a launch template,
you can override parameters that are specified in the launch template. Or, you can
specify additional parameters that are not in the launch template.

###### Note

You can't remove launch template parameters during launch (for example, you
can't specify a null value for the parameter). To remove a parameter, create a
new version of the launch template without the parameter and use that version to
launch the instance.

To launch instances, users must have permission to use the
`ec2:RunInstances` action. Users must also have permissions to create
or use the resources that are created or associated with the instance. You can use
resource-level permissions for the `ec2:RunInstances` action to control
the launch parameters that users can specify. Alternatively, you can grant users
permissions to launch an instance using a launch template. This enables you to
manage launch parameters in a launch template rather than in an IAM policy, and to
use a launch template as an authorization vehicle for launching instances. For
example, you can specify that users can only launch instances using a launch
template, and that they can only use a specific launch template. You can also
control the launch parameters that users can override in the launch template. For
example policies, see [Launch templates](ExamplePolicies_EC2.md#iam-example-runinstances-launch-templates "ExamplePolicies_EC2.md#iam-example-runinstances-launch-templates").

## Control the use of launch

templates

By default, users do not have permissions to work with launch templates. You can
create a policy that grants users permissions to create, modify, describe, and
delete launch templates and launch template versions. You can also apply
resource-level permissions to some launch template actions to control a user's
ability to use specific resources for those actions. For more information, see the
following example policies: [Example: Work with launch
templates](ExamplePolicies_EC2.md#iam-example-launch-templates "ExamplePolicies_EC2.md#iam-example-launch-templates").

Take care when granting users permissions to use the
`ec2:CreateLaunchTemplate` and
`ec2:CreateLaunchTemplateVersion` actions. You can't use
resource-level permissions to control which resources users can specify in the
launch template. To restrict the resources that are used to launch an instance,
ensure that you grant permissions to create launch templates and launch template
versions only to appropriate administrators.

## Important security

concerns when using launch templates with EC2 Fleet or Spot Fleet

To use launch templates, you must grant your users permissions to create, modify,
describe, and delete launch templates and launch template versions. You can control
who can create launch templates and launch template versions by controlling access
to the `ec2:CreateLaunchTemplate` and
`ec2:CreateLaunchTemplateVersion` actions. You can also control who
can modify launch templates by controlling access to the
`ec2:ModifyLaunchTemplate` action.

###### Important

If an EC2 Fleet or Spot Fleet is configured to use the Latest or Default launch template
version, the fleet is not aware if Latest or Default are later changed to point
to a different launch template version. When a different launch template version
is used for Latest or Default, Amazon EC2 does not re-check permissions for actions
to be completed when launching new instances to fulfil the fleet’s target
capacity. This is an important consideration when granting permissions to who
can create and manage launch template versions, particularly the
`ec2:ModifyLaunchTemplate` action that allows a user to change
the Default launch template version.

By granting a user permission to use the EC2 actions for the launch template APIs,
the user is effectively also granted the `iam:PassRole` permission if
they create or update an EC2 Fleet or Spot Fleet to point to a different launch template
version that contains an instance profile (a container for an IAM role). It means
that a user can potentially update a launch template to pass an IAM role to an
instance even if they don’t have the `iam:PassRole` permission. For more
information and an example IAM policy, see [Using an IAM role
to grant permissions to applications running on Amazon EC2 instances](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2.md") in the
_IAM User Guide_.

For more information, see [Control the use of launch
templates](#launch-template-permissions "#launch-template-permissions") and [Example: Work with launch
templates](ExamplePolicies_EC2.md#iam-example-launch-templates "ExamplePolicies_EC2.md#iam-example-launch-templates").
