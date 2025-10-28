# Adding users to Conductor Live

Read this section if you've set up for [local
user authentication](config-conductor-live-users.md "config-conductor-live-users.md"). You must add regular administrators, operators, and viewers to
the cluster. You add these types of users by working on the primary Conductor Live.

(If PAM authentication is enabled, you manage users on your organization's LDAP
server.)

###### Note

When you add users to Conductor Live, keep in mind that the usernames that you assign are case
sensitive. The user _Myuser_ is not the same as the user
_myuser_.

###### To add the first user

To create the first user, you must log in as the API admin (_apiadmin_). But after you've created this user, you should always log in as a
regular administrator.

1. Log into the primary Conductor Live web interface as _apiadmin_. You created this user when you enabled user authentication
2. On the menu bar, choose **Settings**. Then choose
   **Users** from the left bar. Then choose **New User**.
3. Complete the fields as appropriate. Set up the user as **Admin**. You
   can leave the REST API key empty. Conductor Live will generate a key.
4. Choose **Create**. The user is created.

###### To add more users

Log in as a regular administrator and add more users.

1. Log into the primary Conductor Live web interface as a regular administrator.
2. On the menu bar, choose **Settings**. Then choose
   **Users** from the left bar. Then choose **New User**.
3. Complete the fields as appropriate. Choose any role. You can leave **API
   Key** empty. A key will automatically be generated.
4. Choose **Create**. The user is created with the specified
   role.
5. Give each user this information:
   - Give the user their user name (case sensitive) and password.
   - Advise the user to change their password. They must log onto the Conductor Live web
     interface. Then on the menu bar, they can select their name and choose
     **Account** from the dropdown menu. The
     **Account** page has a **Change Password** button
     in the top right corner.
   - If your organization uses the REST API, advise the user to make a note of their
     personal API key. They must log into the Conductor Live web interface. Then on the menu bar,
     they can select their name. The API key appears on the dropdown menu.
   - Tell the user how to log out. On the right side of the menu bar on any page, they
     select **Logout**.
