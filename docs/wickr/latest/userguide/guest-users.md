This guide provides documentation for AWS Wickr. For Wickr
Enterprise, which is the on-premises version of Wickr, see [Enterprise Administration Guide](../enterpriseadminguide/what-is-wickr.md "../enterpriseadminguide/what-is-wickr.md").

# AWS Wickr Guest users

The Wickr guest user feature allows individual guest users to sign in to the Wickr
client and collaborate with Wickr network users.

###### Important

The guest users feature must be enabled for the Wickr network. If you are a guest
user and experience difficulties communicating with users who are registered to a
Wickr network, then the guest users feature might not be enabled for the Wickr
network. Users who are registered to the Wickr network should get in touch with their
Wickr administrator to determine if the guest users feature is enabled. Wickr
administrators see [Guest users](../adminguide/guest-users.md "../adminguide/guest-users.md") in the
_Wickr Administration Guide_.

###### Topics

- [Guest user account limitations](#guest-user-limitations "#guest-user-limitations")
- [Sign up for a guest account in the Wickr client](guest-user-sign-up.md "guest-user-sign-up.md")
- [Close a guest user account in the Wickr client](close-account.md "close-account.md")
- [Report a user in the Wickr client](report-user.md "report-user.md")

## Guest user account limitations

The following limitations apply to guest user accounts:

- Guest users can’t initiate communication with Wickr network users. Wickr
  network users can start communication with guest users and add guest users to
  direct messages, rooms, or groups to initiate a secure conversation. Guest users
  can share their registered email address to let Wickr network users know how
  to find them on Wickr.

###### Note

Wickr network users can find guest users when writing a direct message,
creating a room, or a group message. The dialog box when [writing a direct message](message-write.md "message-write.md"), [creating a room](room-create.md "room-create.md"), or [group message](room-create.md "room-create.md") allows you to search for
network and guest users.

- Guest users can't create rooms or groups. Wickr network users can create a
  room or group, and add guests and external users from other Wickr networks (if
  federation is enabled). After that, guest users can send messages in the room or
  group, view members, and start a direct message.
- Guest users can’t be moderators or add members in Wickr rooms and
  groups.
- Guest users can communicate with each other only when the guest users are in
  the same room as a network user.
- A guest user can continue communicating in the Wickr network, only if a
  network user has communicated with the guest within the last 90 days.
- Message expiration settings are limited to a maximum period of 30 days for
  guest users. For more information, see [Set message expiration and
  burn timers](message-timers.md "message-timers.md").
