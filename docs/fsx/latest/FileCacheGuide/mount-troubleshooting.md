# Troubleshooting cache mount issues

There are a number of potential causes when a cache mount command fails,
as described in the following topics.

## Cache mount fails right away

The cache mount command fails right away. The following code shows an
example.

```
`mount.lustre: mount fc-0123456789abcdef0.fsx.us-east-1.aws@tcp:/fsx at /mnt`
`failed: No such file or directory

Is the MGS specification correct?
Is the filesystem name correct?`
```

This error can occur if you aren't using the correct `mountname` value when
mounting a cache by using the **mount**
command. You can get the `mountname` value from the response of the
[**describe-file-caches**](../../../cli/latest/reference/fsx/describe-file-caches.md "../../../cli/latest/reference/fsx/describe-file-caches.md") AWS CLI command
or the [**DescribeFileCaches**](../APIReference/API_DescribeFileCaches.md "../APIReference/API_DescribeFileCaches.md") API operation, and also from the **Mount name**
field on the cache console's **Summary** panel.

## Cache mount hangs and then fails with

timeout error

The cache mount command hangs for a minute or two, and then fails with a timeout
error.

The following code shows an example.

```
sudo mount -t lustre -o relatime,flock `cache_dns_name`@tcp:/`mountname` /mnt

*[2+ minute wait here]*
Connection timed out
```

This error can occur because the security groups for the Amazon EC2 instance or the
cache aren't configured properly.

**Action to take**

Make sure that your security groups for the cache
have the inbound rules specified in [Amazon VPC security groups](limit-access-security-groups.md#fsx-vpc-security-groups "limit-access-security-groups.md#fsx-vpc-security-groups").

## Automatic mounting fails and the instance is

unresponsive

In some cases, automatic mounting might fail for a cache and your Amazon EC2
instance might stop responding.

This issue can occur if the `_netdev` option wasn't declared. If
`_netdev` is missing, your Amazon EC2 instance can stop responding. This
result is because network caches need to be initialized after the compute instance
starts its networking.

###### Action to take

If this issue occurs, contact AWS Support.

## Cache mount fails during

system boot

The cache mount fails during the system boot. The mounting is automated
using `/etc/fstab`. When the cache is not mounted, the following
error is seen in the syslog for the instance booting time frame.

```
LNetError: 3135:0:(lib-socket.c:583:lnet_sock_listen()) Can't create socket: port 988 already in use
LNetError: 122-1: Can't start acceptor on port 988: port already in use
```

This error can occur when port 988 is not available. When the instance is
configured to mount NFS caches, it is possible that the NFS mounts will
bind its client port to port 988

**Action to take**

You can work around this problem by tuning the NFS client's `noresvport`
and `noauto` mount options where possible.

## Cache mount using DNS name fails

Misconfigured Domain Name Service (DNS) names can cause cache mount failures,
as shown in the following scenarios.

**Scenario 1:** A cache mount that is using a Domain Name Service (DNS) name fails. The
following code shows an example.

```
sudo mount -t lustre `cache_dns_name`@tcp:/`mountname` `/mnt`
mount.lustre: Can't parse NID
'`cache_dns_name`@tcp:/`mountname`'
```

**Action to take**

Check your virtual private cloud (VPC) configuration. If you are using a custom VPC,
make sure that DNS settings are enabled. For more information, see [Using DNS with Your VPC](../../../vpc/latest/userguide/vpc-dns.md "../../../vpc/latest/userguide/vpc-dns.md") in the
_Amazon VPC User Guide_.

To specify a DNS name in the `mount` command, do the following:

- Ensure that the Amazon EC2 instance is in the same VPC as your Amazon File Cache.
- Connect your Amazon EC2 instance inside a VPC configured to use the DNS server
  provided by Amazon. For more information, see [DHCP option sets in Amazon VPC](../../../vpc/latest/userguide/VPC_DHCP_Options.md "../../../vpc/latest/userguide/VPC_DHCP_Options.md")
  in the _Amazon VPC User Guide_.
- Ensure that the Amazon VPC of the connecting Amazon EC2 instance has DNS host names
  enabled. For more information, see [View and update DNS attributes for your VPC](../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-updating "../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-updating")
  in the _Amazon VPC User Guide_.

**Scenario 2:** A cache mount that is using a Domain Name Service (DNS) name fails. The
following code shows an example.

```
mount -t lustre `cache_dns_name`@tcp:/`mountname` `/mnt`
mount.lustre: mount `cache_dns_name`@tcp:/`mountname` at /mnt failed: Input/output error Is the MGS running?
```

**Action to take**

Make sure that the client's VPC security groups have the correct outbound traffic
rules applied. This recommendation holds true especially if you aren't using the
default security group, or if you have modified the default security group. For more
information, see [Cache access control with Amazon VPC](limit-access-security-groups.md "limit-access-security-groups.md").
