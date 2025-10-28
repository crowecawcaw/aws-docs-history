# Using Kubernetes Container Storage Interface

drivers

Kubernetes is an open-source system for automating deployment, scaling, and management of
containerized applications. In a Kubernetes environment, a container is similar to a VM, but
a container has relaxed isolation properties to share the Operating System (OS) among its
applications. Therefore, containers are considered to be more lightweight than VMs. Similar
to a VM, a container has its own filesystem, a share of allocated CPU, memory, process
space, and more. As they are decoupled from the underlying infrastructure, they are portable
across clouds and OS distributions. If you have a Kubernetes cluster, you can install and
configure Kubernetes Container Storage Interface (CSI) drivers across the instances in your
cluster to allow them to use an existing Amazon S3 File Gateway for storage.

After you install the CSI drivers for the type of file share that you want to use, you
must create one or more storage objects. Depending on the type of provisioning that you want
Kubernetes to use when your pods request storage, you must create either a single Kubernetes
`StorageClass` object, or both a `PersistentVolume` object
_and_ a `PersistentVolumeClaim` object to connect your
Kubernetes compute pods to your file share. For more information, refer to the Kubernetes
online documentation at [https://kubernetes.io/docs/concepts/storage/](https://kubernetes.io/docs/concepts/storage/ "https://kubernetes.io/docs/concepts/storage/").

###### Topics

- [Working with SMB CSI drivers](use-smb-csi.md "use-smb-csi.md")
- [Working with NFS CSI drivers](use-nfs-csi.md "use-nfs-csi.md")
