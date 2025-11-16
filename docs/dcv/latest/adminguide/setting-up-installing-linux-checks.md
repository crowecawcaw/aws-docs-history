# Performing post-installation checks

This topic provides some post-installation checks that you should perform after installing Amazon DCV to
ensure that your Amazon DCV server is properly configured.

###### Contents

- [Ensure the Amazon DCV Server is reachable](#checks-port "#checks-port")
- [Ensure that the X server is accessible](#checks-xserver "#checks-xserver")
- [Verify that DCV GL is properly installed](#checks-gl "#checks-gl")
- [Verify the Amazon DCV DEB package signature](#checks-deb "#checks-deb")

## Ensure the Amazon DCV Server is reachable

By default, the Amazon DCV server is configured to communicate over TCP port 8443. Ensure that the server is
reachable over this port. If you have a firewall that prevents access over port 8443, you must
change the port over which the Amazon DCV server communicates. For more information, see
[Changing the Amazon DCV Server TCP/UDP ports and listen address](manage-port-addr.md "manage-port-addr.md").

Also, if you're setting up Amazon DCV on an EC2 instance, create a security group. This
is to enable access to the port over which the Amazon DCV server communicates. For more
information, see [how to configure security groups on EC2](../../../AWSEC2/latest/UserGuide/using-network-security.md "../../../AWSEC2/latest/UserGuide/using-network-security.md").

## Ensure that the X server is accessible

You must ensure that Amazon DCV console and virtual sessions can access the X server.

### Console Sessions

When the Amazon DCV server is installed, a `dcv` user is created. Ensure that
this user can access the X server.

###### To verify that the `dcv` user can access the X server

Run the following command:

```
`$` sudo DISPLAY=:0 XAUTHORITY=$(ps aux | grep "X.*\-auth" | grep -v Xdcv | grep -v grep | sed -n 's/.*-auth \([^ ]\+\).*/\1/p') xhost | grep "SI:localuser:dcv$"
```

If the command returns `SI:localuser:dcv`, the dcv user can access the X server.

If the command does not return `SI:localuser:dcv`, the dcv user doesn't
have access to the X server. Run the following commands to restart the X
server:

- RHEL, Rocky, CentOS, Amazon Linux 2, Ubuntu, and SUSE Linux Enterprise

```
`$` sudo systemctl isolate multi-user.target
```

```
`$` sudo systemctl isolate graphical.target
```

### Virtual sessions

If you installed the DCV GL package, you must ensure that local users can access the X server.
This ensures that OpenGL hardware acceleration works correctly with virtual sessions.

###### To verify that local users can access the X server

Run the following command:

```
`$` sudo DISPLAY=:0 XAUTHORITY=$(ps aux | grep "X.*\-auth" | grep -v Xdcv | grep -v grep | sed -n 's/.*-auth \([^ ]\+\).*/\1/p') xhost | grep "LOCAL:$"
```

If the command returns `LOCAL:`, local users can access the X server.

If the command doesn't return `LOCAL:`, local users don't have access
to the X server. Run the following commands to restart the X server, and to disable
and re-enable DCV GL:

- RHEL, Rocky, CentOS, Amazon Linux 2, Ubuntu, and SUSE Linux Enterprise

```
`$` sudo systemctl isolate multi-user.target
```

```
`$` sudo dcvgladmin disable
```

```
`$` sudo dcvgladmin enable
```

```
`$` sudo systemctl isolate graphical.target
```

## Verify that DCV GL is properly installed

The dcvgldiag utility is automatically installed when you install the
DCV GL package. You can use this utility to check that the Linux server configuration meets the DCV GL
requirements.

###### To run the dcvgldiag utility

Use the following command:

```
`$` sudo dcvgldiag
```

The utility returns a list of warnings and errors, along with the possible solutions.

## Verify the Amazon DCV DEB package signature

After Amazon DCV is installed, you can verify the signature on the Debian package (DEB). This verification
process requires the use of GPG version 1.

###### To verify the DEB package signature

Use the following command:

```
gpg1 --import NICE-GPG-KEY-SECRET
dpkg-sig --verify nice-dcv-server_2025.0.20103-1_amd64.deb
```

This will return a message that includes the term `GOODSIG` to confirm that the signature is verified.
The following example shows a signature confirmation message. In place of `Example Key`, the
key will be displayed.

```
Processing nice-dcv-server_2017.0.0-1_amd64.deb...
GOODSIG _gpgbuilder `Example Key`
```
