# Managing users for IAM-based domains

As a domain administrator, you can use the domain user management page for IAM-based
domains to view all users that are active in the domain. From this page, you can manage access,
update permissions, and modify project membership from a single screen.

To access user management, choose **Users** in the left navigation pane
of the domain administration page.

## Viewing and filtering users

The **Users** page displays all users in the domain. You can use the
following options to find specific users:

- **Search** — Search across all users by
  name.
- **Filter by type** — Filter the list by user
  type: IAM, SSO user, or SSO group.
- **Filter by designation** — Filter by
  designation: Owner or Contributor.
- **Filter by status** — Filter users by their
  Active or Inactive status.

## Adding a user

You can add IAM users and roles, SSO users, or SSO groups to your domain and assign
permissions and project membership.

###### Note

If you are adding an IAM role or user, the [SageMakerStudioUserIAMConsolePolicy](security-iam-awsmanpol-SageMakerStudioUserIAMConsolePolicy.md "security-iam-awsmanpol-SageMakerStudioUserIAMConsolePolicy.md") managed policy must be attached to the
role or user.

To add a new user to the domain, complete the following steps.

1. On the **Users** page, choose **Add user**.
2. For **Type**, select IAM or SSO, and then search for the user or
   group to add.
3. Choose **Next** to assign permissions and project
   membership.
4. (Optional) To make the user a domain administrator, select the
   **Administrator** designation.
5. (Optional) To add the user to existing projects, choose
   **Add project**. Select the project and assign the project
   designation. You can add the user to a maximum of 8 projects.
6. Choose **Add** to add the user to the domain.

The user now appears on the **Users** page.

## Editing a user

You can modify user settings such as status, domain designation, and project
membership.

1. On the **Users** page, choose the user name from the list.
2. Modify the user settings as needed:

   - **Status** — Set to
     _Active_ to allow the user to log in to Amazon SageMaker Unified Studio, or
     _Inactive_ to prevent access.
   - **Domain designation** — Update the user's
     domain-level designation.
   - **Project membership** — Add the user to
     existing projects or remove them from current projects.

3. Choose **Save** to apply your changes.
