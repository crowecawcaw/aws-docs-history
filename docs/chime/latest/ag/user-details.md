**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# Viewing user details

In the Amazon Chime console, under **Users**, you can view a list of all the users in your account and see their user
details. Search for a specific user by their email address and choose their name to see their user details. Under
**User details**, you can see detailed information
about the user, and make updates to their user account.

The following table lists the user details that appear in the console.

###### Note

Complete user details don't appear for Team account users until after they accept their invites.

| Field                    | Description                                                                                                                                                                                 | Example                                                                                                                |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Display name**         | The user's name that appears in Amazon Chime. For Login with Amazon<br>(LWA) users, this is the full name. For Active Directory users, the<br>DISPLAY_NAME_ATTRIBUTE is used.               | Major, Mary                                                                                                            |
| **Email address**        | For LWA users, the email address used for registration. For<br>Active Directory users, the primary email address from Active<br>Directory appears.                                          | mary.major@example.com                                                                                                 |
| **Registration**         | The user’s current registration status. The possible values are<br>different between Enterprise accounts, where invitations are not<br>sent, and Team accounts, where invitations are sent. | **Registered**,<br>**Unregistered\*<br>• (for a Team account), or<br>**Suspended\*<br>• (for an Enterprise<br>account) |
| **Permission tier**      | Set to **Pro\*<br>• by default, to allow users to<br>host meetings. It can be changed to<br>**Basic\*\*.                                                                                    | **Pro**, **Basic**                                                                                                     |
| **Invited**              | For Team accounts, the date when the user was invited to the<br>account.                                                                                                                    | 01/05/2020                                                                                                             |
| **Joined**               | The date when the user first signed into Amazon Chime. For Pro trial<br>users, this is also the date that their Pro trial began.                                                            | 01/10/2020                                                                                                             |
| **Personal PIN**         | The personal meeting PIN that the user can use to schedule<br>meetings.                                                                                                                     | 0123456789                                                                                                             |
| **Privacy setting**      | The presence setting that the user selected.                                                                                                                                                | **Public\*<br>• or<br>**Private\*\*                                                                                    |
| **Meetings attended**    | The number of meetings that a user has attended.                                                                                                                                            | 87                                                                                                                     |
| **Meetings organized**   | The number of meetings that a user has organized.                                                                                                                                           | 12                                                                                                                     |
| **Meeting satisfaction** | The percentage of positive responses given to the end-of-meeting<br>survey.                                                                                                                 | 92%                                                                                                                    |
| **Last active date**     | The date when the user was last active.                                                                                                                                                     | 06/12/2020                                                                                                             |
| **Chat messages sent**   | The number of chat messages the user sent.                                                                                                                                                  | 1025                                                                                                                   |
| **Phone number**         | The phone number assigned to a user, if any.                                                                                                                                                | +12065550100                                                                                                           |
