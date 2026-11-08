

# Grant users access to the AWS Security Agent web application
<a name="grant-user-access"></a>

AWS Security Agent provides two methods for users to access the web application, depending on how you configured your Agent Space during setup.

## Access methods overview
<a name="_access_methods_overview"></a>

 **IAM Identity Center (SSO)** - If you enabled IAM Identity Center when creating your Agent Space, assign individual users or IAM Identity Center groups to the Agent Space in the AWS Security Agent console. Group assignments let you manage access for teams without assigning each user individually. Users sign in to the web application with their Identity Center credentials.

 **Admin Access** - Users with AWS Console access can launch the web application through an admin access link on the Agent Space overview page in the AWS Management Console.

## Grant access with IAM Identity Center (SSO)
<a name="_grant_access_with_iam_identity_center_sso"></a>

If you configured your Agent Space with IAM Identity Center, you can assign individual users, IAM Identity Center groups, or both to the Agent Space using the AWS Security Agent console.

### Assign users through the AWS Security Agent console
<a name="_assign_users_through_the_aws_security_agent_console"></a>

1. In the AWS Security Agent Management Console, navigate to your Agent Space.

1. Choose the **Web app** tab.

1. In the **Users** table, choose **Add users**.

1. Select existing users from IAM Identity Center or create new users.

1. Confirm the user assignments.

**Tip**  
Users assigned to the Agent Space can access the web application by logging in through IAM Identity Center with their SSO credentials.

### Assign groups through the AWS Security Agent console
<a name="grant-user-access-groups"></a>

Assign a group to give its direct members access to the Agent Space without assigning each user individually. Create groups and manage their membership in IAM Identity Center. In AWS Security Agent, you assign existing groups to Agent Spaces. Only direct group members receive access because IAM Identity Center doesn’t support nested groups.

To assign groups to an Agent Space:

1. In the AWS Security Agent Management Console, navigate to your Agent Space.

1. Choose the **Web app** tab.

1. In the **Groups** table, choose **Add groups**.

1. In **IAM Identity Center groups**, search for groups by name and select the groups to add.

1. Confirm the group assignments.

The selected groups appear in the **Groups** table. Their direct members can access the Agent Space.

Keep the following in mind when you assign groups:
+ You can assign up to 100 groups to an Agent Space. IAM Identity Center also limits the AWS Security Agent application to 100 assigned groups across all of its Agent Spaces.
+ You can add groups only from the AWS Security Agent console in the primary Region of your IAM Identity Center instance. Group assignment isn’t supported in additional (replica) Regions.
+ Removing a user from an assigned group, or deleting the group in IAM Identity Center, removes that user’s group-based access. Deleting the group doesn’t remove its assignment from the Agent Space. To remove the leftover assignment, delete the row from the **Groups** table.
+ For users who are already signed in, changes to group membership can take up to two minutes to apply. Signing in again immediately picks up changes that are already available in IAM Identity Center. If you synchronize groups from an external identity provider, synchronization can add another delay before the changes are available in IAM Identity Center.

### Remove a group from an Agent Space
<a name="_remove_a_group_from_an_agent_space"></a>

To remove a group from an Agent Space:

1. In the AWS Security Agent Management Console, navigate to your Agent Space.

1. Choose the **Web app** tab.

1. In the **Groups** table, select the groups to remove, and then choose **Delete groups**.

1. Confirm the deletion.

Removing a group takes effect on the next request, including for users who are already signed in. Members of a removed group lose access to the Agent Space unless you assign them individually or through another group.

### Access the web application with SSO
<a name="_access_the_web_application_with_sso"></a>

After users or groups are assigned to the Agent Space:

1. Users navigate to the web application URL for the Agent Space.
**Tip**  
Find the web application URL on the Agent Space detail page in the AWS Security Agent console. Bookmark this URL for easy access.

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