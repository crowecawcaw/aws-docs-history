# Using multiple authentication methods

The Transfer Family server controls the AND logic when you use multiple authentication methods.
Transfer Family treats this as two separate requests to your custom identity provider: however,
their effect is combined.

Both requests must return successfully with the correct response to allow the
authentication to complete. Transfer Family requires the two responses to be complete, meaning they
contain all of the required elements (role, home directory, policy and the POSIX profile
if you're using Amazon EFS for storage). Transfer Family also requires that the password response must
not include public keys.

The public key request must have a separate response from the identity provider. That
behavior is unchanged when using **Password OR Key** or
**Password AND Key**.

The SSH/SFTP protocol challenges the software client first with a public key
authentication, then requests a password authentication. This operation mandates both
are successful before the user is allowed to complete the authentication.

For custom identity provider options, you can specify any of the following options for
how to authenticate.

- **Password OR Key** – users can authenticate with
  either their password or their key. This is the default value.
- **Password ONLY** – users must provide their password
  to connect.
- **Key ONLY** – users must provide their private key to
  connect.
- **Password AND Key** – users must provide both their
  private key and their password to connect. The server checks the key first, and
  then if the key is valid, the system prompts for a password. If the private key
  provided does not match the public key that is stored, authentication
  fails.
