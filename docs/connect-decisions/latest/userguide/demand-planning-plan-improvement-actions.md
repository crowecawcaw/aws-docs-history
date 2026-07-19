# Plan Improvement Actions

Amazon Connect Decisions proactively identifies opportunities to improve your demand forecast accuracy by detecting patterns and anomalies that require your business context. Plan improvement actions are AI-generated tasks that surface where your input can most meaningfully enhance forecast quality, enabling your AI teammates to learn from your expertise and produce more accurate plans over time.

The system uses ML-driven detection to analyze your demand data, identify products and sites where forecasts would benefit from your input, and presents actions grouped by type. You provide input through the Supply Chain Decisions Teammate, and your feedback is automatically integrated into future forecast runs, creating a continuous improvement loop between you and your AI teammates.

## How Plan improvement actions work

Plan improvement actions follow a three-step workflow:

1. **Detect** - The system analyzes your demand data using ML-driven detection and clustering. It identifies products and product-sites that need your input based on pre-determined scenarios including new products with limited history, products with extremely low forecastability, intermittent demand gaps, anomalous demand patterns, known global events, and high-variability products.
2. **Surface** - Detected actions are converted into digestible, pattern-level insights that you can confirm, correct, or contextualize. Actions are presented in the Demand Plan, grouped by action type.
3. **Act** - You apply validated corrections by providing input through the Supply Chain Decisions Teammate. Your inputs are integrated into planning configuration updates, data treatment rules, related time series inputs, and forecast override rules. The system then uses your input to refine models and improve future forecast accuracy.

###### Note

Plan improvement actions are refreshed every time a plan is run, ensuring that as incremental data is ingested into the system (such as additional products/sites added to planning or recent demand history uploads), you continue to receive updated actions on products and patterns needing your input.

## Viewing Plan improvement actions

When you log into Amazon Connect Decisions, you can access Plan improvement actions from the Plans listing page.

**To view Plan improvement actions:**

1. Navigate to the Plans page from the landing page (Login→Home).
2. In the Plans listing page, locate the demand plan you want to review. Plan prioritization is based on pending Plan improvement actions as one of the factors.
3. Select the plan to open the plan details view.
4. Choose the Plan Improvement Actions tab.

The tab displays a list of actions grouped by action type alongside your forecast outputs. Each action includes:

- **Input Topics** - The category of input needed (static)
- **Description** - Dynamic description of the specific pattern or issue detected, including product, site, and product-site details
- **Status** - Current progress (Open or Closed)
- **Actions** - Available operations (View, Complete)

## Understanding action types

Plan improvement actions cover the most common scenarios where planner expertise improves forecast accuracy:

| #   | Action Type                                                         | Description                                                                                                                     | Example                                                                                                                                                          |
| --- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Provide input for new products/sites**                            | Products launched recently with zero or limited history and no product lineage data available.                                  | 25 products launched in the last 2 months have zero or limited history and no product lineage data available.                                                    |
| 2   | **Provide input on products with extremely low forecastability**    | Products with average demand per period since launch/first order in history < 0.5, such as slow sellers and long tail products. | 30 Slow Sellers/Long Tail Products/Sporadic sellers with average demand per period since launch/first order in history < 0.5.                                    |
| 3   | **Provide input on products with continuous periods of zero sales** | Active products/product-sites with zero orders in the last year that may need discontinuation or scope adjustment.              | 100 Active product/product-site with zero orders in last 1 year.                                                                                                 |
| 4   | **Provide reasoning for intermittent gaps in historical demand**    | Random/non-repeating demand spikes and demand drops in history with no correlated causals (related time series).                | Unexplained, intermittent periods of no sales (e.g., random/non-repeating demand spikes or demand drop in history with no correlated causals).                   |
| 5   | **Validate "known" global events**                                  | One-time anomalies that coincide with known global disruptions or major differences in trend levels during specific periods.    | One-time anomalies that coincide with known global disruptions/Major Difference in trend levels for 100 products during 2020-2021 periods coinciding with COVID. |
| 6   | **Provide causals/events for high-variability products**            | Products exhibiting high variability in historical demand and "flat" forecast outputs.                                          | 26 products exhibit High Variability in historical demand and "flat" forecast outputs.                                                                           |

## Completing a Plan improvement action

You provide input through the Supply Chain Decisions Teammate, which allows you to share business context for multiple products through natural language conversation.

### Using the Supply Chain Decisions Teammate

1. From the Plan Improvement Actions tab, choose View on the action you want to address.
2. The Supply Chain Decisions Teammate panel opens on the right side of the screen, contextual to the selected action topic.
3. The agent will ask clear and specific questions about the products in scope. For example:

   - "What is the reason for the one-time 4x spike in demand for Product X in Feb 2024?"
   - "Do you expect this event to recur?"

4. Provide your response in natural language. The agent will:

   - Clarify through follow-up questions if needed (e.g., if your previous input contradicts new input)
   - Intelligently manage and prevent redundant questions (enabled by smart memory)
   - Present hypotheses for you to validate (e.g., "Should I treat this as promo uplift or true spike?")

5. When you have finished providing input for all product-sites in scope, the action status changes to Closed.

###### Note

You can also initiate a conversation with the agent to provide input proactively, even without navigating from a specific action. For example, you can ask "Why do I see a zero forecast for the entire forecast horizon for product XX?"

###### Note

If 10 products have similar input, the system groups them together as Agent groups to help simplify and ease planner actions.

## Tracking progress

Plan improvement actions have the following status lifecycle:

| Status     | Description                                                                                                      |
| ---------- | ---------------------------------------------------------------------------------------------------------------- |
| **Open**   | The action has been detected and surfaced but no planner input has been provided yet.                            |
| **Closed** | The planner has provided input through the Supply Chain Decisions Teammate, covering all product-sites in scope. |

**Tracking overall progress:**

- The system continuously tracks closed versus open actions after every plan run.
- The action list refreshes based on the latest data. As incremental data is ingested into the system during a new planning cycle (e.g., additional products/sites added to planning or recent demand history uploads), you continue to receive updated/refreshed actions.

## How your input improves forecasts

Your input from Plan improvement actions is seamlessly integrated into three key areas:

1. **Refinement of demand planning rules** - For example, your input on the reason for long periods of missing demand results in the product being removed from planning scope (product discontinuation).
2. **Enriching forecast inputs with causal data** - Enriching forecast inputs with causal data/Related Time Series (RTS) constructed based on your provided business context in natural language (e.g., automatically constructing a related time series for a recurring promotion).
3. **Capturing business rules** - Helps capture business rules unique to a select pattern of products (e.g., exclude from forecasting products with less than 3 orders).

Your inputs can result in different types of plan configuration updates, including:

- **Upload Product Lineage or Site Lineage Data** - Ingest Product Alternate, Site Alternate, or Product-Site Alternate data
- **Update Plan Configuration - Planning Rules** - Update forecast override rules (e.g., use sales forecast or marketing forecast as consensus plan input for 3 months from launch date)
- **Update Plan Configuration - Plan Scope** - Exclude from forecasting, forecast using last n period average
- **Construct Causal Data as Related Time Series** - Construct RTS for anomalies, COVID periods, or causal data (e.g., Price, Promotion, or Marketing Data)

## Best practices

- **Provide context, not just answers** - When using the Supply Chain Decisions Teammate, explain the business reasoning behind your input. This helps the agent learn generalizable patterns.
- **Review actions each planning cycle** - New actions are generated with each plan run as new data is ingested. Regular review ensures your forecasts continuously improve.
