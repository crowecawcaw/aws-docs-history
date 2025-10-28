# Step 5: Create a shared secret key

To encrypt the data tables, the collaboration participants must agree upon and securely
share a shared secret key.

The shared secret key must be at least 256-bits (32 bytes). You can specify a larger key,
but it won't give you any additional security.

###### Important

Remember, the key and collaboration ID used for encryption and decryption must be
identical for all collaboration participants.

The following sections provide examples of console commands for generating a shared secret
key saved as `secret.key` in the respective terminal's current working
directory.

###### Topics

- [Example: Key generation using
  OpenSSL](#generate-key-OpenSSL "#generate-key-OpenSSL")
- [Example: Key generation on Windows
  using PowerShell](#generate-key-powershell "#generate-key-powershell")

## Example: Key generation using

OpenSSL

For a common general purpose cryptography library, run the following command to create a
shared secret key.

`openssl rand 32 > secret.key`

If you're using Windows and don't have OpenSSL installed,
you can generate keys using the example described in [Example: Key generation on Windows using
PowerShell](#generate-key-powershell "#generate-key-powershell").

## Example: Key generation on Windows

using PowerShell

For PowerShell, a terminal application available on
Windows, run the following command to create a shared secret key.

`$bs = New-Object Byte[](32);
 [Security.Cryptography.RandomNumberGenerator]::Create().GetBytes($bs); Set-Content
 'secret.key' -Encoding Byte -Value $bs`
