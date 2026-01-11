# Getting started with AWS DevOps Agent using Terraform

AWS DevOps Agent helps you monitor and manage your AWS infrastructure using AI-powered insights. This guide shows you how to use Terraform to automate the setup and deployment of AWS DevOps Agent resources, providing Infrastructure as Code for your DevOps monitoring solution.

## Overview

This Terraform configuration replicates the AWS DevOps Agent CLI onboarding setup, automating the creation of Agent Spaces, IAM roles, and account associations. Using Terraform provides several advantages:

- **Infrastructure as Code** – Version control your DevOps Agent configuration
- **Reproducible deployments** – Consistent setup across environments
- **Automated provisioning** – Reduce manual configuration errors
- **Cross-account management** – Easily manage multiple AWS accounts

**Note**

AWS DevOps Agent is in preview. The instructions on this page may change before general availability (GA).

## Prerequisites

Before you begin, ensure you have:

- Terraform >= 1.0 installed
- AWS CLI configured with appropriate permissions
- AWS account with administrative access
- AWS DevOps Agent is only available in the `us-east-1` region

### Required IAM permissions

Your AWS credentials must have permissions to create: _IAM roles and policies_ DevOps Agent resources (Agent Spaces, associations) \* Cross-account trust relationships

## Architecture

The Terraform configuration creates the following resources:

### IAM Resources

- **DevOpsAgentRole-AgentSpace** – IAM role for the Agent Space with monitoring permissions
- **DevOpsAgentRole-WebappAdmin** – IAM role for the Operator App interface
- Associated policies and trust relationships for secure access

### DevOps Agent Resources

- **Agent Space** – The main container for your DevOps Agent configuration
- **AWS Account Association** – Links your AWS account for monitoring
- **Operator App** – (Optional) Enables the web-based operator interface
- **External Account Associations** – (Optional) For cross-account monitoring

## Getting started

### Step 1: Clone the repository

```
git clone https://github.com/aws-samples/sample-aws-devops-agent-terraform.git
cd sample-aws-devops-agent-terraform

```

### Step 2: Configure variables

Copy the example variables file and customize it for your environment:

```
cp terraform.tfvars.example terraform.tfvars

```

Edit `terraform.tfvars` with your specific configuration:

```
agent_space_name = "MyCompanyAgentSpace"
agent_space_description = "DevOps monitoring for production workloads"
enable_operator_app = true
auth_flow = "iam"
# external_account_ids = ["123456789012"]  # Optional: for cross-account monitoring

```

### Step 3: Deploy with automation (recommended)

Use the provided deployment script for a streamlined setup:

```
./deploy.sh

```

This script automatically: _Checks prerequisites (Terraform, AWS CLI, credentials)_ Creates `terraform.tfvars` from example if needed _Initializes, validates, plans, and applies Terraform_ Handles IAM propagation delays with retry logic

### Step 4: Complete the setup

Run the post-deployment script to finalize configuration:

```
./post-deploy.sh

```

This script: _Configures AWS DevOps Agent CLI if needed_ Optionally enables the Operator App \* Provides verification commands

## Manual deployment

If you prefer manual control over the deployment process:

### Step 1: Initialize Terraform

```
terraform init

```

### Step 2: Review the plan

```
terraform plan

```

### Step 3: Apply the configuration

```
terraform apply

```

Type `yes` when prompted to confirm the deployment.

## Configuration options

### Input variables

Variable Description Default Required 1`aws_region` AWS region (must be us-east-1) `us-east-1` Yes 2`agent_space_name` Name for the Agent Space `MyAgentSpace` No 3`agent_space_description` Description for the Agent Space `AgentSpace for monitoring my application` No 4`enable_operator_app` Enable the operator web app TRUE No 5`auth_flow` Authentication flow (iam/idc) `iam` No 6`external_account_ids` External AWS accounts to monitor `[]` No 7`tags` Tags for all resources See variables.tf No

### Output values

After deployment, Terraform provides these useful outputs:

- `agent_space_id` – The ID of your Agent Space
- `agent_space_arn` – The ARN of your Agent Space
- `devops_agentspace_role_arn` – ARN of the Agent Space IAM role
- `devops_operator_role_arn` – ARN of the Operator App IAM role
- `manual_setup_instructions` – Next steps and verification commands

## Cross-account monitoring

To monitor resources across multiple AWS accounts, you need to set up cross-account roles.

### Automated setup (recommended)

1. **Deploy the main infrastructure first**: `bash ./deploy.sh ./post-deploy.sh`
2. **Generate cross-account role templates**: `bash ./setup-cross-account-roles.sh`

This script extracts necessary values from your Terraform deployment and generates step-by-step commands for each external account.

1. **Add external account IDs**: Edit `terraform.tfvars` and add: `hcl external_account_ids = ["123456789012", "234567890123"]`
2. **Apply the updated configuration**: `bash terraform apply`

### Manual cross-account setup

For each external AWS account you want to monitor:

1. **Create the trust policy**:

`bash cat > trust-policy.json << EOF { "Version": "2012-10-17" , "Statement": [ { "Effect": "Allow", "Principal": { "AWS": "arn:aws:iam::MONITORING_ACCOUNT_ID:role/DevOpsAgentRole-AgentSpace" }, "Action": "sts:AssumeRole", "Condition": { "StringEquals": { "sts:ExternalId": "arn:aws:aidevops:us-east-1:MONITORING_ACCOUNT_ID:agentspace/AGENT_SPACE_ID" } } } ] } EOF`

1. **Create the cross-account role**:

`bash aws iam create-role \ --role-name DevOpsAgentCrossAccountRole \ --assume-role-policy-document file://trust-policy.json aws iam attach-role-policy \ --role-name DevOpsAgentCrossAccountRole \ --policy-arn arn:aws:iam::aws:policy/AIOpsAssistantPolicy`

1. **Update your Terraform configuration** to include the external account ID in the `external_account_ids` variable.

## Verification

After deployment, verify your setup using the AWS CLI:

### List Agent Spaces

```
aws devopsagent list-agent-spaces \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1

```

### Get Agent Space details

```
aws devopsagent get-agent-space \
  --agent-space-id <AGENT_SPACE_ID> \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1

```

### List associations

```
aws devopsagent list-associations \
  --agent-space-id <AGENT_SPACE_ID> \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1

```

## Accessing AWS DevOps Agent

After successful deployment, you can access AWS DevOps Agent through:

1. **AWS Management Console** – Visit https://console.aws.amazon.com/devopsagent/
2. **AWS CLI** – Use the AWS CLI with the DevOps Agent service model
3. **Operator App** – If enabled, access through the AWS console for interactive investigations

## Troubleshooting

### Common issues

**Region error** : Ensure you're deploying to the `us-east-1` region. AWS DevOps Agent is currently only available in this region.

**Permission errors** : Verify your AWS credentials have the necessary IAM permissions to create roles and policies.

**Role trust issues** : Check that trust policies include the correct account IDs and external IDs.

**IAM propagation delays** : The deployment script includes retry logic for IAM propagation. If deploying manually, wait a few minutes between role creation and usage.

### Getting help

If you encounter issues:

1. Check the Terraform output for error messages
2. Verify your AWS credentials and permissions
3. Ensure you're using the correct region (`us-east-1`)
4. Review the AWS DevOps Agent documentation for service-specific requirements

## Clean up

To remove all resources created by this Terraform configuration:

```
./cleanup.sh

```

Or manually:

```
terraform destroy

```

**Important**

This will permanently delete your Agent Space and all associated configurations. Ensure you have backups of any important data before proceeding.

## Next steps

After setting up AWS DevOps Agent with Terraform:

1. **Configure integrations** – Connect your observability tools, code repositories, and CI/CD pipelines
2. **Set up notifications** – Configure Slack, ServiceNow, or other communication channels
3. **Review topology** – Examine the automatically generated application topology
4. **Test investigations** – Create test incidents to verify the agent's response capabilities

For more information about using AWS DevOps Agent, see the [AWS DevOps Agent User Guide](../userguide.md "../userguide.md").
