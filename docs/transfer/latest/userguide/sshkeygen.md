# Generate SSH keys for service-managed users

You can set up your server to authenticate users using the service managed
authentication method, where usernames and SSH keys are stored within the service. The
user's public SSH key is uploaded to the server as a user's property. This key
is used by the server as part of a standard key-based authentication process. Each user
can have multiple public SSH keys on file with an individual server. For limits on
number of keys that can be stored per user, see [AWS Transfer Family endpoints and quotas](../../../general/latest/gr/transfer-service.md "../../../general/latest/gr/transfer-service.md")
in the _Amazon Web Services General Reference_.

As an alternative to the service managed authentication method, you can authenticate
users using a custom identity provider, or AWS Directory Service for Microsoft Active Directory. For more information, see
[Working with custom identity providers](custom-idp-intro.md "custom-idp-intro.md") or [Using AWS Directory Service for Microsoft
Active Directory](directory-services-users.md "directory-services-users.md").

A server can only authenticate users using one method (service managed, directory
service, or custom identity provider), and that method cannot be changed after the
server is created.

###### Topics

- [Creating SSH keys on macOS, Linux, or
  Unix](macOS-linux-unix-ssh.md "macOS-linux-unix-ssh.md")
- [Creating SSH keys on Microsoft Windows](windows-ssh.md "windows-ssh.md")
- [Converting an SSH2 key to SSH public key
  format](convert-ssh2-public-key.md "convert-ssh2-public-key.md")
