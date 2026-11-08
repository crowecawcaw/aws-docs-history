

# Creating and Configuring a Demand Plan (Self-Tuning)
<a name="creating-and-configuring-a-demand-plan-self-tuning"></a>

## Overview
<a name="creating-and-configuring-a-demand-plan-self-tuning-overview"></a>

Amazon Connect Decisions offers a self-tuning experience for creating and configuring demand plans. Instead of manually selecting settings through a form, you work with the AI supply chain teammate, which analyzes your data, suggests a validated configuration, prepares your data, and generates forecasts through iterative experimentation.

**Note**  
Screens in this guide come from a walkthrough with a fictional company. Your instance shows your own data.

### What the Self-Tuning Experience Does
<a name="creating-and-configuring-a-demand-plan-self-tuning-what-self-tuning-does"></a>
+ Analyzes your uploaded data and suggests a validated plan configuration
+ Inspects and prepares your historical data before forecasting
+ Runs forecasts at multiple hierarchy levels with automatic model selection
+ Incorporates external signals (such as weather, holidays, retail sales data, and sentiment analysis) without manual uploads
+ Allows iterative refinement through natural language conversation
+ Provides ability to promote optimized plan configurations to use for performing production planning

### Key Benefits
<a name="creating-and-configuring-a-demand-plan-self-tuning-key-benefits"></a>
+ Go from data upload to production forecast in days
+ Fully self-serve with no AWS involvement required
+ Configuration validated against your data before plan creation
+ Full transparency into what was corrected and why
+ Provide feedback and context in plain language at every step

## Prerequisites
<a name="creating-and-configuring-a-demand-plan-self-tuning-prerequisites"></a>
+ Your Amazon Connect Decisions instance is set up and configured
+ Your user account is assigned a Manager role
+ Historical demand data has been uploaded to the Supply Chain Data Lake (SCDL)
+ The self-tuning feature is enabled for your instance
+ Product, site (ship-to and ship-from), channel, or customer data entities are prepared and uploaded

**Note**  
For details on required data entities (outbound\_order\_line, product, site, etc.), refer to the Data Entities section of the Demand Planning User Guide.

### Data Readiness Checklist
<a name="creating-and-configuring-a-demand-plan-self-tuning-data-readiness-checklist"></a>

Before you start a draft, confirm that your data meets the following:
+ Every id column is unique per row
+ Every product\_id in your orders exists in Product, and every site\_id exists in Site
+ Demand quantity is in final\_quantity\_requested, not a generic quantity column
+ At least 52 weeks of order history (104 or more weeks for seasonal catalogs)
+ Product descriptions are clean, human readable, and unique per product
+ Product hierarchy levels nest cleanly (no level maps to more than one parent)
+ Sites include a state or region so weather and regional signals can be mapped
+ Discontinued products are flagged, not removed

## Workflow at a Glance
<a name="creating-and-configuring-a-demand-plan-self-tuning-workflow-at-a-glance"></a>

The self-tuning workflow has four steps. A progress indicator shows which step the plan is in at any time.


| Step | Name | What Happens | 
| --- | --- | --- | 
| 1 | Start a New Draft Plan | The AI teammate analyzes your data, suggests a validated configuration, and creates the plan. | 
| 2 | Data Preparation | Your data is inspected and enriched. You review corrections and provide context. | 
| 3 | Review Forecast (Back Test) | Forecast generated using multiple models and levels, with accuracy metrics presented for review. | 
| 4 | Promote to Production | Promote the validated plan to production with a recurring or one-time schedule. | 

To see each stage and its status, click Show steps on the status banner at the top of the plan.

![](https://docs.aws.amazon.com/connect-decisions/latest/userguide/images/creating-and-configuring-a-demand-plan-self-tuning-workflow-progress-indicator.jpg)


*The expanded progress indicator shows each stage of the workflow.*

## Draft Plans and Production Plans
<a name="creating-and-configuring-a-demand-plan-self-tuning-draft-and-production-plans"></a>

Every self-tuning plan starts as a draft. A draft is where you refine the configuration, data, and forecast with the AI teammate. When the draft meets your accuracy targets, you promote it to production.


| Aspect | Draft Plan | Production Plan | 
| --- | --- | --- | 
| Purpose | Experiment and refine configuration, data, and forecasts before going live. | Generate forecasts for operational use. | 
| How It Is Created | Select Start a New Draft from the Plans page and work with the AI teammate. | Promote a validated draft to production. | 
| Schedule | No schedule. Forecasts are generated as back tests while you refine the plan. | Runs one time or on a recurring schedule that you set when you promote. | 

### Settings Not Configured in a Draft
<a name="creating-and-configuring-a-demand-plan-self-tuning-settings-not-configured-in-draft"></a>

When you configure a draft with the AI teammate, the following settings are not part of the draft configuration:
+ Optimization Metric. Instead of selecting an optimization metric, review WAPE and Bias in Step 3: Review Forecast (Back Test) and tell the AI teammate your accuracy targets, for example "WAPE needs to be below 15%."
+ Planning Schedule. You set the schedule when you promote the plan. See Step 4: Promote to Production.

### Discarding a Draft
<a name="creating-and-configuring-a-demand-plan-self-tuning-discarding-a-draft"></a>

To discard a draft, click Discard draft at the top right of the draft plan page. When the discard completes, you receive a Draft discard: Completed notification. You can start a new draft at any time.

## Step 1: Start a New Draft Plan
<a name="creating-and-configuring-a-demand-plan-self-tuning-step-1-start-new-draft"></a>

### Navigate to Plans
<a name="creating-and-configuring-a-demand-plan-self-tuning-navigate-to-plans"></a>

1. From your Amazon Connect Decisions homepage, navigate to Plans.

1. On the Plan page, click the three-dot menu (…).

1. Select Start a New Draft.

**Note**  
If you have an existing plan, the AI teammate offers to carry the current configuration forward. You can keep the same settings or ask to modify them.

![](https://docs.aws.amazon.com/connect-decisions/latest/userguide/images/creating-and-configuring-a-demand-plan-self-tuning-start-new-draft.jpg)


*A new draft opens on the Plan configuration tab, with the AI teammate on the right.*

### Suggested Configuration
<a name="creating-and-configuring-a-demand-plan-self-tuning-suggested-configuration"></a>

The AI teammate analyzes your uploaded data and presents a recommended configuration:
+ Time Bucket (for example, weekly)
+ Forecast Granularity (for example, product and ship-to-site)
+ Planning Horizon (for example, 13 weeks)
+ Forecast Start Date
+ Number of Time Series identified
+ Historical Depth available for training

This configuration is validated against your data and system capabilities to ensure a valid, high-quality forecast.

### Modifying the Configuration
<a name="creating-and-configuring-a-demand-plan-self-tuning-modifying-the-configuration"></a>

You can modify any setting through natural language:
+ "My business works at product and site level"
+ "I need a 52-week forecast horizon"
+ "I want monthly forecasts instead of weekly"

Your preferences are validated against the data and the configuration updates accordingly.

### Defining Plan Scope
<a name="creating-and-configuring-a-demand-plan-self-tuning-defining-plan-scope"></a>

You can scope your plan to specific segments rather than forecasting the entire dataset:
+ "Only focus on products in the Electronics category"
+ "Exclude discontinued products"
+ "Only forecast for North American sites"

### Business Context Awareness
<a name="creating-and-configuring-a-demand-plan-self-tuning-business-context-awareness"></a>

The AI teammate incorporates knowledge about your specific business. It understands your industry context and tailors configurations accordingly (for example, adjusting for food service demand patterns for a quick-service restaurant chain).

### Confirm and Create Plan
<a name="creating-and-configuring-a-demand-plan-self-tuning-confirm-and-create-plan"></a>

When satisfied, confirm by saying: "Looks good, set up the plan." The system will:
+ Create the plan with the finalized configuration
+ Display the configuration summary on the left panel
+ Prompt you to start data preparation

## Step 2: Data Preparation
<a name="creating-and-configuring-a-demand-plan-self-tuning-step-2-data-preparation"></a>

In this step, your historical data is inspected and enriched before it enters the forecasting engine.

Data preparation runs in the background. You can leave the page; you are notified when your data is ready for review. To check progress, click Show steps on the status banner or ask the AI teammate, "What is the status of my plan?"

![](https://docs.aws.amazon.com/connect-decisions/latest/userguide/images/creating-and-configuring-a-demand-plan-self-tuning-data-preparation-running.jpg)


*Data preparation running, with the configuration summary on the Plan configuration tab.*

### What Happens During Data Preparation
<a name="creating-and-configuring-a-demand-plan-self-tuning-what-happens-during-data-prep"></a>
+ Gap Detection: Identifies periods where data should exist but is missing
+ Spike Identification: Detects unusual one-time spikes that could distort the forecast
+ Hidden Demand Detection (Loss-of-Sales Correction): Identifies zero-sales periods caused by inventory stockouts and estimates actual demand
+ Lineage Application: Uses similar products as a baseline for new products with no history
+ Gap Filling: Fills identified gaps with statistically inferred values

### Understanding the Data Preparation View
<a name="creating-and-configuring-a-demand-plan-self-tuning-understanding-data-prep-view"></a>

After data preparation completes, a chart displays two lines:
+ Historical Sales Data (Blue Line): Your raw historical data as uploaded
+ Enriched Sales Data (Red Line): The corrected data after fixes are applied

Use product, site, and channel filters to drill into specific items. Where no corrections were needed, the lines overlap.

![](https://docs.aws.amazon.com/connect-decisions/latest/userguide/images/creating-and-configuring-a-demand-plan-self-tuning-data-preparation-view.jpg)


*The Data preparation view filtered to a single product.*

### Reviewing Corrections
<a name="creating-and-configuring-a-demand-plan-self-tuning-reviewing-corrections"></a>

For each correction, you can see:
+ What was found (for example, "Unusual spike on Feb 5 for Product 1006")
+ What was done (for example, "Flattened the spike as it appears to be a one-time event")
+ Context reasoning (for example, "The November 18 spike was retained because it aligns with holiday demand")

The system is context-aware. It can recognize that a spike near a holiday is seasonal and retain it, while flattening an isolated spike with no seasonal explanation.

To get a summary of what was found and treated, click Analyze data or ask the AI teammate to "analyze the prepared data."

### Responding to Actions
<a name="creating-and-configuring-a-demand-plan-self-tuning-responding-to-actions"></a>

You may be asked for confirmation or additional business context:
+ "Is this spike a one-time event or recurring demand?"
+ "Which existing products should serve as the baseline for new items?"
+ "Was this gap due to a stockout, seasonal shutdown, or data issue?"

Respond in natural language:
+ "The spike in February is expected, it was due to a promotional event"
+ "This product is a replacement for Product-B, use its history"
+ "Fill those gaps with zero, we had a planned production shutdown"

The affected data is reprocessed and the chart updates immediately.

### Modifying Historical Data
<a name="creating-and-configuring-a-demand-plan-self-tuning-modifying-historical-data"></a>

You can proactively modify historical data through conversation:
+ "Remove the bulk order spike from March 2024"
+ "The zero sales in June were due to a stockout, actual demand was approximately 500 units"
+ "The drop in November was a system issue, not a real demand decline"

### Proceeding to Forecasting
<a name="creating-and-configuring-a-demand-plan-self-tuning-proceeding-to-forecasting"></a>

Once satisfied with the prepared data, say: "My history looks good, proceed to forecasting."

## Step 3: Review Forecast (Back Test)
<a name="creating-and-configuring-a-demand-plan-self-tuning-step-3-review-forecast"></a>

### How Forecasting Works
<a name="creating-and-configuring-a-demand-plan-self-tuning-how-forecasting-works"></a>

A back test is run to validate the forecast before applying it to future periods:
+ Identifies the appropriate back test period
+ Forecasts at multiple hierarchy levels (product category, brand, individual SKU)
+ Sources relevant external signals automatically
+ Selects optimal models, removing underperformers
+ Reconciles forecasts across levels
+ Reviews accuracy against demand pattern characteristics (smooth, lumpy, seasonal, intermittent)

If the forecast does not meet thresholds, the system iterates automatically: pruning models, adjusting inputs, and regenerating until acceptable accuracy is achieved.

Forecasting runs in the background. You are notified when the forecast is ready for your review. To check progress, ask the AI teammate, "What is the status of my plan?"

### External Signals
<a name="creating-and-configuring-a-demand-plan-self-tuning-external-signals"></a>

External signals that impact your demand are automatically identified and incorporated. You do not need to upload these.
+ Retail sales volume data
+ Industry-specific market indicators
+ Sentiment analysis for your product brands
+ Macroeconomic indicators
+ Weather
+ Holidays and seasonal events (for example, flu season and sporting events)

Below the chart, click External signals to see each demand driver and the public sources it is built from. Ask the AI teammate to explain the impact of each signal.

![](https://docs.aws.amazon.com/connect-decisions/latest/userguide/images/creating-and-configuring-a-demand-plan-self-tuning-external-signals-tab.jpg)


*The External signals tab lists each demand driver and its public sources.*

### Understanding the Forecast View
<a name="creating-and-configuring-a-demand-plan-self-tuning-understanding-forecast-view"></a>
+ Enriched Sales Data: Your sales history after data preparation
+ Final Forecast (Green Line): The generated forecast
+ Current Year Demand (Blue Line) and Prior Year Demand (Gray Dashed Line): Demand for the current and prior year
+ Forecast Start (Red Dashed Line): The date the forecast begins
+ External Signals Tab: Demand drivers applied, with their public sources
+ Accuracy Metrics: Bias %, WAPE, Forecasted Combinations, Zero Forecast Combinations, and average historical and forecast units per week

![](https://docs.aws.amazon.com/connect-decisions/latest/userguide/images/creating-and-configuring-a-demand-plan-self-tuning-review-forecast-view.jpg)


*The Review forecast view with the accuracy scoreboard and chart.*

### Providing Feedback
<a name="creating-and-configuring-a-demand-plan-self-tuning-providing-feedback"></a>

If you want to improve the forecast:
+ "The bias is too high"
+ "WAPE needs to be below 15%"
+ "This product has a promotional pattern every Q4"

New experiments will run with adjusted parameters.

**Note**  
Reforecasting may take some time. A banner indicates the process is running. You can continue chatting while it regenerates.

## Step 4: Promote to Production
<a name="creating-and-configuring-a-demand-plan-self-tuning-step-4-promote-to-production"></a>

### When to Promote
<a name="creating-and-configuring-a-demand-plan-self-tuning-when-to-promote"></a>

Promote your plan when:
+ The back test meets your accuracy targets
+ You are confident the data preparation reflects your demand patterns
+ You are ready for the plan to run on a schedule

### Promotion Steps
<a name="creating-and-configuring-a-demand-plan-self-tuning-promotion-steps"></a>

1. Click Promote to production at the top of the plan.

1. Choose how to run your production plan:
   + Run Type: One time run or Recurring schedule
   + Forecast Start Date

1. Click Generate. A banner confirms that plan generation has started.

![](https://docs.aws.amazon.com/connect-decisions/latest/userguide/images/creating-and-configuring-a-demand-plan-self-tuning-promote-to-production-dialog.jpg)


*The Promote to production dialog.*

The production plan is generated from the approved draft configuration. When it is ready, you receive a Demand plan generation completed successfully notification. On the Plans page, the draft is marked Approved and the production plan appears beneath it.

![](https://docs.aws.amazon.com/connect-decisions/latest/userguide/images/creating-and-configuring-a-demand-plan-self-tuning-plans-page-approved-draft.jpg)


*The Plans page shows the approved draft and the production plan generated from it.*

### Review and Publish the Production Plan
<a name="creating-and-configuring-a-demand-plan-self-tuning-review-and-publish-production"></a>

Review the production plan the same way as the draft, then click Publish to release it. To start the next planning cycle, open the menu next to Publish and select Start new draft.

![](https://docs.aws.amazon.com/connect-decisions/latest/userguide/images/creating-and-configuring-a-demand-plan-self-tuning-publish-production-plan.jpg)


*Publish the production plan, or start a new draft from the menu.*

## Notifications
<a name="creating-and-configuring-a-demand-plan-self-tuning-notifications"></a>

You receive an email and an in-app notification when a plan task completes or needs your attention. To view in-app notifications, click the bell icon in the top bar, then select a notification to go to the plan. Email notifications include an Open draft button. Notifications are retained for 90 days.

![](https://docs.aws.amazon.com/connect-decisions/latest/userguide/images/creating-and-configuring-a-demand-plan-self-tuning-notifications-page.jpg)


*The Notifications page.*


| Notification | What to Do Next | 
| --- | --- | 
| Data preparation: Ready for your review | Review the corrections in the Data Preparation view and respond to any questions from the AI teammate. Once you are satisfied with the prepared data, say "My history looks good, proceed to forecasting." | 
| Forecast generation: Ready for your review | Review WAPE, Bias, and the external signals in the forecast view. Provide feedback to run new experiments, or click Promote to production when the back test meets your accuracy targets. | 
| Demand plan generation completed successfully | Your production plan is ready for review. Review it, then click Publish. | 
| Draft discard: Completed | Your draft was discarded. Start a new draft whenever you are ready. | 
| Action needed: Demand plan generation for <plan name> has failed | Follow the actions listed in the notification, such as correcting the data in the listed columns or adjusting the configuration. | 
| Needs attention | The task could not be processed. The team is automatically alerted, and you receive a notification when processing is complete. If it is urgent or the issue persists, contact AWS Support. | 

![](https://docs.aws.amazon.com/connect-decisions/latest/userguide/images/creating-and-configuring-a-demand-plan-self-tuning-plan-generation-notifications.jpg)


*A plan generation success notification and a plan generation failure notification.*

## What Changed from the Previous Experience
<a name="creating-and-configuring-a-demand-plan-self-tuning-what-changed"></a>


| Aspect | Previous | Self-Tuning | 
| --- | --- | --- | 
| Plan Configuration | Manual form without data validation. Invalid settings could cause failed or poor forecasts. | Suggested by the AI teammate, validated against your data and system capabilities. | 
| Plan Scope | Entire dataset forecasted. No way to focus on specific segments. | Define scope via natural language (specific products, sites, categories). | 
| Data Preparation | Data passed directly to forecasting without inspection or correction. | Data inspected, gaps filled, anomalies corrected, with corrections shown transparently. | 
| Historical Data Editing | Not possible after upload. | Modify through conversation at any time. | 
| Model Tuning | Required manual effort over multiple weeks. | Automatic: underperformers pruned, models iterated. | 
| External Signals | Manual upload as supplementary time series. | Sourced automatically, no manual uploads needed. | 
| Forecasting | Single pass, one-shot generation. | Multi-level with back test and iterative improvement. | 
| Data Cleaning Rules | Manual pre-processing rules. | Replaced by conversational data preparation. | 
| Time to Production | Weeks. | Days. | 
| Workflow Visibility | Limited: configure and wait. | Full progress tracking at each stage. | 

## Frequently Asked Questions
<a name="creating-and-configuring-a-demand-plan-self-tuning-faq"></a>

### How do I start a new draft plan?
<a name="creating-and-configuring-a-demand-plan-self-tuning-faq-start-new-draft"></a>

From your Amazon Connect Decisions homepage, navigate to Plans, click the three-dot menu (…), and select Start a New Draft. See Step 1: Start a New Draft Plan.

### How do I configure a draft demand plan?
<a name="creating-and-configuring-a-demand-plan-self-tuning-faq-configure-draft"></a>

The AI teammate analyzes your data and suggests a configuration, including time bucket, forecast granularity, planning horizon, and forecast start date. Change any setting in natural language, for example "I need a 52-week forecast horizon." When you are satisfied, say "Looks good, set up the plan." The AI teammate then prompts you to start data preparation.

### What is the difference between a draft plan and a production plan?
<a name="creating-and-configuring-a-demand-plan-self-tuning-faq-draft-vs-production"></a>

A draft plan is where you refine the configuration, data, and forecast. A production plan runs on a one-time or recurring schedule and generates forecasts for operational use. See Draft Plans and Production Plans.

### Can I set the Optimization Metric or Planning Schedule in a draft?
<a name="creating-and-configuring-a-demand-plan-self-tuning-faq-optimization-metric-schedule"></a>

No. These settings are not part of the draft configuration. Instead of selecting an optimization metric, review WAPE and Bias in the back test and tell the AI teammate your accuracy targets. You set the production schedule when you promote the plan to production.

### How do I move a draft to production?
<a name="creating-and-configuring-a-demand-plan-self-tuning-faq-move-to-production"></a>

When the back test meets your accuracy targets, click Promote to production, choose One time run or Recurring schedule, set the forecast start date, and click Generate. When the production plan is ready, review it and click Publish.

### How do I check the status of my plan?
<a name="creating-and-configuring-a-demand-plan-self-tuning-faq-check-status"></a>

Click Show steps on the status banner at the top of the plan, or ask the AI teammate, "What is the status of my plan?"

### How do I discard a draft?
<a name="creating-and-configuring-a-demand-plan-self-tuning-faq-discard-draft"></a>

Click Discard draft at the top right of the draft plan page. You receive a Draft discard: Completed notification when the discard completes.

### What happens after I promote a draft?
<a name="creating-and-configuring-a-demand-plan-self-tuning-faq-after-promote"></a>

The production plan is generated from the approved draft configuration. On the Plans page, the draft is marked Approved and the production plan appears beneath it. Review the production plan, then click Publish.