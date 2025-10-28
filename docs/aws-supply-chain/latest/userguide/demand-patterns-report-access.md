# Demand Pattern and Recommendation Report Access

## First time forecast creation

When creating a forecast for the first time, under the **Demand
Planning** module in AWS Supply Chain, choose **Create a
Plan**. The system guides you through three steps: Data Ingestion, Plan
Configuration, and finally, Forecast Generation. After completing data ingestion and
plan configuration, choose **Generate Forecast** to initiate data
validation. Upon successful validation, the system performs demand pattern analysis, and
you see a hyperlink to access this analysis while your forecast generates.

## Subsequent forecast creation

For subsequent forecasts, choose **Generate Forecast**. You see a
banner displaying three steps: data validation, demand pattern analysis &
recommendation, and forecast creation. After data validation is successful and the
demand pattern analysis is complete, access the report by choosing its hyperlink in the
banner.

## Report content

The Demand Pattern and Recommendations report provides a summary view of
exploratory data analysis at your configured forecast level for a given plan. At the top
of the screen, you see five key pattern cards that show how your products are
distributed: Smooth patterns, Intermittent patterns, Erratic patterns, Lumpy patterns,
and Products with Zero Historical Demand.

Below this summary, you can find a detailed table breaking down patterns by the
highest configured level in product hierarchy in the Demand Plan Settings. For example,
if your product hierarchy configuration follows pattern product id, product group id,
then you will see the summary at the product group id. For each category, you can see
the following:

- # Forecasts, indicating the unique time series are eligible for forecast and its
  percentage of total
- The annual demand volume and its percentage of total
- A visual breakdown of demand pattern within that category
- A visual breakdown of the length of history available within that
  category

To help you navigate this information, you can do the following:

- Use the search box to find specific product categories
- Download a detailed report. The report contains detailed analysis for each
  individual forecast at your configured granularity level
- Sort any product category, # Forecasts, and Annual Demand to focus on specific
  metrics. For product categories containing alphanumeric formats or blank values,
  using the search function may be more effective.

## Ongoing access

After each successful forecast creation, you can revisit this analysis on the
**Demand Pattern** tab in the forecast review pages. In this view,
the analysis responds to any filters you apply in the forecast review. The downloaded
report contains analysis specific to your filtered selection.
