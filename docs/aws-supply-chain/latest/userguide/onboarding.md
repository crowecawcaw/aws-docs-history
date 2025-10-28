# Create your first demand plan

When you log into Demand Planning for the first time, you will be able to view the onboarding pages that highlight
key product features and help you get familiar with the Demand Planning capabilities.

**Overview of the process:**

To create your first forecast, from the left navigation bar, choose **Demand
Planning**, **Manage Demand Plan**, and **Create
forecast**. The system guides you through the following steps. For more
information, see [Role-based access control](rolebased.md "rolebased.md").

1.  _Data ingestion_ – Before proceeding with configuration, the
    system verifies that required datasets are ingested into Data Lake. You need the
    following, at minimum. For more information about which table and columns are used by
    Demand Planning, including prerequisites, see [Demand Planning](required_entities.md "required_entities.md").
    - Required: Outbound Order Line and Product data
    - Recommended: Product Alternate and Supplementary Time Series data

2.  _Plan configuration_ – After data ingestion is complete,
    you'll configure various aspects of your demand plan, including forecast dimensions, time
    frames, settings, and scheduling options. After Demand Planning is configured, you can
    view or modify the demand plan configuration settings by choosing
    **Settings**, **Organization**, and **Demand
    Planning**.
3.  _Plan creation_ – After configuration, choosing
    **Generate Forecast** initiates three sub-processes:

        * Data Validation: System validates data quality and completeness
        * Demand Pattern Analysis & Recommendations: System analyzes historical patterns
         and provides insights
        * Forecast Creation: System generates the forecast

    In an ideal scenario, where no data validation errors are found, the system smoothly
    proceeds through all three steps, creating both the demand pattern analysis report and
    forecast. However, if any data validation errors are detected, the system halts both the
    forecast creation and demand pattern analysis until the errors are resolved. Work with
    your data administrator to correct the underlying data issues, and choose
    **Retry** to try forecast creation again.

4.  On the **Configure Demand Planning** page, there are five steps to
    configure Demand Planning.
    - **Scope** – Defines the dimensions and the
      time frame for Demand Planning to generate forecasts.
    - **Configure your dataset** – Defines the
      outbound_order_line dataset. This option is mandatory for Demand Planning to generate
      an accurate forecast. You also define how you want Demand Planning to handle negative
      quantity values in the outbound_order_line dataset. For more information about
      mandatory and optional Demand Planning fields, see [Data entities and columns used in AWS Supply Chain](data-model.md "data-model.md").
    - **Forecast Settings** – Set global parameters
      to determine the forecast period, minimum forecast value, and initialization values
      for new products with no alternate data.
    - **Scheduler** – You can define how and when
      forecasts should be refreshed and published.
    - **Organization Settings** – Defines where your
      Demand Plans will be published. It also shows other configuration options within the
      application.

5.  Under **Scope**, **Planning Horizon**, select the
    following:

        * **Time Interval** – Select the time interval
         from the choice of daily, weekly, monthly, or yearly options. The time interval is
         used to aggregate and analyze data. Choose a time interval based on the nature of your
         business, availability, and granularity of historical data.
        * **Time Horizon** – Time horizon is the
         specific period for when a forecast is generated. The value should be a whole number
         with a minimum value of 1 and maximum of 500. The amount of historical data available
         also will dictate the Time Horizon. Make sure that at least one product in the
         outbound\_order\_line dataset has sales history at least four times the time horizon
         set. For example, if you set **Time Horizon** to 26 and
         **Time Interval** as *weekly*, the
         minimum order data requirement is 26\*4 = 104 weeks.

    Under **Forecast Granularity**, **Required
    Hierarchy**, select the parameters to define your forecast hierarchy. Product
    ID attribute is mandatory and is automatically selected as the last level in the
    hierarchy. You can choose **Add level** to add additional hierarchy
    levels between product_group_id, product_type, brand_name, color, display_desc, and
    parent_product_id. Make sure that the required hierarchy attributes have information in
    the product dataset, because you can use these attributes to filter the demand
    plan.

Under **Optional Hierarchy**, choose **Add level**
to add up to five attributes from **Site**, **Channel**,
and **Customer** to better manage your forecast. The supported columns
from the _outbound_order_line_ dataset are:

    * Site hierarchy = ship\_from\_site\_id, ship\_to\_site\_id, ship\_to\_site\_address\_city,
     ship\_to\_address\_state, ship\_to\_address\_country
    * Channel hierarchy = channel\_id
    * Customer hierarchy = customer\_tpartner\_id

Make sure that the required hierarchy attributes have information in the product
dataset since these attributes are used to filter demand plans. 3. Choose **Continue**. 4. On the **Configure your dataset** page, under **Configure
Forecast Input**, you should configure the required and recommended
datasets.

###### Note

AWS Supply Chain recommends uploading two to three years of outbound order line
history as an input to generate an accurate forecast. This duration allows the
forecasting models to capture your business cycles and ensure a more robust and reliable
prediction. For improved forecast accuracy, it is also recommended to include product
attributes such as _brand_, _product_group_id_,
and _price_ in the product dataset.

    * Required Datasets – The *outbound\_order\_line* and
     *product* data entities are required to generate a
     forecast.
    * Recommended Datasets – The *product\_alternate* and
     *supplementary\_time\_series* data entities are optional. You can
     generate a forecast without these data entities but when provided, the forecast
     quality will be improved.

5.  Under **Required Datasets**, expand **Historical
    Demand** and choose **Configure** to set the negative value
    for missing data. _outbound_order_line_ dataset is the primary source
    of historical demand.
    - **Ignore** – Select if you want
      AWS Supply Chain to ignore the products with missing order_date before creating the
      forecast.
    - **Replace with zero** – Select if you want
      AWS Supply Chain to replace the missing order_date fields with zero by default to the
      final requested quantity.

6.  No additional configuration is required for _product_ data entity.
    Product attributes are used for filters, configure hierarchy, and for training the
    learning model.
7.  Under **Recommended Datasets**, no additional configuration is
    required for _product_lineage_. You can use the
    _product_alternate_ data entity to provide information on alternate
    or previous version of the product. For more information on product lineage, see [Product lineage](product_lineage.md "product_lineage.md").
8.  Select **Demand Drivers** if you have demand drivers information such
    as promotions, price changes, and so on, you can use
    _supplementary_time_series_ data entity to ingest data. You can
    select up to 13 demand drivers and configure aggregation and missing data filling
    strategy. For more information on demand drivers, see [Forecast based on demand drivers](demand_drivers.md "demand_drivers.md").
9.  Choose **Continue**.
10. On the **Forecast Settings** page, you need to configure the
    following:
    - Choose the forecast model/ensembler for the plan. AWS Supply Chain Demand
      Planning has a default forecast model assigned for the demand plan. Customers have the
      ability to change the default if they choose to.

    ###### Note

    The AWS Supply Chain assigned default model will be used if the user does not
    change the selection.
    - Under **Forecast Start Date**, enter the forecast start date to
      start the planning cycle.
      - Max History Date – Select this option if you want to start forecasting
        from the next time period after the last complete historical data point.
      - Plan Execution Date – Demand Planning uses this date when the forecast
        is triggered as the start of the planning cycle.
      - Custom Date – Select this option when the selected forecast start date
        is later than the outbound_order_line dataset end date then the default planning
        cycle start date is considered. If the selected forecast start date is before the
        outbound_order_line start date or if the length of the demand history is
        insufficient, the forecast will fail and display an error. For more information,
        see [Prequisites before uploading your dataset](data_quality.md "data_quality.md"). It is recommended
        to select the first of the month for monthly intervals or Monday for weekly
        intervals. If you choose a different date, Demand Planning will automatically
        adjust to the nearest default date. For example, if you selected Wednesday as the
        forecast start date, Demand Planning will select the next Monday as the forecast
        start date for weekly intervals. Similarly, selecting May 10th 2024 will result in
        June 1st 2024 as the planning cycle start date for monthly intervals.

    - Under **Handling Partial History and Filling Strategy**, select
      one of the following:
      - Trim Partial History – Select this option to trim the partial history.
        For example, the illustration below explains how trim partial history works for
        the following settings:
        - Weekly granularity start period – Monday (default Demand Planning
          setting)
        - Monthly granularity start period – 1st of the Gregorian Calendar
          Month (default Demand Planning setting)
        - Demand plan granularity – Weekly
        - Forecast start date– Plan run date
        - Trim partial history – Set to _Yes_
        - Plan run date – Set to _Monday_
        - Forecast horizon – Four weeks

      ![Trim partial history example](images/Trim_history.png)
      - Include Partial History – Select this option to include the partial
        history and use a filling strategy to fill the gaps.

      For example, if you are forecasting at a monthly level and your last month in
      history has only 10 days of data, you can choose to trim or exclude the 10 days of
      data. If you choose not to trim or exclude the 10 days of data, you can select a
      filling strategy to fill data for the rest of the month.

          - Zero – Use this filling method when no sales activity is expected
           for certain periods. Impact: May lead to lower forecast, best for seasonal
           data with expected zero demand
          - NaN – Use this filling method when marking data is missing.
          - Mean – Use this filling method when smoothing out
           fluctuations.
          - Median – Use this filling method when minimizing the influence of
           outliers or data skewness.
          - Min – Use this filling method when representing the lowest possible
           value for conservative forecasting.
          - Max – Use this filling method when assuming the highest possible
           value for optimistic forecasting Impact.

    - Under **Configure Forecast Periods in...**, select the start and
      end dates for New Product Introduction (NPI) and End-of-life EOL) products. For more
      information, see [Product lifecycle](product_lifecycle.md "product_lifecycle.md").
    - Under **New Product Initial Forecast**, enter an initial forecast
      value for products with no demand history or product lineage to make the products
      searchable in the demand plan web application and to create a forecast. Specify the
      value and the periods to apply.

    ###### Note

    The time period displayed will depend on the time period you chose under
    **Time intervals** in the **Planning Horizon**
    page. For example, if you chose _Monthly_ under **Time
    intervals**, you will be able to specify the number of months before or
    after to start and stop the forecast, and for products with no demand
    history.
    - The planning cycle start date is based on the last order date in the outbound
      order line dataset. If the time interval configuration is:
      - **Daily** – Planning cycle start date will
        be the day after the last order date. For example, if the last order date is
        October 30, 2023, the planning cycle start date will be October 31, 2023.
      - **Weekly or Monthly** – When the last
        order date is the same as the time boundary, the planning cycle start date will be
        after a week or month. For example, when the last order date is October 29, 2023
        (which is a Sunday and Demand Planning's week time boundary), the planning cycle
        start date will be October 30, 2023.

      When the last order date falls within the time boundary, Demand Planning will
      trim the order history for the last time window and create forecast from the new
      period. For example, when the last order date is November 01, 2023 (which is a
      Wednesday and not in the Demand Planning's week time boundary), the planning cycle
      start date will be October 30, 2023. Demand Planning will ignore the order history
      from October 30, 2023 to November 01, 2023.

    - Under **Accuracy Metrics Preferences**, setup three different
      lags for your organization.

11. Choose **Continue**.
12. On the **Demand Plan Publish Scheduler** page, under **How do
    you like to manage ongoing forecast refresh and demand plan release?**, choose
    **Auto** to view your next forecast plan published on the Demand
    Planning page.

Under **Set the release frequency for the final demand plan**, choose
the frequency at which you want to publish the demand plans to the downstream processes
and close the planning cycle.

(Optional) Under **Set the intra-cycle forecast refresh frequency**,
select the frequency of the forecast update within the same planning cycle without
releasing the interim updates to the downstream processes or closing the planning cycle.
You can also select **None** to opt-out of intra-cycle forecast refresh
frequency. 13. Choose **Continue**. 14. Under **Organization Settings**, note the Amazon Simple Storage Service (Amazon S3) path where
the demand plans are published.

###### Note

You can also find the Amazon S3 path for the published demand plans on the
**Settings** page. For more information, see [Manage Demand Plan settings](settings.md "settings.md").

Forecast is generated only when you ingest data into AWS Supply Chain. Make sure that
all the required and optional attributes that you chose have information in the
dataset.
