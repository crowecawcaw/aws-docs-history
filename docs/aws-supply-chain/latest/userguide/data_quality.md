# Prequisites before uploading your dataset

To successfully generate a forecast, make sure your dataset adheres to the following.

- At least one _product_id_ has a sales history of at least four times the forecast time horizon provided in the _outbound_order_line_ dataset. For example, if the forecast time horizon is 26 weeks, the minimum order data requirement is 26\*4 = 104 weeks.
- _Product_id_ under the product data entity should not contain any incomplete data (null or empty string) or duplicates.
- All the additional columns selected for granularity in the forecast configuration (that are _conditionally required_ ‘) does not contain incomplete data (null or empty string).
- The column _id_ across all data entities (for example, product_id, site_id, ship_from_site_id) does not contain special characters, such as asterisk (\*) and double quotes (" ").
- The _order_date_ does not contain invalid date. For example, 2/29/2023, that is 29th February 2023 is only valid on a leap year.
  To improve forecast accuracy, Demand Planning highly recommends the following.

- Upload two to three years of outbound order line history as input to generate an accurate forecast. This duration allows the forecasting models to capture your business cycles and ensure a more robust and reliable prediction.
- For improved forecast accuracy, it is also recommended to include product attributes such as _brand_, _color_, _product_group_id_, _product_introduction_day_ and _discontinue_day_ in the product data entity.
- You can provide additional demand drivers information through the _supplementary_time_series_ data entity. Note, only numerical values are supported.
- You provide alternate product mapping when you have similar products or previous version for a new product.
- Remove any non-recurring or one-time event such as COVID before uploading the historical sales data.
