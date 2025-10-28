# Connecting to an Amazon DocumentDB cluster from outside an Amazon VPC

Amazon DocumentDB (with MongoDB compatibility) clusters are deployed within an Amazon Virtual Private Cloud (Amazon VPC). They can be accessed directly by Amazon EC2 instances or other AWS services that are deployed in the same Amazon VPC. Additionally, Amazon DocumentDB can be accessed by EC2 instances or other AWS services in different VPCs in the same AWS Region or other Regions via VPC peering.

However, suppose that your use case requires that you (or your
application) access your Amazon DocumentDB resources from outside the cluster's VPC.
In that case, you can use SSH tunneling (also known as
_port forwarding_) to access your Amazon DocumentDB resources.

It is beyond the scope of this topic to discuss SSH tunneling in depth.
For more information about SSH tunneling, see the following:

- [SSH Tunnel](https://www.ssh.com/ssh/tunneling/ "https://www.ssh.com/ssh/tunneling/")
- [SSH Port
  Forwarding Example](https://www.ssh.com/ssh/tunneling/example "https://www.ssh.com/ssh/tunneling/example"),
  specifically the [Local Forwarding](https://www.ssh.com/ssh/tunneling/example#sec-Local-Forwarding "https://www.ssh.com/ssh/tunneling/example#sec-Local-Forwarding")
  section
  To create an SSH tunnel, you need an Amazon EC2 instance running in the same
  Amazon VPC as your Amazon DocumentDB cluster. You can either use an existing EC2 instance
  in the same VPC as your cluster or create one. For more information, see
  the topic that is appropriate for your operating system:

- [Getting Started with Amazon EC2 Linux Instances](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md")
- [Getting Started with Amazon EC2 Windows Instances](../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md "../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md")
  You might typically connect to an EC2 instance using the following
  command.

```
`ssh -i "ec2Access.pem" ubuntu@ec2-34-229-221-164.compute-1.amazonaws.com`
```

If so, you can set up an SSH tunnel to the Amazon DocumentDB cluster
`sample-cluster.node.us-east-1.docdb.amazonaws.com` by running
the following command on your local computer. The `-L` flag is
used for forwarding a local port. When using an SSH tunnel, we recommend
that you connect to your cluster using the cluster endpoint and do not
attempt to connect in replica set mode (i.e., specifying
`replicaSet=rs0` in your connection string) as it will result
in an error.

```
`ssh -i "ec2Access.pem" -L 27017:sample-cluster.node.us-east-1.docdb.amazonaws.com:27017 ubuntu@ec2-34-229-221-164.compute-1.amazonaws.com -N`
```

After the SSH tunnel is created, any commands that you issue to
`localhost:27017` are forwarded to the Amazon DocumentDB cluster
`sample-cluster` running in the Amazon VPC. If Transport Layer
Security (TLS) is enabled on your Amazon DocumentDB cluster, you need to download
the public key for Amazon DocumentDB from [https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem](https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem "https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem")
.
The following operation downloads this file:

```
`wget https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem`
```

###### Note

TLS is enabled by default for new Amazon DocumentDB clusters. However, you can
disable it. For more information, see [Managing Amazon DocumentDB cluster TLS settings](security.encryption.md#security.encryption.ssl.managing "security.encryption.md#security.encryption.ssl.managing").

To connect to your Amazon DocumentDB cluster from outside the Amazon VPC, use the
following command.

```
`mongo --sslAllowInvalidHostnames --ssl --sslCAFile global-bundle.pem --username <yourUsername> --password <yourPassword>`
```
