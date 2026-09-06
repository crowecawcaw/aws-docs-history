

# User interactive sessions
<a name="user-interactive-sessions"></a>

User interactive sessions are sessions tied to a user's sign-in to the AWS access portal or access to [AWS managed applications](awsapps.md). The session duration of authentication into the AWS access portal and applications is the maximum length of time that a user can be signed in without re-authenticating. If you end an active AWS access portal session, this also ends any sessions for these managed applications.

The default session duration for user interactive sessions is 8 hours. You can specify a different duration, from a minimum of 15 minutes to a maximum of 90 days. Custom duration values must be entered in minutes and be between 15 minutes and 129,600 minutes (90 days). For more information, see [Understanding authentication sessions in IAM Identity Center](authconcept.md).

For considerations such as how IAM Identity Center identity sources might affect the user interactive session duration, see [Session duration considerations for using identity sources, the AWS CLI, and AWS SDKs](user-session-duration-prereqs-considerations.md). 

**To configure the duration of a user interactive session**

1. Open the IAM Identity Center console.

1. Choose **Settings**.

1. On the **Settings** page, choose the **Authentication** tab.

1. Under **Authentication**, next to **Session duration**, choose **Configure**. A **Configure session duration** dialog box appears.

1. In the **Configure session duration** dialog box, under **User interactive sessions**, choose the maximum session duration for your users by selecting the drop-down arrow. Choose the length for the session, and then choose **Save**.
**Note**  
Changes to session duration apply only to new sessions. Current sessions keep their original duration.

1. You are returned to the **Authentication** tab. A green notification message appears above the tab indicates that the session settings were updated successfully.