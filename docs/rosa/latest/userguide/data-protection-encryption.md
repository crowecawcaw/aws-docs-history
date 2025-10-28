# Protecting data using encryption

Data protection refers to protecting data while in transit (as it travels to and from ROSA) and at rest (while it is stored on disks in AWS data centers).

Red Hat OpenShift Service on AWS provides secure access to Amazon Elastic Block Store (Amazon EBS) storage volumes attached to Amazon EC2 instances for ROSA control plane, infrastructure, and worker nodes, as well as Kubernetes persistent volumes for persistent storage.
ROSA encrypts volume data at rest and in transit, and uses AWS Key Management Service (AWS KMS) to help protect your encrypted data.
The service uses Amazon S3 for container image registry storage, which is encrypted at rest by default.

###### Important

Because ROSA is a managed service, AWS and Red Hat manage the infrastructure that ROSA uses.
Customers should not attempt to manually shut down the Amazon EC2 instances that ROSA uses from the AWS console or CLI.
This action can lead to customer data loss.

## Data encryption for Amazon EBS-backed storage volumes

Red Hat OpenShift Service on AWS uses the Kubernetes persistent volume (PV) framework to allow cluster administrators to provision a cluster with persistent storage.
Persistent volumes, as well as the control plane, infrastructure, and worker nodes, are backed by Amazon Elastic Block Store (Amazon EBS) storage volumes attached to Amazon EC2 instances.

For ROSA persistent volumes and nodes backed by Amazon EBS, encryption operations occur on the servers that host EC2 instances, ensuring the security of both data at rest and data in transit between an instance and its attached storage.
For more information, see [Amazon EBS encryption](../../../ebs/latest/userguide/ebs-encryption.md "../../../ebs/latest/userguide/ebs-encryption.md") in the _Amazon EC2 User Guide_.

### Data encryption for the Amazon EBS CSI driver and Amazon EFS CSI driver

ROSA defaults to using the Amazon EBS CSI driver to provision Amazon EBS storage.
The Amazon EBS CSI driver and Amazon EBS CSI Driver Operator are installed on the cluster by default in the `openshift-cluster-csi-drivers` namespace.
The Amazon EBS CSI driver and operator allow you to dynamically provision persistent volumes and create volume snapshots.

ROSA is also capable of provisioning persistent volumes using the Amazon EFS CSI driver and Amazon EFS CSI Driver Operator.
The Amazon EFS driver and operator also allow you to share file system data between pods or with other applications within or outside of Kubernetes.

Volume data is secured in transit for both the Amazon EBS CSI driver and Amazon EFS CSI driver.
For more information, see [Using Container Storage Interface (CSI)](https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/storage/using-container-storage-interface-csi "https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/storage/using-container-storage-interface-csi") in the Red Hat documentation.

###### Important

When dynamically provisioning ROSA persistent volumes using the Amazon EFS CSI driver, Amazon EFS considers the user ID, group ID (GID), and secondary group IDs of the access point when evaluating file system permissions.
Amazon EFS replaces the user and group IDs on files with the user and group IDs on the access point and ignores NFS client IDs.
As a result, Amazon EFS silently ignores `fsGroup` settings.
ROSA is not able to replace the GIDs of files by using `fsGroup`.
Any pod that can access a mounted Amazon EFS access point can access any file on the volume.
For more information, see [Working with Amazon EFS access points](../../../efs/latest/ug/efs-access-points.md "../../../efs/latest/ug/efs-access-points.md") in the _Amazon EFS User Guide_.

### etcd encryption

ROSA provides the option to enable encryption of `etcd` key values within the `etcd` volume during cluster creation, adding an additional layer of encryption.
Once `etcd` is encrypted, you will incur approximately 20% additional performance overhead.
We recommend that you enable `etcd` encryption only if you specifically require it for your use case.
For more information, see [etcd encryption](https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/introduction_to_rosa/policies-and-service-definition#rosa-sdpolicy-etcd-encryption_rosa-service-definition "https://access.redhat.com/documentation/en-us/red_hat_openshift_service_on_aws/4/html/introduction_to_rosa/policies-and-service-definition#rosa-sdpolicy-etcd-encryption_rosa-service-definition") in the ROSA service definition.

### Key management

ROSA uses KMS keys to securely manage control plane, infrastructure, and worker data volumes and persistent volumes for customer applications.
During cluster creation, you have the choice of using the default AWS managed KMS key provided by Amazon EBS, or specifying your own customer managed key.
For more information, see [Data encryption using KMS](data-protection-key-management.md "data-protection-key-management.md").

## Data encryption for the built-in image registry

ROSA provides a built-in container image registry to store, retrieve, and share container images via Amazon S3 bucket storage.
The registry is configured and managed by the OpenShift Image Registry Operator.
It provides an out-of-the-box solution for users to manage the images that run their workloads, and runs on top of the existing cluster infrastructure.
For more information, see [Registry](https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/registry/index "https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/registry/index") in the Red Hat documentation.

ROSA offers public and private image registries.
For enterprise applications, we recommend using a private registry to protect your images from being used by unauthorized users.
To protect your registry’s data at rest, ROSA uses server-side encryption by default with Amazon S3 managed keys (SSE-S3).
This does not require any action on your part, and is offered at no additional charge.
For more information, see [Protecting data using server-side encryption with Amazon S3 managed encryption keys (SSE-S3)](../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md "../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md") in the _Amazon S3 User Guide_.

ROSA uses Transport Layer Security (TLS) protocol to secure data in transit to and from the image registry.
For more information, see [Registry](https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/registry/index "https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/registry/index") in the Red Hat documentation.

## Internetwork traffic privacy

Red Hat OpenShift Service on AWS uses Amazon Virtual Private Cloud (Amazon VPC) to create boundaries between resources in your ROSA cluster and control traffic between them, your on-premises network, and the internet.
For more information about Amazon VPC security, see [Internetwork traffic privacy in Amazon VPC](../../../vpc/latest/userguide/VPC_Security.md "../../../vpc/latest/userguide/VPC_Security.md") in the _Amazon VPC User Guide_.

Within the VPC, you can configure your ROSA clusters to use an HTTP or HTTPS proxy server to deny direct internet access.
If you are a cluster administrator, you can also define network policies at the pod level that restrict internetwork traffic to pods in your ROSA cluster.
For more information, see [Infrastructure security in ROSA](infrastructure-security.md "infrastructure-security.md").
