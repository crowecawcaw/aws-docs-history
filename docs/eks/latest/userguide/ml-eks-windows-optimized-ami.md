**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Run GPU-accelerated containers (Windows on EC2 G-Series)

###### Important

The [Kubernetes Device Plugin for DirectX](https://github.com/TensorWorks/DirectX-Device-Plugins "https://github.com/TensorWorks/DirectX-Device-Plugins") by TensorWorks is a third-party tool that is not endorsed, supported, or maintained by AWS. AWS assumes no responsibility for the security, reliability, or performance of this plugin.

Learn how to run GPU-accelerated Windows container workloads on Amazon EKS (Elastic Kubernetes Service) using NVIDIA GPUs with the Kubernetes Device Plugin for DirectX by TensorWorks. For more information, see [Kubernetes Device Plugin for DirectX](https://github.com/TensorWorks/DirectX-Device-Plugins "https://github.com/TensorWorks/DirectX-Device-Plugins").

There are two main approaches to setting up GPU-acceleration for your Windows containers:

- **Option 1**: [Build a custom EKS Windows Optimized AMI](eks-custom-ami-windows.md "eks-custom-ami-windows.md") with the required GPU drivers pre-installed.
  - Use this approach when you need a consistent, pre-configured environment ready to run GPU-accelerated Windows containers, and you’re able to invest the additional effort to build and maintain the custom AMI.

- **Option 2**: Install the necessary GPU drivers on your EKS worker nodes after launching your instance.

      + Use this approach when you want a simpler setup process and don’t mind installing the GPU drivers on each new worker node. More suited to a development environment when you are evaluating or prototyping GPU-accelerated workloads.

  Both approaches can be leveraged using the steps detailed in this guide.

## Considerations

This guide provides steps to install and set up GPU-acceleration for your Windows containers using NVIDIA GPUs, NVIDIA GRID drivers, and the [Kubernetes Device Plugin for DirectX](https://github.com/TensorWorks/DirectX-Device-Plugins "https://github.com/TensorWorks/DirectX-Device-Plugins") by TensorWorks. The steps have been tested and verified to provide GPU-acceleration for your Windows container workloads on Amazon EKS. See [Known limitations](#ml-eks-windows-ami-known-limitations "#ml-eks-windows-ami-known-limitations") for more information on compatible drivers and device plugins. Before proceeding, note the following:

- Only G-family instance types with [NVIDIA GRID drivers](../../../AWSEC2/latest/UserGuide/install-nvidia-driver.md#nvidia-GRID-driver "../../../AWSEC2/latest/UserGuide/install-nvidia-driver.md#nvidia-GRID-driver") have been tested and verified to work with this guide. While other instance types and driver combinations may also be capable of running GPU-accelerated Windows containers, they may require additional configuration steps not covered in this guide.
- Only DirectX-based workloads have been tested and verified to work with this guide. While other GPU APIs like OpenGL, Vulkan, and OpenCL may potentially be compatible to run GPU-accelerated Windows containers, they may require additional configuration steps not covered in this guide.
- There are some known limitations to be aware of before running GPU-accelerated Windows containers. Please see the [Known limitations](#ml-eks-windows-ami-known-limitations "#ml-eks-windows-ami-known-limitations") section for more information.

## Prerequisites

To enable GPU acceleration for your Windows containers on Amazon EKS, you’ll need to prepare the following requirements before proceeding:

- Launch an Amazon EKS cluster with Kubernetes v1.27 or newer.
- Provision Windows nodes with Windows Server 2022 or newer.
- Provision Windows nodes in the G-family of instance types, such as [G4](https://aws.amazon.com/ec2/instance-types/g4/ "https://aws.amazon.com/ec2/instance-types/g4/") or [G5](https://aws.amazon.com/ec2/instance-types/g5/ "https://aws.amazon.com/ec2/instance-types/g5/").
- Provision Windows nodes with a container runtime with containerd `1.7.x` or `2.x.x`. (See [Retrieve Windows AMI version information](eks-ami-versions-windows.md "eks-ami-versions-windows.md") to verify the containerd version in your Amazon EKS Optimized AMI.)

## Install the GPU driver on each Windows Windows node

To install the NVIDIA GRID drivers on your EKS worker nodes, follow the steps outlined in [NVIDIA drivers for your Amazon EC2 instance](../../../AWSEC2/latest/UserGuide/install-nvidia-driver.md "../../../AWSEC2/latest/UserGuide/install-nvidia-driver.md").
Navigate to [Installation options - Option 3: GRID drivers](../../../AWSEC2/latest/UserGuide/install-nvidia-driver.md#nvidia-GRID-driver "../../../AWSEC2/latest/UserGuide/install-nvidia-driver.md#nvidia-GRID-driver") and follow the installation steps.

**Install for Windows Server Core**

For Windows Server Core, which doesn’t have a desktop experience, install NVIDIA GRID drivers silently by using the following commands:

```
$nvidiaInstallerFilePath = nvidia-driver-installer.exe # Replace with path to installer
$installerArguments = "-s -clean -noreboot -noeula"
Start-Process -FilePath $nvidiaInstallerFilePath -ArgumentList $installerArguments -Wait -NoNewWindow -PassThru
```

**Verify your installation**

Run the following PowerShell command to show diagnostic information about the GPUs on the instance:

```
nvidia-smi
```

This command displays the NVIDIA driver version, as well as information about the GPU hardware. Ensure that the output of this command matches the NVIDIA GRID driver version you expected to be installed.

## Deploy the GPU device plugin on each node

To enable discovery and exposure of the GPU resources to containers on your Windows nodes, you will need a device plugin.
Deploy the [DirectX Device Plugin](https://github.com/TensorWorks/DirectX-Device-Plugins "https://github.com/TensorWorks/DirectX-Device-Plugins") by Tensorworks on each worker node by running it as a DaemonSet in your EKS cluster.
Follow the installation guide specified in the [README.md](https://github.com/TensorWorks/DirectX-Device-Plugins/blob/main/README.md "https://github.com/TensorWorks/DirectX-Device-Plugins/blob/main/README.md"), which will entail the following steps. It is recommended to:

- Deploy the device plugin in the `kube-system` namespace.
- Set appropriate resource limits for the DaemonSet to ensure it does not consume excessive resources on your nodes.

###### Note

The device plugin DaemonSet will run on every node as a host process container with elevated privileges. It is recommended to implement RBAC controls to restrict access to this DaemonSet so only authorized users can execute privileged commands.

When running GPU-accelerated containers, the device plugin supports two modes:

- **Single-tenancy mode**: This mode dedicates all GPU resources to a single container on the instance. Install the device plugins with single-tenancy support using the following command. See README.md for more information.

```
kubectl apply -f "https://raw.githubusercontent.com/TensorWorks/directx-device-plugins/main/deployments/default-daemonsets.yml"
```

- **Multi-tenancy mode**: This mode allows sharing GPU resources among multiple containers on the instance. Install the device plugins with multi-tenancy support using the following command. See README.md for more information.

```
kubectl apply -f "https://raw.githubusercontent.com/TensorWorks/directx-device-plugins/main/deployments/multitenancy-inline.yml"
```

Alternatively, use a ConfigMap to specify the multi-tenancy.

```
kubectl apply -f "https://raw.githubusercontent.com/TensorWorks/directx-device-plugins/main/deployments/multitenancy-configmap.yml"
```

### Verifying the device plugin deployment

After you have deployed the device plugin, replace `<namespace>` and run the following command to verify the DirectX Device Plugin is running correctly on your all your Windows nodes.

```
kubectl get ds device-plugin-wddm -n <namespace>
```

### Verifying containers are ready for deployment

Once the device plugin DaemonSet is running on the GPU-powered Windows worker nodes, use the following command to verify that each node has allocatable GPUs. The corresponding number should match the number of DirectX devices on each node.

```
kubectl get nodes "-o=custom-columns=NAME:.metadata.name,DirectX:.status.allocatable.directx\.microsoft\.com/display"
```

## Running Windows containers with GPU-acceleration

Before launching your pods, specify the resource name `directx.microsoft.com/display` in `.spec.containers[].resources`.
This will indicate that your containers require GPU-enabled capabilities, and the `kube-scheduler` will attempt to place your pods on your pre-configured Windows node with available GPU resources.

As an example, see the sample command below which launches a `Job` to run Monte Carlo simulation to estimate the value of pi. This example is from the [Kubernetes Device Plugins for DirectX](https://github.com/TensorWorks/DirectX-Device-Plugins "https://github.com/TensorWorks/DirectX-Device-Plugins") GitHub repository, which has [multiple examples](https://github.com/TensorWorks/DirectX-Device-Plugins/tree/main/examples "https://github.com/TensorWorks/DirectX-Device-Plugins/tree/main/examples") to choose from that you can run to test your Windows node GPU capabilities.

```
cat <<EOF | kubectl apply -f -
apiVersion: batch/v1
kind: Job
metadata:
  name: example-cuda-montecarlo-wddm
spec:
  template:
    spec:
      containers:
      - name: example-cuda-montecarlo-wddm
        image: "index.docker.io/tensorworks/example-cuda-montecarlo:0.0.1"
        resources:
          limits:
            directx.microsoft.com/display: 1
      nodeSelector:
        "kubernetes.io/os": windows
      restartPolicy: Never
  backoffLimit: 0
EOF
```

## Known limitations

### All GPUs are usable

All the GPUs on the instance will be usable by each running container on the host, even when you request a specific number of GPUs for a given container. Additionally, the default behavior is that all containers running on the host will use the GPU with index 0, even if there are multiple GPUs available on the node. Thus, for multi-GPU tasks to operate correctly, you must explicitly designate the specific GPU device to be utilized within your application’s code.

The exact implementation to allocate a device to use for the application will depend on the programming language or framework you are using. For example, if you’re using CUDA programming, to select a specific GPU, you can explicitly specify the device to use in your application code by using the function [cudaSetDevice()](https://docs.nvidia.com/cuda/cuda-runtime-api/group_%5FCUDART%5F_DEVICE.html "https://docs.nvidia.com/cuda/cuda-runtime-api/group_%5FCUDART%5F_DEVICE.html").

The need to explicitly specify the device is due to a known issue affecting Windows containers. You can track the progress on resolving this issue in the [microsoft/Windows-Containers issue #333](https://github.com/microsoft/Windows-Containers/issues/333 "https://github.com/microsoft/Windows-Containers/issues/333").
The following table represents a visual representation and practical example of this GPU allocation behavior.

Consider a scenario whereby there is a single Windows node of EC2 instance type `g4dn.12xlarge`, which comes with four GPUs. Consider a scenario where three pods are launched on this instance. The table shows that regardless of the number of GPUs requested by each container, all three pods have access to all four GPUs on the instance, and by default will utilize the GPU with device index 0.

| Pod   | Requested GPUs | Actual GPU Access | Default GPU Usage | Available GPU Indices | Total Instance GPUs |
| ----- | -------------- | ----------------- | ----------------- | --------------------- | ------------------- |
| Pod 1 | 1 GPU          | All 4 GPUs        | GPU with index 0  | 0, 1, 2, 3            | 4                   |
| Pod 2 | 2 GPUs         | All 4 GPUs        | GPU with index 0  | 0, 1, 2, 3            | 4                   |
| Pod 3 | 1 GPU          | All 4 GPUs        | GPU with index 0  | 0, 1, 2, 3            | 4                   |

### Kubernetes device plugin support

NVIDIA’s official implementation of the [Kubernetes device plugin](https://github.com/NVIDIA/k8s-device-plugin "https://github.com/NVIDIA/k8s-device-plugin") does not support Windows. You can track the progress on adding official Windows support in the [NVIDIA/k8s-device-plugin issue #419](https://github.com/NVIDIA/k8s-device-plugin/issues/419 "https://github.com/NVIDIA/k8s-device-plugin/issues/419").

### GPU compute instance limitations

Depending on your AWS account configuration, you may have service limits on the number and types of Amazon EC2 GPU compute instances that you can launch. If you require additional capacity, you can [Request a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md").

### Must build a Windows GPU Optimized AMI

There is no EKS Windows GPU Optimized AMI or EC2 Image Builder managed component provided by Amazon EKS. You will need to follow the steps in this guide to build a custom EKS Windows Optimized AMI with the required GPU drivers pre-installed, or install the necessary GPU drivers on your EKS worker nodes after launching your instances.

### Inferentia and Trainium not supported

AWS
[Inferentia](https://aws.amazon.com/ai/machine-learning/inferentia/ "https://aws.amazon.com/ai/machine-learning/inferentia/") and AWS
[Trainium](https://aws.amazon.com/ai/machine-learning/trainium/ "https://aws.amazon.com/ai/machine-learning/trainium/") based workloads are not supported on Windows.
