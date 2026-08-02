# Create capacity plans using forecasts and scenarios in Connect Customer

Before you can create a capacity plan, you must create a planning scenario and
publish the forecasts required for your plan type. Hiring plans require a published
long-term forecast and a published short-term forecast. Scheduling plans require only
a published short-term forecast. For more information, see [Forecast requirements by plan type](capacity-planning-plan-types.md#capacity-planning-plan-types-forecast-requirements "capacity-planning-plan-types.md#capacity-planning-plan-types-forecast-requirements").

Connect Customer uses the forecasts and planning scenarios as inputs for creating the capacity
plan. If you haven't yet created a forecast and planning scenario, see [Getting started with forecasting](forecasting.md#getting-started-forecasting "forecasting.md#getting-started-forecasting") and [Create capacity planning scenarios in Connect Customer](capacity-planning-create-scenarios.md "capacity-planning-create-scenarios.md").

## How to create a capacity plan

1. Navigate to the **Capacity Plans** tab, and choose
   **Generate Plan**.
2. For **Plan type**, choose the type of capacity plan
   to generate:

   - Choose **Hiring plan** for long-term FTE
     estimates focused on hiring requirements. This requires a
     forecast group with both published long-term and short-term
     forecasts.
   - Choose **Scheduling plan** for
     interval-level headcount requirements focused on scheduling and
     resource allocation. This requires a forecast group with a
     published short-term forecast only. The plan start and end dates
     must fall within the short-term forecast date range.
     For both plan types, you can enter a total shrinkage percentage in the
     **Shrinkage** field in the **Scenario
     inputs** section. For more information, see [Create capacity
     planning scenarios](capacity-planning-create-scenarios.md "capacity-planning-create-scenarios.md").

3. Provide the plan name, description, forecast group (which has the
   published forecasts required for your selected plan type), start/end
   date, and plan scenario. The following image shows example values for
   these fields.

![The Generate Plan page showing the Plan type tiles and example Plan inputs values.](images/wfm-capacity-planning-create-plan.png) 4. Choose **Generate Capacity Plan**. 5. To quickly identify the plan that is in processing, choose
**Last Computed** to sort the table list. In the
following image, the status of the plan is **In
Progress**.

![The Capacity Plans table showing the Plan Type and Status columns, with Status set to In Progress.](images/wfm-capacity-planning-in-progress.png)

It usually takes between 5-10 minutes for the plan to be generated. If
the plan generation fails, check the forecasts for the selected forecast
group, and then generate the capacity plan again. For Hiring plans, try
publishing the selected long-term forecasts. For Scheduling plans,
confirm that a short-term forecast is published and that it covers the
plan date range.
