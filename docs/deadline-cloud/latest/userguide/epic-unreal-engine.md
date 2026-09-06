

# Epic Unreal Engine
<a name="epic-unreal-engine"></a>

Unreal Engine is a real-time 3D creation tool for photoreal visuals and immersive experiences. Unreal Engine is supported by Deadline Cloud with submitters, conda packages, and an adaptor for increased rendering performance. This guide provides step-by-step instructions for using Deadline Cloud with Unreal Engine to render your Movie Render Queue projects faster by distributing rendering tasks across multiple machines.

## Support overview
<a name="unreal-engine-support-overview"></a>

Unreal Engine is supported by the following components:
+ **Submitter**: Integrated submitter plugin for direct job submission from Unreal Engine with automatic scene and asset detection.
+ **Conda packages**: Deadline Cloud for automatic installation on service-managed fleets.
+ **Adaptor**: A program on worker hosts that keeps the application loaded between tasks for faster rendering and reports render progress.
+ **Cross-platform compatibility**: Submitter and worker support for Windows only.
+ **Movie Render Queue Integration**: Support for Unreal's Movie Render Queue system.

## Unreal Engine version compatibility
<a name="unreal-engine-version-compatibility"></a>

The following table shows current support levels for Unreal Engine versions:


| Major Version | Submitter Support | Conda Support | 
| --- | --- | --- | 
| 5.4 | Windows | Windows | 
| 5.5 | Windows | Windows | 
| 5.6 | Windows | Windows | 
| 5.7 | Windows | Windows | 
| 5.8 | Windows | Windows | 

## Deadline Cloud Conda Channel
<a name="unreal-engine-conda-channel"></a>

The following table lists all conda packages applicable to Unreal Engine available to Service-managed fleets in the `deadline-cloud` conda channel:


| OS | Package | Version | 
| --- | --- | --- | 
| Windows | unreal-engine | 5.4 | 
| Windows | unreal-engine | 5.5 | 
| Windows | unreal-engine | 5.6 | 
| Windows | unreal-engine | 5.7 | 
| Windows | unreal-engine | 5.8 | 
| Windows | unreal-engine-openjd |  | 

## Getting started
<a name="unreal-engine-getting-started"></a>

### Prerequisites
<a name="unreal-engine-prerequisites"></a>

Before installing the Unreal Engine submitter, ensure you have the following:
+ Windows workstation (Windows 10 or later)
+ Supported version of Unreal Engine installed
+ Deadline Cloud monitor installed ([download here](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/monitor-onboarding.html))
+ Access to an Deadline Cloud farm with either a GPU-enabled Windows service-managed fleet or a customer-managed fleet with Unreal Engine, the Unreal Engine adaptor, and licensing set up

## Installing the submitter
<a name="unreal-engine-installation"></a>

The Unreal Engine submitter adds Deadline Cloud functionality as a plugin to Unreal Engine, allowing you to submit your Movie Render Queue jobs directly to Deadline Cloud for rendering.

### Choosing your branch
<a name="unreal-engine-choose-branch"></a>

Select the appropriate branch for your deployment:


| Branch | Stability | Use case | Recommended for | 
| --- | --- | --- | --- | 
| release | Stable | Production | Most users | 
| mainline | Latest features | Development and testing | Advanced users | 

**Tip**  
Use the **release** branch for production environments to ensure stability.

### Creating a new Windows Amazon EC2 instance to install Unreal on (optional)
<a name="unreal-engine-create-ec2"></a>

If you're setting up on a brand new Windows Amazon Elastic Compute Cloud (Amazon EC2) instance as your submitter, a g5.2xlarge instance with 200 GB of storage is a reasonable minimum:

1. Launch an Amazon EC2 instance with a valid Instance Profile. The profile is required to download NVIDIA GRID drivers as instructed below.

1. Download the Epic Installer and install a supported version of Unreal Engine (5.4 through 5.8).
   + UE 5.5 has a known crash bug when running with the DirectX 11 plugin (see UE issue \#UE-276282). If you need DirectX support on UE 5.5, use DirectX 12 or later.

1. NVIDIA GRID drivers - Follow the [Windows installation instructions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-nvidia-driver.html#nvidia-GRID-driver).

### Windows long paths
<a name="unreal-engine-windows-long-paths"></a>

Many of the following steps might create files that exceed the default Windows maximum path length. Before you build and install the Deadline Cloud for Unreal Engine submitter or adapter on a Windows machine, we recommend that you enable Windows long path support. For more information, see [Maximum file path limitation](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry) on the Microsoft website, for example by running the [PowerShell command](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=powershell#tabpanel_1_powershell).

Long path support where you build the submitter is separate from long path support at render time. Windows honors `LongPathsEnabled` only for applications that declare `longPathAware` in their manifest, so enabling it on a worker host doesn't lift the limit for every application. If jobs fail on Windows workers with missing-file errors, see [Why does my job fail on Windows when my file paths are long?](troubleshooting.md#troubleshooting-windows-long-paths).

### Installing build tools
<a name="unreal-engine-install-build-tools"></a>

The Unreal submitter plugin currently must be compiled locally.

1. Install Visual Studio using the [Visual Studio Installer](https://visualstudio.microsoft.com/) on the Microsoft website.

1. Verify your Visual Studio and build tools version are compatible with your version of Unreal by checking the [Epic compatibility table](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine?application_version=5.5) on the Epic Games website.

1. Under **Individual Components**, ensure that the MSVC build tools version selected ("Latest" by default) matches the recommended version in the table. Even though the compatibility guidance may suggest a version "or later", build errors sometimes occur when using a newer version than the one listed as "recommended".

1. Under **Individual Components**, select a recent .NET Framework SDK (4.6.1 and 4.8.1 have been verified).

1. Under **Workloads**, select **Desktop development with C\+\+**.

### Installing Deadline Cloud monitor
<a name="unreal-engine-install-monitor"></a>

Deadline Cloud monitor is used to both manage your credentials for submitting jobs to Deadline Cloud and monitor the status of your jobs.

1. Follow the [Deadline Cloud monitor installation instructions](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/submitter.html#install-deadline-cloud-monitor).

1. Sign in.

### Environment setup
<a name="unreal-engine-environment-setup"></a>

1. (If not already installed) Install a recent version of Python for all users (verified with 3.12).

1. Make sure your environment variables are set correctly. In System Environment Variables, your PATH must include:
   + The path to your Python installation (for example, `C:\Program Files\Python312`).
   + The path to your Python Scripts folder (for example, `C:\Program Files\Python312\scripts`).
   + The path to your Unreal binaries (for example, `C:\Program Files\Epic Games\UE_5.5\Engine\Binaries\Win64`).

### Deadline Cloud software installation
<a name="unreal-engine-deadline-software-install"></a>

Clone or download `deadline-cloud-for-unreal-engine` from either the release branch or mainline, depending on whether you want the most recent tested release or all of the most recent commits.

```
git clone https://github.com/aws-deadline/deadline-cloud-for-unreal-engine.git
cd deadline-cloud-for-unreal-engine
git switch release
```

### Optional - Build and install plugin with script
<a name="unreal-engine-build-with-script"></a>

A helper script at `scripts/build_plugin.py` optionally automates the next two steps. It attempts to find the latest version of Unreal, builds your plugin and Python dependencies, and installs them in the correct locations. You can override settings such as the Unreal version. To see the full help list, run:

```
python scripts/build_plugin.py -h
```

To build and install your current copy of `deadline-cloud-for-unreal-engine` as a submitter with the latest Unreal Engine installation, run:

```
python scripts/build_plugin.py --install
```

If you've installed with this script successfully, you can skip to [Creating a fleet](#unreal-engine-create-fleet).

### Build the plugin
<a name="unreal-engine-build-plugin"></a>

Adjust the first two paths below based on where your installation of Unreal lives, and where you installed `deadline-cloud-for-unreal-engine`.

From the Unreal Install Batchfiles folder (the `package` parameter can be any new directory, however you'll want it to be called `UnrealDeadlineCloudService` later):

```
cd C:\Program Files\Epic Games\UE_5.5\Engine\Build\BatchFiles
runuat.bat BuildPlugin -plugin="C:\deadline\deadline-cloud-for-unreal-engine\src\unreal_plugin\UnrealDeadlineCloudService.uplugin" -package="C:\UnrealDeadlineCloudService"
```

Copy the "package" folder above to your Unreal installation's Plugins folder (for example, `C:\Program Files\Epic Games\UE_5.5\Engine\Plugins\UnrealDeadlineCloudService`).

### Python dependencies
<a name="unreal-engine-python-deps"></a>

There are 4 ways to install the required Python dependencies.

1. If you've built and installed the plugin from the release branch above, you can install from pip. Use the following install command, adjusting the paths to your Unreal installation:

```
"C:\Program Files\Epic Games\UE_5.5\Engine\Binaries\ThirdParty\Python3\Win64\python" -m pip install deadline-cloud-for-unreal-engine --target "C:\Program Files\Epic Games\UE_5.5\Engine\Plugins\UnrealDeadlineCloudService\Content\Python\libraries"
```

2. Alternatively in your `.uplugin` file (in the above steps this would live at `C:\Program Files\Epic Games\UE_5.5\Engine\Plugins\UnrealDeadlineCloudService\UnrealDeadlineCloudService.uplugin`) you can add a `PythonRequirements` section which matches the latest release of `deadline-cloud-for-unreal-engine` in GitHub/PyPI, for example:

```
"PythonRequirements":
[
    {
        "Platform": "All",
        "Requirements":
        [
            "deadline-cloud-for-unreal-engine>=0.5.0"
        ]
    }
]
```

You may wish to deactivate the "strict hash" feature in Unreal's Python settings, or add hash settings for specific library and dependency versions you wish to consume.

3. If you're pulling from mainline you may have Python dependencies which are not yet released to PyPI - you'll need to build and install your local copy which can be done with hatch. The `.whl` file will need to be changed to reflect the version which is output by hatch build:

```
pip install hatch
hatch build
"C:\Program Files\Epic Games\UE_5.5\Engine\Binaries\ThirdParty\Python3\Win64\python" -m pip install dist\deadline_cloud_for_unreal_engine-0.2.2.post21-py3-none-any.whl --target "C:\Program Files\Epic Games\UE_5.5\Engine\Plugins\UnrealDeadlineCloudService\Content\Python\libraries"
```

4. Lastly, Python dependencies can be installed by the submitter installer. These may be out of date with your code above from the release or mainline branch, and this method should not currently be preferred.

1. Download the submitter installer from the Deadline Cloud AWS console's Downloads tab or from within Deadline Cloud monitor under Workstation Setup → Downloads.

1. Run the installer for all users. Default install location is fine.

1. Enable the Unreal Engine plugin.

1. Make sure the Unreal Engine plugin install path matches where your plugin was copied to (in particular make sure your Unreal version matches).

### Update notifications
<a name="unreal-engine-update-notifications"></a>

The submitter plugin automatically checks for newer releases on GitHub when Unreal Editor starts. If an update is available, a dialog will prompt you to visit the release page.

To deactivate update notifications, uncheck **Show submitter update notifications** under **General Settings** in the Deadline Cloud settings panel (**Edit** > **Project Settings** > **Plugins** > **Deadline Cloud**).

Alternatively, you can use the CLI:

```
deadline config set settings.submitter_update_notification false
```

To re-enable:

```
deadline config set settings.submitter_update_notification true
```

## Creating a fleet
<a name="unreal-engine-create-fleet"></a>

If you already have a Windows fleet and don't need to set up a new fleet, you can skip down to [Submitting a test render](#unreal-engine-test-render).

### Creating a service-managed fleet (SMF)
<a name="unreal-engine-create-smf"></a>

Follow the [service-managed fleets user guide](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/smf-manage.html) to create an SMF if you don't already have one. On [service-managed fleets (SMFs)](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/smf-manage.html), the Unreal Engine and adaptor are automatically available using the `deadline-cloud` conda channel with the [default queue environment](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/create-queue-environment.html#conda-queue-environment). You are ready to start rendering. Continue with [Submitting a test render](#unreal-engine-test-render) below to submit a test render job.

### Creating a customer-managed fleet (CMF)
<a name="unreal-engine-create-cmf"></a>

1. Follow [Create a customer-managed fleet](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/create-a-cmf.html) to create a CMF if you don't already have one.
**Warning**  
When associating your CMF to queues, remove the default conda queue environment if you do not use it. This removal prevents the conda environment from being used and accidentally using the default SMF-specific variables for jobs submitted to your CMF. If you use conda in your CMF, remember to update `CondaPackages` and `CondaChannels` variables in **Parameter Definition Overrides** during job submission.

1. Follow [Worker host setup and configuration](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/worker-host.html) to set up a worker host.

1. Follow [Manage access to Windows job user secrets](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/manage-access-windows-secrets.html) to set up the Windows job user secrets for your CMF worker.

1. Follow [Install and configure software required for jobs](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/install-software.html) to install the software required to run jobs.

1. Follow [Setting up a customer-managed fleet (CMF) worker](#unreal-engine-cmf-worker-setup) to set up your worker node to run Unreal Engine jobs.

## Submitting a test render
<a name="unreal-engine-test-render"></a>

This example uses the Meerkat Demo from the Unreal Marketplace:

1. Start the Epic Games Launcher.

1. Install the Meerkat Demo from the **Samples** tab.

1. Create a project from the Meerkat Demo, then open it.

1. From the **Edit** menu, select **Plugins**, search for and enable **UnrealDeadlineCloudService**.

1. Restart Unreal if you've enabled the plugin for the first time.

1. Under **Edit** > **Project Settings**, search for the **Movie Render Pipeline** section.
   + For **Default Remote Executor**, select **MoviePipelineDeadlineCloudRemoteExecutor**.
   + For **Default Executor Job**, select **MoviePipelineDeadlineCloudExecutorJob**.
   + Under **Default Job Settings Classes**, choose the add icon, and add **DeadlineCloudRenderStepSetting**.

1. Search for **Deadline Cloud** settings and verify authentication:
   + Ensure your Status shows "AUTHENTICATED" and Deadline Cloud API shows "AUTHORIZED".
   + If it does not appear, first try using the **Login** button. If that doesn't work, open Deadline Cloud monitor and ensure you're logged in.
   + In the **Deadline Cloud Workstation Configuration** section:
     + Under **Global Settings**, ensure your AWS Profile is set correctly to your Deadline Cloud monitor profile.
     + Under **Profile**, ensure your Default Farm is set to your farm.
     + Under **Farm**, ensure your Default Queue is set to a queue that is associated with the fleet you set up above.

1. Exit the Project Settings window.

1. Choose **Windows**, **Cinematics**, **Movie Render Queue**.
   + Choose **\+ Render**, and select **Main\_SEQ**.
   + Choose **UnsavedConfig** in the settings column.
     + In the popup window, you should see Deadline Cloud settings on the left. This window can then be closed.
   + On the right side of the dialog, configure the job settings:
     + Under **Preset Overrides** (you may need to widen this dialog):
       + Expand **Job Shared Settings**:
         + Set **Name** to `Unreal Test Job`.
         + Set **Maximum retries** to 2.
       + Expand **Job Attachments**:
         + Under **Input Files**, select **Show Auto-Detected**.
         + Verify that the list of auto-detected files populates correctly.
     + Under **Job Template Overrides**:
       + Update the Unreal Engine version in **CondaPackages** if you are using a different version than 5.6.
         + Unreal Engine version autodetection is coming in a future release.
   + Choose **Render (Remote)**.

1. You can go to Deadline Cloud monitor and watch the progress of your job.

## Setting up a customer-managed fleet (CMF) worker
<a name="unreal-engine-cmf-worker-setup"></a>

This section walks you through setting up an Amazon EC2 instance as a CMF worker for Deadline Cloud with Unreal Engine.

### Overview
<a name="unreal-engine-cmf-overview"></a>

The following are key differences between CMF and SMF:
+ **CMF**: Manual installation of Unreal Engine and adaptor on worker hosts.
+ **SMF**: Automatic availability through the `deadline-cloud` conda channel.

### Choosing your branch
<a name="unreal-engine-cmf-choose-branch"></a>

Select the appropriate branch for your deployment:


| Branch | Stability | Use case | 
| --- | --- | --- | 
| release | Stable | Production deployments | 
| mainline | Latest | Development and testing | 

**Important**  
Ensure your worker version matches your submitter version to avoid compatibility issues.

### Amazon EC2 instance setup
<a name="unreal-engine-cmf-ec2-setup"></a>

The following is the recommended instance configuration:
+ **Instance Type**: g5.2xlarge or higher.
+ **Storage**: 200 GB minimum.
+ **OS**: Windows Server 2019/2022.

#### Software installation
<a name="unreal-engine-cmf-software-install"></a>

**1. Install Unreal Engine**:

1. Download the Epic Games Launcher.

1. Install Unreal Engine 5.4 or higher.
**Note**  
Unreal Engine 5.4\+ is required for Deadline Cloud compatibility.

**2. Install NVIDIA GRID drivers**:
+ Follow the [AWS NVIDIA GRID driver installation guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-nvidia-driver.html#nvidia-GRID-driver).
+ Required for GPU-accelerated rendering on Amazon EC2 instances.

### Installing build tools
<a name="unreal-engine-cmf-build-tools"></a>

The Unreal plugin currently must be compiled locally.

1. Install Visual Studio using the [Visual Studio Installer](https://visualstudio.microsoft.com/) on the Microsoft website.

1. Verify your Visual Studio and build tools version are compatible with your version of Unreal by checking the [Epic compatibility table](https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine?application_version=5.5) on the Epic Games website.

1. Under **Individual Components**, ensure that the MSVC build tools version selected ("Latest" by default) matches the recommended version in the table.

1. Under **Individual Components**, select a recent .NET Framework SDK (4.6.1 and 4.8.1 have been verified).

1. Under **Workloads**, select **Desktop development with C\+\+**.

### Deadline Cloud software installation
<a name="unreal-engine-cmf-deadline-install"></a>

Clone or download `deadline-cloud-for-unreal-engine` from either the release branch or mainline. Ensure your worker version of the libraries is compatible with the version being used from your submitters.

```
git clone https://github.com/aws-deadline/deadline-cloud-for-unreal-engine.git
cd deadline-cloud-for-unreal-engine
git switch release
```

Optional - Build and install plugin and dependencies with script:

A helper script exists at `scripts/build_plugin.py` that can automate the remaining installation steps. It attempts to find the latest version of Unreal, build your plugin and python dependencies, and install them in the correct locations. Settings such as the Unreal version to use can be overridden. To see the full help list, run:

```
python scripts/build_plugin.py -h
```

To build and install your current copy of `deadline-cloud-for-unreal-engine` as a worker with the latest Unreal Engine installation, run:

```
python scripts/build_plugin.py --install --worker
```

Configure the Deadline Cloud worker agent by running:

```
install-deadline-worker ^
  --farm-id FARM_ID ^
  --fleet-id FLEET_ID ^
  --region REGION ^
  --allow-shutdown
```

If you've installed with this script and configured the worker agent successfully, you can skip to [Starting the Deadline Cloud worker agent service](#unreal-engine-cmf-start-agent).

```
python -m pip install deadline-cloud-worker-agent
```

The correct version of the adaptor must be installed depending on the version of the submitter being used. If you are using the version of the submitter from the release branch in GitHub, you can simply install with pip:

```
python -m pip install deadline-cloud-for-unreal-engine
```

If you're using mainline or a custom in-development version of the submitter, to avoid compatibility issues we recommend that you build and install from the same version of code or transfer over the `.whl` file from your submitter build:

```
pip install hatch
hatch build
python -m pip install dist\my-built-wheel.whl
```

### Building the plugin
<a name="unreal-engine-cmf-build-plugin"></a>

Adjust the first two paths below based on where your installation of Unreal lives, and where you installed `deadline-cloud-for-unreal-engine`.

From the Unreal Install Batchfiles folder (the `package` parameter can be any new directory, however you'll want it to be called `UnrealDeadlineCloudService` later):

```
cd C:\Program Files\Epic Games\UE_5.5\Engine\Build\BatchFiles
runuat.bat BuildPlugin -plugin="C:\deadline\deadline-cloud-for-unreal-engine\src\unreal_plugin\UnrealDeadlineCloudService.uplugin" -package="C:\UnrealDeadlineCloudService"
```

Copy the "package" folder above to your Unreal installation's Plugins folder (for example, `C:\Program Files\Epic Games\UE_5.5\Engine\Plugins\UnrealDeadlineCloudService`).

### pywin32
<a name="unreal-engine-cmf-pywin32"></a>

Unreal's version of Python will need pywin32. Pip install using a copy of Unreal's third-party Python installation:

```
"C:\Program Files\Epic Games\UE_5.5\Engine\Binaries\ThirdParty\Python3\Win64\python" -m pip install pywin32
```

### Starting the Deadline Cloud worker agent service
<a name="unreal-engine-cmf-start-agent"></a>

On your CMF worker instance:

1. Open **Task Manager**.

1. Choose the **Services** tab on the right.

1. Find **DeadlineWorker**.
   + If you don't see it listed you've likely missed steps (`install-deadline-worker` in particular) from the [CMF host setup steps](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/worker-host.html#worker-agent-config).

1. If the status of the service isn't currently "Running", right-click it and select **Start**.

1. If your DeadlineWorker service isn't starting, check the worker agent launch logs in these locations:
   + `C:\ProgramData\Amazon\Deadline\Logs\worker-agent.log`
   + `C:\ProgramData\Amazon\Deadline\Logs\queue-<queueid>\session-<sessionid>.log`

## Perforce credentials management
<a name="unreal-engine-perforce-credentials"></a>

This section covers secure credential management for integrating Perforce with Deadline Cloud workers.

### Overview
<a name="unreal-engine-p4-cred-overview"></a>

There are several approaches to configure Perforce credentials for Deadline Cloud workers. Each method has different security implications and use cases:


| Method | Security level | Deployment support | Recommended use | 
| --- | --- | --- | --- | 
| AWS Secrets Manager (Secrets Manager) | High | SMF \+ CMF | Production (recommended) | 
| Job environment variables | Low | SMF \+ CMF | Development and testing only | 
| Queue environment variables | Low | SMF \+ CMF | Development and testing only | 
| Windows registry | Medium | CMF only | Legacy CMF setups | 
| Pre-configured admin user | Medium | CMF only | Simplified CMF setups | 

**Important**  
Use Secrets Manager for production environments. It provides centralized, encrypted credential storage with audit trails and works with both SMF and CMF deployments.

### P4 credentials basics
<a name="unreal-engine-p4-cred-basics"></a>

To retrieve connection settings, including Perforce server URL and port, username, and password, Perforce follows the following priority:

1. Connection parameters in any framework for Perforce (P4) (`p4python.P4` for example).

1. User/system environment variables: `P4PORT`, `P4USER`, `P4CLIENT`, `P4PASSWD`.

1. Windows registry: `HKEY_LOCAL_MACHINE\SOFTWARE\Perforce\Environment` (system-wide settings) or `HKEY_CURRENT_USER\SOFTWARE\Perforce\Environment` (user-specific settings).

With these priorities, if you have the following setup:
+ Connection parameter `password` is `password.from.connection`
+ Environment variable `%P4PORT%` is `ssl:perforce.from.env:1666`
+ Windows registry `HKEY_CURRENT_USER\SOFTWARE\Perforce\Environment:P4PORT` is `ssl:perforce.from.registry:1666`
+ Windows registry `HKEY_CURRENT_USER\SOFTWARE\Perforce\Environment:P4USER` is `user.from.registry`
+ Windows registry `HKEY_CURRENT_USER\SOFTWARE\Perforce\Environment:P4PASSWD` is `password.from.registry`

The resulting Perforce connection will be:

```
Port = ssl:perforce.from.env:1666
User = user.from.registry
Password = password.from.connection
```

### Secrets Manager (recommended)
<a name="unreal-engine-p4-cred-secrets-manager"></a>

Secrets Manager provides the most secure and scalable solution for both CMF and SMF deployments.

This approach provides the following benefits:
+ **Centralized security**: Store all P4 credentials in one encrypted location.
+ **No credential exposure**: Credentials never appear in job configurations or logs.
+ **Automatic rotation**: Support credential rotation without job reconfiguration.
+ **Audit trails**: Track credential access and usage.
+ **Universal support**: Works with both CMF and SMF deployments.
+ **Log redaction**: Connection credentials automatically redacted in job logs.

#### Step 1: Create a secret in Secrets Manager
<a name="unreal-engine-p4-create-secret"></a>

Create a secret containing your Perforce connection parameters.

**Required key-value pairs**:
+ `P4PORT` - Perforce server URL and port.
+ `P4USER` - Perforce username.
+ `P4PASSWD` - Perforce password.

**Important**  
Key names must exactly match P4 connection parameters to work with `deadline-cloud-for-unreal-engine`.

**Example secret**:

```
{
   "P4PORT": "ssl:your-perforce-server.com:1666",
   "P4USER": "your-perforce-username",
   "P4PASSWD": "your-perforce-password"
}
```

**To create the secret**:

1. Open the Secrets Manager console.

1. Choose "Store a new secret".

1. Select "Other type of secret".

1. Enter the key-value pairs above.

1. Name your secret (for example, `deadline-cloud-p4-credentials`).

1. Complete the creation process.

#### Step 2: Grant worker access to the secret
<a name="unreal-engine-p4-grant-access"></a>

Workers need `secretsmanager:GetSecretValue` permission to access the secret. This follows the same pattern as [managing Windows job user secrets](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/manage-access-windows-secrets.html#grant-access).

**To grant access**:

1. Open the Secrets Manager console and navigate to your secret.

1. In the "Resource permissions" section, add this policy:

   ```
   {
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "AWS": "QUEUE_ROLE_ARN"
         },
         "Action": [
           "secretsmanager:GetSecretValue"
         ],
         "Resource": "*"
       }
     ]
   }
   ```

1. Replace `QUEUE_ROLE_ARN` with your actual queue role ARN.

1. Save the policy.

**Note**  
Save the secret name - you'll need it when configuring P4 render jobs. See [Creating a Perforce render job](#unreal-engine-perforce-render-job) for next steps.

### Job environment variables
<a name="unreal-engine-p4-job-env"></a>

**Warning**  
This approach is not recommended for production as it exposes credentials in job configurations and logs. Use Secrets Manager for production environments.

You can pass connection credentials within the job environment where workspace creation happens. Examples on the GitHub website include [p4\_sync\_smf\_environment](https://github.com/aws-deadline/deadline-cloud-for-unreal-engine/blob/mainline/src/unreal_plugin/Content/Python/openjd_templates/p4/p4_sync_smf_environment.yml) and [ugs\_sync\_smf\_environment](https://github.com/aws-deadline/deadline-cloud-for-unreal-engine/blob/mainline/src/unreal_plugin/Content/Python/openjd_templates/ugs/ugs_sync_smf_environment.yml), or similar environments for CMF. Alternatively, create a new environment template and prepend it to your job.

```
name: P4Credentials
variables:
  P4PORT: ssl:my-perforce.com:1666
  P4USER: j.doe
  P4PASSWD: MyVeRyS3cretP4ssW0rd
```

This approach has the following security risks:
+ Credentials are visible in job configurations.
+ Passwords may appear in logs (not automatically redacted).
+ No centralized credential management.
+ Difficult to rotate credentials.

### Queue environment variables
<a name="unreal-engine-p4-queue-env"></a>

**Warning**  
This approach is not recommended for production as it stores credentials in queue configurations. Use Secrets Manager for secure credential management.

Per the [Deadline Cloud user guide](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/create-queue-environment.html), you can use queue environments to provide software applications, environment variables, and other resources to jobs in the queue. For queue environment samples, see the [queue\_environments folder in deadline-cloud-samples](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/queue_environments) on the GitHub website.

#### Add queue environment using Deadline Cloud monitor or console
<a name="unreal-engine-p4-add-env-dcm"></a>

1. Open Deadline Cloud monitor or the AWS console.

1. Navigate to the farm and queue you are working with.

1. Select **Queue environments** tab.

1. Choose **Action** and select **Create new with YAML**.

1. Add the following and save:

   ```
   specificationVersion: environment-2023-09
   environment:
      name: P4Credentials
      variables:
         P4PORT: ssl:my-perforce.com:1666
         P4USER: j.doe
         P4PASSWD: MyVeRyS3cretP4ssW0rd
   ```

#### Add queue environment using CLI
<a name="unreal-engine-p4-add-env-cli"></a>

1. Create a `p4_credentials.yaml` file with the sample above.

1. Run the following CLI command:

   ```
   aws deadline create-queue-environment \
    --farm-id FARM_ID \
    --queue-id QUEUE_ID \
    --priority 1 \
    --template-type YAML \
    --template file://p4_credentials.yaml
   ```

### Windows registry (CMF only)
<a name="unreal-engine-p4-windows-registry"></a>

**Important**  
This solution is only suitable for CMF where you can configure worker hosts directly. For SMF deployments, use Secrets Manager.

Windows registry provides local credential storage on worker machines. This method uses the standard Perforce priority system where credentials are stored in:
+ `HKEY_LOCAL_MACHINE\SOFTWARE\Perforce\Environment` (system-wide settings).
+ `HKEY_CURRENT_USER\SOFTWARE\Perforce\Environment` (user-specific settings).

This approach is only suitable for CMF deployments where you have direct access to configure worker machines.

### Pre-configured admin user (CMF only)
<a name="unreal-engine-p4-admin-user"></a>

**Important**  
This solution is only suitable for CMF where you can configure worker hosts directly. For SMF deployments, use Secrets Manager.

Create a dedicated P4 user for render nodes with a non-expiring connection to eliminate the need to pass secret data such as usernames and passwords. In this case, a single dedicated P4 user can be used to connect to all P4 servers, including the Commit (Master) and Edge servers where the project depot is accessible.

Therefore, you only need to pass the port to connect to, if the default is not configured on workers. You can pass the port by adding the following in job environment or queue environment similar to the steps documented above:

```
name: P4Sync
variables:
  P4PORT: ssl:my-perforce.com:1666
```

## Creating a Perforce render job
<a name="unreal-engine-perforce-render-job"></a>

This section walks you through configuring Perforce-integrated render job data assets so you can submit Perforce-integrated render jobs to Deadline Cloud from Unreal Engine.

### Prerequisites
<a name="unreal-engine-p4-prerequisites"></a>

Before submitting a Movie Render Queue (MRQ) job from Unreal Engine in a Perforce repository:

**Unreal project setup**:
+ Project must be within the Perforce workspace.
+ Verify Perforce connection is established and you're logged in.

**Deadline Cloud setup**:
+ Complete [Installing the submitter](#unreal-engine-installation).
+ Configure [Perforce credentials management](#unreal-engine-perforce-credentials) for workers.

**Perforce requirements**:
+ Valid Perforce workspace with project files.
+ Appropriate Perforce permissions for sync operations.

### Perforce render job architecture
<a name="unreal-engine-p4-architecture"></a>

P4 render jobs extend the standard render job with Perforce synchronization capabilities:

```
Deadline Cloud Perforce render job
├── Environments
│   ├── Apply Perforce Credentials from Secrets Manager
│   ├── Sync Perforce Environment (CMF/SMF)
│   │   └── Initializes Perforce workspace and syncs repository on workers
│   └── Launch UE Environment
│       └── Starts Unreal Engine with Perforce workspace paths
└── Steps
    └── Render Step
        └── Executes Movie Render Queue process
```

**Key differences from standard jobs**:
+ **Credential management**: Secure Perforce credential application from Secrets Manager.
+ **Repository sync**: Additional Perforce sync environment for workspace management.
+ **Path resolution**: Environment variables reference Perforce workspace paths.
+ **Dependency collection**: Automatic collection and sync of Perforce-tracked assets.

### How Perforce sync scales for production projects
<a name="unreal-engine-p4-sync-at-scale"></a>

Production Unreal Engine projects can reach hundreds of gigabytes across tens of thousands of files. The Perforce integration keeps sync time proportional to what changed rather than to the size of the project:

Jobs are pinned to a changelist  
At submission, the submitter sets the `PerforceChangelistNumber` job parameter to the changelist your workspace has synced. Every task in the job renders against that same revision, so your job stays reproducible even when artists submit new changes while it runs. Workers can start a task only after the pinned changelist is available on the Perforce server they sync from.

Workers reuse a stable client workspace  
Each worker creates its Perforce client workspace under a persistent root directory. It records the pairing in a `workspace_info.json` registry file stored with the workspace. A replacement worker that receives the same storage reads the registry and reuses the existing client. It doesn't create a new workspace. Because Perforce tracks the have-list on the server under the client name, a normal sync then downloads only the file revisions that changed since the last job.

To benefit from client workspace reuse on a service-managed fleet, enable [persistent storage](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/volumes.html) so the volume holding the synced workspace is reattached to future workers.

If the network path between your fleet's Region and your Perforce server has low throughput or high latency, a Perforce edge server in the fleet's Region can act as a regional cache for depot data. For more information, see [Perforce source control](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/architecture-guidance.html#perforce-asset-access) in the *Deadline Cloud Developer Guide*.

### Setting up Perforce render job components
<a name="unreal-engine-p4-setup-components"></a>

Follow these steps to create the required data assets for Perforce-integrated render jobs.

#### 1. Create Apply Perforce Credentials data asset
<a name="unreal-engine-p4-apply-credentials"></a>

Set up an OpenJD environment for retrieving Perforce credentials from Secrets Manager and applying them to the Perforce connection.

**Note**  
Environment variables appear in logs with the `openjd_env` prefix, but sensitive data (port, user, password) is automatically redacted for security.

**Configuration steps**:

1. Create a new **Deadline Cloud Perforce Environment** data asset.  
![Pick Class For Data Asset Instance dialog filtered to "deadline", with Deadline Cloud Perforce Environment selected.](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/unreal-engine-p4-environment.png)

1. Name the data asset descriptively (for example, "ApplyP4SecretEnv").

1. Select the `p4_apply_secrets_environment.yml` template from `Content/Python/openjd_templates/p4/`.

1. Configure the secret reference:
   + Enter your Perforce credential secret name in **AWS\_SECRET\_P4INFO**.
   + The value should match the secret name created in [Perforce credentials management](#unreal-engine-perforce-credentials).  
![Apply Perforce credentials environment data asset properties: Name P4ApplySecrets, Path to Template p4_apply_secrets_environment.yml, and AWS_SECRET_P4INFO variable set to P4AccessSecretName.](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/unreal-engine-p4-apply-secrets-environment.png)

#### 2. Create Perforce sync environment data asset
<a name="unreal-engine-p4-sync-env"></a>

Set up an OpenJD environment for creating a Perforce workspace, syncing files from the Perforce server, and cleaning up the workspace after rendering.

**Configuration steps**:

1. Create a new **Deadline Cloud Perforce Environment** data asset.

1. Name the data asset based on your fleet type:
   + **P4SyncSMFEnv** for service-managed fleet (SMF).
   + **P4SyncCMFEnv** for customer-managed fleet (CMF).

1. Select the appropriate template from `Content/Python/openjd_templates/p4/`:
   + **SMF**: `p4_sync_smf_environment.yml`.
   + **CMF**: `p4_sync_cmf_environment.yml`.

1. Configure the secret reference:
   + Enter your Perforce credential secret name in **AWS\_SECRET\_P4INFO**.
   + Must match the secret from step 1.  
![Perforce sync environment data asset properties: Name P4SyncSmf, Path to Template p4_sync_smf_environment.yml, and AWS_SECRET_P4INFO variable set to P4AccessSecretName.](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/unreal-engine-p4-sync-smf-environment.png)

#### 3. Create Perforce Launch UE environment data asset
<a name="unreal-engine-p4-launch-env"></a>

Set up an OpenJD environment for launching Unreal Engine with Perforce integration. This automatically references the Perforce workspace created by the sync environment.

**Configuration steps**:

1. Create a new **Deadline Cloud Environment** data asset.

1. Name the data asset descriptively (for example, "P4LaunchUEEnv").

1. Select the `p4_launch_ue_environment.yml` template from `Content/Python/openjd_templates/p4/`.

1. Configure environment settings:
   + Set **REMOTE\_EXECUTION** to `True`.
   + This setting enables remote rendering capabilities.  
![Launch Unreal Engine with Perforce environment data asset properties: Name LaunchUnrealEditorWithP4, Path to Template p4_launch_ue_environment.yml, and REMOTE_EXECUTION variable set to True.](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/unreal-engine-p4-launch-UE-environment.png)

#### 4. Create Perforce render step data asset
<a name="unreal-engine-p4-render-step"></a>

Set up an OpenJD render step for executing the rendering process.

**Configuration steps**:

1. Create a new **Deadline Cloud Render Step** data asset.  
![Pick Class For Data Asset Instance dialog filtered to "deadline cloud", with Deadline Cloud Render Step selected.](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/unreal-engine-p4-render-step-data-asset.png)

1. Name the data asset descriptively (for example, "P4RenderStep").

1. Select the `p4_render_step.yml` template from `Content/Python/openjd_templates/p4/`.

#### 5. Create Perforce render job data asset
<a name="unreal-engine-p4-render-job"></a>

Set up an OpenJD render job that orchestrates the entire rendering workflow.

**Configuration steps**:

1. Create a new **Deadline Cloud Render Job** data asset.  
![Pick Class For Data Asset Instance dialog filtered to "deadline cloud", with Deadline Cloud Render Job selected.](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/unreal-engine-p4-render-job-data-asset.png)

1. Name the data asset descriptively (for example, "P4RenderJob").

1. Select the `p4_render_job.yml` template from `Content/Python/openjd_templates/p4/`.

1. **Review parameter definitions**: The template includes these parameters with their default behaviors:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/epic-unreal-engine.html)

   **Parameter configuration guidelines**:
   + **Auto-populated parameters**: Leave these empty - they're filled automatically during job submission.
   + **Manual parameters**: Review defaults and adjust based on your specific requirements.
   + **ShotsPerTask**: Start with 1, increase for better performance with simple shots.  
![Parameter Definition properties for the Perforce render job data asset, listing ProjectRelativePath, ProjectName, PerforceChangelistNumber, PerforceWorkspaceSpecificationTemplate, MrqJobDependenciesDescriptor, ExtraCmdArgs, ExtraCmdArgsFile, Executable, CondaPackages, CondaChannels, and ChunkSize fields.](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/unreal-engine-p4-job-parameter-definition.png)

1. **Configure environments** (in this exact order):    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/epic-unreal-engine.html)
**Important**  
Environment order is essential for proper dependency resolution and credential flow.

1. **Add render step**: Add "P4RenderStep" to the Steps section.  
![Render job data asset Environments array showing ApplyP4SecretsEnv, P4SyncSMFEnv, and P4LaunchUEEnv in order, with P4RenderStep added under Steps.](http://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/unreal-engine-p4-add-environments-and-steps.png)

### Submitting render outputs back to Perforce
<a name="unreal-engine-p4-submit-mode"></a>

By default, a Perforce render job uploads outputs through job attachments only. The `SubmitMode` job parameter opts in to pushing rendered outputs into Perforce instead, so finished frames land in your depot alongside the project.


| `SubmitMode` value | Behavior | 
| --- | --- | 
| '' (default) | Job attachments only. No Perforce write occurs. Existing jobs behave unchanged. | 
| submit | Each render task shelves the files it produced. When every task has finished, an AssembleShelves step combines all task shelves into a single aggregate changelist and submits it. The job log records the final changelist number. | 
| shelve | Same aggregation as submit, but the final aggregate changelist is shelved instead of submitted, so a person can review the aggregate before committing it. | 

Only files that changed since the last sync end up in the changelist. Each task reconciles the exact files it produced, and the integration reverts files whose content is identical to the depot revision, so re-rendering an unchanged frame produces no changelist entry.

**Note**  
When `SubmitMode` is `submit` or `shelve`, the job doesn't upload render outputs to Amazon S3 through job attachments. Perforce becomes the sole delivery path for the frames. The download outputs feature in Deadline Cloud monitor doesn't find the frames, and downstream jobs that consume outputs through job attachments don't see them. Input attachments are still uploaded through job attachments as normal.

Configure your workers to authenticate to Perforce as the same Perforce user for all tasks in a job, because the aggregation step finds task shelves by owner. The recommended credential setup in [Perforce credentials management](#unreal-engine-perforce-credentials), a single shared secret in Secrets Manager, already satisfies that requirement.

### Best practices
<a name="unreal-engine-p4-best-practices"></a>

#### Pre-submission checklist
<a name="unreal-engine-p4-checklist"></a>
+ **Credentials**: Perforce credentials properly configured (see [Perforce credentials management](#unreal-engine-perforce-credentials)).
+ **Workspace**: Specification includes all necessary view mappings.
+ **Testing**: Test with a small render task before large job submissions.
+ **Dependencies**: Verify all project dependencies are in Perforce and accessible.
+ **Permissions**: Confirm worker roles have access to Secrets Manager.

#### Performance optimization
<a name="unreal-engine-p4-perf-optimization"></a>

The following table shows how the `ShotsPerTask` setting affects performance:


| Shots per task | Use case | Performance impact | 
| --- | --- | --- | 
| 1-2 shots | Complex shots, detailed review needed | Lower throughput, higher quality control | 
| 4-8 shots | Balanced workload, typical projects | Optimal balance of speed and manageability | 
| 10\+ shots | Simple shots, batch processing | Maximum throughput, minimal overhead | 

Consider the following additional optimizations:
+ **Dependencies**: Minimize unnecessary asset dependencies to reduce sync time.
+ **Workspace views**: Optimize Perforce workspace views to sync only required files.

#### Monitoring and debugging
<a name="unreal-engine-p4-monitoring"></a>
+ **Job logs**: Monitor Perforce sync process in job execution logs.
+ **Workspace status**: Check workspace creation and sync completion.
+ **Dependency collection**: Verify all required assets were captured.
+ **Performance metrics**: Track sync times and render performance.

### Troubleshooting
<a name="unreal-engine-p4-troubleshooting"></a>

#### Common issues and solutions
<a name="unreal-engine-p4-common-issues"></a>


| Issue | Symptoms | Solution | 
| --- | --- | --- | 
| P4 connection failures | Authentication errors, timeout | Verify Perforce credentials; check network connectivity; validate Perforce server accessibility | 
| Workspace sync errors | Sync failures, permission denied | Check Perforce user permissions; verify workspace specification; ensure changelist exists | 
| Missing dependencies | Render failures, missing assets | Review MrqJobDependenciesDescriptor; check soft references collection; verify all assets in Perforce | 
| Path resolution issues | File not found errors | Verify P4\_CLIENT\_DIRECTORY variable; check environment order; validate workspace root paths | 

#### Debug steps
<a name="unreal-engine-p4-debug-steps"></a>

1. **Check job logs**: Review Perforce sync environment logs for detailed error messages.

1. **Validate workspace**: Ensure Perforce workspace specification is correct.

1. **Test locally**: Verify Perforce operations work from submitter machine.

1. **Verify permissions**: Confirm worker roles have secret access (if using Secrets Manager).

## Custom host requirements
<a name="unreal-engine-host-requirements"></a>

This section describes how to create and use custom host requirements for Deadline Cloud rendering in Unreal Engine.

### Overview
<a name="unreal-engine-host-overview"></a>

Host requirements define which fleet are eligible to run a particular render step. They are stored inside a `UDeadlineCloudHostRequirements` asset, which is then referenced by a `DeadlineCloudRenderStep` asset.


| Requirement type | Configuration location | Use case | 
| --- | --- | --- | 
| Base system requirements | CPU / RAM / GPU fields | Restrict rendering to machines with specific hardware | 
| Custom amount requirements | Name \+ min/max values | Require numeric resource levels (licenses, tokens, quotas) | 
| Custom attribute requirements | Attribute \+ value list | Required custom attributes on fleets to run the step | 

**Note**  
Hiding a requirement using the eye icon only hides it in the MRQ Submit UI. The requirement still applies when submitting the job.

**Important**  
The `Name` and `Attribute` values used for custom amount requirements and custom attribute requirements must strictly match the valid identifiers defined in the official Open Job Description documentation. For more information, see [Open Job Specifications](https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas#33-hostrequirements) on the GitHub website.

### Step 1: Create the host requirements asset
<a name="unreal-engine-host-step1"></a>

1. Open Content Browser in Unreal Engine.

1. Create a new asset: **Add** → **Miscellaneous** → **Data Asset** → **DeadlineCloudHostRequirements**.

1. Name the asset, for example, `MyHostRequirements`.

### Step 2: Load the default YAML template
<a name="unreal-engine-host-step2"></a>

1. In the asset details panel, locate the field **Path to Template**.

1. Select the default template: `Plugins/UnrealDeadlineCloudService/Content/Python/openjd_templates/host_requirements.yml`.

This loads base requirements such as CPU, Memory, GPU, OS, and architecture.

**Note**  
Base requirements cannot be removed; only their values may be changed.

### Step 3: Configure base (system) requirements
<a name="unreal-engine-host-step3"></a>


| Setting | Example | 
| --- | --- | 
| Operating System | windows | 
| CPU Architecture | x86\_64 | 
| vCPUs (Min) | 16 | 
| GPUs (Min) | 1 | 

If Max = 0, then there is no upper limit for that requirement.

### Step 4: Add custom amount requirements
<a name="unreal-engine-host-step4"></a>

Used when the requirement is numeric (for example, number of licenses, concurrency limits).

1. Find the section **Custom Amount Requirements**.

1. Add a new entry and set a name, for example: `amount.custom.license`.

1. Set Min and Max values:
   + Min: 1.
   + Max: 0 (0 means unlimited).

### Step 5: Add custom attribute requirements
<a name="unreal-engine-host-step5"></a>

Used to filter workers based on tags and labels.

1. Find the section **Custom Attributes Requirements**.

1. Add a new attribute name, for example: `attr.custom.gpu.vendor`.

1. Choose the matching rule:
   + **AllOf** - all values must match.
   + **AnyOf** - at least one must match.

1. Enter attribute values separated by spaces, for example: `nvidia amd`.

### Step 6: Visibility in MRQ (optional)
<a name="unreal-engine-host-step6"></a>

Each requirement entry has an eye icon.


| Eye | Behavior | 
| --- | --- | 
| Visible | The requirement is shown in MRQ Submit UI | 
| Hidden | The requirement is hidden but still included when submitting the job | 

This setting is useful for simplifying UI for artists while preserving technical constraints.

### Step 7: Attach the requirements to a render step
<a name="unreal-engine-host-step7"></a>

1. Open the relevant `DeadlineCloudRenderStep` asset.

1. Find the **Host Requirements** field.

1. Assign your created asset (for example, `MyHostRequirements`).

All MRQ submissions using this step now enforce your host selection logic.

### Summary
<a name="unreal-engine-host-summary"></a>

Using the host requirements asset, you can:
+ Control which worker machines execute your render jobs.
+ Specify minimum resource levels.
+ Target specific worker pools using attribute matching.
+ Simplify UI while keeping technical rules intact.
+ Reuse settings across multiple MRQ steps.

This setup improves job routing consistency and ensures rendering happens on the correct hardware.

## Advanced configurations
<a name="unreal-engine-advanced-configurations"></a>

### Service-managed fleets vs customer-managed fleets
<a name="unreal-engine-fleet-types"></a>

#### Service-managed fleets (SMF)
<a name="unreal-engine-smf"></a>

On service-managed fleets, the Unreal Engine and adaptor are automatically available using the `deadline-cloud` conda channel with the default queue environment. This setup provides the easiest experience.

#### Customer-managed fleets (CMF)
<a name="unreal-engine-cmf"></a>

For customer-managed fleets, Unreal Engine and the adaptor must be manually installed on worker hosts. This setup provides more control and supports additional features like Perforce integration. For detailed instructions, see [Setting up a customer-managed fleet (CMF) worker](#unreal-engine-cmf-worker-setup).

## Unreal Engine rendering features
<a name="unreal-engine-rendering-features"></a>

Unreal Engine's rendering system provides comprehensive support for:


| Feature | Description | Notes | 
| --- | --- | --- | 
| Movie Render Queue | High-quality offline rendering | Integration with job submission | 
| Sequencer | Timeline-based animation system | Automatic shot detection and processing | 
| Project Plugins | Custom plugin support | Automatic detection and inclusion | 
| Asset Dependencies | Content file management | Comprehensive asset tracking | 
| Sticky Rendering | Application persistence between shots | Improved performance for multi-shot sequences | 

All rendering features are automatically detected and configured by the Unreal Engine integrated submitter. The adaptor maintains proper dependency handling and supports efficient multi-shot rendering without restarting Unreal Engine.

## Open source resources
<a name="unreal-engine-open-source"></a>

The submitter and adaptor are open source. For more information, see [Deadline Cloud for Unreal Engine](https://github.com/aws-deadline/deadline-cloud-for-unreal-engine) on the GitHub website.