

# Getting Started
<a name="custom-get-started"></a>

This section describes how to set up AWS Transform custom and run your first transformation.

## Prerequisites
<a name="custom-prerequisites"></a>

Before installing AWS Transform custom, ensure you have the following:

### Supported Platforms
<a name="custom-supported-platforms"></a>

AWS Transform custom supports the following operating systems:
+ **Linux** - Full support for all Linux distributions
+ **macOS** - Full support for macOS systems
+ **Windows** - Full support for native Windows using Windows Terminal and PowerShell (The `atx ct` commands are not yet supported on Windows)
+ **Windows Subsystem for Linux (WSL)** - Supported when running under WSL

### Required Software
<a name="custom-required-software"></a>
+ **Node.js 22 or later** - Download from https://nodejs.org/en/download
+ **Git** - Must be installed and the working directory needs to be a valid Git repo to execute a transformation. Run `git init; git add .; git commit -m "Initial commit"` to initialize a Git repo in your working directory.

### Network Requirements
<a name="custom-network-requirements"></a>

An internet connection with access to the following endpoints is required:
+ `transform-cli.awsstatic.com`
+ `transform-custom.<region>.api.aws`
+ `*.s3.amazonaws.com`

If you are working in an internet-restricted environment, update firewall rules to allowlist these URLs.

## Installing the AWS Transform CLI
<a name="custom-installation"></a>

The recommended installation method is using the installation script. Choose the tab for your operating system.

**To install the AWS Transform CLI**

1. Run the installation script:

------
#### [ Linux and macOS ]

   ```
   curl -fsSL https://transform-cli.awsstatic.com/install.sh | bash
   ```

------
#### [ Windows (PowerShell) ]

   On native Windows, run the installation script from Windows Terminal using PowerShell.

   ```
   irm https://transform-cli.awsstatic.com/install.ps1 | iex
   ```

------

1. Verify the installation:

   ```
   atx --version
   ```

   The command should display the installed version of the AWS Transform CLI.

## Configuring Authentication
<a name="custom-authentication"></a>

AWS Transform custom requires AWS credentials to authenticate with the service. Configure authentication using one of the following methods.

### Environment Variables
<a name="custom-environment-variables"></a>

Set the following environment variables.

------
#### [ Linux and macOS ]

```
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_SESSION_TOKEN=your_session_token
```

------
#### [ Windows (PowerShell) ]

```
$env:AWS_ACCESS_KEY_ID="your_access_key"
$env:AWS_SECRET_ACCESS_KEY="your_secret_key"
$env:AWS_SESSION_TOKEN="your_session_token"
```

------

You can also specify a profile using the `AWS_PROFILE` environment variable.

------
#### [ Linux and macOS ]

```
export AWS_PROFILE=your_profile_name
```

------
#### [ Windows (PowerShell) ]

```
$env:AWS_PROFILE="your_profile_name"
```

------

**Note**  
Environment variables set with `$env:` in PowerShell apply to the current session only. To persist them across sessions, set them through **System Properties** > **Environment Variables**, or use `[System.Environment]::SetEnvironmentVariable()`.

### AWS Credentials File
<a name="custom-credentials-file"></a>

Configure credentials in the AWS credentials file, located at `~/.aws/credentials` on Linux and macOS, or `%USERPROFILE%\.aws\credentials` on Windows:

```
[default]
aws_access_key_id = your_access_key
aws_secret_access_key = your_secret_key
```

### IAM Permissions
<a name="custom-iam-permissions"></a>

Your AWS credentials must have permissions to call the AWS Transform custom service. We recommend attaching the [`AWSTransformCustomFullAccess`](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSTransformCustomFullAccess) AWS managed policy to your IAM user or role. This policy provides full access to AWS Transform custom, including the permission to create the [service-linked role](using-service-linked-roles.md#using-service-linked-roles-custom) required for CloudWatch metrics emission to your account.

For more granular control, AWS Transform custom also provides the following AWS managed policies:
+ [`AWSTransformCustomExecuteTransformations`](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSTransformCustomExecuteTransformations) – Provides access to execute transformations.
+ [`AWSTransformCustomManageTransformations`](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSTransformCustomManageTransformations) – Provides access to create, update, read, and delete transformation resources, as well as execute transformations.

For more information about these policies, see [AWS managed policies for AWS Transform](security-iam-awsmanpol.md). For custom IAM policies with resource-level permissions, refer to the [AWS Transform Custom IAM Service Authorization Reference Guide](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awstransformcustom.html).

**Note**  
Transformation definitions are AWS resources with ARNs (Amazon Resource Names). You can use IAM policies to control access to specific transformations or groups of transformations by specifying the transformation ARN in your IAM policy resource statements. Tags can be used for grouped access control.
AWS IAM Identity Center is required to access the AWS Transform, but is not required to use the CLI.

## Configuring AWS Region
<a name="custom-region-configuration"></a>

AWS Transform custom is available in specific AWS regions and automatically detects your region configuration using standard AWS CLI precedence.

### Supported Regions
<a name="custom-supported-regions"></a>

AWS Transform custom is available in the following AWS regions:
+ `us-east-1` (US East - N. Virginia)
+ `eu-central-1` (Europe - Frankfurt)
+ `eu-west-2` (Europe - London)
+ `ca-central-1` (Canada - Central)
+ `ap-northeast-1` (Asia Pacific - Tokyo)
+ `ap-northeast-2` (Asia Pacific - Seoul)
+ `ap-southeast-2` (Asia Pacific - Sydney)
+ `ap-south-1` (Asia Pacific - Mumbai)

### How Region is Determined
<a name="custom-region-priority"></a>

The CLI checks these sources in priority order to determine which region to use:

1. `AWS_REGION` environment variable (highest priority)

1. `AWS_DEFAULT_REGION` environment variable

1. Selected profile in the AWS config file (via `AWS_PROFILE` environment variable)

1. Default profile in the AWS config file

1. Default fallback to `us-east-1` if no configuration is found

**Note**  
The AWS config file is located at `~/.aws/config` on Linux and macOS, or `%USERPROFILE%\.aws\config` on Windows.

**Note**  
If `ATX_CUSTOM_ENDPOINT` is set, the region is extracted from the endpoint URL and overrides all other settings.

### Setting Your Region
<a name="custom-region-examples"></a>

Choose one of these methods to configure your region:

**Option 1: Environment variable (recommended for temporary use):**

------
#### [ Linux and macOS ]

```
export AWS_REGION=<your-region>
```

------
#### [ Windows (PowerShell) ]

```
$env:AWS_REGION="<your-region>"
```

------

**Option 2: AWS CLI configuration (recommended for permanent setup):**

```
aws configure set region <your-region>
```

**Option 3: Profile-specific configuration:**

------
#### [ Linux and macOS ]

```
aws configure set region <your-region> --profile your_profile_name
export AWS_PROFILE=your_profile_name
```

------
#### [ Windows (PowerShell) ]

```
aws configure set region <your-region> --profile your_profile_name
$env:AWS_PROFILE="your_profile_name"
```

------

**Option 4: Direct file editing:**

Edit the AWS config file directly (`~/.aws/config` on Linux and macOS, or `%USERPROFILE%\.aws\config` on Windows):

```
[default]
region = <your-region>

[profile your_profile_name]
region = <your-region>
```

### Verifying Your Region Configuration
<a name="custom-debug-region-resolution"></a>

To check which region AWS Transform custom will use:

**Check current region setting:**

```
aws configure get region
```

**Check environment variables:**

------
#### [ Linux and macOS ]

```
echo "AWS_REGION: $AWS_REGION"
echo "AWS_DEFAULT_REGION: $AWS_DEFAULT_REGION"
echo "AWS_PROFILE: $AWS_PROFILE"
```

------
#### [ Windows (PowerShell) ]

```
echo "AWS_REGION: $env:AWS_REGION"
echo "AWS_DEFAULT_REGION: $env:AWS_DEFAULT_REGION"
echo "AWS_PROFILE: $env:AWS_PROFILE"
```

------

**View detailed region resolution in debug logs:**

------
#### [ Linux and macOS ]

```
tail -f ~/.aws/atx/logs/debug.log
```

------
#### [ Windows (PowerShell) ]

```
Get-Content "$env:USERPROFILE\.aws\atx\logs\debug.log" -Wait -Tail 10
```

------

Example log output showing region source:

```
2026-01-07 22:34:28 [DEBUG]: Initializing FrontendServiceClient with config:
{
  "endpoint": "https://transform-custom.us-east-1.api.aws",
  "region": "us-east-1",
  "regionSource": "AWS_REGION"
}
```

The `regionSource` field shows where the region was derived from (e.g., "aws-config (profile: default)", "AWS\_REGION", "default").

**Important**  
If your region configuration points to an unsupported region, the CLI will display a clear error message with instructions to update your configuration to a supported region.

## Running Your First Transformation
<a name="custom-first-transformation"></a>

The fastest way to get started is to use an AWS-managed transformation. AWS-managed transformations are pre-built, AWS-vetted transformations that are ready to use without any setup.

**To run an AWS-managed transformation interactively:**

```
atx
```

Then ask the agent to execute a transformation:

```
Execute the AWS/java-aws-sdk-v1-to-v2 transformation on the codebase at ./my-java-project
```

**To run a transformation non-interactively:**

```
atx custom def exec -n AWS/java-aws-sdk-v1-to-v2 -p ./my-java-project -c "mvn clean install" -x -t
```

For detailed information about execution modes, configuration options, and command flags, see [Command Reference](custom-command-reference.md).

## Understanding Transformation Results
<a name="custom-understanding-results"></a>

When a transformation completes, AWS Transform custom provides a report describing the results. If the transformation was not validated (e.g. successful build for a Java applications), the report provides recommendations for further actions.

Most transformations are performed in multiple steps, using Git to commit intermediate ones. You can review the changes made by the transformation using standard Git commands:

```
git status
git log
git diff {{<original commit-id>}}
```

## Creating a Custom Transformation
<a name="custom-creating-custom"></a>

When AWS-managed transformations don't meet your needs, you can create custom transformations tailored to your specific requirements.

**To create a custom transformation**

1. Start the AWS Transform CLI in interactive mode:

   ```
   atx
   ```

1. Tell the agent you want to create a new transformation and describe your requirements.

1. Provide reference materials such as documentation and code samples to improve quality.

1. Test and refine the transformation iteratively.

1. Publish it to your organization's transformation registry.

For detailed instructions on creating custom transformations, see [Workflows](custom-workflows.md).

## AWS Transform Web Application (Optional)
<a name="custom-web-application"></a>

The AWS Transform web application is an optional interface for monitoring large-scale transformation campaigns across multiple repositories. Before using AWS Transform web application, you need to have a user identity enabled to access AWS Transform in your organization. For information about enabling AWS Transform, see [Setting up AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/transform-setup.html).

**To use the AWS Transform web application:**

1. Visit https://aws.amazon.com/transform/ and sign in using AWS IAM Identity Center credentials.

1. Select the "Custom / code" job type in the AWS Transform web application.

1. Tell the agent the name of the transformation definition you would like to use.

1. The web application provides an AWS Transform CLI command that can be shared with your team. This command invokes the transformation definition and logs execution results to the web application.

1. After transformation results are captured, view statistics, time savings measurements, and ask questions about the progress of your job in the Dashboard.

The web application is designed for enterprise-scale operations where you need centralized monitoring of transformations across multiple codebases.

**Note**  
AWS IAM Identity Center is required to access the AWS Transform web application. The CLI does not require IAM Identity Center - only standard AWS credentials are needed.