# Get started with Amazon Bedrock AgentCore Runtime direct

code deployment

Direct code deployment enables you to bring your Python-based agent to Amazon Bedrock AgentCore Runtime
simply by packaging agent code and its dependencies in a .zip file archive. Your agent still
needs to follow [AgentCore Runtime requirements](runtime-service-contract.md "runtime-service-contract.md"): have an entrypoint .py file that either uses the
`@app.entrypoint` annotation from [Amazon Bedrock AgentCore Python
SDK](https://github.com/aws/bedrock-agentcore-sdk-python "https://github.com/aws/bedrock-agentcore-sdk-python") or implements `/invocations` POST and `/ping` GET
server endpoints.

To create your deployment package as .zip file archive, you can use [Amazon Bedrock AgentCore starter
toolkit](https://github.com/aws/bedrock-agentcore-starter-toolkit "https://github.com/aws/bedrock-agentcore-starter-toolkit") or follow the steps in the _Custom zip + boto3_ tab below, or any
other .zip file utility such as [7zip](https://www.7-zip.org/download.html "https://www.7-zip.org/download.html"). The examples shown in the following sections assume you're using a
command-line `zip` tool in a Linux or MacOS environment. To use the same commands
in Windows, you can [install the Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10 "https://docs.microsoft.com/en-us/windows/wsl/install-win10") to get a Windows-integrated version of
Ubuntu and Bash.

Note that AgentCore Runtime uses POSIX file permissions, so you may need to [set permissions for the deployment package folder](http://aws.amazon.com/premiumsupport/knowledge-center/lambda-deployment-package-errors/ "http://aws.amazon.com/premiumsupport/knowledge-center/lambda-deployment-package-errors/") before you create the .zip
file archive.

###### Topics

- [Prerequisites](#prerequisites "#prerequisites")
- [Step 1: Set up project and install dependencies](#step-1-setup "#step-1-setup")
- [Step 2: Create your agent project](#step-2-create-agent "#step-2-create-agent")
- [Step 3: Test locally](#step-3-test-locally "#step-3-test-locally")
- [Step 4: Enable observability for your
  agent](#step-4-enable-observability "#step-4-enable-observability")
- [Step 5: Deploy to AgentCore Runtime and invoke](#step-5-deploy "#step-5-deploy")
- [Step 6: Update or cleanup](#step-6-update-cleanup "#step-6-update-cleanup")
- [Direct code deployment concepts](#runtime-code-deploy-concepts "#runtime-code-deploy-concepts")
- [Common Issues](#common-issues-direct-code-deploy "#common-issues-direct-code-deploy")

## Prerequisites

Before you start, make sure you have:

- **AWS Account** with credentials configured. To
  configure your AWS credentials, see [Configuration and credential file settings in the AWS CLI.](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md")
- [**Uv**](https://docs.astral.sh/uv/getting-started/installation/ "https://docs.astral.sh/uv/getting-started/installation/")
  **installed** and [**Python 3.10+**](https://docs.astral.sh/uv/guides/install-python/ "https://docs.astral.sh/uv/guides/install-python/") installed
- **AWS Permissions**: To create and deploy an
  agent with the starter toolkit, you must have appropriate permissions. For
  information, see [Use the starter toolkit](runtime-permissions.md#runtime-permissions-starter-toolkit "runtime-permissions.md#runtime-permissions-starter-toolkit").
- **Model access**: Anthropic Claude Sonnet 4.0
  [enabled](../../../bedrock/latest/userguide/model-access-modify.md "../../../bedrock/latest/userguide/model-access-modify.md") in the Amazon Bedrock console. For information about using a
  different model with the Strands Agents see the _Model
  Providers_ section in the [Strands Agents
  SDK](https://strandsagents.com/latest/documentation/docs/ "https://strandsagents.com/latest/documentation/docs/") documentation.

## Step 1: Set up project and install dependencies

Initialize your project with the following commands:

```
uv init agentcore_runtime_direct_deploy --python 3.13
cd agentcore_runtime_direct_deploy
```

Add core packages:

```
uv add bedrock-agentcore strands-agents
```

Add optional packages:

```
uv add --dev bedrock-agentcore-starter-toolkit
```

Package descriptions:

- **bedrock-agentcore** - The Amazon Bedrock AgentCore SDK
  for building AI agents
- **strands-agents** - The [Strands Agents](https://strandsagents.com/latest/ "https://strandsagents.com/latest/") SDK
- **bedrock-agentcore-starter-toolkit** - The
  Amazon Bedrock AgentCore starter toolkit

Optional, `uv add aws-opentelemetry-distro`, to enable [Amazon Bedrock AgentCore observability traces](../../../xray/latest/devguide/xray-services-adot.md "../../../xray/latest/devguide/xray-services-adot.md").

Uv will automatically create a `pyproject.toml` file with
dependencies, `uv.lock` file with dependency closure and
`.venv` directory.

## Step 2: Create your agent project

Use the `agentcore create` command to set up a skeleton agent project with the framework of your choice:

```
agentcore create
```

The command will prompt you to:

- Choose a framework (choose Strands Agents for this tutorial)
- Provide a project name
- Choose a template (basic or production)
- Choose model provider and other options

This command generates:

- Agent code with your selected framework
- A `requirements.txt` file with necessary dependencies
- A `.bedrock_agentcore.yaml` configuration file
- Infrastructure as Code (IaC) files if production template is selected

## Step 3: Test locally

Make sure port 8080 is free before starting. See _Port 8080 in use (local
only)_ in [Common issues and solutions](runtime-get-started-toolkit.md#common-issues "runtime-get-started-toolkit.md#common-issues").

Open a terminal window and start your agent with the following command:

```
agentcore dev
```

Test your agent by opening another terminal window and enter the following
command:

```
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello!"}'
```

**Success:** You should see a response like
`{"result": "Hello! I'm here to help..."}`. In the terminal window that's
running the agent, enter `Ctrl+C` to stop the agent.

## Step 4: Enable observability for your

agent

[Amazon Bedrock AgentCore Observability](observability.md "observability.md") helps you trace, debug, and monitor agents
that you host in AgentCore Runtime. First enable CloudWatch Transaction Search by following the
instructions at [Enabling Amazon Bedrock AgentCore runtime observability](observability-configure.md#observability-configure-builtin "observability-configure.md#observability-configure-builtin"). To observe your agent,
see [View observability data for your Amazon Bedrock AgentCore agents](observability-view.md "observability-view.md").

## Step 5: Deploy to AgentCore Runtime and invoke

Deploy your agent using one of the following methods:

starter toolkit
The following steps will be required to deploy an agent to AgentCore Runtime,
refer to [Get started with the Amazon Bedrock AgentCore starter toolkit](runtime-get-started-toolkit.md "runtime-get-started-toolkit.md"), for
detailed steps. If Uv is available, the starter toolkit will recommend
direct code deployment. Otherwise it will default to container deployment
type.

Once you have your agent set up using `agentcore create`, use the `launch` command to create a zip deployment package, upload it to the specified bucket, and deploy the agent.

```
agentcore launch
```

Let's prompt the agent to tell a joke!

```
agentcore invoke '{"prompt":"Tell me a joke"}'
```

The first deployment takes time to install dependencies but subsequent
updates to the agent optimizes this by re-using zipped dependencies

###### Configuration management

You can modify your agent configuration at any time using the `configure` command:

```
agentcore configure -e src/main.py
```

The command allows you to update deployment parameters such as your VPC configuration, execution roles, session timeouts, and OAuth authorizer settings.

Custom zip + boto3
To download a wheel that's compatible with AgentCore Runtime, you use the uv pip
`--python-platform` option. AgentCore Runtime only supports **arm64** instruction set architecture, run the
following command. Replace `--python 3.x` with the version of the
Python runtime you are using.

```
uv pip install \
--python-platform aarch64-manylinux2014 \
--python-version 3.13 \
--target=deployment_package \
--only-binary=:all: \
-r pyproject.toml
```

Create a .zip file with the installed libraries at the project
root.

```
cd deployment_package
zip -r ../deployment_package.zip .
```

Add the `main.py` file and other files in your package
to the root of the .zip file.

```
cd ..
zip deployment_package.zip main.py
```

After you have created your .zip deployment package, you can use it to
create a new AgentCore Runtime or update an existing one. You can deploy your .zip
package using AgentCore Runtime API, AgentCore Runtime console and AWS Command Line
Interface. Amazon Bedrock AgentCore starter toolkit will take care of above steps
to create .zip.

###### Note

1. The maximum size for a .zip deployment package for AgentCore Runtime
   is 250 MB (zipped) and 750 MB (unzipped). Note that this limit
   applies to the combined size of all the files you upload.
2. The AgentCore Runtime needs permission to read the files in your
   deployment package. In Linux permissions octal notation,
   AgentCore Runtime needs 644 permissions for non-executable files
   (rw-r—r--) and 755 permissions (rwxr-xr-x) for directories and
   executable files.
3. In Linux and MacOS, use the `chmod` command to
   change file permissions on files and directories in your
   deployment package. For example, to give a non-executable file
   the correct permissions, run the following command, `chmod
644 <filepath>`. To change file permissions in
   Windows, see [Set, View, Change, or Remove Permissions on an
   Object](<https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc731667(v=ws.10)> "https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc731667(v=ws.10)") in the Microsoft Windows
   documentation.
   1. If you don't grant AgentCore Runtime the permissions it needs
      to access directories in your deployment package,
      AgentCore Runtime sets the permissions for those directories to
      755 (rwxr-xr-x).

A ZIP archive containing Linux **arm64**
dependencies needs to be uploaded to S3 as a pre-requisite to Create Agent
Runtime. The below code requires the specified S3 bucket to already exist.
Please follow the AWS documentation [here](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/create_bucket.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/create_bucket.html") to create an bucket using boto3. Following boto3 code will
upload .zip file archive to a s3 and create Amazon Bedrock AgentCore
runtime.

```
import boto3

account_id = "your aws account id"
agent_name = "strands_10_23"

s3_client = boto3.client('s3', region_name='us-west-2')
print("Uploading deployment.zip to S3...")
s3_client.upload_file(
    'deployment_package.zip', # archive on file system
    f"bedrock-agentcore-code-{account_id}-us-west-2", # bucket name
    f"{agent_name}/deployment_package.zip", # prefix
    ExtraArgs={'ExpectedBucketOwner': account_id} # ownership check
)
print("Upload completed successfully!")
print(f"S3 Location: s3://bedrock-agentcore-code-{account_id}-us-west-2/deployment_package.zip")

agentcore_client = boto3.client('bedrock-agentcore-control', region_name='us-west-2')
response = agentcore_client.create_agent_runtime(
    agentRuntimeName=agent_name,
    agentRuntimeArtifact={
        'codeConfiguration': {
            'code': {
                's3': {
                    'bucket': f"bedrock-agentcore-code-{account_id}-us-west-2",
                    'prefix': f"{agent_name}/deployment_package.zip"
                }
            },
            'runtime': 'PYTHON_3_13',
            'entryPoint': ['opentelemetry-instrument', 'main.py']
        } # if not adding otel dependency, remove opentelemetry-instrument from entrypoint array
    },
    networkConfiguration={"networkMode": "PUBLIC"},
    roleArn=f"arn:aws:iam::{account_id}:role/AmazonBedrockAgentCoreSDKRuntime-us-west-2"
)
print(f"Agent Runtime created successfully!")
print(f"Agent Runtime ARN: {response['agentRuntimeArn']}")
print(f"Status: {response['status']}")
```

To invoke an agent on Amazon Bedrock AgentCore runtime using boto3, refer: [https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-get-started-toolkit.html#invoke-programmatically](runtime-get-started-toolkit.md#invoke-programmatically "runtime-get-started-toolkit.md#invoke-programmatically")

console
You can deploy your agent using the Amazon Bedrock AgentCore console with managed runtime support. The console provides an intuitive interface for uploading ZIP files and configuring agent settings.

To deploy using the console, first create your deployment package following the steps in the _Custom zip + boto3_ tab above.

###### Create agent through console

To create your agent:

1. From the Agents home page, click **Host Agent**
2. Choose your source selection:
   - **S3 Source** - Upload from S3 bucket
   - **Local Upload** - Upload ZIP file from your computer
   - **Templates** - Use pre-built agent templates

3. Configure your agent settings:
   - Agent name
   - Runtime version (Python 3.13 recommended)
   - Entry point (e.g., `main.py`)
   - Execution role (create new or use existing)

4. Click **Create Agent** to deploy

###### Create endpoint

Click **Create Endpoint** to create a new endpoint for your agent. The endpoint name and associated version will be pre-filled.

###### Test endpoint

Select an endpoint and click **Test Endpoint** to navigate to the Playground/Sandbox for testing.

###### Execution role requirements

Your agent requires an execution role with appropriate permissions. For detailed information about execution roles and permissions, see [AgentCore Runtime permissions](runtime-permissions.md "runtime-permissions.md"). The execution role must include basic Amazon Bedrock AgentCore runtime permissions, S3 access permissions for your deployment package, and CloudWatch Logs permissions for observability.

## Step 6: Update or cleanup

Update or cleanup your agent using one of the following methods:

starter toolkit
To update previously deployed AgentCore Runtime execute:

```
agentcore launch
```

To delete all resources related to a AgentCore Runtime execute:

```
agentcore destroy
```

boto3
Following boto3 code will update an AgentCore Runtime.

```
import boto3

account_id = "your aws account id"
agent_name = "strands_10_23"

s3_client = boto3.client('s3', region_name='us-west-2')
print("Uploading deployment.zip to S3...")
s3_client.upload_file(
    'deployment_package.zip', # archive on file system
    f"bedrock-agentcore-code-{account_id}-us-west-2", # bucket name
    f"{agent_name}/deployment_package.zip", # prefix
    ExtraArgs={'ExpectedBucketOwner': account_id} # ownership check
)
print("Upload completed successfully!")
print(f"S3 Location: s3://bedrock-agentcore-code-{account_id}-us-west-2/deployment_package.zip")

bedrock_agentcore_client = boto3.client('bedrock-agentcore-control', region_name='us-west-2')
response = bedrock_agentcore_client.update_agent_runtime(
    agentRuntimeId='<your-agent-id>',
    agentRuntimeArtifact={
        'codeConfiguration': {
            'code': {
                's3': {
                    'bucket': f"bedrock-agentcore-code-{account_id}-us-west-2",
                    'prefix': 'strands/deployment_package.zip'
                }
            },
            'runtime': 'PYTHON_3_12',
            'entryPoint': ['opentelemetry-instrument', 'main.py']
        } # if not adding otel dependency, remove opentelemetry-instrument from entrypoint array
    },
    networkConfiguration={"networkMode": "PUBLIC"},
    roleArn=f"arn:aws:iam::{account_id}:role/AmazonBedrockAgentCoreSDKRuntime-us-west-2"
)

print(f"Agent Runtime updated successfully!")
print(f"Agent Runtime ARN: {response['agentRuntimeArn']}")
print(f"Status: {response['status']}")
```

Following boto3 code will delete Amazon Bedrock AgentCore runtime and .zip
archive file in s3.

```
import boto3

account_id = "your aws account id"
agent_name = "strands_10_23"

bedrock_agentcore_client = boto3.client('bedrock-agentcore-control', region_name='us-west-2')
print("Deleting Agent from Amazon Bedrock AgentCore Runtime!")
response = bedrock_agentcore_client.delete_agent_runtime(
    agentRuntimeId='<agent-id>'
)
print(f"Agent Runtime delete successfully!")
print(f"Status: {response['status']}")

s3_client = boto3.client('s3', region_name='us-west-2')
print("Deleting deployment archive from S3...")
s3_client.delete_object(
    Bucket=f"bedrock-agentcore-code-{account_id}-us-west-2",
    Key=f"{agent_name}/deployment_package.zip",
    ExtraArgs={'ExpectedBucketOwner': account_id}
)
print("Archive deleted successfully from S3!")
```

console

###### Update agent

From the Agent details page, click **Update hosting** to create a new version with updated code or configuration.

###### Update endpoint

Select an endpoint from the Endpoints table and click **Edit** to update the description or associated version.

###### Delete endpoint

Select an endpoint and click **Delete**. You'll need to type "delete" to confirm the deletion.

###### Delete agent

From the agent list or details page, select your agent and click **Delete** to remove the agent and all associated resources.

## Direct code deployment concepts

Learn about key concepts when using direct code deployment with
Amazon Bedrock AgentCore Runtime.

###### Topics

Amazon Bedrock AgentCore Runtime with direct code deployment uses a shared responsibility model
similar to AWS Lambda. AgentCore Runtime manages the Python runtime environment and
applies security patches automatically, while you focus on your agent code and
dependencies.

If you're using [container images to deploy your agents](getting-started-custom.md "getting-started-custom.md"), then AgentCore Runtime is responsible
to patch only compute kernel. In this case, you're responsible for rebuilding your
agent's container image from the latest secure image and redeploying the container
image.

This is summarized in the following table:

| Shared responsibility model | Deployment mode                                                                                                                                                                     | AgentCore Runtime's responsibility                                                                                                                                                         | Your responsibility |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------- |
| Direct deploy mode          | 1. Publish new language runtime version containing the<br>latest patches for language runtime.<br>2. Apply language runtime patches to existing AgentCore Runtime<br>direct deploy. | 1. Update your agent code, including dependencies, to<br>address any security vulnerabilities.                                                                                             |
| Container image             | 1. Automatically patch underlying compute OS kernel with<br>latest version.                                                                                                         | 1. Update your agent code, including dependencies, to<br>address any security vulnerabilities.<br>2. Regularly re-build and re-deploy your container image<br>using the latest base image. |

For more information about shared responsibility with AWS, see [Shared
Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/").

AgentCore Runtime keeps each direct code deploy runtime up to date with security updates,
bug fixes, new features, performance enhancements, and support for minor version
releases. These runtime updates are published as _runtime
versions_. AgentCore Runtime applies direct code deploy runtime updates to
agents by migrating the agents from an earlier runtime version to a new runtime
version.

For direct deploy runtimes, AgentCore Runtime applies runtime updates automatically. With
automatic runtime updates, AgentCore Runtime takes on the operational burden of patching the
runtime versions. For most customers, this should be a safe choice as only language
runtime patches will be automatically applied and customers are responsible to bring
and managed their code dependencies. Currently AgentCore Runtime doesn't support changing
this automated patching behavior.

AgentCore Runtime strives to provide runtime updates that are backward compatible with
existing functions. However, as with software patching, there are rare cases in
which a runtime update can negatively impact an existing function. For example,
security patches can expose an underlying issue with an existing function that
depends on the previous, insecure behavior. If in extremely rare cases this risk is
not acceptable, please use [container images to deploy your agent](getting-started-custom.md "getting-started-custom.md").

The following table lists the supported AgentCore Runtime direct code deploy language
runtimes and projected deprecation dates. After a language environment is
deprecated, you're still able to create and update functions for a limited period.
The table provides the currently forecasted dates for runtime deprecation, based on
our [Runtime deprecation policy](../../../lambda/latest/dg/lambda-runtimes.md#runtime-support-policy "../../../lambda/latest/dg/lambda-runtimes.md#runtime-support-policy"). These dates are provided for planning
purposes and are subject to change.

| Supported runtimes | #           | Name          | Identifier        | Operating system | Deprecation date | Block function update |
| ------------------ | ----------- | ------------- | ----------------- | ---------------- | ---------------- | --------------------- |
| 1                  | Python 3.13 | `PYTHON_3_13` | Amazon Linux 2023 | 6/30/2029        | 8/31/2029        |
| 2                  | Python 3.12 | `PYTHON_3_12` | Amazon Linux 2023 | 10/31/2028       | 1/10/2029        |
| 3                  | Python 3.11 | `PYTHON_3_11` | Amazon Linux 2023 | 6/30/2026        | 8/31/2026        |
| 4                  | Python 3.10 | `PYTHON_3_10` | Amazon Linux 2023 | 6/30/2026        | 8/31/2026        |

#### Language environment deprecation

policy

AgentCore Runtime direct code deploy for .zip file archives are built around a
combination of operating system, programming language, and software libraries
that are subject to maintenance and security updates. AgentCore Runtime standard
deprecation policy is to deprecate a language runtime when any major component
of the runtime reaches the end of community long-term support (LTS) and security
updates are no longer available. Most usually, this is the language runtime,
though in some cases, a runtime can be deprecated because the operating system
(OS) reaches end of LTS.

After a runtime is deprecated, AWS may no longer apply security patches or
updates to that runtime, and functions using that runtime are no longer eligible
for technical support. Such deprecated runtimes are provided 'as-is', without
any warranties, and may contain bugs, errors, defects, or other
vulnerabilities.

###### Important

AgentCore Runtime occasionally delays deprecation of a AgentCore Runtime direct code
deploy programming language runtime for a limited period beyond the end of
support date of the language version that the runtime supports. During this
period, AgentCore Runtime only applies security patches to the runtime OS. AgentCore Runtime
doesn't apply security patches to programming language runtimes after they
reach their end of support date.

Some of the dimensions of comparison to see how one option differs from the other,
so it helps to choose the right option

- **Deployment Process**: Direct code
  deployment deploys agents using ZIP files instead of containers, lending
  itself to faster development iterations.
- **Deployment time**: Although there is not
  much difference during first deployment of an agent, subsequent updates to
  the agent are significantly faster with direct code deployment.
- **Customization**: Direct code supports for
  custom dependencies through ZIP-based packaging while maintaining deployment
  simplicity while container based depends on a Docker file.
- **Package size**: Direct code deployment
  limits the package size to 250MB whereas container based packages can be
  upto 1GB in size.
- **Session creation rate**: The direct code
  deployment allows for higher session creation of 25 new sessions/second
  compared to 0.16 new sessions/second with container based
  deployments.
  Our general guidance is

- If the size of the deployment package exceeds 250MB, and you have existing
  container CI/CD pipelines, and you need highly specialized dependencies and
  packaging, then container based deployments is a good option to
  choose.
- If the size of the deployment package is small, the code and package is
  not complex to build and uses common frameworks and languages, and you need
  rapid prototyping and iteration, then direct code deployment would be the
  option.
  There can also be a hybrid option where developers use the direct code deployment
  to quickly experiment and prototype agents and then switch to container based
  deployments (for the above reasons) to develop, test and deploy to
  production.

When you use an `import` statement in your code, the Python runtime
searches the directories in its search path until it finds the module or package. By
default, the first location the runtime searches is the directory into which your
.zip deployment package is decompressed and mounted
(`/var/task`).

You can see the full search path for your AgentCore Runtime agent by adding the following
code snippet.

```
import sys
search_path = sys.path
print(search_path)
```

You can also add dependencies in a separate folder inside your .zip package. For
example, you might add a version of the Boto3 SDK to a folder in your .zip package
called `common`. When your .zip package is decompressed and
mounted, this folder is placed inside the `/var/task` directory.
To use a dependency from a folder in your .zip deployment package in your code, use
an `import from` statement. For example, to use a version of Boto3 from a
folder named `common` in your .zip package, use the following
statement.

```
from common import boto3
```

We recommend that you don't include `__pycache__` folders in
your agent's deployment package. Python bytecode that's compiled on a build machine
with a different architecture or operating system might not be compatible with the
AgentCore Runtime execution environment.

If your function uses only pure Python packages and modules, you can use the
`uv pip install` command to install your dependencies on any local
build machine and create your .zip file. Many popular Python libraries, including
NumPy and Pandas, are not pure Python and contain code written in C or C++. When you
add libraries containing C/C++ code to your deployment package, you must build your
package correctly to make it compatible with the AgentCore Runtime execution
environment.

Most packages available on the Python Package Index ([PyPI](https://pypi.org/ "https://pypi.org/")) are available as "wheels" (.whl files). A
.whl file is a type of ZIP file which contains a built distribution with
pre-compiled binaries for a particular operating system and instruction set
architecture. To make your deployment package compatible with Amazon Bedrock AgentCore
AgentCore Runtime, you install the wheel for Linux operating systems and **arm64** instruction set architecture.

Some packages may only be available as source distributions. For these packages,
you need to compile and build the C/C++ components yourself.

To see what distributions are available for your required package, do the
following:

1. Search for the name of the package on the [Python Package Index main page](https://pypi.org/ "https://pypi.org/").
2. Choose the version of the package you want to use.
3. Choose **Download files**.
   If your package is only available as a source distribution, you need to build the
   C/C++ libraries yourself. To make your package compatible with the Amazon Bedrock AgentCore
   AgentCore Runtime execution environment, you need to build it in an environment that uses
   the same Amazon Linux operating system with **arm64**
   instruction set. You can do this by building your package in an Amazon Elastic
   Compute Cloud (Amazon EC2) Linux instance.

To learn how to launch and connect to an Amazon EC2 Linux instance, see [Get started with Amazon EC2](../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md "../../../AWSEC2/latest/UserGuide/EC2_GetStarted.md") in the _Amazon EC2 User
Guide_.

## Common Issues

Common issues and solutions when getting started with the Amazon Bedrock AgentCore starter
toolkit. For more troubleshooting information, see [Troubleshoot Amazon Bedrock AgentCore AgentCore Runtime](runtime-troubleshooting.md "runtime-troubleshooting.md").

### Permission Issues - Insufficient S3

permissions

**When this occurs:** During agent creation or update
with zipped artifact in S3 via console, SDK, or CLI

**Why this happens:** The role used to call
Create/UpdateAgentRuntime does not have s3:GetObject permissions on S3 uri passed in
the API input.

**Solution:** Add s3:GetObject permission in role
used to call the Agentcore Runtime create/update API.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
        "Effect": "Allow",
        "Action": "s3:GetObject",
        "Resource": "arn:aws:s3:::your-bucket-name/*"
    }
  ]
}
```

### Permission Issues - CMK Encrypted S3 Object

Access

**When this occurs:** During agent creation with
CMK-encrypted S3 objects when the execution role lacks KMS decrypt
permissions.

**Why this happens:** The role used to call
Create/UpdateAgentRuntime does not have kms:Decrypt permissions on the CMK used to
encrypt the S3 object containing the agent code.

**Solution:** Add kms:Decrypt permission to the role
for the specific CMK:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
        "Effect": "Allow",
        "Action": [
            "s3:GetObject",
            "kms:Decrypt"
        ],
        "Resource": [
            "arn:aws:s3:::your-bucket-name/*",
            "arn:aws:kms:us-west-2:your-account:key/your-cmk-key-id"
        ]
    }
  ]
}
```

### Code Package Compatibility

Issues

**When this occurs:** During agent creation or update
with incompatible code packages (wrong architecture, Python version, or package
format).

**Why this happens:** The uploaded ZIP file contains
binaries compiled for wrong architecture (ARM64 vs x86_64), incompatible Python
version, or incorrect package structure that doesn't match AgentCore Runtime
requirements.

**Solution:**

- Ensure code is compiled for arm64
- Use compatible Python version (check AgentCore Runtime supported versions)
- Verify ZIP structure contains proper entry points and dependencies
- Rebuild packages on compatible runtime environment

**Error indicators:**

- Agent status: CREATE_FAILED or runtime errors
- Import errors or "cannot execute binary file" messages in cloudwatch
  logs
- Architecture mismatch errors when you do getAgentRuntimeEndpoint.
