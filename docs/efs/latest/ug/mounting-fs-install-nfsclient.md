# Installing the NFS client

To mount your EFS file system on your Amazon EC2 instance, first you need to
install an NFS client. To connect to your EC2 instance and install an NFS client, you need the
public DNS name of the EC2 instance and a user name to log in. That user name for your
instance is typically `ec2-user`.

###### To connect your EC2 instance and install the NFS client

1. Connect to your EC2 instance. For more information, see [Connect to your
   EC2 instance](../../../AWSEC2/latest/UserGuide/connect.md "../../../AWSEC2/latest/UserGuide/connect.md") in the
   _Amazon EC2 User Guide_.

The key file cannot be publicly viewable for SSH. You can use the
**chmod 400 `filename`.pem** command to set these
permissions. For more information, see
[Create a key pair for your Amazon EC2 instance](../../../AWSEC2/latest/UserGuide/create-key-pairs.md "../../../AWSEC2/latest/UserGuide/create-key-pairs.md"). 2. (Optional) Get updates and reboot.

```
`$` sudo yum -y update
            `$` sudo reboot
```

3. After the reboot, reconnect to your EC2 instance.
4. Install the NFS client.

If you're using an Amazon Linux AMI or Red Hat Linux AMI, install the NFS client with the following command.

```
`$` sudo yum -y install nfs-utils
```

If you're using an Ubuntu Amazon EC2 AMI, install the NFS client with the following command.

```
`$` sudo apt-get -y install nfs-common
```

5. Start the NFS service using the following command:

```
`$` `sudo service nfs-server start`
```

6. Verify that the NFS service started, as follows.

```
`$` `sudo service nfs-server status`
`Redirecting to /bin/systemctl status nfs.service
● nfs-server.service - NFS server and services
 Loaded: loaded (/usr/lib/systemd/system/nfs-server.service; disabled; vendor preset: disabled)
 Active: active (exited) since Wed 2019-10-30 16:13:44 UTC; 5s ago
 Process: 29446 ExecStart=/usr/sbin/rpc.nfsd $RPCNFSDARGS (code=exited, status=0/SUCCESS)
 Process: 29441 ExecStartPre=/bin/sh -c /bin/kill -HUP `cat /run/gssproxy.pid` (code=exited, status=0/SUCCESS)
 Process: 29439 ExecStartPre=/usr/sbin/exportfs -r (code=exited, status=0/SUCCESS)
 Main PID: 29446 (code=exited, status=0/SUCCESS)
 CGroup: /system.slice/nfs-server.service`
```

If you use a custom kernel (that is, if you build a custom AMI), you need to include at
a minimum the NFSv4.1 client kernel module and the right NFS4 userspace mount helper.

###### Note

If you choose **Amazon Linux AMI 2016.03.0** or
**Amazon Linux AMI 2016.09.0** when launching your Amazon EC2
instance, you don't need to install `nfs-utils` because it's already included
in the AMI by default.

###### Next: Mount your file system

Use one of the following procedures to mount your file system.

- [Mounting on Amazon EC2 with a DNS name](mounting-fs-mount-cmd-dns-name.md "mounting-fs-mount-cmd-dns-name.md")
- [Mounting with an IP address](mounting-fs-mount-cmd-ip-addr.md "mounting-fs-mount-cmd-ip-addr.md")
- [Automatically mounting EFS file systems](nfs-automount-efs.md "nfs-automount-efs.md")
