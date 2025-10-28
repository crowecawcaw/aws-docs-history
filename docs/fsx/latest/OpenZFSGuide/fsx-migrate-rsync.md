# Migrating files to Amazon FSx for OpenZFS using rsync

With **rsync**, you can replicate data between any source and destination, but
at least one must be locally accessible to the client instance.

Amazon EC2 instance

###### To migrate existing files to Amazon FSx from a Linux-based Amazon EC2 instance

The following procedure configures your FSx for OpenZFS destination volume
as a local NFS mount on a Linux-based EC2 instance and uses the **rsync** command
to synchronize data from your source file system or existing directory on your
EC2 instance.

1. Launch a Linux-based Amazon EC2 instance or connect to an existing EC2 instance
   that contains your desired source data.
2. Mount your destination FSx for OpenZFS
   source volume; for more information, see [Step 2: Mount your file system from an Amazon EC2 instance](getting-started.md#getting-started-step2 "getting-started.md#getting-started-step2").
   The following step assumes that you have mounted your desired
   destination on your OpenZFS volume to `/fsx/destination_path` on
   your EC2 instance.
3. Run **rsync** from this EC2 instance to synchronize data from your source.
   If your source data is already on the EC2 instance, use the following command:

```
sudo rsync -avR /`source_path` /fsx/destination_path
```

###### Note

You can also run **rsync** with GNU parallel to maximize performance.
The following instructions apply for EC2 Linux instances running Amazon Linux 2:.

```
sudo amazon-linux-extras install epel
sudo yum install nload sysstat parallel -y
sudo time find -L /`source_path` -type f | parallel rsync -avR {} /fsx/destination_path
```

If your source is a directory on a remote host, use the following command:

```
sudo rsync -avR `username`@`source_dns_or_ip`:/`source_path` /fsx/destination_path
```

Use the following variant if you need to use .pem key-based authentication:

```
sudo rsync -avR -e "ssh -i key.pem" `username`@`source_dns_or_ip`:/`source_path` /fsx/destination_path
```

On-premises

###### To migrate existing files to Amazon FSx from your on-premises Linux-based source

The following procedure configures your FSx for OpenZFS destination volume as a local
NFS mount on a Linux-based EC2 instance. Then, you use **rsync** from your source to connect
to this EC2 instance and synchronize files to the path where the destination Amazon FSx
volume is mounted.

1. Launch a Linux-based Amazon EC2 instance and mount your destination FSx for OpenZFS
   source volume. For more information, see
   [Step 2: Mount your file system from an Amazon EC2 instance](getting-started.md#getting-started-step2 "getting-started.md#getting-started-step2").
   The following step assumes that you have mounted the desired
   destination on your OpenZFS volume to `/fsx/destination_path` on
   your EC2 instance.
2. From your on-premises Linux-based source, run **rsync** to connect to this
   EC2 instance and synchronize data from any locally accessible path. For example,
   `source_path` can refer to a locally accessible directory or a path on another
   shared file system.

```
sudo rsync -e "ssh -i key.pem" /`source_path` `ec2-user`@`ec2_dns_name`.amazonaws.com:/fsx/destination_path
```
