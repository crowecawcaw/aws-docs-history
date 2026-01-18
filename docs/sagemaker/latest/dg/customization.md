# Customize add-on

## Template

Templates are reusable workspace configurations that serve as admin-controlled
blueprints for workspace creation. They provide defaults for workspace configuration
values, and guardrails to control what data scientists can do. Templates exist at a
cluster level, and can be re-used across namespaces.

SageMaker Spaces creates two system templates as a starting point for data
scientists, one for Code Editor and one for JupyterLab. These system templates are
managed by the addon and cannot be editied directly. Instead, admins can create new
templates and set them as default.

## Task Governance

```
apiVersion: workspace.jupyter.org/v1alpha1
kind: WorkspaceTemplate
metadata:
  name: my-jupyter-template
  namespace: my-namespace
  labels:
    kueue.x-k8s.io/priority-class: <user-input>-priority
spec:
  displayName: "My Custom Jupyter Lab"
  description: "Custom Jupyter Lab with specific configurations"
  defaultImage: "public.ecr.aws/sagemaker/sagemaker-distribution:latest-cpu"
  allowedImages:
    - "public.ecr.aws/sagemaker/sagemaker-distribution:latest-cpu"
    - "public.ecr.aws/sagemaker/sagemaker-distribution:latest-gpu"
  defaultResources:
    requests:
      cpu: "1"
      memory: "4Gi"
    limits:
      cpu: "4"
      memory: "16Gi"
  primaryStorage:
    defaultSize: "10Gi"
    minSize: "5Gi"
    maxSize: "50Gi"
    defaultStorageClassName: "sagemaker-spaces-default-storage-class"
    defaultMountPath: "/home/sagemaker-user"
  defaultContainerConfig:
    command: ["/opt/amazon/sagemaker/workspace/bin/entrypoint-workspace-jupyterlab"]
  defaultPodSecurityContext:
    fsGroup: 1000
  defaultOwnershipType: "Public"
  defaultAccessStrategy:
    name: "hyperpod-access-strategy"
  allowSecondaryStorages: true
  appType: "jupyterlab"
```

## SMD / Custom images

Customers can configure image policies through templates by providing a default
image and a list of allowed images. Additionally, administrators can choose whether
to allow data scientists to bring their own custom images. The system defaults to
using the latest SageMaker Distribution, but if you wish to pin to a particular
version, you can specify the exact SMD version to use in a template.

Custom image requirements:

- `curl` if you want to use idle shutdown
- port 8888
- remote access

## Remote IDE Requirement

### VS Code version requirement

VS Code version [v1.90](https://code.visualstudio.com/updates/v1_90 "https://code.visualstudio.com/updates/v1_90") or greater is required. We recommend using the [latest stable version of VS
Code](https://code.visualstudio.com/updates "https://code.visualstudio.com/updates").

### Operating system requirements

You need one of the following operating systems to remotely connect to Studio
spaces:

- macOS 13+
- Windows 10
  - [Windows 10 support ends on October 14, 2025](https://support.microsoft.com/en-us/windows/windows-10-support-ends-on-october-14-2025-2ca8b313-1946-43d3-b55c-2b95b107f281 "https://support.microsoft.com/en-us/windows/windows-10-support-ends-on-october-14-2025-2ca8b313-1946-43d3-b55c-2b95b107f281")

- Windows 11
- Linux
- Install the official [Microsoft VS
  Code for Linux](https://code.visualstudio.com/docs/setup/linux "https://code.visualstudio.com/docs/setup/linux")
  - not an open-source version

### Local machine prerequisites

Before connecting your local Visual Studio Code to Studio spaces, ensure your
local machine has the required dependencies and network access.

###### Note

Environments with software installation restrictions may prevent users
from installing required dependencies. The AWS Toolkit for Visual Studio
Code automatically searches for these dependencies when initiating remote
connections and will prompt for installation if any are missing. Coordinate
with your IT department to ensure these components are available.

**Required local dependencies**

Your local machine must have the following components installed:

- **[**Remote-SSH
  Extension**](https://code.visualstudio.com/docs/remote/ssh "https://code.visualstudio.com/docs/remote/ssh")**
- — Standard VS Code Marketplace extension for remote development
- **[Session Manager plugin](../../../systems-manager/latest/userguide/session-manager-working-with-install-plugin.md "../../../systems-manager/latest/userguide/session-manager-working-with-install-plugin.md")** — Required for secure
  session management
- **SSH Client** — Standard component on
  most machines ([OpenSSH recommended for Windows](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse "https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse"))
- **[**VS Code CLI
  Command**](https://code.visualstudio.com/docs/configure/command-line "https://code.visualstudio.com/docs/configure/command-line")**
- Typically included with VS Code installation

**Platform-specific requirements**

- **Windows users** — PowerShell 5.1 or
  later is required for SSH terminal connections

**Network connectivity requirements**

Your local machine must have network access to [Session Manager
endpoints](../../../general/latest/gr/ssm.md "../../../general/latest/gr/ssm.md"). For example, in US East (N. Virginia) (us-east-1) these
can be:

- `ssm.us-east-1.amazonaws.com`
- `ssm.us-east-1.api.aws`
- `ssmmessages.us-east-1.amazonaws.com`
- `ec2messages.us-east-1.amazonaws.com`

### Image requirements

**SageMaker Distribution images**

When using SageMaker Distribution with remote access, use [SageMaker Distribution](sagemaker-distribution.md "sagemaker-distribution.md") version 2.7 or later.

**Custom images**

When you [Bring your own image (BYOI)](studio-updated-byoi.md "studio-updated-byoi.md") with remote access, ensure that you
follow the [custom image specifications](studio-updated-byoi-specs.md "studio-updated-byoi-specs.md") and ensure the following dependencies
are installed:

- `curl` or `wget` — Required for downloading AWS CLI components
- `unzip` — Required for extracting AWS CLI installation files
- `tar` — Required for archive extraction
- `gzip` — Required for compressed file handling

### Instance requirements

- **Memory** — 8GB or more
- Use instances with at least 8GB of memory. The following instance
  types are _not_ supported due to
  insufficient memory (less than 8GB):
  `ml.t3.medium`,
  `ml.c7i.large`,
  `ml.c6i.large`,
  `ml.c6id.large`, and
  `ml.c5.large`. For a more complete list of instance types, see the [Amazon EC2
  On-Demand Pricing page](https://aws.amazon.com/ec2/pricing/on-demand/ "https://aws.amazon.com/ec2/pricing/on-demand/")

## Optimizing Kubernetes Startup Time by Pre-Warming Container Images

Container image pulling performance has become a significant bottleneck for many
EKS customers, especially as AI/ML workloads rely on increasingly large container
images. Pulling and unpacking these large images typically takes several minutes the
first time they are used on each EKS node. This delay adds substantial latency when
launching SageMaker Spaces and directly impacts user experience—particularly in
environments where fast startup is essential, such as notebooks, interactive
development jobs.

Image pre-warming is a technique used to preload specific container images onto
every node in the EKS/HyperPod cluster before they are needed. Instead of waiting
for a pod to trigger the first pull of a large image, the cluster proactively
downloads and caches images across all nodes. This ensures that when workloads
launch, the required images are already available locally, eliminating long
cold-start delays. Image pre-warming improves SageMaker Spaces startup speed and
provides a more predictable and responsive experience for end users.

### Pre-Warming via DaemonSet

We recommend using a DaemonSet to preload images. A DaemonSet ensures that one
pod runs on every node in the cluster. Each container inside the DaemonSet pod
references an image you want to cache. When Kubernetes starts the pod, it
automatically pulls the images, warming the cache on each node.

The following example shows how to create a DaemonSet that preloads two GPU
images. Each container runs a lightweight `sleep infinity` command to
keep the pod active with minimal overhead.

```
cat <<EOF | kubectl apply -n "namespace_1" -f -
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: image-preload-ds
spec:
  selector:
    matchLabels:
      app: image-preloader
  template:
    metadata:
      labels:
        app: image-preloader
    spec:
      containers:
      - name: preloader-3-4-2
        image: public.ecr.aws/sagemaker/sagemaker-distribution:3.4.2-gpu
        command: ["sleep"]
        args: ["infinity"]
        resources:
          requests:
            cpu: 1m
            memory: 16Mi
          limits:
            cpu: 5m
            memory: 32Mi
      - name: preloader-3-3-2
        image: public.ecr.aws/sagemaker/sagemaker-distribution:3.3.2-gpu
        command: ["sleep"]
        args: ["infinity"]
        resources:
          requests:
            cpu: 1m
            memory: 16Mi
          limits:
            cpu: 5m
            memory: 32Mi
EOF
```

### How It Works

- Each container references one image.
- Kubernetes must download each image before starting the
  container.
- Once the pod is running on every node, the images are cached
  locally.
- Any workload using these images now starts much faster.

## Space default storage (EBS)

The system uses the EBS CSI driver by default to provision EBS storage volumes for
each workspace. SageMaker creates an EBS storage class for use with workspaces, and
administrators can customize the default and maximum size of these volumes using
template settings. For advanced users working with CLI tools, you can also customize
the storage class of the workspace, which allows users to leverage other storage
classes including configuring customer-managed KMS keys for their EBS
volumes.

Note that EBS volumes are bound to a particular AZ, which means workspaces can
only be scheduled on nodes in the same AZ as their storage volume. This can lead to
scheduling failures if cluster capacity exists but not in the correct AZ.

## Additional storage

SageMaker Spaces supports attaching additional storage volumes such as Amazon
EFS, FSx for Lustre, or S3 Mountpoint to your development spaces. This allows you
to access shared datasets, collaborate on projects, or use high-performance storage
for your workloads.

### Prerequisites

Before attaching additional storage to spaces, you must:

1. **Install the appropriate CSI driver
   add-on** via [EKS add-ons](../../../eks/latest/userguide/workloads-add-ons-available-eks.md "../../../eks/latest/userguide/workloads-add-ons-available-eks.md") (Amazon EFS CSI Driver, Amazon FSx for Lustre
   CSI Driver, or Mountpoint for Amazon S3 CSI Driver)
2. **Set up storage resources and
   PersistentVolumeClaims** following the CSI driver
   documentation for your specific storage type
3. **Ensure the PVC is available** in the
   same namespace where you plan to create your space

### Attaching storage to spaces

Once you have a PersistentVolumeClaim configured, you can attach it to a
space using either the HyperPod CLI or kubectl.

**HyperPod CLI**

```
hyp create hyp-space \
    --name my-space \
    --display-name "My Space with FSx" \
    --memory 8Gi \
    --volume name=shared-fsx,mountPath=/shared,persistentVolumeClaimName=my-fsx-pvc
```

**kubectl**

```
apiVersion: workspace.jupyter.org/v1alpha1
kind: Workspace
metadata:
  name: my-space
spec:
  displayName: "My Space with FSx"
  desiredStatus: Running
  volumes:
  - name: shared-fsx
    mountPath: /shared
    persistentVolumeClaimName: my-fsx-pvc
```

### Multiple volumes

You can attach multiple additional storage volumes to a single space by
specifying multiple `--volume` flags with the CLI or multiple entries in the
`volumes` array with kubectl.

**HyperPod CLI**

```
hyp create hyp-space \
    --name my-space \
    --display-name "My Space with Multiple Storage" \
    --memory 8Gi \
    --volume name=shared-efs,mountPath=/shared,persistentVolumeClaimName=my-efs-pvc \
    --volume name=datasets,mountPath=/datasets,persistentVolumeClaimName=my-s3-pvc
```

**kubectl**

```
apiVersion: workspace.jupyter.org/v1alpha1
kind: Workspace
metadata:
  name: my-space
spec:
  displayName: "My Space with Multiple Storage"
  desiredStatus: Running
  volumes:
  - name: shared-efs
    mountPath: /shared
    persistentVolumeClaimName: my-efs-pvc
  - name: datasets
    mountPath: /datasets
    persistentVolumeClaimName: my-s3-pvc
```

## Resource configuration

SageMaker Spaces allows you to configure compute resources for your development
environments, including CPU, memory, and GPU resources to match your workload
requirements.

### GPU configuration

SageMaker Spaces supports both whole GPU allocation and GPU partitioning using
NVIDIA Multi-Instance GPU (MIG) technology. This allows you to optimize GPU
utilization for different types of machine learning workloads.

#### Whole GPU allocation

**HyperPod CLI**

```
hyp create hyp-space \
    --name gpu-space \
    --display-name "GPU Development Space" \
    --image public.ecr.aws/sagemaker/sagemaker-distribution:latest-gpu \
    --memory 16Gi \
    --gpu 1 \
    --gpu-limit 1
```

**kubectl**

```
apiVersion: workspace.jupyter.org/v1alpha1
kind: Workspace
metadata:
  name: gpu-space
spec:
  displayName: "GPU Development Space"
  image: "public.ecr.aws/sagemaker/sagemaker-distribution:latest-gpu"
  desiredStatus: Running
  resources:
    requests:
      memory: "16Gi"
      nvidia.com/gpu: "1"
    limits:
      memory: "16Gi"
      nvidia.com/gpu: "1"
```

#### GPU partitioning (MIG)

GPU partitioning using NVIDIA Multi-Instance GPU (MIG) technology allows
you to partition a single GPU into smaller, isolated instances. Your
HyperPod cluster must have GPU nodes that support MIG and have MIG profiles
configured. For more information on setting up MIG on your HyperPod cluster,
see [GPU partitioning using NVIDIA MIG](sagemaker-hyperpod-eks-gpu-partitioning-setup.md "sagemaker-hyperpod-eks-gpu-partitioning-setup.md").

**HyperPod CLI**

```
hyp create hyp-space \
    --name mig-space \
    --display-name "MIG GPU Space" \
    --image public.ecr.aws/sagemaker/sagemaker-distribution:latest-gpu \
    --memory 8Gi \
    --accelerator-partition-type mig-3g.20gb \
    --accelerator-partition-count 1
```

**kubectl**

```
apiVersion: workspace.jupyter.org/v1alpha1
kind: Workspace
metadata:
  name: mig-space
spec:
  displayName: "MIG GPU Space"
  image: "public.ecr.aws/sagemaker/sagemaker-distribution:latest-gpu"
  desiredStatus: Running
  resources:
    requests:
      memory: "8Gi"
      nvidia.com/mig-3g.20gb: "1"
    limits:
      memory: "8Gi"
      nvidia.com/mig-3g.20gb: "1"
```

## Lifecycle

Lifecycle configuration provides startup scripts that run when a workspace is
created or started. These scripts allow administrators to customize the workspace
environment during startup. These are bash scripts with a maximum size of 1 KB. If
you need larger setup configuration, we recommend adding a script to the container
image and triggering the script from the lifecycle configuration.

We leverage Kubernetes container lifecycle hooks to provide this functionality
[https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/](https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/ "https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/").
Note that Kubernetes does not provide guarantees of when the startup script will be
run in relation to the entrypoint of the container.

## Idle shutdown

Configure automatic shutdown of idle workspaces to optimize resource usage.

### Idle shutdown

```
idleShutdown:
  enabled: true
  idleShutdownTimeoutMinutes: 30
  detection:
    httpGet:
      path: /api/idle
      port: 8888
      scheme: HTTP
```

### Parameters

**enabled** (boolean, required) - Enables or
disables idle shutdown for the workspace.

**idleShutdownTimeoutMinutes** (integer,
required) - Number of minutes of inactivity before the workspace shuts down.
Minimum value is 1.

**detection** (object, required) - Defines how to
detect workspace idle state.

**detection.httpGet** (object, optional) - HTTP
endpoint configuration for idle detection. Uses Kubernetes HTTPGetAction
specification.

- **path** - HTTP path to request
- **port** - Port number or name
- **scheme** - HTTP or HTTPS (default:
  HTTP)

### Configuration Locations

**Workspace Configuration**

Define idle shutdown directly in the workspace specification:

```
apiVersion: workspace.jupyter.org/v1alpha1
kind: Workspace
metadata:

      name: my-workspace
spec:
  displayName: "Development Workspace"
  image:
      jupyter/scipy-notebook:latest
  idleShutdown:
    enabled: true

      idleShutdownTimeoutMinutes: 30
    detection:
      httpGet:
        path:
      /api/idle
        port: 8888

```

**Template Configuration**

Define default idle shutdown behavior in a WorkspaceTemplate:

```
apiVersion: workspace.jupyter.org/v1alpha1
kind: WorkspaceTemplate
metadata:
  name: jupyter-template
spec:
  displayName: "Jupyter Template"
  defaultImage: jupyter/scipy-notebook:latest
  defaultIdleShutdown:
    enabled: true
    idleShutdownTimeoutMinutes: 30
    detection:
      httpGet:
        path: /api/idle
        port: 8888
  idleShutdownOverrides:
    allow: true
    minTimeoutMinutes: 60
    maxTimeoutMinutes: 240

```

### Template Inheritance and Overrides

Workspaces using a template automatically inherit the template's `defaultIdleShutdown` configuration. Workspaces can override this configuration if the template allows it.

**Override Policy**

Templates control override behavior through `idleShutdownOverrides`:

**allow** (boolean, default: true)- Whether
workspaces can override the default idle shutdown configuration.

**minTimeoutMinutes** (integer, optional)-
Minimum allowed timeout value for workspace overrides.

**maxTimeoutMinutes** (integer, optional)-
Maximum allowed timeout value for workspace overrides.

**Inheritance Example**

Workspace inherits template defaults:

```
apiVersion: workspace.jupyter.org/v1alpha1
kind: Workspace
metadata:
  name: my-workspace
spec:
  displayName: "My Workspace"
  templateRef:
    name: jupyter-template
  # Inherits defaultIdleShutdown from template

```

**Override Example**

Workspace overrides template defaults:

```
apiVersion: workspace.jupyter.org/v1alpha1
kind: Workspace
metadata:
  name: my-workspace
spec:
  displayName: "My Workspace"
  templateRef:
    name: jupyter-template
  idleShutdown:
    enabled: true
    idleShutdownTimeoutMinutes: 60  # Must be within template bounds
    detection:
      httpGet:
        path: /api/idle
        port: 8888

```

**Locked Configuration**

Prevent workspace overrides:

```
apiVersion: workspace.jupyter.org/v1alpha1
kind: WorkspaceTemplate
metadata:
  name: locked-template
spec:
  displayName: "Locked Template"
  defaultImage: jupyter/scipy-notebook:latest
  defaultIdleShutdown:
    enabled: true
    idleShutdownTimeoutMinutes: 30
    detection:
      httpGet:
        path: /api/idle
        port: 8888
  idleShutdownOverrides:
    allow: false  # Workspaces cannot override

```

### Behavior

When idle shutdown is enabled, the system periodically checks the workspace
for activity using the configured HTTP endpoint. If the endpoint indicates the
workspace is idle for the specified timeout duration, the workspace
automatically stops. You can manually restart the workspace when needed.

## Template updates

The client tools such as Kubectl or Hyperpod CLI and SDK can be used for managing
Spaces within the EKS cluster. Administrators can provision Space Templates for
default Space configurations, while Data Scientists can customize their integrated
development environments without needing to understand the underlying Kubernetes
complexity. For detailed usage instructions, please refer to the CLI and SDK
documentation at [https://sagemaker-hyperpod-cli.readthedocs.io/en/latest/index.html](https://sagemaker-hyperpod-cli.readthedocs.io/en/latest/index.html "https://sagemaker-hyperpod-cli.readthedocs.io/en/latest/index.html").

Administrators can perform CRUD operations on Space Templates, which serve as the
base configurations when creating a Space. Data Scientists can perform CRUD
operations on Spaces and override various parameters, including the Multi-Instance
GPU profiles for specific compute nodes. They can start, stop, and connect to the
Spaces via remote VSCode access and the Web UI. When a Space Template is updated,
any subsequently created Space will be configured with the settings in the updated
template. Compliance checks will be performed when existing Spaces are updated or
started. If any settings are out of bounds or mismatched, the Spaces will fail to
update or start.

## Using hyp cli and kubectl

User can perform CRUD on the templates with the Hyperpod CLI

```
### 1. Create a Space Template
hyp create hyp-space-template --file template.yaml

### 2. List Space Templates
hyp list hyp-space-template
hyp list hyp-space-template --output json

### 3. Describe a Space Template
hyp describe hyp-space-template --name my-template
hyp describe hyp-space-template --name my-template --output json

### 4. Update a Space Template
hyp update hyp-space-template --name my-template --file updated-template.yaml

### 5. Delete a Space Template
hyp delete hyp-space-template --name my-template
```

To create custom templates, you can use our system templates as a starting point.
This template will work for SMD-like images, however it can be customized based on
the images used by admins.

Example custom JupyterLab template:

```
apiVersion: workspace.jupyter.org/v1alpha1
kind: WorkspaceTemplate
metadata:
  name: my-jupyter-template
  namespace: my-namespace
spec:
  displayName: "My Custom Jupyter Lab"
  description: "Custom Jupyter Lab with specific configurations"
  defaultImage: "public.ecr.aws/sagemaker/sagemaker-distribution:latest-cpu"
  allowedImages:
    - "public.ecr.aws/sagemaker/sagemaker-distribution:latest-cpu"
    - "public.ecr.aws/sagemaker/sagemaker-distribution:latest-gpu"
  defaultResources:
    requests:
      cpu: "1"
      memory: "4Gi"
    limits:
      cpu: "4"
      memory: "16Gi"
  primaryStorage:
    defaultSize: "10Gi"
    minSize: "5Gi"
    maxSize: "50Gi"
    defaultStorageClassName: "sagemaker-spaces-default-storage-class"
    defaultMountPath: "/home/sagemaker-user"
  defaultContainerConfig:
    command: ["/opt/amazon/sagemaker/workspace/bin/entrypoint-workspace-jupyterlab"]
  defaultPodSecurityContext:
    fsGroup: 1000
  defaultOwnershipType: "Public"
  defaultAccessStrategy:
    name: "hyperpod-access-strategy"
  allowSecondaryStorages: true
  appType: "jupyterlab"
```

Example custom Code Editor template:

```
apiVersion: workspace.jupyter.org/v1alpha1
kind: WorkspaceTemplate
metadata:
  name: my-code-editor-template
  namespace: my-namespace
spec:
  displayName: "My Custom Code Editor"
  description: "Custom Code Editor with specific configurations"
  defaultImage: "public.ecr.aws/sagemaker/sagemaker-distribution:latest-cpu"
  allowedImages:
    - "public.ecr.aws/sagemaker/sagemaker-distribution:latest-cpu"
    - "public.ecr.aws/sagemaker/sagemaker-distribution:latest-gpu"
  defaultResources:
    requests:
      cpu: "1"
      memory: "4Gi"
    limits:
      cpu: "4"
      memory: "16Gi"
  primaryStorage:
    defaultSize: "10Gi"
    minSize: "5Gi"
    maxSize: "50Gi"
    defaultStorageClassName: "sagemaker-spaces-default-storage-class"
    defaultMountPath: "/home/sagemaker-user"
  defaultContainerConfig:
    command: ["/opt/amazon/sagemaker/workspace/bin/entrypoint-workspace-code-editor"]
  defaultPodSecurityContext:
    fsGroup: 1000
  defaultOwnershipType: "Public"
  defaultAccessStrategy:
    name: "hyperpod-access-strategy"
  allowSecondaryStorages: true
  appType: "code-editor"
```
