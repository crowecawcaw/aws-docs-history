After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Managing user access with SSO

###### Important

Amazon FinSpace Dataset Browser will be discontinued on `March 26,
 2025`. Starting `November 29, 2023`, FinSpace will no longer accept the creation of new Dataset Browser
environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/ "https://aws.amazon.com/finspace/features/managed-kdb-insights/") will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

This section describes how you can manage users in an Amazon FinSpace environment created
with SAML based SSO authentication.

###### Note

1. In order to create and manage users, you must be a superuser or a member
   of a group with necessary permissions - **Manage Users
   and Permission Groups**.
2. You will need administrator privileges to assign and remove users to your
   configured FinSpace application in your Identity Provider.
   You can invite users by creating a FinSpace account for them. When using SAML based
   Single Sign On as the authentication method for your FinSpace environment, you need to
   execute two steps to add users in FinSpace.

3. Assign user to your FinSpace application in your Identity Provider (IdP) with
   their email.
4. Create the user in FinSpace environment. The email of the user created in FinSpace
   environment must match their email in their identity record with the Identity
   provider.
   If above steps are not followed, a user will not be successfully authenticated to
   use FinSpace.

## Creating the first

superuser

The first superuser must be created after a new FinSpace environment is created.
The user must be assigned to the FinSpace application created in your IdP. See details
in [this section](create-an-amazon-finspace-environment.md "create-an-amazon-finspace-environment.md"). Once
the first superuser is created, they can sign in to FinSpace web application and setup
other superusers and application users. Subsequent superusers can be created by
the first superuser in the FinSpace web application.

## Inviting users to access FinSpace

In FinSpace, you can invite users by creating a FinSpace account for them. For more
information about signing in for the first time, see [Signing in to the Amazon FinSpace web application](signing-into-amazon-finspace.md "signing-into-amazon-finspace.md").

###### To create FinSpace accounts and invite users

1. Assign the new user to the application created for FinSpace in your
   IdP.
2. Sign in to the FinSpace web application. For more information, see [Signing in to the Amazon FinSpace web application](signing-into-amazon-finspace.md "signing-into-amazon-finspace.md").
3. On the left navigation bar of the home page, choose **Users and Groups**.
4. On the **Users and Permission Groups** page, choose
   **Add User**.
5. On the **Create User** page, specify the **User
   Details**. The email that you enter must match the email of the
   user record in your IdP.
6. For **Superuser**, choose **Yes** to
   designate the user as a superuser or **No** to designate
   this user as an application user.
7. For **Programmatic Access**, choose
   **Yes** to provide access to use FinSpace APIs and SDK or
   choose **No** to deny programmatic access.

When you choose **Yes**, you are required to specify the
**IAM Principal ARN** for this user in the format
`arn:partition:service::region::account::resource`. 8. Choose **Create User**. 9. After the account is created, copy the credentials to clipboard and share
them with the new user. The user can sign in to FinSpace with their SSO
credentials.

## Viewing user

details

###### To view details of a user

1. Sign in to the FinSpace web application. For more information, see [Signing in to the Amazon FinSpace web application](signing-into-amazon-finspace.md "signing-into-amazon-finspace.md").
2. On the left navigation bar of the home page, choose **Users and Groups**. The **Users and Permission Groups** page, displays the list of users under the **FinSpace Users** tab.
3. Select a user to view their details.

## Deactivating a

user

###### To deactivate a user

1. Remove the user from the list of assigned users from the FinSpace application
   in your Identity Provider (IdP).
2. Sign in to the FinSpace web application. For more information, see [Signing in to the Amazon FinSpace web application](signing-into-amazon-finspace.md "signing-into-amazon-finspace.md").
3. On the left navigation bar of the home page, choose **Users and Groups**.
4. Choose **FinSpace Users** tab.
5. Select a user to view their details.
6. On the top right corner, choose **More** menu.
7. Choose **Deactivate User**. This button is only visible to superusers and users with necessary permissions – **Manage Users and Permission Groups**.
8. On the confirmation dialog box, choose **Deactivate**. You can activate a user again later if necessary.
