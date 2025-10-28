# Manage host keys for your SFTP-enabled

server

Server host keys are private keys used by the Transfer Family server to provide a unique identity to
the caller, and to guarantee that it is the correct server. That guarantee is enforced by
the presence of the correct public key in the caller's `known_hosts` file. (The
`known_hosts` file is a standard feature used by most SSH clients to store
the public keys for the servers that you've connected to.) You can retrieve the public key
that corresponds to your server host key by running `ssh-keyscan` for your
server.

###### Important

Accidentally changing a server's host key can be disruptive. Depending on how
your SFTP client is configured, it can fail immediately, with the message that no
trusted host key exists, or present threatening prompts. If there are scripts for
automating connections, they most likely would fail as well.

By default, AWS Transfer Family generates host keys for your SFTP-enabled server. You can import
server host keys to preserve host identity and avoid updating client trust stores. [When to import host keys](#host-key-import-use-cases "#host-key-import-use-cases") lists a
few reasons you might want to do this. If you do not provide host keys, new ones will be
generated for you.

AWS Transfer Family supports multiple host keys of different types (RSA, ECDSA, and ED25519) to
provide compatibility with a broader range of client host signature algorithms. Different
key types enable specific algorithms: RSA keys enable **rsa-\*** algorithms,
ECDSA keys enable **ecdsa-\*** algorithms, and ED25519 keys enable
**ed25519** algorithms. Plan your key types at server creation time, as
introducing additional key types after clients have started interacting with the server can
be disruptive for some clients and may be as problematic as replacing existing host
keys.

To prevent your users from being prompted to verify the authenticity of your SFTP-enabled
server again, import the host key for your on-premises server to the SFTP-enabled server.
Doing this also prevents your users from getting a warning about a potential
man-in-the-middle attack.

You can also rotate host keys periodically, as an additional security measure. For
details, see [Rotate the server host keys](server-host-key-rotate.md "server-host-key-rotate.md").

###### Note

Server host keys are used by servers that support the SFTP protocol.

## When to import host keys

While AWS Transfer Family can generate host keys automatically, there are several scenarios where
importing your own host keys provides operational benefits:

- _Server migration_ - You're migrating from an existing
  server to AWS Transfer Family and want to avoid updating client trust stores
  (`known_hosts` files) for existing clients.
- _Disaster recovery and failover_ - You have multiple
  AWS Transfer Family servers (for example, one in US East (Ohio) and one in
  US West (Oregon)) that share the same public DNS name. Using the same host
  keys on both servers ensures seamless failover without client authentication
  failures.
- _Operational continuity_ - You want the host key material
  available for use with other servers (AWS Transfer Family or otherwise) in the future to
  maintain consistent server identity across your infrastructure.
- _Algorithm control_ - You want greater client compatibility
  by providing more Host Key Algorithms, or you want to control which algorithms
  clients can use by only offering keys compatible with specific
  algorithms.

The following topics provide detailed procedures for managing server host keys:

- [Add an additional server host key](server-host-key-add.md "server-host-key-add.md") - Add
  additional host keys to your server
- [Delete a server host key](server-host-key-delete.md "server-host-key-delete.md") -
  Remove host keys from your server
- [Rotate the server host keys](server-host-key-rotate.md "server-host-key-rotate.md") -
  Rotate host keys for enhanced security
- [Additional server host key information](server-host-key-other.md "server-host-key-other.md") -
  View and manage host key details
