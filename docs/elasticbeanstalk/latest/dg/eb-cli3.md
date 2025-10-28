# Setting up the EB command line interface (EB CLI) to manage Elastic Beanstalk

The EB CLI is a command line interface which provides interactive commands to create, update, and monitor environments in AWS Elastic Beanstalk. The EB CLI open-source project is on Github: `aws/aws-elastic-beanstalk-cli`

After you install the EB CLI and configure a project directory, you can create environments with a single command:

```
$ `eb create `my-beanstalk-environment``
```

We recommend installing with the setup script, learn how in [Install EB CLI with setup script (recommended)](#eb-cli3-install "#eb-cli3-install").

The AWS CLI provides direct access to low-level Elastic Beanstalk APIs. Although powerful, it is also verbose and less preferred over the EB CLI. For example, creating an environment with the AWS CLI requires the following series of commands:

```
$ `aws elasticbeanstalk check-dns-availability \
 --cname-prefix `my-cname``
$ `aws elasticbeanstalk create-application-version \
 --application-name `my-application` \
 --version-label `v1` \
 --source-bundle S3Bucket=`amzn-s3-demo-bucket,S3Key=php-proxy-sample.zip``
$ `aws elasticbeanstalk create-environment \
 --cname-prefix `my-cnam`e \
 --application-name `my-app` \
 --version-label `v1` \
 --environment-name `my-env` \
 --solution-stack-name "`64bit Amazon Linux 2023 v4.5.0 running Ruby 3.4`"`
```

## Install EB CLI with setup script (recommended)

###### We recommend the installer script

We recommend using the installer script to set up the EB CLI and its dependencies and
prevent potential conflicts with other Python packages.

Pre-requisites: Git, Python, and [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html "https://virtualenv.pypa.io/en/latest/installation.html")

###### To download and use the installer script

1. Clone the repository.

```
`git clone https://github.com/aws/aws-elastic-beanstalk-cli-setup.git`
```

2. Install or upgrade the EB CLI.

**macOS / Linux** in Bash or Zsh

```
`python ./aws-elastic-beanstalk-cli-setup/scripts/ebcli_installer.py`
```

**Windows** in PowerShell or Command window

```
`python .\aws-elastic-beanstalk-cli-setup\scripts\ebcli_installer.py`
```

3. Verify that the EB CLI is installed correctly.

```
$ `eb --version`
EB CLI 3.21.0 (Python 3.12)
```

For complete installation instructions, see the [`aws/aws-elastic-beanstalk-cli-setup`](https://github.com/aws/aws-elastic-beanstalk-cli-setup "https://github.com/aws/aws-elastic-beanstalk-cli-setup") repository on GitHub.

## Manually install the EB CLI

You can install the EB CLI on Linux, macOS, and Windows with the `pip` package
manager for Python which provides installation, upgrade, and removal of Python packages and
their dependencies.

###### We recommend the installer script

We recommend using the [Install EB CLI](#eb-cli3-install "#eb-cli3-install") to set up the EB CLI and prevent dependency
conflicts.

**Prerequisite** - You must have a supported version of
Python installed. You can download it from the [Python downloads](https://www.python.org/downloads/ "https://www.python.org/downloads/") page on the Python website.

###### To install the EB CLI (manually)

1. Run the following command.

```
$ `pip install awsebcli --upgrade --user`
```

The `--upgrade` option tells `pip` to upgrade any requirements
that are already installed. The `--user` option tells `pip` to
install the program to a subdirectory of your user directory to avoid modifying libraries
that your operating system uses.

###### Troubleshooting issues

If you encounter issues when you try to install the EB CLI with `pip`,
you can [install the EB CLI in a virtual
environment](#eb-cli3-install-virtualenv "#eb-cli3-install-virtualenv") to isolate the tool and its dependencies, or use a different
version of Python than you normally do. 2. Add the path to the executable file to your `PATH` variable:

    * On Linux and macOS:


    **Linux** – `~/.local/bin`


    **macOS** –
     `~/Library/Python/`3.12`/bin`


    To modify your `PATH` variable (Linux, Unix, or macOS ):


    	1. Find your shell's profile script in your user folder. If you are not sure which shell you
    	 have, run `echo $SHELL`.



    	```
    	$ `ls -a ~`
    	.  ..  .bash_logout  .bash_profile  .bashrc  Desktop  Documents  Downloads
    	```



    		+ **Bash** – `.bash_profile`,
    		 `.profile`, or `.bash_login`.
    		+ **Zsh** – `.zshrc`
    		+ **Tcsh** – `.tcshrc`,
    		 `.cshrc` or `.login`.
    	2. Add an export command to your profile script. The following example adds the path represented
    	 by `LOCAL_PATH` to the current `PATH` variable.



    	```
    	export PATH=`LOCAL_PATH`:$PATH
    	```
    	3. Load the profile script described in the first step into your current session. The
    	 following example loads the profile script represented by `PROFILE_SCRIPT`.




    	```
    	$ `source ~/`PROFILE_SCRIPT``
    	```
    * On Windows:


    **Python 3.12** –
     `%USERPROFILE%\AppData\Roaming\Python\Python312\Scripts`


    **Python earlier versions** –
     `%USERPROFILE%\AppData\Roaming\Python\Scripts`


    To modify your `PATH` variable (Windows):


    	1. Press the Windows key, and then enter `environment variables`.
    	2. Choose **Edit environment variables for your account**.
    	3. Choose **PATH**, and then choose **Edit**.
    	4. Add paths to the **Variable value** field, separated by semicolons. For example:
    	 ``C:\item1\path``;`C:\item2\path```
    	5. Choose **OK** twice to apply the new settings.
    	6. Close any running Command Prompt windows, and then reopen a Command Prompt window.

3. Verify that the EB CLI installed correctly by running **eb
   --version**.

```
$ `eb --version`
EB CLI 3.21.0 (Python 3.12)
```

The EB CLI is updated regularly to add functionality that supports [the latest Elastic Beanstalk features](../relnotes.md "../relnotes.md"). To update to the latest version
of the EB CLI, run the installation command again.

```
$ `pip install awsebcli --upgrade --user`
```

If you need to uninstall the EB CLI, use `pip uninstall`.

```
$ `pip uninstall awsebcli`
```

## Install the EB CLI in a virtual

environment

You can avoid version requirement conflicts with other `pip` packages by
installing the EB CLI in a virtual environment.

###### To install the EB CLI in a virtual environment

1. First, install `virtualenv` with `pip`.

```
$ `pip install --user virtualenv`
```

2. Create a virtual environment.

```
$ `virtualenv `~/eb-ve``
```

To use a Python executable other than the default, use the `-p` option.

```
$ `virtualenv -p /usr/bin/python3.12 `~/eb-ve``
```

3. Activate the virtual environment.

**Linux, Unix, or macOS**

```
$ `source `~/eb-ve`/bin/activate`
```

**Windows**

```
$ ``%USERPROFILE%\eb-ve`\Scripts\activate`
```

4. Install the EB CLI.

```
(eb-ve)$ `pip install awsebcli --upgrade`
```

5. Verify that the EB CLI is installed correctly.

```
$ `eb --version`
EB CLI 3.23.0 (Python 3.12)
```

You can use the `deactivate` command to exit the virtual environment. Whenever
you start a new session, run the activation command again.

To upgrade to the latest version, run the installation command again.

```
(eb-ve)$ `pip install awsebcli --upgrade`
```

## Install the EB CLI with homebrew

The latest version of the EB CLI is typically available from `Homebrew` a
couple of days after it appears in `pip`.

###### We recommend the installer script

We recommend using the [Install EB CLI](#eb-cli3-install "#eb-cli3-install") to set up the EB CLI and prevent dependency
conflicts.

###### To install the EB CLI with `Homebrew`

1. Ensure you have the latest version of `Homebrew`.

```
$ `brew update`
```

2. Run `brew install awsebcli`.

```
$ `brew install awsebcli`
```

3. Verify that the EB CLI is installed correctly.

```
$ `eb --version`
EB CLI 3.21.0 (Python 3.12)
```
