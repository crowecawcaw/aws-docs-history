**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Build a custom EKS-optimized Amazon Linux AMI

###### Warning

Amazon EKS stopped publishing EKS-optimized Amazon Linux 2 (AL2) AMIs on November 26, 2025. AL2023 and Bottlerocket based AMIs for Amazon EKS are available for all supported Kubernetes versions including 1.33 and higher.

Amazon EKS provides open-source build scripts in the [Amazon EKS AMI Build Specification](https://github.com/awslabs/amazon-eks-ami "https://github.com/awslabs/amazon-eks-ami") repository that you can use to view the configurations for `kubelet`, the runtime, the AWS IAM Authenticator for Kubernetes, and build your own AL-based AMI from scratch.

This repository contains the specialized [bootstrap script for AL2](https://github.com/awslabs/amazon-eks-ami/blob/main/templates/al2/runtime/bootstrap.sh "https://github.com/awslabs/amazon-eks-ami/blob/main/templates/al2/runtime/bootstrap.sh") and [nodeadm tool for AL2023](https://awslabs.github.io/amazon-eks-ami/nodeadm/ "https://awslabs.github.io/amazon-eks-ami/nodeadm/") that runs at boot time. These scripts configure your instance’s certificate data, control plane endpoint, cluster name, and more. The scripts are considered the source of truth for Amazon EKS-optimized AMI builds, so you can follow the GitHub repository to monitor changes to our AMIs.

When building custom AMIs with the EKS-optimized AMIs as the base, it is not recommended or supported to run an operating system upgrade (ie. `dnf upgrade`) or upgrade any of the Kubernetes or GPU packages that are included in the EKS-optimized AMIs, as this risks breaking component compatibility. If you do upgrade the operating system or packages that are included in the EKS-optimized AMIs, it is recommended to thoroughly test in a development or staging environment before deploying to production.

When building custom AMIs for GPU instances, it is recommended to build separate custom AMIs for each instance type generation and family that you will run. The EKS-optimized accelerated AMIs selectively install drivers and packages at runtime based on the underlying instance type generation and family. For more information, see the EKS AMI scripts for [installation](https://github.com/awslabs/amazon-eks-ami/blob/main/templates/al2023/provisioners/install-nvidia-driver.sh "https://github.com/awslabs/amazon-eks-ami/blob/main/templates/al2023/provisioners/install-nvidia-driver.sh") and [runtime](https://github.com/awslabs/amazon-eks-ami/blob/main/templates/al2023/runtime/gpu/nvidia-kmod-load.sh "https://github.com/awslabs/amazon-eks-ami/blob/main/templates/al2023/runtime/gpu/nvidia-kmod-load.sh").

## Prerequisites

- [Install the AWS CLI](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md")
- [Install HashiCorp Packer v1.9.4+](https://developer.hashicorp.com/packer/downloads "https://developer.hashicorp.com/packer/downloads")
- [Install GNU Make](https://www.gnu.org/software/make/ "https://www.gnu.org/software/make/")

## Quickstart

This quickstart shows you the commands to create a custom AMI in your AWS account. To learn more about the configurations available to customize your AMI, see the template variables on the [Amazon Linux 2023](https://awslabs.github.io/amazon-eks-ami/usage/al2023/ "https://awslabs.github.io/amazon-eks-ami/usage/al2023/") page.

### Prerequisites

Install the required [Amazon plugin](https://developer.hashicorp.com/packer/integrations/hashicorp/amazon "https://developer.hashicorp.com/packer/integrations/hashicorp/amazon"). For example:

```
packer plugins install github.com/hashicorp/amazon
```

### Step 1. Setup your environment

Clone or fork the official Amazon EKS AMI repository. For example:

```
git clone https://github.com/awslabs/amazon-eks-ami.git
cd amazon-eks-ami
```

Verify that Packer is installed:

```
packer --version
```

### Step 2. Create a custom AMI

The following are example commands for various custom AMIs.

**Basic NVIDIA AL2 AMI:**

```
make k8s=1.31 os_distro=al2 \
  enable_accelerator=nvidia \
  nvidia_driver_major_version=560 \
  enable_efa=true
```

**Basic NVIDIA AL2023 AMI:**

```
make k8s=1.31 os_distro=al2023 \
  enable_accelerator=nvidia \
  nvidia_driver_major_version=560 \
  enable_efa=true
```

**STIG-Compliant Neuron AL2023 AMI:**

```
make k8s=1.31 os_distro=al2023 \
  enable_accelerator=neuron \
  enable_fips=true \
  source_ami_id=ami-0abcd1234efgh5678 \
  kms_key_id=alias/aws-stig
```

After you run these commands, Packer will do the following: \* Launch a temporary Amazon EC2 instance. \* Install Kubernetes components, drivers, and configurations. \* Create the AMI in your AWS account.

The expected output should look like this:

```
==> Wait completed after 8 minutes 42 seconds

==> Builds finished. The artifacts of successful builds are:
--> amazon-ebs: AMIs were created:
us-west-2: ami-0e139a4b1a7a9a3e9

--> amazon-ebs: AMIs were created:
us-west-2: ami-0e139a4b1a7a9a3e9

--> amazon-ebs: AMIs were created:
us-west-2: ami-0e139a4b1a7a9a3e9
```

### Step 3. View default values

To view default values and additional options, run the following command:

```
make help
```
