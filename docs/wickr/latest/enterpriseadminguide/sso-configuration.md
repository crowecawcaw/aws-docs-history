This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# SSO configuration

SSO configuration allows an administrator to add SSO authentication to a specific
network. If using ADFS it is also possible to sync Wickr security groups with active
directory user groups.

- **Network Endpoint:** This is the URL of the Enterprise endpoint to
  enter into your SSO system. This is pre-filled based on the supplied install hostname
  and may not be what your physical networking requires.
- **SSO Configuration:** These options are what Enterprise will use
  to connect to your SSO system.

###### Note

The Company ID value will be visible to end users during registration. This ID
must be unique per network as it is used to point the Enterprise client to the
specific SSO resource.

- **Security Group Synchronization:** When SSO is configured with an
  ADFS or openLDAP system, this will allow the local Enterprise Security Groups to be
  synchronized with an OU on the ADFS side.

- **Grace period for token refresh:** Occasionally, there may be
  instances where identity providers encounter temporary or extended outages, which may
  lead to your users being logged out unexpectedly due to a failed refresh token for their
  client session. To prevent this problem, you can establish a grace period that allows
  your users to remain signed in even if their client refresh token fails during such
  outages.

Here are the available options for the grace period:

    + No grace period (default): Users will be signed out immediately after a refresh
     token failure.
    + 30-minute grace period: Users can stay signed in for up to 30 minutes after a
     refresh token failure.
    + 60-minute grace period: Users can stay signed in for up to 60 minutes after a
     refresh token failure.
