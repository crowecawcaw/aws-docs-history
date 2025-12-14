# Add an additional server host key

On the AWS Transfer Family console, you can add additional server host keys. Adding additional
host keys of differing formats can be useful for identifying a server when clients
connect to it, as well as improving your security profile. For example, if your original
key is an RSA key, you could add an additional ECDSA key.

###### Note

The SFTP client will connect using the oldest key in the configuration that
matches the key's algorithm. The oldest key for each key type (RSA, ECDSA, or
ED25519) is the active key for the server for that type.

###### Security note when a Transfer Family server has multiple types of host keys

If a server has multiple types of host keys, the SFTP client can assign a
preference by type. So, when there exist RSA, ECDSA, and ED25519 host keys for the
server, the choice is driven by the preference by type.

Modern SFTP clients prefer ECDSA and ED25519 host keys when they exist. This becomes
important if you want to add an ECDSA or ED25519 key when the server previously only had
RSA keys. The addition of the new ECDSA or ED25519 key would potentially manifest as a
security warning for a client.

To the client, the key will appear as having changed, when in fact it was not changed:
the new key was added in addition to the existing RSA key. Keep this in mind if you
decide to add new types of server host keys.

###### To add an additional server host key

1. Open the AWS Transfer Family console at [https://console.aws.amazon.com/transfer/](https://console.aws.amazon.com/transfer/ "https://console.aws.amazon.com/transfer/").
2. In the left navigation pane, choose
   **Servers**, and then choose a server that
   uses the SFTP protocol.
3. On the server details page, scroll down to the **Server host
   keys** section.

![The Server host keys console section.](/images/transfer/latest/userguide/images/server-host-keys.png) 4. Choose **Add host key**.

The **Add server host key** page displays. 5. In the **Server Host Key** section, enter an RSA, ECDSA, or
ED25519 private key that is used to identify your server when clients connect to
it over the SFTP-enabled server.

###### Note

When you create a server host key, make sure to specify `-N ""`
(no passphrase). See [Creating SSH keys on macOS, Linux, or
Unix](macOS-linux-unix-ssh.md "macOS-linux-unix-ssh.md") for details on how to generate
key pairs. 6. (Optional) Add a description to differentiate among multiple server host keys.
You can also add tags for your key. 7. Choose **Add key**. You are returned to the **Server
details** page.
To add a host key by using the AWS Command Line Interface (AWS CLI), use the [ImportHostKey](../APIReference/API_ImportHostKey.md "../APIReference/API_ImportHostKey.md") API
operation and provide the new host key. If you create a new SFTP-enabled server, you
provide your host key as a parameter in the [CreateServer](../APIReference/API_CreateServer.md "../APIReference/API_CreateServer.md") API
operation. You can also use the AWS CLI to update the description for an existing host
key.

The following example `import-host-key` AWS CLI command imports a host key
for the specified SFTP-enabled server.

```
aws transfer import-host-key --description `key-description` --server-id `your-server-id` --host-key-body `file://my-host-key`
```
