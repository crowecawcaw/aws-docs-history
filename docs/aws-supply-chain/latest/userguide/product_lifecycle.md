# Product lifecycle

Product lifecycle describes the lifecycle of a product from introduction to End of Life
(EoL). AWS Supply Chain supports forecasting products through it's lifecycle. To enable the
Product lifecycle feature, populate the _product_introduction_day_ and
_discontinue_day_ columns in the _Product_ data
entity. Demand Planning uses the data from these columns to create forecast for a product when
the product is active. For more information data entities, see [Data entities and columns used in AWS Supply Chain](data-model.md "data-model.md").

To enable product lifecycle, make sure the columns _id_,
_description_, _product_available_day_,
_discontinue_day_, and _is_deleted_ are populated in
the _Product_ data entity.

The example below displays how Demand Planning works when data is ingested in the Product
data entity.

| Column name           | Required for Data Lake | Required for Demand Planning | Scenario 1                                                                                                                                                      | Scenario 2                                                                                                                              | Scenario 3                                                             | Scenario 4                                                | Scenario 5                          | Scenario 6                                    | Scenario 7                                                                            |
| --------------------- | ---------------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------- | ----------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------- |
| id                    | Yes                    | Yes                          | Product123                                                                                                                                                      | Product123                                                                                                                              | Product123                                                             | Product123                                                | Product123                          | Product123                                    | Product123                                                                            |
| description           | Yes                    | Yes                          | Bottle                                                                                                                                                          | Bottle                                                                                                                                  | Bottle                                                                 | Bottle                                                    | Bottle                              | Bottle                                        | Bottle                                                                                |
| product_available_day | No                     | No                           | May 1, 2023                                                                                                                                                     | May 1, 2023                                                                                                                             | May 1, 2023                                                            | Null                                                      | Null                                | May 1, 2022                                   | May 1, 2022                                                                           |
| discontinue_day       | No                     | No                           | Null                                                                                                                                                            | December 31, 2023                                                                                                                       | December 31, 2023                                                      | Null                                                      | Null                                | May 1, 2023                                   | Past                                                                                  |
| is_deleted            | No                     | No                           | No                                                                                                                                                              | No                                                                                                                                      | Yes                                                                    | No                                                        | Null                                | No                                            | No                                                                                    |
| **Expected behavior** | NA                     | NA                           | Forecast will be created starting 3 months prior (or as configured) prior to May 1, 2023 to the end of the planning horizon since there is no discontinue date. | Forecast will be created starting 3 months prior (or as configured) prior to May 1, 2023 until the discontinue date (or as configured). | Forecast will not be created since the product is considered inactive. | Forecast will be created for the entire planning horizon. | Assumed that the product is active. | Forecast will be created for one day (May 1). | In case of conflict between is_deleted and discontinue_day, is_deleted is considered. |

For information on how to configure Product lifecycle, see [Create your first demand plan](onboarding.md "onboarding.md").

Under Demand Planning settings, you can set your forecast start date depending on the
_product_available_day_ in the Product data entity. By default, the
forecast starts on the _product_available_day_. _Period_
refers to the time interval set under **Scope** (daily, weekly, monthly, or
yearly). You can adjust the start date to optimize inventory management.

Similar to start date, you can set an end date for your forecast depending on the
_product_discontinue_day_ in the Product data entity. By default,
forecast will end on the _product_discontinue_day_. You can adjust the end
date to prevent inaccurate forecasting beyond the product shelf life and avoid excess
inventory cost. Enter zero if you want the forecast to match the
_product_available_day_ and _product_discontinue_day_.
This global setting will apply to all eligible products.

When _product_available_day_ and
_product_discontinue_day_ are not available, the forecast is created for
the entire planning horizon.

You can also configure your system to initialize forecast values for products without
historical data or alternate product links. The default value is zero. You can also set the
period until which your system should use the initialize product forecast value based on the
time interval set under **Scope** (daily, weekly, monthly, or yearly). The
default value is three periods. This global setting will apply to all eligible products at the
intersection of site, customer and channel dimensions, if they are selected as additional
forecast granularity. For example, when forecast is set to weekly with an initialized value of
10 for 12 periods, and the start forecast is set to three periods before the
_product_available_day_, for a Product X with October 2, 2023
product_available_date, the initialized value of 10 will be applied for each week from
September 11, 2023 to December 3, 2023.

To change the _product_available_day_ and
_product_discontinue_day_, update the Product data entity in
AWS Supply Chain data lake. You can also update the forecast start and stop date. When you
change the initialization value and period settings, the changes are applied to all eligible
products, including those which were initialized with a different value in the previous
planning cycles. All the updates are applied to the next forecast creation cycle.
