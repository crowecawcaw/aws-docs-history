# Set up user permissions

With the complex option, MediaLive users must have permissions to use the trusted entity wizard.
This wizard is in the **IAM Role** section on the **Channel and input
details** pane:

![IAM role configuration options for AWS Elemental MediaLive channel access permissions.](images/medialiveaccessrole_withUpdateButton.png)
Topics

## Set up wizard permissions

You must set up all MediaLive users with permission to use the wizard to type a trusted entity
role into the wizard. Users will refer to the list of roles that you will give them.

You must give all users the access described in the following table. The action is in the
IAM service. Include this action in the policy (or in one of the policies) that you create for
the users.

| Fields in the wizard                 | Description                                                                                                                                                                                                                                                                                                                                                               | Actions        |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| Use existing role                    | Users must _not<br>• be able to view the list in the<br>selection field that accompanies the \*\*Use existing role_<br>• field.<br>That list shows all the roles that are created in the AWS account. Users must not<br>be able to select from this list. Instead of selecting an existing role, users<br>will type a role into the **Specify custom role ARN**<br>field. | None           |
| **Create role from template option** | Users must _not<br>• be able to select the<br>\*\*Create role from template_<br>• field. Users don't create roles. Only<br>administrators create roles.                                                                                                                                                                                                                   | None           |
| **Specify custom role ARN**          | Users must be able to type a role into the entry field that accompanies the<br>\*_Specify custom role ARN_<br>• field. They must then be able to pass that<br>role to MediaLive.                                                                                                                                                                                          | `iam:PassRole` |
| **Update**                           | Users do _not<br>• need to be able to choose the<br>\*\*Update_<br>• button because this button only ever appears in implementations<br>that use `MediaLiveAccessRole`. The complex option does not use this role;<br>therefore, this button never appears.                                                                                                               | None           |

## Information that users need

When a user creates a channel, they will pass a role to MediaLive to set up MediaLive with the
correct trusted policies. You created these policies when you [set up the trusted entity](setup-trusted-entity-complex.md "setup-trusted-entity-complex.md"). Specifically, when you
[created the trusted entity
role](complex-scenario-create-trusted-entity-role-step3.md "complex-scenario-create-trusted-entity-role-step3.md"), you made a note of the ARNs of all the roles that you created.

You must give each user a list of the roles (identified by an ARN) that they must use with
each workflow (channel) that they work with.

- Make sure that you give each user the correct roles for the workflows that they are
  responsible for. Each role gives MediaLive access the resources that apply for a specific
  workflow.
- Each user probably has a different list of roles.

When the user selects **Specify custom role ARN**, the user will consult
their list to find the workflow the channel applies to and the role ARN that therefore
applies.
