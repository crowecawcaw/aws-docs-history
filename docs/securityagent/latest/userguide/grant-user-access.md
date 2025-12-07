# Grant users access to the AWS Security Agent web app

AWS Security Agent provides two methods for users to access the web application, depending on how you configured your Agent Space during setup.

## Access methods overview

**IAM Identity Center (SSO)** - If you enabled IAM Identity Center when creating your Agent Space, users can access the web application directly through SSO. You assign users to the Agent Space either through the IAM Identity Center console or through the AWS Security Agent console, and users log in using their Identity Center credentials.

**Admin Access** - Users with AWS Console access can launch the web application through an admin access link on the Agent Space overview page in the AWS Management Console.

## Grant access with IAM Identity Center (SSO)

If you configured your Agent Space with IAM Identity Center, you can assign users to the Agent Space using either the AWS Security Agent console or the IAM Identity Center console.

### Assign users through the AWS Security Agent console

1. In the AWS Security Agent Management Console, navigate to your Agent Space.
2. Select the **Web app** tab.
3. In the **Users** table, click **Add users**.
4. Select existing users from IAM Identity Center or create new users.
5. Confirm the user assignments.

###### Tip

Users assigned to the Agent Space can access the web application by logging in through IAM Identity Center with their SSO credentials.

### Assign users through the IAM Identity Center console

You can also manage user access directly from the IAM Identity Center console. Learn how to [assign user access to applications in the IAM Identity Center console](../../../singlesignon/latest/userguide/assignuserstoapp.md "../../../singlesignon/latest/userguide/assignuserstoapp.md") in the AWS IAM Identity Center User Guide.

### Access the web application with SSO

After users are assigned to the Agent Space:

1. Users navigate to the web application URL for the Agent Space.

###### Tip

Find the web app URL on the Agent Space detail page in the AWS Security Agent console by selecting **Copy web app URL**. Users should bookmark this URL for easy access. 2. Users log in using their SSO credentials. 3. After authentication, users can select the Agent Space and begin conducting security assessments.

## Grant access with IAM-only access

If you configured your Agent Space with IAM-only access, users with AWS Console access can launch the web application through an admin access link.

### Use the admin access link

1. Log into the AWS Security Agent console.
2. Navigate to the Agent Space you want to access.
3. On the Web app tab of the Agent Space landing page click the **Admin access** button to launch the web application.
4. The web application opens in a new tab with the user automatically authenticated.

###### Note

The admin access link is only available to users who are already authenticated to the AWS Console with appropriate AWS Security Agent permissions. This method does not require IAM Identity Center configuration.

## Next steps

After granting users access to the web application:

- Users can create and manage penetration test configurations and runs
- Users can create and manage design reviews
- Users can view security findings and remediation guidance
- Configure notification preferences for security findings
