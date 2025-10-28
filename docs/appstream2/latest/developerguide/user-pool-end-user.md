# User Pool End User Experience for Amazon AppStream 2.0

The following steps summarize the initial connection experience for users in the user
pool.

1. You create new users in the Region you want by specifying their email
   addresses.
2. AppStream 2.0 sends them a welcome email.
3. You assign one or more stacks to the users.
4. AppStream 2.0 sends them an optional notification email. This email includes
   information about how to access the stacks that are newly assigned to
   them.
5. The users connect to the login portal by entering the information included in
   the welcome email, and they set a permanent password. The login portal link
   never expires and can be used any time.
6. They sign in to AppStream 2.0 by entering their email address and permanent password.
7. After they sign in, the users can view their application catalogs.
   The login portal link provided in the welcome email should be saved for future use, as
   it does not change and is valid for all users in the user pool. The login portal URL and
   users in the user pool are managed on a per-Region basis.
