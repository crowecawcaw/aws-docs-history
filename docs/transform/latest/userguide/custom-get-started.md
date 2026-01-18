# Getting Started

This section describes how to set up AWS Transform custom and run your first transformation.

## Prerequisites

Before installing AWS Transform custom, ensure you have the following:

### Supported Platforms

AWS Transform custom supports the following operating systems:

- **Linux** - Full support for all Linux distributions
- **macOS** - Full support for macOS systems
- **Windows Subsystem for Linux (WSL)** - Supported when running under WSL

###### Important

Windows native execution is not supported. AWS Transform custom will detect native Windows environments and exit with an error message. For Windows users, install and use Windows Subsystem for Linux (WSL).

### Required Software

- **Node.js 20 or later** - Download from https://nodejs.org/en/download
- **Git** - Must be installed and the working directory needs to be a valid Git repo to execute a transformation. Run `git init; git add .; git commit -m "Initial commit"` to initialize a Git repo in your working directory.

### Network Requirements

An internet connection with access to the following endpoints is required:

- `desktop-release.transform.us-east-1.api.aws`
- `transform-custom.<region>.api.aws`
- `*.s3.amazonaws.com`

If you are working in an internet-restricted environment, update firewall rules to allowlist these URLs.

## Installing the AWS Transform CLI

The recommended installation method is using the installation script.

**To install the AWS Transform CLI**

1. Run the installation script:

```
curl -fsSL https://desktop-release.transform.us-east-1.api.aws/install.sh | bash
```

2. Verify the installation:

```
atx --version
```

The command should display the installed version of the AWS Transform CLI.

## Configuring Authentication

AWS Transform custom requires AWS credentials to authenticate with the service. Configure authentication using one of the following methods.

### Environment Variables

Set the following environment variables:

```
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_SESSION_TOKEN=your_session_token
```

You can also specify a profile using the `AWS_PROFILE` environment variable:

```
export AWS_PROFILE=your_profile_name
```

### AWS Credentials File

Configure credentials in `~/.aws/credentials`:

```
[default]
aws_access_key_id = your_access_key
aws_secret_access_key = your_secret_key
```

### IAM Permissions

Your AWS credentials must have permissions to call the AWS Transform service. At minimum, you need `transform-custom:*` permissions.

The following IAM policy provides full access to AWS Transform custom:

```
{
  "Version": "2012-10-17"		 	 	 ,
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "transform-custom:*"
      ],
      "Resource": "*"
    }
  ]
}
```

For more granular control, please refer to the [AWS Transform Custom IAM Service Authorization Reference Guide](../../../service-authorization/latest/reference/list_awstransformcustom.md "../../../service-authorization/latest/reference/list_awstransformcustom.md")

###### Note

- Transformation definitions are AWS resources with ARNs (Amazon Resource Names).
  You can use IAM policies to control access to specific transformations or groups of transformations by specifying
  the transformation ARN in your IAM policy resource statements. Tags can be used for grouped access control.
- AWS IAM Identity Center is required to access the AWS Transform, but is not required to use the CLI.

## Configuring AWS Region

AWS Transform custom is available in specific AWS regions and automatically detects your region configuration using standard AWS CLI precedence.

### Supported Regions

AWS Transform custom is available in the following AWS regions:

- `us-east-1` (US East - N. Virginia)
- `eu-central-1` (Europe - Frankfurt)

### How Region is Determined

The CLI checks these sources in priority order to determine which region to use:

1. `AWS_REGION` environment variable (highest priority)
2. `AWS_DEFAULT_REGION` environment variable
3. Selected profile in `~/.aws/config` (via `AWS_PROFILE` environment variable)
4. Default profile in `~/.aws/config`
5. Default fallback to `us-east-1` if no configuration is found

###### Note

If `ATX_CUSTOM_ENDPOINT` is set, the region is extracted from the endpoint URL and overrides all other settings.

### Setting Your Region

Choose one of these methods to configure your region:

**Option 1: Environment variable (recommended for temporary use):**

```
export AWS_REGION=<your-region>
```

**Option 2: AWS CLI configuration (recommended for permanent setup):**

```
aws configure set region <your-region>
```

**Option 3: Profile-specific configuration:**

```
aws configure set region <your-region> --profile your_profile_name
export AWS_PROFILE=your_profile_name
```

**Option 4: Direct file editing:**

Edit `~/.aws/config` directly:

```
[default]
region = <your-region>

[profile your_profile_name]
region = <your-region>
```

### Verifying Your Region Configuration

To check which region AWS Transform custom will use:

**Check current region setting:**

```
aws configure get region
```

**Check environment variables:**

```
echo "AWS_REGION: $AWS_REGION"
echo "AWS_DEFAULT_REGION: $AWS_DEFAULT_REGION"
echo "AWS_PROFILE: $AWS_PROFILE"
```

**View detailed region resolution in debug logs:**

```
tail -f ~/.aws/atx/logs/debug.log
```

Example log output showing region source:

```
2026-01-07 22:34:28 [DEBUG]: Initializing FrontendServiceClient with config:
{
  "endpoint": "https://transform-custom.us-east-1.api.aws",
  "region": "us-east-1",
  "regionSource": "AWS_REGION"
}
```

The `regionSource` field shows where the region was derived from (e.g., "aws-config (profile: default)", "AWS_REGION", "default").

###### Important

If your region configuration points to an unsupported region, the CLI will display a clear error message with instructions to update your configuration to a supported region.

## Running Your First Transformation

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

For detailed information about execution modes, configuration options, and command flags, see [Command Reference](custom-command-reference.md "custom-command-reference.md").

## Understanding Transformation Results

When a transformation completes, AWS Transform custom provides a report describing the results. If the transformation was not validated (e.g. successful build for a Java applications), the report provides recommendations for further actions.

Most transformations are performed in multiple steps, using Git to commit intermediate ones. You can review the changes made by the transformation using standard Git commands:

```
git status
git log
git diff `<original commit-id>`
```

## Creating a Custom Transformation

When AWS-managed transformations don't meet your needs, you can create custom transformations tailored to your specific requirements.

**To create a custom transformation**

1. Start the AWS Transform CLI in interactive mode:

```
atx
```

2. Tell the agent you want to create a new transformation and describe your requirements.
3. Provide reference materials such as documentation and code samples to improve quality.
4. Test and refine the transformation iteratively.
5. Publish it to your organization's transformation registry.

For detailed instructions on creating custom transformations, see [Workflows](custom-workflows.md "custom-workflows.md").

## AWS Transform Web Application (Optional)

The AWS Transform web application is an optional interface for monitoring large-scale transformation campaigns across multiple repositories. Before using AWS Transform web application, you need to have a user identity enabled to access AWS Transform in your organization. For information about enabling AWS Transform, see [Setting up AWS Transform](transform-setup.md "transform-setup.md").

**To use the AWS Transform web application:**

1. Visit https://aws.amazon.com/transform/ and sign in using AWS IAM Identity Center credentials.
2. Select the "Custom / code" job type in the AWS Transform web application.
3. Tell the agent the name of the transformation definition you would like to use.
4. The web application provides an AWS Transform CLI command that can be shared with your team. This command invokes the transformation definition and logs execution results to the web application.
5. After transformation results are captured, view statistics, time savings measurements, and ask questions about the progress of your job in the Dashboard.

The web application is designed for enterprise-scale operations where you need centralized monitoring of transformations across multiple codebases.

###### Note

AWS IAM Identity Center is required to access the AWS Transform web application. The CLI does not require IAM Identity Center - only standard AWS credentials are needed.
