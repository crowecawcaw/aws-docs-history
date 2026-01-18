**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Patch security updates for hybrid nodes

This topic describes the procedure to perform in-place patching of security updates for specific packages and dependencies running on your hybrid nodes. As a best practice we recommend you to regularly update your hybrid nodes to receive CVEs and security patches.

For steps to upgrade the Kubernetes version, see [Upgrade hybrid nodes for your cluster](hybrid-nodes-upgrade.md "hybrid-nodes-upgrade.md").

One example of software that might need security patching is `containerd`.

## `Containerd`

`containerd` is the standard Kubernetes container runtime and core dependency for EKS Hybrid Nodes, used for managing container lifecycle, including pulling images and managing container execution. On an hybrid node, you can install `containerd` through the [nodeadm CLI](hybrid-nodes-nodeadm.md "hybrid-nodes-nodeadm.md") or manually. Depending on the operating system of your node, `nodeadm` will install `containerd` from the OS-distributed package or Docker package.

When a CVE in `containerd` has been published, you have the following options to upgrade to the patched version of `containerd` on your Hybrid nodes.

## Step 1: Check if the patch published to package managers

You can check whether the `containerd` CVE patch has been published to each respective OS package manager by referring to the corresponding security bulletins:

- [Amazon Linux 2023](https://alas.aws.amazon.com/alas2023.html "https://alas.aws.amazon.com/alas2023.html")
- [RHEL](https://access.redhat.com/security/security-updates/security-advisories "https://access.redhat.com/security/security-updates/security-advisories")
- [Ubuntu 20.04](https://ubuntu.com/security/notices?order=newest&release=focal "https://ubuntu.com/security/notices?order=newest&release=focal")
- [Ubuntu 22.04](https://ubuntu.com/security/notices?order=newest&release=jammy "https://ubuntu.com/security/notices?order=newest&release=jammy")
- [Ubuntu 24.04](https://ubuntu.com/security/notices?order=newest&release=noble "https://ubuntu.com/security/notices?order=newest&release=noble")

If you use the Docker repo as the source of `containerd`, you can check the [Docker security announcements](https://docs.docker.com/security/security-announcements/ "https://docs.docker.com/security/security-announcements/") to identify the availability of the patched version in the Docker repo.

## Step 2: Choose the method to install the patch

There are three methods to patch and install security upgrades in-place on nodes. Which method you can use depends on whether the patch is available from the operating system in the package manager or not:

1. Install patches with `nodeadm upgrade` that are published to package managers, see [Step 2 a](#hybrid-nodes-security-nodeadm "#hybrid-nodes-security-nodeadm").
2. Install patches with the package managers directly, see [Step 2 b](#hybrid-nodes-security-package "#hybrid-nodes-security-package").
3. Install custom patches that aren’t published in package managers. Note that there are special considerations for custom patches for `containerd`, [Step 2 c](#hybrid-nodes-security-manual "#hybrid-nodes-security-manual").

## Step 2 a: Patching with `nodeadm upgrade`

After you confirm that the `containerd` CVE patch has been published to the OS or Docker repos (either Apt or RPM), you can use the `nodeadm upgrade` command to upgrade to the latest version of `containerd`. Since this isn’t a Kubernetes version upgrade, you must pass in your current Kubernetes version to the `nodeadm` upgrade command.

```
 nodeadm upgrade <replaceable>K8S_VERSION</replaceable> --config-source file:///root/nodeConfig.yaml
```

## Step 2 b: Patching with operating system package managers

Alternatively you can also update through the respective package manager and use it to upgrade the `containerd` package as follows.

**Amazon Linux 2023**

```
 sudo yum update -y
sudo yum install -y containerd
```

**RHEL**

```
 sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://download.docker.com/linux/rhel/docker-ce.repo
sudo yum update -y
sudo yum install -y containerd
```

**Ubuntu**

```
 sudo mkdir -p /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update -y
sudo apt install -y --only-upgrade containerd.io
```

## Step 2 c: `Containerd` CVE patch not published in package managers

If the patched `containerd` version is only available by other means instead of in the package manager, for example in GitHub releases, then you can install `containerd` from the official GitHub site.

1. If the machine has already joined the cluster as a hybrid node, then you need to run the `nodeadm uninstall` command.
2. Install the official `containerd` binaries. You can use the steps [official installation steps](https://github.com/containerd/containerd/blob/main/docs/getting-started.md#option-1-from-the-official-binaries "https://github.com/containerd/containerd/blob/main/docs/getting-started.md#option-1-from-the-official-binaries") on GitHub.
3. Run the `nodeadm install` command with the `--containerd-source` argument set to `none`, which will skip `containerd` installation through `nodeadm`. You can use the value of `none` in the `containerd` source for any operating system that the node is running.

```
 nodeadm install <replaceable>K8S_VERSION</replaceable> --credential-provider <replaceable>CREDS_PROVIDER</replaceable> --containerd-source none
```
