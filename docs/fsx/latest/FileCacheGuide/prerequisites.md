# Prerequisites

To perform this getting started exercise, you'll need the following:

- An AWS account with the permissions necessary to create an Amazon File Cache and an
  Amazon Elastic Compute Cloud (Amazon EC2) instance. For more information, see [Setting up](setting-up.md "setting-up.md").
- Each cache requires four IP addresses for the metadata servers (MDS) and
  one IP address for each storage server (OSS). Caches are provisioned with 2.4 TiB of
  storage per OSS.
- An Amazon EC2 instance running a supported Linux release in your virtual private cloud
  (VPC) based on the Amazon VPC service. You'll install the Lustre client on this Amazon EC2 instance,
  and then mount your cache on the Amazon EC2 instance. The Lustre client supports
  Amazon Linux, Amazon Linux 2, CentOS and Red Hat Enterprise Linux 7.9 and 8.4 through 8.6, Rocky Linux 8.4
  through 8.6, and Ubuntu 18.04, 20.04, and 22.04. For this getting started exercise,
  we'll use Ubuntu 22.04.

When creating your Amazon EC2 instance for this getting started exercise, keep the
following in mind:

    + We recommend that you create your instance in your default VPC.
    + We recommend that you use the default security group when creating your Amazon EC2
     instance.

- An Amazon S3 bucket storing the data for your workload to process. The Amazon S3 bucket will be
  the linked data repository for your cache.
