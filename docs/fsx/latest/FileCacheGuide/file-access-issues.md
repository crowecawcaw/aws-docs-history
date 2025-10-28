# Troubleshooting file access issues

There are a number of potential causes for being unable to access files.

## Cannot see files on the cache

You mounted your cache, but you don't see any files.

**Action to take**

Ensure that you’re running a supported Lustre client and that the Linux instance
you’re using to access the cache has a Linux kernel version that meets the minimum
requirement for your client operating system. For more information,
see [Installing the Lustre client](install-lustre-client.md "install-lustre-client.md").

## Cannot read files in linked NFS file system

You can successfully create a cache linked to your NFS file system, but you get
an error when you try to read a file on it.

**Action to take**

If this issue occurs, do the following:

1. Ensure that your setup complies with the
   [Prerequisites for linking to on-premises
   NFS data repositories](nfs-filer-prereqs.md "nfs-filer-prereqs.md").

###### Note

While Amazon File Cache supports NFSv3 file systems with most NFSv3
export policies, you must not use the NFS export option `all_squash`. 2. Are all of the file servers and metadata servers in the cache able to reach your
linked NFS file system?

In order for Amazon File Cache to be able to access data in your NFS file system,
all of the File Cache network interfaces must be able to communicate with your NFS
file system. If you have a network firewall or IP allow-list, ensure that it includes
all of the cache IP addresses and allows traffic on the ports that File Cache requires
to be open. For more information, see [Cache access control with Amazon VPC](limit-access-security-groups.md "limit-access-security-groups.md").

You can see all of your cache IP addresses by going to the Amazon EC2 console, go to
**Network Interfaces** in the left-side menu under
**Network & Security**, and filter by `Cache ID`.

Alternatively, you can use the AWS CLI and type the following command:

```
aws ec2 describe-network-interfaces --filters Name=description,Values=*fc-0123456789abcdef0
```

For `Values` in the `--filters` option, be sure to replace the
sample cache ID in the command with your cache ID.
