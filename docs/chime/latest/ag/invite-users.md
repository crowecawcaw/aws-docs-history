**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# Invite multiple users

The following example shows how to invite multiple users to an Amazon Chime `Team`
account.

```
List<String> emails = new ArrayList<>();
emails.add("`janedoe@example.com`");
emails.add("`richardroe@example.net`");
InviteUsersRequest inviteUsersRequest = new InviteUsersRequest()
    .withAccountId("`chimeAccountId`")
    .withUserEmailList(emails);

chime.inviteUsers(inviteUsersRequest);
```
