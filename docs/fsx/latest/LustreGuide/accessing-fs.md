# Accessing file systems

Using Amazon FSx, you can burst your compute-intensive workloads from on-premises into the Amazon Web Services
Cloud by importing data over AWS Direct Connect or VPN. You can access your Amazon FSx file system from
on-premises, copy data into your file system as-needed, and run compute-intensive workloads on
in-cloud instances.

In the following section, you can learn how to access your Amazon FSx for Lustre file system on a
Linux instance. In addition, you can find how to use the file `fstab` to
automatically remount your file system after any system restarts.

Before you can mount a file system, you must create, configure, and launch your related AWS
resources. For detailed instructions, see [Getting started with Amazon FSx for Lustre](getting-started.md "getting-started.md"). Next, you can install and configure the Lustre client on
your compute instance.

###### Topics

- [Lustre file system and client kernel compatibility](lustre-client-matrix.md "lustre-client-matrix.md")
- [Installing the Lustre client](install-lustre-client.md "install-lustre-client.md")
- [Mounting from an Amazon Elastic Compute Cloud
  instance](mounting-ec2-instance.md "mounting-ec2-instance.md")
- [Configuring EFA clients](configure-efa-clients.md "configure-efa-clients.md")
- [Mounting from Amazon Elastic Container Service](mounting-ecs.md "mounting-ecs.md")
- [Mounting Amazon FSx file systems from on-premises or a peered Amazon VPC](mounting-on-premises.md "mounting-on-premises.md")
- [Mounting your Amazon FSx file system
  automatically](mount-fs-auto-mount-onreboot.md "mount-fs-auto-mount-onreboot.md")
- [Mounting specific filesets](mounting-from-fileset.md "mounting-from-fileset.md")
- [Unmounting file systems](unmounting-fs.md "unmounting-fs.md")
- [Working with Amazon EC2 Spot Instances](working-with-ec2-spot-instances.md "working-with-ec2-spot-instances.md")
