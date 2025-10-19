# View and end active sessions for your workforce users

As an IAM Identity Center administrator, you can view the list of your workforce users' active sessions, and if required, end one or more sessions for a user. For example, you might need to end a user's sessions when:


* The user no longer requires the sessions.
* The user shouldn't maintain their current authentication state. This can occur when they leave the company or their permissions change.
You can view and end these sessions by using the IAM Identity Center console. Your users can also view and end their own sessions by using the AWS access portal. For information about how your workforce users can view and end their sessions without assistance from an administrator, see [Viewing and ending your active session](end-user-how-to-end-active-sessions-accessportal.md "end-user-how-to-end-active-sessions-accessportal.md").

###### Note

Ending an active session for an IAM Identity Center user doesn't end any active IAM role sessions in the AWS Management Console or AWS CLI. For more information, see [Understanding authentication sessions in IAM Identity Center](authconcept.md "authconcept.md").

###### To end an active session for a workforce user (IAM Identity Center console)

1. Open the IAM Identity Center console.
2. Choose **Users**.
3. On the **Users** page, choose the username of the user whose sessions you want to manage. This takes you to a page with the user's information.
4. On the user's page, choose the **Active sessions** tab. The number in parentheses next to **Active sessions** indicates the number of active sessions for this user.
5. ###### Search for user background sessions (optional)


To search for sessions by the Amazon Resource Name (ARN) of the job that is using the session, in the **Session type** list, choose **User background sessions**, and then enter the job ARN in the search box.


###### Note

You can only end active sessions that are loaded. If a user has many sessions, choose **Load more active sessions** to display additional sessions.
6. Select the check box next to each session that you want to end, and then choose **End sessions**.
7. A dialog box appears that confirms you are ending active sessions for this user. Review the information, and if you want to continue, type `confirm`, and then choose **End sessions**.
8. You are returned to the user's page. A green notification message appears to indicate that the selected sessions were successfully ended.
