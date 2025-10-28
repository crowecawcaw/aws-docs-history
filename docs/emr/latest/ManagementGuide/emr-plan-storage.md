# Instance storage options and behavior in Amazon EMR

## Overview

Instance store and Amazon EBS volume storage is used for HDFS data and for buffers, caches,
scratch data, and other temporary content that some applications might "spill" to the
local file system.

Amazon EBS works differently within Amazon EMR than it does with regular Amazon EC2 instances. Amazon EBS
volumes attached to Amazon EMR clusters are ephemeral: the volumes are deleted upon cluster
and instance termination (for example, when shrinking instance groups), so you shouldn't
expect data to persist. Although the data is ephemeral, it is possible that data in HDFS
could be replicated depending on the number and specialization of nodes in the cluster.
When you add Amazon EBS storage volumes, these are mounted as additional volumes. They are
not a part of the boot volume. YARN is configured to use all the additional volumes, but
you are responsible for allocating the additional volumes as local storage (for local
log files, for example).

## Considerations

Keep in mind these additional considerations when you use Amazon EBS with
EMR clusters:

- You can't snapshot an Amazon EBS volume and then restore it within Amazon EMR. To create
  reusable custom configurations, use a custom AMI (available in Amazon EMR version
  5.7.0 and later). For more information, see [Using a custom AMI to provide more flexibility for Amazon EMR cluster configuration](emr-custom-ami.md "emr-custom-ami.md").
- An encrypted Amazon EBS root device volume is supported only when using a custom
  AMI. For more information, see [Creating a custom AMI with an encrypted
  Amazon EBS root device volume](emr-custom-ami.md#emr-custom-ami-encrypted "emr-custom-ami.md#emr-custom-ami-encrypted").
- If you apply tags using the Amazon EMR API, those operations are applied to EBS
  volumes.
- There is a limit of 25 volumes per instance.
- The Amazon EBS volumes on core nodes cannot be less than 5 GB.
- Amazon EBS has a fixed limit of 2,500 EBS volumes per instance launch request. This limit also applies to
  Amazon EMR on EC2 clusters. We recommend that you launch clusters with the total number of EBS volumes within this limit, and then
  manually scale up the cluster or with Amazon EMR managed scaling as needed. To learn more about the EBS volume limit,
  see [Service quotas](../../../general/latest/gr/ebs-service.md#limits_ebs:~:text=Amazon%20EBS%20has,exceeding%20the%20limit. "../../../general/latest/gr/ebs-service.md#limits_ebs:~:text=Amazon%20EBS%20has,exceeding%20the%20limit.").

## Default Amazon EBS storage for

instances

For EC2 instances that have EBS-only storage, Amazon EMR allocates Amazon EBS gp2 or gp3 storage
volumes to instances. When you create a cluster with Amazon EMR releases 5.22.0 and higher,
the default amount of Amazon EBS storage increases relative to the size of the
instance.

We split any increased storage across multiple volumes. This gives increased IOPS
performance and, in turn, increased performance for some standardized workloads. If you
want to use a different Amazon EBS instance storage configuration, you can specify this when
you create an EMR cluster or add nodes to an existing cluster. You can use Amazon EBS gp2
or gp3 volumes as root volumes, and add gp2 or gp3 volumes as additional volumes. For
more information, see [Specifying additional EBS
storage volumes](#emr-plan-storage-additional-ebs-volumes "#emr-plan-storage-additional-ebs-volumes").

The following table identifies the default number of Amazon EBS gp2 storage volumes, sizes,
and total sizes per instance type. For information about gp2 volumes compared to gp3,
see [Comparing Amazon EBS volume types gp2
and gp3](emr-plan-storage-compare-volume-types.md "emr-plan-storage-compare-volume-types.md").

Default Amazon EBS gp2 storage volumes and size by instance type for Amazon EMR 5.22.0 and
higher| Instance size | Number of volumes | Volume size (GiB) | Total size (GiB) |
| --- | --- | --- | --- |
| \*.large | 1 | 32 | 32 |
| \*.xlarge | 2 | 32 | 64 |
| \*.2xlarge | 4 | 32 | 128 |
| \*.4xlarge | 4 | 64 | 256 |
| \*.8xlarge | 4 | 128 | 512 |
| \*.9xlarge | 4 | 144 | 576 |
| \*.10xlarge | 4 | 160 | 640 |
| \*.12xlarge | 4 | 192 | 768 |
| \*.16xlarge | 4 | 256 | 1024 |
| \*.18xlarge | 4 | 288 | 1152 |
| \*.24xlarge | 4 | 384 | 1536 | ## Default Amazon EBS root volume for instances With Amazon EMR releases 6.15 and higher, Amazon EMR automatically attaches an Amazon EBS General Purpose SSD (gp3) as the root device for its AMIs to enhance performance. With earlier releases, Amazon EMR attaches EBS General Purpose SSD (gp2) as the root device.
| | 6.15 and higher | 6.14 and lower | | --- | --- | --- |
| Default root volume type | <br>• gp3 | <br>• gp2 | | Default size | <br>• 15 GiB <br>• (configurable)
| <br>• 6.10 and higher = 15 GiB <br>• 6.9 and lower = 10 GiB <br>• (configurable) | | Default IOPS | <br>• 3000 <br>• (configurable) | |
| Default throughput | <br>• 125 MiB/s <br>• (configurable) | | For information on how to customize the Amazon EBS root device volume, see [Specifying additional EBS storage volumes](#emr-plan-storage-additional-ebs-volumes "#emr-plan-storage-additional-ebs-volumes"). ## Specifying additional EBS storage volumes When you configure instance types in Amazon EMR, you can specify additional EBS volumes to add capacity beyond the instance store (if present) and the default EBS volume. Amazon EBS provides the following volume types: General Purpose (SSD), Provisioned IOPS (SSD), Throughput Optimized (HDD), Cold (HDD), and Magnetic. They differ in performance characteristics and price, so you can tailor your storage to the analytic and business needs of your applications. For example, some applications might need to spill to disk while others can safely work in-memory or with Amazon S3. You can only attach Amazon EBS volumes to instances at cluster startup time and when you add an extra task node instance group. If an instance in an Amazon EMR cluster fails, then both the instance and attached Amazon EBS volumes are replaced with new volumes. Consequently, if you manually detach an Amazon EBS volume, Amazon EMR treats that as a failure and replaces both instance storage (if applicable) and the volume stores. Amazon EMR doesn’t allow you to modify your volume type from gp2 to gp3 for an existing EMR cluster. To use gp3 for your workloads, launch a new EMR cluster. In addition, we don't recommend that you update the throughput and IOPS on a cluster that is in use or that is being provisioned, because Amazon EMR uses the throughput and IOPS values you specify at cluster launch time for any new instance that it adds during cluster scale-up. For more information, see [Comparing Amazon EBS volume types gp2 and gp3](emr-plan-storage-compare-volume-types.md "emr-plan-storage-compare-volume-types.md") and [Selecting IOPS and throughput when migrating to gp3 Amazon EBS volume types](emr-plan-storage-gp3-migration-selection.md "emr-plan-storage-gp3-migration-selection.md"). ###### Important To use a gp3 volume with your EMR cluster, you must launch a new cluster.
