# Managing AWS SAM CLI versions

Manage your AWS Serverless Application Model Command Line Interface (AWS SAM CLI) versions through upgrading,
downgrading, and uninstalling. Optionally, you can download and install the AWS SAM CLI nightly
build.

###### Topics

- [Upgrading the AWS SAM CLI](#manage-sam-cli-versions-upgrade "#manage-sam-cli-versions-upgrade")
- [Uninstalling the AWS SAM CLI](#manage-sam-cli-versions-uninstall "#manage-sam-cli-versions-uninstall")
- [Switch from using Homebrew to manage the AWS SAM CLI](#manage-sam-cli-versions-switch "#manage-sam-cli-versions-switch")
- [Managing the AWS SAM CLI nightly build](#manage-sam-cli-versions-nightly-build "#manage-sam-cli-versions-nightly-build")
- [Installing the AWS SAM CLI into a virtual environment using
  pip](#manage-sam-cli-versions-install-virtual "#manage-sam-cli-versions-install-virtual")
- [Managing the AWS SAM CLI with Homebrew](#manage-sam-cli-versions-homebrew "#manage-sam-cli-versions-homebrew")
- [Troubleshooting](#manage-sam-cli-versions-troubleshoot "#manage-sam-cli-versions-troubleshoot")

## Upgrading the AWS SAM CLI

To upgrade the AWS SAM CLI on Linux, follow the installation instructions in [Installing the AWS SAM CLI](install-sam-cli.md#install-sam-cli-instructions "install-sam-cli.md#install-sam-cli-instructions"),
but add the `--update` option to the install command, as follows:

```
`sudo ./sam-installation/install --update`
```

The AWS SAM CLI must be upgraded through the same method used to install it. We recommend that you use the package
installer to install and upgrade the AWS SAM CLI.

To upgrade the AWS SAM CLI using the package installer, install the latest package version. For instructions,
see [Installing the AWS SAM CLI](install-sam-cli.md#install-sam-cli-instructions "install-sam-cli.md#install-sam-cli-instructions").

To upgrade the AWS SAM CLI, repeat the Windows installation steps in [Install the AWS SAM CLI](install-sam-cli.md "install-sam-cli.md") again.

## Uninstalling the AWS SAM CLI

To uninstall the AWS SAM CLI on Linux, you must delete the symlink and installation
directory by running the following commands:

1. Locate the symlink and install paths.
   - Find the symlink using the **which** command:

   ```
   `which sam`
   ```

   The output shows the path where the AWS SAM binaries are located, for
   example:

   ```
    /usr/local/bin/sam
   ```

   - Find the directory that the symlink points to using the **ls**
     command:

   ```
   `ls -l /usr/local/bin/sam`
   ```

   In the following example, the installation directory is
   `/usr/local/aws-sam-cli`.

   ```
    lrwxrwxrwx 1 ec2-user ec2-user 49 Oct 22 09:49 /usr/local/bin/sam -> /usr/local/aws-sam-cli/current/bin/sam
   ```

2. Delete the symlink.

```
`sudo rm /usr/local/bin/sam`
```

3. Delete the installation directory.

```
`sudo rm -rf /usr/local/aws-sam-cli`
```

Uninstall the AWS SAM CLI through the same method that was used to install it. We recommend that you use the
package installer to install the AWS SAM CLI.

If you installed the AWS SAM CLI using the package installer, follow these steps to uninstall.

###### To uninstall the AWS SAM CLI

1. Remove the AWS SAM CLI program by modifying and running the following:

```
`$` ``sudo` rm -rf `/path-to`/aws-sam-cli`
```

    1. `sudo` – If your user has write permissions to where the
     AWS SAM CLI program is installed, **sudo** is not required. Otherwise,
     **sudo** is required.
    2. `/path-to` – Path to where you installed the AWS SAM CLI program.
     The default location is `/usr/local`.

2. Remove the AWS SAM CLI `$PATH` by modifying and running the following:

```
`$` ``sudo` rm -rf `/path-to-symlink-directory`/sam`
```

    1. `sudo` – If your user has write permissions to `$PATH`,
     **sudo** is not required. Otherwise, **sudo** is required.
    2. `path-to-symlink-directory` – Your `$PATH` environment
     variable. The default location is `/usr/local/bin`.

3. Verify that the AWS SAM CLI is uninstalled by running the following:

```
`$` `sam --version`
command not found: sam
```

To uninstall the AWS SAM CLI using Windows Settings, follow these steps:

1. From the Start menu, search for "Add or remove programs".
2. Choose the result named **AWS SAM Command Line Interface**, and
   then choose **Uninstall** to launch the uninstaller.
3. Confirm that you want to uninstall the AWS SAM CLI.

## Switch from using Homebrew to manage the AWS SAM CLI

If you use Homebrew to install and upgrade the AWS SAM CLI, we recommend using an AWS
supported method. Follow these instructions to switch to a supported method.

###### To switch from using Homebrew

1. Follow instructions at [Uninstalling a Homebrew installed AWS SAM
   CLI](#manage-sam-cli-versions-homebrew-uninstall "#manage-sam-cli-versions-homebrew-uninstall") to uninstall the Homebrew managed
   version.
2. Follow instructions at [Install the AWS SAM CLI](install-sam-cli.md "install-sam-cli.md") to install the AWS SAM
   CLI using a supported method.

## Managing the AWS SAM CLI nightly build

You can download and install the AWS SAM CLI nightly build. It contains a pre-release
version of the AWS SAM CLI code that may be less stable than the production version. When
installed, you can use the nightly build with the `sam-nightly` command. You
can install and use both the production and nightly build versions of the AWS SAM CLI at the
same time.

###### Note

The nightly build does not contain a pre-release version of the build image. Because of
that, building your serverless application with the **--use-container**
option uses the latest production version of the build image.

### Installing the AWS SAM CLI nightly build

To install the AWS SAM CLI nightly build, follow these instructions.

You can install the nightly build version of the AWS SAM CLI on the Linux x86_64 platform
using the package installer.

###### To install the AWS SAM CLI nightly build

1. Download the package installer from [sam-cli-nightly](https://github.com/aws/aws-sam-cli/releases/sam-cli-nightly/ "https://github.com/aws/aws-sam-cli/releases/sam-cli-nightly/") in the
   _aws-sam-cli GitHub repository_.
2. Follow the steps for [installing the AWS SAM CLI](install-sam-cli.md "install-sam-cli.md") to install the nightly
   build package.
   You can install the nightly build version of the AWS SAM CLI on macOS, using the nightly build
   package installer.

###### To install the AWS SAM CLI nightly build

1. Download the package installer for your platform from [sam-cli-nightly](https://github.com/aws/aws-sam-cli/releases/sam-cli-nightly/ "https://github.com/aws/aws-sam-cli/releases/sam-cli-nightly/") in the
   _aws-sam-cli GitHub repository_.
2. Follow the steps for [installing the AWS SAM CLI](install-sam-cli.md "install-sam-cli.md") to install the nightly
   build package.
   The nightly build version of the AWS SAM CLI is available with this download link:
   [AWS SAM CLI nightly build](https://github.com/aws/aws-sam-cli/releases/download/sam-cli-nightly/AWS_SAM_CLI_64_PY3.msi "https://github.com/aws/aws-sam-cli/releases/download/sam-cli-nightly/AWS_SAM_CLI_64_PY3.msi"). To install the nightly build on Windows, perform the
   same steps as in the [Install the AWS SAM CLI](install-sam-cli.md "install-sam-cli.md"),
   but use the nightly build download link instead.

To verify that you have installed the nightly build version, run the
**sam-nightly --version** command. The output of this command is in the
form `1.X.Y.dev<YYYYMMDDHHmm>`, for example:

```
SAM CLI, version 1.20.0.dev202103151200
```

### Switch from Homebrew to the package

installer

If you are using Homebrew to install and upgrade the AWS SAM CLI nightly build and would like to
switch to using the package installer, follow these steps.

###### To switch from Homebrew to the package installer

1. Uninstall the Homebrew installed AWS SAM CLI nightly build.

```
`$` `brew uninstall aws-sam-cli-nightly`
```

2. Verify that the AWS SAM CLI nightly build is uninstalled by running the following:

```
`$` `sam-nightly --version`
zsh: command not found: sam-nightly
```

3. Follow steps in the previous section to install the AWS SAM CLI nightly build.

## Installing the AWS SAM CLI into a virtual environment using

pip

We recommend using the native package installer to install the AWS SAM CLI. If you must use pip, we
recommend that you install the AWS SAM CLI into a virtual environment. This ensures a clean installation environment and
an isolated environment if errors occur.

###### Note

As of October 24, 2023, the AWS SAM CLI is discontinuing support for Python 3.7. To
learn more, see [AWS SAM CLI discontinuing support for Python 3.7](important-notes.md#important-notes-2023-10-python "important-notes.md#important-notes-2023-10-python").

###### To install the AWS SAM CLI into a virtual environment

1. From a starting directory of your choice, create a virtual environment and name it.

Linux / macOS

```
`$` `mkdir `project``
`$` `cd `project``
`$` `python3 -m venv `venv``
```

Windows

```
`>` `mkdir `project``
`>` `cd `project``
`>` `py -3 -m venv `venv``
```

2. Activate the virtual environment

Linux / macOS

```
`$` `. `venv`/bin/activate`
```

The prompt changes to show you that your virtual environment is active.

```
`(venv) $`
```

Windows

```
`>` ``venv`\Scripts\activate`
```

The prompt changes to show you that your virtual environment is active.

```
`(venv) >`
```

3. Install the AWS SAM CLI into your virtual environment.

```
`(venv) $` `pip install --upgrade aws-sam-cli`
```

4. Verify that the AWS SAM CLI is installed correctly.

```
`(venv) $` `sam --version`
SAM CLI, version `1.94.0`
```

5. You can use the `deactivate` command to exit the virtual environment. Whenever you start a new
   session, you must reactivate the environment.

## Managing the AWS SAM CLI with Homebrew

###### Note

Starting September 2023, AWS will no longer maintain the AWS managed Homebrew installer for the AWS SAM CLI
(`aws/tap/aws-sam-cli`). To continue using Homebrew, you can use the community managed
installer (`aws-sam-cli`). From September 2023, any Homebrew command that references
`aws/tap/aws-sam-cli` will redirect to `aws-sam-cli`.

We recommend that you use our supported [installation](install-sam-cli.md "install-sam-cli.md") and [upgrade](#manage-sam-cli-versions-upgrade "#manage-sam-cli-versions-upgrade") methods.

### Installing the AWS SAM CLI using Homebrew

###### Note

These instructions use the community managed AWS SAM CLI Homebrew installer. For further support,
see the _[homebrew-core](https://github.com/Homebrew/homebrew-core/issues "https://github.com/Homebrew/homebrew-core/issues")
repository_.

###### To install the AWS SAM CLI

1. Run the following:

```
`$` `brew install aws-sam-cli`
```

2. Verify the installation:

```
`$` `sam --version`
```

After successful installation of the AWS SAM CLI, you should see output like the following:

```
SAM CLI, version `1.94.0`
```

### Upgrading the AWS SAM CLI using Homebrew

To upgrade the AWS SAM CLI using Homebrew, run the following command:

```
`$` `brew upgrade aws-sam-cli`
```

### Uninstalling a Homebrew installed AWS SAM

CLI

If the AWS SAM CLI was installed using Homebrew, follow these steps to uninstall
it.

###### To uninstall the AWS SAM CLI

1. Run the following:

```
`$` `brew uninstall aws-sam-cli`
```

2. Verify that the AWS SAM CLI is uninstalled by running the following:

```
`$` `sam --version`
command not found: sam
```

### Switching to the community managed

Homebrew installer

If you are using the AWS managed Homebrew installer (`aws/tap/aws-sam-cli`) and prefer
to continue using Homebrew, we recommend switching to the community managed Homebrew
installer (`aws-sam-cli`).

To switch in a single command, run the following:

```
`$` `brew uninstall aws-sam-cli && brew untap aws/tap && brew cleanup aws/tap && brew update && brew install aws-sam-cli`
```

Follow these instructions to run each command individually.

###### To switch to the community managed Homebrew installer

1. Uninstall the AWS managed Homebrew version of the AWS SAM CLI:

```
`$` `brew uninstall aws-sam-cli`
```

2. Verify that the AWS SAM CLI has been uninstalled:

```
`$` `which sam`
sam not found
```

3. Remove the AWS managed AWS SAM CLI tap:

```
`$` `brew untap aws/tap`
```

If you receive an error like the following, add the `--force` option and try again.

```
Error: Refusing to untap aws/tap because it contains the following installed formulae or casks:
aws-sam-cli-nightly
```

4. Remove cached files for the AWS managed installer:

```
`$` `brew cleanup aws/tap`
```

5. Update Homebrew and all formulae:

```
`$` `brew update`
```

6. Install the community managed version of the AWS SAM CLI:

```
`$` `brew install aws-sam-cli`
```

7. Verify that the AWS SAM CLI is successfully installed:

```
`$` `sam --version`
SAM CLI, version `1.94.0`
```

## Troubleshooting

If you come across errors when installing or using the AWS SAM CLI, see [AWS SAM CLI troubleshooting](sam-cli-troubleshooting.md "sam-cli-troubleshooting.md").
