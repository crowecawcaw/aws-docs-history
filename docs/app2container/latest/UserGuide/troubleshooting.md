AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Troubleshooting App2Container issues

The following documentation can help you troubleshoot problems that you might have with the App2Container CLI.

###### Contents

- [Access App2Container logs on your server](#troubleshooting-access-server-logs "#troubleshooting-access-server-logs")
- [Access application logs inside of a running container](#troubleshooting-access-container-logs "#troubleshooting-access-container-logs")
- [AWS resource creation fails for the generate command](#troubleshooting-aws-access "#troubleshooting-aws-access")
- [Troubleshoot Java applications on Linux](#troubleshooting-linux "#troubleshooting-linux")
- [Troubleshoot .NET applications on Windows](#troubleshooting-windows "#troubleshooting-windows")
- [Troubleshoot generate pipeline build for Jenkins](#troubleshooting-jenkins-a2c-pipeline "#troubleshooting-jenkins-a2c-pipeline")

## Access App2Container logs on your server

A common first step in troubleshooting issues with any application is reviewing
application logs. App2Container logs contain a history of the information and error messages
that are produced by the commands that you run. If you opted out of metrics during
initialization, the metrics messages are also logged in the local application log
file.

Review log files in one of the following locations, depending on where you are running the command that
needs troubleshooting:

###### Application logs

- **Linux:** `/root/app2container/log/app2container.log`
- **Windows:** `C:\Users\Administrator\AppData\Local\app2container\log\app2container.log`

###### Upgrade logs

- **Linux:** `/usr/local/app2container/log/app2container_upgrade.log`
- **Windows:** `C:\Users\Administrator\app2container\log\app2container_upgrade.log`

If there is more than one log file, it means that the first log file reached its maximum size, and a new
log file was created to continue logging. Choose the most recent log file to troubleshoot.

## Access application logs inside of a running container

You can access application logs on your running container by running a command shell from the container
host that attaches to your container. Choose the tab that matches your container operating system to see
the command.

Linux
From the host server, run an interactive bash shell on your running
container.

```
`$` `docker exec -it `container-id` bash`
```

Using the bash shell, you can then navigate to the location where your application logs are
stored.

Windows
From the host server, run an interactive PowerShell session attached to your running container.

```
`PS>` `docker exec -it `container-id` powershell.exe`
```

Using the PowerShell session, you can then navigate to the location where your application logs are
stored.

To look up Docker commands, use the Docker command line reference. See
[Use the Docker command line](https://docs.docker.com/engine/reference/commandline/cli/ "https://docs.docker.com/engine/reference/commandline/cli/").

## AWS resource creation fails for the generate command

### Description

When you run the **generate app-deployment** or **generate pipeline** command, you receive an error
message saying AWS resource creation has failed.

### Cause

App2Container requires permission to access and create AWS resources when it generates
and deploys application containers or pipelines. If the permission has not been
configured in your IAM policy, or if you are using the default AWS profile for a
command using the `--deploy` option, the command will fail.

### Solution

Verify your IAM resources and AWS profile settings and adjust as necessary, depending on the command that
failed and the details shown in your error message. For more information and instructions about how to
set up IAM resources for App2Container, see [Identity and access management in App2Container](iam-a2c.md "iam-a2c.md").

## Troubleshoot Java applications on Linux

This section contains issues you might have with using App2Container for Java applications
running on Linux servers.

###### Note

The App2Container **containerize** command creates a Dockerfile,
along with other deployment artifacts. To reduce container sizes for Java applications, the
Dockerfile installs the Java Runtime Environment (JRE) on your container
by default. If your application requires the Java Development Kit (JDK)
instead, you can edit your Dockerfile to change it. Your container
size will be affected.

Edit the Dockerfile in your application directory
(`<app2container workspace>/<app ID>/Artifacts/Dockerfile`)
as follows:

###### Configure Dockerfile to use JDK

1. Locate the line that installs the JRE and change it to install the JDK.
   The change that you make depends on your container base image.
   For example, if your container uses an `Ubuntu` or
   `Debian` base image, you would change the package name
   from `openjdk-<version>-jre` to
   `openjdk-<version>-jdk`.
2. Re-run the **containerize** command, using the
   `--build-only` option, which instructs App2Container to recreate
   the container using the existing build artifacts.

```
`$` `sudo app2container containerize --application-id `java-tomcat-9e8e4799` --build-only`
```

#### Description

Your application container image is much larger than expected.

#### Cause

The application container image includes a kernel image with the application bits layered on top.
The size of the image depends on both the size of the container operating system and the size of the
application.

To catch all potential dependencies for Java applications on Linux that are not using JBoss or Tomcat
frameworks, the container initially includes everything except the files that are already included
in the kernel image.

#### Solution

Follow these steps to reduce the size of your application container image.

1. Use the `appExcludedFiles` section in your `analysis.json`
   file to exclude specific file and directory paths from the containerization process, and
   save the file when you are done.
2. Run the **[containerize](cmd-containerize.md "cmd-containerize.md")** command
   again to create a new application container image with the updates
   that you specified.

You can repeat this process as needed to further reduce the size.

#### Description

When you run the **containerize** command, it fails with the following error message:
**`Error: Insufficient disk space`**.

#### Cause

For Java applications running on Linux, App2Container calculates the disk
space that is required to generate the application container, and produces
this error message if there is not enough free space. The calculation
includes the space needed for the application archive (including all
non-system files on the server), plus the space needed for **docker
build** actions.

#### Solution

The error message generated by the **containerize** command
includes the estimated space it needs to run successfully. There are many
ways to address an insufficient space issue on Linux.

One way to ensure that your **containerize** command runs
successfully is to reduce the size of the container that you are creating.
Follow these steps to reduce the size of your application container
image.

1. Use the `appExcludedFiles` section in your `analysis.json`
   file to exclude specific file and directory paths from the containerization process, and save
   the file when you are done.
2. Run the **[containerize](cmd-containerize.md "cmd-containerize.md")** command
   again to create a new application container image with the updates
   that you specified.

You can repeat this process as needed to further reduce the size.

## Troubleshoot .NET applications on Windows

This section contains issues you might have with using App2Container for .NET applications
running in IIS on Windows servers.

#### Description

Your application container image is much larger than expected.

#### Cause

The application container image includes a kernel image with the application bits layered on top.
The size of the image depends on both the size of the container operating system and the size of the
application. The Windows Server Core image can be quite large, especially for versions prior to
Windows Server Core 2019.

#### Solution

We recommend that you use Windows Server Core 2019 for your container operating system to create the
smallest base container size possible.

Follow these steps to reduce the size of your application container image if you are not currently using
Windows Server Core 2019 as your base image. To ensure that you get the correct version, specify the version
tag as shown below. The repository for Windows base images does not support the concept of "latest" to target
the most recent image version.

1. Use the `containerBaseImage` section in your `analysis.json`
   file to target the Windows Server Core 2019 base image tagged as `ltsc2019` and save
   the file when you are done.

The `containerBaseImage` value includes both the image name and the `ltsc2019` tag,
separated by a colon (:). For example:
`"containerBaseImage": "mcr.microsoft.com/dotnet/framework/aspnet:4.7.2-windowsservercore-ltsc2019"`. 2. Run the **[containerize](cmd-containerize.md "cmd-containerize.md")** command
again to create a new application container image. It will use the
container operating system image that you specify in the
`containerBaseImage` of your
`analysis.json` file to build a new
application container image.

## Troubleshoot generate pipeline build for Jenkins

This section contains issues you might have for your App2Container pipeline build that is configured for Jenkins.
As with any other troubleshooting scenario, the first step should be to review your application logs.
For more information, see [Access App2Container logs on your server](#troubleshooting-access-server-logs "#troubleshooting-access-server-logs").

#### Description

Your Jenkins Windows agent, or the Jenkins server, if it's running on Windows is
not able to connect to your CodeCommit repository to perform Git operations.

#### Cause

Pre-conditions:

- You are running the **generate pipeline** command
  with the `--deploy` option to deploy a Jenkins pipeline.
- You are deploying the pipeline for a Windows application.
- You have CodeCommit configured as your Jenkins code repository.

When the **generate pipeline** command runs with the
`--deploy` option, App2Container detects the code repository that you
have configured for Jenkins. If CodeCommit is your Jenkins code repository, App2Container
generates an SSH-RSA key for the Jenkins server or Windows agent to connect
to the CodeCommit repository for Git operations.

If OpenSSH on your Jenkins server or Windows agent is not configured to
accept RSA-encrypted keys, your **generate pipeline** build
fails with an error message that is similar to this example:

```
`Unable to negotiate with `11.22.333.444` port 22: no matching host key type found. Their offer: ssh-rsa`
```

#### Solution

To configure OpenSSH in your Jenkins environment, add the following
configuration to your user profile `%userprofile%/.ssh/config`
on Jenkins Windows agents, and also on the Jenkins server, if it is running
on Windows.

```
Host git-codecommit.*.amazonaws.com
   HostkeyAlgorithms +ssh-rsa
   PubkeyAcceptedKeyTypes +ssh-rsa
```

###### Note

- If your Jenkins server is running on Windows, update
  the user profile that you ran the Jenkins setup with.
- For Jenkins Windows agents, update the user profile
  that has your connection to the Jenkins server configured.
