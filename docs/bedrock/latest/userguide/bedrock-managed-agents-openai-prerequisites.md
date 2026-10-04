

# Set up permissions and prerequisites
<a name="bedrock-managed-agents-openai-prerequisites"></a>

Before using Amazon Bedrock Managed Agents, powered by OpenAI, configure an AWS identity, select a supported Region and model, and prepare an execution environment.

## Prerequisites
<a name="bedrock-managed-agents-openai-prerequisites-prerequisites"></a>

For either example, install:
+ Node.js 20 or later and npm.
+ AWS CLI version 2, including `aws configure export-credentials`.
+ Bash, `curl` with AWS SigV4 support, and `jq`.
+ Codex CLI version 0.154.0 or later, which includes `codex exec-server`.

The AgentCore example also requires Python 3 and Docker with Linux ARM64 build support. Use Python 3.12 or later to run the supplied Runtime unit tests. The optional Python REST client requires the packages in `examples/requirements.txt`.

Use a dedicated workspace for agent execution. The agent can use the files, tools, and permissions available to that environment.

## Configure AWS credentials and Region
<a name="bedrock-managed-agents-openai-prerequisites-configure-aws-credentials-and-region"></a>

Configure an AWS profile using your organization's authentication method. For IAM Identity Center, see [Configure the AWS CLI with IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html).

Select the profile that you use to deploy the examples:

```
export AWS_PROFILE=my-deployment-profile
export AWS_REGION=us-east-1
export AWS_DEFAULT_REGION="$AWS_REGION"
export BMA_REGION="$AWS_REGION"
export BMA_ENDPOINT="https://bedrock-mantle.${BMA_REGION}.api.aws"
aws sts get-caller-identity
```

Check that the returned account is the account where you intend to create resources. Keep the AWS deployment Region, BMA signing Region, and endpoint consistent. An existing `AWS_REGION` or `AWS_DEFAULT_REGION` environment variable can override a profile's default Region.

The deployment identity needs permission to create the resources in the chosen CDK application. The identity that calls the BMA API can be a separate, more restricted role.

## Understand the IAM roles
<a name="bedrock-managed-agents-openai-prerequisites-understand-the-iam-roles"></a>


|  Identity or role  |  Purpose  | 
| --- | --- | 
| Deployment identity | Creates and deletes the example's CloudFormation, IAM, and other AWS resources. | 
| BMA client identity | Signs session and event requests. It needs BMA API permissions and `iam:PassRole` for the session role. | 
| Session role | BMA assumes this role for customer-authorized inference and configured AWS integrations. Supply its ARN in `role_arn` when creating a session. | 
| AgentCore Runtime execution role | The Runtime uses this role for image access, logging, storage, and exec-server registration. It is separate from the session role. | 

The examples create a session role named `BedrockManagedAgentsPreviewInferenceServiceRole`. This is the example's default name. You can use an existing role in the calling account if its trust and permissions meet the [session-role requirements](bedrock-managed-agents-openai-security.md). Set `BMA_INFERENCE_ROLE_ARN` to use a different role with the scripts.

Only one CloudFormation stack can own a role with a given name. If the example's session role already exists, deploy the other example with `ManageCustomerInferenceRole=false`. That option leaves the role's ownership and policies with the stack or IAM configuration that already manages it.

## Configure a client profile after deployment
<a name="bedrock-managed-agents-openai-prerequisites-configure-a-client-profile-after-deployment"></a>

After deploying an example, read `BmaAccessRoleArn` from the stack outputs. If your existing profile can assume that role, you can configure a separate AWS CLI profile:

```
BMA_ACCESS_ROLE_ARN=$(aws cloudformation describe-stacks \
  --stack-name BmaSelfHostedStack --region "$BMA_REGION" \
  --query "Stacks[0].Outputs[?OutputKey=='BmaAccessRoleArn'].OutputValue | [0]" \
  --output text)
aws configure set profile.bma-client.role_arn "$BMA_ACCESS_ROLE_ARN"
aws configure set profile.bma-client.source_profile my-deployment-profile
aws configure set profile.bma-client.region "$BMA_REGION"
export AWS_PROFILE=bma-client
aws sts get-caller-identity
```

Use `AcBmaStack` for the AgentCore example. Replace `my-deployment-profile` with your existing source profile. Your source identity must be authorized to call `sts:AssumeRole` on the generated client role. These commands configure a profile; the example's scripts only read the profile that you select.

## Get the examples and Codex exec server
<a name="bedrock-managed-agents-openai-prerequisites-get-the-examples-and-codex-exec-server"></a>

Download and extract the [BMA example bundle](samples/bma-examples.zip). The extracted directory contains `self-hosted/`, `acr/`, and an empty `bin/` directory.

The Codex executable is downloaded separately. Choose the binary for the host that will run it:


|  Execution host  |  Codex 0.154.0 archive  | 
| --- | --- | 
| macOS, Apple Silicon |  [macOS ARM64](https://github.com/openai/codex/releases/download/rust-v0.154.0/codex-aarch64-apple-darwin.tar.gz)  | 
| Linux, x86-64 |  [Linux x86-64](https://github.com/openai/codex/releases/download/rust-v0.154.0/codex-x86_64-unknown-linux-musl.tar.gz)  | 
| AgentCore Runtime or Linux ARM64 |  [Linux ARM64](https://github.com/openai/codex/releases/download/rust-v0.154.0/codex-aarch64-unknown-linux-musl.tar.gz)  | 

For example, extract the Linux ARM64 archive from the bundle root:

```
mkdir -p bin
tar -xzf /path/to/codex-aarch64-unknown-linux-musl.tar.gz -C bin
mv bin/codex-aarch64-unknown-linux-musl bin/codex
chmod +x bin/codex
```

Use the corresponding archive and extracted filename for a self-hosted Mac or Linux x86-64 host. For AgentCore, always use the Linux ARM64 executable, including when you deploy from a Mac. The AgentCore stack checks the binary before synthesis.

If you test both workflows on a Mac, keep the macOS and Linux executables at separate paths. Pass the macOS executable's path to the self-hosted attach script. Keep the Linux ARM64 executable at the bundle's `bin/codex` for the AgentCore image.

## Bootstrap AWS CDK
<a name="bedrock-managed-agents-openai-prerequisites-bootstrap-aws-cdk"></a>

From the example directory that you plan to deploy, install dependencies and bootstrap the account and Region:

```
npm ci
npx cdk bootstrap
```

Bootstrapping creates resources used by CDK to publish deployment assets. See [AWS CDK bootstrapping](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html). Bootstrap each account and Region where you deploy an example.

## Select a model
<a name="bedrock-managed-agents-openai-prerequisites-select-a-model"></a>

The session scripts default to `openai.gpt-5.6-luna`. Select an OpenAI model supported by BMA and available in your target Region and account. To override the example:

```
export BMA_MODEL=openai.gpt-5.6-luna
```

The optional signed Python client can list the endpoint's model catalog:

```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 bma_client.py GET /v1/models
```

The endpoint's catalog also contains models for other inference APIs. Catalog presence alone does not establish BMA compatibility. Model access and the session role's inference permissions are both required.