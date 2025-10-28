# Setting up your Python development environment for Elastic Beanstalk

This topic provides instructions to set up a Python development environment to test your application locally prior to deploying it to AWS Elastic Beanstalk.
It also references websites that provide installation instructions for useful tools.

To follow the procedures in this guide, you will need a command line terminal or shell to run commands. Commands are shown in
listings preceded by a
prompt symbol ($) and the name of the current directory, when appropriate.

```
~/eb-project$ `this is a command`
this is output
```

On Linux and macOS, you can use your preferred shell and package manager. On Windows you can [install the Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10 "https://docs.microsoft.com/en-us/windows/wsl/install-win10") to get a Windows-integrated version of
Ubuntu and Bash.

###### Sections

- [Prerequisites](#python-common-prereq "#python-common-prereq")
- [Using a virtual environment](#python-common-setup-venv "#python-common-setup-venv")
- [Configuring a Python project for Elastic Beanstalk](#python-common-configuring "#python-common-configuring")

## Prerequisites

The following list provides the common prerequisites for working with Elastic Beanstalk and your Python applications:

- Python language – Install the version of the Python language that's included on your chosen Elastic Beanstalk Python
  platform version. For a list of our supported Python language versions, see [Supported Python platforms](../platforms/platforms-supported.md#platforms-supported.python "../platforms/platforms-supported.md#platforms-supported.python") in the
  _AWS Elastic Beanstalk Platforms_ guide. If you don't already have Python set up on your development machine, see the [Python downloads](https://www.python.org/downloads/ "https://www.python.org/downloads/") page on the Python website.
- `pip` utility – The `pip` utility is Python's package installer. It installs and lists
  dependencies for your project, so that Elastic Beanstalk knows how to set up your application's environment. For more information about `pip`,
  see the [pip page](https://pip.pypa.io/en/stable/ "https://pip.pypa.io/en/stable/") on the _pip.pypa.io_ website.
- (Optional) The Elastic Beanstalk Command Line Interface (EB CLI) – The [EB CLI](eb-cli3.md "eb-cli3.md") can package
  your application with the necessary deployment files. It can also create an Elastic Beanstalk environment and deploy your application to it. You can also make
  deployments via the Elastic Beanstalk console, so the EB CLI is not strictly necessary.
- A working `SSH` installation – You can connect to your running instances with the SSH protocol to
  examine or debug a deployment.
- `virtualenv` package – This `virtualenv` tool creates a development and test
  environment for your application. Elastic Beanstalk can replicate this environment without installing extra packages that aren't required by your application. For
  more information, see the [virtualenv](https://virtualenv.pypa.io/en/latest/ "https://virtualenv.pypa.io/en/latest/") website. After installing Python, you can install
  `virtualenv` package with the following command:

```
$ `pip install virtualenv`
```

## Using a virtual environment

Once you have the prerequisites installed, set up a virtual environment with `virtualenv` to install your application's dependencies. By
using a virtual environment, you can discern exactly which packages are needed by your application so that the required packages are installed on the EC2
instances that are running your application.

###### To set up a virtual environment

1. Open a command-line window and type:

```
$ `virtualenv /tmp/`eb_python_app``
```

Replace `eb_python_app` with a name that makes sense for your application (using your application's name is a good idea).
The `virtualenv` command creates a virtual environment for you in the specified directory and prints the results of its actions:

```
Running virtualenv with interpreter /usr/bin/python
New python executable in /tmp/eb_python_app/bin/python3.12
Also creating executable in /tmp/eb_python_app/bin/python
Installing setuptools, pip...done.
```

2. Once your virtual environment is ready, start it by running the `activate` script located in the environment's `bin`
   directory. For example, to start the **eb_python_app** environment created in the previous step, you would type:

```
$ `source /tmp/eb_python_app/bin/activate`
```

The virtual environment prints its name (for example: `(eb_python_app)`) at the beginning of each command prompt, reminding you that
you're in a virtual Python environment. 3. To stop using your virtual environment and go back to the system’s default Python interpreter with all its installed libraries, run the
`deactivate` command.

```
(eb_python_app) $ `deactivate`
```

###### Note

Once created, you can restart the virtual environment at any time by running its `activate` script again.

## Configuring a Python project for Elastic Beanstalk

You can use the Elastic Beanstalk CLI to prepare your Python applications for deployment with Elastic Beanstalk.

###### To configure a Python application for deployment with Elastic Beanstalk

1. From within your [virtual environment](#python-common-setup-venv "#python-common-setup-venv"), return to the top of your project's directory tree
   (`python_eb_app`), and type:

```
pip freeze >requirements.txt
```

This command copies the names and versions of the packages that are installed in your virtual environment to
`requirements.txt`, For example, if the _PyYAML_ package, version _3.11_ is installed in your
virtual environment, the file will contain the line:

```
PyYAML==3.11
```

This allows Elastic Beanstalk to replicate your application's Python environment using the same packages and same versions that you used to develop and test
your application. 2. Configure the EB CLI repository with the **eb init** command. Follow the prompts to choose a region, platform and other options.

By default, Elastic Beanstalk looks for a file called `application.py` to start your application. If this doesn't exist in the Python project that
you've created, some adjustment of your application's environment is necessary. You will also need to set environment variables so that your application's
modules can be loaded. See [Using the Elastic Beanstalk Python platform](create-deploy-python-container.md "create-deploy-python-container.md") for more information.
