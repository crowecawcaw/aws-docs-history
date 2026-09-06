

# Grant users access to the AWS Security Agent web application
<a name="grant-user-access"></a>

AWS Security Agent provides two methods for users to access the web application, depending on how you configured your Agent Space during setup.

## Access methods overview
<a name="_access_methods_overview"></a>

 **IAM Identity Center (SSO)** - If you enabled IAM Identity Center when creating your Agent Space, users can access the web application directly through SSO. You assign users to the Agent Space through the AWS Security Agent console, and users log in using their Identity Center credentials.

 **Admin Access** - Users with AWS Console access can launch the web application through an admin access link on the Agent Space overview page in the AWS Management Console.

## Grant access with IAM Identity Center (SSO)
<a name="_grant_access_with_iam_identity_center_sso"></a>

If you configured your Agent Space with IAM Identity Center, you can assign users to the Agent Space using the AWS Security Agent console.

### Assign users through the AWS Security Agent console
<a name="_assign_users_through_the_aws_security_agent_console"></a>

1. In the AWS Security Agent Management Console, navigate to your Agent Space.

1. Select the **Web app** tab.

1. In the **Users** table, choose **Add users**.

1. Select existing users from IAM Identity Center or create new users.

1. Confirm the user assignments.

**Tip**  
Users assigned to the Agent Space can access the web application by logging in through IAM Identity Center with their SSO credentials.

### Access the web application with SSO
<a name="_access_the_web_application_with_sso"></a>

After users are assigned to the Agent Space:

1. Users navigate to the web application URL for the Agent Space.
**Tip**  
Find the web app URL on the Agent Space detail page in the AWS Security Agent console by selecting **Copy web app URL**. Users should bookmark this URL for easy access.

1. Users log in using their SSO credentials.

1. After authentication, users can select the Agent Space and begin conducting security assessments.

## Grant access with IAM-only access
<a name="_grant_access_with_iam_only_access"></a>

If you configured your Agent Space with IAM-only access, users with AWS Console access can launch the web application through an admin access link.

### Use the admin access link
<a name="_use_the_admin_access_link"></a>

1. Log into the AWS Security Agent console.

1. Navigate to the Agent Space you want to access.

1. On the Web app tab of the Agent Space landing page choose the **Admin access** button to launch the web application.

1. The web application opens in a new tab with the user automatically authenticated.

**Note**  
The admin access link is only available to users who are already authenticated to the AWS Console with appropriate AWS Security Agent permissions. This method does not require IAM Identity Center configuration.

## Next steps
<a name="_next_steps"></a>

After granting users access to the web application:
+ Users can create and manage penetration test configurations and runs
+ Users can create and manage design reviews
+ Users can view security findings and remediation guidance
+ Configure notification preferences for security findings