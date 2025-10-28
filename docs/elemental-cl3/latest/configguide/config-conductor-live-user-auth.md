# Configuring user authentication in

Conductor Live

You can enable user authentication on the cluster, so that
all users
must provide valid credentials to work from either the web interface or the REST API. When user
authentication is enabled, users must provide the following credentials:

- For the web interface, users must enter user credentials—a user name and a password.
- For the REST API, users must include these additional HTTP headers
  (`X-Auth-User`, `X-Auth-Expires`, `X-Auth-Key`) in
  commands that they send.

For more information about using the API with authentication enabled, see the AWS Elemental Conductor Live
REST API documentation.
**Benefits**

User authentication has the following benefits:

- It prevents unauthorized access to nodes.
- It lets an administrator track node activity on a per-user basis.

###### Topics

- [About
  user authentication](config-conductor-live-user-auth-overview.md "config-conductor-live-user-auth-overview.md")
- [Step 1: Enable
  the
  user authentication
  feature](conductor-live-config-auth.md "conductor-live-config-auth.md")
- [Step 2:
  Apply user
  authentication on worker
  nodes](conductor-live-config-auth-wrkr.md "conductor-live-config-auth-wrkr.md")
- [Disabling user authentication](conductor-live-config-auth-chg.md "conductor-live-config-auth-chg.md")
