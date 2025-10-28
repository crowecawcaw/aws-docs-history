# Troubleshoot compatibility on Proton

In this step, you will set up Proton on your own machine, so you can troubleshoot compatibility issues between your Amazon GameLift Streams application and Proton. Running your application in a simulated environment without the Amazon GameLift Streams server can help you identify issues specific to your application and runtime environment.

## Prerequisites

- Ubuntu 22.04 LTS with GPU drivers installed. For instructions, refer to [Set up a local machine](troubleshoot-compatibility-setup-local.md "troubleshoot-compatibility-setup-local.md") or [Set up a remote machine](troubleshoot-compatibility-setup-remote.md "troubleshoot-compatibility-setup-remote.md").

## Install Proton

To install Proton on your Ubuntu 22.04 LTS machine, use the following script to clone, build, and configure the version of Proton
you want to test from the [Proton GitHub repository](https://github.com/ValveSoftware/Proton/ "https://github.com/ValveSoftware/Proton/").

1. Copy and paste the following code into a file called `proton-setup.sh` on your Ubuntu 22.04 LTS machine.

```
#!/bin/bash
# This is a script to build Proton. The default build is a tag from the
# experimental_9.0 branch of Proton, but can be changed as a parameter to this script.
#
# Usage: ./proton-setup.sh [optional proton_branch_name {default: experimental-9.0-20241121b}]
set -e

sudo apt install -y podman make git

# clone proton from github, recurse submodules
# if no proton git link is supplied, use a default tag from the experimental_8.0 branch
PROTON_BRANCH=${1:-"experimental-9.0-20241121b"}
PROTON_BUILD_DIR=protonBuild
PROTON_DIR=$(pwd)/proton
if git clone https://github.com/ValveSoftware/Proton.git --recurse-submodules --branch $PROTON_BRANCH proton;
then
	echo "Successfully cloned Proton and its submodules."
else
	echo "Warning: a proton directory/repository already exists. It is recommended to delete this folder and re-run this script unless it is a valid repository with initialized submodules."
fi

if [ -d $PROTON_BUILD_DIR ];
then
	echo "Error: protonBuild directory already exists. Delete this folder first to create a fresh build of Proton before re-running this script."
	exit 1
fi
mkdir $PROTON_BUILD_DIR
cd $PROTON_BUILD_DIR
$PROTON_DIR/configure.sh --enable-ccache --container-engine=podman

# build proton
echo "Building Proton"
make
echo "Done building Proton!"

# prepare proton for execution
cd dist
mkdir compatdata
if [ -e ./dist ]; then
  PROTON_FILES=dist
elif [ -e ./files ]; then
  PROTON_FILES=files
fi
cp version $PROTON_FILES/
echo "Finished installing proton. Proton binary location: $(pwd)/proton"
echo "STEAM_COMPAT_DATA_PATH: $(pwd)/compatdata"
echo "STEAM_COMPAT_CLIENT_INSTALL_PATH: anything"
```

2. In this step you will run the Proton setup script to clone and install Proton and additional dependencies. The script accepts as
   an argument the tag or branch name for the Proton version you want to install. To simulate one of the custom builds of Proton that
   Amazon GameLift Streams provides, use the instructions for that version, below.

###### Note

Expect the cloning from GitHub to take some time. There are many submodules to download, totalling several gigabytes.

In your terminal, run the `proton-setup.sh` script and specify the Proton version branch:

    * **Built-in Proton versions**





    	+ For Proton 9.0-2 (`PROTON-20250516`), use [experimental-9.0-20241121b](https://github.com/ValveSoftware/Proton/tree/experimental-9.0-20241121b "https://github.com/ValveSoftware/Proton/tree/experimental-9.0-20241121b").



    	```
    	proton-setup.sh experimental-9.0-20241121b
    	```
    	+ For Proton 8.0-5 (`PROTON-20241007`), use [experimental-8.0-20240205](https://github.com/ValveSoftware/Proton/tree/experimental-8.0-20240205 "https://github.com/ValveSoftware/Proton/tree/experimental-8.0-20240205").



    	```
    	proton-setup.sh experimental-8.0-20240205
    	```

    	Typically, no additional source code is needed. However, if you run into problems with Electra Media Player, (an
    	 Unreal Engine plugin) we recommend using the fixes found in [https://github.com/ValveSoftware/wine/pull/257](https://github.com/ValveSoftware/wine/pull/257 "https://github.com/ValveSoftware/wine/pull/257").
    ###### Note

     For Proton 8.0-2c (`PROTON-20230704`), Amazon GameLift Streams uses a proprietary build, which is not
     available to buld locally.
    * **Recommended custom Proton version**



     For a custom Proton version, we recommend using the Proton experimental\_8.0 branch.



    ```
    proton-setup.sh experimental_8.0
    ```
    * **Other custom Proton versions**



     For other Proton versions, use an exact branch or tag name listed in [Proton releases](https://github.com/ValveSoftware/Proton/releases "https://github.com/ValveSoftware/Proton/releases").



    ```
    proton-setup.sh `branch-or-tag-name`
    ```

If your installation is successful, the output in your terminal should be similar to the following:

```
...
Done building Proton!
Finished preparing proton. Proton binary location: /home/test/protonBuild/dist/proton
STEAM_COMPAT_DATA_PATH: /home/test/protonBuild/dist/compatdata
STEAM_COMPAT_CLIENT_INSTALL_PATH: anything
```

Take note of the following variables from the output because you will need them to run Proton in the next step:

    * Proton binary location
    * `STEAM_COMPAT_DATA_PATH`
    * `STEAM_COMPAT_CLIENT_INSTALL_PATH`

## Run your application on Proton

The following steps assume that the application executable is located in `path/myapplication/bin/application.exe`. Replace it with the path and file name for your application.

- In a terminal, navigate to the folder where your application executable is located.

```
cd `path/myapplication/bin/application.exe`
```

- Run your application on Proton. Use the Proton binary location and the environment variables that you got in the previous step.

```
STEAM_COMPAT_DATA_PATH=/home/test/protonBuild/dist/compatdata STEAM_COMPAT_CLIENT_INSTALL_PATH=anything /home/test/protonBuild/dist/proton run application.exe
```

The application should now attempt to start. If the application
starts locally, but not on Amazon GameLift Streams, it may be due to a
configuration issue when calling Amazon GameLift Streams APIs. Verify that the API
call parameters are correct. Otherwise, continue to the next step
for debugging.

## Debug the application through log files

If your application has issues running on the local Proton environment, check the output log.
The log contains output from your application and runtime environment.
Trace where your application is failing to discover issues on the application side.

To dump the log output into a text file, such as `proton.log`, use the following command:

```
STEAM_COMPAT_DATA_PATH=/home/test/protonBuild/dist/compatdata STEAM_COMPAT_CLIENT_INSTALL_PATH=anything /home/test/protonBuild/dist/proton run application.exe &>proton.log
```

Proton also indicates if the issue is due to a Wine plugin, unimplemented function, missing dlls, and so on.
For more information, see [Wine HQ's Debugging Wine](https://wiki.winehq.org/Wine_Developers_Guide/Debugging_Wine "https://wiki.winehq.org/Wine_Developers_Guide/Debugging_Wine") guide.
If you find a Proton or Wine error in the logs that you can't fix on the application side, reach out to your AWS Account Manager or
post a question in [AWS re:Post](https://repost.aws/tags/TAOU7EpUOuTQSSWmIHCfb2fQ/amazon-gamelift-streams "https://repost.aws/tags/TAOU7EpUOuTQSSWmIHCfb2fQ/amazon-gamelift-streams") for help with further debugging.
