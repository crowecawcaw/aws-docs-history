AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Verify the signature

of the Session Manager plugin

The Session Manager plugin RPM and Debian installer packages for Linux instances are
cryptographically signed. You can use a public key to verify that the plugin
binary and package is original and unmodified. If the file is altered or
damaged, the verification fails. You can verify the signature of the
installer package using the GNU Privacy Guard (GPG) tool. The following
information is for Session Manager plugin versions 1.2.707.0 or later.

Complete the following steps to verify the signature of the Session Manager plugin
installer package.

###### Topics

- [Step 1:
  Download the Session Manager plugin installer package](#install-plugin-linux-verify-signature-installer-packages "#install-plugin-linux-verify-signature-installer-packages")
- [Step 2:
  Download the associated signature file](#install-plugin-linux-verify-signature-packages "#install-plugin-linux-verify-signature-packages")
- [Step 3:
  Install the GPG tool](#install-plugin-linux-verify-signature-packages-gpg "#install-plugin-linux-verify-signature-packages-gpg")
- [Step 4:
  Verify the Session Manager plugin installer package on a Linux server](#install-plugin-linux-verify-signature-packages "#install-plugin-linux-verify-signature-packages")

## Step 1:

Download the Session Manager plugin installer package

Download the Session Manager plugin installer package you want to verify.

**Amazon Linux 2, AL2023, and RHEL RPM
packages**

x86_64

```
curl -o "session-manager-plugin.rpm" "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/linux_64bit/session-manager-plugin.rpm"
```

ARM64

```
curl -o "session-manager-plugin.rpm" "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/linux_arm64/session-manager-plugin.rpm"
```

**Debian Server and Ubuntu Server Deb
packages**

x86_64

```
curl -o "session-manager-plugin.deb" "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/ubuntu_64bit/session-manager-plugin.deb"
```

ARM64

```
curl -o "session-manager-plugin.deb" "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/ubuntu_arm64/session-manager-plugin.deb"
```

## Step 2:

Download the associated signature file

After you download the installer package, download the associated
signature file for package verification. To provide an extra layer of
protection against unauthorized copying or use of the
session-manager-plugin binary file inside the package, we also offer
binary signatures, which you can use to validate individual binary
files. You can choose to use these binary signatures based on your
security needs.

**Amazon Linux 2, AL2023, and RHEL signature
packages**

x86_64
Package:

```
curl -o "session-manager-plugin.rpm.sig" "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/linux_64bit/session-manager-plugin.rpm.sig"
```

Binary:

```
curl -o "session-manager-plugin.sig" "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/linux_64bit/session-manager-plugin.sig"
```

ARM64
Package:

```
curl -o "session-manager-plugin.rpm.sig" "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/linux_arm64/session-manager-plugin.rpm.sig"
```

Binary:

```
curl -o "session-manager-plugin.sig" "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/linux_arm64/session-manager-plugin.sig"
```

**Debian Server and Ubuntu Server Deb signature
packages**

x86_64
Package:

```
curl -o "session-manager-plugin.deb.sig" "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/ubuntu_64bit/session-manager-plugin.deb.sig"
```

Binary:

```
curl -o "session-manager-plugin.sig" "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/ubuntu_64bit/session-manager-plugin.sig"
```

ARM64
Package:

```
curl -o "session-manager-plugin.deb.sig" "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/ubuntu_arm64/session-manager-plugin.deb.sig"
```

Binary:

```
curl -o "session-manager-plugin.sig" "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/ubuntu_arm64/session-manager-plugin.sig"
```

## Step 3:

Install the GPG tool

To verify the signature of the Session Manager plugin, you must have the GNU Privacy
Guard (GPG) tool installed on your system. The verification process
requires GPG version 2.1 or later. You can check your GPG version by
running the following command:

```
gpg --version
```

If your GPG version is older than 2.1, update it before proceeding
with the verification process. For most systems, you can update the GPG
tool using your package manager. For example, on supported Amazon Linux and
RHEL versions, you can use the following commands:

```
sudo yum update
sudo yum install gnupg2
```

On supported Ubuntu Server and Debian Server systems, you can use the
following commands:

```
sudo apt-get update
sudo apt-get install gnupg2
```

Ensure you have the required GPG version before continuing with the
verification process.

## Step 4:

Verify the Session Manager plugin installer package on a Linux server

Use the following procedure to verify the Session Manager plugin installer package
on a Linux server.

###### Note

Amazon Linux 2 doesn't support the gpg tool version 2.1 or higher. If the
following procedure doesn't work on your Amazon Linux 2 instances, verify the
signature on a different platform before installing it on your Amazon Linux 2
instances.

1. Copy the following public key, and save it to a file named
   session-manager-plugin.gpg.

```
-----BEGIN PGP PUBLIC KEY BLOCK-----

mFIEZ5ERQxMIKoZIzj0DAQcCAwQjuZy+IjFoYg57sLTGhF3aZLBaGpzB+gY6j7Ix
P7NqbpXyjVj8a+dy79gSd64OEaMxUb7vw/jug+CfRXwVGRMNtIBBV1MgU1NNIFNl
c3Npb24gTWFuYWdlciA8c2Vzc2lvbi1tYW5hZ2VyLXBsdWdpbi1zaWduZXJAYW1h
em9uLmNvbT4gKEFXUyBTeXN0ZW1zIE1hbmFnZXIgU2Vzc2lvbiBNYW5hZ2VyIFBs
dWdpbiBMaW51eCBTaWduZXIgS2V5KYkBAAQQEwgAqAUCZ5ERQ4EcQVdTIFNTTSBT
ZXNzaW9uIE1hbmFnZXIgPHNlc3Npb24tbWFuYWdlci1wbHVnaW4tc2lnbmVyQGFt
YXpvbi5jb20+IChBV1MgU3lzdGVtcyBNYW5hZ2VyIFNlc3Npb24gTWFuYWdlciBQ
bHVnaW4gTGludXggU2lnbmVyIEtleSkWIQR5WWNxJM4JOtUB1HosTUr/b2dX7gIe
AwIbAwIVCAAKCRAsTUr/b2dX7rO1AQCa1kig3lQ78W/QHGU76uHx3XAyv0tfpE9U
oQBCIwFLSgEA3PDHt3lZ+s6m9JLGJsy+Cp5ZFzpiF6RgluR/2gA861M=
=2DQm
-----END PGP PUBLIC KEY BLOCK-----
```

2. Import the public key into your keyring. The returned key
   value should be `2C4D4AFF6F6757EE`.

```
$ gpg --import session-manager-plugin.gpg
gpg: key 2C4D4AFF6F6757EE: public key "AWS SSM Session Manager <session-manager-plugin-signer@amazon.com> (AWS Systems Manager Session Manager Plugin Linux Signer Key)" imported
gpg: Total number processed: 1
gpg:               imported: 1
```

3. Run the following command to verify the fingerprint.

```
gpg --fingerprint 2C4D4AFF6F6757EE
```

The fingerprint for the command output should match the
following.

```
7959 6371 24CE 093A D501 D47A 2C4D 4AFF 6F67 57EE
```

```
pub   nistp256 2025-01-22 [SC]
      7959 6371 24CE 093A D501  D47A 2C4D 4AFF 6F67 57EE
uid           [ unknown] AWS SSM Session Manager <session-manager-plugin-signer@amazon.com> (AWS Systems Manager Session Manager Plugin Linux Signer Key)
```

If the fingerprint doesn't match, don't install the plugin.
Contact AWS Support. 4. Verify the installer package signature. Replace the
`signature-filename` and
`downloaded-plugin-filename` with
the values you specified when downloading the signature file and
session-manager-plugin, as listed in the table earlier in this
topic.

```
gpg --verify `signature-filename` `downloaded-plugin-filename`
```

For example, for the x86_64 architecture on Amazon Linux 2, the command
is as follows:

```
gpg --verify session-manager-plugin.rpm.sig session-manager-plugin.rpm
```

This command returns output similar to the following.

```
gpg: Signature made Mon Feb 3 20:08:32 2025 UTC gpg: using ECDSA key 2C4D4AFF6F6757EE
gpg: Good signature from "AWS Systems Manager Session Manager <session-manager-plugin-signer@amazon.com> (AWS Systems Manager Session Manager Plugin Linux Signer Key)" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg: There is no indication that the signature belongs to the owner.
Primary key fingerprint: 7959 6371 24CE 093A D501 D47A 2C4D 4AFF 6F67 57EE
```

If the output includes the phrase `BAD signature`, check
whether you performed the procedure correctly. If you continue to get
this response, contact AWS Support and don't install the package. The
warning message about the trust doesn't mean that the signature isn't
valid, only that you haven't verified the public key. A key is trusted
only if you or someone who you trust has signed it. If the output
includes the phrase `Can't check signature: No public key`,
verify you downloaded Session Manager plugin with version 1.2.707.0 or later.
