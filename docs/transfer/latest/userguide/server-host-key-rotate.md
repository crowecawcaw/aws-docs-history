# Rotate the server host keys

Periodically, you can rotate your server host key. This topic describes how the server
chooses which key to apply, and the procedure for rotating these keys.

## How the client chooses a server host

key

The way that Transfer Family chooses which server key to apply depends on conditions for the
SFTP client, as explained here. The assumption is that there is one older key and
one newer key.

- An SFTP client has no prior public host key for the server. The first time
  the client connects to the server, either of the following occurs:
  - The client fails the connection, if it is configured to do
    so.
  - Or, the client chooses the first key that matches the possible
    available algorithms and asks the user if that key can be trusted.
    If so, the client auto-updates the `known_hosts` file (or
    whatever local configuration file or resource the client uses to
    record trust decisions) and enters that key.

- An SFTP client has an older key in its `known_hosts` file. The
  client prefers to use this key, even if a newer key exists, either for this
  key's algorithm or another algorithm. This is because the client has a
  higher level of trust for the key that is in its `known_hosts`
  file.
- An SFTP client has the new key (in any of the available algorithms) in its
  `known_hosts` keys file. The client ignores older keys
  because they are not trusted and uses the new key.
- An SFTP client has both keys in its `known_hosts` file. The
  client chooses the first key by index that matches the list of available
  keys offered by the server.

Transfer Family prefers that the SFTP client has all of the keys in its
`known_hosts` file, since this allows the most flexibility when
connecting to a Transfer Family server. Key rotation is based on the fact that multiple entries
can exist in the `known_hosts` file for the same Transfer Family server.

## Rotate the server host key procedure

As an example, assume that you have added the following set of server host keys to
your Transfer Family server.

| Server host keys | Host key type    | Date added to the server |
| ---------------- | ---------------- | ------------------------ |
| RSA              | April 1, 2020    |
| ECDSA            | February 1, 2020 |
| ED25519          | December 1, 2019 |
| RSA              | October 1, 2019  |
| ECDSA            | June 1, 2019     |
| ED25519          | March 1, 2019    |

###### To rotate the server host key

1. Add a new server host key. This procedure is described in [Add an additional server host key](server-host-key-add.md "server-host-key-add.md").
2. Delete one or more of the host keys of the same type that you had added
   previously. This procedure is described in [Delete a server host key](server-host-key-delete.md "server-host-key-delete.md").
3. All keys are visible, and can be active, subject to the behavior described
   previously in [How the client chooses a server host
   key](#server-key-behavior "#server-key-behavior").
