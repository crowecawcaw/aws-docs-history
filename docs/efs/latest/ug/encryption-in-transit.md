# Encrypting data in transit

Amazon EFS supports encryption of data in transit with Transport Layer Security (TLS). When
encryption of data in transit is declared as a mount option for your EFS file
system, Amazon EFS establishes a secure TLS connection with your EFS file system upon
mounting your file system. All NFS traffic is routed through this encrypted
connection.

## How encrypting in transit works

We recommend using the EFS mount helper to mount your file system because it
simplifies the mounting process as compared to mounting with NFS `mount`. The
EFS mount helper manages the process by using either efs-proxy (for efs-utils version
2.0.0 and later) or stunnel (for efs-utils earlier versions) to establish a secure TLS
connection with your EFS file system.

If you're not using the mount helper, you can still enable encryption of data in transit. The following are the steps to do so.

###### To enable encryption of data in transit without using the mount helper

1. Download and install `stunnel`, and note the port that the application
   is listening on. For more information, see [Upgrading stunnel](upgrading-stunnel.md "upgrading-stunnel.md").
2. Run `stunnel` to connect to your EFS file system on port
   2049 using TLS.
3. Using the NFS client, mount
   `localhost:`port`, where
`port`` is the port that you noted in the
   first step.

Because encryption of data in transit is configured on a per-connection basis, each
configured mount has a dedicated `stunnel` process running on the instance. By
default, the stunnel process used by the mount helper listens on a local port between
20049 and 20449, and it connects to Amazon EFS on port 2049.

###### Note

By default, when using the EFS mount helper with TLS, it enforces the use of the
Online Certificate Status Protocol (OCSP) and certificate hostname checking. The
EFS mount helper uses the stunnel program for its TLS functionality. Some versions of
Linux don't include a version of stunnel that supports these TLS features by default.
When using one of those Linux versions, mounting an EFS file system using TLS
fails.

After you've installed the amazon-efs-utils package, to upgrade your system's
version of stunnel, see [Upgrading stunnel](upgrading-stunnel.md "upgrading-stunnel.md").

For issues with encryption, see [Troubleshooting encryption](troubleshooting-efs-encryption.md "troubleshooting-efs-encryption.md").

When using encryption of data in transit, your NFS client setup is changed. When you
inspect your actively mounted file systems, you see one mounted to 127.0.0.1, or
`localhost`, as in the following example.

```
$ mount | column -t
127.0.0.1:/  on  /home/ec2-user/efs        type  nfs4         (rw,relatime,vers=4.1,rsize=1048576,wsize=1048576,namlen=255,hard,proto=tcp,port=20127,timeo=600,retrans=2,sec=sys,clientaddr=127.0.0.1,local_lock=none,addr=127.0.0.1)
```

When mounting with TLS and the EFS mount helper, you are reconfiguring your NFS
client to mount to a local port. The EFS mount helper starts a client
`stunnel` process that is listening on this local port, and
`stunnel` is opening an encrypted connection to the EFS file
system using TLS. The EFS mount helper is responsible for setting up and maintaining this
encrypted connection and the associated configuration.

To determine which Amazon EFS file system ID corresponds to which local mount point, you
can use the following command. Remember to replace
`efs-mount-point` with the local path where you’ve mounted your
file system.

```
grep -E "Successfully mounted.*`efs-mount-point`" /var/log/amazon/efs/mount.log | tail -1
```

When you use the EFS mount helper for encryption of data in transit, it also creates
a process called `amazon-efs-mount-watchdog`. This process ensures that each
mount's stunnel process is running, and stops the stunnel when the EFS file system is
unmounted. If for some reason a stunnel process is terminated unexpectedly, the watchdog
process restarts it.
