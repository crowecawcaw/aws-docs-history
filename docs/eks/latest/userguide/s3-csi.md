**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Access Amazon S3 objects with Mountpoint for Amazon S3 CSI driver

With the [Mountpoint for Amazon S3 Container Storage Interface (CSI) driver](https://github.com/awslabs/mountpoint-s3-csi-driver "https://github.com/awslabs/mountpoint-s3-csi-driver"), your Kubernetes applications can access Amazon S3 objects through a file system interface, achieving high aggregate throughput without changing any application code. Built on [Mountpoint for Amazon S3](https://github.com/awslabs/mountpoint-s3 "https://github.com/awslabs/mountpoint-s3"), the CSI driver presents an Amazon S3 bucket as a volume that can be accessed by containers in Amazon EKS and self-managed Kubernetes clusters.

## Considerations

- The Mountpoint for Amazon S3 CSI driver isn’t presently compatible with Windows-based container images.
- The Mountpoint for Amazon S3 CSI driver isn’t presently compatible with Amazon EKS Hybrid Nodes.
- The Mountpoint for Amazon S3 CSI driver doesn’t support AWS Fargate. However, containers that are running in Amazon EC2 (either with Amazon EKS or a custom Kubernetes installation) are supported.
- The Mountpoint for Amazon S3 CSI driver supports only static provisioning. Dynamic provisioning, or creation of new buckets, isn’t supported.

###### Note

Static provisioning refers to using an existing Amazon S3 bucket that is specified as the `bucketName` in the `volumeAttributes` in the `PersistentVolume` object. For more information, see [Static Provisioning](https://github.com/awslabs/mountpoint-s3-csi-driver/blob/main/examples/kubernetes/static_provisioning/README.md "https://github.com/awslabs/mountpoint-s3-csi-driver/blob/main/examples/kubernetes/static_provisioning/README.md") on GitHub.

- Volumes mounted with the Mountpoint for Amazon S3 CSI driver don’t support all POSIX file-system features. For details about file-system behavior, see [Mountpoint for Amazon S3 file system behavior](https://github.com/awslabs/mountpoint-s3/blob/main/doc/SEMANTICS.md "https://github.com/awslabs/mountpoint-s3/blob/main/doc/SEMANTICS.md") on GitHub.

For details on deploying the driver, see [Deploy the Mountpoint for Amazon S3 driver](s3-csi-create.md "s3-csi-create.md"). For details on removing the driver, see [Remove the Mountpoint for Amazon S3 Amazon EKS add-on](removing-s3-csi-eks-add-on.md "removing-s3-csi-eks-add-on.md").
