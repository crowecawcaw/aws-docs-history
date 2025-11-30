# Security policies for AWS Transfer Family SFTP

connectors

SFTP connector security policies in AWS Transfer Family allow you to limit the set of cryptographic
algorithms (message authentication codes (MACs), key exchanges (KEXs), and cipher suites)
associated with your SFTP connector. The following is a list of supported cryptographic
algorithms for each SFTP connector security policy.

###### Note

`TransferSFTPConnectorSecurityPolicy-2024-03` is the default
security policy that is applied to SFTP connectors.

You can change the security policy for your connector. Select
**Connectors** from the Transfer Family left navigation pane, and select your
connector. Then select **Edit** in the **Sftp
configuration** section. In the **Cryptographic algorithm
options** section, choose any available security policy from the dropdown list
in the **Security Policy** field.

## Cryptographic algorithms

For host keys, SFTP connectors support all the algorithms that are supported for Transfer Family
servers, except for ed25519:

- `rsa-sha2-256`
- `rsa-sha2-512`
- `ecdsa-sha2-nistp256`
- `ecdsa-sha2-nistp384`
- `ecdsa-sha2-nistp521`

Additionally, for host keys, we support `ssh-rsa`, but only for
`TransferSFTPConnectorSecurityPolicy-2023-07`.

For authentication, SFTP connectors support the following key types:

- `ssh-rsa`
- `ecdsa`

## SFTP connector security policy

details

The following table shows the specific cryptographic algorithms supported by each SFTP
connector security policy.

| Security policy                      | TransferSFTPConnectorSecurityPolicy-FIPS-2024-10 | TransferSFTPConnectorSecurityPolicy-2024-03 | TransferSFTPConnectorSecurityPolicy-2023-07 |
| ------------------------------------ | ------------------------------------------------ | ------------------------------------------- | ------------------------------------------- |
| **Ciphers**                          |
| aes128-ctr                           |                                                  |                                             | ♦                                           |
| aes128-gcm@openssh.com               | ♦                                                | ♦                                           | ♦                                           |
| aes192-ctr                           |                                                  | ♦                                           | ♦                                           |
| aes256-ctr                           |                                                  | ♦                                           | ♦                                           |
| aes256-gcm@openssh.com               | ♦                                                | ♦                                           | ♦                                           |
| **Kexs**                             |
| curve25519-sha256                    |                                                  | ♦                                           | ♦                                           |
| curve25519-sha256@libssh.org         |                                                  | ♦                                           | ♦                                           |
| diffie-hellman-group14-sha1          |                                                  |                                             | ♦                                           |
| diffie-hellman-group16-sha512        |                                                  | ♦                                           | ♦                                           |
| diffie-hellman-group18-sha512        |                                                  | ♦                                           | ♦                                           |
| diffie-hellman-group-exchange-sha256 |                                                  | ♦                                           | ♦                                           |
| ecdh-sha2-nistp256                   | ♦                                                |                                             |                                             |
| ecdh-sha2-nistp384                   | ♦                                                |                                             |                                             |
| ecdh-sha2-nistp521                   | ♦                                                |                                             |                                             |
| **Macs**                             |
| hmac-sha2-512-etm@openssh.com        |                                                  | ♦                                           | ♦                                           |
| hmac-sha2-256-etm@openssh.com        |                                                  | ♦                                           | ♦                                           |
| hmac-sha2-512                        | ♦                                                | ♦                                           | ♦                                           |
| hmac-sha2-256                        | ♦                                                | ♦                                           | ♦                                           |
| hmac-sha1                            |                                                  |                                             | ♦                                           |
| hmac-sha1-96                         |                                                  |                                             | ♦                                           |
| **Host Key<br>Algorithms**           |
| rsa-sha2-256                         | ♦                                                | ♦                                           | ♦                                           |
| rsa-sha2-512                         | ♦                                                | ♦                                           | ♦                                           |
| ecdsa-sha2-nistp256                  | ♦                                                | ♦                                           | ♦                                           |
| ecdsa-sha2-nistp384                  |                                                  | ♦                                           | ♦                                           |
| ecdsa-sha2-nistp521                  |                                                  | ♦                                           | ♦                                           |
| ssh-rsa                              |                                                  |                                             | ♦                                           |
