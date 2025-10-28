# Managing users in

Conductor Live

If you have enabled user authentication, you must add users to the
cluster. After you've added users, you can manage existing users and add new
users. If you don't enable user authentication, there is no need to create
users. However, we strongly advise against deploying a cluster without user
authentication enabled.

You perform user management tasks as follows:

- If you've set up with local authentication on the cluster, you manage users and user
  roles using AWS Elemental Conductor Live, as described in this section.
- If you've set up with PAM authentication on the cluster, you manage
  users on your organization's LDAP server.

###### Note

The username of a user is case sensitive.

###### Topics

- [Types of users](users-types.md "users-types.md")
- [Adding users to Conductor Live](conductor-live-config-users.md "conductor-live-config-users.md")
- [Adding users to
  worker nodes](config-conductor-live-users-add-workers.md "config-conductor-live-users-add-workers.md")
- [Role policies for PAM
  authentication](config-rpolicies.md "config-rpolicies.md")
