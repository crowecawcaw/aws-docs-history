This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Add Users

When you enable local authentication on the node, users must enter valid credentials to
access the node. This section describes how to create users. For information about user
authentication, see [User Authentication Reference](config-wrkr-srvr-cg-auth-ref.md "config-wrkr-srvr-cg-auth-ref.md").

###### Note

If you enabled PAM authentication, your users are maintained in the LDAP server. You can
manage the roles through the node, as described in [Create New User Roles](config-wrkr-srvr-cg-users-create.md "config-wrkr-srvr-cg-users-create.md"), but you don't add the users to
the node.

###### To add users

1. Log in to the AWS Elemental Server web interface using the REST API administrator credentials that you
   created when you enabled authentication.
2. Hover over **Settings** and choose **Users**.
3. On the **Users** screen, choose **New User**.
4. Complete all fields and choose **Create**. Some notes:
   - **Expires**: If selected, the user name automatically expires after
     the specified period of time.
   - **Force Password Reset**: If checked, the users must reset their
     passwords the first time they log in.
   - **Role**: Select a role. The available options are Admin, Manager, User, Viewer. For
     information about the actions allowed with each role, see the following section _User roles_.

5. If your organization uses the REST API, make sure to tell each user to choose
   **Settings** > **User Profile** to make note of
   their personal API key. Users have a different key for each node that they can
   access.

This API key is randomly generated when the user is created. You can't manually set
the API key.

###### User roles

Node access is defined by the role assigned to the user. This section describes the
actions that each user role can perform.

- **Viewer**
  - Read-only access to AWS Elemental Server

- **Operator**
  - Same access as Viewer
  - Control the state of a job (cancel, archive, etc)

- **Manager**
  - Same access as Viewer
  - Same access as Operator
  - Create and edit jobs
  - Create and edit presets
  - Create and edit profiles
  - Create and edit watch folders

- **Administrator**
  - Access to the entire AWS Elemental Server system, including all of the access
    provided by the other roles
