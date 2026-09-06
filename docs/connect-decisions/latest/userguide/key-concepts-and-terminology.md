

# Key Concepts and Terminology
<a name="key-concepts-and-terminology"></a>

## Decisioning
<a name="key-concepts-decisioning"></a>
+ **Insights:** The core resource for proactive supply chain monitoring, and the primary entity you work with in Amazon Connect Decisions. An insight brings together detection, root cause analysis, and recommended actions for a supply chain issue, helping you identify and resolve problems before they impact operations. An insight is generated when a rule detects that a metric has breached its defined conditions (for example, "Forecast accuracy for Product A dropped to 72% at Site B"). Related detections that share the same product, site, and recommendation type are consolidated into a single insight, giving you one place to investigate and act.
+ **Metrics:** Quantifiable measures that evaluate supply chain performance. Metrics define what to monitor (e.g., forecast accuracy, inventory levels, days of cover) and how to calculate these measures across your data.
+ **Rules:** Business logic that defines when exceptions (insights) should be generated. Rules specify the thresholds, conditions, and criteria that trigger insights based on your metrics (e.g., “Generate an exception when forecast accuracy falls below 85% for A-class products”). Metrics and rules work together to generate insights. Metrics define what to measure while rules evaluate those metrics against thresholds to determine when to generate insights. For example, a forecast accuracy metric calculates performance, and a rule triggers an insight when that metric falls below 85% for A-class products.
+ **Root cause:** The AI-powered investigation that explains why an exception occurred. Root cause analysis examines contributing factors, data patterns, and contextual information to identify the underlying reasons for performance deviations.
+ **Recommendations:** AI-generated suggested actions to resolve exceptions. Recommendations provide specific, actionable steps to address root causes and restore normal operations.
+ **Agent guidelines:** Instructions that guide the AI agent's behavior when analyzing exceptions and generating recommendations. These guidelines incorporate your business policies, operational constraints, and decision-making preferences.
+ **Severity Factors:** Configuration settings that determine how financial impact influences exception prioritization. Severity factors help the system surface the most business-critical issues first.

## Planning
<a name="key-concepts-planning"></a>

The following is the common terminology used in Demand Planning:
+ **Baseline forecast** – It refers to the use of the historical data by the system to generate a forecast. It provides initial demand prediction before you apply any overrides.
+ **Dataset** – A collection of data used for generating forecasts, such as historical sales orders or product information.
+ **Demand planning cycle** – The time taken to create and finalize demand plans, which include forecast generation, and collaborating with stakeholders to adjust and publish demand plans.
+ **Demand plan** – A plan is created for a defined time horizon and refreshed periodically through rolling time windows (planning cycles). Each demand plan can contain multiple versions within a planning cycle to support refinement of plan for any incremental data received within a planning cycle. The demand plan can display statuses including:
  + **Pending** – The plan configuration is created but not submitted for plan creation.
  + **In progress** – The plan configuration is submitted for plan creation and the plan is in progress for forecast generation.
  + **Failed** – The plan forecast has failed. Look for email and in-app notification to resolve issue.
  + **In-review** – The planning cycle is open and you can edit your forecast.
  + **Final** – The planning cycle is closed, and you cannot edit your forecast. However, you can view the demand plan.
+ **Forecast configuration** – The set of planning conditions that govern the plan for forecast generation. This includes the planning cycle configuration, time horizon granularity, and that hierarchy configuration that influences how Demand Planning will generate the forecast.
+ **Forecast granularity** – Defines how you want to create and manage the forecast. You can use a combination of product, location, customer, and channel dimensions. You can also choose the time interval for the forecast data to be aggregated by day, week, month, or year for each product in the dataset. For example, if your forecast granularity is set as Daily, you will see the forecast daily for each product in the dataset.
+ 
**Note**  
Demand Planning uses the Gregorian calendar for planning. The default start day of the week is Monday.
+ **Override** – A modification that you make to the system generated forecast.
+ **Planning Horizon** – The total length of time into the future for which forecasts are generated, measured from the forecast start date. The planning horizon is determined by combining the time bucket (Daily, Weekly, or Monthly) with the plan horizon length. For example, a weekly plan with a 26-week plan horizon creates forecasts covering the next 26 weeks from the forecast start date.
+ **Product lifecycle** – The product lifecycle refers to the various stages of a product from introduction to End of Life (EoL).
+ **Published demand plan** – The final output of the plan. You can choose to publish the finalized demand plan to downstream inventory and supply planning systems for implementation.