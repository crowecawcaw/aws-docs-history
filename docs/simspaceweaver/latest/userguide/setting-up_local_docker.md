End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Set up the SimSpace Weaver distribution package for Amazon Linux 2 (AL2) in Docker

This section provides instructions for setting up your local SimSpace Weaver distribution zip with an AL2 environment in Docker.
For instructions to set up with AL2 in Windows Subsystem for Linux (WSL), see
[Set up the SimSpace Weaver distribution package for Amazon Linux 2 (AL2) in Windows Subsystem for Linux (WSL)](setting-up_local_wsl.md "setting-up_local_wsl.md").

###### Requirements

- Microsoft Windows 10 or higher, or a compatible Linux system
- [Microsoft
  Visual Studio 2019](https://learn.microsoft.com/en-us/visualstudio/releases/2019/release-notes "https://learn.microsoft.com/en-us/visualstudio/releases/2019/release-notes") or later, with the
  [_Desktop development
  with C++_](https://learn.microsoft.com/en-us/cpp/build/vscpp-step-0-installation?view=msvc-160 "https://learn.microsoft.com/en-us/cpp/build/vscpp-step-0-installation?view=msvc-160") workload installed
- [CMake3](https://cmake.org/download "https://cmake.org/download")
- [Git](https://git-scm.com/downloads "https://git-scm.com/downloads")
- [Docker Desktop](https://docs.docker.com/docker-for-windows/install "https://docs.docker.com/docker-for-windows/install")
- [AWS CLI](../../../cli/latest/userguide/install-cliv2.md "../../../cli/latest/userguide/install-cliv2.md")
- [Python 3.9](https://www.python.org/downloads/release/python-3913/ "https://www.python.org/downloads/release/python-3913/")

###### To set up the SimSpace Weaver distribution zip with AL2 in Docker

1. If you have not already configured your AWS credentials for the AWS CLI, follow these instructions:
   [Configuring the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md").
2. [Download the SimSpace Weaver app SDK distributable package](https://artifacts.simspaceweaver.us-east-2.amazonaws.com/latest/SimSpaceWeaverAppSdkDistributable.zip "https://artifacts.simspaceweaver.us-east-2.amazonaws.com/latest/SimSpaceWeaverAppSdkDistributable.zip"). It contains the
   following:
   - Binaries and libraries for SimSpace Weaver app development
   - Helper scripts that automate parts of the development workflow
   - Sample applications that demonstrate SimSpace Weaver concepts

3. Unzip the file to an `sdk-folder` of your choice.
4. Go to the `sdk-folder`.
5. Enter the following command to install the required Python packages:

```
pip install -r PackagingTools/python_requirements.txt
```

6. Enter the following command to setup the SimSpace Weaver distribution with a Docker image.

```
python setup.py
```

This command does the following:

    * Creates an AL2 docker image with all the requirements for building SimSpace Weaver projects installed.
    * Creates the CloudFormation resources required to launch a simulation.





    	+ The sample CloudFormation stack template can be found in ``sdk-folder`/PackagingTools/sample-stack-template.yaml`
    * Configures the provided sample projects with the correct paths for your local system.

## Troubleshooting

- Docker appears stuck
  - If the console output appears to be stuck after Docker commands are called, try restarting the Docker engine. If that doesn't work, restart your computer.
