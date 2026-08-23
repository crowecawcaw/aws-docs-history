# How are Insights generated?

Amazon Connect Decisions uses a systematic process to monitor your supply chain data, detect issues, and generate insights with actionable recommendations. Understanding this process helps you configure effective rules and interpret the insights you receive.

## The Insight Generation Process

Insight generation follows a four-stage process that transforms your supply chain data into actionable intelligence:

### 1. Metric Calculation

The system continuously calculates metrics based on your supply chain data. These metrics are quantifiable measurements that assess performance across your operations, such as:

- Projected inventory levels
- Days of supply
- Inventory turns
- Lead time variability
- Forecast accuracy

Metrics are calculated at the granularity you define, such as by product, site, or product-site combination. The system updates these calculations based on the frequency you configure (daily, weekly, or as new data arrives).

### 2. Rule Evaluation

Once metrics are calculated, Amazon Connect Decisions evaluates them against your configured metric-based rules. Metric-based rules define the specific conditions under which you want to be alerted to potential issues.

Each metric-based rule includes three essential components:

**Metrics**: The quantifiable measurements being monitored

**Thresholds**: The boundary values that trigger an insight when crossed

**Scope**: The products, sites, or other dimensions the rule applies to

For example, a rule might state: "Alert when projected inventory falls below safety stock minimum AND days until stockout is 14 or fewer AND customer impact risk exceeds $25,000."

When a rule's conditions are met, the system initiates the insight generation process for the affected items.

### 3. Root Cause Analysis

When a rule is triggered, Amazon Connect Decisions automatically performs root cause analysis to understand why the issue occurred. The system:

- Examines relevant supply chain data across multiple dimensions
- Reviews historical patterns and recent changes
- Analyzes relationships between different factors (demand, supply, inventory, orders)
- Applies your policy-based rules to provide business context

Policy-based rules guide this analysis by providing qualitative guidelines on how the system should consider and analyze problems. For example, a policy-based rule might state: "For inventory shortage insights, always analyze the following root causes: demand forecast error, supplier lead time issues, production capacity constraints."

The root cause analysis identifies the primary drivers behind the issue and provides detailed explanation of contributing factors.

### 4. Insight Creation and Recommendation Generation

After completing the root cause analysis, the system creates the insight with:

- A clear description of the issue
- The root cause explanation
- Relevant metrics and data visualizations
- Priority classification based on your configured prioritization factors
- Recommended actions to resolve the issue
- Alternative actions for consideration

Recommendations are generated based on your business rules, operational constraints, and the specific context of the issue. The system considers factors such as available inventory at other locations, supplier lead times, production capacity, and financial impact when formulating recommendations.

## Timing and Frequency

Insights are generated based on the frequency you configure in your metric-based rules (typically daily or weekly). The system processes new data according to your data refresh schedule, recalculates metrics, evaluates rules, and generates insights for any new issues detected.

Existing insights are automatically updated or marked as complete when new data shows that the issue no longer meets the configured thresholds.
