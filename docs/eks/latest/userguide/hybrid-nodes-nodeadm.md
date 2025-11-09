**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Hybrid nodes `nodeadm` reference

The Amazon EKS Hybrid Nodes CLI (`nodeadm`) simplifies the installation, configuration, registration, and uninstallation of the hybrid nodes components. You can include `nodeadm` in your operating system images to automate hybrid node bootstrap, see [Prepare operating system for hybrid nodes](hybrid-nodes-os.md "hybrid-nodes-os.md") for more information.

The `nodeadm` version for hybrid nodes differs from the `nodeadm` version used for bootstrapping Amazon EC2 instances as nodes in Amazon EKS clusters. Follow the documentation and references for the appropriate `nodeadm` version. This documentation page is for the hybrid nodes `nodeadm` version.

The source code for the hybrid nodes `nodeadm` is published in the [https://github.com/aws/eks-hybrid](https://github.com/aws/eks-hybrid "https://github.com/aws/eks-hybrid")
GitHub repository.

###### Important

You must run `nodeadm` with a user that has root/sudo privileges.

## Download `nodeadm`

The hybrid nodes version of `nodeadm` is hosted in Amazon S3 fronted by Amazon CloudFront. To install `nodeadm` on each on-premises host, you can run the following command from your on-premises hosts.

**For x86_64 hosts**

```
curl -OL 'https://hybrid-assets.eks.amazonaws.com/releases/latest/bin/linux/amd64/nodeadm'
```

**For ARM hosts**

```
curl -OL 'https://hybrid-assets.eks.amazonaws.com/releases/latest/bin/linux/arm64/nodeadm'
```

Add executable file permission to the downloaded binary on each host.

```
chmod +x nodeadm
```

## `nodeadm install`

The `nodeadm install` command is used to install the artifacts and dependencies required to run and join hybrid nodes to an Amazon EKS cluster. The `nodeadm install` command can be run individually on each hybrid node or can be run during image build pipelines to preinstall the hybrid nodes dependencies in operating system images.

**Usage**

```
nodeadm install [KUBERNETES_VERSION] [flags]
```

**Positional Arguments**

(Required) `KUBERNETES_VERSION` The major.minor version of EKS Kubernetes to install, for example `1.32`

**Flags**

| Name                             | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-p`,<br>`--credential-provider` | TRUE     | Credential provider to install. Supported values are `iam-ra` and `ssm`. See [Prepare credentials for hybrid nodes](hybrid-nodes-creds.md "hybrid-nodes-creds.md") for more information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `-s`,<br>`--containerd-source`   | FALSE    | Source for `containerd`. `nodeadm` supports installing `containerd` from the OS distro, Docker packages, and skipping `containerd` install.<br>**Values**<br>`distro`<br>• This is the default value. `nodeadm` will install the latest `containerd` package distributed by the node OS that is compatible with the EKS Kubernetes version. `distro` is not a supported value for Red Hat Enterprise Linux (RHEL) operating systems.<br>`docker`<br>• `nodeadm` will install the latest `containerd` package built and distributed by Docker that is compatible with the EKS Kubernetes version. `docker` is not a supported value for Amazon Linux 2023.<br>`none`<br>• `nodeadm` will not install `containerd` package. You must manually install `containerd` before running `nodeadm init`. |
| `-r`,<br>`--region`              | FALSE    | Specifies the AWS Region for downloading artifacts such as the SSM Agent. Defaults to `us-west-2`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `-t`,<br>`--timeout`             | FALSE    | Maximum install command duration. The input follows duration format. For example `1h23m`. Default download timeout for install command is set to 20 minutes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `-h`, `--help`                   | FALSE    | Displays help message with available flag, subcommand and positional value parameters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

**Examples**

Install Kubernetes version `1.32` with AWS Systems Manager (SSM) as the credential provider

```
nodeadm install 1.32 --credential-provider ssm
```

Install Kubernetes version `1.32` with AWS Systems Manager (SSM) as the credential provider, Docker as the containerd source, with a download timeout of 20 minutes.

```
nodeadm install 1.32 --credential-provider ssm --containerd-source docker --timeout 20m
```

Install Kubernetes version `1.32` with AWS IAM Roles Anywhere as the credential provider

```
nodeadm install 1.32 --credential-provider iam-ra
```

## `nodeadm config check`

The `nodeadm config check` command checks the provided node configuration for errors. This command can be used to verify and validate the correctness of a hybrid node configuration file.

**Usage**

```
nodeadm config check [flags]
```

**Flags**

| Name                       | Required | Description                                                                                       |
| -------------------------- | -------- | ------------------------------------------------------------------------------------------------- |
| `-c`,<br>`--config-source` | TRUE     | Source of nodeadm configuration. For hybrid nodes the input should follow a URI with file scheme. |
| `-h`, `--help`             | FALSE    | Displays help message with available flag, subcommand and positional value parameters.            |

**Examples**

```
nodeadm config check -c file://nodeConfig.yaml
```

## `nodeadm init`

The `nodeadm init` command starts and connects the hybrid node with the configured Amazon EKS cluster. See [Node Config for SSM hybrid activations](#hybrid-nodes-node-config-ssm "#hybrid-nodes-node-config-ssm") or [Node Config for IAM Roles Anywhere](#hybrid-nodes-node-config-iamra "#hybrid-nodes-node-config-iamra") for details of how to configure the `nodeConfig.yaml` file.

**Usage**

```
nodeadm init [flags]
```

**Flags**

| Name                       | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `-c`,<br>`--config-source` | TRUE     | Source of `nodeadm` configuration. For hybrid nodes the input should follow a URI with file scheme.                                                                                                                                                                                                                                                                                                                                                          |
| `-s`,<br>`--skip`          | FALSE    | Phases of `init` to be skipped. It is not recommended to skip any of the phases unless it helps to fix an issue.<br>**Values**<br>`install-validation` skips checking if the preceding install command ran successfully.<br>`cni-validation` skips checking if either Cilium or Calico CNI’s VXLAN ports are opened if firewall is enabled on the node<br>`node-ip-validation` skips checking if the node IP falls within a CIDR in the remote node networks |
| `-h`, `--help`             | FALSE    | Displays help message with available flag, subcommand and positional value parameters.                                                                                                                                                                                                                                                                                                                                                                       |

**Examples**

```
nodeadm init -c file://nodeConfig.yaml
```

## `nodeadm upgrade`

The `nodeadm upgrade` command upgrades all the installed artifacts to the latest version and bootstraps the node to configure the upgraded artifacts and join the EKS cluster on AWS. Upgrade is a disruptive command to the workloads running on the node. Please move your workloads to another node before running upgrade.

**Usage**

```
nodeadm upgrade [KUBERNETES_VERSION] [flags]
```

**Positional Arguments**

(Required) `KUBERNETES_VERSION` The major.minor version of EKS Kubernetes to install, for example `1.32`

**Flags**

| Name                       | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `-c`,<br>`--config-source` | TRUE     | Source of `nodeadm` configuration. For hybrid nodes the input should follow a URI with file scheme.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `-t`,<br>`--timeout`       | FALSE    | Timeout for downloading artifacts. The input follows duration format. For example 1h23m. Default download timeout for upgrade command is set to 10 minutes.                                                                                                                                                                                                                                                                                                                                                                          |
| `-s`,<br>`--skip`          | FALSE    | Phases of upgrade to be skipped. It is not recommended to skip any of the phase unless it helps to fix an issue.<br>**Values**<br>`pod-validation` skips checking if all the no pods are running on the node, except daemon sets and static pods.<br>`node-validation` skips checking if the node has been cordoned.<br>`init-validation` skips checking if the node has been initialized successfully before running upgrade.<br>`containerd-major-version-upgrade` prevents containerd major version upgrades during node upgrade. |
| `-h`, `--help`             | FALSE    | Displays help message with available flag, subcommand and positional value parameters.                                                                                                                                                                                                                                                                                                                                                                                                                                               |

**Examples**

```
nodeadm upgrade 1.32 -c file://nodeConfig.yaml
```

```
nodeadm upgrade 1.32 -c file://nodeConfig.yaml --timeout 20m
```

## `nodeadm uninstall`

The `nodeadm uninstall` command stops and removes the artifacts `nodeadm` installs during `nodeadm install`, including the kubelet and containerd. Note, the uninstall command does not drain or delete your hybrid nodes from your cluster. You must run the drain and delete operations separately, see [Remove hybrid nodes](hybrid-nodes-remove.md "hybrid-nodes-remove.md") for more information. By default, `nodeadm uninstall` will not proceed if there are pods remaining on the node. Similarly, `nodeadm uninstall` does not remove CNI dependencies or dependencies of other Kubernetes add-ons you run on your cluster. To fully remove the CNI installation from your host, see the instructions at [Configure CNI for hybrid nodes](hybrid-nodes-cni.md "hybrid-nodes-cni.md"). If you are using AWS SSM hybrid activations as your on-premises credentials provider, the `nodeadm uninstall` command deregisters your hosts as AWS SSM managed instances.

**Usage**

```
nodeadm uninstall [flags]
```

**Flags**

| Name               | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `-s`,<br>`--skip`  | FALSE    | Phases of uninstall to be skipped. It is not recommended to skip any of the phases unless it helps to fix an issue.<br>**Values**<br>`pod-validation` skips checking if all the no pods are running on the node, except daemon sets and static pods.<br>`node-validation` skips checking if the node has been cordoned.<br>`init-validation` skips checking if the node has been initialized successfully before running uninstall.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `-h`,<br>`--help`  | FALSE    | Displays help message with available flag, subcommand and positional value parameters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `-f`,<br>`--force` | FALSE    | Force delete additional directories that might contain remaining files from Kubernetes and CNI components.<br>**WARNING**<br>This will delete all contents in default Kubernetes and CNI directories (`/var/lib/cni`, `/etc/cni/net.d`, etc). Do not use this flag if you store your own data in these locations.<br>Starting from nodeadm `v1.0.9`, the `./nodeadm uninstall --skip node-validation,pod-validation --force` command no longer deletes the `/var/lib/kubelet` directory. This is because it may contain Pod volumes and volume-subpath directories that sometimes include the mounted node filesystem.<br>**Safe handling tips**<br>• Deleting mounted paths can lead to accidental deletion of the actual mounted node filesystem. Before manually deleting the `/var/lib/kubelet` directory, carefully inspect all active mounts and unmount volumes safely to avoid data loss. |

**Examples**

```
nodeadm uninstall
```

```
nodeadm uninstall --skip node-validation,pod-validation
```

## `nodeadm debug`

The `nodeadm debug` command can be used to troubleshoot unhealthy or misconfigured hybrid nodes. It validates the following requirements are in-place.

- The node has network access to the required AWS APIs for obtaining credentials,
- The node is able to get AWS credentials for the configured Hybrid Nodes IAM role,
- The node has network access to the EKS Kubernetes API endpoint and the validity of the EKS Kubernetes API endpoint certificate,
- The node is able to authenticate with the EKS cluster, its identity in the cluster is valid, and that the node has access to the EKS cluster through the VPC configured for the EKS cluster.

If errors are found, the command’s output suggests troubleshooting steps. Certain validation steps show child processes. If these fail, the output is showed in a stderr section under the validation error.

**Usage**

```
nodeadm debug [flags]
```

**Flags**

| Name                    | Required | Description                                                                                         |
| ----------------------- | -------- | --------------------------------------------------------------------------------------------------- |
| `-c`, `--config-source` | TRUE     | Source of `nodeadm` configuration. For hybrid nodes the input should follow a URI with file scheme. |
| `--no-color`            | FALSE    | Disables color output. Useful for automation.                                                       |
| `-h`, `--help`          | FALSE    | Displays help message with available flag, subcommand and positional value parameters.              |

**Examples**

```
nodeadm debug -c file://nodeConfig.yaml
```

## Nodeadm file locations

### nodeadm install

When running `nodeadm install`, the following files and file locations are configured.

| Artifact                    | Path                                                                                                              |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| IAM Roles Anywhere CLI      | /usr/local/bin/aws_signing_helper                                                                                 |
| Kubelet binary              | /usr/bin/kubelet                                                                                                  |
| Kubectl binary              | usr/local/bin/kubectl                                                                                             |
| ECR Credentials Provider    | /etc/eks/image-credential-provider/ecr-credential-provider                                                        |
| AWS IAM Authenticator       | /usr/local/bin/aws-iam-authenticator                                                                              |
| SSM Setup CLI               | /opt/ssm/ssm-setup-cli                                                                                            |
| SSM Agent                   | On Ubuntu<br>• /snap/amazon-ssm-agent/current/amazon-ssm-agent<br>On RHEL & AL2023<br>• /usr/bin/amazon-ssm-agent |
| Containerd                  | On Ubuntu & AL2023<br>• /usr/bin/containerd<br>On RHEL<br>• /bin/containerd                                       |
| Iptables                    | On Ubuntu & AL2023<br>• /usr/sbin/iptables<br>On RHEL<br>• /sbin/iptables                                         |
| CNI plugins                 | /opt/cni/bin                                                                                                      |
| installed artifacts tracker | /opt/nodeadm/tracker                                                                                              |

### nodeadm init

When running `nodeadm init`, the following files and file locations are configured.

| Name                                              | Path                                                  |
| ------------------------------------------------- | ----------------------------------------------------- |
| Kubelet kubeconfig                                | /var/lib/kubelet/kubeconfig                           |
| Kubelet config                                    | /etc/kubernetes/kubelet/config.json                   |
| Kubelet systemd unit                              | /etc/systemd/system/kubelet.service                   |
| Image credentials provider config                 | /etc/eks/image-credential-provider/config.json        |
| Kubelet env file                                  | /etc/eks/kubelet/environment                          |
| Kubelet Certs                                     | /etc/kubernetes/pki/ca.crt                            |
| Containerd config                                 | /etc/containerd/config.toml                           |
| Containerd kernel modules config                  | /etc/modules-load.d/contianerd.conf                   |
| AWS config file                                   | /etc/aws/hybrid/config                                |
| AWS credentials file (if enable credentials file) | /eks-hybrid/.aws/credentials                          |
| AWS signing helper system unit                    | /etc/systemd/system/aws_signing_helper_update.service |
| Sysctl conf file                                  | /etc/sysctl.d/99-nodeadm.conf                         |
| Ca-certificates                                   | /etc/ssl/certs/ca-certificates.crt                    |
| Gpg key file                                      | /etc/apt/keyrings/docker.asc                          |
| Docker repo source file                           | /etc/apt/sources.list.d/docker.list                   |

## Node Config for SSM hybrid activations

The following is a sample `nodeConfig.yaml` when using AWS SSM hybrid activations for hybrid nodes credentials.

```
apiVersion: node.eks.aws/v1alpha1
kind: NodeConfig
spec:
  cluster:
    name:             # Name of the EKS cluster
    region:           # AWS Region where the EKS cluster resides
  hybrid:
    ssm:
      activationCode: # SSM hybrid activation code
      activationId:   # SSM hybrid activation id
```

## Node Config for IAM Roles Anywhere

The following is a sample `nodeConfig.yaml` for AWS IAM Roles Anywhere for hybrid nodes credentials.

When using AWS IAM Roles Anywhere as your on-premises credentials provider, the `nodeName` you use in your `nodeadm` configuration must align with the permissions you scoped for your Hybrid Nodes IAM role. For example, if your permissions for the Hybrid Nodes IAM role only allow AWS IAM Roles Anywhere to assume the role when the role session name is equal to the CN of the host certificate, then the `nodeName` in your `nodeadm` configuration must be the same as the CN of your certificates. The `nodeName` that you use can’t be longer than 64 characters. For more information, see [Prepare credentials for hybrid nodes](hybrid-nodes-creds.md "hybrid-nodes-creds.md").

```
apiVersion: node.eks.aws/v1alpha1
kind: NodeConfig
spec:
  cluster:
    name:              # Name of the EKS cluster
    region:            # AWS Region where the EKS cluster resides
  hybrid:
    iamRolesAnywhere:
      nodeName:        # Name of the node
      trustAnchorArn:  # ARN of the IAM Roles Anywhere trust anchor
      profileArn:      # ARN of the IAM Roles Anywhere profile
      roleArn:         # ARN of the Hybrid Nodes IAM role
      certificatePath: # Path to the certificate file to authenticate with the IAM Roles Anywhere trust anchor
      privateKeyPath:  # Path to the private key file for the certificate
```

## Node Config for customizing kubelet (Optional)

You can pass kubelet configuration and flags in your `nodeadm` configuration. See the example below for how to add an additional node label `abc.amazonaws.com/test-label` and config for setting `shutdownGracePeriod` to 30 seconds.

```
apiVersion: node.eks.aws/v1alpha1
kind: NodeConfig
spec:
  cluster:
    name:             # Name of the EKS cluster
    region:           # AWS Region where the EKS cluster resides
  kubelet:
    config:           # Map of kubelet config and values
       shutdownGracePeriod: 30s
    flags:            # List of kubelet flags
       - --node-labels=abc.company.com/test-label=true
  hybrid:
    ssm:
      activationCode: # SSM hybrid activation code
      activationId:   # SSM hybrid activation id
```

## Node Config for customizing containerd (Optional)

You can pass custom containerd configuration in your `nodeadm` configuration. The containerd configuration for `nodeadm` accepts in-line TOML. See the example below for how to configure containerd to disable deletion of unpacked image layers in the containerd content store.

```
apiVersion: node.eks.aws/v1alpha1
kind: NodeConfig
spec:
  cluster:
    name:             # Name of the EKS cluster
    region:           # AWS Region where the EKS cluster resides
  containerd:
    config: |         # Inline TOML containerd additional configuration
       [plugins."io.containerd.grpc.v1.cri".containerd]
       discard_unpacked_layers = false
  hybrid:
    ssm:
      activationCode: # SSM hybrid activation code
      activationId:   # SSM hybrid activation id
```

###### Note

Containerd versions 1.x and 2.x use different configuration formats. Containerd 1.x uses config version 2, while containerd 2.x uses config version 3. Although containerd 2.x remains backward compatible with config version 2, config version 3 is recommended for optimal performance. Check your containerd version with `containerd --version` or review `nodeadm` install logs. For more details on config versioning, see [https://containerd.io/releases/](https://containerd.io/releases/ "https://containerd.io/releases/")

You can also use the containerd configuration to enable SELinux support. With SELinux enabled on containerd, ensure pods scheduled on the node have the proper securityContext and seLinuxOptions enabled. More information on configuring a security context can be found on the [Kubernetes documentation](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/ "https://kubernetes.io/docs/tasks/configure-pod-container/security-context/").

###### Note

Red Hat Enterprise Linux (RHEL) 8 and RHEL 9 have SELinux enabled by default and set to strict on the host. Amazon Linux 2023 has SELinux enabled by default and set to permissive mode. When SELinux is set to permissive mode on the host, enabling it on containerd will not block requests but will log it according to the SELinux configuration on the host.

```
apiVersion: node.eks.aws/v1alpha1
kind: NodeConfig
spec:
  cluster:
    name:             # Name of the EKS cluster
    region:           # AWS Region where the EKS cluster resides
  containerd:
    config: |         # Inline TOML containerd additional configuration
       [plugins."io.containerd.grpc.v1.cri"]
       enable_selinux = true
  hybrid:
    ssm:
      activationCode: # SSM hybrid activation code
      activationId:   # SSM hybrid activation id
```
