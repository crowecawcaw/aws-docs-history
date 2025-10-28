# Installing Finch to use with the AWS SAM CLI

Finch is AWS's container development tool that provides an alternative to
Docker, particularly beneficial on macOS and Linux systems. For more
information, see [Finch on GitHub](https://github.com/runfinch "https://github.com/runfinch"). With
Finch, AWS SAM can provide a local environment similar to AWS Lambda as a
container to build, test, and debug your serverless applications.

###### Note

You need Finch for testing your applications locally, for building
deployment packages using the `--use-container` option, and building OCI image
functions. Starting with AWS SAM CLI version 1.145.0, AWS SAM CLI supports Finch as
an alternative container runtime to Docker.

###### Topics

- [Installing Finch](#install-finch-instructions "#install-finch-instructions")
- [Configuring Finch with AWS SAM
  CLI](#install-finch-configuration "#install-finch-configuration")
- [Verifying the installation](#install-finch-verification "#install-finch-verification")
- [Stopping Finch](#install-finch-stopping "#install-finch-stopping")
- [Troubleshooting](#install-finch-troubleshooting "#install-finch-troubleshooting")
- [Next steps](#install-finch-next-steps "#install-finch-next-steps")

## Installing Finch

Follow these instructions to install Finch on your operating system.

### Prerequisites

###### Note

Finch integration in AWS SAM CLI is available on macOS and Linux systems.
For Windows users, consider using a virtual machine or Linux environment for
Finch functionality.

**macOS versions:**

- macOS 15 Sequoia
- macOS 14 Sonoma

###### Note

Finch supports the latest two versions of macOS.

**Linux:**

- Linux Kernel v4.x+

### Installing Finch

###### To install Finch on macOS

1. Install Finch using the `brew` CLI. If prompted, enter
   your macOS password.

```
`$` `brew install finch`
```

2. Check the installed Finch version.

```
`$` `finch --version`
```

3. Initialize Finch virtual machine (first time setup).

```
`$` `finch vm init`
```

4. Start Finch virtual machine.

```
`$` `finch vm start`
```

5. Check the status of the Finch virtual machine.

```
`$` `finch vm status`
```

6. Verify that Finch runs correctly.

```
`$` `finch --info`
`$` `finch ps`
```

For more information, see [Installing Finch on
macOS](https://runfinch.com/docs/managing-finch/macos/installation/ "https://runfinch.com/docs/managing-finch/macos/installation/").

You can install Finch on Amazon Linux, Ubuntu, or by using a generic
installation method. For more information, see [Installing Finch on
Linux](https://runfinch.com/docs/managing-finch/linux/installation/ "https://runfinch.com/docs/managing-finch/linux/installation/").

## Configuring Finch with AWS SAM

CLI

After you install Finch, the AWS SAM CLI automatically detects and uses
Finch as a container runtime when Docker does not run.

###### Note

Finch serves as a fallback to Docker. If you have both
Docker and Finch installed and running, AWS SAM CLI
prioritizes Docker by default.

### Administrator preference configuration (macOS)

You can configure AWS SAM CLI to use a specific container runtime as the default by creating an administrator preference file. This system-wide preference overrides the default fallback behavior.

**Available configuration options**

- **Set Finch as preferred container runtime:**

```
`$` `sudo /usr/libexec/PlistBuddy -c "Add :DefaultContainerRuntime string finch" /Library/Preferences/com.amazon.samcli.plist`
```

- **Set Docker as preferred container runtime:**

```
`$` `sudo /usr/libexec/PlistBuddy -c "Add :DefaultContainerRuntime string docker" /Library/Preferences/com.amazon.samcli.plist`
```

- **Remove preference (return to default behavior):**

```
`$` `sudo /usr/libexec/PlistBuddy -c "Remove :DefaultContainerRuntime" /Library/Preferences/com.amazon.samcli.plist`
```

###### Note

When no administrator preference is set, AWS SAM CLI uses Docker by default when available, with Finch as a fallback when Docker is not running.

### Directory mounting differences (macOS)

On macOS, AWS SAM local commands fail if you locate your project outside your home directory
(`~`) or `/Volumes`. This design restricts automatic directory mounting for security
reasons without your knowledge.

**Mitigation options**

- **Option 1:** Open the Finch configuration in a text
  editor `~/.finch/finch.yaml` and add your project path under the
  `additional_directories` section, then restart the Finch
  virtual machine. For additional information, see [Finch documentation](https://runfinch.com/docs/managing-finch/macos/disk-management/#adding-additional-disk-mounts "https://runfinch.com/docs/managing-finch/macos/disk-management/#adding-additional-disk-mounts").

```
`$` `finch vm stop`
`$` `finch vm start`
```

- **Option 2:** Move your project to your home directory.

## Verifying the installation

After you install and start Finch, verify that it works with AWS SAM CLI.

### Basic verification

Run the following command to verify that AWS SAM CLI can use Finch:

```
`$` `sam build --use-container`
```

You should see AWS SAM CLI using Finch to build your application in a container environment.

###### Note

Finch serves as a fallback to Docker. If
Docker is running, AWS SAM CLI will prioritize Docker by
default.

### Testing Finch as a fallback

To test Finch as a fallback when Docker is running, you need to stop Docker first.

###### To test Finch fallback functionality

1. Stop Docker using the appropriate commands for your operating
   system.

**macOS:**

```
`$` `docker stop $(docker ps -q)`
`$` `pkill -f "Docker Desktop"`
```

Verify Docker is stopped.

```
`$` `docker ps`
```

**Linux:**

```
`$` `docker stop $(docker ps -q)`
`$` `sudo systemctl stop docker`
```

Verify Docker is stopped.

```
`$` `sudo systemctl status docker`
```

2. Run the `sam build --use-container` command to verify AWS SAM CLI automatically uses Finch as a fallback.

## Stopping Finch

If you need to stop Finch, use the following commands:

**macOS:**

```
`$` `finch vm stop`
`$` `sudo pkill -f finch`
```

Verify Finch is stopped.

```
`$` `finch vm status`
```

**Linux:**

```
`$` `sudo systemctl stop finch`
`$` `sudo pkill -f finch`
```

Verify Finch is stopped.

```
`$` `sudo systemctl status finch`
```

## Troubleshooting

If you encounter issues with Finch:

- Verify that your operating system meets the prerequisites.
- Verify that you have enabled virtualization on your system.
- For macOS, verify that you have sufficient disk space for the virtual machine.
- For Linux, verify that you have proper permissions to run `systemctl` commands.
- If you encounter AWS CloudFormation deployment failures with "media type not supported" errors when you push multi-architecture images to Amazon Elastic Container Registry (Amazon ECR), create a single image artifact instead of using multi-architecture images. This occurs because Finch pushes both the image index and image to Amazon ECR, while Docker pushes only the image.
- If cross-platform building fails when the target function architecture doesn't match the host machine architecture on Linux, enable cross-platform emulation by running `sudo finch run --privileged --rm tonistiigi/binfmt:master --install all`.

For additional troubleshooting, see the [Finch documentation](https://runfinch.com/docs/ "https://runfinch.com/docs/")
or the [AWS SAM CLI troubleshooting](sam-cli-troubleshooting.md "sam-cli-troubleshooting.md").

## Next steps

Now that you have Finch installed, you can use it with AWS SAM CLI to:

- Build serverless applications using containers with `sam build --use-container`.
  For more information, see [sam build](sam-cli-command-reference-sam-build.md "sam-cli-command-reference-sam-build.md").
- Test Lambda functions locally with `sam local invoke`. For more information, see
  [sam local invoke](sam-cli-command-reference-sam-local-invoke.md "sam-cli-command-reference-sam-local-invoke.md").
- Start a local API Gateway with `sam local start-api`. For more information, see [sam local start-api](sam-cli-command-reference-sam-local-start-api.md "sam-cli-command-reference-sam-local-start-api.md").
- Start a local Lambda endpoint with `sam local start-lambda`. For more information,
  see [sam local start-lambda](sam-cli-command-reference-sam-local-start-lambda.md "sam-cli-command-reference-sam-local-start-lambda.md").

For more information about using AWS SAM CLI with containers, see [Default build with AWS SAM](serverless-sam-cli-using-build.md "serverless-sam-cli-using-build.md").
