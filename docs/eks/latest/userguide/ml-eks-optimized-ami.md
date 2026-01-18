**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Use EKS-optimized accelerated AMIs for GPU instances

Amazon EKS supports EKS-optimized Amazon Linux and Bottlerocket AMIs for GPU instances. The EKS-optimized accelerated AMIs simplify running AI and ML workloads in EKS clusters by providing pre-built, validated operating system images for the accelerated Kubernetes stack. In addition to the core Kubernetes components that are included in the standard EKS-optimized AMIs, the EKS-optimized accelerated AMIs include the kernel modules and drivers required to run the NVIDIA GPU `G` and `P` EC2 instances, and the AWS GPU [Inferentia](https://aws.amazon.com/machine-learning/inferentia/ "https://aws.amazon.com/machine-learning/inferentia/") and [Trainium](https://aws.amazon.com/machine-learning/trainium/ "https://aws.amazon.com/machine-learning/trainium/") EC2 instances in EKS clusters.

The table below shows the supported GPU instance types for each EKS-optimized accelerated AMI variant. See the EKS-optimized [AL2023 releases](https://github.com/awslabs/amazon-eks-ami/releases "https://github.com/awslabs/amazon-eks-ami/releases") and [Bottlerocket releases](https://github.com/bottlerocket-os/bottlerocket/blob/develop/CHANGELOG.md "https://github.com/bottlerocket-os/bottlerocket/blob/develop/CHANGELOG.md") on GitHub for the latest updates to the AMI variants.

| EKS AMI variant                           | EC2 instance types                                                                      |
| ----------------------------------------- | --------------------------------------------------------------------------------------- |
| AL2023 x86_64 NVIDIA                      | p6-b300, p6-b200, p5, p5e, p5en, p4d, p4de, p3, p3dn, gr6, g6, g6e, g6f, gr6f, g5, g4dn |
| AL2023 ARM NVIDIA                         | p6e-gb200, g5g                                                                          |
| AL2023 x86_64 Neuron                      | inf1, inf2, trn1, trn2                                                                  |
| Bottlerocket x86_64 aws-k8s-nvidia        | p6-b300, p6-b200, p5, p5e, p5en, p4d, p4de, p3, p3dn, gr6, g6, g6e, g6f, gr6f, g5, g4dn |
| Bottlerocket aarch64/arm64 aws-k8s-nvidia | g5g                                                                                     |
| Bottlerocket x86_64 aws-k8s               | inf1, inf2, trn1, trn2                                                                  |

## EKS-optimized NVIDIA AMIs

By using the EKS-optimized NVIDIA AMIs, you agree to [NVIDIA’s Cloud End User License Agreement (EULA)](https://s3.amazonaws.com/EULA/NVidiaEULAforAWS.pdf "https://s3.amazonaws.com/EULA/NVidiaEULAforAWS.pdf").

To find the latest EKS-optimized NVIDIA AMIs, see [Retrieve recommended Amazon Linux AMI IDs](retrieve-ami-id.md "retrieve-ami-id.md") and [Retrieve recommended Bottlerocket AMI IDs](retrieve-ami-id-bottlerocket.md "retrieve-ami-id-bottlerocket.md").

When using Amazon Elastic Fabric Adaptor (EFA) with the EKS-optimized AL2023 or Bottlerocket NVIDIA AMIs, you must install the EFA device plugin separately. For more information, see [Run machine learning training on Amazon EKS with Elastic Fabric Adapter](node-efa.md "node-efa.md").

## EKS AL2023 NVIDIA AMIs

When using the [NVIDIA GPU operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/overview.html "https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/overview.html") with the EKS-optimized AL2023 NVIDIA AMIs, you must disable the operator installation of the driver and toolkit, as these are already included in the EKS AMIs. The EKS-optimized AL2023 NVIDIA AMIs do not include the NVIDIA Kubernetes device plugin or the NVIDIA DRA driver, and these must be installed separately. For more information, see [Install NVIDIA Kubernetes device plugin](ml-eks-k8s-device-plugin.md#eks-nvidia-device-plugin "ml-eks-k8s-device-plugin.md#eks-nvidia-device-plugin").

In addition to the standard EKS AMI components, the EKS-optimized AL2023 NVIDIA AMIs include the following components.

- NVIDIA driver
- NVIDIA CUDA user mode driver
- NVIDIA container toolkit
- NVIDIA fabric manager
- NVIDIA persistenced
- NVIDIA IMEX driver
- NVIDIA NVLink Subnet Manager
- EFA minimal (kernel module and rdma-core)

For details on the NVIDIA CUDA user mode driver and the CUDA runtime/libraries used within application containers, see the [NVIDIA documentation](https://docs.nvidia.com/deploy/cuda-compatibility/why-cuda-compatibility.html#why-cuda-compatibility "https://docs.nvidia.com/deploy/cuda-compatibility/why-cuda-compatibility.html#why-cuda-compatibility"). The CUDA version shown from `nvidia-smi` is the version of the NVIDIA CUDA user mode driver installed on the host, which must be compatible with the CUDA runtime/libraries used in application containers.

The EKS-optimized AL2023 NVIDIA AMIs support kernel 6.12 for Kubernetes versions 1.33 and above, and the NVIDIA driver 580 version for all Kubernetes versions. The NVIDIA 580 driver is required to use CUDA 13+.

See the EKS-optimized [AL2023 releases](https://github.com/awslabs/amazon-eks-ami/releases "https://github.com/awslabs/amazon-eks-ami/releases") on GitHub for details of the component versions included in the AMIs. See the EKS AL2023 NVIDIA AMI [installation script](https://github.com/awslabs/amazon-eks-ami/blob/main/templates/al2023/provisioners/install-nvidia-driver.sh "https://github.com/awslabs/amazon-eks-ami/blob/main/templates/al2023/provisioners/install-nvidia-driver.sh") and [kernel loading script](https://github.com/awslabs/amazon-eks-ami/blob/main/templates/al2023/runtime/gpu/nvidia-kmod-load.sh "https://github.com/awslabs/amazon-eks-ami/blob/main/templates/al2023/runtime/gpu/nvidia-kmod-load.sh") for details on how the EKS AMIs configure the NVIDIA dependencies. You can find the list of installed packages and their versions on a running EC2 instance with the `dnf list installed` command.

When building custom AMIs with the EKS-optimized AMIs as the base, it is not recommended or supported to run an operating system upgrade (ie. `dnf upgrade`) or upgrade any of the Kubernetes or GPU packages that are included in the EKS-optimized AMIs, as this risks breaking component compatibility. If you do upgrade the operating system or packages that are included in the EKS-optimized AMIs, it is recommended to thoroughly test in a development or staging environment before deploying to production.

When building custom AMIs for GPU instances, it is recommended to build separate custom AMIs for each instance type generation and family that you will run. The EKS-optimized accelerated AMIs selectively install drivers and packages at runtime based on the underlying instance type generation and family. For more information, see the EKS AMI scripts for [installation](https://github.com/awslabs/amazon-eks-ami/blob/main/templates/al2023/provisioners/install-nvidia-driver.sh "https://github.com/awslabs/amazon-eks-ami/blob/main/templates/al2023/provisioners/install-nvidia-driver.sh") and [runtime](https://github.com/awslabs/amazon-eks-ami/blob/main/templates/al2023/runtime/gpu/nvidia-kmod-load.sh "https://github.com/awslabs/amazon-eks-ami/blob/main/templates/al2023/runtime/gpu/nvidia-kmod-load.sh").

## EKS Bottlerocket NVIDIA AMIs

When using the [NVIDIA GPU operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/overview.html "https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/overview.html") with the EKS-optimized Bottlerocket NVIDIA AMIs, you must disable the operator installation of the driver, toolkit, and device plugin as these are already included in the EKS AMIs.

In addition to the standard EKS AMI components, the EKS-optimized Bottlerocket NVIDIA AMIs include the following components. The minimal dependencies for EFA (kernel module and rdma-core) are installed in all Bottlerocket variants.

- NVIDIA Kubernetes device plugin
- NVIDIA driver
- NVIDIA CUDA user mode driver
- NVIDIA container toolkit
- NVIDIA fabric manager
- NVIDIA persistenced
- NVIDIA IMEX driver
- NVIDIA NVLink Subnet Manager
- NVIDIA MIG manager

For details on the NVIDIA CUDA user mode driver and the CUDA runtime/libraries used within application containers, see the [NVIDIA documentation](https://docs.nvidia.com/deploy/cuda-compatibility/why-cuda-compatibility.html#why-cuda-compatibility "https://docs.nvidia.com/deploy/cuda-compatibility/why-cuda-compatibility.html#why-cuda-compatibility"). The CUDA version shown from `nvidia-smi` is the version of the NVIDIA CUDA user mode driver installed on the host, which must be compatible with the CUDA runtime/libraries used in application containers.

See the Bottlerocket Version Information in the [Bottlerocket documentation](https://bottlerocket.dev/en/ "https://bottlerocket.dev/en/") for details on the installed packages and their versions. The EKS-optimized Bottlerocket NVIDIA AMIs support kernel 6.12 for Kubernetes versions 1.33 and above, and the NVIDIA driver 580 version for Kubernetes versions 1.34 and above. The NVIDIA 580 driver is required to use CUDA 13+.

## EKS-optimized Neuron AMIs

For details on how to run training and inference workloads using Neuron with Amazon EKS, see the following references:

- [Containers - Kubernetes - Getting Started](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/kubernetes-getting-started.html "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/kubernetes-getting-started.html") in the AWS Neuron Documentation
- [Training example](https://github.com/aws-neuron/aws-neuron-eks-samples/blob/master/README.md#training "https://github.com/aws-neuron/aws-neuron-eks-samples/blob/master/README.md#training") in AWS Neuron EKS Samples on GitHub
- [Deploy ML inference workloads with Inferentia on Amazon EKS](inferentia-support.md "inferentia-support.md")

To find the latest EKS-optimized Neuron AMIs, see [Retrieve recommended Amazon Linux AMI IDs](retrieve-ami-id.md "retrieve-ami-id.md") and [Retrieve recommended Bottlerocket AMI IDs](retrieve-ami-id-bottlerocket.md "retrieve-ami-id-bottlerocket.md").

When using Amazon Elastic Fabric Adaptor (EFA) with the EKS-optimized AL2023 or Bottlerocket Neuron AMIs, you must install the EFA device plugin separately. For more information, see [Run machine learning training on Amazon EKS with Elastic Fabric Adapter](node-efa.md "node-efa.md").

## EKS AL2023 Neuron AMIs

The EKS-optimized AL2023 Neuron AMIs do not include the Neuron Kubernetes device plugin or the [Neuron Kubernetes scheduler extension](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/tutorials/k8s-neuron-scheduler.html "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/tutorials/k8s-neuron-scheduler.html"), and these must be installed separately. For more information, see [Install Neuron Kubernetes device plugin](ml-eks-k8s-device-plugin.md#eks-neuron-device-plugin "ml-eks-k8s-device-plugin.md#eks-neuron-device-plugin").

In addition to the standard EKS AMI components, the EKS-optimized AL2023 Neuron AMIs include the following components.

- Neuron driver (aws-neuronx-dkms)
- Neuron tools (aws-neuronx-tools)
- EFA minimal (kernel module and rdma-core)

See the EKS AL2023 Neuron AMI [installation script](https://github.com/awslabs/amazon-eks-ami/blob/main/templates/al2023/provisioners/install-neuron-driver.sh "https://github.com/awslabs/amazon-eks-ami/blob/main/templates/al2023/provisioners/install-neuron-driver.sh") for details on how the EKS AMIs configure the Neuron dependencies. See the EKS-optimized [AL2023 releases](https://github.com/awslabs/amazon-eks-ami/releases "https://github.com/awslabs/amazon-eks-ami/releases") on GitHub to see the component versions included in the AMIs. You can find the list of installed packages and their versions on a running EC2 instance with the `dnf list installed` command.

## EKS Bottlerocket Neuron AMIs

The standard Bottlerocket variants (aws-k8s) include the Neuron dependencies that are automatically detected and loaded when running on AWS Inferentia or Trainium EC2 instances.

The EKS-optimized Bottlerocket AMIs do not include the Neuron Kubernetes device plugin or the [Neuron Kubernetes scheduler extension](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/tutorials/k8s-neuron-scheduler.html "https://awsdocs-neuron.readthedocs-hosted.com/en/latest/containers/tutorials/k8s-neuron-scheduler.html"), and these must be installed separately. For more information, see [Install Neuron Kubernetes device plugin](ml-eks-k8s-device-plugin.md#eks-neuron-device-plugin "ml-eks-k8s-device-plugin.md#eks-neuron-device-plugin").

In addition to the standard EKS AMI components, the EKS-optimized Bottlerocket Neuron AMIs include the following components.

- Neuron driver (aws-neuronx-dkms)
- EFA minimal (kernel module and rdma-core)

When using the EKS-optimized Bottlerocket AMIs with Neuron instances, the following must be configured in the Bottlerocket user-data. This setting allows the container to take ownership of the mounted Neuron device based on the `runAsUser` and `runAsGroup` values provided in the workload specification. For more information on Neuron support in Bottlerocket, see the [Quickstart on EKS readme](https://github.com/bottlerocket-os/bottlerocket/blob/develop/QUICKSTART-EKS.md#neuron-support "https://github.com/bottlerocket-os/bottlerocket/blob/develop/QUICKSTART-EKS.md#neuron-support") on GitHub.

```
 [settings]
[settings.kubernetes]
device-ownership-from-security-context = true
```

See the [Bottlerocket kernel kit changelog](https://github.com/bottlerocket-os/bottlerocket-kernel-kit/blob/develop/CHANGELOG.md "https://github.com/bottlerocket-os/bottlerocket-kernel-kit/blob/develop/CHANGELOG.md") for information on the Neuron driver version included in the EKS-optimized Bottlerocket AMIs.
