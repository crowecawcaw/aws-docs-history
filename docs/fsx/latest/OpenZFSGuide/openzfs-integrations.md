# Accessing your data using AWS container services

In addition to using Amazon EC2 instances, you can also access your Amazon FSx for OpenZFS file systems using other AWS services, including Amazon Elastic Container Service, Amazon Elastic Kubernetes Service, and Amazon S3.
You can mount your file system from an Amazon ECS Docker container, manage file system and volume life cycle using Amazon EKS, and use S3 Access Points to access file data using S3.
For more information about accessing FSx for OpenZFS file data with S3, see [Accessing your data using Amazon S3 access points](s3accesspoints-for-FSx.md "s3accesspoints-for-FSx.md").

To use Amazon EKS clusters to manage the life cycle of your file systems and volumes, see the [Amazon FSx for OpenZFS CSI Driver README](https://github.com/kubernetes-sigs/aws-fsx-openzfs-csi-driver?tab=readme-ov-file#readme "https://github.com/kubernetes-sigs/aws-fsx-openzfs-csi-driver?tab=readme-ov-file#readme").

The following section provides instructions on how to mount your file system from an Amazon ECS Docker
container on an Amazon EC2 Linux instance using a bind mount.

###### Note

Using the FSx for OpenZFS CSI Driver is not supported for file systems using the Intelligent-Tiering storage class.

###### Topics

- [Mounting your file system from an Amazon ECS container](#mount-openzfs-ecs-containers "#mount-openzfs-ecs-containers")

## Mounting your file system from an Amazon ECS container

You can access your Amazon FSx for OpenZFS file systems from an Amazon Elastic Container Service (Amazon ECS) Docker
container on an Amazon EC2 Linux instance by mounting volumes using a bind mount. For more information,
see [Bind mounts](../../../AmazonECS/latest/developerguide/bind-mounts.md "../../../AmazonECS/latest/developerguide/bind-mounts.md") in the _Amazon Elastic Container Service Developer Guide_.

###### To mount a volume on an Amazon ECS Linux container

1. Create an ECS cluster using the EC2 Linux + Networking cluster template for your Linux containers.
   For more information, see [Clusters](../../../AmazonECS/latest/developerguide/clusters.md "../../../AmazonECS/latest/developerguide/clusters.md") in the _Amazon ECS Developer Guide_.
2. Create a directory on the EC2 instance for mounting the volume as follows:

```
sudo mkdir /fsxopenzfs
```

3. Mount your FSx for OpenZFS volume on the Linux EC2 instance by either using a
   user-data script during instance launch, or by running the following
   commands:

```
sudo mount -t nfs -o nfsvers=`NFS_version` `file-system-dns-name`:/`volume-path` /`localpath`
```

The following example uses sample values in the mount command.

```
sudo mount -t nfs -o nfsvers=4.1 fs-01234567890abcdef1.fsx.us-east-1.amazonaws.com:/fsx/vol1 /fsxopenzfs
```

You can also use the file system's IP address instead of its DNS name.

```
sudo mount -t nfs -o nfsvers=4.1 198.51.100.1:/fsx/vol1 /fsxopenzfs
```

4. When creating your Amazon ECS task definitions, add the following
   `volumes` and `mountPoints` container properties
   in the JSON container definition. Replace the `sourcePath` with
   the mount point and directory in your FSx for OpenZFS file system.

```
{
    "volumes": [
        {
            "name": "openzfs-volume",
            "host": {
                "sourcePath": "`mountpoint`"
            }
        }
    ],
    "mountPoints": [
        {
            "containerPath": "`container_local_path`",
            "sourceVolume": "openzfs-volume"
        }
    ],
    .
    .
    .
}
```
