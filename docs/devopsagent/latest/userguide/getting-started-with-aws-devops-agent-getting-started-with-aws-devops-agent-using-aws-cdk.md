# Getting started with AWS DevOps Agent using AWS CDK

## Overview

This guide shows you how to use AWS Cloud Development Kit (CDK) to create and deploy AWS DevOps Agent resources, including the agent space, IAM roles, and AWS account associations. Using CDK provides infrastructure as code benefits such as version control, repeatability, and automated deployment.

The CDK approach automates the manual steps described in the [CLI onboarding guide](getting-started-with-aws-devops-agent-cli-onboarding-guide.md "getting-started-with-aws-devops-agent-cli-onboarding-guide.md") by creating all required resources through CloudFormation.

###### Note

AWS DevOps Agent is in preview. The instructions on this page may change before general availability (GA).

## Prerequisites

- AWS CLI installed and configured with appropriate credentials
- Node.js (version 18 or later)
- AWS CDK CLI installed globally: `npm install -g aws-cdk`
- AWS DevOps Agent is available in us-east-1

## What gets created

The CDK stack creates the following resources using CloudFormation:

### IAM Roles

- **DevOpsAgentRole-AgentSpace**: Main role for the agent space with:
- Trust policy for `aidevops.amazonaws.com` service
- `AIOpsAssistantPolicy` managed policy
- Additional inline policies for support and expanded permissions
- **DevOpsAgentRole-WebappAdmin**: Operator app role with:
- Trust policy for `aidevops.amazonaws.com` service
- Inline policies for basic operator actions and support

### DevOps Agent Resources

- **Agent Space**: Created using `AWS::DevOpsAgent::AgentSpace` CloudFormation resource
- **AWS Association**: Created using `AWS::DevOpsAgent::Association` CloudFormation resource

## Setup

### 1. Clone the sample repository

```
git clone https://github.com/aws-samples/sample-aws-devops-agent-cdk.git
cd sample-aws-devops-agent-cdk

```

### 2. Install dependencies

```
npm install

```

### 3. Bootstrap your AWS environment

If you haven't bootstrapped CDK in your AWS account and region before:

```
cdk bootstrap --region us-east-1

```

### 4. Review the configuration

The CDK stack is pre-configured with sensible defaults. You can modify the following in `lib/sample-aws-devops-agent-cdk-stack.ts`:

- Agent space name (default: "MyAgentSpace")
- IAM role names
- Policy configurations

## Deployment

### 1. Build the TypeScript code

```
npm run build

```

### 2. Preview the changes

Review what resources will be created:

```
cdk diff --region us-east-1

```

### 3. Deploy the stack

```
cdk deploy --region us-east-1

```

The deployment will create all necessary resources and output important values:

- `AgentSpaceId`: The ID of the created agent space
- `AgentSpaceRoleArn`: The ARN of the agent space role
- `OperatorRoleArn`: The ARN of the operator role
- `AssociationId`: The ID of the AWS association

### 4. Enable the operator app

After deployment, run the provided script to enable the operator app:

```
./scripts/enable-operator-app.sh

```

This script uses the stack outputs to automatically configure the operator app with the correct role ARN and agent space ID.

## Verification

Verify your setup using the AWS CLI:

```
# Get details of your AgentSpace (replace <AGENT_SPACE_ID> with the output value)
aws devopsagent get-agent-space \
  --agent-space-id <AGENT_SPACE_ID> \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1

# List associations
aws devopsagent list-associations \
  --agent-space-id <AGENT_SPACE_ID> \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1

```

## Adding additional associations

After the initial deployment, you can extend your setup by adding associations for:

- Additional AWS accounts (cross-account monitoring)
- GitHub repositories
- ServiceNow instances
- Dynatrace environments
- Splunk instances
- New Relic accounts
- Datadog instances

Use the CLI commands from the [CLI onboarding guide](getting-started-with-aws-devops-agent-cli-onboarding-guide.md "getting-started-with-aws-devops-agent-cli-onboarding-guide.md") to add these associations to your CDK-created agent space.

## Customization

### Modifying IAM policies

To add custom permissions to the agent space role, modify the inline policy in the CDK stack:

```
agentSpaceRole.addToPolicy(new PolicyStatement({
  effect: Effect.ALLOW,
  actions: ['your-custom-action:*'],
  resources: ['*']
}));

```

### Adding multiple agent spaces

To create multiple agent spaces, instantiate additional `AgentSpace` constructs in your stack:

```
const secondAgentSpace = new CfnAgentSpace(this, 'SecondAgentSpace', {
  name: 'SecondAgentSpace',
  description: 'Second agent space for different environment'
});

```

### Cross-account deployment

To deploy the stack in a different account, ensure your CDK deployment role has the necessary permissions and specify the account in your CDK app:

```
new SampleAwsDevopsAgentCdkStack(app, 'SampleAwsDevopsAgentCdkStack', {
  env: {
    account: 'TARGET_ACCOUNT_ID',
    region: 'us-east-1'
  }
});

```

## Troubleshooting

### Common deployment issues

**CloudFormation resource not found** _Ensure you're deploying in the us-east-1 region_ Verify your AWS CLI is configured with appropriate permissions

**IAM role creation failed** _Check that your deployment role has IAM permissions_ Verify the trust policy conditions match your account ID

**IAM propagation delays** : The deployment script includes retry logic for IAM propagation. If deploying manually, wait a few minutes between role creation and usage.

**Agent space creation failed** _Ensure the DevOps Agent service is available in your region_ Check that the IAM role was created successfully before the agent space

### Updating the stack

To update your deployment with changes:

```
npm run build
cdk diff --region us-east-1
cdk deploy --region us-east-1

```

## Cleanup

To remove all resources created by the stack:

```
cdk destroy --region us-east-1

```

**Warning**

This will permanently delete your agent space and all associated data. Ensure you have backed up any important information before proceeding.

## Security considerations

- The CDK stack creates IAM roles with specific trust policies that only allow the DevOps Agent service to assume them
- All policies follow the principle of least privilege
- The agent space role includes conditions that restrict access to your specific AWS account and agent space
- Review and customize the IAM policies based on your organization's security requirements

## Next steps

After successfully deploying your AWS DevOps Agent using CDK:

1. **Explore capabilities**: Learn about the full range of DevOps Agent features in the [user guide](../userguide.md "../userguide.md")
2. **Automate further**: Consider integrating the CDK deployment into your CI/CD pipelines

## Additional resources

- [AWS DevOps Agent User Guide](../userguide.md "../userguide.md")
- [Sample CDK repository](https://github.com/aws-samples/sample-aws-devops-agent-cdk "https://github.com/aws-samples/sample-aws-devops-agent-cdk")
