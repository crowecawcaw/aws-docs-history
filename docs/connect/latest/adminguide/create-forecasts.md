# Create forecasts in Amazon Connect

Forecasts are a projection of the workload in your contact center. Amazon Connect provides
long-term and short-term forecasts for you to generate capacity plans and agent
schedules. The forecasts include inbound, transfer, and callback contacts in both
voice and chat channels.

After creating a forecast, you do not need to generate it manually.

- Long-term forecasts are generated for 64 weeks and automatically updated
  weekly.
- Short-term forecasts are generated for 18 weeks and automatically updated
  daily.
- Every forecast is computed using the most current contact data.
- The models for short-term and long-term forecasts are retrained on a
  weekly and monthly basis, respectively, to incorporate the latest contact
  patterns.
- You can delete forecasts. However, downstream capacity plans and schedules
  created based on the forecasts are impacted.

###### To create a forecast

1. Before creating a forecast, you must create at least one forecast group.
   If you haven't done that, see [Create forecast
   groups](create-forecast-groups.md "create-forecast-groups.md"). We strongly recommend
   creating all of your forecast groups before creating any forecasts.
2. Log in to the Amazon Connect admin website with an account that has security profile permissions
   for **Analytics**, **Forecasting - Edit**.

For more information, see [Assign
permissions](required-optimization-permissions.md "required-optimization-permissions.md"). 3. On the Amazon Connect navigation menu, select **Analytics and
optimization**, **Forecasting**. 4. Select the **Forecast** tab, and then choose
**Create Forecast**. 5. On the **Create Forecast** page, choose the forecast
groups.

![The Create forecast page, the Forecast groups dropdown menu.](images/wfm-forecasting-create-forecast.png) 6. Choose the forecast type. Amazon Connect creates a forecast for each type you
select.

    * **Long-term** forecasts are used for capacity
     planning. For example, how many Full Time Equivalent (FTE) agents
     you need to hire in the next few months, quarter, and year.
    * **Short-term** forecasts are used for scheduling
     agents and interval level agent headcount estimation.

7. Choose **Save**. If the forecast group has already been
   included in a forecast, an error message is displayed.
8. If the forecast was created successfully, it's Status =
   **Scheduled**.

The status is **Complete** when the computation
finishes. You can use **Search** to find forecasts by
forecast group name. 9. Amazon Connect creates a forecast for each forecast type, as shown in the following
image.

![A list of forecasts, short-term and long-term.](images/wfm-forecasting-types.png)
