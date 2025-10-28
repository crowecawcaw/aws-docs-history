# AWS Partner Central permissions best practices

When assigning AWS Partner Central roles, use the following guidelines.

###### Topics

- [Assign roles according to the principle of least privilege](#least-privilege "#least-privilege")
- [Audit role assignments](#audit-role-assignments "#audit-role-assignments")
- [Use unique credentials](#use-unique-credentials "#use-unique-credentials")
- [Avoid generic logins](#avoid-generic-logins "#avoid-generic-logins")

## Assign roles according to the principle of least privilege

Users should have permissions to access only those resources that they need to perform their jobs. For example, if one of your team members is responsible only for updating and reporting on opportunities across your pipeline in the APN Customer Engagements (ACE) Pipeline Manager they should have the ACE manager role, not the alliance team role. For more information, refer to [Apply least privilege permissions](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") in the IAM User Guide.

## Audit role assignments

Periodically audit your role assignments and adjust permissions as people change roles at your organization. Audit your user list to ensure you have deactivated users who have left your organization or moved to roles that no longer require access to AWS Partner Central.

## Use unique credentials

Ensure that users log in to AWS Partner Central with unique login credentials. Sharing user credentials violates the AWS Partner Network and AWS Partner Network Customer Engagements (ACE) terms and conditions and creates security risks.

## Avoid generic logins

Avoid keeping a generic login (for example, `APN_Admin@company.com`) assigned to
the alliance lead role. Follow best practices for managing permissions and avoid having multiple
users sign in to AWS Partner Central with the same generic credentials. Instead, reassign an
individual user to the alliance lead role, assign other users to the roles they require, and
deactivate the generic account.

###### To reassign a generic login

1. Identify all of the users currently signing in to AWS Partner Central with the generic login.
2. Assign an individual user to the alliance lead role.
3. Assign other users to roles based on the principle of least privilege. For a summary of
   roles and their permissions, refer to [AWS Partner Central roles](role-summaries.md "role-summaries.md").
4. Confirm that all assigned users can access AWS Partner Central. After confirmation is
   complete, the alliance lead can deactivate the generic account.

######

To deactivate a generic account

1. Sign in to [AWS Partner Central](https://partnercentral.awspartner.com/APNLogin "https://partnercentral.awspartner.com/APNLogin") with the alliance lead role.
2. Choose **View my APN Account.**
3. In the **Partner Users section**, choose **Manage Active Partner Users**.
4. For the generic account, choose **Deactivate** from the action menu.
