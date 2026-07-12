# Using agents for lead prospecting

AWS Partner Central agents support AI-powered capabilities that generate personalized sales assets for enriched leads. After a lead is enriched with AWS signals, the **Actions** menu on the lead detail page unlocks AI-powered creation of lead overviews, sales plays, call scripts, and outreach emails.

## Prerequisites

- Your account has migrated to AWS Partner Central in the AWS Management Console.
- Your leads have been enriched with AWS signals through the lead enrichment workflow. For more information about the lead enrichment workflow, see [Enriching leads](lead-enrichment.md "lead-enrichment.md").
- Your AWS Identity and Access Management (IAM) user or role must have the following permissions:

  - `partnercentral:List*`
  - `partnercentral:Get*`
  - `aws-marketplace:ListEntities`
  - `aws-marketplace:DescribeEntity`

###### Important

Agent outputs are AI-generated and intended to guide your sales activities. They do not guarantee accuracy or completeness. Verify all AI-generated content before using it in customer engagements.

## How to access agent actions

1. Open the **Leads** page, and then choose the **Enriched lead batches** tab.
2. Choose a completed batch to view its individual enriched leads.
3. Choose a lead to open its detail page with AWS insights, solution match data, and AI-powered actions.
4. Use the **Actions** menu to select the desired AI-generated output.

The following sections describe each available agent action.

### Sales play

The sales play agent generates a sales strategy tailored to the prospect's business needs, AWS engagement signals, and your solution. The sales play includes positioning guidance, objection handling, recommended next steps, and messaging relevant to the prospect and AWS insights.

**Best for:** account planning, pre-call preparation, sales team briefings, and strategic account development.

### Lead overview

The lead overview agent provides a concise summary of the lead, including company context, enrichment insights, and qualification status. The lead overview combines AWS signals and lead data into a brief summary.

**Best for:** quickly briefing team members, pipeline reviews, lead handoffs between reps, and prioritization discussions.

### Call script

The call script agent generates a personalized phone call script with talking points, discovery questions, and messaging relevant to the prospect and AWS insights. The script is structured to guide a productive conversation from introduction through next steps.

**Best for:** outbound prospecting calls and follow-up conversations.

### Outreach email draft

The outreach email agent creates a targeted prospecting email with messaging aligned to the prospect's industry, AWS engagement signals, and your capabilities. The email draft is ready to personalize and send.

**Best for:** initial outreach, re-engagement sequences, and scaling personalized email prospecting.

###### Note

You can run each agent action multiple times on the same lead to produce new versions. Agent outputs are also available through Model Context Protocol (MCP) integration.

## Related resources

- [Enriching leads](lead-enrichment.md "lead-enrichment.md")
- [Agents for opportunity management](partner-cosell-agent.md "partner-cosell-agent.md")
