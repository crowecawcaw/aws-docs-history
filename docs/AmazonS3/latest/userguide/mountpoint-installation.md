# Installing Mountpoint

You can download and install prebuilt packages of Mountpoint for Amazon S3 by using the command line.
The instructions for downloading and installing Mountpoint vary, depending on which
Linux operating system that you're using.

###### Topics

- [Amazon Linux 2023 (AL2023)](#mountpoint-install-al2023 "#mountpoint-install-al2023")
- [Other RPM-based distributions (Amazon Linux 2, Fedora, CentOS, RHEL)](#mountpoint-install-rpm "#mountpoint-install-rpm")
- [DEB-based distributions (Debian, Ubuntu)](#mountpoint.install.deb "#mountpoint.install.deb")
- [Other Linux distributions](#mountpoint-install-other "#mountpoint-install-other")
- [Verifying the signature of the Mountpoint for Amazon S3 package](#mountpoint-install-verify "#mountpoint-install-verify")

## Amazon Linux 2023 (AL2023)

Mountpoint is available directly in the Amazon Linux 2023 repository since AL2023 version 2023.9.20251110.

1. Install it by entering the following command:

```
sudo dnf install mount-s3
```

2. Verify that Mountpoint for Amazon S3 is successfully installed:

```
mount-s3 --version
```

You should see output similar to the following:

```
mount-s3 1.21.0+1.amzn2023
```

## Other RPM-based distributions (Amazon Linux 2, Fedora, CentOS, RHEL)

1. Copy the following download URL for your architecture.

_x86_64_:

```
https://s3.amazonaws.com/mountpoint-s3-release/latest/x86_64/mount-s3.rpm
```

_ARM64 (Graviton)_:

```
https://s3.amazonaws.com/mountpoint-s3-release/latest/arm64/mount-s3.rpm
```

2. Download the Mountpoint for Amazon S3 package. Replace
   `download-link` with the appropriate download
   URL from the preceding step.

```
wget `download-link`
```

3. (Optional) Verify the authenticity and integrity of the downloaded file. First, copy
   the appropriate signature URL for your architecture.

_x86_64_:

```
https://s3.amazonaws.com/mountpoint-s3-release/latest/x86_64/mount-s3.rpm.asc
```

_ARM64 (Graviton)_:

```
https://s3.amazonaws.com/mountpoint-s3-release/latest/arm64/mount-s3.rpm.asc
```

Next, see [Verifying the signature of the
Mountpoint for Amazon S3 package](#mountpoint-install-verify "#mountpoint-install-verify"). 4. Install the package by using the following command:

```
sudo yum install ./mount-s3.rpm
```

5. Verify that Mountpoint is successfully installed by entering the following
   command:

```
mount-s3 --version
```

You should see output similar to the following:

```
mount-s3 1.21.0
```

## DEB-based distributions (Debian, Ubuntu)

1. Copy the download URL for your architecture.

_x86_64_:

```
https://s3.amazonaws.com/mountpoint-s3-release/latest/x86_64/mount-s3.deb
```

_ARM64 (Graviton)_:

```
https://s3.amazonaws.com/mountpoint-s3-release/latest/arm64/mount-s3.deb
```

2. Download the Mountpoint for Amazon S3 package. Replace
   `download-link` with the appropriate download
   URL from the preceding step.

```
wget `download-link`
```

3. (Optional) Verify the authenticity and integrity of the downloaded file. First, copy
   the signature URL for your architecture.

_x86_64_:

```
https://s3.amazonaws.com/mountpoint-s3-release/latest/x86_64/mount-s3.deb.asc
```

_ARM64 (Graviton)_:

```
https://s3.amazonaws.com/mountpoint-s3-release/latest/arm64/mount-s3.deb.asc
```

Next, see [Verifying the signature of the
Mountpoint for Amazon S3 package](#mountpoint-install-verify "#mountpoint-install-verify"). 4. Install the package by using the following command:

```
sudo apt-get install ./mount-s3.deb
```

5. Verify that Mountpoint for Amazon S3 is successfully installed by running the following
   command:

```
mount-s3 --version
```

You should see output similar to the following:

```
mount-s3 1.21.0
```

## Other Linux distributions

1. Consult your operating system documentation to install the `FUSE` and
   `libfuse2` packages, which are required.
2. Copy the download URL for your architecture.

_x86_64_:

```
https://s3.amazonaws.com/mountpoint-s3-release/latest/x86_64/mount-s3.tar.gz
```

_ARM64
(Graviton)_:

```
https://s3.amazonaws.com/mountpoint-s3-release/latest/arm64/mount-s3.tar.gz
```

3. Download the Mountpoint for Amazon S3 package. Replace
   `download-link` with the appropriate download
   URL from the preceding step.

```
wget `download-link`
```

4. (Optional) Verify the authenticity and integrity of the downloaded file. First, copy
   the signature URL for your architecture.

_x86_64_:

```
https://s3.amazonaws.com/mountpoint-s3-release/latest/x86_64/mount-s3.tar.gz.asc
```

_ARM64 (Graviton)_:

```
https://s3.amazonaws.com/mountpoint-s3-release/latest/arm64/mount-s3.tar.gz.asc
```

Next, see [Verifying the signature of the
Mountpoint for Amazon S3 package](#mountpoint-install-verify "#mountpoint-install-verify"). 5. Install the package by using the following command:

```
sudo mkdir -p /opt/aws/mountpoint-s3 && sudo tar -C /opt/aws/mountpoint-s3 -xzf ./mount-s3.tar.gz
```

6. Add the `mount-s3` binary to your `PATH` environment variable.
   In your `$HOME/.profile` file, append the following line:

```
export PATH=$PATH:/opt/aws/mountpoint-s3/bin
```

Save the `.profile` file, and run the following command:

```
source $HOME/.profile
```

7. Verify that Mountpoint for Amazon S3 is successfully installed by running the following
   command:

```
mount-s3 --version
```

You should see output similar to the following:

```
mount-s3 1.21.0
```

## Verifying the signature of the Mountpoint for Amazon S3 package

1. Install GnuPG (the `gpg` command). It is required to
   verify the authenticity and integrity of a downloaded Mountpoint for Amazon S3 package.
   GnuPG is installed by default on Amazon Linux Amazon Machine Images (AMIs).
   After you installGnuPG, proceed to step 2.
2. Download the Mountpoint public key by running the following command:

```
wget https://s3.amazonaws.com/mountpoint-s3-release/public_keys/KEYS
```

3. Import the Mountpoint public key into your keyring by running the following
   command:

```
gpg --import KEYS
```

4. Verify the fingerprint of the Mountpoint public key by running the following
   command:

```
gpg --fingerprint mountpoint-s3@amazon.com
```

Confirm that the displayed fingerprint string matches the following:

```
673F E406 1506 BB46 9A0E  F857 BE39 7A52 B086 DA5A
```

If the fingerprint string doesn't match, do not finish installing
Mountpoint, and contact [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/"). 5. Download the package signature file. Replace
`signature-link` with the appropriate
signature link from the preceding sections.

```
wget `signature-link`
```

6. Verify the signature of the downloaded package by running the following command.
   Replace `signature-filename` with the file name
   from the previous step.

```
gpg --verify `signature-filename`
```

For example, on RPM-based distributions, including Amazon Linux, enter the following
command:

```
gpg --verify mount-s3.rpm.asc
```

7. The output should include the phrase `Good signature`. If the output
   includes the phrase `BAD signature`, redownload the Mountpoint
   package file and repeat these steps. If the issue persists, do not finish installing
   Mountpoint, and contact [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").

The output may include a warning about a trusted signature. This does not indicate a
problem. It only means that you have not independently verified the Mountpoint
public key.
