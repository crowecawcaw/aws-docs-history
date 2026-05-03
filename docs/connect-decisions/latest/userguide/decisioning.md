# Decisioning

Amazon Connect Decisions continuously monitors your supply chain to detect issues that
require attention and generate actionable recommendations to resolve them. The Decisioning
section of this guide covers everything you need to get the system working effectively —
from teaching it what to watch for, to reviewing and acting on the insights it surfaces.

## What are Insights?

Insights are the primary output of Amazon Connect Decisions. Each insight represents a
detected supply chain issue, paired with root cause analysis and recommended actions to
resolve it. Insights are generated when your configured monitoring rules detect that a
metric has crossed a defined threshold — for example, when projected inventory falls
below safety stock minimums, or when days of supply drop below an acceptable level.

Each insight includes:

- A description of the detected issue and its business context
- Root cause analysis explaining why the issue occurred
- Recommended actions with specific parameters such as quantities, locations,
  and timelines
- Financial impact to help you prioritize your response (if data provided by
  the admin)
- Related insights that may share the same underlying cause

Insights cover both demand and supply monitoring. They are ranked by severity based on
financial impact, so your team can focus on the issues that matter most to your
operations.

## How Decisioning Works

Decisioning operates in two phases that work together: configuration and management.

**Configuration** is how you teach Amazon Connect Decisions
what to monitor, how to interpret what it finds, and how to prioritize what surfaces to
your team. You define the metrics and rules that trigger insights, provide guidelines
that shape root cause analysis and recommendations, and assign financial impact factors
that determine severity ranking. Configuration is completed once during setup and refined
over time as your operational needs evolve.

**Managing Insights** is the day-to-day experience of
reviewing, filtering, and acting on the insights the system generates. Once configuration
is in place, your team uses the Insights page to find relevant issues, understand their
root causes, and execute or dismiss the recommended actions.

## What You'll Find in This Section

**Configuring Insights**

- **How are Insights Generated**: Understand the
  four-stage process that transforms your supply chain data and configuration into
  actionable insights
- **Knowledge Sources**: Share SOPs and documented
  business best practices so Amazon Connect Decisions understands your operational
  context before generating metrics, rules, and guidelines
- **Detection**: Define the metrics and rules that
  determine when an insight is triggered for demand or supply monitoring
- **Guidelines for Root Causes and Recommendations**:
  Shape how root cause analysis and recommendations are generated so they align
  with your business practices and operational constraints
- **Prioritization and Severity**: Assign financial
  impact to insight types so Amazon Connect Decisions can rank insights by business
  priority

**Managing Insights**

- **Filtering and Sorting Insights**: Navigate the
  Insights page, apply filters by product hierarchy, site, severity, and custom
  segments, and sort by impact or urgency to focus on what matters most
- **Understanding Insights Details**: Review root
  cause analysis, key metrics, recommendations, and related insights for a specific
  insight
- **Taking Action on Recommendations**: Accept,
  discard, or mark recommendations as complete, and track the progress of
  resolution activities
- **Providing Feedback on Insights**: Rate the
  quality of insights and recommendations to help the system improve over time
