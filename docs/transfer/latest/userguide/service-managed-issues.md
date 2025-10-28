# Troubleshoot service-managed user issues

This section describes possible solutions for issues with service-managed users.

###### Topics

- [Troubleshoot service-managed
  users](#transfer-service-managed-issues "#transfer-service-managed-issues")

## Troubleshoot service-managed

users

This section describes possible solutions for the following issues.

###### Topics

- [Troubleshoot public key body too long](#pgp-keys "#pgp-keys")
- [Troubleshoot failed to add SSH public key](#ssh2-public-keys "#ssh2-public-keys")

### Troubleshoot public key body too long

Description

When you try to create a service-managed user, you receive the following
error:

```
Failed to create user (1 validation error detected:
'sshPublicKeyBody' failed to satisfy constraint: Member must have length less than or equal to 2048)
```

Cause

You might be entering a PGP key for the public key body, and AWS Transfer Family does not
support PGP keys for service-managed users.

Solution

If the PGP key is RSA-based, you can convert it to PEM format. For example, Ubuntu
provides a conversion tool here: [https://manpages.ubuntu.com/manpages/jammy/en/man1/openpgp2ssh.1.html](https://manpages.ubuntu.com/manpages/jammy/en/man1/openpgp2ssh.1.html "https://manpages.ubuntu.com/manpages/jammy/en/man1/openpgp2ssh.1.html")

### Troubleshoot failed to add SSH public key

Description

When you try to add a public key for a service-managed user, you receive the
following error:

```
Failed to add SSH public key (Unsupported or invalid SSH public key format)
```

Cause

You might be attempting to import an SSH2-formatted public key, and AWS Transfer Family does
not support SSH2-formatted public keys for service-managed users.

Solution

You need to convert the key into OpenSSH format. This process is described in
[Converting an SSH2 key to SSH public key
format](convert-ssh2-public-key.md "convert-ssh2-public-key.md").
