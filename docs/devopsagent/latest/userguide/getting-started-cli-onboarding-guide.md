# CLI Onboarding Guide

## Overview

AWS DevOps Agent helps you monitor and manage your AWS infrastructure. This guide walks you through setting up AWS DevOps Agent in the **us-east-1** region.

**Note:** AWS DevOps Agent is in preview. The instructions on this page may change before general availability (GA)

## Prerequisites

- AWS CLI installed and configured
- Authenticated to your AWS monitoring account
- AWS DevOps Agent is available in us-east-1

## Setup AWS CLI for DevOps Agent

### Download the Service Model

Download the AWS DevOps Agent model file:

```
# Download from: https://d1co8nkiwcta1g.cloudfront.net/devopsagent.json
# Save as: devopsagent.json
```

### Patch AWS CLI

Add the DevOps Agent service to your AWS CLI:

```
aws configure add-model --service-model "file://${PWD}/devopsagent.json" --service-name devopsagent
```

Test the installation:

```
aws devopsagent help
```

## IAM Roles Setup

### Create DevOps Agent Space Role

Create the IAM trust policy:

```
cat > devops-agentspace-trust-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "aidevops.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "<ACCOUNT_ID>"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:aidevops:us-east-1:<ACCOUNT_ID>:agentspace/*"
        }
      }
    }
  ]
}
EOF
```

Create the IAM role:

```
aws iam create-role \
  --region us-east-1 \
  --role-name DevOpsAgentRole-AgentSpace \
  --assume-role-policy-document file://devops-agentspace-trust-policy.json

# Save the role ARN
aws iam get-role --role-name DevOpsAgentRole-AgentSpace --query 'Role.Arn' --output text
```

Attach the AWS managed policy:

```
aws iam attach-role-policy \
  --role-name DevOpsAgentRole-AgentSpace \
  --policy-arn arn:aws:iam::aws:policy/AIOpsAssistantPolicy
```

Create and attach additional inline policy:

```
cat > devops-agentspace-inline-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowAwsSupportActions",
      "Effect": "Allow",
      "Action": [
        "support:CreateCase",
        "support:DescribeCases"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Sid": "AllowExpandedAIOpsAssistantPolicy",
      "Effect": "Allow",
      "Action": [
        "aidevops:GetKnowledgeItem",
        "aidevops:ListKnowledgeItems",
        "eks:AccessKubernetesApi",
        "synthetics:GetCanaryRuns",
        "route53:GetHealthCheckStatus",
        "resource-explorer-2:Search"
      ],
      "Resource": [
        "*"
      ]
    }
  ]
}
EOF

aws iam put-role-policy \
  --role-name DevOpsAgentRole-AgentSpace \
  --policy-name AllowExpandedAIOpsAssistantPolicy \
  --policy-document file://devops-agentspace-inline-policy.json
```

### Create Operator App IAM Role

Create the IAM trust policy:

```
cat > devops-operator-trust-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "aidevops.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "<ACCOUNT_ID>"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:aidevops:us-east-1:<ACCOUNT_ID>:agentspace/*"
        }
      }
    }
  ]
}
EOF
```

Create the IAM role:

```
aws iam create-role \
  --role-name DevOpsAgentRole-WebappAdmin \
  --assume-role-policy-document file://devops-operator-trust-policy.json \
  --region us-east-1

# Save the role ARN
aws iam get-role --role-name DevOpsAgentRole-WebappAdmin --query 'Role.Arn' --output text
```

Create and attach the operator app inline policy:

```
cat > devops-operator-inline-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowBasicOperatorActions",
      "Effect": "Allow",
      "Action": [
        "aidevops:GetAgentSpace",
        "aidevops:GetAssociation",
        "aidevops:ListAssociations",
        "aidevops:CreateBacklogTask",
        "aidevops:GetBacklogTask",
        "aidevops:UpdateBacklogTask",
        "aidevops:ListBacklogTasks",
        "aidevops:ListChildExecutions",
        "aidevops:ListJournalRecords",
        "aidevops:DiscoverTopology",
        "aidevops:InvokeAgent",
        "aidevops:ListGoals",
        "aidevops:ListRecommendations",
        "aidevops:ListExecutions",
        "aidevops:GetRecommendation",
        "aidevops:UpdateRecommendation",
        "aidevops:CreateKnowledgeItem",
        "aidevops:ListKnowledgeItems",
        "aidevops:GetKnowledgeItem",
        "aidevops:UpdateKnowledgeItem",
        "aidevops:ListPendingMessages",
        "aidevops:InitiateChatForCase",
        "aidevops:EndChatForCase",
        "aidevops:DescribeSupportLevel",
        "aidevops:SendChatMessage"
      ],
      "Resource": "arn:aws:aidevops:us-east-1:<ACCOUNT_ID>:agentspace/*"
    },
    {
      "Sid": "AllowSupportOperatorActions",
      "Effect": "Allow",
      "Action": [
        "support:DescribeCases",
        "support:InitiateChatForCase",
        "support:DescribeSupportLevel"
      ],
      "Resource": "*"
    }
  ]
}
EOF

aws iam put-role-policy \
  --role-name DevOpsAgentRole-WebappAdmin \
  --policy-name AIDevOpsBasicOperatorActionsPolicy \
  --policy-document file://devops-operator-inline-policy.json
```

## Onboarding Steps

### Create an Agent Space

```
aws devopsagent create-agent-space \
  --name "MyAgentSpace" \
  --description "AgentSpace for monitoring my application" \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1
```

Save the `agentSpaceId` from the response.

To list your agent spaces later:

```
aws devopsagent list-agent-spaces \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1
```

### Associate AWS Account

Associate your AWS account to enable topology discovery. This is the primary source or monitoring account, the account where the agentspace exists.

```
aws devopsagent associate-service \
  --agent-space-id <AGENT_SPACE_ID> \
  --service-id aws \
  --configuration '{
    "aws": {
      "assumableRoleArn": "arn:aws:iam::<ACCOUNT_ID>:role/DevOpsAgentRole-AgentSpace",
      "accountId": "<ACCOUNT_ID>",
      "accountType": "monitor",
      "resources": [
      ]
    }
  }' \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1
```

### Enable Operator App

Authentication flows can use IAM, IDC. Enable the Operator App for your AgentSpace:

```
aws devopsagent enable-operator-app \
  --agent-space-id <AGENT_SPACE_ID> \
  --auth-flow iam \
  --operator-app-role-arn "arn:aws:iam::<ACCOUNT_ID>:role/DevOpsAgentRole-WebappAdmin" \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1
```

###### Note

If you have previously created an Operator App role for another AgentSpace in your account, you can reuse that role ARN.

### (Optional) Associate Additional Source Accounts

For additional accounts that AWS DevOps Agent should monitor, you need to create an IAM cross-account role.

#### Create Cross-Account Role in External Account

Switch to the external account and create the trust policy, the `MONITORING_ACCOUNT_ID` is the main account hosting the agentspace setup in step 2. This allows the monitoring account to assume a role in the secondary source account(s).

```
cat > devops-cross-account-trust-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::<MONITORING_ACCOUNT_ID>:role/DevOpsAgentRole-AgentSpace"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "arn:aws:aidevops:us-east-1:<MONITORING_ACCOUNT_ID>:agentspace/<AGENT_SPACE_ID>"
        }
      }
    }
  ]
}
EOF
```

Create the cross-account IAM role:

```
aws iam create-role \
  --role-name DevOpsAgentCrossAccountRole \
  --assume-role-policy-document file://devops-cross-account-trust-policy.json

# Save the role ARN
aws iam get-role --role-name DevOpsAgentCrossAccountRole --query 'Role.Arn' --output text
```

Attach the AWS managed policy:

```
aws iam attach-role-policy \
  --role-name DevOpsAgentCrossAccountRole \
  --policy-arn arn:aws:iam::aws:policy/AIOpsAssistantPolicy
```

Attach the additional inline policy (json created in step 2):

```
aws iam put-role-policy \
  --role-name DevOpsAgentCrossAccountRole \
  --policy-name AIDevOpsAdditionalPermissions \
  --policy-document file://devops-agentspace-inline-policy.json
```

#### Update Monitoring Account Role

**Switch back to your monitoring account** and add cross-account permissions:

```
cat > devops-cross-account-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Resource": "arn:aws:iam::<EXTERNAL_ACCOUNT_ID>:role/DevOpsAgentCrossAccountRole"
    }
  ]
}
EOF

aws iam put-role-policy \
  --role-name DevOpsAgentRole-AgentSpace \
  --policy-name DevOpsAgentCrossAccountAccess \
  --policy-document file://devops-cross-account-policy.json
```

#### Associate the External Account

```
aws devopsagent associate-service \
  --agent-space-id <AGENT_SPACE_ID> \
  --service-id aws \
  --configuration '{
    "sourceAws": {
      "accountId": "<EXTERNAL_ACCOUNT_ID>",
      "accountType": "source",
      "assumableRoleArn": "arn:aws:iam::<EXTERNAL_ACCOUNT_ID>:role/DevOpsAgentCrossAccountRole",
      "resources": []
    }
  }' \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1
```

### (Optional) Associate GitHub

###### Note

GitHub must first be registered through the AWS DevOps Agent Console UI via OAuth flow before it can be associated via CLI.

List registered services:

```
aws devopsagent list-services \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1
```

Save the `serviceId` for serviceType:"github"

Search for accessible GitHub repositories:

```
aws devopsagent search-service-accessible-resource \
  --service-id <serviceId> \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1
```

Save the `name`, `id`, and extract the `owner` from the `fullName`. The `ownerType` will either be user or organization depending on the type of repo.

After registering GitHub in the UI, associate GitHub repositories:

```
aws devopsagent associate-service \
  --agent-space-id <AGENT_SPACE_ID> \
  --service-id github \
  --configuration '{
    "github": {
      "repoName": "<GITHUB_REPO_NAME>",
      "repoId": "<GITHUB_REPO_ID>",
      "owner": "<GITHUB_OWNER>",
      "ownerType": "organization"
    }
  }' \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1
```

### (Optional) Register and Associate ServiceNow

First, register the ServiceNow service with OAuth credentials:

```
aws devopsagent register-service \
  --service servicenow \
  --service-details  '{
    "servicenow": {
      "instanceUrl": "<SERVICENOW_INSTANCE_URL>",
      "authorizationConfig": {
        "oAuthClientCredentials": {
            "clientName": "<SERVICENOW_CLIENT_NAME>",
            "clientId": "<SERVICENOW_CLIENT_ID>",
            "clientSecret": "<SERVICENOW_CLIENT_SECRET>"
        }
      }
    }
  }' \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1
```

Save the returned `<SERVICE_ID>`, then associate ServiceNow:

```
aws devopsagent associate-service \
  --agent-space-id <AGENT_SPACE_ID> \
  --service-id <SERVICE_ID> \
  --configuration '{
    "servicenow": {
      "instanceUrl": "<SERVICENOW_INSTANCE_URL>"
    }
  }' \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1
```

### (Optional) Register and Associate Dynatrace

First, register the Dynatrace service with OAuth credentials:

```
aws devopsagent register-service \
  --service dynatrace \
  --service-details '{
  "dynatrace": {
    "accountUrn": "<DYNATRACE_ACCOUNT_URN>",
    "authorizationConfig": {
        "oAuthClientCredentials": {
            "clientName": "<DYNATRACE_CLIENT_NAME>",
            "clientId": "<DYNATRACE_CLIENT_ID>",
            "clientSecret": "<DYNATRACE_CLIENT_SECRET>"
        }
      }
    }
  }' \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1
```

Save the returned `<SERVICE_ID>`, then associate Dynatrace (resources are optional), the environment is which specific Dynatrace environment to associate with:

```
aws devopsagent associate-service \
  --agent-space-id <AGENT_SPACE_ID> \
  --service-id <SERVICE_ID> \
  --configuration '{
    "dynatrace": {
      "envId": "<DYNATRACE_ENVIRONMENT_ID>",
      "resources": [
        "<DYNATRACE_RESOURCE_1>",
        "<DYNATRACE_RESOURCE_2>"
      ]
    }
  }' \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1
```

The response will include webhook information for integration, you can trigger an investigation from Dynatrace using this webhook.

### (Optional) Register and Associate Splunk

First, register the Splunk service with OAuth credentials:

The endpoint will look something like: `"endpoint": "https://<XXX>.api.scs.splunk.com/<XXX>/mcp/v1/"`

```
aws devopsagent register-service \
  --service mcpserversplunk \
  --service-details '{
  "mcpserversplunk": {
    "name": "<SPLUNK_NAME>",
    "endpoint": "<SPLUNK_ENDPOINT>",
    "authorizationConfig": {
        "bearerToken": {
            "tokenName": "<SPLUNK_TOKEN_NAME>",
            "tokenValue": "<SPLUNK_TOKEN_VALUE>"
        }
      }
    }
  }' \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1
```

Save the returned `<SERVICE_ID>`, then associate Splunk:

```
aws devopsagent associate-service \
  --agent-space-id <AGENT_SPACE_ID> \
  --service-id <SERVICE_ID> \
  --configuration '{
    "mcpserversplunk":  {
      "name": "<SPLUNK_NAME>",
      "endpoint": "<SPLUNK_ENDPOINT>"
    }
  }' \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1
```

The response will include webhook information for integration, you can trigger an investigation from Splunk using this webhook.

### (Optional) Register and Associate New Relic

First, register the New Relic service with apiKey credentials:

Region: Either "US" or "EU"

Optional fields: `applicationIds`, `entityGuids`, `alertPolicyIds`

```
aws devopsagent register-service \
  --service mcpservernewrelic \
  --service-details '{
    "mcpservernewrelic": {
      "authorizationConfig": {
        "apiKey": {
          "apiKey": "<YOUR_NEW_RELIC_API_KEY>",
          "accountId": "<YOUR_ACCOUNT_ID>",
          "region": "US",
          "applicationIds": ["<APP_ID_1>", "<APP_ID_2>"],
          "entityGuids": ["<ENTITY_GUID_1>"],
          "alertPolicyIds": ["<POLICY_ID_1>"]
        }
      }
    }
  }' \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1
```

Save the returned `<SERVICE_ID>`, then associate New Relic:

```
aws devopsagent associate-service \
  --agent-space-id <AGENT_SPACE_ID> \
  --service-id <SERVICE_ID> \
  --configuration '{
    "mcpservernewrelic":  {
      "accountId": "<YOUR_ACCOUNT_ID>",
      "endpoint": "https://mcp.newrelic.com/mcp/"
    }
  }' \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1
```

The response will include webhook information for integration, you can trigger an investigation from New Relic using this webhook.

### (Optional) Register and Associate Datadog

Datadog must first be registered through the AWS DevOps Agent Console UI via OAuth flow before it can be associated via CLI.

List registered services:

```
aws devopsagent list-services \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1
```

Note the serviceId for serviceType:"mcpserverdatadog"

Save the returned `<SERVICE_ID>`, then associate Datadog:

```
aws devopsagent associate-service \
  --agent-space-id <AGENT_SPACE_ID> \
  --service-id <SERVICE_ID> \
  --configuration '{
    "mcpserverdatadog": {
      "name": "Datadog-MCP-Server",
      "endpoint": "<DATADOG_MCP_ENDPOINT>"
    }
  }' \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1
```

The response will include webhook information for integration, you can trigger an investigation from Datadog using this webhook.

## Verification

Verify your setup:

```
# List your AgentSpaces
aws devopsagent list-agent-spaces \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1

# Get details of a specific AgentSpace
aws devopsagent get-agent-space \
  --agent-space-id <AGENT_SPACE_ID> \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1

# List associations for an AgentSpace
aws devopsagent list-associations \
  --agent-space-id <AGENT_SPACE_ID> \
  --endpoint-url "https://api.prod.cp.aidevops.us-east-1.api.aws" \
  --region us-east-1
```

## Notes

- Replace `<AGENT_SPACE_ID>`, `<ACCOUNT_ID>`, `<STACK_NAME>`, `<TEAM_ID>`, etc. with your actual values
- All commands must be run in us-east-1 region
- When onboarding accounts, we recommend providing CloudFormation stacks to expedite resource indexing
- Alternatively, you can use tag key:value pairs
- If you want to onboard all stacks in an account, leave the resources list empty
