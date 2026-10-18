

# Performing post-installation checks for the Amazon DCV server on Linux with Wayland
<a name="setting-up-installing-linux-wayland-post-installation-checks"></a>

This topic provides some post-installation checks that you should perform after installing Amazon DCV to ensure that your Amazon DCV server is properly configured.

**Topics**
+ [Ensure the Amazon DCV Server is reachable](#checks-port)
+ [Verify the Amazon DCV DEB package signature](#checks-deb)

## Ensure the Amazon DCV Server is reachable
<a name="checks-port"></a>

By default, the Amazon DCV server is configured to communicate over TCP port 8443. Ensure that the server is reachable over this port. If you have a firewall that prevents access over port 8443, you must change the port over which the Amazon DCV server communicates. For more information, see [Changing the Amazon DCV Server TCP/UDP ports and listen address](manage-port-addr.md).

Also, if you're setting up Amazon DCV on an EC2 instance, create a security group. This is to enable access to the port over which the Amazon DCV server communicates. For more information, see [how to configure security groups on EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html). 

## Verify the Amazon DCV DEB package signature
<a name="checks-deb"></a>

After Amazon DCV is installed, you can verify the signature on the Debian package (DEB). This verification process requires the use of GPG version 1.

**To verify the DEB package signature**  
Use the following command:

```
gpg1 --import NICE-GPG-KEY-SECRET
dpkg-sig --verify nice-dcv-server_2026.0.24952-1_amd64.deb
```

This will return a message that includes the term `GOODSIG` to confirm that the signature is verified. The following example shows a signature confirmation message. In place of {{Example Key}}, the key will be displayed.

```
Processing nice-dcv-server_2026.0.24952-1_amd64.deb...
GOODSIG _gpgbuilder {{Example Key}}
```