# Installation options for Eksctl

`eksctl` is available to install from official releases as described below. We recommend that you install `eksctl` from only the official GitHub releases. You may opt to use a third-party installer, but please be advised that AWS does not maintain nor support these methods of installation. Use them at your own discretion.

## Prerequisite

You will need to have AWS API credentials configured. What works for AWS CLI or any other tools (kops, Terraform, etc.) should be sufficient. You can use [`~/.aws/credentials` file](../../../cli/latest/userguide/cli-config-files.md "../../../cli/latest/userguide/cli-config-files.md")
or [environment variables](../../../cli/latest/userguide/cli-environment.md "../../../cli/latest/userguide/cli-environment.md"). For more information, see the [AWS CLI Reference](../../../cli/latest/userguide/cli-environment.md "../../../cli/latest/userguide/cli-environment.md").

You will also need [AWS IAM Authenticator for Kubernetes](https://github.com/kubernetes-sigs/aws-iam-authenticator "https://github.com/kubernetes-sigs/aws-iam-authenticator") command (either `aws-iam-authenticator` or `aws eks get-token` (available in version 1.16.156 or greater of AWS CLI) in your `PATH`.

The IAM account used for EKS cluster creation should have these minimal access levels.

| AWS Service      | Access Level                                                |
| ---------------- | ----------------------------------------------------------- |
| CloudFormation   | Full Access                                                 |
| EC2              | **Full:\*<br>• Tagging **Limited:\*<br>• List, Read, Write  |
| EC2 Auto Scaling | \*_Limited:_<br>• List, Write                               |
| EKS              | Full Access                                                 |
| IAM              | \*_Limited:_<br>• List, Read, Write, Permissions Management |
| Systems Manager  | \*_Limited:_<br>• List, Read                                |

## For Unix

To download the latest release, run:

```
# for ARM systems, set ARCH to: `arm64`, `armv6` or `armv7`
ARCH=amd64
PLATFORM=$(uname -s)_$ARCH

curl -sLO "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_$PLATFORM.tar.gz"

# (Optional) Verify checksum
curl -sL "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_checksums.txt" | grep $PLATFORM | sha256sum --check

tar -xzf eksctl_$PLATFORM.tar.gz -C /tmp && rm eksctl_$PLATFORM.tar.gz

sudo install -m 0755 /tmp/eksctl /usr/local/bin && rm /tmp/eksctl
```

## For Windows

Direct download (latest release):

- [AMD64/x86_64](https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_windows_amd64.zip "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_windows_amd64.zip")
- [ARMv6](https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_windows_armv6.zip "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_windows_armv6.zip")
- [ARMv7](https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_windows_armv7.zip "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_windows_armv7.zip")
- [ARM64](https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_windows_arm64.zip "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_windows_arm64.zip")

Make sure to unzip the archive to a folder in the `PATH` variable.

Optionally, verify the checksum:

1. Download the checksum file: [latest](https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_checksums.txt "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_checksums.txt")
2. Use Command Prompt to manually compare `CertUtil`'s output to the checksum file downloaded.

```
  REM Replace amd64 with armv6, armv7 or arm64
  CertUtil -hashfile eksctl_Windows_amd64.zip SHA256
```

3. Using PowerShell to automate the verification using the `-eq` operator to get a `True` or `False` result:

```
# Replace amd64 with armv6, armv7 or arm64
 (Get-FileHash -Algorithm SHA256 .\eksctl_Windows_amd64.zip).Hash -eq ((Get-Content .\eksctl_checksums.txt) -match 'eksctl_Windows_amd64.zip' -split ' ')[0]
```

### Using Git Bash:

```
# for ARM systems, set ARCH to: `arm64`, `armv6` or `armv7`
ARCH=amd64
PLATFORM=windows_$ARCH

curl -sLO "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_$PLATFORM.zip"

# (Optional) Verify checksum
curl -sL "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_checksums.txt" | grep $PLATFORM | sha256sum --check

unzip eksctl_$PLATFORM.zip -d $HOME/bin

rm eksctl_$PLATFORM.zip
```

The `eksctl` executable is placed in `$HOME/bin`, which is in `$PATH` from Git Bash.

## Homebrew

You can use Homebrew to install software on MacOS and Linux.

AWS maintains a Homebrew tap including eksctl.

For more information about the Homebrew tap, see the [project on Github](https://github.com/aws/homebrew-tap "https://github.com/aws/homebrew-tap") and the [Homebrew formula](https://github.com/aws/homebrew-tap/blob/master/Formula/eksctl.rb "https://github.com/aws/homebrew-tap/blob/master/Formula/eksctl.rb") for eksctl.

**To install eksctl with Homebrew**

1. (Prerequisite) Install [Homebrew](https://brew.sh/ "https://brew.sh/")
2. Add the AWS tap

```
brew tap aws/tap
```

3. Install eksctl

```
brew install aws/tap/eksctl
```

## Docker

For every release and RC a container image is pushed to ECR repository `public.ecr.aws/eksctl/eksctl`. Learn more about the usage on [ECR Public Gallery - eksctl](https://gallery.ecr.aws/eksctl/eksctl "https://gallery.ecr.aws/eksctl/eksctl"). For example,

```
docker run --rm -it public.ecr.aws/eksctl/eksctl version
```

## Shell Completion

### Bash

To enable bash completion, run the following, or put it in `~/.bashrc` or `~/.profile`:

```
. <(eksctl completion bash)
```

### Zsh

For zsh completion, please run:

```
mkdir -p ~/.zsh/completion/
eksctl completion zsh > ~/.zsh/completion/_eksctl
```

and put the following in `~/.zshrc`:

```
fpath=($fpath ~/.zsh/completion)
```

Note if you’re not running a distribution like oh-my-zsh you may first have to enable autocompletion (and put in `~/.zshrc` to make it persistent):

```
autoload -U compinit
compinit
```

### Fish

The below commands can be used for fish auto completion:

```
mkdir -p ~/.config/fish/completions
eksctl completion fish > ~/.config/fish/completions/eksctl.fish
```

### Powershell

The below command can be referred for setting it up. Please note that the path might be different depending on your
system settings.

```
eksctl completion powershell > C:\Users\Documents\WindowsPowerShell\Scripts\eksctl.ps1
```

## Updates

###### Important

If you install eksctl by directly downloading it (not using a package manager) you need to manually update it.
