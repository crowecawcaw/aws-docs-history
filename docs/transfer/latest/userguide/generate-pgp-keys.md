# Generate PGP keys

You can use Pretty Good Privacy (PGP) decryption with the files that Transfer Family processes
with workflows. To use decryption in a workflow step, provide a PGP key. For detailed
information about PGP key algorithms, including recommendations and FIPS compliance, see
[PGP key pair algorithms](key-management.md#pgp-key-algorithms "key-management.md#pgp-key-algorithms").

The AWS storage blog has a post that describes how to simply decrypt files without writing any code using Transfer Family Managed workflows,
[Encrypt and decrypt files with PGP and AWS Transfer Family](https://aws.amazon.com/blogs/storage/encrypt-and-decrypt-files-with-pgp-and-aws-transfer-family/ "https://aws.amazon.com/blogs/storage/encrypt-and-decrypt-files-with-pgp-and-aws-transfer-family/").

The operator that you use to generate your PGP keys depends on your operating system
and the version of the key-generation software that you're using.

If you're using Linux or Unix, use your package installer to install `gpg`.
Depending on your Linux distribution, one of the following commands should work for
you.

```
sudo yum install gnupg
```

```
sudo apt-get install gnupg
```

For Windows or macOS, you can download what you need from [https://gnupg.org/download/](https://gnupg.org/download/ "https://gnupg.org/download/").

After you install your PGP key generator software, you run the `gpg
 --full-gen-key` or `gpg --gen-key` command to generate a key
pair.

###### Note

If you're using `GnuPG` version 2.3.0 or newer, you
must run `gpg --full-gen-key`. When prompted for the type of key
to create, choose RSA or ECC. However, if you choose ECC, make sure to choose either
NIST or BrainPool for the elliptic curve.
**Do not** choose Curve 25519.

Useful `gpg` subcommands

The following are some useful subcommands for `gpg`:

- `gpg --help` – This command lists the available options and
  might include some examples.
- `gpg --list-keys` – This command lists the details for all
  the key pairs that you have created.
- `gpg --fingerprint` – This command lists the details for all
  your key pairs, including each key's fingerprint.
- `gpg --export -a `user-name`–
This command exports the public key portion of the key for the`user-name`` that was used when the
  key was generated.
