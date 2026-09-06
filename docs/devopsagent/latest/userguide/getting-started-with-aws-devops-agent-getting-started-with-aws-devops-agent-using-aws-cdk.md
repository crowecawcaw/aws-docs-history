

# Getting started with AWS DevOps Agent using AWS CDK
<a name="getting-started-with-aws-devops-agent-getting-started-with-aws-devops-agent-using-aws-cdk"></a>

## Overview
<a name="overview"></a>

This guide shows you how to use the AWS Cloud Development Kit (AWS CDK) to create and deploy AWS DevOps Agent resources. The AWS CDK application automates the creation of an agent space, AWS Identity and Access Management (IAM) roles, an operator app, and AWS account associations through AWS CloudFormation.

The AWS CDK approach automates the manual steps described in the [CLI onboarding guide](https://docs.aws.amazon.com/devopsagent/latest/userguide/getting-started-with-aws-devops-agent-cli-onboarding-guide.html) by defining all required resources as infrastructure as code.

AWS DevOps Agent is available in multiple AWS Regions. For the full list, see [Supported Regions](about-aws-devops-agent-supported-regions.md).

## Prerequisites
<a name="prerequisites"></a>

Before you begin, make sure that you have the following:
+ AWS Command Line Interface (AWS CLI) installed and configured with the appropriate credentials
+ Node.js version 18 or later
+ AWS CDK command line interface (CLI) installed globally. To install the AWS CDK CLI, run the following command:

```
npm install -g aws-cdk
```
+ One AWS account for the monitoring (primary) account
+ (Optional) A second AWS account if you want to set up cross-account monitoring
+ (For Part 3) `aws-cdk-lib` version 2.268.0 or later. The `CfnAsset` and `CfnTrigger` constructs used in Part 3 were added in that version. To check the version in your project, run `npm list aws-cdk-lib`.

## What this guide covers
<a name="what-this-guide-covers"></a>

This guide is divided into the following parts:
+ **Part 1** — Deploy an agent space with an operator app and an AWS association in your monitoring account. After you complete this part, the agent can monitor issues in that account.
+ **Part 2 (Optional)** — Add a source AWS association for a service account and deploy a cross-account IAM role into that account. This configuration enables the agent space to monitor resources across accounts.
+ **Part 3 (Optional)** — Add a skill, a custom agent, and a scheduled trigger to the agent space, so the agent has custom knowledge and the scheduled trigger runs that custom agent automatically.

## Resources created
<a name="resources-created"></a>

### Part 1: DevOpsAgentStack (monitoring account)
<a name="part-1-devopsagentstack-monitoring-account"></a>
+ **IAM role** (`DevOpsAgentRole-AgentSpace`) — Assumed by the DevOps Agent service to monitor the account. Includes the `AIDevOpsAgentAccessPolicy` managed policy and an inline policy that allows creation of the Resource Explorer service-linked role.
+ **IAM role** (`DevOpsAgentRole-WebappAdmin`) — Operator app role with the `AIDevOpsOperatorAppAccessPolicy` managed policy for agent operations.
+ **Agent space** (`MyCDKAgentSpace`) — The central agent space, created by using the `AWS::DevOpsAgent::AgentSpace` CloudFormation resource. Includes operator app configuration.
+ **Association** (AWS monitor) — Links the monitoring account to the agent space by using the `AWS::DevOpsAgent::Association` CloudFormation resource.
+ **Association** (AWS source) — (Optional) Links the service account to the agent space for cross-account monitoring.

### Part 2: ServiceStack (service account, optional)
<a name="part-2-servicestack-service-account-optional"></a>
+ **IAM role** (`DevOpsAgentRole-SecondaryAccount`) — Cross-account role with a fixed name. Trusted by the agent space in the monitoring account. Includes the `AIDevOpsAgentAccessPolicy` managed policy and an inline policy that allows creation of the Resource Explorer service-linked role.
+ **Lambda function** (`echo-service`) — A simple example service that echoes back input events.

### Part 3: Assets and triggers (monitoring account, optional)
<a name="part-3-assets-and-triggers-monitoring-account-optional"></a>

This stack creates the following resources:
+ **Skill** (`rds-performance-investigation`) — A skill the agent loads when relevant, created by using the `CfnAsset` construct with an `assetType` of `skill`.
+ **Custom agent** (`rds-firefighter`) — Scopes the agent to a specific workflow with attached skills, created by using the `CfnAsset` construct with an `assetType` of `custom_agent`.
+ **Trigger** (`TIME_BASED`) — Runs the custom agent on a schedule, created by using the `CfnTrigger` construct.

## Setup
<a name="setup"></a>

### Step 1: Clone the sample repository
<a name="step-1-clone-the-sample-repository"></a>

Run the following commands to clone the repository and change to the project directory:

```
git clone https://github.com/aws-samples/sample-aws-devops-agent-cdk.git
cd sample-aws-devops-agent-cdk
```

### Step 2: Install dependencies
<a name="step-2-install-dependencies"></a>

Run the following command to install the project dependencies:

```
npm install
```

## Part 1: Deploy the agent space
<a name="part-1-deploy-the-agent-space"></a>

In this section, you create the agent space, IAM roles, operator app, and an AWS association in your monitoring account.

### Step 1: Configure the monitoring account ID
<a name="step-1-configure-the-monitoring-account-id"></a>

Open `lib/constants.ts` and set your monitoring account ID:

The following example shows the constant to update:

```
export const MONITORING_ACCOUNT_ID = "<YOUR_MONITORING_ACCOUNT_ID>";
```

### Step 2: Bootstrap the AWS CDK environment
<a name="step-2-bootstrap-the-aws-cdk-environment"></a>

If you haven't bootstrapped the AWS CDK in your monitoring account, run the following command:

```
cdk bootstrap aws://<MONITORING_ACCOUNT_ID>/<REGION> --profile monitoring
```

### Step 3: Build and deploy
<a name="step-3-build-and-deploy"></a>

Run the following commands to build the TypeScript code and deploy the stack:

```
npm run build
cdk deploy DevOpsAgentStack --profile monitoring
```

### Step 4: Record the stack outputs
<a name="step-4-record-the-stack-outputs"></a>

After deployment completes, the AWS CDK prints the stack outputs. Record these values for later use.

The following example shows the expected output:

```
Outputs:
DevOpsAgentStack.AgentSpaceArn = arn:aws:aidevops:<REGION>:123456789012:agentspace/abc123
DevOpsAgentStack.AgentSpaceRoleArn = arn:aws:iam::123456789012:role/DevOpsAgentRole-AgentSpace
DevOpsAgentStack.OperatorRoleArn = arn:aws:iam::123456789012:role/DevOpsAgentRole-WebappAdmin
DevOpsAgentStack.AssociationId = assoc-xyz
```

If you plan to complete Part 2, save the `AgentSpaceArn` value. You need it to configure the service account stack.

The stack outputs the agent space ARN, not the agent space ID. Later steps ask for the ID, which is the segment after `agentspace/` in the ARN. In the preceding example, the ARN ends with `agentspace/abc123`, so the agent space ID is `abc123`. Record that value as well.

### Step 5: Verify the deployment
<a name="step-5-verify-the-deployment"></a>

To verify that the agent space was created successfully, run the following AWS CLI command:

```
aws devops-agent get-agent-space \
  --agent-space-id <AGENT_SPACE_ID> \
  --region <REGION>
```

At this point, your agent space is deployed with the operator app enabled and your monitoring account associated. The agent can monitor issues in this account.

## Part 2 (Optional): Add cross-account monitoring
<a name="part-2-optional-add-cross-account-monitoring"></a>

In this section, you extend the setup so that your agent space can monitor resources in a second AWS account (the service account). This involves two actions:

1. Adding a source AWS association in the DevOpsAgentStack that points to the service account.

1. Deploying the ServiceStack into the service account with an IAM role that trusts the agent space.

**Important**  
** You must complete Part 1 before you proceed. The ServiceStack requires the `AgentSpaceArn` from the DevOpsAgentStack deployment output.

### Step 1: Configure the service account ID
<a name="step-1-configure-the-service-account-id"></a>

Open `lib/constants.ts` and set your service account ID:

The following example shows the constant to update:

```
export const SERVICE_ACCOUNT_ID = "<YOUR_SERVICE_ACCOUNT_ID>";
```

The DevOpsAgentStack creates a source AWS association by using this account ID. If you deployed the DevOpsAgentStack before setting this value, redeploy to create the association:

Run the following commands to redeploy:

```
npm run build
cdk deploy DevOpsAgentStack --profile monitoring
```

### Step 2: Set the agent space ARN
<a name="step-2-set-the-agent-space-arn"></a>

Copy the `AgentSpaceArn` value from the DevOpsAgentStack output (Part 1, Step 4) and set it in `lib/constants.ts`:

The following example shows the constant to update:

```
export const AGENT_SPACE_ARN = "arn:aws:aidevops:<REGION>:<MONITORING_ACCOUNT_ID>:agentspace/<SPACE_ID>";
```

The ServiceStack uses this value to scope the trust policy on the secondary account role. The ServiceStack is only synthesized when this value is set.

### Step 3: Bootstrap the service account
<a name="step-3-bootstrap-the-service-account"></a>

If you haven't bootstrapped the AWS CDK in your service account, run the following command:

```
cdk bootstrap aws://<SERVICE_ACCOUNT_ID>/<REGION> --profile service
```

### Step 4: Deploy the ServiceStack
<a name="step-4-deploy-the-servicestack"></a>

Run the following commands to build and deploy the ServiceStack by using credentials for the service account:

```
npm run build
cdk deploy ServiceStack --profile service
```

This creates the following resources in the service account:
+ An IAM role (`DevOpsAgentRole-SecondaryAccount`) that trusts the agent space in the monitoring account
+ An echo Lambda function (`echo-service`) as an example service

### Step 5: Verify the deployment
<a name="step-5-verify-the-deployment"></a>

To confirm that the Lambda function was deployed successfully, run the following commands to test the echo service:

```
aws lambda invoke \
  --function-name echo-service \
  --payload '{"test": "hello world"}' \
  --profile service \
  response.json
cat response.json
```

## Part 3 (Optional): Add a skill, custom agent, and scheduled trigger
<a name="part-3-optional-add-a-skill-custom-agent-and-scheduled-trigger"></a>

In this section, you add three resources to the agent space you created in Part 1. You add a **skill** the agent loads when relevant and a **custom agent** that scopes the agent to a specific workflow. You also add a **scheduled trigger** that runs the custom agent automatically. These resources use the `CfnAsset` and `CfnTrigger` constructs from the `aws-cdk-lib/aws-devopsagent` module.

These resources might incur additional charges to your AWS account. To remove them when you are done, follow the Cleanup section at the end of this guide.

This example uses the `skill` and `custom_agent` asset types. The same `CfnAsset` construct creates every asset type—such as `memory_store`, `agents_md`, and `attachment`. To use a different type, change the `assetType` property and supply the metadata that type requires. For the full list of asset types, their required metadata, and the property reference, see [Managing assets](about-aws-devops-agent-managing-assets.md).

**Important**  
** You must complete Part 1 before you proceed. This stack requires the agent space ID from the DevOpsAgentStack deployment.

### Step 1: Create the content stack
<a name="step-1-create-the-content-stack"></a>

Create a file named `lib/content-stack.ts` with the following contents. A time-based trigger's action references the custom agent by asset ID, in the form `custom:<assetId>`. The stack automatically wires this reference by using the value from the custom agent's `attrAssetId` attribute.

```
import * as cdk from 'aws-cdk-lib';
import { CfnAsset, CfnTrigger } from 'aws-cdk-lib/aws-devopsagent';
import { Construct } from 'constructs';

export interface ContentStackProps extends cdk.StackProps {
  readonly agentSpaceId: string;
}

export class ContentStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props: ContentStackProps) {
    super(scope, id, props);

    // A skill the agent loads when relevant
    const skill = new CfnAsset(this, 'ExampleSkill', {
      agentSpaceId: props.agentSpaceId,
      assetType: 'skill',
      metadata: {
        name: 'rds-performance-investigation',
        description: 'Investigation procedures for RDS performance issues.',
        agent_types: ['GENERIC'],
      },
      files: [
        {
          path: 'SKILL.md',
          contentText: [
            '# RDS Performance Investigation',
            'Use this skill when investigating database latency, connection',
            'errors, or query timeouts.',
          ].join('\n'),
        },
      ],
    });

    // A custom agent with attached skills that a trigger can invoke
    const customAgent = new CfnAsset(this, 'ExampleCustomAgent', {
      agentSpaceId: props.agentSpaceId,
      assetType: 'custom_agent',
      metadata: {
        name: 'rds-firefighter',
        skills: ['rds-performance-investigation'],
      },
      files: [
        {
          path: 'AGENT.md',
          contentText: ['# RDS Firefighter', 'Custom agent for RDS incidents.'].join('\n'),
        },
      ],
    });
    customAgent.node.addDependency(skill);

    // A time-based trigger that runs the custom agent on a schedule
    const dailyTrigger = new CfnTrigger(this, 'DailyTrigger', {
      agentSpaceId: props.agentSpaceId,
      type: 'TIME_BASED',
      condition: {
        schedule: {
          expression: 'rate(1 day)',
        },
      },
      action: {
        actionType: 'create:task',
        task: {
          agent: `custom:${customAgent.attrAssetId}`,
        },
      },
      status: 'Active',
    });

    new cdk.CfnOutput(this, 'SkillAssetId', {
      description: 'The skill asset ID',
      value: skill.attrAssetId,
    });
    new cdk.CfnOutput(this, 'CustomAgentAssetId', {
      description: 'The custom agent asset ID',
      value: customAgent.attrAssetId,
    });
    new cdk.CfnOutput(this, 'TriggerId', {
      description: 'The trigger ID',
      value: dailyTrigger.attrTriggerId,
    });
  }
}
```

### Step 2: Add the stack to your AWS CDK app
<a name="step-2-add-the-stack-to-your-aws-cdk-app"></a>

In your app entry point (for example, `bin/app.ts`), instantiate the stack and pass the agent space ID you recorded in Part 1, Step 4. Use the ID, such as `abc123`, and not the full `AgentSpaceArn` value:

```
new ContentStack(app, 'ContentStack', {
  env: { account: MONITORING_ACCOUNT_ID, region: process.env.CDK_DEFAULT_REGION },
  agentSpaceId: '<AGENT_SPACE_ID>',
});
```

### Step 3: Deploy the stack
<a name="step-3-deploy-the-stack"></a>

Run the following commands to build and deploy the stack by using monitoring account credentials:

```
npm run build
cdk deploy ContentStack --profile monitoring
```

The `agentSpaceId` and `assetType` properties of an asset are create-only, as are the `agentSpaceId`, `type`, `condition`, and `action` properties of a trigger. Changing any of them replaces the resource. You can update the trigger's `status` (`Active` or `Inactive`) in place—set it to `Inactive` to pause the trigger without deleting it. For more information about the other asset types and the full property reference, see [Managing assets](about-aws-devops-agent-managing-assets.md).

### Step 4: Verify the deployment
<a name="step-4-verify-the-deployment"></a>

To confirm that the assets and trigger were created, run the following AWS CLI commands:

```
aws devops-agent list-assets \
  --agent-space-id <AGENT_SPACE_ID> \
  --region <REGION>

aws devops-agent list-triggers \
  --agent-space-id <AGENT_SPACE_ID> \
  --region <REGION>
```

## Troubleshooting
<a name="troubleshooting"></a>

This section describes common issues and how to resolve them.

**`CfnAsset` or `CfnTrigger` is not exported from `aws-cdk-lib/aws-devopsagent`**
+ These constructs require `aws-cdk-lib` version 2.268.0 or later. Run `npm list aws-cdk-lib` to check your version, and run `npm install aws-cdk-lib@latest` to upgrade.

**CloudFormation resource type not found**
+ Verify that you are deploying in a [Supported Regions](about-aws-devops-agent-supported-regions.md).
+ Confirm that your AWS CLI is configured with the appropriate permissions.

**IAM role creation failed**
+ Verify that your deployment role has permissions to create IAM roles.
+ Check that the trust policy conditions match your account ID.

**Cross-account deployment fails with "Could not assume role in target account"**
+ Each stack must be deployed with credentials for the target account. Use the `--profile` flag to specify the correct AWS CLI profile.
+ Verify that the AWS CDK has been bootstrapped in the target account.

**IAM propagation delays**
+ IAM role changes can take a few minutes to propagate. If the agent space creation fails immediately after role creation, wait a few minutes and redeploy.

## Cleanup
<a name="cleanup"></a>

To remove all resources, destroy the stacks in reverse order.

Run the following commands to destroy the stacks:

```
# If you deployed the Part 3 ContentStack, destroy it first
cdk destroy ContentStack --profile monitoring
# If you deployed the ServiceStack, destroy it next
cdk destroy ServiceStack --profile service
# Then destroy the DevOpsAgentStack
cdk destroy DevOpsAgentStack --profile monitoring
```

**Warning:** This action permanently deletes your agent space and all associated data. This action can't be undone. Make sure that you have backed up any important information before you proceed.

## Security considerations
<a name="security-considerations"></a>
+ The AWS CDK application creates IAM roles with trust policies that only allow the `aidevops.amazonaws.com` service principal to assume them.
+ Trust policies include conditions that restrict access to your specific AWS account and agent space ARN.
+ All policies follow the principle of least privilege. Review and customize the IAM policies based on your organization's security requirements.
+ The cross-account role (`DevOpsAgentRole-SecondaryAccount`) uses a fixed name and is scoped to a specific agent space ARN.

## Next steps
<a name="next-steps"></a>

After you have deployed your AWS DevOps Agent by using the AWS CDK:

1. Learn about the full range of DevOps Agent capabilities in the [AWS DevOps Agent User Guide](https://docs.aws.amazon.com/devopsagent/latest/userguide/).

1. Consider integrating the AWS CDK deployment into your CI/CD pipelines for automated infrastructure management.

1. If you register a third-party integration, get its webhook URL and secret by rotating the webhook in the console. The AWS CDK deploys through AWS CloudFormation, which does not return the webhook secret as a stack output. For instructions on managing webhook credentials, see [Managing webhook credentials](configuring-integrations-and-knowledge-invoking-devops-agent-through-webhook.md).

## Additional resources
<a name="additional-resources"></a>
+ [AWS DevOps Agent User Guide](https://docs.aws.amazon.com/devopsagent/latest/userguide/)
+ [Sample CDK repository](https://github.com/aws-samples/sample-aws-devops-agent-cdk) on the GitHub website
+ [CLI onboarding guide](https://docs.aws.amazon.com/devopsagent/latest/userguide/getting-started-with-aws-devops-agent-cli-onboarding-guide.html)
+ [Managing assets](about-aws-devops-agent-managing-assets.md)
+ [AWS CDK DevOps Agent construct library reference](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_devopsagent-readme.html) in the *AWS CDK API Reference*
+ [CfnAsset](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_devopsagent.CfnAsset.html) and [CfnTrigger](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_devopsagent.CfnTrigger.html) construct references in the *AWS CDK API Reference*
+ [AWS DevOps Agent resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/AWS_DevOpsAgent.html) in the *AWS CloudFormation Template Reference*