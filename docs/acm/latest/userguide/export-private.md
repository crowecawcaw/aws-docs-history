# Export an AWS Certificate Manager private certificate

You can export a certificate issued by AWS Private CA for use anywhere in your private
PKI environment. The exported file contains the certificate, the certificate chain,
and the encrypted private key. This file must be stored securely. For more
information about AWS Private CA, see [AWS Private Certificate Authority User Guide](../../../privateca/latest/userguide.md "../../../privateca/latest/userguide.md").

###### Note

If you want to export public certificates issued through ACM, see [ACM exportable public certificates](acm-exportable-certificates.md "acm-exportable-certificates.md").

###### Topics

- [Export a private certificate (console)](#export-console "#export-console")
- [Export a private certificate (CLI)](#export-cli "#export-cli")

## Export a private certificate (console)

1. Sign into the AWS Management Console and open the ACM console at
   [https://console.aws.amazon.com/acm/home](https://console.aws.amazon.com/acm/home "https://console.aws.amazon.com/acm/home").
2. Choose **Certificate Manager**
3. Choose the link of the certificate that you want to export.
4. Choose **Export**.
5. Enter and confirm a passphrase for the private key.

###### Note

When creating your passphrase, you can use any ASCII character
except #, $, or %. 6. Choose **Generate PEM Encoding**. 7. You can copy the certificate, certificate chain, and encrypted key to
memory or choose **Export to a file** for each. 8. Choose **Done**.

## Export a private certificate (CLI)

Use the [export-certificate](../../../cli/latest/reference/acm/export-certificate.md "../../../cli/latest/reference/acm/export-certificate.md") command to export a private certificate and
private key. You must assign a passphrase when you run the command. For added
security, use a file editor to store your passphrase in a file, and then supply
the passphrase by supplying the file. This prevents your passphrase from being
stored in the command history and prevents others from seeing the passphrase as
you type it in.

###### Note

The file containing the passphrase must not end in a line terminator. You
can check your password file like this:

```
`$` `file -k passphrase.txt`
passphrase.txt: ASCII text, with no line terminators
```

The following examples pipe the command output to `jq` to apply PEM
formatting.

```
[Windows/Linux]
`$` `aws acm export-certificate \
 --certificate-arn arn:aws:acm:`Region`:`444455556666`:certificate/`certificate_ID` \
 --passphrase fileb://`path-to-passphrase-file` \
 | jq -r '"\(.Certificate)\(.CertificateChain)\(.PrivateKey)"'`
```

This outputs a base64-encoded, PEM-format certificate, also containing the
certificate chain and encrypted private key, as in the following abbreviated
example.

```
-----BEGIN CERTIFICATE-----
MIIDTDCCAjSgAwIBAgIRANWuFpqA16g3IwStE3vVpTwwDQYJKoZIhvcNAQELBQAw
EzERMA8GA1UECgwIdHJvbG9sb2wwHhcNMTkwNzE5MTYxNTU1WhcNMjAwODE5MTcx
NTU1WjAXMRUwEwYDVQQDDAx3d3cuc3B1ZHMuaW8wggEiMA0GCSqGSIb3DQEBAQUA
...
8UNFQvNoo1VtICL4cwWOdLOkxpwkkKWtcEkQuHE1v5Vn6HpbfFmxkdPEasoDhthH
FFWIf4/+VOlbDLgjU4HgtmV4IJDtqM9rGOZ42eFYmmc3eQO0GmigBBwwXp3j6hoi
74YM+igvtILnbYkPYhY9qz8h7lHUmannS8j6YxmtpPY=
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIIC8zCCAdugAwIBAgIRAM/jQ/6h2/MI1NYWX3dDaZswDQYJKoZIhvcNAQELBQAw
EzERMA8GA1UECgwIdHJvbG9sb2wwHhcNMTkwNjE5MTk0NTE2WhcNMjkwNjE5MjA0
NTE2WjATMREwDwYDVQQKDAh0cm9sb2xvbDCCASIwDQYJKoZIhvcNAQEBBQADggEP
...
j2PAOviqIXjwr08Zo/rTy/8m6LAsmm3LVVYKLyPdl+KB6M/+H93Z1/Bs8ERqqga/
6lfM6iw2JHtkW+q4WexvQSoqRXFhCZWbWPZTUpBS0d4/Y5q92S3iJLRa/JQ0d4U1
tWZyqJ2rj2RL+h7CE71XIAM//oHGcDDPaQBFD2DTisB/+ppGeDuB
-----END CERTIFICATE-----
-----BEGIN ENCRYPTED PRIVATE KEY-----
MIIFKzBVBgkqhkiG9w0BBQ0wSDAnBgkqhkiG9w0BBQwwGgQUMrZb7kZJ8nTZg7aB
1zmaQh4vwloCAggAMB0GCWCGSAFlAwQBKgQQDViroIHStQgNOjR6nTUnuwSCBNAN
JM4SG202YPUiddWeWmX/RKGg3lIdE+A0WLTPskNCdCAHqdhOSqBwt65qUTZe3gBt
...
ZGipF/DobHDMkpwiaRR5sz6nG4wcki0ryYjAQrdGsR6EVvUUXADkrnrrxuHTWjFl
wEuqyd8X/ApkQsYFX/nhepOEIGWf8Xu0nrjQo77/evhG0sHXborGzgCJwKuimPVy
Fs5kw5mvEoe5DAe3rSKsSUJ1tM4RagJj2WH+BC04SZWNH8kxfOC1E/GSLBCixv3v
+Lwq38CEJRQJLdpta8NcLKnFBwmmVs9OV/VXzNuHYg==
-----END ENCRYPTED PRIVATE KEY-----
```

To output everything to a file, append the `>` redirect to the
previous example, yielding the following.

```
`$` `aws acm export-certificate \
 --certificate-arn arn:aws:acm:`Region`:`444455556666`:certificate/`certificate_ID` \
 --passphrase fileb://`path-to-passphrase-file` \
 | jq -r '"\(.Certificate)\(.CertificateChain)\(.PrivateKey)"' \
 > `/tmp/export.txt``
```
