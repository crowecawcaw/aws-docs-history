

# Run your agent on Amazon Bedrock AgentCore Runtime
<a name="bedrock-managed-agents-openai-agentcore-runtime"></a>

This tutorial deploys an AgentCore Runtime that runs `codex exec-server` for BMA. BMA activates the Runtime for agent work. You do not attach an exec server manually.

## What the example creates
<a name="bedrock-managed-agents-openai-agentcore-runtime-what-the-example-creates"></a>

The CDK application creates an ARM64 Runtime, its execution role, a BMA client role, and an optional session role. It also creates:
+ A VPC with private subnets, an S3 gateway endpoint, and one NAT gateway.
+ A versioned skills bucket and a versioned outputs bucket with public access blocked.
+ S3 Files filesystems, mount targets, and access points for the buckets.
+ AgentCore session storage mounted at `/mnt/workspace`.

The Runtime's network rules allow HTTPS egress and NFS connections to the example's S3 Files mount targets. See [security](bedrock-managed-agents-openai-security.md) for the roles and storage permissions.

These resources can incur charges until you remove them. Use a development account and retain only the test data that you need.

## Step 1: Prepare the container build
<a name="bedrock-managed-agents-openai-agentcore-runtime-step-1-prepare-the-container-build"></a>

Complete the [prerequisites](bedrock-managed-agents-openai-prerequisites.md). Save the Linux ARM64 Codex executable at `bin/codex` in the bundle root, and ensure that Docker is running with ARM64 build support.

From the bundle root:

```
cd acr
export AWS_PROFILE=my-deployment-profile
export AWS_REGION=us-east-1
export AWS_DEFAULT_REGION="$AWS_REGION"
export BMA_REGION="$AWS_REGION"
export BMA_ENDPOINT="https://bedrock-mantle.${BMA_REGION}.api.aws"
npm ci
npx cdk bootstrap
```

## Step 2: Deploy
<a name="bedrock-managed-agents-openai-agentcore-runtime-step-2-deploy"></a>

```
npm run deploy -- \
  --parameters BmaRegion="$BMA_REGION" \
  --parameters BmaEndpoint="$BMA_ENDPOINT"
```

If the session role already exists, add `--parameters ManageCustomerInferenceRole=false`. For example, use that option when the self-hosted stack owns the role.

Wait for the stack to reach `CREATE_COMPLETE` or `UPDATE_COMPLETE`. The outputs include `RuntimeArn`, `SkillsBucketName`, `OutputsBucketName`, `BmaAccessRoleArn`, and `CustomerInferenceRoleArn`.

The Runtime and its storage must be available in the deployment Region. Use Availability Zones enabled for your account. See [troubleshooting](bedrock-managed-agents-openai-troubleshooting.md) if deployment fails while creating networking or storage resources.

## Step 3: Create a BMA session
<a name="bedrock-managed-agents-openai-agentcore-runtime-step-3-create-a-bma-session"></a>

Select your BMA client profile:

```
export AWS_PROFILE=my-bma-client-profile
./scripts/bma/0.create-session.sh
```

The script obtains the Runtime ARN from `AcBmaStack`. You can instead set `BMA_AGENTCORE_RUNTIME_ARN` explicitly, such as when using a Runtime that another stack manages.

The session's environment uses `type: "aws_bedrock_agentcore"`. It identifies the Runtime ARN, a Runtime qualifier, a workspace directory, and capability directories. The default qualifier is `DEFAULT`.

## Step 4: Run the sample skill
<a name="bedrock-managed-agents-openai-agentcore-runtime-step-4-run-the-sample-skill"></a>

```
./scripts/bma/2.submit-turn.sh "Run the hello-bma skill."
./scripts/bma/3.read-result.sh
```

BMA invokes the Runtime adapter, which prepares storage and starts the exec server. The sample skill verifies that its files reached the execution environment. It reads the skill instructions and lists the available skills.

You can inspect the BMA session while work is running:

```
./scripts/bma/1.status.sh
```

The BMA session role authorizes Runtime activation and cleanup. The Runtime execution role authorizes the container's registration and connection to BMA. The adapter uses the Runtime role and rejects requests that attempt to supply alternative AWS credentials.

## Workspace, skills, and outputs
<a name="bedrock-managed-agents-openai-agentcore-runtime-workspace-skills-and-outputs"></a>


|  Container path  |  Purpose  | 
| --- | --- | 
|  `/mnt/workspace`  | AgentCore session storage and the agent's working directory | 
|  `/mnt/workspace/skills`  | Skills made available for capability discovery | 
|  `/mnt/bma/skills`  | Skills from the S3 Files mount | 
|  `/mnt/output`  | Generated files synchronized to the outputs bucket | 

The adapter copies the mounted skills into the workspace when it activates. Use [skills and tools](bedrock-managed-agents-openai-skills-tools.md) to add your own skill files.

To generate a file:

```
./scripts/bma/2.submit-turn.sh "Write the text BMA_OUTPUT_VERIFIED to /mnt/output/verification.txt, then read it back."
./scripts/bma/3.read-result.sh
```

Retrieve the bucket name and the file:

```
OUTPUTS_BUCKET=$(aws cloudformation describe-stacks \
  --stack-name AcBmaStack --region "$BMA_REGION" \
  --query "Stacks[0].Outputs[?OutputKey=='OutputsBucketName'].OutputValue | [0]" \
  --output text)
aws s3 cp "s3://${OUTPUTS_BUCKET}/verification.txt" ./verification.txt
```

S3 Files synchronization is asynchronous. A completed agent write can precede the object's availability through the S3 API. Retry the download after synchronization if the object is not yet available.

## Runtime lifecycle
<a name="bedrock-managed-agents-openai-agentcore-runtime-runtime-lifecycle"></a>

The example sets both the idle timeout and maximum compute lifetime to 28,800 seconds (eight hours). Keep these settings for the preview example. The adapter also supports bounded turn leases so active work can report busy health to AgentCore.

A maximum compute lifetime still applies while a turn is busy. Compute replacement does not preserve running processes or sockets. The adapter stores connection state in session storage and uses it when replacement compute is activated for the same Runtime session.

Session storage and the S3-backed files have different lifecycles. Review [AgentCore Runtime lifecycle settings](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-lifecycle-settings.html) and [filesystem configuration](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-filesystem-configurations.html) before relying on persistence across compute replacement or Runtime updates.

## Step 5: Clean up
<a name="bedrock-managed-agents-openai-agentcore-runtime-step-5-clean-up"></a>

```
./scripts/bma/4.delete-session.sh
export AWS_PROFILE=my-deployment-profile
npm run destroy
```

Download any outputs that you want to keep first. The sample stack uses destructive removal policies for its storage resources, including automatic deletion of objects. See [cleanup](bedrock-managed-agents-openai-cleanup.md) when both example stacks share the session role.