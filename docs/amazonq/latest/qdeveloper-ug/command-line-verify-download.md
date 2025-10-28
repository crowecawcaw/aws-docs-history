# To verify the download (optional)

If you chose to manually download the Amazon Q command line installer package .zip, you can verify the signatures using the GnuPG tool:

1. Download and install the gpg command using your package manager. For more information, see the [GnuPG documentation](https://gnupg.org/documentation/index.html "https://gnupg.org/documentation/index.html").
2. Create a public key file by creating a text file, and then paste in the following text:

```
-----BEGIN PGP PUBLIC KEY BLOCK-----

mDMEZig60RYJKwYBBAHaRw8BAQdAy/+G05U5/EOA72WlcD4WkYn5SInri8pc4Z6D
BKNNGOm0JEFtYXpvbiBRIENMSSBUZWFtIDxxLWNsaUBhbWF6b24uY29tPoiZBBMW
CgBBFiEEmvYEF+gnQskUPgPsUNx6jcJMVmcFAmYoOtECGwMFCQPCZwAFCwkIBwIC
IgIGFQoJCAsCBBYCAwECHgcCF4AACgkQUNx6jcJMVmef5QD/QWWEGG/cOnbDnp68
SJXuFkwiNwlH2rPw9ZRIQMnfAS0A/0V6ZsGB4kOylBfc7CNfzRFGtovdBBgHqA6P
zQ/PNscGuDgEZig60RIKKwYBBAGXVQEFAQEHQC4qleONMBCq3+wJwbZSr0vbuRba
D1xr4wUPn4Avn4AnAwEIB4h+BBgWCgAmFiEEmvYEF+gnQskUPgPsUNx6jcJMVmcF
AmYoOtECGwwFCQPCZwAACgkQUNx6jcJMVmchMgEA6l3RveCM0YHAGQaSFMkguoAo
vK6FgOkDawgP0NPIP2oA/jIAO4gsAntuQgMOsPunEdDeji2t+AhV02+DQIsXZpoB
=f8yY
-----END PGP PUBLIC KEY BLOCK-----
```

3. Import the Amazon Q command line public key with the following command, substituting `public-key-file-name` with the file name of the public key you created:

```
gpg --import public-key-file-name
```

```
gpg: directory '/home/username/.gnupg' created
gpg: keybox '/home/username/.gnupg/pubring.kbx' created
gpg: /home/username/.gnupg/trustdb.gpg: trustdb created
gpg: key 50DC7A8DC24C5667: public key "Amazon Q command line Team <q-command line@amazon.com>" imported
gpg: Total number processed: 1
gpg:               imported: 1
```

4. Download the Amazon Q command line signature file for the package you downloaded. It has the same path and name as the .zip file it corresponds to, but has the extension .sig.

Standard version (glibc 2.34+):

Linux x86-64:

```
curl --proto '=https' --tlsv1.2 -sSf "https://desktop-release.q.us-east-1.amazonaws.com/latest/q-x86_64-linux.zip.sig" -o "q.zip.sig"
```

Linux ARM (aarch64):

```
curl --proto '=https' --tlsv1.2 -sSf "https://desktop-release.q.us-east-1.amazonaws.com/latest/q-aarch64-linux.zip.sig" -o "q.zip.sig"
```

Musl version (for glibc < 2.34):

Linux x86-64 with musl:

```
curl --proto '=https' --tlsv1.2 -sSf "https://desktop-release.q.us-east-1.amazonaws.com/latest/q-x86_64-linux-musl.zip.sig" -o "q.zip.sig"
```

Linux ARM (aarch64) with musl:

```
curl --proto '=https' --tlsv1.2 -sSf "https://desktop-release.q.us-east-1.amazonaws.com/latest/q-aarch64-linux-musl.zip.sig" -o "q.zip.sig"
```

5. Verify the signature, passing both the downloaded .sig and .zip file names as parameters to the gpg command:

```
gpg --verify q.zip.sig q.zip
```

The output should look similar to the following:

```
gpg: Signature made Wed 24 Apr 2024 12:08:49 AM UTC
gpg:                using EDDSA key 9AF60417E82742C9143E03EC50DC7A8DC24C566
gpg: Good signature from "Amazon Q command line Team <q-command line@amazon.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 9AF6 0417 E827 42C9 143E  03EC 50DC 7A8D C24C 5667
```

###### Note

The warning in the output is expected and doesn't indicate a problem. It occurs because there isn't a chain of trust between your personal PGP key (if you have one) and the Amazon Q for command line PGP key. For more information, see Web of trust.
