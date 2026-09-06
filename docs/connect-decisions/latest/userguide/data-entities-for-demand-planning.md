

# Data Entities for Demand Planning
<a name="data-entities-for-demand-planning"></a>

The following table lists the data entities and columns used by Demand Planning.

## How to read the table:
<a name="data-entities-for-demand-planning-how-to-read"></a>
+ **Required** – The columns in this data entity are mandatory to execute a demand forecast without any failures.
+ **Conditionally required** – The columns in this data entity are required depending on the configurations set under demand plan settings.
+ **Recommended for forecast quality** – The columns in this data entity are required for the quality for the forecast.
+ **Optional** – The column name is optional. For enhanced feature output, it is recommended to add the column name with values.

## outbound\_order\_line (required)
<a name="data-entities-for-demand-planning-outbound-order-line"></a>

**How is this data entity used?** Demand Planning uses this data as the primary source of historical demand for forecast. Additionally, fields selected as granularity are sent for training and are available as filters to review the demand plan.


**outbound\_order\_line columns**  

<table>
<thead>
  <tr><th>Column</th><th>Is the column required?</th><th>How is this column used in Forecasting?</th></tr>
</thead>
<tbody>
  <tr><td>id</td><td>Required</td><td rowspan="3"><i>id</i>, <i>cust_order_id</i>, and <i>product_id</i> are used to uniquely identify a record in the data entity and this combination should always be unique. Make sure the column values do not have invalid characters such as asterisk and double-quotes.</td></tr>
  <tr><td>cust_order_id</td><td>Required</td></tr>
  <tr><td>product_id</td><td>Required</td></tr>
  <tr><td>order_date</td><td>Required</td><td>Required for forecast creation. Identifies the period for time-series forecasting.</td></tr>
  <tr><td>final_quantity_requested</td><td>Required</td><td>Required for forecast creation. Identifies the quantity used for time-series forecasting. This column must not contain null values and must be <i>numerical</i>. Make sure there are no commas in the values. For example, 500000.00 is an accepted value in Demand Planning.</td></tr>
  <tr><td>ship_from_site_id</td><td>Conditionally required</td><td rowspan="2">This column is conditionally required for forecast creation <i>if</i> the column is selected for forecast dimension (Site Hierarchy). This column must have a value and is used for filtering and analysis of data.</td></tr>
  <tr><td>ship_to_site_id</td><td>Conditionally required</td></tr>
  <tr><td>channel_id</td><td>Conditionally required</td><td>This column is conditionally required for forecast creation <i>if</i> the column is selected for forecast dimension (Channel Hierarchy). This column must have a value and is used for filtering and analysis of data.</td></tr>
  <tr><td>customer_tpartner_id</td><td>Conditionally required</td><td>This column is conditionally required for forecast creation <i>if</i> the column is selected for forecast dimension (Customer Hierarchy). This column must have a value and is used for filtering and analysis of data.</td></tr>
  <tr><td>ship_to_site_address_city</td><td>Conditionally required</td><td rowspan="3">This column is conditionally required for forecast creation <i>if</i> the column is selected for forecast dimension (Site Hierarchy). This column must have a value and is used for filtering and analysis of data.</td></tr>
  <tr><td>ship_to_site_address_state</td><td>Conditionally required</td></tr>
  <tr><td>ship_to_site_address_country</td><td>Conditionally required</td></tr>
  <tr><td>status</td><td>Recommended for forecast quality</td><td>This column is recommended for forecast quality. Orders with <i>canceled</i> status are not considered as forecast input.</td></tr>
</tbody>
</table>


## product (required)
<a name="data-entities-for-demand-planning-product"></a>

**How is this data entity used?**

Demand Planning uses the product attributes to establish hierarchy filters for demand plan review and for model training.


**product columns**  

<table>
<thead>
  <tr><th>Column</th><th>Is the column required?</th><th>How is this column used in Forecasting?</th></tr>
</thead>
<tbody>
  <tr><td>id</td><td>Required</td><td>Required for data ingestion into Supply Chain Data Lake (SCDL). Make sure the column values do not have duplicate IDs and special characters such as asterix and double-quotes.</td></tr>
  <tr><td>description</td><td>Required</td><td>Required for data ingestion into Supply Chain Data Lake (SCDL). This column can contain special characters such as asterix, hyphen, quotes, and double-quotes.</td></tr>
  <tr><td>parent_product_id</td><td>Conditionally required</td><td rowspan="5">This column is conditionally required for forecast creation <i>if</i> the column is selected for forecast dimensions (Product Hierarchy). Make sure the column has values and is used for filtering and analysis of data and model training.</td></tr>
  <tr><td>product_group_id</td><td>Conditionally required</td></tr>
  <tr><td>product_type</td><td>Conditionally required</td></tr>
  <tr><td>brand_name</td><td>Conditionally required</td></tr>
  <tr><td>color</td><td>Conditionally required</td></tr>
  <tr><td>display_desc</td><td>Conditionally required</td><td></td></tr>
  <tr><td>product_available_day</td><td>Recommended for forecast quality</td><td>Recommended. The value in this column improves forecast quality by allowing the forecasting model to consider the timing of new product introductions.</td></tr>
  <tr><td>discontinue_day</td><td>Recommended for forecast quality</td><td>Recommended. The value in this column improves forecast quality by allowing the forecasting model to consider the timing for product retirements.</td></tr>
  <tr><td>base_uom</td><td>Recommended for forecast quality</td><td>Unit of measure for product. Default is Eaches. Currently demand planning only supports Eaches.</td></tr>
  <tr><td>is_deleted</td><td>Recommended for forecast quality</td><td>Recommended. Enter <i>Y</i> if the product ID should be excluded from forecasting.</td></tr>
  <tr><td>pkg_height</td><td>Recommended for forecast quality</td><td rowspan="5">Recommended. The physical characteristics of the product that the forecasting models can understand.</td></tr>
  <tr><td>pkg_length</td><td>Recommended for forecast quality</td></tr>
  <tr><td>pkg_width</td><td>Recommended for forecast quality</td></tr>
  <tr><td>shipping_dimension</td><td>Recommended for forecast quality</td></tr>
  <tr><td>casepack_size</td><td>Recommended for forecast quality</td></tr>
</tbody>
</table>


## product\_alternate (Recommended for forecast quality)
<a name="data-entities-for-demand-planning-product-alternate"></a>

**How is this data entity used?**

Demand Planning uses the data of product's predecessor(s) or alternate(s) to create forecast for new products. When data is ingested into the *product\_alternate* data entity, Product lineage support for forecast is enabled. You can skip ingesting data into the *product\_alternate* data entity and the forecast can still be generated.


**product\_alternate columns**  

| Column | Is the column required? | How is this column used in Forecasting? | 
| --- | --- | --- | 
| alternative\_product\_id | Required | Required for data ingestion into Supply Chain Data Lake (SCDL). Unique record identifier. | 
| product\_id | Required | Required for data ingestion into Supply Chain Data Lake (SCDL). ID of the new product or new version of the product. Make sure *product\_id* is populated in the *product* data entity. | 
| product\_alternate\_id | Required | Required for data ingestion into SCDL. Identifier for a similar product or previous version of the product. To consider multiple similar products as a single *product\_id*, enter the products in separate rows. Make sure *product\_alternate\_id* is populated in the *product* data entity. | 
| alternate\_type | Required | Required for applying product supercession or lineage. Use the static value *similar\_demand\_product* in all the rows. | 
| alternate\_product\_qty | Required | Required for applying product supercession or lineage. Enter the proportion of history of the *alternate\_product\_id* you want to use for forecasting *product\_id*. For example, if it is 60%, enter 60. When you have multiple *alternative\_product\_id* for a single *product\_id*, the *alternate\_product\_qty* does not have to add up to 100. | 
| alternate\_product\_qty\_uom | Required | Required for applying product supercession or lineage. Use the specific static value "percentage". | 
| eff\_start\_date | Required | Required for data ingestion into SCDL. Enter the start timeframe to consider the history of a similar product. Make sure this date is on or before the *eff\_end\_date* or you can leave this field empty and Demand Planning will auto-fill the year with 1000. | 
| eff\_end\_date | Required | Required for data ingestion into SCDL. Enter the end timeframe to consider in history of a similar product. Make sure this date is on or after the *eff\_start\_date*. | 
| status | Recommended for forecast quality | Recommended. Enter *Inactive* to ignore the product supercession or lineage mapping. | 

## supplementary\_time\_series (recommended for forecast quality)
<a name="data-entities-for-demand-planning-supplementary-time-series"></a>

**How is this data entity used?** Demand Planning uses this data as the primary source for tagging casual factors such as promotional events, discounts, holidays, and so on.


**supplementary\_time\_series columns**  

| Column | Is the column required? | How is this column used in Forecasting? | 
| --- | --- | --- | 
| id | Required | Required for data ingestion into Supply Chain Data Lake (SCDL). Unique record identifier. | 
| order\_date | Required | Required for data ingestion into Supply Chain Data Lake (SCDL). Timestamp when the timeseries was recorded. | 
| time\_series\_name | Required | Required for data ingestion into Supply Chain Data Lake (SCDL). Name of the specific type of time series. The *time\_series\_name* column must start with a letter, be 2 to 56 characters long, and can contain letters, numbers, and underscores. No other special characters are allowed. | 
| time\_series\_value | Required | Required for data ingestion into SCDL. Value corresponding to the specific time series. Demand Planning only supports numerical input and time-series with categorical value is not considered. | 
| product\_id | Optional | Recommended. Unique identifier for a specific product. Use this column if the demand driver is available at product level. | 
| site\_id | Optional | Recommended. Unique identifier for a specific site or location. Use this column if the demand driver is available at site level. This column can represent either *ship\_from\_site\_id* or *ship\_to\_site\_id* based on the lowest level site hierarchy configuration. | 
| channel\_id | Optional | Recommended. Unique identifier for a specific channel. Use this column if the demand driver is available at channel level. | 
| customer\_tpartner\_id | Optional | Recommended. Unique identifier for a specific customer. Use this column if the demand driver is available at customer level. | 

## Historical vs. Future Supplementary Time Series: Understanding Covariates in Forecasting
<a name="data-entities-for-demand-planning-historical-vs-future-sts"></a>

Accurate demand forecasting requires understanding not just historical sales patterns, but the external factors that drive demand changes. Supplementary Time Series (STS) data—also called covariates—captures these demand drivers like promotions, pricing, holidays, and inventory levels, enabling forecasting models to distinguish explainable patterns from random noise and predict how future business actions will impact demand. However, a critical distinction exists between covariates that are only known historically (like past inventory levels or competitor actions) versus those known in advance (like planned promotions or scheduled holidays), and understanding this difference is essential for building accurate forecasts that support proactive planning decisions.

A critical distinction in demand forecasting is between **past covariates** and **known covariates** (also called future covariates). Understanding this difference is essential for building accurate forecasting models.

### Past Covariates (Historical STS Data)
<a name="data-entities-for-demand-planning-past-covariates"></a>

Past covariates are supplementary time series values that are only known for historical periods. These variables are observed alongside your historical demand but cannot be predicted or known in advance for future periods.

**Examples of Past Covariates:**
+ **Historical Inventory Availability**: You know what inventory levels were in the past, but future availability depends on demand, replenishment, and other uncertain factors
+ **Actual Competitor Pricing**: Historical competitor price data is observable, but future competitor actions are unknown
+ **Weather Conditions**: Past weather is recorded, but future weather (beyond short term forecasts) is uncertain
+ **Website Traffic**: Historical traffic patterns are known, but future traffic depends on many unpredictable factors

**Use in Forecasting Models:** Past covariates help the model learn historical relationships and patterns. For example, if high inventory availability historically correlated with higher sales (due to better product visibility or fulfillment speed), the model learns this relationship. However, since these values are unknown for future periods, the model must forecast without them or make assumptions about their future values.

### Known Covariates (Future STS Data)
<a name="data-entities-for-demand-planning-known-covariates"></a>

Known covariates are supplementary time series values that are known or can be determined in advance for future periods. These are the most valuable inputs for forecasting because they provide concrete information about future conditions.

**Examples of Known Covariates:**
+ **Planned Promotional Discounts**: Your marketing team has already scheduled promotional campaigns with specific discount levels for future dates
+ **Price Index Changes**: Planned price adjustments are determined in advance based on your pricing strategy
+ **Holiday Indicators**: Calendar based events (holidays, shopping seasons, fiscal periods) are known years in advance
+ **Planned Marketing Spend**: Budget allocations and campaign schedules are predetermined
+ **Store Opening/Closing Events**: Expansion or consolidation plans are known ahead of time

**Use in Forecasting Models:** Known covariates dramatically improve forecast accuracy because the model can incorporate actual future conditions rather than assumptions. For example, if you know a 25% discount promotion is planned for next month, the model can predict the expected demand lift based on historical discount response patterns.

### Practical Implementation Strategy
<a name="data-entities-for-demand-planning-practical-implementation"></a>

**For Historical Periods (Training Data):** Include both past covariates and known covariates in your supplementary time series data. This allows the model to learn relationships from all available demand drivers. Your dataset should contain actual observed values for all time series types up to the present date.

**For Future Periods (Forecasting Horizon):** Only include known covariates in your supplementary time series data. These are the demand drivers you can confidently specify for future dates. For example:

```
id,order_date,time_series_name,time_series_value,product_id,site_id,channel_id,customer_tpartner_id
        1001,2025-02-01,discount_percentage,20.0,PROD_001,SITE_NYC,CHANNEL_ONLINE,CUST_12345
        1002,2025-02-14,discount_percentage,30.0,PROD_001,SITE_NYC,CHANNEL_ONLINE,CUST_12345
        1003,2025-02-01,holiday_indicator,0,PROD_001,SITE_NYC,CHANNEL_ONLINE,CUST_12345
        1004,2025-02-14,holiday_indicator,1,PROD_001,SITE_NYC,CHANNEL_ONLINE,CUST_12345
```

This future data tells the model that a 20% discount is planned for February 1st and a 30% Valentine's Day promotion is scheduled for February 14th.

## Practical Applications
<a name="data-entities-for-demand-planning-practical-applications"></a>
+ **Promotional Planning**: Track discount percentages over time to understand how promotional intensity affects demand. This helps identify optimal discount levels and predict the demand lift from future promotions.
+ **Price Elasticity Analysis**: Monitor price index movements to quantify how price changes influence customer purchasing behavior across different products, locations, and channels.
+ **Inventory Constraint Modeling**: Capture inventory availability levels to identify when stockouts or low inventory constrained sales, ensuring forecasts account for supply limitations rather than true demand signals.

## Benefits for Demand Planning
<a name="data-entities-for-demand-planning-benefits"></a>

By incorporating supplementary time series data, your Demand Planning system can:
+ **Improve Forecast Accuracy**: Account for known demand drivers rather than treating them as unexplained variance
+ **Enable Scenario Planning**: Model "what if" scenarios by adjusting future values of demand drivers
+ **Identify Causal Relationships**: Understand which factors most significantly impact demand for different products and markets
+ **Support Strategic Decisions**: Provide data driven insights for pricing, promotional, and inventory strategies