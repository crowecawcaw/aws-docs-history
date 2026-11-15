

# Generative AI with CID
<a name="generative-ai"></a>

## Ask your dashboards anything
<a name="ask-your-dashboards-anything"></a>

Your Cloud Intelligence Dashboards (CID) already hold the answers: where the money goes, which resources sit idle, which accounts have critical security findings, which applications depend on a single Availability Zone. Finding them means opening several dashboards, picking the right tab and connecting the dots yourself.

With CID agents for Amazon Quick, you ask instead:
+  *"What are my top three savings opportunities this month, and how much would each save?"* 
+  *"Which production databases run in a single Availability Zone?"* 
+  *"Which AWS Health events need our action in the next 30 days?"* 

The agent answers from your own dashboard data, suggests what to do next, and can point you to where to find each number in the dashboards.
+  **Cross-dashboard analysis**: insights correlated across CUDOS, CORA, KPI, Trusted Advisor, AWS Health Events, Graviton Savings and more.
+  **Proactive recommendations**: optimization opportunities, security risks and operational improvements, found before they affect your business.
+  **Faster teams**: FinOps, security and operations teams get answers in minutes instead of searching through dashboards.

### Click to see the demo
<a name="genai-demo"></a>

![CID FinOps Advisor answering cost optimization questions](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/QuickSuite_FinOps_examples.gif)


## What you get
<a name="what-you-get"></a>
+  **Ready-made agents, not a blank page.** Six agents built by the CID team, each with instructions that know the CID dashboards: which tab answers which question, how to combine dashboards and what to prioritize. See the [Agent catalog](genai-agent-catalog.md).
+  **Deployed in one command.** `cid-cmd create-agent` finds the dashboards you have deployed, creates the agent and its Space, and gives you the link. No prompt copying, no manual setup. See [Deploy agents](genai-deploy-agents.md).
+  **Grounded in your data.** Agents answer only from the dashboards and datasets in their Space, with the same access controls as the dashboards.
+  **Kept up to date.** As the CID team improves an agent, `cid-cmd update-agent` brings your agent to the latest version.
+  **Flows and research.** Automate recurring analysis with [Flows](genai-flows.md) and combine dashboard data with external sources in [Research](genai-research.md).

## How it works
<a name="how-it-works"></a>

The building blocks are the same for agents now and for flows later:


|  |  | 
| --- |--- |
|  **Dashboards**  | The CID dashboards you have already deployed, and their datasets. | 
|  **Space**  | A collection of dashboards and datasets on one topic, for example the CID FinOps Space. The Space is the knowledge: an agent or flow can only use what is in its Space. | 
|  **Agent**  | A chat assistant with instructions (persona), starter prompts and a Space. You ask, it analyzes the Space data and answers. | 
|  **Flow**  | A repeatable, multi-step automation over a Space, for example a weekly cost anomaly report. | 

Several agents and flows can share one Space, so users need access to one Space rather than one per agent.

![Architecture of CID with Amazon Quick](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/QuickSuite_architecture.png)


**Note**  
Amazon Quick generative AI features incur additional charges. Review [Amazon Quick pricing](https://aws.amazon.com/quicksight/pricing/) for Author Pro, Reader Pro and the infrastructure fee before you start.

## Get started in three steps
<a name="get-started-in-three-steps"></a>

1. Deploy at least one CID dashboard, for example the [CUDOS Dashboard](cudos-cid-kpi.md#foundational-cudos-dashboard).

1. Pick an agent from the [Agent catalog](genai-agent-catalog.md). Not sure? Start with the CID Operations Advisor.

1. Run `cid-cmd create-agent` and open the link it prints. See [Deploy agents](genai-deploy-agents.md).

## Authors
<a name="authors"></a>
+ Symour Omandac, Senior Technical Account Manager
+ Yuriy Prykhodko, Principal Technical Account Manager
+ Matej Macek, Senior Solutions Architect

## Contributors
<a name="contributors"></a>
+ Pedro Nino, ESL Technical Account Manager
+ Petro Kashlikov, Senior Solutions Architect

## Feedback & Support
<a name="genai-feedback-support"></a>

Follow [Feedback & Support](feedback-support.md) guide

**Note**  
This solution uses generative AI and is a decision-support tool. Validate AI-generated recommendations against your business requirements and AWS best practices. The agents complement, and do not replace, human expertise and judgment.