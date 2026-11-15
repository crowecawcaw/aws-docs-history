

# Agent catalog
<a name="genai-agent-catalog"></a>

## Choose your agent
<a name="choose-your-agent"></a>

Each agent works as soon as one of its dashboards is deployed, and gets better with every additional dashboard. `cid-cmd list-agents` shows which agents are ready for your account.

**Note**  
 **Deploy any agent with one command** in AWS CloudShell, in the account and Region of your CID dashboards:  

```
pip3 install -U cid-cmd
cid-cmd create-agent
```
Pick the agent from the list, or pass its id, for example `--agent-id finops`. For prerequisites and how to update, share or delete agents, see [Deploy agents](genai-deploy-agents.md).


| Agent | Best for | Try asking | Uses | 
| --- | --- | --- | --- | 
|  ** [CID Operations Advisor](#genai-agent-operations) ** (start here) | One assistant for everything in CID | "What are the most critical risks across cost, security and resilience right now?" | Most CID dashboards | 
|  ** [CID FinOps Advisor](#genai-agent-finops) **  | Savings, idle resources, commitments, upcoming fees | "Which three savings opportunities should we act on first, and how much will they save?" | CUDOS, CORA, Graviton Savings, Extended Support, Pricing Change Analysis | 
|  ** [CID Security Advisor](#genai-agent-security) **  | Security findings, compliance, detection coverage | "Which accounts have the most critical findings, and where do we start?" | Trusted Advisor, AWS Config, CUDOS, Health Events, AWS Feeds | 
|  ** [CID Resilience Advisor](#genai-agent-resilience) **  | Single points of failure, recovery targets, maintenance | "Which production workloads depend on a single Availability Zone?" | ResilienceVue, Trusted Advisor, CUDOS, Health Events, AWS Config | 
|  ** [CID Support Cases Analyst](#genai-agent-support) **  | Support case summaries and recurring issues | "Summarize our open high-severity cases and what is blocking them." | Support Cases Radar | 
|  ** [CID Health Events Analyst](#genai-agent-health) **  | AWS Health events that need action soon | "Which scheduled changes and end-of-support deadlines affect us this month?" | Health Events Dashboard | 

**Tip**  
Deploy one agent per team. For example, the FinOps team uses the CID FinOps Advisor and the security team the CID Security Advisor, while leadership uses the CID Operations Advisor for the full picture.

Want to see exactly what an agent knows? Every agent’s instructions and Space are open source in the [CID GitHub repository](https://github.com/aws-solutions-library-samples/cloud-intelligence-dashboards-framework/tree/main/agentic).

## CID Operations Advisor
<a name="genai-agent-operations"></a>

 **For:** leaders, cloud center of excellence teams and anyone who wants one assistant for all of CID.

Ask across domains in one conversation. The advisor connects cost, security, resilience, AWS Health and support data, for example a cost spike with the AWS Health event and support cases behind it.

 **Dashboards:** [CUDOS](cudos-cid-kpi.md#foundational-cudos-dashboard), [KPI](cudos-cid-kpi.md), [CORA](cora-dashboard.md), [Graviton Savings](graviton-savings-dashboard.md), [Extended Support Cost Projection](extended-support.md), [Pricing Change Analysis](pricing-change-dashboard.md), [Trusted Advisor Organizational View](trusted-advisor-dashboard.md), [AWS Config Resource Compliance](config-resource-compliance-dashboard.md), [AWS Feeds](news-feeds.md), [ResilienceVue](resiliencevue-dashboard.md), [Health Events](health-events-dashboard.md), [Support Cases Radar](support-cases-radar.md) 

 **Deploy:** `cid-cmd create-agent --agent-id operations`. See [Deploy agents](genai-deploy-agents.md).

### Click to see the demo
<a name="genai-agent-operations-demo"></a>

![CID Operations Advisor demo](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/QuickSuite_Operations_examples.gif)


## CID FinOps Advisor
<a name="genai-agent-finops"></a>

 **For:** FinOps practitioners, cost owners and finance teams.

Turns cost data into a ranked list of savings with dollar amounts. It knows which CUDOS tab shows idle resources, how to avoid double-counting CORA savings, which Extended Support charges are coming and how much Graviton would save. It also explains why spend changed.

 **Dashboards:** [CUDOS](cudos-cid-kpi.md#foundational-cudos-dashboard) (recommended), [CORA](cora-dashboard.md), [Graviton Savings](graviton-savings-dashboard.md), [Extended Support Cost Projection](extended-support.md), [Pricing Change Analysis](pricing-change-dashboard.md) 

 **Deploy:** `cid-cmd create-agent --agent-id finops`. See [Deploy agents](genai-deploy-agents.md).

### Click to see the demo
<a name="genai-agent-finops-demo"></a>

![CID FinOps Advisor demo](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/QuickSuite_FinOps_examples.gif)


## CID Security Advisor
<a name="genai-agent-security"></a>

 **For:** security and compliance teams.

Prioritizes security findings and non-compliant resources across accounts, finds gaps in detection coverage (for example accounts or Regions without Amazon GuardDuty), and flags security notifications and bulletins that affect you.

 **Dashboards:** [Trusted Advisor Organizational View](trusted-advisor-dashboard.md), [AWS Config Resource Compliance](config-resource-compliance-dashboard.md), [CUDOS](cudos-cid-kpi.md#foundational-cudos-dashboard) (Security tab), [Health Events](health-events-dashboard.md), [AWS Feeds](news-feeds.md) 

 **Deploy:** `cid-cmd create-agent --agent-id security`. See [Deploy agents](genai-deploy-agents.md).

### Click to see the demo
<a name="genai-agent-security-demo"></a>

![CID Security Advisor demo](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/QuickSuite_Security_examples.gif)


## CID Resilience Advisor
<a name="genai-agent-resilience"></a>

 **For:** operations, SRE and architecture teams.

Finds single points of failure and recovery gaps: single-AZ databases and instances, applications that miss their RTO or RPO targets, service limits close to exhaustion, and upcoming maintenance that hits fragile workloads.

 **Dashboards:** [ResilienceVue](resiliencevue-dashboard.md), [Trusted Advisor Organizational View](trusted-advisor-dashboard.md), [CUDOS](cudos-cid-kpi.md#foundational-cudos-dashboard), [Health Events](health-events-dashboard.md), [AWS Config Resource Compliance](config-resource-compliance-dashboard.md) 

 **Deploy:** `cid-cmd create-agent --agent-id resilience`. See [Deploy agents](genai-deploy-agents.md).

### Click to see the demo
<a name="genai-agent-resilience-demo"></a>

![CID Resilience Advisor demo](https://docs.aws.amazon.com/guidance/latest/cloud-intelligence-dashboards/images/QuickSuite_Resilience_examples.gif)


## CID Support Cases Analyst
<a name="genai-agent-support"></a>

 **For:** operations teams, technical account managers and support owners.

Summarizes any support case from its full communication history, and spots patterns: the services and topics you open cases for most, recurring issues and cases that wait on you.

 **Dashboards:** [Support Cases Radar](support-cases-radar.md) 

 **Deploy:** `cid-cmd create-agent --agent-id support`. See [Deploy agents](genai-deploy-agents.md).

## CID Health Events Analyst
<a name="genai-agent-health"></a>

 **For:** operations and platform teams.

Cuts through AWS Health noise. It ranks events by impact and deadline, so you see the open issues that affect your resources, the maintenance and end-of-support deadlines coming up, and which accounts and resources each one touches.

 **Dashboards:** [Health Events](health-events-dashboard.md) 

 **Deploy:** `cid-cmd create-agent --agent-id health`. See [Deploy agents](genai-deploy-agents.md).