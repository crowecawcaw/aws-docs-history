

# Getting started with AWS DevOps Agent using AWS CloudFormation
<a name="getting-started-with-aws-devops-agent-getting-started-with-aws-devops-agent-using-aws-cloudformation"></a>

## Overview
<a name="overview"></a>

This guide shows you how to use AWS CloudFormation templates to create and deploy AWS DevOps Agent resources. The templates automate the creation of an agent space, AWS Identity and Access Management (IAM) roles, an operator app, and AWS account associations as infrastructure as code.

The CloudFormation approach automates the manual steps described in the [CLI onboarding guide](https://docs.aws.amazon.com/devopsagent/latest/userguide/getting-started-with-aws-devops-agent-cli-onboarding-guide.html) by defining all required resources in declarative YAML templates.

AWS DevOps Agent is available in multiple AWS Regions. For the full list, see [Supported Regions](about-aws-devops-agent-supported-regions.md).

## Prerequisites
<a name="prerequisites"></a>

Before you begin, make sure that you have the following:
+ AWS Command Line Interface (AWS CLI) installed and configured with the appropriate credentials
+ Permissions to create IAM roles and CloudFormation stacks
+ One AWS account for the monitoring (primary) account
+ (Optional) A second AWS account if you want to set up cross-account monitoring

## What this guide covers
<a name="what-this-guide-covers"></a>

This guide is divided into the following parts:
+ **Part 1** – Deploy an agent space with an operator app and an AWS association in your monitoring account. After you complete this part, the agent can monitor issues in that account.
+ **Part 2 (Optional)** – Deploy a cross-account IAM role into a secondary account and add a source AWS association. This configuration enables the agent space to monitor resources across accounts.
+ **Part 3 (Optional)** – Add a skill, a custom agent, and a scheduled trigger to the agent space, so the agent has custom knowledge and runs a custom agent on a schedule.

## Part 1: Deploy the agent space
<a name="part-1-deploy-the-agent-space"></a>

In this section, you create a CloudFormation template that provisions the agent space, IAM roles, operator app, and an AWS association in your monitoring account.

### Step 1: Create the CloudFormation template
<a name="step-1-create-the-cloudformation-template"></a>

Save the following template as `devops-agent-stack.yaml`:

```
AWSTemplateFormatVersion: '2010-09-09'
Description: AWS DevOps Agent - Agent Space with IAM roles, operator app, and AWS association

Parameters:
  AgentSpaceName:
    Type: String
    Default: MyCloudFormationAgentSpace
    Description: Name for the agent space
  AgentSpaceDescription:
    Type: String
    Default: Agent space deployed with CloudFormation
    Description: Description for the agent space

Resources:
  # IAM role assumed by the DevOps Agent service to monitor the account
  DevOpsAgentSpaceRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: DevOpsAgentRole-AgentSpace
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: aidevops.amazonaws.com
            Action: sts:AssumeRole
            Condition:
              StringEquals:
                aws:SourceAccount: !Ref AWS::AccountId
              ArnLike:
                aws:SourceArn: !Sub arn:aws:aidevops:${AWS::Region}:${AWS::AccountId}:agentspace/*
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/AIDevOpsAgentAccessPolicy
      Policies:
        - PolicyName: AllowCreateServiceLinkedRoles
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Sid: AllowCreateServiceLinkedRoles
                Effect: Allow
                Action:
                  - iam:CreateServiceLinkedRole
                Resource:
                  - !Sub arn:aws:iam::${AWS::AccountId}:role/aws-service-role/resource-explorer-2.amazonaws.com/AWSServiceRoleForResourceExplorer

  # IAM role for the operator app interface
  DevOpsOperatorRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: DevOpsAgentRole-WebappAdmin
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: aidevops.amazonaws.com
            Action:
              - sts:AssumeRole
              - sts:TagSession
            Condition:
              StringEquals:
                aws:SourceAccount: !Ref AWS::AccountId
              ArnLike:
                aws:SourceArn: !Sub arn:aws:aidevops:${AWS::Region}:${AWS::AccountId}:agentspace/*
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/AIDevOpsOperatorAppAccessPolicy

  # The agent space resource
  AgentSpace:
    Type: AWS::DevOpsAgent::AgentSpace
    DependsOn:
      - DevOpsAgentSpaceRole
      - DevOpsOperatorRole
    Properties:
      Name: !Ref AgentSpaceName
      Description: !Ref AgentSpaceDescription
      OperatorApp:
        Iam:
          OperatorAppRoleArn: !GetAtt DevOpsOperatorRole.Arn

  # Association linking the monitoring account to the agent space
  MonitorAssociation:
    Type: AWS::DevOpsAgent::Association
    Properties:
      AgentSpaceId: !GetAtt AgentSpace.AgentSpaceId
      ServiceId: aws
      Configuration:
        Aws:
          AssumableRoleArn: !GetAtt DevOpsAgentSpaceRole.Arn
          AccountId: !Ref AWS::AccountId
          AccountType: monitor

Outputs:
  AgentSpaceId:
    Description: The agent space ID
    Value: !GetAtt AgentSpace.AgentSpaceId
  AgentSpaceArn:
    Description: The agent space ARN
    Value: !GetAtt AgentSpace.Arn
  AgentSpaceRoleArn:
    Description: The agent space IAM role ARN
    Value: !GetAtt DevOpsAgentSpaceRole.Arn
  OperatorRoleArn:
    Description: The operator app IAM role ARN
    Value: !GetAtt DevOpsOperatorRole.Arn
```

### Step 2: Deploy the stack
<a name="step-2-deploy-the-stack"></a>

Run the following command to deploy the stack. Replace `<REGION>` with a [Supported Regions](about-aws-devops-agent-supported-regions.md) (for example, `us-east-1`).

```
aws cloudformation deploy \
  --template-file devops-agent-stack.yaml \
  --stack-name DevOpsAgentStack \
  --capabilities CAPABILITY_NAMED_IAM \
  --region <REGION>
```

### Step 3: Record the stack outputs
<a name="step-3-record-the-stack-outputs"></a>

After deployment completes, run the following command to retrieve the stack outputs. Record these values for later use.

```
aws cloudformation describe-stacks \
  --stack-name DevOpsAgentStack \
  --query 'Stacks[0].Outputs' \
  --region <REGION>
```

The following example shows the expected output:

```
[
  {
    "OutputKey": "AgentSpaceId",
    "OutputValue": "abc123def456"
  },
  {
    "OutputKey": "AgentSpaceArn",
    "OutputValue": "arn:aws:aidevops:<REGION>:<ACCOUNT_ID>:agentspace/abc123def456"
  },
  {
    "OutputKey": "AgentSpaceRoleArn",
    "OutputValue": "arn:aws:iam::<ACCOUNT_ID>:role/DevOpsAgentRole-AgentSpace"
  },
  {
    "OutputKey": "OperatorRoleArn",
    "OutputValue": "arn:aws:iam::<ACCOUNT_ID>:role/DevOpsAgentRole-WebappAdmin"
  }
]
```

If you plan to complete Part 2, save the `AgentSpaceArn` value. You need it to configure the cross-account role.

### Step 4: Verify the deployment
<a name="step-4-verify-the-deployment"></a>

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

1. Deploying an IAM role in the service account that trusts the agent space.

1. Adding a source AWS association in the monitoring account that points to the service account.

You must complete Part 1 before you proceed. The service account template requires the `AgentSpaceArn` from the Part 1 stack outputs.

### Step 1: Create the service account template
<a name="step-1-create-the-service-account-template"></a>

Save the following template as `devops-agent-service-account.yaml`. This template creates a cross-account IAM role in the secondary account.

```
AWSTemplateFormatVersion: '2010-09-09'
Description: AWS DevOps Agent - Cross-account IAM role for secondary account monitoring

Parameters:
  MonitoringAccountId:
    Type: String
    Description: The 12-digit AWS account ID of the monitoring account
  AgentSpaceArn:
    Type: String
    Description: The ARN of the agent space from the monitoring account

Resources:
  # Cross-account IAM role trusted by the agent space
  DevOpsSecondaryAccountRole:
    Type: AWS::IAM::Role
    Properties:
      RoleName: DevOpsAgentRole-SecondaryAccount
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: aidevops.amazonaws.com
            Action: sts:AssumeRole
            Condition:
              StringEquals:
                aws:SourceAccount: !Ref MonitoringAccountId
              ArnLike:
                aws:SourceArn: !Ref AgentSpaceArn
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/AIDevOpsAgentAccessPolicy
      Policies:
        - PolicyName: AllowCreateServiceLinkedRoles
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Sid: AllowCreateServiceLinkedRoles
                Effect: Allow
                Action:
                  - iam:CreateServiceLinkedRole
                Resource:
                  - !Sub arn:aws:iam::${AWS::AccountId}:role/aws-service-role/resource-explorer-2.amazonaws.com/AWSServiceRoleForResourceExplorer

Outputs:
  SecondaryAccountRoleArn:
    Description: The cross-account IAM role ARN
    Value: !GetAtt DevOpsSecondaryAccountRole.Arn
```

### Step 2: Deploy the service account stack
<a name="step-2-deploy-the-service-account-stack"></a>

Using credentials for the service account, run the following command:

```
aws cloudformation deploy \
  --template-file devops-agent-service-account.yaml \
  --stack-name DevOpsAgentServiceAccountStack \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides \
    MonitoringAccountId=<MONITORING_ACCOUNT_ID> \
    AgentSpaceArn=<AGENT_SPACE_ARN> \
  --region <REGION>
```

### Step 3: Add the source AWS association
<a name="step-3-add-the-source-aws-association"></a>

Switch back to the monitoring account and create a source AWS association. You can do this by creating a separate stack or by updating the original template. The following example uses a standalone template.

Save the following template as `devops-agent-source-association.yaml`:

```
AWSTemplateFormatVersion: '2010-09-09'
Description: AWS DevOps Agent - Source AWS association for cross-account monitoring

Parameters:
  AgentSpaceId:
    Type: String
    Description: The agent space ID from the monitoring account stack
  ServiceAccountId:
    Type: String
    Description: The 12-digit AWS account ID of the service account
  ServiceAccountRoleArn:
    Type: String
    Description: The ARN of the DevOpsAgentRole-SecondaryAccount role in the service account

Resources:
  SourceAssociation:
    Type: AWS::DevOpsAgent::Association
    Properties:
      AgentSpaceId: !Ref AgentSpaceId
      ServiceId: aws
      Configuration:
        SourceAws:
          AccountId: !Ref ServiceAccountId
          AccountType: source
          AssumableRoleArn: !Ref ServiceAccountRoleArn

Outputs:
  SourceAssociationId:
    Description: The source association ID
    Value: !Ref SourceAssociation
```

Deploy the association stack using monitoring account credentials:

```
aws cloudformation deploy \
  --template-file devops-agent-source-association.yaml \
  --stack-name DevOpsAgentSourceAssociationStack \
  --parameter-overrides \
    AgentSpaceId=<AGENT_SPACE_ID> \
    ServiceAccountId=<SERVICE_ACCOUNT_ID> \
    ServiceAccountRoleArn=arn:aws:iam::<SERVICE_ACCOUNT_ID>:role/DevOpsAgentRole-SecondaryAccount \
  --region <REGION>
```

## Part 3: Add a skill, custom agent, and scheduled trigger
<a name="part-3-add-a-skill-custom-agent-and-scheduled-trigger"></a>

This part is optional. In this section, you add four resources to the agent space you created in Part 1: a **skill** the agent loads when relevant, a **memory store** that holds operational context, a **custom agent** that scopes the agent to a specific workflow, and a **scheduled trigger** that runs the custom agent automatically. These resources use the `AWS::DevOpsAgent::Asset` and `AWS::DevOpsAgent::Trigger` resource types. For more information about managing assets as infrastructure as code, see [Managing assets](about-aws-devops-agent-managing-assets.md).

You must complete Part 1 before you proceed. This template requires the `AgentSpaceId` from the Part 1 stack outputs.

### Step 1: Create the template
<a name="step-1-create-the-template"></a>

Save the following template as `devops-agent-content.yaml`. A time-based trigger's action references the custom agent by asset ID, in the form `custom:<assetId>`. The template wires this automatically with `Fn::GetAtt`.

```
AWSTemplateFormatVersion: '2010-09-09'
Description: AWS DevOps Agent - Example skill, memory store, custom agent, and scheduled trigger

Parameters:
  AgentSpaceId:
    Type: String
    Description: The agent space ID from the Part 1 stack outputs

Resources:
  # A skill the agent loads when relevant
  ExampleSkill:
    Type: AWS::DevOpsAgent::Asset
    Properties:
      AgentSpaceId: !Ref AgentSpaceId
      AssetType: skill
      Metadata:
        name: rds-performance-investigation
        description: Investigation procedures for RDS performance issues.
        agent_types:
          - GENERIC
      Files:
        - Path: SKILL.md
          ContentText: |
            # RDS Performance Investigation
            Use this skill when investigating database latency, connection
            errors, or query timeouts.

  # A memory store that holds operational context
  ExampleMemoryStore:
    Type: AWS::DevOpsAgent::Asset
    Properties:
      AgentSpaceId: !Ref AgentSpaceId
      AssetType: memory_store
      Metadata:
        name: payments-runbook
        description: Standing guidance and known issues for the payments service.
        agent_types:
          - GENERIC
      Files:
        - Path: README.md
          ContentText: |
            Operational memories for the payments service.

  # A custom agent with attached memory stores that a trigger can invoke
  ExampleCustomAgent:
    Type: AWS::DevOpsAgent::Asset
    DependsOn: ExampleMemoryStore
    Properties:
      AgentSpaceId: !Ref AgentSpaceId
      AssetType: custom_agent
      Metadata:
        name: rds-firefighter
        skills:
          - rds-performance-investigation
        memory_stores:
          - payments-runbook
      Files:
        - Path: AGENT.md
          ContentText: |
            # RDS Firefighter
            Custom agent for RDS incidents.

  # A time-based trigger that runs the custom agent on a schedule
  DailyTrigger:
    Type: AWS::DevOpsAgent::Trigger
    Properties:
      AgentSpaceId: !Ref AgentSpaceId
      Type: TIME_BASED
      Condition:
        Schedule:
          Expression: rate(1 day)
      Action:
        actionType: create:task
        task:
          agent: !Sub
            - custom:${AssetId}
            - AssetId: !GetAtt ExampleCustomAgent.AssetId
      Status: Active

Outputs:
  SkillAssetId:
    Description: The skill asset ID
    Value: !GetAtt ExampleSkill.AssetId
  MemoryStoreAssetId:
    Description: The memory store asset ID
    Value: !GetAtt ExampleMemoryStore.AssetId
  CustomAgentAssetId:
    Description: The custom agent asset ID
    Value: !GetAtt ExampleCustomAgent.AssetId
  TriggerId:
    Description: The trigger ID
    Value: !GetAtt DailyTrigger.TriggerId
```

### Step 2: Deploy the stack
<a name="step-2-deploy-the-stack"></a>

Using monitoring account credentials, run the following command. Replace `<AGENT_SPACE_ID>` with the value from the Part 1 outputs.

```
aws cloudformation deploy \
  --template-file devops-agent-content.yaml \
  --stack-name DevOpsAgentContentStack \
  --parameter-overrides AgentSpaceId=<AGENT_SPACE_ID> \
  --region <REGION>
```

The `AgentSpaceId`, `Type`, `Condition`, and `Action` properties are create-only. Changing any of them replaces the resource. You can update the trigger's `Status` (`Active` or `Inactive`) in place—set it to `Inactive` to pause the trigger without deleting it. For more information about the other asset types and the full property reference, see [Managing assets](about-aws-devops-agent-managing-assets.md).

## Verification
<a name="verification"></a>

Verify your setup by running the following AWS CLI commands:

```
# List your agent spaces
aws devops-agent list-agent-spaces \
  --region <REGION>

# Get details of a specific agent space
aws devops-agent get-agent-space \
  --agent-space-id <AGENT_SPACE_ID> \
  --region <REGION>

# List associations for an agent space
aws devops-agent list-associations \
  --agent-space-id <AGENT_SPACE_ID> \
  --region <REGION>
```

## Troubleshooting
<a name="troubleshooting"></a>

This section describes common issues and how to resolve them.

**CloudFormation resource type not found**
+ Verify that you are deploying in a [Supported Regions](about-aws-devops-agent-supported-regions.md).
+ Confirm that your AWS CLI is configured with the appropriate permissions.

**IAM role creation failed**
+ Verify that your deployment credentials have permissions to create IAM roles with custom names (`CAPABILITY_NAMED_IAM`).
+ Check that the trust policy conditions match your account ID.

**Cross-account deployment fails**
+ Each stack must be deployed with credentials for the target account. Use the `--profile` flag to specify the correct AWS CLI profile.
+ Verify that the `AgentSpaceArn` parameter matches the exact ARN from the Part 1 stack outputs.

**IAM propagation delays**
+ IAM role changes can take a few minutes to propagate. If the agent space creation fails immediately after role creation, wait a few minutes and redeploy.

## Cleanup
<a name="cleanup"></a>

To remove all resources, delete the stacks in reverse order.

**Warning:** This action permanently deletes your agent space and all associated data. This action can't be undone. Make sure that you have backed up any important information before you proceed.

Run the following commands to delete the stacks:

```
# If you deployed the Part 3 content stack, delete it first
aws cloudformation delete-stack \
  --stack-name DevOpsAgentContentStack \
  --region <REGION>

aws cloudformation wait stack-delete-complete \
  --stack-name DevOpsAgentContentStack \
  --region <REGION>

# If you deployed the source association stack, delete it next
aws cloudformation delete-stack \
  --stack-name DevOpsAgentSourceAssociationStack \
  --region <REGION>

aws cloudformation wait stack-delete-complete \
  --stack-name DevOpsAgentSourceAssociationStack \
  --region <REGION>

# If you deployed the service account stack, delete it next (using service account credentials)
aws cloudformation delete-stack \
  --stack-name DevOpsAgentServiceAccountStack \
  --region <REGION>

aws cloudformation wait stack-delete-complete \
  --stack-name DevOpsAgentServiceAccountStack \
  --region <REGION>

# Delete the main stack last
aws cloudformation delete-stack \
  --stack-name DevOpsAgentStack \
  --region <REGION>
```

## Next steps
<a name="next-steps"></a>

After you have deployed your AWS DevOps Agent by using AWS CloudFormation:
+ To connect additional integrations, see [Configuring integrations and knowledge](configuring-integrations-and-knowledge.md).
+ If you register a third-party integration, get its webhook URL and secret by rotating the webhook in the console. AWS CloudFormation does not return the webhook secret as a stack output, because it is sensitive. For instructions on managing webhook credentials, see [Managing webhook credentials](configuring-integrations-and-knowledge-invoking-devops-agent-through-webhook.md).
+ To learn about agent skills and capabilities, see [DevOps Agent Skills](about-aws-devops-agent-devops-agent-skills.md).
+ For more information about managing skills, custom agents, and other assets as infrastructure as code, see [Managing assets](about-aws-devops-agent-managing-assets.md).
+ To understand the operator web app, see [What is a DevOps Agent Web App?](about-aws-devops-agent-what-is-a-devops-agent-web-app.md).
+ For detailed property references for the CloudFormation resource types used in this guide, see [AWS DevOps Agent resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/AWS_DevOpsAgent.html) in the *AWS CloudFormation Template Reference*.