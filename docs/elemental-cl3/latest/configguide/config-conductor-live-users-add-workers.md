# Adding users to

worker nodes

Read this section if you've set up for [local user authentication](config-conductor-live-users.md#config-conductor-live-users.title "config-conductor-live-users.md#config-conductor-live-users.title").
You
can add users to worker nodes.

(If PAM authentication is enabled, you manage users on your
organization's LDAP server.)

On the worker nodes,
you should only add regular administrators, and only so that they can troubleshoot problems on
a node. We recommend that you create access only for
one or two
people
Typically
you set up these people as regular administrators on a worker node

- Peope
  who are administrators of the cluster. Make sure you create at least one
  administrator on each node.
- People
  who are managers of teams.

###### Note

The user names that you assign are case sensitive. The user
_Myuser_ is not the same as the user
_myuser_.

###### To add users

1. Log into the worker node as _apiadmin_. If you followed the procedure in [Step 2:
   Apply user
   authentication on worker
   nodes](conductor-live-config-auth-wrkr.md "conductor-live-config-auth-wrkr.md"), then this user is the
   only user that initially exists on the node.
2. Hover over **Settings** and choose
   **Users**, then choose **New
   User** (on the far right of the page).
3. Complete the fields as appropriate. You can leave **API
   Key** empty. A key will automatically be generated.
4. Choose **Create**. The user is created with the specified role.
5. Give each user this information:
   - Give the user their user name (case sensitive) and
     password.
   - Advise the user to display their user information. They must
     log into the worker web interface. Then on the menu bar, they can
     hover over **Settings** and choose **User
     Profile**,
