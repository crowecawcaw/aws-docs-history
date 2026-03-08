# Getting started with AWS DevOps Agent using AWS CDK

## Overview

This guide shows you how to use the AWS Cloud Development Kit (AWS CDK) to create and deploy AWS DevOps Agent resources. The CDK application automates the creation of an agent space, IAM roles, an operator app, and AWS account associations through AWS CloudFormation.

The CDK approach automates the manual steps described in the [CLI onboarding guide](getting-started-with-aws-devops-agent-cli-onboarding-guide.md "getting-started-with-aws-devops-agent-cli-onboarding-guide.md") by defining all required resources as infrastructure as code.

###### Note

AWS DevOps Agent is in preview. The instructions on this page may change before general availability (GA).

## Prerequisites

Before you begin, make sure you have the following:

- AWS CLI installed and configured with appropriate credentials
- Node.js version 18 or later
- AWS CDK CLI installed globally: `npm install -g aws-cdk`
- One AWS account for the monitoring (primary) account
- (Optional) A second AWS account if you want to set up cross-account monitoring

###### Important

AWS DevOps Agent is currently available in the `us-east-1` Region.

## What this guide covers

This guide is divided into two parts:

- **Part 1** — Deploy an agent space with an operator app and an AWS association in your monitoring account. After completing this part, the agent can monitor issues in that account.
- **Part 2 (Optional)** — Add a source AWS association for a service account and deploy a cross-account IAM role into that account. This allows the agent space to monitor resources across accounts.

## Resources created

### Part 1: DevOpsAgentStack (monitoring account)

- **IAM role** (`DevOpsAgentRole-AgentSpace`) — Assumed by the DevOps Agent service to monitor the account. Includes the `AIOpsAssistantPolicy` managed policy and inline policies for support and expanded permissions.
- **IAM role** (`DevOpsAgentRole-WebappAdmin`) — Operator app role with inline policies for agent operations and support actions.
- **Agent space** (`MyCDKAgentSpace`) — The central agent space, created using the `AWS::DevOpsAgent::AgentSpace` CloudFormation resource. Includes operator app configuration.
- **Association** (AWS monitor) — Links the monitoring account to the agent space using the `AWS::DevOpsAgent::Association` CloudFormation resource.
- **Association** (AWS source) — (Optional) Links the service account to the agent space for cross-account monitoring.

### Part 2: ServiceStack (service account, optional)

- **IAM role** (`DevOpsAgentRole-SecondaryAccount`) — Cross-account role with a fixed name. Trusted by the agent space in the monitoring account. Includes the `AIOpsAssistantPolicy` managed policy and expanded inline policies.
- **Lambda function** (`echo-service`) — A simple example service that echoes back input events.

## Setup

### Step 1: Clone the sample repository

```
git clone https://github.com/aws-samples/sample-aws-devops-agent-cdk.gitcd sample-aws-devops-agent-cdk
```

### Step 2: Install dependencies

```
npm install

```

## Part 1: Deploy the agent space

In this section, you create the agent space, IAM roles, operator app, and an AWS association in your monitoring account.

### Step 1: Configure the monitoring account ID

Open `lib/constants.ts` and set your monitoring account ID:

```
export const MONITORING_ACCOUNT_ID = "<YOUR_MONITORING_ACCOUNT_ID>";

```

### Step 2: Bootstrap the AWS CDK environment

If you have not bootstrapped the AWS CDK in your monitoring account, run the following command:

```
cdk bootstrap aws://<MONITORING_ACCOUNT_ID>/us-east-1 --profile monitoring
```

### Step 3: Build and deploy

Build the TypeScript code and deploy the stack:

```
npm run build
cdk deploy DevOpsAgentStack --profile monitoring
```

### Step 4: Record the stack outputs

After deployment completes, the AWS CDK prints the stack outputs. Record these values for later use:

```
Outputs:
DevOpsAgentStack.AgentSpaceArn = arn:aws:aidevops:us-east-1:123456789012:agentspace/abc123
DevOpsAgentStack.AgentSpaceRoleArn = arn:aws:iam::123456789012:role/DevOpsAgentRole-AgentSpace
DevOpsAgentStack.OperatorRoleArn = arn:aws:iam::123456789012:role/DevOpsAgentRole-WebappAdmin
DevOpsAgentStack.AssociationId = assoc-xyz
```

If you plan to complete Part 2, save the `AgentSpaceArn` value. You will need it to configure the service account stack.

### Step 5: Verify the deployment

Use the AWS CLI to verify that the agent space was created successfully:

```
aws devopsagent get-agent-space \
  --agent-space-id <AGENT_SPACE_ID> \
--region us-east-1
```

At this point, your agent space is deployed with the operator app enabled and your monitoring account associated. The agent can monitor issues in this account.

## Part 2 (Optional): Add cross-account monitoring

In this section, you extend the setup so the agent space can monitor resources in a second AWS account (the service account). This involves two actions:

1. Adding a source AWS association in the DevOpsAgentStack that points to the service account.
2. Deploying the ServiceStack into the service account with an IAM role that trusts the agent space.

###### Important

You must complete Part 1 before proceeding. The ServiceStack requires the `AgentSpaceArn` from the DevOpsAgentStack deployment output.

### Step 1: Configure the service account ID

Open `lib/constants.ts` and set your service account ID:

```
export const SERVICE_ACCOUNT_ID = "<YOUR_SERVICE_ACCOUNT_ID>";

```

The DevOpsAgentStack creates a source AWS association using this account ID. If you deployed the DevOpsAgentStack before setting this value, redeploy to create the association:

```
npm run build
cdk deploy DevOpsAgentStack --profile monitoring
```

### Step 2: Set the agent space ARN

Copy the `AgentSpaceArn` value from the DevOpsAgentStack output (Part 1, Step 4) and set it in `lib/constants.ts`:

```
export const AGENT_SPACE_ARN = "arn:aws:aidevops:us-east-1:<MONITORING_ACCOUNT_ID>:agentspace/<SPACE_ID>";

```

The ServiceStack uses this value to scope the trust policy on the secondary account role. The ServiceStack is only synthesized when this value is set.

### Step 3: Bootstrap the service account

If you have not bootstrapped the AWS CDK in your service account, run the following command:

```
cdk bootstrap aws://<SERVICE_ACCOUNT_ID>/us-east-1 --profile service

```

### Step 4: Deploy the ServiceStack

Build and deploy the ServiceStack using credentials for the service account:

```
npm run build
cdk deploy ServiceStack --profile service

```

This creates the following resources in the service account:

- An IAM role (`DevOpsAgentRole-SecondaryAccount`) that trusts the agent space in the monitoring account
- An echo Lambda function (`echo-service`) as an example service

### Step 5: Verify the deployment

Test the echo service to confirm the Lambda function was deployed successfully:

```
aws lambda invoke \
  --function-name echo-service \
--payload '{"test": "hello world"}' \
--profile service \
  response.json
cat response.json
```

## Troubleshooting

**CloudFormation resource type not found**

- Verify that you are deploying in the `us-east-1` Region.
- Confirm that your AWS CLI is configured with the appropriate permissions.

**IAM role creation failed**

- Verify that your deployment role has permissions to create IAM roles.
- Check that the trust policy conditions match your account ID.

**Cross-account deployment fails with "Could not assume role in target account"**

- Each stack must be deployed with credentials for the target account. Use the `--profile` flag to specify the correct AWS CLI profile.
- Verify that the AWS CDK has been bootstrapped in the target account.

**IAM propagation delays**

- IAM role changes can take a few minutes to propagate. If the agent space creation fails immediately after role creation, wait a few minutes and redeploy.

## Cleanup

To remove all resources, destroy the stacks in reverse order:

```
# If you deployed the ServiceStack, destroy it first
cdk destroy ServiceStack --profile service
# Then destroy the DevOpsAgentStack
cdk destroy DevOpsAgentStack --profile monitoring
```

**Warning:** This permanently deletes your agent space and all associated data. Make sure you have backed up any important information before proceeding.

## Security considerations

- The CDK application creates IAM roles with trust policies that only allow the `aidevops.amazonaws.com` service principal to assume them.
- Trust policies include conditions that restrict access to your specific AWS account and agent space ARN.
- All policies follow the principle of least privilege. Review and customize the IAM policies based on your organization's security requirements.
- The cross-account role (`DevOpsAgentRole-SecondaryAccount`) uses a fixed name and is scoped to a specific agent space ARN.

## Next steps

After you have deployed your AWS DevOps Agent using the AWS CDK:

1. Learn about the full range of DevOps Agent capabilities in the [AWS DevOps Agent User Guide](../userguide.md "../userguide.md").
2. Consider integrating the CDK deployment into your CI/CD pipelines for automated infrastructure management.

## Additional resources

- [AWS DevOps Agent User Guide](../userguide.md "../userguide.md")
- [Sample CDK repository](https://github.com/aws-samples/sample-aws-devops-agent-cdk "https://github.com/aws-samples/sample-aws-devops-agent-cdk")
- [CLI onboarding guide](getting-started-with-aws-devops-agent-cli-onboarding-guide.md "getting-started-with-aws-devops-agent-cli-onboarding-guide.md")
