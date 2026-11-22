

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# AWS Quick

AWS Quick is the AI companion built for work. It connects to your local files and the tools you use every day and builds an understanding of your business over time. By bringing the AWS Partner Central agents into Quick through the [Partner Central agents MCP (Model Context Protocol) Server](https://docs.aws.amazon.com/partner-central/latest/developer-guide/partner-central-mcp-server.html), you pair AWS co-sell and funding capabilities with your own customer context in one place, then apply ready-made AWS Partner skills to move faster. The value grows as you adapt it to your workflow by plugging in your own tools, data, and processes so it reflects how your team runs.

Three layers work together:
+ **AWS Quick** — the agentic workspace where your team works and where your business context lives.
+ **The Partner Central agents** — reached through the Partner Central agents MCP Server, these bring opportunity management, customer insights, and funding capabilities into Quick through natural language.
+ **The AWS Partner skills** — ready-made, customizable workflows that turn the agents' capabilities into repeatable, partner-specific motions.

This page is the business-user home for working with AWS Quick and the Partner Central agents. It links out to the canonical setup and developer documentation rather than restating it, so nothing here goes stale as those pages change.

## Get set up on AWS Quick
<a name="mcp-quick-setup"></a>

Start by getting set up in AWS Quick, on the web or the desktop application. You can install and run skills on both.
+ [AWS Quick on desktop](https://docs.aws.amazon.com/quick/latest/userguide/amazon-quick-desktop.html)
+ [Getting started with the AWS Quick desktop application](https://docs.aws.amazon.com/quick/latest/userguide/getting-started-desktop.html)

After you are set up in Quick, continue to [Connect to the Partner Central agents MCP](#mcp-quick-connect) to connect the Partner Central agents.

## Connect to the Partner Central agents MCP
<a name="mcp-quick-connect"></a>

Connected in AWS Quick, the Partner Central agents turn the co-sell and funding lifecycle into a conversation — draft a high-quality opportunity from a call transcript, ask what's at risk in your pipeline, advance a deal to its next stage, and check which funding programs a deal qualifies for, without leaving your workspace. You make it yours by plugging in your own business context (your tools, data, and processes) so it fits how your team runs. To get there, you make a few setup decisions and complete the steps in the following sections.

Creating the Partner Central Agents MCP Cloud Connector in AWS Quick involves technical steps, but each one rests on a business decision. Make those decisions first.

The full, click-by-click setup (creating the Cloud Connector, choosing OAuth sign-in, publishing it to your team, and installing it on the desktop) lives in the developer documentation:
+ [Getting Started with the Partner Central Agent MCP Server](https://docs.aws.amazon.com/partner-central/latest/developer-guide/mcp-getting-started.html)
+ [Connect AI agents to AWS Partner Central with the MCP Server (capabilities overview)](https://docs.aws.amazon.com/partner-central/latest/developer-guide/partner-central-mcp-server.html)

### Support you might need
<a name="mcp-quick-support"></a>

Creating the Cloud Connector combines technical steps with decisions that carry business implications, so it helps to line up the right support before you begin:
+ **Central IT or AWS Quick support** — for your AWS Quick setup and the Cloud Connector.
+ **IAM administrator** (AWS Identity and Access Management) — to decide what permissions the Cloud Connector (or connectors) should hold for your company.
+ **Additional connectors you might want to add** — this is how you tailor it to your business: plug in your tools, data, and processes so each skill reflects how your team runs. Common sources are CRM, email, messenger, and local files; see [The art of the possible with AWS Quick](#mcp-quick-use-cases) for how they enrich each use case.

### How the Cloud Connector works
<a name="mcp-quick-connector"></a>

A **Cloud Connector** is the link between your AWS Quick workspace and the Partner Central agents. You create it once in Quick, publish it to the people who should use it, and from then on **the Cloud Connector, not each individual, is what reaches the agents**, with the one identity and the permissions it was set up with.

A few things to understand up front:
+ **The Cloud Connector is a shared entity, not a personal login.** A person authorizes the Cloud Connector once through browser-based AWS Sign-In; after that, everyone you publish it to operates through that single shared identity. The Cloud Connector is **not user-aware** — it does not know which individual is typing. (See [Decisions to make before you create the Cloud Connector](#mcp-quick-decisions) for how this shared identity maps to individual use.)
+ **Authorizing it grants no extra permissions.** As the Getting Started guide states, authorizing an agent does not grant it any additional AWS permissions. AWS evaluates every request against your IAM policies, service control policies, resource control policies, and permission boundaries.
+ **You set it up once and publish it.** When you create the Cloud Connector you choose the aliases or the organization you share it with, and who else can own it.
+ **Every change to your pipeline asks first.** Before the agents create or change anything in Partner Central, they show you the action and wait for your approval.

### Decisions to make before you create the Cloud Connector
<a name="mcp-quick-decisions"></a>

Because the Cloud Connector carries one shared identity, the choices you make when you create it reach everyone you publish it to. Make these three decisions first, then bring in the support described earlier to configure them.

**Decision 1: What permissions should the Cloud Connector hold?**  
There are two layers of access, and they do different jobs:
+ **Protocol access** — the ability to *reach* the agents. The Getting Started guide notes the MCP server grants this by default to authenticated AWS identities (for OAuth sign-in you add an Allow for `signin:AuthorizeOAuth2Access` and `signin:CreateOAuth2Token`). On its own, protocol access lets the agent connect but **cannot read or change anything** in your pipeline.
+ **Data access** — what the Cloud Connector can actually *do* with your Partner Central data. As the guide puts it, to perform Partner Central operations such as querying opportunities or managing funding, you must also grant data access permissions. This is the layer that matters for the business, and it comes in two flavors: **read** (list and view) and **write** (create, update, submit).

Decide how much data access the Cloud Connector should hold, then have your IAM administrator apply it. Four common scopes:


| Access scope | What it enables in Quick | 
| --- | --- | 
| Protocol only (no data access) | The agent connects, but can't read or change anything: "show me my pipeline" returns nothing usable. | 
| Read-only | The agent can see and summarize: pipeline insights, opportunity summaries, funding reads. It cannot change anything. Note that read access includes financial details such as opportunity values and funding amounts. | 
| Read \+ opportunity write | Adds drafting, updating, and submitting opportunities (the full create and progress motion). Funding writes stay blocked. | 
| Full access | Everything the agents offer: opportunities, drafting fund requests, Marketplace lookups, onboarding. | 

For the exact permission set behind each scope, see [Getting Started](https://docs.aws.amazon.com/partner-central/latest/developer-guide/mcp-getting-started.html) and the [Configuration Reference](https://docs.aws.amazon.com/partner-central/latest/developer-guide/mcp-configuration-reference.html).

**Important**  
**Read access is account-wide.** In the documented policy model, data-access permissions are granted at the account level: the example policies use `"Resource": "*"` and the documentation shows no per-user or owner-based condition for opportunities. Combined with the fact that the Cloud Connector authenticates as one shared identity, this means a Cloud Connector with **read access can list the account's entire co-sell pipeline** — a request like *show me my pipeline* or a Pipeline Health Check can return the whole company's pipeline, not only the asker's opportunities. Decide Cloud Connector sharing deliberately, and set the data-access scope to the least you need. See [Getting Started](https://docs.aws.amazon.com/partner-central/latest/developer-guide/mcp-getting-started.html) and the [Configuration Reference](https://docs.aws.amazon.com/partner-central/latest/developer-guide/mcp-configuration-reference.html).

**Note**  
**Can I limit the pipeline per user?** The documented permission model lets you control **which actions** a Cloud Connector can take (read-only, opportunity-write, or full) and **who can use a Cloud Connector** (through publishing, or an explicit `Deny` on `partnercentral:InvokeMcp` to block access entirely). You can also configure specific Resource values in your permission set to limit which opportunities a connector can access, though pipeline analysis may still show broader overview data. If different groups need different scopes, create separate Cloud Connectors with different action scopes and publish each to the right group.

**Decision 2: Who should be able to use this Cloud Connector?**  
When you publish it, you choose the aliases or the whole organization it is shared with. Everyone you include shares the Cloud Connector's one identity, and its pipeline visibility (see the preceding note). Decide this deliberately.

**Decision 3: Who should own the Cloud Connector?**  
The Cloud Connector owner is responsible for maintaining the session. When the session expires, the owner must open the connector page in AWS Quick and choose **Sign In** to re-authenticate. If the owner does not re-sign in and another user is prompted instead:
+ If that user has no Partner Central permissions configured for the Cloud Connector, they get an error and cannot use it.
+ If that user does sign in, the Cloud Connector inherits that user's permissions instead of the centrally managed ones, which may not be scoped correctly for the MCP or may be narrower than intended.

Choose an owner who can stay on top of session renewals and understands the connector's intended permission scope. For more information about session duration, see [OAuth sign-in overview](https://docs.aws.amazon.com/signin/latest/userguide/oauth-sign-in-overview.html) in the AWS Sign-In User Guide.

## Find and add the AWS Partner skills
<a name="mcp-quick-skills"></a>

The **AWS Partner skills** are ready-made, persona-based workflows that turn the agents' capabilities into repeatable motions. There are two ways to get them.

### Option A (recommended): Add from the official skills catalog in AWS Quick
<a name="mcp-quick-catalog"></a>

AWS Quick includes an **Official** skills catalog, published by Amazon, that you browse from within the app.

1. In AWS Quick, go to **Customize**, **Skills**, then choose **Browse all** to open the **Add to Quick** catalog, scoped to skills. (See [Customize](https://docs.aws.amazon.com/quick/latest/userguide/customize-desktop.html) and [Skills](https://docs.aws.amazon.com/quick/latest/userguide/skills-desktop.html) in the AWS Quick User Guide.)

1. Choose the **Official** set — the curated, first-party skills published by Amazon, which you can filter by category.

1. Search for `AWS Partner` to find the AWS Partner skills.

1. Choose a skill to preview its description, then add it.

### Option B: Download from the official GitHub catalog
<a name="mcp-quick-github"></a>

The AWS Partner skills are also published in the official Amazon Quick catalog repository on GitHub, which you can download and import:
+ See the [Amazon Quick official catalog](https://github.com/Amazon-Quick/Amazon-Quick-official-catalog) on the GitHub website.

For importing a downloaded skill (from a file or folder), see [Creating a skill](https://docs.aws.amazon.com/quick/latest/userguide/skills-desktop.html) in the AWS Quick User Guide.

### The AWS Partner skills
<a name="mcp-quick-skills-list"></a>

Each skill reaches AWS through the [Partner Central agents MCP Server](https://docs.aws.amazon.com/partner-central/latest/developer-guide/partner-central-mcp-server.html). The **Data access** column shows the minimum scope each skill needs — see the four scopes in [Decisions to make before you create the Cloud Connector](#mcp-quick-decisions).


| Skill | What it does | Data access | 
| --- | --- | --- | 
| AWS Partner High-Quality Co-sell Opportunity Submission | Guides a partner field-by-field to draft or review a co-sell opportunity, scored against Opportunity Quality Score best practices, so the submission is complete before it reaches AWS. | Read \+ create/update opportunities | 
| AWS Partner Deal Progression and Sales Play | Moves one opportunity to its next stage by validating the stage gate, naming the single blocker, and packaging context for a Partner Central agent to author the sales play. | Read \+ update opportunities | 
| AWS Partner Funding Eligibility Check | Determines which AWS funding programs a deal qualifies for by delegating to the funding-recommendation capability, and optionally drafts (never submits) a fund request. | Read \+ draft fund requests | 
| AWS Partner Pipeline Health Check | Delivers a prioritized pipeline health briefing by cross-referencing Partner Central opportunities with the partner's engagement signals. | Read-only | 
| AWS Partner Weekly Digest | Compiles a ranked, read-only digest across funding, opportunities, Marketplace activity, referrals, and compliance on a chosen cadence. | Read-only | 

Every write that any skill performs goes through the agents' built-in approval step. For funding behavior and disclaimers, see the [Funding Agent guide](https://docs.aws.amazon.com/partner-central/latest/getting-started/partner-funding-agent.html); for opportunity scoring and co-sell motions, see [Co-sell engagement](https://docs.aws.amazon.com/partner-central/latest/sales-guide/co-sell-engagement.html).

### Keeping skills current
<a name="mcp-quick-skills-current"></a>

The AWS Partner skills are **official skills, updated centrally.** When you add one from the Official catalog, it enters your list as a reference to the published version and **stays in sync automatically** as Amazon republishes it — you do not have to do anything to stay current.

Be aware of what happens if you **duplicate** a skill: duplicating creates a separate copy that you own and can edit, but that copy is a point-in-time fork with no sync relationship to the original, so **it stops receiving the central updates.** Duplicate only when you genuinely need to customize. For the full owner/viewer and duplicate behavior, see [Skills](https://docs.aws.amazon.com/quick/latest/userguide/skills-desktop.html) in the AWS Quick User Guide.

## The art of the possible with AWS Quick
<a name="mcp-quick-use-cases"></a>

After the Cloud Connector is in place and the skills are added, here is what becomes possible. **Adapt it to your workflow by plugging in your business context (your tools, your data, your processes) so each motion reflects how your team runs.** That is where the value is: the skills work out of the box, and they get powerful when you connect your own sources. For each use case that follows, note what the skill does out of the box and how you tailor it to your business.

Data you use in Quick stays in your environment and your conversations remain private.

The business-context connectors to consider adding (generic categories — use whatever tools your company runs):
+ **CRM** — your sales-pipeline system: customer, revenue, stage, ownership, segmentation.
+ **Email** — the customer's problem, commitments, and next steps in their own words; threads with your Partner Development Manager.
+ **Messenger** — recurring team and deal signals.
+ **Local files** — contracts, SOWs, proposals, meeting notes, and Quarterly Business Review (QBR) templates. (Your Partner Business Plan lives in Partner Central, not as a file you maintain outside the tool.)

### Use case 1: Create a high-quality opportunity
<a name="mcp-quick-usecase-opportunity"></a>

**What the skill does.** The AWS Partner High-Quality Co-sell Opportunity Submission skill guides opportunity creation field by field, validates each field against Opportunity Quality Score best practices, suggests AWS products, and, after you approve, creates the opportunity through the agents. It accepts a natural-language description or an uploaded document. See [Co-sell engagement](https://docs.aws.amazon.com/partner-central/latest/sales-guide/co-sell-engagement.html).

**Tailor it to your business.** Connect **local files** (SOWs and proposals) for services, scope, and quantified outcomes; **CRM** for customer, revenue, and stage; **email** for the customer's problem in their own words.

**Consider.** *Where does your best description of the customer's problem live today — the Statement of Work (SOW), the CRM, or a meeting recording — and which is connected to your workspace?*

### Use case 2: Advance a deal and build the sales play
<a name="mcp-quick-usecase-progression"></a>

**What the skill does.** The AWS Partner Deal Progression and Sales Play skill moves one opportunity to its next stage: it validates the stage gate, names the single blocker, benchmarks against the customer's history, finds people to engage, and packages the context for a Partner Central agent to author the sales play. See [the co-sell agent](https://docs.aws.amazon.com/partner-central/latest/sales-guide/partner-cosell-agent.html).

**Tailor it to your business.** Connect **local files** and **email and messenger** for the next step, the "why now," and evidence of customer commitment; **CRM** for stage and spend to keep both systems aligned.

**Consider.** *When a deal moves forward, where does the proof of that movement land first — and could the skill read it there?*

### Use case 3: Check funding eligibility and draft a fund request
<a name="mcp-quick-usecase-funding"></a>

**What the skill does.** The AWS Partner Funding Eligibility Check skill delegates to the Partner Central funding-recommendation capability: it evaluates an opportunity against available AWS funding programs, estimates amounts, and drafts a fund request — always stopping at a draft for you to review and submit. When a program is tied to a Standard Strategic Collaboration Agreement (SCA), it surfaces SCA budget allocation but does not access the SCA document itself. Recommendations are informational and do not guarantee approval. See the [Funding Agent guide](https://docs.aws.amazon.com/partner-central/latest/getting-started/partner-funding-agent.html).

**Tailor it to your business.** The funding skill recommends against programs *available* to your account, but it does not detect invite-only or nomination-gated programs, or named-list gates such as whether a customer is on a target account list (for example, a T2K list). A **local file** listing the programs you are eligible for and actively leverage — especially the invite-only ones — fills that gap, which matters most for mature partners where those programs carry the highest value. Add **local files** (SOWs) for justification and **CRM** for spend and stage to inform the estimate. Your own finance system remains the record for how you track funding consumption.

**Consider.** *Which funding programs do you use most, do you have an active SCA, and where do you track that funding today?*

### Use case 4: Run a pipeline health check and a recurring business review
<a name="mcp-quick-usecase-review"></a>

**What the skills do.** The AWS Partner Pipeline Health Check skill gives a point-in-time triage — a prioritized read across at-risk opportunities, stage progression, stalled deals, close-date forecasts, and closed-lost patterns. The AWS Partner Weekly Digest delivers a read-only, ranked digest across funding, opportunities, Marketplace activity, referrals, and compliance on a cadence you choose.

**Tailor it to your business.** Out of the box these are a point-in-time read and a recurring digest; by connecting your context they become a recurring, auto-populated quarterly business review: a **local file** QBR template becomes the output format; your **local** SCA or Partner Business Plan supplies the targets; **email** threads with your Partner Development Manager (PDM) verify the data; funding status folds into the same view; **CRM** refines ownership and segmentation.

**Consider.** *Your pipeline health lives in Partner Central — what's in your local QBR template, your SCA or Partner Business Plan goals, and your PDM email threads that we could auto-populate into a standing AWS business review?*

## Where to go next
<a name="mcp-quick-next-steps"></a>

The more of your own tools, data, and processes you connect, the more these skills do for your specific business — that is where the value compounds.
+ **Connect the agents (developer setup):** [Getting Started with the Partner Central Agent MCP Server](https://docs.aws.amazon.com/partner-central/latest/developer-guide/mcp-getting-started.html)
+ **Agent capabilities overview:** [Connect AI agents to AWS Partner Central with the MCP Server](https://docs.aws.amazon.com/partner-central/latest/developer-guide/partner-central-mcp-server.html)
+ **Set up the workspace:** [AWS Quick on desktop](https://docs.aws.amazon.com/quick/latest/userguide/amazon-quick-desktop.html)
+ **Manage skills:** [Skills](https://docs.aws.amazon.com/quick/latest/userguide/skills-desktop.html) and [Customize](https://docs.aws.amazon.com/quick/latest/userguide/customize-desktop.html)
+ **Official skills catalog:** See the [Amazon Quick official catalog](https://github.com/Amazon-Quick/Amazon-Quick-official-catalog) on the GitHub website.