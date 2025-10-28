# Demand plan

After the forecast is generated, you can review the forecast values on the **Demand Plan** tab. The
**Enterprise demand plan** is a single workbook that serves as
a collaborative platform to work together. It provides a centralized location for you to
consolidate and synchronize the forecasting effort.

The Demand Plan table displays the following information:

- **Forecasted Demand** – Displays the system
  generated forecast and includes the following three values:
  - **Lower Bound** – Forecast prediction that is
    typically higher than the actual demand around 90 percent of the time.
  - **Median Demand** – Forecast prediction that
    is typically higher than the actual demand 50 percent of the time (central
    estimate).
  - **Upper Bound** – Forecast prediction that is
    typically higher than the actual demand 10 percent of the time.

  ###### Note

  _Lower and Upper Bound_ information is only displayed when a
  _product_id_ is selected. _Median Demand_ is
  displayed at both aggregate level and when a single _product id_
  is selected.

- **Demand Plan** – Median Demand is replicated in
  this row to allow for overrides.
- **Actual Demand** – Displays demand history for
  the current and prior years.

When comparing historical data on a weekly basis, Demand Planning will reference the
closest Monday in the previous year. This is because Demand Planning considers Monday as
the starting day of the week. Due to variations between years and leap years, the
corresponding week in the previous year might not have the exact same date. For example,
to compare if historical sales data for the week of 6/3/2023 is available, which is a
Monday, Demand Planning will reference the week with the closest Monday in the previous
year, which is 7/2/2022.

- **Prior Forecast Versions** – The last published
  demand plan displays. This will be blank during the first forecast creation because no
  history is available.
- **Lifecycle and Events** – Displays the products
  in the demand plan that are New Product Introductions (NPI) or products that are nearing
  End of Life (EoL). When you hover over the **NPI** or
  **EoL** icons, when more than one product is selected, you can view the
  number of products and the list of products. When only one product is selected, you can
  view the product metadata. , product available day in case of NPI, discontinue day in case
  of EoL, and forecast start and stop date.

###### Note

You will only see the number of products that are new or nearing EoL listed when the
product category is set to all or when a higher level in product hierarchy is
selected.
You can use the **Graph** toggle button to hide or show the graph view.
You can hide or show the specific value by choosing the eye icon. When you filter by products,
you can hover over the _i_ help icon to view the product description, unit
of measure (UoM), product available date, and discontinue date.

## Viewing the forecast

To view the forecast, complete the following steps:

1. On the **Enterprise demand plan** page, you can see the timestamp of
   the forecast generated. If the **Enterprise demand plan** is in
   _active_ state, you can use the filters and make adjustments.
2. On the **Enterprise demand plan** page, under
   **All**, choose **Change category/product** to change
   the generated forecast view. By default, the forecast displayed represents the total
   forecast demand for all products within the defined scope or time horizon.
3. On the **Select Category/Product** page, you can select the product
   from the list or use the search box to search for a particular product by
   _Product ID_ or _Description_.
4. Choose **Apply**. You can now view the filtered forecast for the
   selected product or category.

###### Note

If you had chosen optional hierarchies during forecast configuration, the summary
box will display the count of site, customer, and channel the selected product is
sold. 5. Under **Refine your search**, if you chose optional hierarchies
during forecast configuration, you can filter for **Site**,
**Channel**, or **Customer** to further refine your
forecast. For example, if you chose **Site** and
**Channel** hierarchy during forecast configuration, the filters for
Site and Channel will be available on the **Demand Plan**
page. 6. In the **Time interval** dropdown list, select the time interval to
view the forecast. You can use this filter to adjust the time hierarchy and view the
forecast in both table and graph form. The lowest value corresponds to the forecast
granularity time interval setting. For example, if the time interval is
_Weekly_, you can view the forecast at _Weekly_,
_Monthly_ and _Yearly_.

You can also use the **Viewing window start** and
**Viewing window end** to narrow down the period that you want to
view in the forecast, both in table and graph view. You can view the historical sales for 28 days, 52 weeks, 48 months, and 10 years.

**Time interval example 1**

Demand Plan is generated at daily time-intervals per configuration. You can view the
Demand Plan at weekly time interval by selecting the option on the Time Interval filter on the
Demand Plan page. The system will aggregate values into weeks with Monday as the starting day
of the week.

You can also view the demand plan in monthly time interval by using the Time Interval
filter and selecting the monthly option. System will aggregate values into Gregorian calendar
month with start day as 1, because demand plan is available at daily granularity.

![Time interval example](images/Time-interval-example1.png)
**Time interval example 2**

Demand plan is generated at weekly time-interval per configuration. You can view the
Demand plan at monthly time interval by selecting the Time Interval filter. The time
boundaries for month will not be strict Gregorian calendar month.

![Time interval example](images/Time_interval_example.png)

## Adding an override

This section describes how to manually edit the forecast to override the projected
demand.

###### Note

Manual forecast overrides from one planning cycle are automatically saved and reapplied
on the next planning cycle.

1. Under **Demand Plan**, you can add overrides on the graph by moving
   the dot to the desired value or update the values directly on the Demand Plan row in the table.
2. On the **Edit Quantity** page, under **Change**,
   select if you want to increase, decrease, or fixed amount the demand.
3. Choose **Bulk edit** to bulk edit the forecast and add an override.

The **Edit your forecast** page appears. 4. Under **Change**, select the dropdown to increase or decrease
the demand, or enter a value. 5. Under **Reason Code**, select from one of the options between
_Promotion_, _Holiday_,
_Seasonal_, _New Product_, _Product
Rampdown_ or _Others_. The reason code is mandatory to
successfully process the override. It is optional to add more descriptive notes to a
forecast override. 6. Choose **Save and Update**.

When you create an override, the impact can be viewed throughout the relevant levels
of hierarchies. You can create many overrides but only the last override will be
considered. After an override is created, a _clock_ icon
appears under **Demand Plan**. When you choose the
_clock_ icon, you can view the most recent change in the planning
cycle. Choose **View more changes** to view past updates. 7. To make multiple overrides at the same time, from the **Edit
Quantity**, choose **Go to bulk editing**. You can also choose
**Bulk Edit** against **Demand Plan**.

###### Note

You can bulk edit only from the table. 8. On the **Edit your forecast** page, you can select all check boxes or
a check box for each time period that you want to update, and then enter the
updates. 9. Choose **Save and Update**.

The **Forecasted Demand** is updated.

## Exporting data plan files

You can export **Demand Plan**, **Forecast Demand**, **Prior Forecast Versions**, and
**Actual Demand History** from Demand Planning as individual
.csv files.

###### Note

The exported .csv file will contain the entire demand plan, despite which filters were
active on the **Demand Planning** page at the time of
export.

To export the data plan, complete the following steps:

1. On the **Enterprise demand plan** page, select the vertical ellipsis.
2. Choose **Export Data Plan**.

![Exporting data plans](images/export_data_plan.png) 3. On the **Export** page, select the required data you would like to download. 4. Choose **Export**.

The file is downloaded on your local computer.

## Importing forecast overrides

You can use the import forecast overrides option to import the forecast overrides using a .csv file.

To upload the forecast overrides through a .csv file, complete the following steps:

1. On the **Enterprise demand plan** page, select the vertical ellipsis.
2. Choose **Import Forecast Overrides**.

The **Import Forecast Overrides** page appears.

![Importing forecast overrides](images/import_forecast_overrides.png) 3. Under **Upload files**, choose **Download CSV template** to download the .csv file you need to use to add the override values.

The .csv file will contain the headers from the dataset you used to generate the forecast. The .csv file can only contain upto 1000 rows and the file size should be within 5 MB. 4. After the .csv file is updated, you can drag and drop the files or choose **select files** to add the file. 5. Choose **Upload overrides**.

If the upload fails, check the following:

    * Make sure the required fields *override\_start\_date*, *override\_end\_date*, *value*, and *reason\_code* are populated.
    * The supported reason codes are *Promotion* *Holiday*, *Seasonal*, *New Product*, *Product Rampdown*, and *Others*.
    * Make sure the *override\_start\_date* and *override\_end\_date* is the first day of the week or month depending on your configuration.

6. Under **Import Forecast Overrides Status**, you will see the status of all the forecast overrides you uploaded.

You can filter the forecast override status by **Data Uploaded**, **User ID**, or upload status.

## Demand Plan scheduler

Schedulers in Demand Planning determine when forecasts are generated and demand plans are finalized. Schedulers can be configured to operate automatically at set time
intervals (auto schedulers) or triggered manually. Auto-schedulers ensure that the planning process runs smoothly and consistently accordingly to predefined timelines, while manual
schedulers gives you the flexibility to initiate forecast refreshes and finalize demand plans.

- Manual refresh and release – Make sure you choose **Manual** under **Demand Plan Scheduler** when you configure demand planning. To start
  a forecast refresh, on the **Demand Plan** page, select the three dots on the top-right, and choose **Generate Forecast**.

Select **Finalize demand plan**, if the demand plan is final and ready to be released to downstream processes.

Once the demand plan is final, the information is published to the _Forecast_ data entity in Data Lake and to Amazon S3. The status on the demand plan page for this plan is changed to _Published_. You can view the Amazon S3 link under _Settings_ > _Organization_, _Demand Planning_, _Publish Demand Plans_.
You can see the **Generate forecast** button to start the next planning cycle.

When the **Finalize demand plan** is not selected, Demand Planning will publish the forecast as an interim version to the _Forecast_ data entity
in Data Lake. The status is changed to _Closed_. You can see the **Generate forecast** button to start the next planning cycle. Demand planning will initiate a new forecast as set in the demand planning configuration page and will use the same start date as the previous plan.

- Automatic refresh and release – Make sure you choose **Auto** under **Demand Plan Scheduler** when you configure demand planning. For more information, see [Create your first demand plan](onboarding.md "onboarding.md").
