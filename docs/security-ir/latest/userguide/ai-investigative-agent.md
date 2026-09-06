

# AI Investigative Agent
<a name="ai-investigative-agent"></a>

## Overview
<a name="ai-investigative-agent-overview"></a>

 The AI-powered investigation agent works alongside customers and AWS Security Incident Response engineers to expedite security investigations. When a customer creates an AWS supported case, the agent automatically activates in parallel with Security Incident Response engineer engagement, reducing resolution time from days to hours. 

 During customer escalations, Security Incident Response cases might be created by you or proactively by AWS Security Incident Response. When a new AWS supported case is created, the investigative agent automatically triggers. You can manage all cases through the console, API, or Amazon EventBridge integrations. 

**Key benefits**
+ **Parallel investigation** – The agent works simultaneously with responders—providing both AI-powered automation and human expertise.
+ **Automated evidence gathering** – Eliminates manual log analysis by automatically querying AWS CloudTrail, IAM, Amazon EC2, and Cost Explorer.
+ **Natural language interface** – Describe security concerns in plain language without needing expertise in AWS log formats.
+ **Faster response** – Investigation summaries available within minutes in the Investigation tab.
+ **Full auditability** – All agent actions are logged in AWS CloudTrail under the `AWSServiceRoleForSupport` role.

**Important**  
 This feature is only available for AWS-supported cases. Self-managed cases do not include AI investigation capabilities. 

## How it works
<a name="ai-investigative-agent-how-it-works"></a>

 The AI investigation agent follows a structured workflow when analyzing AWS supported security cases: 

**Investigation workflow**

1. **Case creation** – Customer creates an AWS supported case in the Security Incident Response console describing the security concern.

1. **Parallel activation**
   + Security Incident Response engineers engage with the case.
   + Simultaneously, the AI agent begins its investigation workflow.

1. **Contextual questions (optional)** – The agent may ask clarifying questions to gather specific details:
   + Affected AWS account IDs
   + Involved IAM principals (users, roles, access keys)
   + Specific resource identifiers (S3 buckets, EC2 instances, ARNs)
   + Timeframe of suspicious activity

1. **Evidence gathering** – The agent automatically queries AWS data sources:
   + *AWS CloudTrail* – API calls and activities associated with the incident
   + *IAM* – User and role permissions, policy changes, and new identity creation
   + *Amazon EC2 Instance APIs* – Information about compute resources if involved
   + *Cost Explorer* – Cost and usage metrics for unusual resource consumption

1. **Analysis and correlation** – The agent correlates evidence across services, identifies patterns, and builds a timeline of events.

1. **Summary generation** – Within minutes, the agent presents a comprehensive investigation summary in the Investigation tab.

**Note**  
 All fields are optional. If no answer is provided within 10 minutes, the investigation starts automatically. In some cases, if sufficient information is already available, the agent may skip the optional questions entirely. 

**Accessing investigation results**

To view the AI analysis:

1. Navigate to your case in the Security Incident Response console.

1. Select the **Investigation** tab.

1. Review the investigation summary with findings, timeline, and context.

 The AI investigative agent summary is automatically posted as a comment in the case's **Communication** section, making it easy to review alongside other case updates. 

**Data access and permissions**

 The AI investigation agent uses the `AWSServiceRoleForSupport` Service-Linked Role to access AWS resources. This role provides read-only permissions necessary for evidence gathering. 

 All actions performed by the agent are logged in AWS CloudTrail, allowing customers to audit exactly what data was accessed during the investigation. In AWS CloudTrail logs, these actions are attributed to `AWSServiceRoleForSupport`. 

## Prerequisites
<a name="ai-investigative-agent-prerequisites"></a>

 Before using the AI-powered investigation capabilities, ensure the following: 

**Required setup**
+ **AWS Security Incident Response enabled** – The service must be enabled through the AWS Organizations management account.
+ **AWSsupported case type** – AI investigation is only available for AWS supported cases (not self-managed cases).
+ **AWSServiceRoleForSupport** – This service-linked role is automatically created and provides necessary permissions for the investigation agent.

**Required permissions**

 To create AWS supported cases and access investigation results, the IAM principal needs the following permissions: 

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
<a name="ai-investigative-agent-using"></a>

 The AI investigation agent activates automatically when creating an AWS-supported case. 

**To monitor AI investigation progress**

1. Open your case in the AWS Security Incident Response console.

1. Choose the **Investigation** tab.

1. View the investigation status (*In Progress* or *Completed*).

1. Once completed, review the comprehensive investigation summary with findings, timeline, and recommendations.

**Responsible AI disclosure**

 Investigation summaries are generated using AWS Generative AI capabilities. You are responsible for evaluating AI-generated recommendations in your specific context, implementing appropriate oversight mechanisms, verifying findings independently, and maintaining human oversight of all security decisions. 

**Use of customer data**

 AI Investigative Agent does not use customer data for model training, and it does not share customer data with third parties. 