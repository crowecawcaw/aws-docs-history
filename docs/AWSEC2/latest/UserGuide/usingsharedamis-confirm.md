# Prepare to use shared AMIs for Linux

Before you use a shared AMI for Linux, take the following steps to confirm that there are no
pre-installed credentials that would allow unwanted access to your instance by a
third party and no pre-configured remote logging that could transmit sensitive data
to a third party. Check the documentation for the Linux distribution used by the AMI
for information about improving the security of the system.

To ensure that you don't accidentally lose access to your instance, we recommend
that you initiate two SSH sessions and keep the second session open until you've
removed credentials that you don't recognize and confirmed that you can still log
into your instance using SSH.

1. Identify and disable any unauthorized public SSH keys. The only key in the
   file should be the key you used to launch the AMI. The following command
   locates `authorized_keys` files:

```
`[ec2-user ~]$` **sudo find** / -name "authorized_keys" -print -exec cat {} \;
```

2. Disable password-based authentication for the root user. Open the
   `sshd_config` file and edit the
   `PermitRootLogin` line as follows:

```
PermitRootLogin without-password
```

Alternatively, you can disable the ability to log into the instance as the root
user:

```
PermitRootLogin No
```

Restart the sshd service. 3. Check whether there are any other users that are able to log in to
your instance. Users with superuser privileges are particularly
dangerous. Remove or lock the password of any unknown accounts. 4. Check for open ports that you aren't using and running network services
listening for incoming connections. 5. To prevent preconfigured remote logging, you should delete the existing configuration
file and restart the `rsyslog` service. For example:

```
`[ec2-user ~]$` sudo rm /etc/rsyslog.conf
`[ec2-user ~]$` sudo service rsyslog restart
```

6. Verify that all cron jobs are legitimate.
   If you discover a public AMI that you feel presents a security risk, contact the
   AWS security team. For more information, see the [AWS Security Center](https://aws.amazon.com/security/ "https://aws.amazon.com/security/").
