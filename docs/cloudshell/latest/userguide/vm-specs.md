# AWS CloudShell compute environment: specifications and software

When you launch AWS CloudShell, a compute environment that's based on [Amazon Linux 2023](https://aws.amazon.com/linux/amazon-linux-2023/ "https://aws.amazon.com/linux/amazon-linux-2023/") is created to host the
shell experience. The environment is configured with [compute
resources (vCPU and memory)](#vm-configuration "#vm-configuration") and provides a wide range of [pre-installed software](#pre-installed-software "#pre-installed-software") that can be accessed from the
command line interface.
Make sure that any software
you install in the compute environment is patched and up to date. You can also
configure your default environment by installing software and modifying shell scripts.

## Compute environment resources

Each AWS CloudShell compute environment is assigned the following CPU and memory resources:

- 1 vCPU (virtual central processing unit)
- 2-GiB RAM

And, the environment is provisioned with the following storage configuration:

- 1-GB persistent storage (storage persists after the session ends)

For more information, see [Persistent storage](limits.md#persistent-storage-limitations "limits.md#persistent-storage-limitations").

## CloudShell network requirements

**WebSockets**

CloudShell depends on the _WebSocket protocol_, which allows two-way
interactive communication between the user's web browser and the CloudShell service in the
AWS Cloud. If you're using a browser in a private network, secure access to the internet is
probably facilitated by proxy servers and firewalls. WebSocket communication can usually traverse
proxy servers without a problem. But in some cases, proxy servers prevent WebSockets from working
correctly. If this issue occurs, your CloudShell interface reports the following error:
`Failed to open sessions : Timed out while opening the session`.

If this error occurs repeatedly, see the documentation for your proxy server to ensure that
it's configured to allow WebSockets. Alternatively, you can contact your network's system
administrator.

###### Note

If you want to define granular permissions by allow-listing specific URLs, you can add part of
the URL that the AWS Systems Manager session uses to open a WebSocket connection for sending input and
receiving outputs. (Your AWS CloudShell commands are sent to that Systems Manager session.)

The format for this StreamUrl used by Systems Manager is `wss://ssmmessages.**region**.amazonaws.com/v1/data-channel/**session-id**?stream=(input|output)`.

The **region** represents the Region identifier for an AWS
Region supported by AWS Systems Manager, such as `us-east-2` for the US East (Ohio)
Region.

Because the **session-id** is created _after_ a particular Systems Manager session is successfully started, you can only specify
`wss://ssmmessages.region.amazonaws.com` when updating your URL allowlist.
For more information, see the [StartSession](../../../systems-manager/latest/APIReference/API_StartSession.md "../../../systems-manager/latest/APIReference/API_StartSession.md") operation
in the _AWS Systems Manager API Reference_.

## Pre-installed software

###### Note

Because the AWS CloudShell development environment is regularly updated to provide access to the
latest software, we don't provide specific version numbers in this documentation. Instead, we
describe how you can check which version is installed. To check the installed version, enter the
program name followed by the `--version` option (for example, `git
 --version`).

### Shells

| Pre-installed shells | Name                                                                                                                                                                                                                                        | Description      | Version information |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------- |
| Bash                 | The Bash shell is the default shell application for AWS CloudShell.                                                                                                                                                                         | `bash --version` |
| PowerShell (pwsh)    | Offering a command line interface and scripting language support, PowerShell is built on<br>top of Microsoft’s .NET Command Language Runtime. PowerShell uses lightweight commands called<br>`cmdlets` that accept and return .NET objects. | `pwsh --version` |
| Z Shell (zsh)        | The Z Shell, also known as `zsh`, is an extended version of the Bourne<br>Shell that offers enhanced customization support for themes and plugins.                                                                                          | `zsh --version`  |

### AWS command line interfaces (CLI)

| CLI                      | Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Description                                    | Version information |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------- | ------------------- |
| AWS CDK Toolkit CLI      | The AWS CDK Toolkit, the CLI command, `cdk`, is the primary tool that<br>interacts with your AWS CDK app. It executes your app, interrogates the application model you<br>defined, and produces and deploys the AWS CloudFormation templates generated by the AWS CDK.<br>For more information, see [AWS CDK Toolkit](../../../cdk/v2/guide/cli.md "../../../cdk/v2/guide/cli.md").                                                                                                                                                                                                                                                                                                  | `cdk --version`                                |
| AWS CLI                  | The AWS CLI is a command line interface that you can use to manage multiple AWS<br>services from the command line and automate them using scripts. For more information, see<br>[Manage AWS services from CLI in CloudShell](working-with-aws-cli.md "working-with-aws-cli.md"). For<br>information about how you can ensure that you're using the most up-to-date version AWS CLI<br>version 2, see [Installing AWS CLI to your home directory](#install-cli-software "#install-cli-software").                                                                                                                                                                                     | `aws --version`                                |
| EB CLI                   | The AWS Elastic Beanstalk CLI provides a command line interface to simplify creating, updating,<br>and monitoring environments from a local repository.<br>For more information, see [Using the Elastic<br>Beanstalk command line interface (EB CLI)](../../../elasticbeanstalk/latest/dg/eb-cli3.md "../../../elasticbeanstalk/latest/dg/eb-cli3.md") in the<br>_AWS Elastic Beanstalk Developer Guide_.                                                                                                                                                                                                                                                                            | `eb --version`                                 |
| Amazon ECS CLI           | Amazon Elastic Container Service (Amazon ECS) command line interface (CLI) provides high-level commands to<br>simplify creating, updating, and monitoring clusters and tasks.<br>For more information, see [Using the Amazon ECS<br>Command Line Interface](../../../AmazonECS/latest/developerguide/ECS_CLI.md "../../../AmazonECS/latest/developerguide/ECS_CLI.md") in the _Amazon Elastic Container Service Developer Guide_.                                                                                                                                                                                                                                                    | `ecs-cli --version`                            |
| AWS SAM CLI              | AWS SAM CLI is a command line tool that operates on an AWS Serverless Application Model template and<br>application code. You can perform several tasks. These include invoking Lambda functions<br>locally, creating a deployment package for your serverless application, and deploying your<br>serverless application to the AWS Cloud.<br>For more information, see the [AWS SAM CLI command<br>reference](../../../serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.md "../../../serverless-application-model/latest/developerguide/serverless-sam-cli-command-reference.md") in the _AWS Serverless Application Model Developer Guide_. | `sam --version`                                |
| AWS Tools for PowerShell | The AWS Tools for PowerShell are PowerShell modules that are built on the functionality exposed by<br>the SDK for .NET. With AWS Tools for PowerShell, you can script operations on your AWS resources from the<br>PowerShell command line.AWS CloudShell pre-installs the modularized version (AWS.Tools) of the<br>AWS Tools for PowerShell.For more information, see [Using the<br>AWS Tools for PowerShell](../../../powershell/latest/userguide/pstools-using.md "../../../powershell/latest/userguide/pstools-using.md") in the _AWS Tools for PowerShell User<br>Guide_.                                                                                                      | `pwsh --Command<br>'Get-AWSPowerShellVersion'` |

### Runtimes and AWS SDKs: Node.js and Python 3

| Runtimes and AWS SDKs         | Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Description                                                | Version information |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ------------------- |
| Node.js (with npm)            | Node.js is a JavaScript runtime that's designed to make it easier to apply<br>asynchronous programming techniques. For more information, see the [documentation on the official Node.js<br>site](https://nodejs.org/en/docs/ "https://nodejs.org/en/docs/").<br>npm is a package manager that provides access to an online registry of JavaScript<br>modules. For more information, see the [documentation<br>on the official npm site](https://docs.npmjs.com/ "https://docs.npmjs.com/").                                                                                                                                                                                             | • Node.js: `node --version`<br>• npm: `npm --version`      |
| SDK for JavaScript in Node.js | The software development kit (SDK) helps simplify coding by providing JavaScript<br>objects for AWS services including Amazon S3, Amazon EC2, DynamoDB, and Amazon SWF. For more information, see<br>the [AWS SDK for JavaScript Developer Guide](../../../sdk-for-javascript/latest/developer-guide.md "../../../sdk-for-javascript/latest/developer-guide.md").                                                                                                                                                                                                                                                                                                                       | `npm -g ls --depth 0 2>/dev/null                           | grep aws-sdk`       |
| Python                        | Python 3 is ready to use in the shell environment. Python 3 is now considered the<br>default version of the programming language (support for Python 2 ended in January 2020).<br>For more information, see the [documentation on the<br>official Python site](https://www.python.org/doc/ "https://www.python.org/doc/").<br>Also, pre-installed is pip, the package installer for Python. You can use this command<br>line program to install Python packages from the online indexes such as the Python Package<br>Index. For more information, see the [documentation provided by the Python Packaging Authority](https://pip.pypa.io/en/stable/ "https://pip.pypa.io/en/stable/"). | • Python 3: `python3 --version`<br>• pip: `pip3 --version` |
| SDK for Python (Boto3)        | Boto is the software development kit (SDK) that Python developers use to create,<br>configure, and manage AWS services, such as Amazon EC2 and Amazon S3. The SDK provides an<br>easy-to-use, object-oriented API, as well as low-level access to AWS services.<br>For more information, see the [Boto3<br>documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html "https://boto3.amazonaws.com/v1/documentation/api/latest/index.html").                                                                                                                                                                                                                     | `pip3 list                                                 | grep boto3`         |

### Development tools and shell utilities

| Development tools and shell utilities | Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Description                               | Version information |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | ------------------- |
| bash-completion                       | bash-completion is a collection of shell functions that allow the autocompletion of<br>partially typed commands or arguments by pressing the **Tab**<br>key. You can find the packages that bash-completion supports in<br>`/usr/share/bash-completion/completions`.<br>To set up autocomplete for a package's commands, the program file must be sourced. For<br>example, to set up autocomplete for Git commands, add the following line to<br>`.bashrc` so the feature is available whenever your AWS CloudShell session<br>starts:<br>`source /usr/share/bash-completion/completions/git`<br>If you want to use custom completion scripts, add them to your persistent home<br>directory (`$HOME`) and source them directly in<br>`.bashrc`.<br>For more information, see the project's [README](https://github.com/scop/bash-completion#readme "https://github.com/scop/bash-completion#readme") page on GitHub.         | `dnf info bash-completion`                |
| cqlsh-expansion                       | `cqlsh-expansion` is a toolkit that includes cqlsh and helpers that are<br>preconfigured for Amazon Keyspaces while maintaining full compatibility with Apache Cassandra. For more<br>information, see [Using<br>cqlsh to connect to Amazon Keyspaces](../../../keyspaces/latest/devguide/programmatic.md "../../../keyspaces/latest/devguide/programmatic.md") in _Amazon Keyspaces<br>(for Apache Cassandra) Developer Guide_.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `cqlsh-expansion --version`               |
| Docker                                | [Docker](https://docs.docker.com/guides/workshop/ "https://docs.docker.com/guides/workshop/") is an open<br>platform for developing, shipping and running applications. Docker enables you to separate<br>your applications from your infrastructure so you can deliver software quickly. It enables<br>you to build Dockerfiles inside AWS CloudShell, and build Docker assets with CDK. For information<br>about which AWS Regions are supported with Docker, see [Supported AWS Regions for AWS CloudShell](supported-aws-regions.md "supported-aws-regions.md"). You should be<br>aware that Docker has limited space in the environment. If you have large individual<br>images, or too many pre-existing Docker images, it can cause issues. For more information<br>on Docker, see the [Docker<br>Documentation guide](https://docs.docker.com/get-started/overview/ "https://docs.docker.com/get-started/overview/"). | `docker --version`                        |
| Git                                   | Git is a distributed version control system that supports modern software development<br>practices through branch workflows and content staging. For more information, see the<br>[documentation page on Git's official site](https://git-scm.com/doc "https://git-scm.com/doc").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `git --version`                           |
| iputils                               | The iputils package contains utilities for Linux networking. For more information<br>about the utilities provided, see the [iputils repository on GitHub](https://github.com/iputils/iputils "https://github.com/iputils/iputils").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Examples for an iputils tool: `arping -V` |
| jq                                    | The jq utility parses JSON-formatted data to produce output that's modified by command<br>line filters. For more information, see the [jq manual hosted on GitHub](https://stedolan.github.io/jq/manual/ "https://stedolan.github.io/jq/manual/").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `jq --version`                            |
| kubectl                               | kubectl is a command line tool for communicating with a Kubernetes cluster's control<br>plane, using the Kubernetes API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `kubectl --version`                       |
| make                                  | The make utility uses `makefiles` to automate sets of tasks and<br>organize code compilation. For more information, see the [GNU Make documentation](https://www.gnu.org/software/make/ "https://www.gnu.org/software/make/").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `make --version`                          |
| man                                   | The man command provides manual pages for command line utilities and tools. For<br>example, `man ls` returns the manual page for the `ls` command that<br>lists the contents of directories. For more information, see the [Wikipedia entry on man page](https://en.wikipedia.org/wiki/Man_page "https://en.wikipedia.org/wiki/Man_page").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `man --version`                           |
| nano                                  | nano is a small and user-friendly editor for text-based interface. For more<br>information, see the [GNU nano<br>documentation](https://www.nano-editor.org/docs.php "https://www.nano-editor.org/docs.php").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `nano --version`                          |
| OpenJDK 21                            | Amazon Corretto 21 is a Long-Term Supported (LTS) distribution of [OpenJDK 21](https://openjdk.org/projects/jdk/21/ "https://openjdk.org/projects/jdk/21/"). Amazon Corretto is a<br>no-cost, multiplatform, production-ready distribution of the Open Java Development Kit<br>(OpenJDK). For more information, see [What is Amazon Corretto 21?](../../../corretto/latest/corretto-21-ug/what-is-corretto-21.md "../../../corretto/latest/corretto-21-ug/what-is-corretto-21.md") in the _Corretto 21 User<br>Guide_.                                                                                                                                                                                                                                                                                                                                                                                                        | `java -version`                           |
| procps                                | procps is a system administration utility that you can use to monitor and halt<br>currently running processes. For more information, see [the README file that lists<br>programs that can be run with procps.](https://gitlab.com/procps-ng/procps/blob/master/README.md "https://gitlab.com/procps-ng/procps/blob/master/README.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `ps --version`                            |
| psql                                  | PostgreSQL is a powerful, open source database system that uses standard SQL<br>capabilities while providing robust features for securely managing and scaling complex data<br>operations. For more information, see [What is<br>PostgreSQL](https://www.postgresql.org/about/ "https://www.postgresql.org/about/").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `psql --version`                          |
| SSH client                            | SSH clients use the secure shell protocol for encrypted communications with a remote<br>computer. OpenSSH is the SSH client that's pre-installed. For more information, see the<br>[OpenSSH site](https://www.openssh.com/ "https://www.openssh.com/") maintained by the OpenBSD.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `ssh -V`                                  |
| sudo                                  | With the sudo utility, users can run a program with the security permissions of<br>another user, typically the superuser. Sudo is useful when you need to install applications<br>as a system administrator. For more information, see the [Sudo Manual](https://www.sudo.ws/man/1.8.14/sudo.man.html "https://www.sudo.ws/man/1.8.14/sudo.man.html").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `sudo --version`                          |
| tar                                   | tar is a command line utility that you can use to group multiple files in a single<br>archive file (often called a tarball). For more information, see the [GNU tar documentation](https://www.gnu.org/software/wget/manual/ "https://www.gnu.org/software/wget/manual/").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `tar --version`                           |
| tmux                                  | tmux is a terminal multiplexer that you can use to run different programs simultaneous<br>in multiple windows. For more information, see [a blog that provides a<br>concise introduction to tmux](https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/ "https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `tmux -V`                                 |
| vim                                   | vim is a customizable editor that you can interact with through a text-based<br>interface. For more information, see the [documentation resources provided on vim.org](https://www.vim.org/docs.php "https://www.vim.org/docs.php").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `vim --version`                           |
| wget                                  | wget is a computer program used to retrieve content from web servers specified by<br>endpoints in the command line. For more information, see the [GNU Wget documentation](https://www.gnu.org/software/wget/manual/ "https://www.gnu.org/software/wget/manual/").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `wget --version`                          |
| zip/unzip                             | The zip/unzip utilities use an archive file format that delivers lossless data<br>compression without data loss. Call the zip command to group and compress files in a single<br>archive. Use unzip to extract files from an archive into a specified directory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `unzip --version`<br>`zip --version`      |

## Installing AWS CLI to your home directory

Like the rest of the software that's pre-installed in your CloudShell environment, the
AWS CLI tool is updated automatically with scheduled upgrades and security patches. If you want to
ensure that you have the most up-to-date version of AWS CLI, you can choose to manually install the
tool in the shell's home directory.

###### Important

You need to manually install your copy of AWS CLI in the home directory so that it's
available the next time you start a CloudShell session. This installation is needed because
files that are added to directories outside of `$HOME` are deleted after you
finish a shell session. Also, after you install this copy of AWS CLI, it isn't automatically
updated. In other words, it's your responsibility to manage updates and security patches.

For more information about the AWS Shared Responsibility Model, see [Data protection in AWS CloudShell](data-protection.md "data-protection.md").

###### To install AWS CLI

1. In the CloudShell command line, use the `curl` command to transfer a zipped
   copy of the AWS CLI installed to the shell:

```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
```

2. Unzip the zipped folder:

```
unzip awscliv2.zip
```

3. To add the tool to a specified folder, run the AWS CLI installer:

```
sudo ./aws/install --install-dir /home/cloudshell-user/usr/local/aws-cli --bin-dir /home/cloudshell-user/usr/local/bin
```

If it's installed successfully, the command line displays the following message:

```
You can now run: /home/cloudshell-user/usr/local/bin/aws --version
```

4. For your own convenience, we recommend that you also update the `PATH`
   environmental variable so that you don't need to specify the path to your installation of the
   tool when running `aws` commands:

```
export PATH=/home/cloudshell-user/usr/local/bin:$PATH
```

###### Note

If you undo this change to `PATH`, `aws` commands that
don't feature a specified path use the pre-installed version of AWS CLI by default.

## Installing third-party software on your shell

environment

###### Note

We recommend that you review the [Shared Security Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") before you install any third-party applications
to the AWS CloudShell's compute environment.

By default, all AWS CloudShell users have sudo permissions. Therefore, you can use the
`sudo` command to install software that's not already available in the shell's
compute environment. For example, you can use `sudo` with the DNF package-management
utility to install `cowsay`, which generates ASCII art pictures of a cow with a
message:

```
sudo dnf install cowsay
```

You can then launch the newly installed program by typing `echo "Welcome to AWS
 CloudShell" | cowsay`.

###### Important

Package manage utilities such as dnf install programs in directories
(`/usr/bin`, for example), which are recycled when your shell session ends.
This means additional software is installed and used on a per-session basis.

## Modifying your shell with scripts

If you want to modify the default shell environment, you can edit a shell script that runs
every time the shell environment starts up. The `.bashrc` script runs whenever
the default bash shell starts up.

###### Warning

If you incorrectly modify your `.bashrc` file, you might not be able to
access your shell environment afterward. It's good practice to make a copy of the file before
editing. You can also mitigate risk by opening two shells when editing
`.bashrc`. If you lose access in one shell, you're still logged in into the
other shell and can roll back any changes.

If you do lose access after incorrectly modifying `.bashrc` or any other
file, you can return AWS CloudShell to its default settings by [deleting your home directory](getting-started.md#delete-shell-session "getting-started.md#delete-shell-session").

In the procedure, you'll modify the `.bashrc` script so that your shell
environment switches automatically to running the Z shell.

1. Open the `.bashrc` using a text editor (Vim, for example):

```
vim .bashrc
```

2. In the editor interface, press the **I** key to start
   editing, and then add the following:

```
zsh
```

3. To exit and save the edited `.bashrc` file, press
   **Esc** to enter the Vim command mode and enter the following:

`:wq` 4. Use the `source` command to reload the `.bashrc`
file:

```
source .bashrc
```

When the command line interface becomes available again, the prompt symbol has changed to
`%` to indicate that you're now using the Z shell.
