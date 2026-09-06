# Creating and Configuring a Demand Plan (Self-Tuning)

**Self-Tuning Experience**

_Amazon Connect Decisions | Demand Intelligence User Guide | August 2026_

## Overview

Amazon Connect Decisions offers a self-tuning experience for creating and configuring demand plans. Instead of manually selecting settings through a form, you work with the Decisions teammate, which analyzes your data, suggests a validated configuration, prepares your data, and generates forecasts through iterative experimentation.

### What the Self-Tuning Experience Does

- Analyzes your uploaded data and suggests a validated plan configuration
- Inspects and prepares your historical data before forecasting
- Runs forecasts at multiple hierarchy levels with automatic model selection
- Incorporates external signals (retail sales data, sentiment analysis) without manual uploads
- Allows iterative refinement through natural language conversation
- Provides ability to promote optimized plan configurations to use for performing production planning

### Key Benefits

- Go from data upload to production forecast in days
- Fully self-serve with no AWS involvement required
- Configuration validated against your data before plan creation
- Full transparency into what was corrected and why
- Provide feedback and context in plain language at every step

## Prerequisites

- Your Amazon Connect Decisions instance is set up and configured
- Your user account is assigned a Manager role
- Historical demand data has been uploaded to the Supply Chain Data Lake (SCDL)
- The self-tuning feature is enabled for your instance
- Product, site (ship-to and ship-from), channel, or customer data entities are prepared and uploaded

###### Note

For details on required data entities (outbound\_order\_line, product, site, etc.), refer to the Data Entities section of the Demand Planning User Guide.

## Workflow at a Glance

The self-tuning workflow has four steps. A progress indicator shows which step the plan is in at any time.

Self-tuning workflow steps| Step | Name | What Happens |
| --- | --- | --- |
| 1 | Start a New Draft Plan | Decisions teammate analyzes your data, suggests a validated configuration, and creates the plan. |
| 2 | Data Preparation | Your data is inspected and enriched. You review corrections and provide context. |
| 3 | Review Forecast (Back Test) | Forecast generated using multiple models and levels, with accuracy metrics presented for review. |
| 4 | Promote to Production | Promote the validated plan to production with a recurring or one-time schedule. |

## Step 1: Start a New Draft Plan

### Navigate to Plans

1. From your Amazon Connect Decisions homepage, navigate to Plans.
2. On the Plan page, click the three-dot menu (...).
3. Select Start a New Draft.

###### Note

If you have an existing plan, the Decisions teammate offers to carry the current configuration forward. You can keep the same settings or ask to modify them.

### Suggested Configuration

The Decisions teammate analyzes your uploaded data and presents a recommended configuration:

- Time Bucket (for example, weekly)
- Forecast Granularity (for example, product and ship-to-site)
- Planning Horizon (for example, 13 weeks)
- Forecast Start Date
- Number of Time Series identified
- Historical Depth available for training

This configuration is validated against your data and system capabilities to ensure a valid, high-quality forecast.

### Modifying the Configuration

You can modify any setting through natural language:

- "My business works at product and site level"
- "I need a 52-week forecast horizon"
- "I want monthly forecasts instead of weekly"

Your preferences are validated against the data and the configuration updates accordingly.

### Defining Plan Scope

You can scope your plan to specific segments rather than forecasting the entire dataset:

- "Only focus on products in the Electronics category"
- "Exclude discontinued products"
- "Only forecast for North American sites"

### Business Context Awareness

The Decisions teammate incorporates knowledge about your specific business. It understands your industry context and tailors configurations accordingly (for example, adjusting for food service demand patterns for a quick-service restaurant chain).

### Confirm and Create Plan

When satisfied, confirm by saying: "Looks good, set up the plan." The system will:

1. Create the plan with the finalized configuration
2. Display the configuration summary on the left panel
3. Automatically proceed to data preparation

## Step 2: Data Preparation

In this step, your historical data is inspected and enriched before it enters the forecasting engine.

### What Happens During Data Preparation

- **Gap Detection**: Identifies periods where data should exist but is missing
- **Spike Identification**: Detects unusual one-time spikes that could distort the forecast
- **Loss-of-Sales Correction**: Identifies zero-sales periods caused by inventory stockouts and estimates actual demand
- **Lineage Application**: Uses similar products as a baseline for new products with no history
- **Gap Filling**: Fills identified gaps with statistically inferred values

### Understanding the Data Preparation View

After data preparation completes, a chart displays two lines:

- **Original Data (Blue Line)**: Your raw historical data as uploaded
- **Enriched Data (Red Line)**: The corrected data after fixes are applied

Use product, site, and channel filters to drill into specific items. Where no corrections were needed, the lines overlap.

### Reviewing Corrections

For each correction, you can see:

- What was found (for example, "Unusual spike on Feb 5 for Product 1006")
- What was done (for example, "Flattened the spike as it appears to be a one-time event")
- Context reasoning (for example, "The November 18 spike was retained because it aligns with holiday demand")

The system is context-aware. It can recognize that a spike near a holiday is seasonal and retain it, while flattening an isolated spike with no seasonal explanation.

### Responding to Actions

You may be asked for confirmation or additional business context:

- "Is this spike a one-time event or recurring demand?"
- "Which existing products should serve as the baseline for new items?"
- "Was this gap due to a stockout, seasonal shutdown, or data issue?"

Respond in natural language:

- "The spike in February is expected, it was due to a promotional event"
- "This product is a replacement for Product-B, use its history"
- "Fill those gaps with zero, we had a planned production shutdown"

The affected data is reprocessed and the chart updates immediately.

### Modifying Historical Data

You can proactively modify historical data through conversation:

- "Remove the bulk order spike from March 2024"
- "The zero sales in June were due to a stockout, actual demand was approximately 500 units"
- "The drop in November was a system issue, not a real demand decline"

### Proceeding to Forecasting

Once satisfied with the prepared data, say: "My history looks good, proceed to forecasting."

## Step 3: Review Forecast (Back Test)

### How Forecasting Works

A back test is run to validate the forecast before applying it to future periods:

- Identifies the appropriate back test period
- Forecasts at multiple hierarchy levels (product category, brand, individual SKU)
- Sources relevant external signals automatically
- Selects optimal models, removing underperformers
- Reconciles forecasts across levels
- Reviews accuracy against demand pattern characteristics (smooth, lumpy, seasonal, intermittent)

If the forecast does not meet thresholds, the system iterates automatically: pruning models, adjusting inputs, and regenerating until acceptable accuracy is achieved.

### External Signals

External signals that impact your demand are automatically identified and incorporated. You do not need to upload these.

- Retail sales volume data
- Industry-specific market indicators
- Sentiment analysis for your product brands
- Macroeconomic indicators

Select a product in the forecast view to see which signals were applied. Ask the Decisions teammate to explain the impact of each signal.

### Understanding the Forecast View

- **Treated Historical Data (Blue Line)**: Enriched sales history from data preparation
- **Forecast (Green Line)**: The generated forecast
- **External Signals Panel**: Signals applied per product
- **Accuracy Metrics**: WAPE and Bias

### Providing Feedback

If you want to improve the forecast:

- "The bias is too high"
- "WAPE needs to be below 15%"
- "This product has a promotional pattern every Q4"

New experiments will run with adjusted parameters.

###### Note

Reforecasting may take some time. A banner indicates the process is running. You can continue chatting while it regenerates.

## Step 4: Promote to Production

### When to Promote

Promote your plan when:

- The back test meets your accuracy targets
- You are confident the data preparation reflects your demand patterns
- You are ready for the plan to run on a schedule

### Promotion Steps

1. Click Promote to Production.
2. Configure the production schedule:

   - Forecast Start Date
   - Run Type: One-time or Recurring
   - Recurrence Frequency: Weekly, monthly, or custom

3. Confirm the settings.

The plan now runs automatically on your schedule and appears as a Production Plan in the Plans list.

## What Changed from the Previous Experience

Comparison of the previous and self-tuning experiences| Aspect | Previous | Self-Tuning |
| --- | --- | --- |
| Plan Configuration | Manual form without data validation. Invalid settings could cause failed or poor forecasts. | Suggested by the Decisions teammate, validated against your data and system capabilities. |
| Plan Scope | Entire dataset forecasted. No way to focus on specific segments. | Define scope via natural language (specific products, sites, categories). |
| Data Preparation | Data passed directly to forecasting without inspection or correction. | Data inspected, gaps filled, anomalies corrected, with corrections shown transparently. |
| Historical Data Editing | Not possible after upload. | Modify through conversation at any time. |
| Model Tuning | Required manual effort over multiple weeks. | Automatic: underperformers pruned, models iterated. |
| External Signals | Manual upload as supplementary time series. | Sourced automatically, no manual uploads needed. |
| Forecasting | Single pass, one-shot generation. | Multi-level with back test and iterative improvement. |
| Data Cleaning Rules | Manual pre-processing rules. | Replaced by conversational data preparation. |
| Time to Production | Weeks. | Days. |
| Workflow Visibility | Limited: configure and wait. | Full progress tracking at each stage. |

## Glossary

Glossary of terms| Term | Definition |
| --- | --- |
| Back Test | A validation technique where a forecast is generated for a historical period to evaluate accuracy before applying the model to future periods. |
| Data Preparation | The step where historical data is inspected, corrected, and enriched before forecasting. |
| Decisions Teammate | The natural language interface in Amazon Connect Decisions that guides you through plan creation, data preparation, forecasting, and continuous improvement. |
| Draft Plan | A plan in experimentation mode where you refine configuration, data, and forecasts before promoting to production. |
| Enriched Data | Historical data after corrections (gap filling, spike removal, stockout adjustment) have been applied. |
| External Signals | Market indicators, retail sales data, and other signals automatically sourced to improve forecast accuracy. |
| Forecast Override Rules | Rules that adjust the baseline forecast to align with organizational goals, such as quantile selection, precedence logic, and lifecycle-based adjustments. |
| Lineage | Product-alternate mapping used for new products without history. Demand patterns from similar products serve as a baseline. |
| Plan Input Rules | Rules that control how the baseline forecast is created, including data inclusion/exclusion criteria, anomaly treatment, and history construction for new products. |
| Plan Scope | The defined subset of products and sites included in a plan. |
| Production Plan | A finalized plan that runs on a recurring schedule, generating forecasts for operational use. |
| Self-Tuning | The capability to automatically configure, correct data, select models, and iteratively improve forecasts without manual intervention. |
