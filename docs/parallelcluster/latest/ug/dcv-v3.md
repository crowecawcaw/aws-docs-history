

# Connect to the head and login nodes through Amazon DCV
<a name="dcv-v3"></a>

Amazon DCV is a remote visualization technology that enables users to securely connect to graphic intensive 3D applications that are hosted on a remote high-performance server. For more information, see [Amazon DCV](https://docs.aws.amazon.com/dcv/).

The Amazon DCV software is automatically installed on the head node and can be enabled by using the [`Dcv`](HeadNode-v3.md#HeadNode-v3-Dcv) section from the [`HeadNode`.](HeadNode-v3.md)

Starting from AWS ParallelCluster version 3.11, Amazon DCV can be enabled for a login node pool by using the Dcv section from the [`LoginNodes` section](LoginNodes-v3.md) / [Pools](LoginNodes-v3.md#LoginNodes-v3-Pools) configuration.

```
LoginNodes:
  Pools:
    Dcv: 
      Enabled: true
```

AWS ParallelCluster sets `/home/{{<DEFAULT_AMI_USER>}}` as the [DCV server storage folder](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-storage.html). For more information about Amazon DCV configuration parameters, see [`HeadNode`](HeadNode-v3.md) / [`Dcv`](HeadNode-v3.md#HeadNode-v3-Dcv).

To connect to the Amazon DCV session on the head node, use the [`dcv-connect`](pcluster.dcv-connect-v3.md) command. To connect on a login node, use `dcv-connect` with the `--login-node-ip` parameter and pass in the public or private IP address of the login node you wish to connect to.

## Amazon DCV HTTPS certificate
<a name="dcv-v3-certificate"></a>

Amazon DCV automatically generates a self-signed certificate to secure traffic between the Amazon DCV client and Amazon DCV server.

To replace the default self-signed Amazon DCV certificate with another certificate, first connect to the head node. Then, copy both the certificate and key to the `/etc/dcv` folder before running the [`pcluster dcv-connect`](pcluster.dcv-connect-v3.md) command.

For more information, see [Changing the TLS certificate](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-cert.html) in the *Amazon DCV Administrator Guide*.

## Licensing Amazon DCV
<a name="dcv-v3-license"></a>

The Amazon DCV server doesn't require a license server when running on Amazon EC2 instances. However, the Amazon DCV server must periodically connect to an Amazon S3 bucket to determine if a valid license is available.

AWS ParallelCluster automatically adds the required permissions to the head node IAM policy. When using a custom IAM Instance Policy, use the permissions described in [Amazon DCV on Amazon EC2 ](https://docs.aws.amazon.com/dcv/latest/adminguide/setting-up-license.html#setting-up-license-ec2) in the *Amazon DCV Administrator Guide*.

For troubleshooting tips, see [Troubleshooting issues in Amazon DCV](troubleshooting-v3-nice-dcv.md).