# Terminology used in Demand Planning

The following is the common terminology that you may frequently use in Demand
Planning.

- Enterprise demand plan – A single planning
  workbook that consolidates forecast input from multiple stakeholders to create a unified
  forecast. It can consist of multiple planning cycles, enabling iterative refinement of
  forecast based on evolving forecast input dataset. The enterprise demand plan displays two
  status points:
  - **Active** – The planning cycle is open and
    you can edit your forecast.
  - **Published** – The planning cycle is closed,
    and you cannot edit your forecast. However, you can view the demand plan.

- **Demand planning cycle** – The time taken to create
  and finalize demand plans, which include forecast generation, and collaborating with
  stakeholders to adjust and publish demand plans.
- **Dataset** – A collection of data used for
  generating forecasts, such as historical sales orders or product information.
- **Forecast granularity** – Defines how you want to
  create and manage the forecast. You can use a combination of product, location, customer,
  and channel dimensions. You can also choose the time interval for the forecast data to be
  aggregated by day, week, month, or year for each product in the dataset. For example, if
  your forecast granularity is set as Daily, you will see the forecast daily for each
  product in the dataset.

###### Note

Demand Planning uses the Gregorian calendar for planning. The default start day of
the week is Monday.

- **Forecast configuration** – The set of
  configurations for forecast generation. This includes the planning cycle configuration,
  time horizon granularity, and that hierarchy configuration that influences how Demand
  Planning will generate the forecast.
- **System generated forecast** – This is also known
  as the baseline forecast. It refers to the use of the historical data by the system to
  generate a forecast. It provides initial demand prediction before you apply any
  overrides.
- **Override** – A modification that you make to the
  system generated forecast.
- **Published demand plan** – The final output of
  the planning workbook. You can choose to publish the finalized demand plan to downstream
  inventory and supply planning systems for implementation.
- **Product lineage** – You can establish links between products and their previous versions or alternate products and set rules for the amount of historical data to be used in forecasting. For more information, see
  [Product lineage](product_lineage.md "product_lineage.md").
- **Product lifecycle** – The product lifecycle
  refers to the various stages of a product from introduction to End of Life (EoL). For more
  information on product lifecycle, see [Product lifecycle](product_lifecycle.md "product_lifecycle.md").
- **Demand driver** – Factors that directly
  influence the level of demand for a particular product. For example, advertising and
  marketing efforts, pricing strategies, and so on. For more information on demand drivers,
  see [Forecast based on demand drivers](demand_drivers.md "demand_drivers.md").
- **Forecast lag** – The time between when the forecast was created and the actual demand. For example, forecast from January considered for February
  is considered a one month lag. Similarly, forecast from January that is considered for March is considered a two month lag.
- **Forecast Model Analyzer** – You can use this tool to execute trial or experimental forecast by varying test conditions and reviewing the
  results of the different forecast methods. You can use the results to compare and evaluate model performance, ensuring the best selection based on business priorities.
- **Forecast Lock** – You can use the forecast lock feature to lock specific periods in your forecast to prevent any further edits or adjustments.
- **Intra-cycle Forecast Refresh** – You can refresh the forecast mid-cycle and incorporate the latest forecast input data without finalizing the demand plan.
- **# of Forecasts** – Number of unique time-series forecasts, where each time-series represents a distinct combination of product, site, customer, and channel as per demand plan configuration.
- **Critical Rules** – Data validation rules that, if violated, can block forecast creation. For more information, see [Prequisites before uploading your dataset](data_quality.md "data_quality.md").
- **Data Validation** – The process of checking data for completeness, correctness, and consistency before using it for forecasting.
- **Demand Pattern Analysis** – Exploratory Data Analysis of forecast input data including classifying historical demand data into different patterns.
