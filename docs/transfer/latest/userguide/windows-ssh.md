# Creating SSH keys on Microsoft Windows

Windows includes OpenSSH as a built-in feature, which you can use to generate SSH
keys in the same format as on Linux or macOS. Alternatively, you can use third-party
tools like PuTTY's key generator (PuTTYgen).

## Using Windows built-in OpenSSH

Recent versions of Windows include OpenSSH by default. You can use the same
`ssh-keygen` commands as described in the macOS/Linux
section:

1. Open Windows PowerShell or Command Prompt.
2. Run one of the following commands based on the type of key you want to
   generate:
   - To generate an RSA 4096-bit key pair:

   ```
   ssh-keygen -t rsa -b 4096 -f `key_name`
   ```

   - To generate an ECDSA 521-bit key-pair:

   ```
   ssh-keygen -t ecdsa -b 521 -f `key_name`
   ```

   - To generate an ED25519 key pair:

   ```
   ssh-keygen -t ed25519 -f `key_name`
   ```

3. Follow the same steps as in the macOS/Linux section to upload your
   public key to AWS Transfer Family.

## Using PuTTYgen (third-party tool)

Some third-party SSH clients for Windows, such as PuTTY, use different key
formats. PuTTY uses the `PPK` format for private keys. If you're
using PuTTY or related tools like WinSCP, you can use PuTTYgen to create keys in
this format.

###### Note

If you present WinSCP with a private key file not in
`.ppk` format, that client offers to convert the key
into `.ppk` format for you.

For a tutorial about creating SSH keys by using PuTTYgen, see the [SSH.com
website](https://www.ssh.com/ssh/putty/windows/puttygen "https://www.ssh.com/ssh/putty/windows/puttygen").
