# Cookie-Based Authentication in Amazon AppStream 2.0

AppStream 2.0 uses browser cookies to authenticate streaming sessions and allow users to
reconnect to an active session without re-entering their sign-in credentials every time.
Authentication tokens are stored in browser cookies for every authentication scenario.
While cookies are necessary for many online services, they can potentially be vulnerable
to cookie theft attacks. We strongly recommend that you take proactive measures to
prevent cookie theft, such as implementing robust endpoint protection solutions for your
users' devices. Furthermore, to mitigate the potential impact in the event of cookie
theft, we advise you to consider the following actions:

- **Enforce single-session limit**: For your AppStream 2.0 Windows
  images, create a registry key under
  `HKEY_USERS\S-1-5-18\Software\GSettings\com\nicesoftware\dcv\session-management`
  with the name **max-concurrent-clients** set to 1 to only allow
  one connection at a time. This limits the number of concurrent session to one,
  and blocks mirroring of active sessions. For more information, see [session-management Parameters](../../../dcv/latest/adminguide/config-param-ref.md#session_management "../../../dcv/latest/adminguide/config-param-ref.md#session_management").
- **Enforce session expiry and re-authentication**
  - Reduce the SessionDuration value so that the authentication token
    expires after the user successfully starts the streaming session.
    Reusing authentication cookies after the sessionDuration expires
    requires users to re-authenticate themselves. SessionDuration specifies
    the maximum amount of time that a federated streaming session for a user
    can remain active before re-authentication is required. The default
    value is 60 minutes. For more information, see [Step 5: Create
    Assertions for the SAML Authentication Response](external-identity-providers-setting-up-saml.md#external-identity-providers-create-assertions "external-identity-providers-setting-up-saml.md#external-identity-providers-create-assertions").
  - To help maximize security, users should end sessions properly with the
    toolbar (terminate session), instead of closing the streaming window.
    Ending the session through the toolbar terminates both the user session
    and the streaming instance. This requires re-authentication for future
    access, preventing cookie misuse. If a user closes the streaming window
    without ending the session, the session and instance remains active for
    a configurable disconnect timeout period (in minutes). The disconnect
    timeout must be a number between 1 and 5760, with a default value of 15
    minutes. To prevent misuse of inactive sessions, we recommend setting a
    short disconnect timeout. For more information, see [Create a Fleet in Amazon AppStream 2.0](set-up-stacks-fleets-create.md "set-up-stacks-fleets-create.md").

- **Limit access to stream AppStream 2.0 applications to your IP
  ranges**: We recommend that you implement IP-based IAM policies.
  This ensures that AppStream 2.0 sessions can only be accessed from clients whose IP
  address belongs to an authorized IP range. All connection attempts initiated by
  a user whose client's IP address is outside an authorized range will be denied,
  even if they are presenting an otherwise valid authentication cookie
  (potentially stolen from a user). For more information, see [Limit access to stream Amazon AppStream 2.0 applications to your IP
  ranges](https://aws.amazon.com/blogs/desktop-and-application-streaming/limit-access-to-stream-amazon-appstream-2-0-applications-to-your-ip-ranges/ "https://aws.amazon.com/blogs/desktop-and-application-streaming/limit-access-to-stream-amazon-appstream-2-0-applications-to-your-ip-ranges/").
- **Add additional authentication**: To launch domain-joined
  streaming instances, you can join your AppStream 2.0 Always-On and On-Demand Windows
  fleets and image builders to domains in Microsoft Active Directory, and use your
  existing Active Directory domains, either cloud-based or on-premises. After the
  initial SAML-based authentication, your users will be prompted to provide their
  domain credentials for additional authentication against the organizational
  domain. For more information, see [Using Active Directory with AppStream 2.0](active-directory.md "active-directory.md").
  If you have any concerns or need help, contact [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").
