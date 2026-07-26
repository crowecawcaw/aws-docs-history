# Getting started with AWS DevOps Agent using Terraform

## Overview

This guide shows you how to use Terraform to create and deploy AWS DevOps Agent resources. The Terraform configuration automates the creation of an agent space, IAM roles, an operator app, and AWS account associations.

The Terraform approach automates the manual steps described in the [CLI onboarding guide](getting-started-with-aws-devops-agent-cli-onboarding-guide.md "getting-started-with-aws-devops-agent-cli-onboarding-guide.md") by defining all required resources as infrastructure as code.

AWS DevOps Agent is available in the following 6 AWS Regions: US East (N. Virginia), US West (Oregon), Asia Pacific (Sydney), Asia Pacific (Tokyo), Europe (Frankfurt), and Europe (Ireland). For more information about supported Regions, see [Supported Regions](about-aws-devops-agent-supported-regions.md "about-aws-devops-agent-supported-regions.md").

## Prerequisites

Before you begin, make sure you have the following:

- Terraform >= 1.0 installed
- AWS CLI installed and configured with appropriate credentials
- One AWS account for the monitoring (primary) account
- (Optional) A second AWS account if you want to set up cross-account monitoring

## What this guide covers

This guide is divided into three parts:

- **Part 1** — Deploy an agent space with an operator app and an AWS association in your monitoring account. After completing this part, the agent can monitor issues in that account.
- **Part 2 (Optional)** — Add a source AWS association for a service account and deploy a cross-account IAM role plus an echo Lambda into that account. This allows the agent space to monitor resources across accounts.
- **Part 3 (Optional)** — Register third-party services (Dynatrace, ServiceNow, Splunk, New Relic, GitLab, PagerDuty) and associate them with the agent space.

## Resources created

### Part 1: Monitoring account

- **IAM role** (`DevOpsAgentRole-AgentSpace-*`) — Assumed by the DevOps Agent service to monitor the account. Includes the `AIDevOpsAgentAccessPolicy` managed policy and an inline policy that allows creation of the Resource Explorer service-linked role. Created only when `existing_agentspace_role_arn` is not set.
- **IAM role** (`DevOpsAgentRole-WebappAdmin-*`) — Operator app role with the `AIDevOpsOperatorAppAccessPolicy` managed policy for agent operations. Created only when `existing_operator_role_arn` is not set.
- **Agent space** (configurable name) — The central agent space, created using the `awscc_devopsagent_agent_space` resource. Includes operator app configuration.
- **Association** (AWS monitor) — Links the monitoring account to the agent space using the `awscc_devopsagent_association` resource.
- **Association** (AWS source) — (Optional) Links the service account to the agent space for cross-account monitoring.

### Part 2: Service account (optional)

- **IAM role** (`DevOpsAgentRole-SecondaryAccount-TF`) — Cross-account role with a fixed name. Trusted by the agent space in the monitoring account. Includes the `AIDevOpsAgentAccessPolicy` managed policy and an inline policy that allows creation of the Resource Explorer service-linked role.
- **Lambda function** (`echo-service-tf`) — A simple example service that echoes back input events.

## Setup

### Step 1: Clone the sample repository

```
git clone https://github.com/aws-samples/sample-aws-devops-agent-terraform.git
cd sample-aws-devops-agent-terraform
```

### Step 2: Configure variables

Copy the example variables file and customize it for your environment:

```
cp terraform.tfvars.example terraform.tfvars
```

Edit `terraform.tfvars` with your agent space name and description:

```
agent_space_name        = "MyCompanyAgentSpace"
agent_space_description = "DevOps Agent Space for monitoring production workloads"
```

## Part 1: Deploy the agent space

In this section, you create the agent space, IAM roles, operator app, and an AWS association in your monitoring account.

### Step 1: Deploy with automation (recommended)

Use the provided deployment script for a streamlined setup:

```
./deploy.sh
```

This script automatically:

- Checks prerequisites (Terraform, AWS CLI, credentials)
- Creates `terraform.tfvars` from example if needed
- Initializes, validates, plans, and applies Terraform

Alternatively, if you prefer manual control:

```
terraform init
terraform plan
terraform apply
```

Type `yes` when prompted to confirm the deployment.

### Step 2: Record the outputs

After deployment completes, Terraform prints the outputs. Record these values for later use:

```
Outputs:
agent_space_id              = "abc123"
agent_space_arn             = "arn:aws:aidevops:<REGION>:<MONITORING_ACCOUNT_ID>:agentspace/abc123"
agent_space_name            = "MyCompanyAgentSpace"
devops_agentspace_role_arn  = "arn:aws:iam::<MONITORING_ACCOUNT_ID>:role/DevOpsAgentRole-AgentSpace-a1b2c3d4"
devops_operator_role_arn    = "arn:aws:iam::<MONITORING_ACCOUNT_ID>:role/DevOpsAgentRole-WebappAdmin-a1b2c3d4"
primary_account_id          = "<MONITORING_ACCOUNT_ID>"
primary_account_association_id = "assoc-xyz"
```

If you plan to complete Part 2, save the `agent_space_arn` value. You will need it to configure the service account resources.

### Step 3: Verify the deployment

Run the post-deployment verification script:

```
./post-deploy.sh
```

Or use the AWS CLI to verify that the agent space was created successfully:

```
aws devops-agent get-agent-space \
  --agent-space-id <AGENT_SPACE_ID> \
  --region <REGION>
```

At this point, your agent space is deployed with the operator app enabled and your monitoring account associated. The agent can monitor issues in this account.

## Part 2 (Optional): Add cross-account monitoring

In this section, you extend the setup so the agent space can monitor resources in a second AWS account (the service account). This involves two actions:

1. Adding a source AWS association that points to the service account.
2. Deploying a cross-account IAM role and an echo Lambda function into the service account.

###### Important

You must complete Part 1 before proceeding. The service account resources require the `agent_space_arn` from the Part 1 deployment output.

### Step 1: Configure the service account ID

In `terraform.tfvars`, set your service account ID:

```
service_account_id = "<YOUR_SERVICE_ACCOUNT_ID>"
```

### Step 2: Set the agent space ARN

Copy the `agent_space_arn` value from the Part 1 output (Step 2) and set it in `terraform.tfvars`:

```
agent_space_arn = "arn:aws:aidevops:<REGION>:<MONITORING_ACCOUNT_ID>:agentspace/<SPACE_ID>"
```

The service account resources use this value to scope the trust policy on the secondary account role. These resources are only created when this value is set.

### Step 3: Configure the `aws.service` provider

In `main.tf`, configure the `aws.service` provider alias with credentials for the service account. You can use either a named profile or an assume role:

Using a profile:

```
provider "aws" {
  alias   = "service"
  region  = var.aws_region
  profile = "your-service-account-profile"
}
```

Or using assume role:

```
provider "aws" {
  alias  = "service"
  region = var.aws_region
  assume_role {
    role_arn = "arn:aws:iam::<SERVICE_ACCOUNT_ID>:role/OrganizationAccountAccessRole"
  }
}
```

### Step 4: Deploy

Apply the updated configuration:

```
terraform apply
```

This creates the following resources in the service account:

- An IAM role (`DevOpsAgentRole-SecondaryAccount-TF`) that trusts the agent space in the monitoring account
- An echo Lambda function (`echo-service-tf`) as an example service

It also creates a source AWS association in the monitoring account that links the service account.

### Step 5: Verify the deployment

Test the echo service to confirm the Lambda function was deployed successfully:

```
aws lambda invoke \
  --function-name echo-service-tf \
  --payload '{"test": "hello world"}' \
  --profile <your-service-account-profile> \
  --region <REGION> \
  response.json
cat response.json
```

## Part 3 (Optional): Register third-party integrations

In this section, you register external services (Dynatrace, ServiceNow, Splunk, New Relic, GitLab, PagerDuty) with the agent space. These integrations enable AWS DevOps Agent to access telemetry, incident data, and source control information during investigations.

Unlike the AWS CDK sample — which requires a separate IntegrationsStack phase and manual wiring of the agent space ID — these resources reference the agent space directly and can be deployed in the same `terraform apply` as Part 1.

### Supported integrations

| Service    | Service type        | Authentication           |
| ---------- | ------------------- | ------------------------ |
| Dynatrace  | `dynatrace`         | OAuth client credentials |
| ServiceNow | `servicenow`        | OAuth client credentials |
| Splunk     | `mcpserversplunk`   | Bearer token             |
| New Relic  | `mcpservernewrelic` | API key                  |
| GitLab     | `gitlab`            | Access token             |
| PagerDuty  | `pagerduty`         | OAuth client credentials |

###### Note

Datadog is not included in the Terraform configuration. Connecting Datadog requires interactive user OAuth authorization (browser login and consent) as described in [Connecting DataDog](connecting-telemetry-sources-connecting-datadog.md "connecting-telemetry-sources-connecting-datadog.md"), which Terraform cannot automate. Register Datadog manually through the Capability Providers page in the console.

### Step 1: Configure integration credentials

Add an `integrations` block to `terraform.tfvars`, populating only the services you want. The following example shows a Dynatrace integration:

```
integrations = {
  dynatrace = {
    account_urn   = "<DYNATRACE_ACCOUNT_URN>"
    client_id     = "<DYNATRACE_CLIENT_ID>"
    client_name   = "<DYNATRACE_CLIENT_NAME>"
    client_secret = "<DYNATRACE_CLIENT_SECRET>"
    env_id        = "<DYNATRACE_ENVIRONMENT_ID>"
    resources     = ["<DYNATRACE_RESOURCE_1>"]
  }
}
```

For the complete shape of each integration, see `terraform.tfvars.example` in the sample repository.

**ServiceNow requirement:** Always set `instance_id` explicitly to the short instance name (for example, `"ven04972"` — not the full `instance_url`). If `instance_id` is omitted, the association falls back to `instance_url`, which the DevOps Agent API rejects with a `400 GeneralServiceException: instanceId '<url>' does not match the registered ServiceNow instance`.

**Security:** The `integrations` variable is marked `sensitive`, so its values are redacted from plan and apply output. Do not commit real credentials to `terraform.tfvars`. For production, source secrets from AWS Secrets Manager or AWS Systems Manager Parameter Store (for example, using `data` sources) rather than plaintext.

### Step 2: Deploy

Apply the configuration:

```
terraform apply
```

This creates a service registration and association for each enabled integration.

### Step 3: Review the outputs

After deployment completes, the integration outputs map each enabled service to its registered IDs:

```
integration_service_ids = {
  "dynatrace" = "service-abc123"
}
integration_association_ids = {
  "dynatrace" = "assoc-xyz789"
}
```

For more information about configuring credentials for each service, see:

- [Connecting Dynatrace](connecting-telemetry-sources-connecting-dynatrace.md "connecting-telemetry-sources-connecting-dynatrace.md")
- [Connecting ServiceNow](connecting-to-ticketing-and-chat-connecting-servicenow.md "connecting-to-ticketing-and-chat-connecting-servicenow.md")
- [Connecting Splunk](connecting-telemetry-sources-connecting-splunk.md "connecting-telemetry-sources-connecting-splunk.md")
- [Connecting New Relic](connecting-telemetry-sources-connecting-new-relic.md "connecting-telemetry-sources-connecting-new-relic.md")
- [Connecting GitLab](connecting-to-cicd-pipelines-connecting-gitlab.md "connecting-to-cicd-pipelines-connecting-gitlab.md")
- [Connecting PagerDuty](connecting-to-ticketing-and-chat-connecting-pagerduty.md "connecting-to-ticketing-and-chat-connecting-pagerduty.md")

## Using existing IAM roles (Optional)

By default, the Terraform configuration creates new IAM roles for the agent space and operator app. If you already have IAM roles with the required policies, you can skip role creation and provide the existing role ARNs instead.

### Requirements

The existing roles must meet the following requirements:

#### Agent space role

- Trust policy allows `aidevops.amazonaws.com` to assume the role with `sts:AssumeRole`
- Has the `AIDevOpsAgentAccessPolicy` managed policy attached
- (Optional) Has an inline policy that allows creation of the Resource Explorer service-linked role

#### Operator app role

- Trust policy allows `aidevops.amazonaws.com` to assume the role with `sts:AssumeRole` and `sts:TagSession`
- Has the `AIDevOpsOperatorAppAccessPolicy` managed policy attached

### Configuration

In `terraform.tfvars`, set one or both role ARNs:

```
existing_agentspace_role_arn = "arn:aws:iam::ACCOUNT_ID:role/YourAgentSpaceRole"
existing_operator_role_arn   = "arn:aws:iam::ACCOUNT_ID:role/YourOperatorRole"
```

When these values are set, the corresponding role resources in `iam.tf` are skipped. This approach is fully backward compatible — existing configurations with empty values (the default) preserve the current role-creation behavior.

## Troubleshooting

**IAM propagation delays**

- The configuration includes a 30-second `time_sleep` between IAM role creation and Agent Space creation. The DevOps Agent service validates the operator role's trust policy during Agent Space creation, and this can fail if IAM hasn't fully propagated. If you still see trust policy errors, wait a minute and run `terraform apply` again — the IAM roles will already exist and the apply will pick up where it left off.

**ServiceNow `instanceId does not match` error**

- Set `instance_id` explicitly in the `service_now` integration block to the short instance name (for example, `"ven04972"`), not the full `instance_url`. See the note in Part 3 above.

**Dynatrace association `status: invalid`**

- If `terraform apply` succeeds but the resulting association reports `status = "invalid"` (visible using `aws devops-agent get-association` or the console), this indicates Dynatrace rejected the OAuth client credentials. Double-check `client_id`, `client_secret`, and `account_urn` against the Dynatrace account, rather than a Terraform configuration issue.

**Permission errors**

- Verify that your AWS credentials have the necessary IAM permissions to create roles and policies.
- Check that the trust policy conditions match your account ID.

**Cross-account deployment fails**

- The `aws.service` provider must be configured with credentials for the service account. Use a named profile or an assume role block.
- Verify that the `agent_space_arn` value matches the ARN from the Part 1 output.

**Terraform resource type not found**

- Verify that you have the `awscc` provider version `~> 1.0` or later. The `awscc_devopsagent_agent_space` and `awscc_devopsagent_association` resources require the AWS Cloud Control provider.

## Cleanup

To remove all resources, destroy in reverse order if you deployed Part 2:

```
./cleanup.sh
```

Or manually:

```
terraform destroy
```

**Warning:** This permanently deletes your agent space and all associated data. Make sure you have backed up any important information before proceeding.

## Security considerations

- The Terraform configuration creates IAM roles with trust policies that only allow the `aidevops.amazonaws.com` service principal to assume them.
- Trust policies include conditions that restrict access to your specific AWS account and agent space ARN.
- All policies follow the principle of least privilege. Review and customize the IAM policies based on your organization's security requirements.
- The cross-account role (`DevOpsAgentRole-SecondaryAccount-TF`) uses a fixed name and is scoped to a specific agent space ARN.

## Next steps

After you have deployed your AWS DevOps Agent using Terraform:

1. Learn about the full range of DevOps Agent capabilities in the [AWS DevOps Agent User Guide](../userguide.md "../userguide.md").
2. Consider integrating the Terraform deployment into your CI/CD pipelines for automated infrastructure management.

## Additional resources

- [AWS DevOps Agent User Guide](../userguide.md "../userguide.md")
- [Sample Terraform repository](https://github.com/aws-samples/sample-aws-devops-agent-terraform "https://github.com/aws-samples/sample-aws-devops-agent-terraform")
- [CLI onboarding guide](getting-started-with-aws-devops-agent-cli-onboarding-guide.md "getting-started-with-aws-devops-agent-cli-onboarding-guide.md")
- [awscc\_devopsagent\_agent\_space](https://registry.terraform.io/providers/hashicorp/awscc/latest/docs/resources/devopsagent_agent_space "https://registry.terraform.io/providers/hashicorp/awscc/latest/docs/resources/devopsagent_agent_space") resource in the _Terraform Registry_
- [awscc\_devopsagent\_association](https://registry.terraform.io/providers/hashicorp/awscc/latest/docs/resources/devopsagent_association "https://registry.terraform.io/providers/hashicorp/awscc/latest/docs/resources/devopsagent_association") resource in the _Terraform Registry_
- [awscc\_devopsagent\_private\_connection](https://registry.terraform.io/providers/hashicorp/awscc/latest/docs/resources/devopsagent_private_connection "https://registry.terraform.io/providers/hashicorp/awscc/latest/docs/resources/devopsagent_private_connection") resource in the _Terraform Registry_
