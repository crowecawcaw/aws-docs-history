# Setting up AWS ParallelCluster

The following topics describe how to set up AWS ParallelCluster. You will learn how to install
the necessary tools and how to use them, how to implement and manage multiple user access to
clusters, and the best practices.

###### Topics

- [Prerequisites](#prerequisites "#prerequisites")
- [Installing the AWS ParallelCluster command line interface (CLI)](install-v3-parallelcluster.md "install-v3-parallelcluster.md")
- [Steps to take after installation](install-v3-after-install.md "install-v3-after-install.md")
- [Installing the PCUI](install-pcui-v3.md "install-pcui-v3.md")
- [Getting started with AWS ParallelCluster](getting-started-v3.md "getting-started-v3.md")
- [Multiple user access to clusters](multi-user-v3.md "multi-user-v3.md")
- [Best practices](best-practices-v3.md "best-practices-v3.md")
- [Moving from AWS ParallelCluster 2.x to 3.x](moving-from-v2-to-v3.md "moving-from-v2-to-v3.md")

## Prerequisites

Before you can start setting up and using AWS ParallelCluster, make sure that you've completed the following prerequisites.

### Setting up an AWS account

Set up an AWS account to use AWS ParallelCluster.

#### Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

### Create a key pair

To deploy clusters, AWS ParallelCluster launches Amazon EC2 instances to create the cluster head node and compute nodes. To perform cluster tasks,
such as running and monitoring jobs, or managing users, you must be able to access the cluster head node. To verify you can access the head node
instance using SSH, you must use an Amazon EC2 key pair. To learn how to create a key pair, see [Create a key pair](../../../AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.md#create-a-key-pair "../../../AWSEC2/latest/UserGuide/get-set-up-for-amazon-ec2.md#create-a-key-pair") in the _Amazon Elastic Compute Cloud_
User Guide for Linux Instances.
