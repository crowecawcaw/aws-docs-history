# Install EC2Rescue on an Amazon EC2 Linux instance

The EC2Rescue for Linux tool can be installed on an Amazon EC2 Linux instance that meets the
following prerequisites.

###### Prerequisites

- Supported operating systems:
  - Amazon Linux 2
  - Amazon Linux 2016.09+
  - SUSE Linux Enterprise Server 12+
  - RHEL 7+
  - Ubuntu 16.04+

- Software requirements:
  - Python 2.7.9+ or 3.2+

## Install EC2Rescue

The `AWSSupport-TroubleshootSSH` runbook installs EC2Rescue for Linux and
then uses the tool to check or attempt to fix common issues that prevent a remote connection
to a Linux machine via SSH. For more information, and to run this automation, see [Support-TroubleshootSSH](../../../systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshootssh.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-awssupport-troubleshootssh.md").

If your system has the required Python version, you can install the standard build.
Otherwise, you can install the bundled build, which includes a minimal copy of Python.

###### To install the standard build

1. From a working Linux instance, download the [EC2Rescue for Linux](https://s3.amazonaws.com/ec2rescuelinux/ec2rl.tgz "https://s3.amazonaws.com/ec2rescuelinux/ec2rl.tgz")
   tool:

```
`curl -O https://s3.amazonaws.com/ec2rescuelinux/ec2rl.tgz`
```

2. (_Optional_) Verify the signature of the EC2Rescue for Linux installation file.
   For more information, see [(Optional) Verify the signature of
   EC2Rescue for Linux](#ec2rl_verify "#ec2rl_verify").
3. Download the sha256 hash file:

```
`curl -O https://s3.amazonaws.com/ec2rescuelinux/ec2rl.tgz.sha256`
```

4. Verify the integrity of the tarball:

```
`sha256sum -c ec2rl.tgz.sha256`
```

5. Unpack the tarball:

```
`tar -xzvf ec2rl.tgz`
```

6. Verify the installation by listing out the help file:

```
`cd ec2rl-`<version_number>`
./ec2rl help`
```

###### To install the bundled build

For a link to the download and a list of limitations, see [EC2Rescue for Linux](https://github.com/awslabs/aws-ec2rescue-linux/blob/master/README.md "https://github.com/awslabs/aws-ec2rescue-linux/blob/master/README.md") on github.

## (Optional) Verify the signature of

EC2Rescue for Linux

The following is the recommended process of verifying the validity of the
EC2Rescue for Linux package for Linux-based operating systems.

When you download an application from the internet, we recommend that you authenticate the
identity of the software publisher and check that the application has not been altered or
corrupted after it was published. This protects you from installing a version of the
application that contains a virus or other malicious code.

If, after running the steps in this topic, you determine that the software for
EC2Rescue for Linux is altered or corrupted, do not run the installation file. Instead,
contact Amazon Web Services.

EC2Rescue for Linux files for Linux-based operating systems are signed using GnuPG, an
open-source implementation of the Pretty Good Privacy (OpenPGP) standard for secure digital
signatures. GnuPG (also known as GPG) provides authentication and integrity checking through a
digital signature. AWS publishes a public key and signatures that you can use to verify the
downloaded EC2Rescue for Linux package. For more information about PGP and GnuPG (GPG), see
[https://www.gnupg.org/](https://www.gnupg.org/ "https://www.gnupg.org/").

The first step is to establish trust with the software publisher. Download the public key
of the software publisher, check that the owner of the public key is who they claim to be, and
then add the public key to your keyring. Your keyring is a collection of known public keys.
After you establish the authenticity of the public key, you can use it to verify the signature
of the application.

###### Tasks

- [Authenticate and import the public key](#ec2rl_authenticate "#ec2rl_authenticate")
- [Verify the signature of the package](#ec2rl_verify_signature "#ec2rl_verify_signature")

### Authenticate and import the public key

The next step in the process is to authenticate the EC2Rescue for Linux public key and
add it as a trusted key in your GPG keyring.

###### To authenticate and import the EC2Rescue for Linux public key

1. At a command prompt, use the following command to obtain a copy of our public GPG
   build key:

```
`curl -O https://s3.amazonaws.com/ec2rescuelinux/ec2rl.key`
```

2. At a command prompt in the directory where you saved `ec2rl.key`, use the
   following command to import the EC2Rescue for Linux public key into your
   keyring:

```
`gpg2 --import ec2rl.key`
```

The command returns results similar to the following:

```
gpg: /home/ec2-user/.gnupg/trustdb.gpg: trustdb created
gpg: key 2FAE2A1C: public key "ec2autodiag@amazon.com <EC2 Rescue for Linux>" imported
gpg: Total number processed: 1
gpg:               imported: 1  (RSA: 1)
```

###### Tip

If you see an error stating that the command cannot be found, install the
GnuPG utility with `apt-get install gnupg2` (Debian-based Linux)
or `yum install gnupg2` (Red Hat- based Linux).

### Verify the signature of the package

After you've installed the GPG tools, authenticated and imported the
EC2Rescue for Linux public key, and verified that the EC2Rescue for Linux public key is
trusted, you are ready to verify the signature of the EC2Rescue for Linux installation
script.

###### To verify the EC2Rescue for Linux installation script signature

1. At a command prompt, run the following command to download the signature file for
   the installation script:

```
`curl -O https://s3.amazonaws.com/ec2rescuelinux/ec2rl.tgz.sig`
```

2. Verify the signature by running the following command at a command prompt in the
   directory where you saved `ec2rl.tgz.sig` and the EC2Rescue for Linux
   installation file. Both files must be present.

```
`gpg2 --verify ./ec2rl.tgz.sig`
```

The output should look something like the following:

```
gpg: Signature made Thu 12 Jul 2018 01:57:51 AM UTC using RSA key ID 6991ED45
gpg: Good signature from "ec2autodiag@amazon.com <EC2 Rescue for Linux>"
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: E528 BCC9 0DBF 5AFA 0F6C  C36A F780 4843 2FAE 2A1C
     Subkey fingerprint: 966B 0D27 85E9 AEEC 1146  7A9D 8851 1153 6991 ED45
```

If the output contains the phrase `Good signature from "ec2autodiag@amazon.com
 <EC2 Rescue for Linux>"`, it means that the signature has successfully been
verified, and you can proceed to run the EC2Rescue for Linux installation
script.

If the output includes the phrase `BAD signature`, check whether you
performed the procedure correctly. If you continue to get this response, contact
Amazon Web Services and do not run the installation file that you downloaded previously.

The following are details about the warnings that you might see:

- **WARNING: This key is not certified with a trusted signature! There is no
  indication that the signature belongs to the owner.** This refers to your
  personal level of trust in your belief that you possess an authentic public key for
  EC2Rescue for Linux. In an ideal world, you would visit an Amazon Web Services office and
  receive the key in person. However, more often you download it from a website. In this
  case, the website is an Amazon Web Services website.
- **gpg2: no ultimately trusted keys found.** This means that the
  specific key is not "ultimately trusted" by you (or by other people whom you
  trust).

For more information, see [https://www.gnupg.org/](https://www.gnupg.org/ "https://www.gnupg.org/").
