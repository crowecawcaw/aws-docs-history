End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Set up your local environment for SimSpace Weaver

SimSpace Weaver simulations run in containerized Amazon Linux 2 (AL2) environments.
You must have an AL2 environment to compile and link your apps with the SimSpace Weaver app SDK.
The standard local development environment is an AL2 container in Docker.
If you choose not to use Docker, we provide alternate instructions to run an AL2 environment
in Windows Subsystem for Linux (WSL). You can also use your own method to create a local AL2
environment. For some additional ways to run AL2 locally, see the [Amazon EC2 documentation](../../../AWSEC2/latest/UserGuide/amazon-linux-2-virtual-machine.md "../../../AWSEC2/latest/UserGuide/amazon-linux-2-virtual-machine.md").

###### Important

**Docker on Microsoft Windows is the standard development
environment.** For your convenience, we suggest other ways to set up your
local development environment, but they are not standard and are unsupported.

###### Topics

- [Set up the SimSpace Weaver distribution package for Amazon Linux 2 (AL2) in Docker](setting-up_local_docker.md "setting-up_local_docker.md")
- [Set up the SimSpace Weaver distribution package for Amazon Linux 2 (AL2) in Windows Subsystem for Linux (WSL)](setting-up_local_wsl.md "setting-up_local_wsl.md")
