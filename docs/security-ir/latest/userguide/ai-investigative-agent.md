# AI Investigative Agent

## Overview

The AI-powered investigation agent works alongside customers and AWS Security Incident Response engineers
to expedite security investigations. When a customer creates an AWS-supported case, the agent automatically activates
in parallel with Security Incident Response engineer engagement, reducing resolution time from days to hours.

Security Incident Response cases can be created by customers or proactively by AWS Security Incident Response during customer escalations.
The investigative agent is automatically triggered whenever a new AWS-supported case is created, and all cases can be
managed through the console, API, or Amazon EventBridge integrations.

**Key benefits**

- **Parallel investigation** – The agent works simultaneously with
  responders—providing both AI-powered automation and human expertise.
- **Automated evidence gathering** – Eliminates manual log analysis by
  automatically querying AWS CloudTrail, IAM, Amazon EC2, and Cost Explorer.
- **Natural language interface** – Describe security concerns in plain
  language without needing expertise in AWS log formats.
- **Faster response** – Investigation summaries available within minutes
  in the Investigation tab.
- **Full auditability** – All agent actions are logged in AWS CloudTrail under
  the `AWSServiceRoleForSupport` role.

###### Important

This feature is only available for AWS-supported cases. Self-managed cases do not include AI investigation capabilities.

## How it works

The AI investigation agent follows a structured workflow when analyzing AWS-supported security cases:

**Investigation workflow**

1. **Case creation** – Customer creates an AWS-supported case in the
   Security Incident Response console describing the security concern.
2. **Parallel activation**
   - Security Incident Response engineers engage with the case.
   - Simultaneously, the AI agent begins its investigation workflow.

3. **Contextual questions (optional)** – The agent may ask clarifying
   questions to gather specific details:
   - Affected AWS account IDs
   - Involved IAM principals (users, roles, access keys)
   - Specific resource identifiers (S3 buckets, EC2 instances, ARNs)
   - Timeframe of suspicious activity

4. **Evidence gathering** – The agent automatically queries AWS data sources:
   - _AWS CloudTrail_ – API calls and activities associated with the incident
   - _IAM_ – User and role permissions, policy changes, and new identity creation
   - _Amazon EC2 Instance APIs_ – Information about compute resources if involved
   - _Cost Explorer_ – Cost and usage metrics for unusual resource consumption

5. **Analysis and correlation** – The agent correlates evidence across
   services, identifies patterns, and builds a timeline of events.
6. **Summary generation** – Within minutes, the agent presents a
   comprehensive investigation summary in the Investigation tab.

###### Note

All fields are optional. If no answer is provided within 10 minutes, the investigation starts automatically. In some
cases, if sufficient information is already available, the agent may skip the optional questions entirely.

**Accessing investigation results**

To view the AI analysis:

1. Navigate to your case in the Security Incident Response console.
2. Select the **Investigation** tab.
3. Review the investigation summary with findings, timeline, and context.

The AI investigative agent summary is automatically posted as a comment in the case's Communication section, making it
easy to review alongside other case updates.

**Data access and permissions**

The AI investigation agent uses the `AWSServiceRoleForSupport` Service-Linked Role to access AWS resources.
This role provides read-only permissions necessary for evidence gathering.

All actions performed by the agent are logged in AWS CloudTrail, allowing customers to audit exactly what data was accessed
during the investigation. In AWS CloudTrail logs, these actions are attributed to `AWSServiceRoleForSupport`.

## Prerequisites

Before using the AI-powered investigation capabilities, ensure the following:

**Required setup**

- **AWS Security Incident Response enabled** – The service must be enabled through the
  AWS Organizations management account.
- **AWS-supported case type** – AI investigation is only available
  for AWS-supported cases (not self-managed cases).
- **AWSServiceRoleForSupport** – This service-linked role is
  automatically created and provides necessary permissions for the investigation agent.

**Required permissions**

To create AWS-supported cases and access investigation results, the IAM principal needs the following permissions:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "security-ir:CreateCase",
                "security-ir:GetCase",
                "security-ir:ListCases",
                "security-ir:UpdateCase"
            ],
            "Resource": "*"
        }
    ]
}
```

## Using the investigative agent

The AI investigation agent activates automatically when creating an AWS-supported case.

**To monitor AI investigation progress**

1. Open your case in the AWS Security Incident Response console.
2. Choose the **Investigation** tab.
3. View the investigation status (_In Progress_ or _Completed_).
4. Once completed, review the comprehensive investigation summary with findings, timeline, and recommendations.

**Responsible AI disclosure**

Investigation summaries are generated using AWS Generative AI capabilities. You are responsible for evaluating
AI-generated recommendations in your specific context, implementing appropriate oversight mechanisms, verifying
findings independently, and maintaining human oversight of all security decisions.
