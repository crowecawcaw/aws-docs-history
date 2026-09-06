

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# Guide to Amazon Chime transition features
<a name="amazon-chime-transition-features"></a>

After careful consideration, we decided to end support for the Amazon Chime service, including Business Calling features, effective February 20, 2026. Amazon Chime will no longer accept new customers beginning February 19, 2025. As an existing customer with an Amazon Chime Team or Enterprise account created before February 19, 2025, you can continue to use Amazon Chime features, including Business Calling, scheduling and hosting meetings, adding and managing users, and other capabilities supported through the Amazon Chime admin console. After February 20, 2026, you will no longer be able to manage your users, host Amazon Chime meetings, or use any of the Business Calling features. Contact Support if you are unable to delete your data before February 20, 2026.

**Note**  
This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk).

This page provides instructions and best practices for Amazon Chime IT administrators and users to transition to alternate collaboration solutions to meet your business needs. This might include solutions provided by AWS, such as [Wickr](https://aws.amazon.com/wickr/), or from AWS partners, such as Slack, Webex, and Zoom. Visit the [AWS Marketplace](https://aws.amazon.com/marketplace) for more information about our AWS partners' solutions.

## Transition features for Amazon Chime administrators
<a name="transition-features"></a>

The following transition features are available to Amazon Chime administrators.

### Usage reporting
<a name="usage-reporting"></a>

Before you transition to a new collaboration solution, it may be helpful to understand who within your organization are active users and which features they are using. With Amazon Chime’s usage reporting, you can get contact information to reach out to your active users, collect use cases, and compile requirements for a new solution.

Usage reporting provides you with information on each user’s activity, including their name, email, registration status, user account creation date, meetings attended, meetings hosted, and messages sent. This data is available at a weekly level for each Team or Enterprise account that you have created in the Amazon Chime console. The weekly reports will show usage for weeks starting on Sunday 00:00 and ending on Saturday 23:59. Data processing may delay weekly reports until the Monday of the following week. All dates and times are presented using Coordinated Universal Time (UTC).

### Turn on usage reporting
<a name="turn-on-usage-reporting"></a>

An Amazon Simple Storage Service (Amazon S3) bucket is used as the destination for your weekly usage reporting CSV files. Follow these steps to create an Amazon S3 bucket or select an existing one where the Amazon Chime service will deliver the weekly usage reports. For more information about creating Amazon S3 buckets or navigating and managing access to existing Amazon S3 buckets, visit [Getting started with Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html) in the *Amazon S3 User Guide*.

1. Open the Amazon Chime console at [https://chime.aws.amazon.com/](https://chime.aws.amazon.com).

1. Select **Usage reporting** under **Global settings**.

1. To turn on the Amazon Chime usage reporting for your Amazon Chime account, first create or select an Amazon S3 bucket.

   1. Under **Report destination**, choose **New S3 bucket** to create a new bucket and enter a name following the guidance listed. You can also select **Existing S3 bucket** if you already have a location where you want to store the files.

   1. Choose **Save** to create the new S3 bucket or select an existing S3 bucket.

   1. Usage reporting is now turned on.

1. Your weekly usage reporting will begin on the following Sunday at midnight UTC, and files will be stored in the S3 bucket identified.  
![Set up the Amazon S3 bucket and turn on weekly usage reporting](http://docs.aws.amazon.com/chime/latest/ag/images/usage-reporting.png)

### Turn off usage reporting
<a name="turn-off-usage-reporting"></a>

You can stop generating new usage reports at any time.

1. Open the Amazon Chime console at [https://chime.aws.amazon.com/](https://chime.aws.amazon.com).

1. Select **Usage reporting** under **Global settings**.

1. Choose **Turn off reporting**.

1. Confirm that you want the reporting to be stopped by choosing **Disable**.  
![Confirm that weekly usage reporting should be turned off](http://docs.aws.amazon.com/chime/latest/ag/images/turn-off-usage-reporrting.png)

### Report contents
<a name="usage-report-contents"></a>

Reports are generated weekly. Complete the following steps to view the usage reporting.

1. To view your data, browse to the Amazon S3 console.

1. Locate the bucket name.

1. The weekly usage report file will be placed in the following location in your S3 bucket:

   ```
   Amazon-Chime-User-Activity-Reports/csv/{{<AWSaccountID>}}/{{<year>}}/{{<month>}}/{{<day>}}/{{<AmazonChimeAccountName>}}_{{<AmazonChimeAccountId>}}_{{<yyyymmdd>}}.csv
   ```

   For example:

   ```
   Amazon-Chime-User-Activity-Reports/csv/123456789012/2024/11/03/ExampleSales_12abcdef-34gh-56i7-89jk-01234lmnopq56_20241103.csv
   ```

1. The following fields are included in each report:
   +  Team or Enterprise account name
   +  Week starting date
   +  User’s display name associated with their Amazon Chime account
   +  User’s email address
   +  User’s registration status
   +  User’s account creation date
   +  The number of meetings that the user attended during the week
   +  The number of meetings that the user hosted during the week
   +  The number of messages that the user sent (1:1, group, and chat room posts) during the week  
![Fields and data included in the weekly usage report](http://docs.aws.amazon.com/chime/latest/ag/images/example-sales-report.png)

### Business calling - Phone number porting
<a name="business-calling-phone-number-porting"></a>

To aid in the transition from Amazon Chime Business Calling for voice and SMS, you can port your Business Calling phone numbers to another carrier. For more information see [Porting phone numbers out](porting.md#port-out).

### Managing your user accounts - Team accounts
<a name="manage-user-accounts-team-accounts"></a>

You will need to remove all users before you can delete your Team account. When you set up an Amazon Chime Team account, you can invite new users, set their permission level (Pro or Basic), configure regions and other account settings, and pay for users to host meetings or use Business Calling features. When you remove a user from an Amazon Chime Team, they are not able to use paid features, but they can continue to use messaging features and attend meetings. When you remove them, they still have access to the Amazon Chime user account and will maintain their contacts, 1:1 and group message history, and chat room membership.

1. Open the Amazon Chime console at [https://chime.aws.amazon.com/](https://chime.aws.amazon.com).

1. Click on a Team name under the Account name heading.

1. Click the Select all check box or the check box next to individual user(s).

1. Choose Remove user from the User actions menu.  
![Choose Remove user from the Action menu when managing a Team account](http://docs.aws.amazon.com/chime/latest/ag/images/remove-user.png)

Once your user(s) are removed, they can still sign in and access Amazon Chime, but they will no longer be able to host meetings. If they would like to delete their Amazon Chime account, they can use the delete me option using the Amazon Chime Assistant. For more information, see [Using the Amazon Chime Assistant to get attachments or request that your account be deleted](https://answers.chime.aws/articles/500/using-the-amazon-chime-assistant-to-get-attachment.html) in the *Amazon Chime Help Center*.

### Managing your user accounts - Enterprise accounts
<a name="manage-user-accounts-enterprise-accounts"></a>

You will need to remove all domains before you can delete your Enterprise account. You can upgrade from an Amazon Chime Team to an Enterprise account by claiming your domain. When you claim your domain, you prove that your company owns the domain and therefore will own your users’ data. All registered Amazon Chime users with email addresses that match your claimed domains will be pulled into your Enterprise account. You set their permission level (Pro or Basic), set account settings like supported meeting regions and chat retention rules, and pay for your users to host meetings or use Business Calling features. You can release all users by choosing to remove your domain(s). This process will reset each user’s profile and delete all data, contacts, 1:1 and group conversations, chat room membership and history. Once you unclaim a domain, users will no longer be able to sign in using SSO, host or schedule meetings, and the profile associated with their email address will be reset. If they want to continue to use Amazon Chime, they can create a new account following the instructions provided on the [Amazon Chime getting started page](https://aws.amazon.com/chime/getting-started). Once all domains are removed you can delete your Enterprise account.

1. Open the Amazon Chime console at [https://chime.aws.amazon.com/](https://chime.aws.amazon.com).

1. Choose the name of an Enterprise account in the **Account name** column.

1. Choose **Domains** under **Identity**.

1. Choose **Remove**.

1. When prompted, review the outcomes of completing this task and click the check box next to **I understand that this action cannot be reversed**.

1. Select **Remove**.  
![Removing a domain resets all your users’ profiles. Confirm that you understand the impact of removing the domain.](http://docs.aws.amazon.com/chime/latest/ag/images/remove-domain-2.png)

## Transition features for Amazon Chime Users
<a name="transition-features-chime-users"></a>

The following transition features are available to Amazon Chime administrators.

### Pro Users - Removing Amazon Chime from your meeting invites
<a name="remove-chime-meeting-invites"></a>

Amazon Chime auto-calls meeting attendees who are signed into their Amazon Chime clients when you have Amazon Chime Pro permissions and invite `meet@chime.aws` to your meetings. Either delete your meeting and re-create the invite using the new solution or complete the following procedure to remove the Amazon Chime meeting details from an existing meeting on your calendar.

1. Open your calendar application (not a mobile calendar application).

1. Open a recurring series or a meeting.

1. Take the following steps to remove Amazon Chime (and auto-calling) and add the new solution’s meeting instructions:

   1. Remove the `meet@chime.aws` and `pin+{{<meetingid>}}@chime.aws` from the **To:** field.

   1. Remove Amazon Chime meeting instructions from the body of the invite.

   1. If you have a new meeting solution, generate new meeting instructions and add it to the body.

1. Send the invite and be sure to choose to send the update to all.

1. Your meeting should no longer appear in your Amazon Chime Home page under **Upcoming meetings** and there will be no Amazon Chime auto-ring for your attendees.  
![Remove Amazon Chime users from the To: line and meeting instructions from the Body](http://docs.aws.amazon.com/chime/latest/ag/images/meeting-invite-changes-highlighted.png)

### Chat Room Administrators - Get a list of members
<a name="chat-room-members-list"></a>

Amazon Chime provides chat rooms for as many as 10,000 members. When you move to a new messaging solution, it can be helpful to be able to contact the members in your Amazon Chime room to recreate the chat room in your new solution. If you are a chat room administrator, you can export the name, email address, and role of each member of your chat room by completing the following procedure.

1. Sign into an Amazon Chime Windows, macOS, or [web client](https://app.chime.aws). This is not available using the mobile clients.

1. Navigate to a chat room where you have the Administrator role.

1. From **Room settings** (the ⋮ icon) choose **Export member list**.

1. You will be prompted to save the CSV file to your computer if you are using the Windows or macOS client. If you are performing this action from the [web client](https://app.chime.aws), the member list will be saved to your downloads folder. The default file name will include the room name.  
![Example file name: Amazon_Chime_Arnav Desai_Project_Team_room_member_list.csv](http://docs.aws.amazon.com/chime/latest/ag/images/chat-room-export-members-list.png)

### Amazon Chime Users - Export your personal contacts
<a name="chime-users-export-personal-contacts"></a>

Amazon Chime provides users with a personal contact list (with up to 100 contacts). You add Amazon Chime user information to your list of personal contacts when you invite them, or when you use the **Add to contacts** action displayed during meetings on the meeting roster, from your Contacts list, or choose the **Add to contacts** action next to their name in the **Favorites** or **Recent Messages** lists. When you move to a new messaging solution, it can be helpful to maintain user information for those outside your company or others that you have added to your personal contacts. The following procedure allows you to save relevant names, email addresses and phone numbers if you are using Business Calling.

1. Sign into an Amazon Chime Windows, macOS, or [web client](https://app.chime.aws). This is not available using the mobile clients.

1. Navigate to **Contacts** on the upper menu when you are using a Windows or macOS client or **View my contacts** under **Quick actions** on the [web client](https://app.chime.aws).

1. Choose **Export personal contacts**.

1. You will be prompted to save the CSV file to your computer if you are using the Windows or macOS client. If you are performing this action from the [web client](https://app.chime.aws), the member list will be saved to your **Downloads** folder.  
![Example file name: Amazon_Chime_(Arnav Desai)_personal_contacts.csv](http://docs.aws.amazon.com/chime/latest/ag/images/contacts-for-export.png)

## Summary
<a name="summary"></a>

Organizations with at least one Amazon Chime Team or Enterprise account, can continue to use Amazon Chime and Business Calling features until February 20, 2026, when support for the service will end. Features that will no longer be supported include scheduling and hosting meetings, adding and managing users, and other capabilities available using the Amazon Chime console.

## Additional Resources
<a name="additional-resources"></a>
+ [Amazon Chime website](https://aws.amazon.com/chime/)
+ [Amazon Chime User Guide](https://docs.aws.amazon.com/chime/latest/ug/)
+ [Amazon Chime Help Center](https://answers.chime.aws)
+ Learn more about [AWS Wickr](https://aws.amazon.com/wickr) and [AWS partner solutions](https://aws.amazon.com/marketplace).
+ If you need assistance or have feedback, contact [Support](https://aws.amazon.com/support/).