This is version 2.18 of the AWS Elemental Conductor File documentation. This is the
latest version. For prior versions, see the _Archive_ section of
[AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Add Users

To set up users for the entire cluster, you need to perform this setup only on the Conductor node. If you have two Conductor nodes, you need to perform this setup only on the primary Conductor node.

If you answered Yes to the installer prompt “Do you wish to enable authentication”, then users must be set up on the node to access the AWS Elemental product from both interfaces as follows:

- The web interface: When the user goes to the web interface, a login page will appear.
- The REST API: REST commands must include additional HTTP headers that identify the user: X-Auth-User header, X-Auth-Expires header, X-Auth-Key header (which includes the API key that each user creates for themselves).

For information on REST API access with user authentication, see the documentation on the REST API.

###### To add users

1. Make sure that you are logged into the Conductor web interface as the “admin” user you created via the configure script.
2. Hover over **Configuration** (cog icon) on the main menu and choose **Users** from the dropdown menu.
3. On the Conductor Configuration screen, choose **Settings** > **Users**.
4. On the Users screen, complete all fields and choose **Create**. Some notes:
   - **Expires**: If selected, the user will automatically expire after the specified period of time.
   - **Force Password Reset**: If checked, the user must reset their password the first time they login.
   - **Role**: Select a role: Admin, Manager, User, Viewer. For information about the actions allowed with each role, see the following section _user Roles_.

5. If your organization uses the REST API, make sure to tell each user to choose **Settings** > **User Profile** to make a note of their personal API key.

This API key is randomly generated when the user is created. It cannot be created manually (meaning that you cannot specify a specific set of characters for the key).

###### User roles

This section describes the actions that each user role can perform.

- **Viewer**
  - Read-only access to AWS Elemental Conductor File and AWS Elemental Server

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
  - Access to the entire AWS Elemental Conductor File and AWS Elemental Server systems, including all of the
    access provided by the other roles
