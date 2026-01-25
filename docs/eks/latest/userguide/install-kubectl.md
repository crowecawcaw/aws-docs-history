**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Set up `kubectl` and `eksctl`

###### Tip

[Register](https://aws-experience.com/emea/smb/events/series/get-hands-on-with-amazon-eks?trk=4a9b4147-2490-4c63-bc9f-f8a84b122c8c&sc_channel=el "https://aws-experience.com/emea/smb/events/series/get-hands-on-with-amazon-eks?trk=4a9b4147-2490-4c63-bc9f-f8a84b122c8c&sc_channel=el") for upcoming Amazon EKS workshops.

Once the AWS CLI is installed, there are two other tools you should install to create and manage your Kubernetes clusters:

- `kubectl`: The `kubectl` command line tool is the main tool you will use to manage resources within your Kubernetes cluster. This page describes how to download and set up the `kubectl` binary that matches the version of your Kubernetes cluster. See [Install or update kubectl](#kubectl-install-update "#kubectl-install-update").
- `eksctl`: The `eksctl` command line tool is made for creating EKS clusters in the AWS cloud or on-premises (with EKS Anywhere), as well as modifying and deleting those clusters. See [Install eksctl](#eksctl-install-update "#eksctl-install-update").

## Install or update `kubectl`

This topic helps you to download and install, or update, the `kubectl` binary on your device. The binary is identical to the [upstream community versions](https://kubernetes.io/docs/tasks/tools/#kubectl "https://kubernetes.io/docs/tasks/tools/#kubectl"). The binary is not unique to Amazon EKS or AWS. Use the steps below to get the specific version of `kubectl` that you need, although many builders simply run `brew install kubectl` to install it.

###### Note

You must use a `kubectl` version that is within one minor version difference of your Amazon EKS cluster control plane. For example, a `1.32`
`kubectl` client works with Kubernetes `1.31`, `1.32`, and `1.33` clusters.

## Step 1: Check if `kubectl` is installed

Determine whether you already have `kubectl` installed on your device.

```
kubectl version --client
```

If you have `kubectl` installed in the path of your device, the example output includes information similar to the following. If you want to update the version that you currently have installed with a later version, complete the next step, making sure to install the new version in the same location that your current version is in.

```
Client Version: v1.31.X-eks-1234567
```

If you receive no output, then you either don’t have `kubectl` installed, or it’s not installed in a location that’s in your device’s path.

## Step 2: Install or update `kubectl`

Install or update `kubectl` on one of the following operating systems:

- [macOS](#macos_kubectl "#macos_kubectl")
- [Linux (amd64)](#linux_amd64_kubectl "#linux_amd64_kubectl")
- [Linux (arm64)](#linux_arm64_kubectl "#linux_arm64_kubectl")
- [Windows](#windows_kubectl "#windows_kubectl")

###### Note

If downloads are slow to your AWS Region from the AWS Regions used in this section,
consider setting up CloudFront to front the content.
For further information, see [Get started with a basic CloudFront distribution](../../../AmazonCloudFront/latest/DeveloperGuide/GettingStartedSimpleDistributon.md "../../../AmazonCloudFront/latest/DeveloperGuide/GettingStartedSimpleDistributon.md").

### macOS

Follow the steps below to install `kubectl` on macOS. The steps include:

- Choosing and downloading the binary for the Kubernetes version you want.
- Optionally checking the binary’s checksum.
- Adding execute to the binary’s permissions.
- Copying the binary to a folder in your PATH.
- Optionally adding the binary’s directory to your PATH.

Procedure:

1. Download the binary for your cluster’s Kubernetes version from Amazon S3.
   - Kubernetes `1.34`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.34.2/2025-11-13/bin/darwin/amd64/kubectl
   ```

   - Kubernetes `1.33`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.33.5/2025-11-13/bin/darwin/amd64/kubectl
   ```

   - Kubernetes `1.32`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.32.9/2025-11-13/bin/darwin/amd64/kubectl
   ```

   - Kubernetes `1.31`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.31.13/2025-11-13/bin/darwin/amd64/kubectl
   ```

   - Kubernetes `1.30`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.30.14/2025-11-13/bin/darwin/amd64/kubectl
   ```

   - Kubernetes `1.29`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.29.15/2025-11-13/bin/darwin/amd64/kubectl
   ```

   - Kubernetes `1.28`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.28.15/2025-11-13/bin/darwin/amd64/kubectl
   ```

   - Kubernetes `1.27`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.27.16/2025-01-10/bin/darwin/amd64/kubectl
   ```

   - Kubernetes `1.26`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.26.15/2024-12-12/bin/darwin/amd64/kubectl
   ```

2. (Optional) Verify the downloaded binary with the `SHA-256` checksum for your binary.
   1. Download the `SHA-256` checksum for your cluster’s Kubernetes version.
      - Kubernetes `1.34`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.34.2/2025-11-13/bin/darwin/amd64/kubectl.sha256
      ```

      - Kubernetes `1.33`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.33.5/2025-11-13/bin/darwin/amd64/kubectl.sha256
      ```

      - Kubernetes `1.32`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.32.9/2025-11-13/bin/darwin/amd64/kubectl.sha256
      ```

      - Kubernetes `1.31`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.31.13/2025-11-13/bin/darwin/amd64/kubectl.sha256
      ```

      - Kubernetes `1.30`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.30.14/2025-11-13/bin/darwin/amd64/kubectl.sha256
      ```

      - Kubernetes `1.29`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.29.15/2025-11-13/bin/darwin/amd64/kubectl.sha256
      ```

      - Kubernetes `1.28`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.28.15/2025-11-13/bin/darwin/amd64/kubectl.sha256
      ```

      - Kubernetes `1.27`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.27.16/2025-01-10/bin/darwin/amd64/kubectl.sha256
      ```

      - Kubernetes `1.26`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.26.15/2024-12-12/bin/darwin/amd64/kubectl.sha256
      ```

   2. Check the `SHA-256` checksum for your downloaded binary.

   ```
   openssl sha1 -sha256 kubectl
   ```

   3. Make sure that the generated checksum in the output matches in the checksum in the downloaded `kubectl.sha256` file.

3. Apply execute permissions to the binary.

```
chmod +x ./kubectl
```

4. Copy the binary to a folder in your `PATH`. If you have already installed a version of `kubectl`, then we recommend creating a `$HOME/bin/kubectl` and ensuring that `$HOME/bin` comes first in your `$PATH`.

```
mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$HOME/bin:$PATH
```

5. (Optional) Add the `$HOME/bin` path to your shell initialization file so that it is configured when you open a shell.

```
echo 'export PATH=$HOME/bin:$PATH' >> ~/.bash_profile
```

### Linux (amd64)

Follow the steps below to install `kubectl` on Linux (amd64). The steps include:

- Choosing and downloading the binary for the Kubernetes version you want.
- Optionally checking the binary’s checksum.
- Adding execute to the binary’s permissions.
- Copying the binary to a folder in your PATH.
- Optionally adding the binary’s directory to your PATH.

Procedure:

1. Download the `kubectl` binary for your cluster’s Kubernetes version from Amazon S3.
   - Kubernetes `1.34`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.34.2/2025-11-13/bin/linux/amd64/kubectl
   ```

   - Kubernetes `1.33`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.33.5/2025-11-13/bin/linux/amd64/kubectl
   ```

   - Kubernetes `1.32`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.32.9/2025-11-13/bin/linux/amd64/kubectl
   ```

   - Kubernetes `1.31`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.31.13/2025-11-13/bin/linux/amd64/kubectl
   ```

   - Kubernetes `1.30`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.30.14/2025-11-13/bin/linux/amd64/kubectl
   ```

   - Kubernetes `1.29`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.29.15/2025-11-13/bin/linux/amd64/kubectl
   ```

   - Kubernetes `1.28`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.28.15/2025-11-13/bin/linux/amd64/kubectl
   ```

   - Kubernetes `1.27`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.27.16/2024-12-12/bin/linux/amd64/kubectl
   ```

   - Kubernetes `1.26`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.26.15/2024-12-12/bin/linux/amd64/kubectl
   ```

2. (Optional) Verify the downloaded binary with the `SHA-256` checksum for your binary.
   1. Download the `SHA-256` checksum for your cluster’s Kubernetes version from Amazon S3using the command for your device’s hardware platform.
      - Kubernetes `1.34`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.34.2/2025-11-13/bin/linux/amd64/kubectl.sha256
      ```

      - Kubernetes `1.33`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.33.5/2025-11-13/bin/linux/amd64/kubectl.sha256
      ```

      - Kubernetes `1.32`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.32.9/2025-11-13/bin/linux/amd64/kubectl.sha256
      ```

      - Kubernetes `1.31`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.31.13/2025-11-13/bin/linux/amd64/kubectl.sha256
      ```

      - Kubernetes `1.30`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.30.14/2025-11-13/bin/linux/amd64/kubectl.sha256
      ```

      - Kubernetes `1.29`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.29.15/2025-11-13/bin/linux/amd64/kubectl.sha256
      ```

      - Kubernetes `1.28`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.28.15/2025-11-13/bin/linux/amd64/kubectl.sha256
      ```

      - Kubernetes `1.27`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.27.16/2024-12-12/bin/linux/amd64/kubectl.sha256
      ```

      - Kubernetes `1.26`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.26.15/2024-12-12/bin/linux/amd64/kubectl.sha256
      ```

   2. Check the `SHA-256` checksum for your downloaded binary with one of the following commands.

   ```
   sha256sum -c kubectl.sha256
   ```

   or

   ```
   openssl sha1 -sha256 kubectl
   ```

   3. For the first, you should see `kubectl: OK`, for the second, you can check that the generated checksum in the output matches in the checksum in the downloaded `kubectl.sha256` file.

3. Apply execute permissions to the binary.

```
chmod +x ./kubectl
```

4. Copy the binary to a folder in your `PATH`. If you have already installed a version of `kubectl`, then we recommend creating a `$HOME/bin/kubectl` and ensuring that `$HOME/bin` comes first in your `$PATH`.

```
mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$HOME/bin:$PATH
```

5. (Optional) Add the `$HOME/bin` path to your shell initialization file so that it is configured when you open a shell.

###### Note

This step assumes you are using the Bash shell; if you are using another shell, change the command to use your specific shell initialization file.

```
echo 'export PATH=$HOME/bin:$PATH' >> ~/.bashrc
```

### Linux (arm64)

Follow the steps below to install `kubectl` on Linux (arm64). The steps include:

- Choosing and downloading the binary for the Kubernetes version you want.
- Optionally checking the binary’s checksum.
- Adding execute to the binary’s permissions.
- Copying the binary to a folder in your PATH.
- Optionally adding the binary’s directory to your PATH.

Procedure:

1. Download the `kubectl` binary for your cluster’s Kubernetes version from Amazon S3.
   - Kubernetes `1.34`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.34.2/2025-11-13/bin/linux/arm64/kubectl
   ```

   - Kubernetes `1.33`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.33.5/2025-11-13/bin/linux/arm64/kubectl
   ```

   - Kubernetes `1.32`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.32.9/2025-11-13/bin/linux/arm64/kubectl
   ```

   - Kubernetes `1.31`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.31.13/2025-11-13/bin/linux/arm64/kubectl
   ```

   - Kubernetes `1.30`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.30.14/2025-11-13/bin/linux/arm64/kubectl
   ```

   - Kubernetes `1.29`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.29.15/2025-11-13/bin/linux/arm64/kubectl
   ```

   - Kubernetes `1.28`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.28.15/2025-11-13/bin/linux/arm64/kubectl
   ```

   - Kubernetes `1.27`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.27.16/2024-12-12/bin/linux/arm64/kubectl
   ```

   - Kubernetes `1.26`

   ```
   curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.26.15/2024-12-12/bin/linux/arm64/kubectl
   ```

2. (Optional) Verify the downloaded binary with the `SHA-256` checksum for your binary.
   1. Download the `SHA-256` checksum for your cluster’s Kubernetes version from Amazon S3using the command for your device’s hardware platform.
      - Kubernetes `1.34`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.34.2/2025-11-13/bin/linux/arm64/kubectl.sha256
      ```

      - Kubernetes `1.33`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.33.5/2025-11-13/bin/linux/arm64/kubectl.sha256
      ```

      - Kubernetes `1.32`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.32.9/2025-11-13/bin/linux/arm64/kubectl.sha256
      ```

      - Kubernetes `1.31`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.31.13/2025-11-13/bin/linux/arm64/kubectl.sha256
      ```

      - Kubernetes `1.30`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.30.14/2025-11-13/bin/linux/arm64/kubectl.sha256
      ```

      - Kubernetes `1.29`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.29.15/2025-11-13/bin/linux/arm64/kubectl.sha256
      ```

      - Kubernetes `1.28`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.28.15/2025-11-13/bin/linux/arm64/kubectl.sha256
      ```

      - Kubernetes `1.27`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.27.16/2024-12-12/bin/linux/arm64/kubectl.sha256
      ```

      - Kubernetes `1.26`

      ```
      curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.26.15/2024-12-12/bin/linux/arm64/kubectl.sha256
      ```

   2. Check the `SHA-256` checksum for your downloaded binary with one of the following commands.

   ```
   sha256sum -c kubectl.sha256
   ```

   or

   ```
   openssl sha1 -sha256 kubectl
   ```

   3. For the first, you should see `kubectl: OK`, for the second, you can check that the generated checksum in the output matches in the checksum in the downloaded `kubectl.sha256` file.

3. Apply execute permissions to the binary.

```
chmod +x ./kubectl
```

4. Copy the binary to a folder in your `PATH`. If you have already installed a version of `kubectl`, then we recommend creating a `$HOME/bin/kubectl` and ensuring that `$HOME/bin` comes first in your `$PATH`.

```
mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$HOME/bin:$PATH
```

5. (Optional) Add the `$HOME/bin` path to your shell initialization file so that it is configured when you open a shell.

###### Note

This step assumes you are using the Bash shell; if you are using another shell, change the command to use your specific shell initialization file.

```
echo 'export PATH=$HOME/bin:$PATH' >> ~/.bashrc
```

### Windows

Follow the steps below to install `kubectl` on Windows. The steps include:

- Choosing and downloading the binary for the Kubernetes version you want.
- Optionally checking the binary’s checksum.
- Copying the binary to a folder in your PATH.
- Optionally adding the binary’s directory to your PATH.

Procedure:

1. Open a PowerShell terminal.
2. Download the `kubectl` binary for your cluster’s Kubernetes version from Amazon S3.
   - Kubernetes `1.34`

   ```
   curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.34.2/2025-11-13/bin/windows/amd64/kubectl.exe
   ```

   - Kubernetes `1.33`

   ```
   curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.33.5/2025-11-13/bin/windows/amd64/kubectl.exe
   ```

   - Kubernetes `1.32`

   ```
   curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.32.9/2025-11-13/bin/windows/amd64/kubectl.exe
   ```

   - Kubernetes `1.31`

   ```
   curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.31.13/2025-11-13/bin/windows/amd64/kubectl.exe
   ```

   - Kubernetes `1.30`

   ```
   curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.30.14/2025-11-13/bin/windows/amd64/kubectl.exe
   ```

   - Kubernetes `1.29`

   ```
   curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.29.15/2025-11-13/bin/windows/amd64/kubectl.exe
   ```

   - Kubernetes `1.28`

   ```
   curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.28.15/2025-11-13/bin/windows/amd64/kubectl.exe
   ```

   - Kubernetes `1.27`

   ```
   curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.27.16/2024-12-12/bin/windows/amd64/kubectl.exe
   ```

   - Kubernetes `1.26`

   ```
   curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.26.15/2024-12-12/bin/windows/amd64/kubectl.exe
   ```

3. (Optional) Verify the downloaded binary with the `SHA-256` checksum for your binary.
   1. Download the `SHA-256` checksum for your cluster’s Kubernetes version for Windows.
      - Kubernetes `1.34`

      ```
      curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.34.2/2025-11-13/bin/windows/amd64/kubectl.exe.sha256
      ```

      - Kubernetes `1.33`

      ```
      curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.33.5/2025-11-13/bin/windows/amd64/kubectl.exe.sha256
      ```

      - Kubernetes `1.32`

      ```
      curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.32.9/2025-11-13/bin/windows/amd64/kubectl.exe.sha256
      ```

      - Kubernetes `1.31`

      ```
      curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.31.13/2025-11-13/bin/windows/amd64/kubectl.exe.sha256
      ```

      - Kubernetes `1.30`

      ```
      curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.30.14/2025-11-13/bin/windows/amd64/kubectl.exe.sha256
      ```

      - Kubernetes `1.29`

      ```
      curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.29.15/2025-11-13/bin/windows/amd64/kubectl.exe.sha256
      ```

      - Kubernetes `1.28`

      ```
      curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.28.15/2025-11-13/bin/windows/amd64/kubectl.exe.sha256
      ```

      - Kubernetes `1.27`

      ```
      curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.27.16/2024-12-12/bin/windows/amd64/kubectl.exe.sha256
      ```

      - Kubernetes `1.26`

      ```
      curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.26.15/2024-12-12/bin/windows/amd64/kubectl.exe.sha256
      ```

   2. Check the `SHA-256` checksum for your downloaded binary.

   ```
   Get-FileHash kubectl.exe
   ```

   3. Make sure that the generated checksum in the output matches in the checksum in the downloaded `kubectl.sha256` file. The PowerShell output should be an uppercase equivalent string of characters.

4. Copy the binary to a folder in your `PATH`. If you have an existing directory in your `PATH` that you use for command line utilities, copy the binary to that directory. Otherwise, complete the following steps.
   1. Create a new directory for your command line binaries, such as `C:\bin`.
   2. Copy the `kubectl.exe` binary to your new directory.
   3. Edit your user or system `PATH` environment variable to add the new directory to your `PATH`.
   4. Close your PowerShell terminal and open a new one to pick up the new `PATH` variable.

5. After you install `kubectl`, you can verify its version.

```
kubectl version --client
```

6. When first installing `kubectl`, it isn’t yet configured to communicate with any server. We will cover this configuration as needed in other procedures. If you ever need to update the configuration to communicate with a particular cluster, you can run the following command. Replace `region-code` with the AWS Region that your cluster is in. Replace `my-cluster` with the name of your cluster.

```
aws eks update-kubeconfig --region region-code --name my-cluster
```

7. Consider configuring auto completion, which lets you use the tab key to complete `kubectl` subcommands after typing the first few letters. See [Kubectl autocomplete](https://kubernetes.io/docs/reference/kubectl/quick-reference/#kubectl-autocomplete "https://kubernetes.io/docs/reference/kubectl/quick-reference/#kubectl-autocomplete") in the Kubernetes documentation for details.

## Install `eksctl`

The `eksctl` CLI is used to work with EKS clusters. It automates many individual tasks. See [Installation](https://eksctl.io/installation "https://eksctl.io/installation") in the `eksctl` documentation for instructions on installing `eksctl`. For Linux, use the UNIX instructions.

When using `eksctl` the IAM security principal that you’re using must have permissions to work with Amazon EKS IAM roles, service linked roles, AWS CloudFormation, a VPC, and related resources. For more information, see [Actions](../../../service-authorization/latest/reference/list_amazonelastickubernetesservice.md "../../../service-authorization/latest/reference/list_amazonelastickubernetesservice.md") and [Using service-linked roles](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") in the IAM User Guide. You must complete all steps in this guide as the same user. To check the current user, run the following command:

```
aws sts get-caller-identity
```

## Next steps

- [Quickstart: Deploy a web app and store data](quickstart.md "quickstart.md")
