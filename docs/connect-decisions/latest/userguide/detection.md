

# Detection (Metrics and Rules)
<a name="detection"></a>

Detection configuration defines what Amazon Connect Decisions measures and when those measurements become actionable Insights for both demand and supply monitoring. It has two components that work together:
+ **Metrics:** Quantifiable calculations Amazon Connect Decisions runs against your supply chain data; for example, forecast accuracy over the last four weeks for A-class products, or inventory days of supply by site. Metrics can function as standalone KPIs or serve as inputs into rules.
+ **Rules:** Conditions that trigger an Insight by referencing one or more metrics and firing when thresholds are met; for example, a rule that triggers when forecast accuracy drops below 85% or when days of supply falls below the reorder threshold.

Metrics provide the measurement; rules determine when that measurement becomes something your team should act on.

## Configuring Metrics
<a name="detection-configuring-metrics"></a>

The Insights configuration tab displays your configured metrics and rules alongside a preview of the insights they generate under the Detection tab. This unified view allows you to see both your monitoring configurations and their operational impact in one place.

From this page, you can:
+ View all configured metrics and rules for both demand and supply monitoring
+ Edit individual metrics or rules
+ Review the overall insights that would be generated with your current configurations

### Creating a New Metric
<a name="detection-creating-a-new-metric"></a>

To create a new metric, you can either:
+ **Use Natural Language:** Ask the onboarding agent to create a metric for you. For example: "Create a metric to track forecast accuracy for A-class products over the last 4 weeks." The agent translates your requirements into a metric configuration.
+ **Use the Create Metric Button:** Click "Add metrics" to open the metric creation interface and define parameters directly.

When you create or edit a metric, the system saves it with a "Draft" status. This allows you to configure and test the metric without impacting production insights.

### Reviewing an Existing Metric
<a name="detection-reviewing-an-existing-metric"></a>

When you click on a metric, you arrive at the metric review page where you can:
+ **Review the configuration:** See the current setup of your metric, including its descriptors, dimension grain, time span, and other parameters.
+ **Ask questions with natural language:** Work with the onboarding teammate to understand and refine your metric. Ask questions like:
  + "How does this metric work?"
  + "Can we confine this to only A-class products?"
  + The agent helps you iterate on the metric definition conversationally, translating your business requirements into the appropriate configuration.
+ **Review explainability:** Instead of reviewing SQL queries directly, view the Explainability section that describes how the metric operates in plain language. To do so,
  + Un-collapse "SQL Query" section
  + Click on "Explainability" tab
+ **Preview individual metric impact:** Use the metric preview to see how the metric would be generated at runtime with your current configuration. Filter the preview by specific products and sites to understand how the metric will impact different parts of your supply chain. To do so:
  + Expand the "Metric Preview" element at the bottom of the screen.
  + Click "Preview metric" to generate runtime metrics.
  + Refine your preview with search criteria across products and sites.
+ **Iterate with preview:** As you work with the onboarding agent to refine the metric, use preview to validate changes. Continue iterating until the preview results match your operational needs, then save your configuration.

**Edit fields directly (optional):** If you prefer to configure the metric yourself, click "Edit" to change fields directly without agent support. Even when editing manually, you can still ask the onboarding teammate questions like:
+ "What does this field do?"
+ "Can you help me edit my forecast accuracy SQL?"
+ "How should I set the temporal grain for weekly reporting?"

Your onboarding teammate provides interim configuration support even when you're working in the direct editing interface.

### Activating Your Metric
<a name="detection-activating-your-metric"></a>

Once you're satisfied with your metric configuration and preview results:

1. Change the metric status from Draft to Ready.

1. Click "Save changes" to activate the metric.

The metric will now recalculate for your production insights based on your configured thresholds.

## Configuring Rules
<a name="detection-configuring-rules"></a>

The "Insights" configuration tab displays your configured metrics and rules alongside a preview of the insights they generate under the "Insights" tab. This unified view allows you to see both your monitoring configurations and their operational impact in one place.

### Creating a New Rule
<a name="detection-creating-a-new-rule"></a>

To create a new rule, you can either:
+ **Use natural language:** Ask your onboarding teammate to create a rule for you. For example: "Create a rule to alert when forecast accuracy drops below 85% for A-class products." The agent translates your requirements into a rule configuration.
+ **Use the create rule button:** Click "*Add rule"* to open the rule creation interface and define parameters directly.

When you create or edit a rule, the system saves it with a "Draft" status. This allows you to configure and test the rule without impacting production insights.

### Reviewing an Existing Rule
<a name="detection-reviewing-an-existing-rule"></a>

When you click on a rule, you arrive at the rule review page where you can:
+ **Review the configuration:** See the current setup of your rule, including metric connections, thresholds, conditions, and granularity settings.
+ **Ask questions with natural language:** Work with the onboarding teammate to understand and refine your rule. Ask questions like:
  + "How does this rule determine when to trigger insights?"
  + "Can we add filtering for specific product categories?"
  + The agent helps you iterate on the rule logic conversationally, translating your monitoring requirements into the appropriate configuration.
+ **Preview individual rule impact:** Use the rule preview to see how insights would be generated at runtime with your current configuration. Filter the preview by specific products and sites to understand how the rule will impact different parts of your supply chain.
  + Expand the "Preview" element at the bottom of the screen.
  + Click "Preview insight" to generate runtime insights.
  + Refine your preview with search criteria across products and sites.
+ **Iterate with Preview:** As you work with the onboarding agent to refine the rule, use preview to validate changes. Continue iterating until the preview results match your operational needs, then save your configuration.

**Edit Fields Directly (Optional):** If you prefer to configure the rule yourself, click "Edit" to change fields directly without agent support. Even when editing manually, you can still ask the onboarding teammate questions like:
+ "What does this threshold field control?"
+ "Can you help me limit this to Class A products?"

Your onboarding teammate provides interim configuration support even when you're working in the direct editing interface.

### Activating Your Rule
<a name="detection-activating-your-rule"></a>

Once you're satisfied with your rule configuration and preview results:

1. Change the rule status from Draft to Ready.

1. Click "Save changes" to activate the rule.

The rule will now generate insights in production based on your configured thresholds and conditions.

## Reviewing Overall Insights
<a name="detection-reviewing-overall-insights"></a>

After configuring and activating your metrics and rules, review the combined impact of all your configurations:

1. Navigate to the **Detection** tab on the Monitoring Configuration page and expand the preview panel.

1. This global view preview displays the complete set of insights that would be generated with all your current configurations, showing you the combined effect of your metrics and rules.

1. Use this view to assess whether your monitoring setup produces the right volume and insights for your operations.

1. If you need to adjust the sensitivity or coverage of your monitoring, work directly with the onboarding agent to tweak them or navigate to individual metrics or rules to refine them further.