# Configuring Insights

Insights configuration is how you teach Amazon Connect Decisions what to watch for, how to
interpret what it finds, and how to prioritize what surfaces to your team. Configuration
applies to both demand and supply monitoring. There are four areas to work through in
sequence: Knowledge Sources, Detection (Metrics and Rules), Root Causes and Recommendations
(Guidelines), and Prioritization (Severity). A preview is available at each step so you can
validate before activating any configurations.

To open configuration: From the home page, navigate to **Insights**
in the left-hand navigation, then select **Configuration**.

## The four configuration areas

- **Knowledge Sources:** Share SOPs and documented
  business best practices so Amazon Connect Decisions understands your operational
  context before generating metrics, rules, and guidelines.
- **Detection:** Define the metrics and rules that
  determine when an insight is triggered for demand or supply monitoring.
- **Guidelines:** Shape how root cause analysis and
  recommendations are generated so they align with your business practices.
- **Severity:** Assign financial impact to insight
  types so Amazon Connect Decisions can rank Insights by business priority.

## How configuration connects to Insights output

Each area feeds the Insights experience directly. Detection determines what surfaces;
guidelines shape the analysis and recommended actions; severity determines the order in
which Insights appear. Changes to any area take effect as soon as the relevant items are
set to Ready status.

## Best practices

- **Start with clear monitoring objectives:** Before
  creating metrics and rules, define what supply chain performance issues matter
  most to your operations. This helps you configure focused, actionable monitoring
  rather than generating excessive alerts.
- **Leverage your onboarding teammate:** Use natural
  language to describe monitoring needs rather than attempting to write technical
  specifications. Ask questions like “Can we make this more sensitive to
  A-class products?” or “What does this field do?” Connect
  Decisions agents translate your business requirements into appropriate
  configurations.
- **Preview extensively:** Always preview metric and
  rule changes before activating them. Use the preview function to:

  - Validate that metrics calculate correctly against your data
  - Confirm that rules trigger insights at appropriate thresholds
  - Filter preview results by products and sites to understand impact
    across your supply chain
  - Iterate on configurations until preview results match your operational
    needs

- **Use explainability instead of SQL:** When
  reviewing how metrics and rules operate, use the Explainability tab rather than
  examining SQL queries directly. This helps you understand the logic in plain
  language without technical complexity. When you see something that doesn’t
  match your expectation work with the agent to correct that via explainability.
- **Iterate with draft status:** Take advantage of the
  Draft status to configure and test metrics and rules without impacting production
  insights. Only change status to Ready when you’re confident in the
  configuration.
- **Balance sensitivity:** Set thresholds that catch
  meaningful insights without generating excessive noise. Use preview to find the
  right balance between alert coverage and operational manageability.
- **Start simple, then expand:** Begin with a few key
  metrics and rules for your highest-priority monitoring needs. Once you’re
  comfortable with the configuration workflow, expand to additional monitoring
  areas.
- **Review and refine regularly:** After activating
  metrics and rules, monitor the quality and relevance of generated insights on
  your Planning Intelligence home page. Return to Monitoring Configuration to
  refine settings based on operational experience.
