# Recommendations for creating shared Linux AMIs

Use the following guidelines to reduce the attack surface and improve the reliability of the
AMIs you create.

###### Important

No list of security guidelines can be exhaustive. Build your shared AMIs
carefully and take time to consider where you might expose sensitive data.

###### Contents

- [Disable password-based remote
  logins for the root user](#public-amis-disable-password-logins-for-root "#public-amis-disable-password-logins-for-root")
- [Disable local root access](#restrict-root-access "#restrict-root-access")
- [Remove SSH host key pairs](#remove-ssh-host-key-pairs "#remove-ssh-host-key-pairs")
- [Install public key credentials](#public-amis-install-credentials "#public-amis-install-credentials")
- [Disable sshd DNS checks (optional)](#public-amis-disable-ssh-dns-lookups "#public-amis-disable-ssh-dns-lookups")
- [Remove sensitive data](#public-amis-protect-yourself "#public-amis-protect-yourself")
  If you are building AMIs for AWS Marketplace, see [Best
  practices for building AMIs](../../../marketplace/latest/userguide/best-practices-for-building-your-amis.md "../../../marketplace/latest/userguide/best-practices-for-building-your-amis.md") in the _AWS Marketplace Seller Guide_ for guidelines, policies, and best practices.

## Disable password-based remote

logins for the root user

Using a fixed root password for a public AMI is a security risk that can quickly
become known. Even relying on users to change the password after the first login
opens a small window of opportunity for potential abuse.

To solve this problem, disable password-based remote logins for the root user.

###### To disable password-based remote logins for the root user

1. Open the `/etc/ssh/sshd_config` file with a text editor and
   locate the following line:

```
#PermitRootLogin yes
```

2. Change the line to:

```
PermitRootLogin without-password
```

The location of this configuration file might differ for your
distribution, or if you are not running OpenSSH. If this is the case,
consult the relevant documentation.

## Disable local root access

When you work with shared AMIs, a best practice is to disable direct root logins. To do
this, log into your running instance and issue the following command:

```
`[ec2-user ~]$` sudo passwd -l root
```

###### Note

This command does not impact the use of `sudo`.

## Remove SSH host key pairs

If you plan to share an AMI derived from a public AMI, remove the existing SSH
host key pairs located in `/etc/ssh`. This forces SSH to generate new
unique SSH key pairs when someone launches an instance using your AMI, improving
security and reducing the likelihood of "man-in-the-middle" attacks.

Remove all of the following key files that are present on your system.

- ssh_host_dsa_key
- ssh_host_dsa_key.pub
- ssh_host_key
- ssh_host_key.pub
- ssh_host_rsa_key
- ssh_host_rsa_key.pub
- ssh_host_ecdsa_key
- ssh_host_ecdsa_key.pub
- ssh_host_ed25519_key
- ssh_host_ed25519_key.pub

You can securely remove all of these files with the following
command.

```
`[ec2-user ~]$` sudo shred -u /etc/ssh/*_key /etc/ssh/*_key.pub
```

###### Warning

Secure deletion utilities such as **shred** might not remove all copies
of a file from your storage media. Hidden copies of files may be created by
journalling file systems (including Amazon Linux default ext4), snapshots, backups,
RAID, and temporary caching. For more information, see the
[shred documentation](https://www.gnu.org/software/coreutils/manual/html_node/shred-invocation.html "https://www.gnu.org/software/coreutils/manual/html_node/shred-invocation.html").

###### Important

If you forget to remove the existing SSH host key pairs from your public AMI,
our routine auditing process notifies you and all customers running instances of
your AMI of the potential security risk. After a short grace period, we mark the
AMI private.

## Install public key credentials

After configuring the AMI to prevent logging in using a password, you must make
sure users can log in using another mechanism.

Amazon EC2 allows users to specify a public-private key pair name when launching an
instance. When a valid key pair name is provided to the
`RunInstances` API call (or through the command line API
tools), the public key (the portion of the key pair that Amazon EC2 retains on the server
after a call to `CreateKeyPair` or
`ImportKeyPair`) is made available to the instance through an
HTTP query against the instance metadata.

To log in through SSH, your AMI must retrieve the key value at boot and append it
to `/root/.ssh/authorized_keys` (or the equivalent for any other user
account on the AMI). Users can launch instances of your AMI with a key pair and log
in without requiring a root password.

Many distributions, including Amazon Linux and Ubuntu, use the
`cloud-init` package to inject public key credentials for a
configured user. If your distribution does not support
`cloud-init`, you can add the following code to a system start-up
script (such as `/etc/rc.local`) to pull in the public key you
specified at launch for the root user.

###### Note

In the following example, the IP address http://169.254.169.254/ is a link-local address and is valid only from the instance.

IMDSv2

```
if [ ! -d /root/.ssh ] ; then
        mkdir -p /root/.ssh
        chmod 700 /root/.ssh
fi
# Fetch public key using HTTP
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key > /tmp/my-key
if [ $? -eq 0 ] ; then
        cat /tmp/my-key >> /root/.ssh/authorized_keys
        chmod 700 /root/.ssh/authorized_keys
        rm /tmp/my-key
fi
```

IMDSv1

```
if [ ! -d /root/.ssh ] ; then
        mkdir -p /root/.ssh
        chmod 700 /root/.ssh
fi
# Fetch public key using HTTP
curl http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key > /tmp/my-key
if [ $? -eq 0 ] ; then
        cat /tmp/my-key >> /root/.ssh/authorized_keys
        chmod 700 /root/.ssh/authorized_keys
        rm /tmp/my-key
fi
```

This can be applied to any user; you do not need to restrict it to
the `root` user.

###### Note

Rebundling an instance based on this AMI includes the key with which it was
launched. To prevent the key's inclusion, you must clear out (or delete) the
`authorized_keys` file or exclude this file from rebundling.

## Disable sshd DNS checks (optional)

Disabling sshd DNS checks slightly weakens your sshd security. However, if DNS
resolution fails, SSH logins still work. If you do not disable sshd checks, DNS
resolution failures prevent all logins.

###### To disable sshd DNS checks

1. Open the `/etc/ssh/sshd_config` file with a text editor and
   locate the following line:

```
#UseDNS yes
```

2. Change the line to:

```
UseDNS no
```

###### Note

The location of this configuration file can differ for your distribution or if
you are not running OpenSSH. If this is the case, consult the relevant
documentation.

## Remove sensitive data

We recommend against storing sensitive data or software on any AMI that you share.
Users who launch a shared AMI might be able to rebundle it and register it as their
own. Follow these guidelines to help you to avoid some easily overlooked security
risks:

- We recommend using the `--exclude `directory``option
on`ec2-bundle-vol`to skip any directories and subdirectories
that contain secret information that you would not like to include in your
bundle. In particular, exclude all user-owned SSH public/private key pairs
and SSH`authorized_keys`files when bundling the
image. The Amazon public AMIs store these in`/root/.ssh`for the root user, and`/home/`user_name`/.ssh/`
  for regular users. For more information, see [ec2-bundle-vol](ami-tools-commands.md#ami-bundle-vol "ami-tools-commands.md#ami-bundle-vol").
- Always delete the shell history before bundling. If you attempt more than
  one bundle upload in the same AMI, the shell history contains your access key.
  The following example should be the last command you run before bundling from
  within the instance.

```
`[ec2-user ~]$` shred -u ~/.*history
```

###### Warning

The limitations of **shred** described in the
warning above apply here as well.

Be aware that bash writes the history of the current session to the
disk on exit. If you log out of your instance after deleting
`~/.bash_history`, and then log back in, you
will find that `~/.bash_history` has been
re-created and contains all of the commands you ran during your
previous session.

Other programs besides bash also write histories to disk, Use caution
and remove or exclude unnecessary dot-files and dot-directories.

- Bundling a running instance requires your private key and X.509
  certificate. Put these and other credentials in a location that is not
  bundled (such as the instance store).
