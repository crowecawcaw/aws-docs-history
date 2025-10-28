# Lead time deviations and recommendations

For every generated lead time insight, you can select a row to view the historical trend on the vendor's performance on delivering products from a given ship location to the destination location.

For all orders that are in progress, you can view the status of the order and anticipate the delivery date. Insights uses a machine learning model trained on historical data spanning 1 to 5 years,
a time frame chosen during the watchlist creation process, to provide predicted delivery dates with varying levels of confidence.

The **Historical Orders** graph displays the historical average lead times by month calculated from historical order data based on
submitted and delivery dates. The bar graphs represent the current planned lead time value and the recommended lead time for
vendors at specific sites for the given products. The actual lead time for future orders will be equal or lower than the recommended lead time 50% of the time.

The **Upcoming Orders** graph displays the future purchase order lead times by day, calculated by viewing the order’s submitted date and
delivery dates. The bar graphs represent the current planned lead time value and the recommended lead time for
vendors at specific sites for the given products. The actual lead time for future orders will be equal or lower than the recommended lead time 50% of the time.

The **Orders in Progress** table displays detailed information of the current or upcoming purchase orders that are at risk based on the model
predictions from the historical data for the given vendor, product, and site. The table displays the granular view of all open orders with details such as order quantity, the expected or planned delivery date available from the order
line data, and Insights predicted delivery dates with multiple options categorized as _Estimated - Low_ and _Estimated - High_. The _deviation_ determines the disparity between the estimated high dates and the actual delivery dates available at the order line level.

###### Note

The x-axis in the Historical Orders chart shows months according to the UTC timezone regardless of your location. This means that the beginning of the month coincides with 00h:00m:00s UTC
of the first day of the month and the end of the month coincides with 23h:59m:59s UTC of the last day of the month.
