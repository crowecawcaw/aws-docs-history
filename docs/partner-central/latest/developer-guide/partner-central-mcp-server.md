

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Connect AI agents to AWS Partner Central with the MCP Server
<a name="partner-central-mcp-server"></a>

The Partner Central agents MCP Server provides Partner Central tools through the Model Context Protocol (MCP), enabling your AI agents and tools to discover and interact with opportunity management, customer insights, and funding programs through natural language.

The server handles authentication, session management, and human-in-the-loop approval for write operations maintaining control while streamlining workflows.

## Overview
<a name="mcp-server-overview"></a>

The Partner Central agents MCP Server is a fully managed, AWS-hosted service that connects MCP-compatible AI clients to the Partner Central agents. It uses JSON-RPC 2.0 over HTTPS with SigV4 authentication and supports Server-Sent Events (SSE) for real-time streaming responses.

The server supports multi-turn conversations, file attachments for document analysis, and a built-in approval workflow that requires your explicit consent before any write operation executes.

### Agent capabilities
<a name="mcp-agent-capabilities"></a>
+ **Pipeline insights** — Get conversational intelligence about your sales pipeline, including at-risk opportunities, stage progression, and closed-lost analysis
+ **Opportunity creation** — Create new opportunities through natural language conversation, by uploading meeting notes, proposals, or call transcripts, or by cloning an existing opportunity
+ **Opportunity summary** — Generate concise, at-a-glance summaries of any deal covering stage, spend, close date, and more
+ **Sales play generation** — Build customized sales strategies combining opportunity details, industry context, and AWS solution recommendations
+ **Customer profile creation** — Generate company profiles using publicly available information covering industry, business model, geography, and recent developments
+ **Solution recommendation** — Cross-reference your registered solutions against opportunity requirements to find the best match
+ **Funding recommendation** — Evaluate opportunities against available AWS funding programs, estimate amounts, and create fund requests
+ **Next step recommendations** — Get prioritized action plans grounded in AWS co-sell standards and stage progression guidance
+ **Opportunity progression** — Upload supporting documents, extract relevant data, and progress opportunities through pipeline stages
+ **AI-assisted product listing** — Generate high-quality AWS Marketplace product listings from your existing digital assets, score listing strength against AWS Marketplace standards, and receive field-level recommendations to improve discoverability. For more information, see [AI-assisted product listing](https://docs.aws.amazon.com/marketplace/latest/userguide/ai-assisted-product-listing.html) in the *AWS Marketplace Seller Guide*.

## Key benefits
<a name="mcp-key-benefits"></a>
+ **Conversational access to Partner Central** — Ask questions in natural language instead of navigating complex console workflows
+ **More time selling** — Create opportunities through a short conversation instead of completing a multi-step form, which reduces data entry and lets partner sales teams spend more time selling, with the agent recommending improvements so partners submit higher-quality opportunities and improve pipeline hygiene
+ **Human-in-the-loop safety** — All write operations require your explicit approval before execution
+ **Multi-turn conversations** — Refine your queries within a session without repeating context
+ **File analysis** — Attach documents (PDF, DOCX, XLSX, CSV, images) for the agent to analyze alongside your questions
+ **Centralized access management** — Control access through IAM policies with fine-grained permissions
+ **Sandbox testing** — Test workflows in an isolated sandbox environment before touching production data
+ **Streaming responses** — Get feedback via SSE as the agent processes your request

## Usage examples
<a name="mcp-usage-examples"></a>

All AI-generated insights include a Session ID for traceability. Data is isolated to the logged-in partner's own opportunities. All content carries clear disclosure labels and is governed by the [AWS Responsible AI Policy](https://aws.amazon.com/machine-learning/responsible-ai/policy/).

### Opportunity creation
<a name="mcp-opportunity-creation"></a>

The agent creates a new opportunity from a natural language description or an uploaded document (PDF, DOCX, XLSX, TXT). It extracts customer name, project scope, expected close date, and other required fields, enriches customer details from publicly available web data, validates the draft against AWS readiness requirements, and creates the opportunity through the Partner Central Selling API after you approve.
+ "Create an opportunity for Acme Corp — they want to migrate their data warehouse to Redshift, target close date end of Q3, expected $40K monthly AWS spend"
+ "Here are my call notes from yesterday's meeting with GlobalTech — create an opportunity from this transcript"
+ "Use this proposal PDF to create an opportunity for the customer's SAP migration"

### Opportunity cloning
<a name="mcp-opportunity-cloning"></a>

The agent creates a new opportunity from an existing one, merges in the new customer or project details you provide, and validates that at least one differentiating field has changed before submission so duplicates are not rejected by AWS review.
+ "Clone opportunity O1234567890 for a new customer — Globex, same workload, target close date end of Q4"
+ "Create an opportunity like O9876543210 but for the customer's production environment instead of the sandbox"

### Pipeline insights
<a name="mcp-pipeline-insights"></a>

Get conversational intelligence about your sales pipeline. The agent analyzes stage progression, deadlines, stalled deals, and closed-lost patterns to surface what matters most.
+ "Which opportunities need my attention this week?"
+ "How many opportunities are closing next month?"
+ "What are the top reasons we've lost opportunities in the last 6 months?"

### Opportunity summary
<a name="mcp-opportunity-summary"></a>

The agent synthesizes company name, industry, stage, expected monthly AWS spend, target close date, and other key details into a concise summary — no need to scan individual form fields.
+ "Give me a summary of opportunity O1234567890"
+ "What's the current status and key details for the Acme Corp deal?"

### Sales play generation
<a name="mcp-sales-play-generation"></a>

The agent builds a customized sales strategy by combining the opportunity's details, the customer's industry context, and relevant AWS solution recommendations into a ready-to-use sales play.
+ "Generate a sales play for opportunity O1234567890"
+ "What's the best approach to sell cloud migration to this financial services customer?"
+ "Build me a sales strategy for the GlobalTech data analytics deal"

### Customer profile creation
<a name="mcp-customer-profile-creation"></a>

The agent generates a company profile using publicly available information — covering industry classification, business model (B2B/B2C/hybrid), geographic presence, company size, market focus, and recent business developments. Profiles are labeled "Generated with publicly available data and AWS AI insights."
+ "Create a customer profile for Acme Corp"
+ "What do we know about this customer's industry and business model?"
+ "Pull together a company overview for my upcoming meeting with GlobalTech"

### Solution recommendation
<a name="mcp-solution-recommendation"></a>

The agent cross-references your registered solutions against opportunity requirements, showing solution name, description, and whether it's already attached to the opportunity.
+ "Which of our solutions best match opportunity O1234567890?"
+ "Is our data analytics solution already attached to this deal?"
+ "Recommend solutions for a customer looking to migrate their SAP workloads"

### Funding recommendation
<a name="mcp-funding-recommendation"></a>

The agent evaluates each opportunity against available AWS funding programs based on opportunity details and program eligibility criteria. When a match is found, it displays program name, description, and detailed reasoning. You can then estimate funding amounts, create auto-populated fund request drafts, or learn more about programs conversationally. SCA (Strategic Collaboration Agreement) budget availability is surfaced when relevant, and all actions respect IAM permissions.
+ "Am I eligible for any funding programs on opportunity O6789012345?"
+ "Estimate the funding amount for a POC with this customer"
+ "Create a MAP benefit application for this opportunity"

### Next step recommendations
<a name="mcp-next-step-recommendations"></a>

The agent evaluates the opportunity against AWS's stage progression guidance, compares current data against criteria for well-qualified opportunities, and identifies exactly what information you still need to collect. The result is a prioritized action plan grounded in AWS co-sell standards.
+ "What do I need to do next to advance opportunity O1234567890?"
+ "Is this opportunity ready for submission? What fields are missing?"
+ "What are the requirements to move this deal from Prospect to Qualified?"

### Opportunity progression
<a name="mcp-opportunity-progression"></a>

The agent accepts supporting documents (meeting transcripts, call notes, email summaries), extracts relevant information, maps it to opportunity fields, evaluates stage requirements, and updates the opportunity. If gaps remain, it returns a breakdown of satisfied vs. unsatisfied requirements.
+ "Here are my call notes — update opportunity O1234567890 with the relevant details"
+ "I'm attaching the meeting transcript. Progress this opportunity based on what we discussed."
+ "Review this email summary and tell me which opportunity fields it satisfies"

## Agentic experience for partner onboarding
<a name="mcp-onboarding-agent"></a>

The agent automates partner onboarding to Partner Central and provides guided assistance for Marketplace seller setup and PRM compliance — all through natural language.

Agent capabilities:
+ **Partner profile automation** — Scan your website, auto-populate your partner profile, and manage visibility, alliance lead contact, training domains, and account connections
+ **Seller setup guidance** — Step-by-step guidance for Marketplace seller registration including tax forms, banking, compliance (KYC/BAV/SU), ESC catalog, and service-linked roles
+ **PRM compliance guidance** — Assess PRM readiness, retrieve product codes for revenue tagging, and verify subsidiary account connections for consolidated revenue attribution

### Partner profile automation
<a name="mcp-onboarding-profile-automation"></a>

The agent scans your company website to extract and auto-populate your partner profile, then guides you through any remaining gaps. It can update profile fields, change visibility, manage your alliance lead contact, link training certification domains, and handle account connection invitations.
+ "Can you look at my website and fill in my profile?"
+ "Make our profile public so AWS customers can find us"
+ "Update our alliance lead contact to [name] at [email]"
+ "Connect our EMEA subsidiary account"

### Seller setup guidance
<a name="mcp-onboarding-seller-setup"></a>

The agent walks through Marketplace seller registration end-to-end, determining the right tax form based on your country and entity type, explaining banking and disbursement setup by region, and identifying compliance requirements (KYC, Bank Account Verification, Secondary User verification) that apply to you.
+ "I want to start selling on Marketplace — where do I begin?"
+ "What tax form do I need? I'm a company in Germany"
+ "Do I need KYC? I'm selling to customers in France"
+ "How do I set up payments if I'm outside the US?"

### PRM compliance guidance
<a name="mcp-onboarding-prm-compliance"></a>

The agent checks whether your account is PRM-ready — verifying that your account is connected, a listing exists, and your product code is available for tagging. For partners with subsidiary accounts, it verifies that all seller accounts are properly linked for consolidated revenue attribution.
+ "Am I PRM compliant?"
+ "Where do I find my product code for tagging?"
+ "Tell me all the steps I need to perform to be PRM compliant"

## Get started
<a name="mcp-get-started"></a>

Ready to set up the Partner Central agents MCP Server? Head to the [Getting started](https://docs.aws.amazon.com/partner-central/latest/APIReference/mcp-getting-started.html) guide for step-by-step setup instructions.