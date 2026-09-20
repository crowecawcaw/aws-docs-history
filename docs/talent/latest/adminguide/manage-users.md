

# Manage users
<a name="manage-users"></a>

Add users to Amazon Connect Talent and configure them with information and permissions. Each user receives a [security profile](manage-security-profiles.md) that determines what they can access and do.

## View users
<a name="manage-users-view"></a>

To view users, navigate to **Settings** > **Admin** > **User management**. The page displays a table of all users in your instance. From this page, you can search for users, add users, delete users, refresh the list, and choose a user name to edit that user.

## To add a user individually
<a name="manage-users-add-individually"></a>

1. Choose **Add user**.

1. Choose **Add a user manually**.

1. Enter the first name, last name, email address, username, and security profile. For user pool directory instances, also enter a password of 8–64 characters.

1. Choose **Save**.

**Note**  
For SAML-based instances, the **Password** field does not appear. The username must match the identity configured in your identity provider (IdP).

## To add users in bulk from a CSV file
<a name="manage-users-bulk-add"></a>

1. Choose **Add user**.

1. Choose **Import users using a .csv template**.

1. Download the template, fill in user data, and upload the completed file.

1. Review the validation results. The system displays errors by row if any exist.

1. Choose **Save**.

## To delete a user
<a name="manage-users-delete"></a>

1. Select the checkbox next to one or more users.

1. Choose **Delete user**.

1. Confirm the deletion.

You can select multiple users to delete them in bulk.