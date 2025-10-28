End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Set up the SimSpace Weaver distribution package for Amazon Linux 2 (AL2) in Windows Subsystem for Linux (WSL)

This section provides instructions for setting up your SimSpace Weaver distribution zip with an AL2 environment in Windows
Subsystem for Linux (WSL). For instructions to set up AL2 in Docker, see
[Set up the SimSpace Weaver distribution package for Amazon Linux 2 (AL2) in Docker](setting-up_local_docker.md "setting-up_local_docker.md").

###### Important

This section describes a solution that uses a version of AL2 that is not owned,
developed, or supported by Amazon. This solution is provided for your convenience only,
if you choose not to use Docker. Amazon and AWS assume no liability if you choose to use
this solution.

###### Requirements

- [Hyper-V on Windows 10](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v "https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v")
- [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/install "https://docs.microsoft.com/en-us/windows/wsl/install")
- Third-party open source AL2 distribution for WSL
  ([download version 2.0.20200722.0-update.2](https://github.com/yosukes-dev/AmazonWSL/releases/tag/2.0.20200722.0-update.2 "https://github.com/yosukes-dev/AmazonWSL/releases/tag/2.0.20200722.0-update.2"))
  (see the [instructions](https://github.com/yosukes-dev/AmazonWSL "https://github.com/yosukes-dev/AmazonWSL"))

###### Important

Our WSL instructions use the
_[2.0.20200722.0-update.2](https://github.com/yosukes-dev/AmazonWSL/releases/tag/2.0.20200722.0-update.2 "https://github.com/yosukes-dev/AmazonWSL/releases/tag/2.0.20200722.0-update.2")_
version of the AL2 distribution for WSL. You might experience errors if you use any other version.

###### To set up the SimSpace Weaver distibution zip with AL2 in WSL

1. At a **Windows command prompt**, start your AL2 environment in WSL.

```
wsl -d Amazon2
```

###### Important

While you are running in WSL, include the `--al2` option when running one of the `quick-start.py` Python helper scripts located at `sdky-folder/Samples/sample-name/tools/cloud/quick-start.py`. 2. At a **Linux shell prompt**, update your yum package manager.

```
yum update -y
```

###### Important

If this step times-out, you might need to switch to WSL1 and retry these procedures.
Exit your WSL AL2 session and enter the following at your **Windows
command prompt**:

```
wsl --set-version Amazon2 1
```

3. Install the unzip tool.

```
yum install -y unzip
```

4. Remove any AWS CLI that `yum` installed. Try both of the following commands if you are unsure
   if `yum` installed an AWS CLI.

```
yum remove awscli
```

```
yum remove aws-cli
```

5. Make a temporary directory and go to it.

```
mkdir ~/temp
cd ~/temp
```

6. Download and install the AWS CLI:

```
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
./aws/install
```

7. You can remove the temporary directory.

```
cd ~
rm -rf temp
```

8. Restart the shell session to update the path in the environment.

```
exec
```

9. Configure your AWS credentials for the AWS CLI in your AL2 environment. For more information,
   see [Configuring the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md").
   If you use AWS IAM Identity Center, see [Configuring
   the AWS CLI to use AWS IAM Identity Center](../../../cli/latest/userguide/cli-configure-sso.md "../../../cli/latest/userguide/cli-configure-sso.md") in the _AWS Command Line Interface User Guide_.

```
aws configure
```

10. Install Git.

```
yum install -y git
```

11. Install `wget`.

```
yum install -y wget
```

12. Create a folder for the SimSpace Weaver app SDK.

```
mkdir `sdk-folder`
```

13. Go to your SDK folder.

```
cd `sdk-folder`
```

14. Download the SimSpace Weaver app SDK distributable package. It contains the
    following:
    - Binaries and libraries for SimSpace Weaver app development
    - Helper scripts that automate parts of the development workflow
    - Sample applications that demonstrate SimSpace Weaver concepts

```
wget https://artifacts.simspaceweaver.us-east-2.amazonaws.com/latest/SimSpaceWeaverAppSdkDistributable.zip
```

15. Unzip the file.

```
unzip *.zip
```

16. Run the WSL setup script.

```
source ./setup-wsl-distro.sh
```

17. Enter the following command to install the required Python packages:

```
pip install -r PackagingTools/python_requirements.txt
```

18. Run the SimSpace Weaver distribution zip setup script:

```
python setup.py --samples --cloudformation
```

This command does the following:

    * Creates the CloudFormation resources required to launch a simulation.





    	+ The sample CloudFormation stack template can be found in ``sdk-folder`/PackagingTools/sample-stack-template.yaml`
    * Configures the provided sample projects with the correct paths for your local system.

###### Note

You only need to do this one time for your AL2 environment in WSL.
