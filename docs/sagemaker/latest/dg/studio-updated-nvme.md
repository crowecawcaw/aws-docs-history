# NVMe stores with Amazon SageMaker Studio

Amazon SageMaker Studio applications and their associated notebooks run on Amazon Elastic Compute Cloud (Amazon EC2)
instances. Some of the Amazon EC2 instance types, such as the `ml.m5d` instance
family, offer non-volatile memory express (NVMe) solid state drives (SSD) instance stores.
NVMe instance stores are local ephemeral disk stores that are physically connected to an
instance for fast temporary storage. Studio applications support NVMe instance stores
for supported instance types. For more information about instance types and their associated
NVMe store volumes, see the [Amazon Elastic Compute Cloud
Instance Type Details](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/"). This topic provides information about accessing and using
NVMe instance stores, as well as considerations when using NVMe instance stores with
Studio.

## Considerations

The following considerations apply when using NVMe instance stores with
Studio.

- An NVMe instance store is temporary storage. The data stored on the NVMe store
  is deleted when the instance is terminated, stopped, or hibernated. When using
  NVMe stores with Studio applications, the data on the NVMe instance store
  is lost whenever the application is deleted, restarted, or patched. We recommend
  that you back up valuable data to persistent storage solutions, such as Amazon Elastic Block Store,
  Amazon Elastic File System, or Amazon Simple Storage Service.
- Studio patches instances periodically to install new security updates.
  When an instance is patched, the instance is restarted. This restart results in
  the deletion of data stored in the NVMe instance store. We recommend that you
  frequently back up necessary data from the NVMe instance store to persistent
  storage solutions, such as Amazon Elastic Block Store, Amazon Elastic File System, or Amazon Simple Storage Service.
- The following Studio applications support using NVMe storage:
  - JupyterLab
  - Code Editor, based on Code-OSS, Visual Studio Code - Open Source
  - KernelGateway

## Access NVMe instance stores

When you select an instance type with attached NVMe instance stores to host a
Studio application, the NVMe instance store directory is mounted to the application
container at the following location:

```
/mnt/sagemaker-nvme
```

If an instance has more than 1 NVMe instance store attached to it, Studio creates
a striped logical volume that spans all of the local disks attached. Studio then
mounts this striped logical volume to the `/mnt/sagemaker-nvme` directory. As
a result, the directory storage size is the sum of all NVMe instance store volume sizes
attached to the instance.

If the `/mnt/sagemaker-nvme` directory does not exist, verify that the
instance type hosting your application has an attached NVMe instance store
volume.
